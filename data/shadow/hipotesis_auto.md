# Hipótesis automáticas — 2026-11-08 20:18 UTC
_Generado por shadow_postmortem.py sobre 1249913 resoluciones (PNL=+170021.64€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.5` → IC=-0.317 (n=195)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=697)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.198 (n=1011)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.505 (IC base=+0.128)

- **PATRÓN** `n_total_lado` > `62.0` → IC=+0.185 (n=322)

  - _Acción_: Kelly boost +0.93€ cuando `n_total_lado` > 62.0 (IC base=+0.128)

- **PATRÓN** `banda_hit_calibrado` > `0.6128` → IC=+0.241 (n=636)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6128 (IC base=+0.128)

- **PATRÓN** `banda_z` > `8.618` → IC=+0.201 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.618 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.146 (n=354)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.129 (n=685)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 12.0 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=1039)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.128)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.302 (n=165)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=497)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.196 (n=876)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.505 (IC base=+0.131)

- **PATRÓN** `n_total_lado` > `66.0` → IC=+0.186 (n=275)

  - _Acción_: Kelly boost +0.93€ cuando `n_total_lado` > 66.0 (IC base=+0.131)

- **PATRÓN** `banda_hit_calibrado` > `0.8128` → IC=+0.274 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8128 (IC base=+0.131)

- **PATRÓN** `banda_z` > `8.922` → IC=+0.206 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.922 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.151 (n=302)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.131)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=939)

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
- **FILTRO** `restante_s_al_confirmar` < `132.65` → IC=-0.223 (n=11633)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 132.65
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=34899)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `125.12` → IC=-0.259 (n=1193)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 125.12
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=3581)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `116.33` → IC=-0.290 (n=1207)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 116.33
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=3624)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `117.39` → IC=-0.166 (n=3166)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 117.39
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=9501)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `152.18` → IC=-0.249 (n=3163)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 152.18
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=9492)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `129.15` → IC=-0.263 (n=2192)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 129.15
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=6581)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.210 (n=27105)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `8363.8673` → IC=+0.159 (n=2294)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 8363.8673 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.128 (n=23128)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=28097)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.223 (n=21276)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=8175)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `6605.0986` → IC=+0.147 (n=3157)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 6605.0986 (IC base=+0.124)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.184 (n=2087)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 6.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` > `0.765` → IC=+0.364 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.765 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.181 (n=2679)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `9392.7207` → IC=+0.181 (n=1864)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 9392.7207 (IC base=+0.178)

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
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=2155)

- **PATRÓN** `py_entrada` > `0.61` → IC=+0.170 (n=591)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.61 (IC base=+0.076)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.144 (n=1384)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.44 (IC base=+0.082)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.168 (n=4900)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 6.0 (IC base=+0.165)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.169 (n=4365)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 15.0 (IC base=+0.165)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.376 (n=1672)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.212 (n=2337)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.331 (n=937)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=2716)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.144 (n=624)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 15.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.147 (n=1125)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 15.0 (IC base=+0.142)

- **PATRÓN** `py_entrada` > `0.675` → IC=+0.254 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.675 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.142 (n=1469)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.02 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.156 (n=155)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.074)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.255 (n=936)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.228)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.420 (n=1304)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.146 (n=1408)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 7.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.156 (n=724)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.145)

- **PATRÓN** `py_entrada` < `0.345` → IC=+0.278 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.345 (IC base=+0.145)

### FAVORITO_CONFIRMADO#SOL#60min
- **FILTRO** `libro_liquidez` < `951.9496` → IC=-0.127 (n=156)

  - _Acción_: SKIP cuando `libro_liquidez` < 951.9496
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=317)

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

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=23258)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.199 (n=19658)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 15.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.227 (n=9728)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `4915.142` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4915.142 (IC base=+0.197)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.176 (n=5302)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.173 (n=5288)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 18.0 (IC base=+0.173)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.181 (n=5328)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.74 (IC base=+0.173)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.173 (n=4463)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.214 (n=3103)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.216 (n=2062)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.211)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.253 (n=1563)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.211)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=5197)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.180 (n=4410)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.179 (n=5355)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.73 (IC base=+0.178)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.186 (n=4065)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.178)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.257 (n=4390)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.250)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.251 (n=3717)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.250)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.366 (n=1395)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.8 (IC base=+0.250)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.250)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=5107)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.190 (n=4331)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.186)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.192 (n=3802)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.186)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.429 (n=943)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.426)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.429 (n=838)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.426)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=955)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.426)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.432 (n=1000)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.426)

- **PATRÓN** `libro_liquidez` > `4484.2424` → IC=+0.444 (n=608)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4484.2424 (IC base=+0.426)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` < `11.0` → IC=+0.450 (n=258)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.457 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.440)

- **PATRÓN** `libro_liquidez` > `12295.9377` → IC=+0.446 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12295.9377 (IC base=+0.440)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.430 (n=372)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.425)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.428 (n=372)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.425)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.436 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=417)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.204 (n=30441)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.240 (n=30838)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.187 (n=4538)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 18.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.180 (n=9713)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 12.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.190 (n=13930)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.179)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=6321)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.287 (n=4345)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.182 (n=12784)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 7.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.198 (n=10799)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.72 (IC base=+0.180)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.227 (n=4260)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.224 (n=4858)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.268 (n=4281)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `hora_utc` > `3.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `libro_liquidez` < `3176.5987` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 3176.5987
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.212 (n=4327)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.257 (n=4470)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.202 (n=5062)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.199 (n=5030)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.244 (n=5309)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.192 (n=10943)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.139 (n=11364)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.49` → IC=+0.137 (n=13308)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.49 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=5326)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.143 (n=5122)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.126 (n=6663)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.62` → IC=+0.143 (n=5024)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 2.62 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.191 (n=5617)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.137 (n=6942)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.95 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `3.17` → IC=+0.137 (n=6684)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.17 (IC base=+0.116)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.306 (n=1355)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.386 (n=692)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.292)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.283 (n=911)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.279)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.365 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.279)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.319 (n=657)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.298)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.301 (n=962)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.298)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.393 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.298)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` < `16.0` → IC=+0.365 (n=94)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.343)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.390 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.343)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.375 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.343)

- **PATRÓN** `libro_liquidez` > `745.0217` → IC=+0.374 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 745.0217 (IC base=+0.343)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.447 (n=299)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.445 (n=889)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.440)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.440 (n=1068)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.440)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.435 (n=432)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.432)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.437 (n=299)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.432)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.431 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.432)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.432)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.466 (n=144)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.448)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.449 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.448)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.448 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.448)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.449 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.448)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4738` → IC=+0.139 (n=17152)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4738 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.127 (n=17357)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.127 (n=11926)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.978` → IC=+0.246 (n=5718)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.978 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.795` → IC=+0.284 (n=970)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.795 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.502` → IC=+0.184 (n=8574)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 3.502 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.6247` → IC=+0.265 (n=5102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6247 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.304` → IC=+0.249 (n=1769)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.304 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.7506` → IC=+0.235 (n=4104)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7506 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=8529)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `4652.5098` → IC=+0.147 (n=5717)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 4652.5098 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.122 (n=10704)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0061 (IC base=+0.081)

- **PATRÓN** `ibs_20min` < `0.5663` → IC=+0.143 (n=21391)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.5663 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` > `0.6096` → IC=+0.192 (n=1451)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.6096 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` < `0.1607` → IC=+0.190 (n=8436)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.1607 (IC base=+0.081)

- **PATRÓN** `volumen_regimen` < `0.6965` → IC=+0.195 (n=3825)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.6965 (IC base=+0.081)

- **PATRÓN** `volumen_pendiente_norm` > `0.2965` → IC=+0.228 (n=2144)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2965 (IC base=+0.081)

- **PATRÓN** `volumen_spike_ratio` > `2.6801` → IC=+0.210 (n=4922)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6801 (IC base=+0.081)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.227 (n=14685)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.081)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3626` → IC=+0.213 (n=3659)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3626 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.225 (n=1779)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.213 (n=2451)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.9868` → IC=+0.278 (n=1659)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9868 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.499` → IC=+0.278 (n=1625)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.499 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.2825` → IC=+0.266 (n=477)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2825 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.4349` → IC=+0.213 (n=3506)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4349 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.225 (n=4027)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2046.32` → IC=+0.212 (n=1220)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2046.32 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.226 (n=2253)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0102` → IC=+0.243 (n=3211)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0102 (IC base=+0.242)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.244 (n=1457)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0091 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.0891` → IC=+0.280 (n=1069)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0891 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.250 (n=1195)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.245 (n=1476)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.242)

- **PATRÓN** `ibs_20min` < `0.5616` → IC=+0.259 (n=3207)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5616 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` < `0.0944` → IC=+0.246 (n=2902)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0944 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` > `0.2882` → IC=+0.247 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2882 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` < `1.4451` → IC=+0.247 (n=1019)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4451 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` > `1.8555` → IC=+0.243 (n=2037)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8555 (IC base=+0.242)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.244 (n=3685)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.242)

- **PATRÓN** `libro_liquidez` > `1781.58` → IC=+0.247 (n=2137)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1781.58 (IC base=+0.242)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.230 (n=2695)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0055 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.0804` → IC=+0.262 (n=1020)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0804 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=3206)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.227 (n=2169)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.9081` → IC=+0.260 (n=1020)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9081 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.1838` → IC=+0.233 (n=1408)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1838 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` < `0.3319` → IC=+0.224 (n=3023)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3319 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.906` → IC=+0.262 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.906 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` < `1.2256` → IC=+0.224 (n=3060)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2256 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `0.6994` → IC=+0.230 (n=2733)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6994 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2788` → IC=+0.269 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2788 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.4415` → IC=+0.251 (n=1007)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4415 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.152 (n=3256)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0063 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.0761` → IC=+0.153 (n=1087)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.0761 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.151 (n=1213)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.3507` → IC=+0.198 (n=2171)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.3507 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.936` → IC=+0.137 (n=2974)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 3.936 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.6343` → IC=+0.148 (n=1086)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.6343 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.0715` → IC=+0.154 (n=1324)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.0715 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `2.4394` → IC=+0.139 (n=3130)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.4394 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.129 (n=4225)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `204.0` → IC=+0.171 (n=1365)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 204.0 (IC base=+0.129)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.213 (n=1761)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=4079)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.263 (n=1511)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.994` → IC=+0.280 (n=851)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.994 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` < `0.0977` → IC=+0.198 (n=3475)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.0977 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.3526` → IC=+0.222 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3526 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` > `2.7301` → IC=+0.214 (n=1718)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7301 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.201 (n=4694)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `1917.81` → IC=+0.204 (n=1759)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1917.81 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.225 (n=3140)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.2926` → IC=+0.231 (n=2378)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2926 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.242 (n=1352)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.221 (n=1616)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` < `0.0438` → IC=+0.270 (n=1189)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0438 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.875` → IC=+0.265 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.875 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.3488` → IC=+0.251 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3488 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` < `1.7679` → IC=+0.219 (n=1508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7679 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `2.1616` → IC=+0.227 (n=2285)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1616 (IC base=+0.219)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.225 (n=1807)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `1906.4295` → IC=+0.228 (n=1617)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1906.4295 (IC base=+0.219)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.222 (n=3391)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 25.0 (IC base=+0.219)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.160 (n=201)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=4663)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.157 (n=651)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0038 (IC base=+0.057)

- **PATRÓN** `ibs_20min` > `0.9435` → IC=+0.231 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9435 (IC base=+0.057)

- **PATRÓN** `dist_vwap_pct` > `0.1397` → IC=+0.340 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1397 (IC base=+0.057)

- **PATRÓN** `dist_vwap_pct` < `0.5418` → IC=+0.333 (n=806)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5418 (IC base=+0.057)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.077` → IC=+0.202 (n=1419)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.077 (IC base=+0.057)

- **PATRÓN** `volumen_regimen` > `0.7027` → IC=+0.340 (n=685)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7027 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` < `0.1669` → IC=+0.335 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1669 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.3024` → IC=+0.334 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3024 (IC base=+0.057)

- **PATRÓN** `volumen_spike_ratio` < `1.4207` → IC=+0.345 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4207 (IC base=+0.057)

- **PATRÓN** `volumen_spike_ratio` > `2.2799` → IC=+0.335 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2799 (IC base=+0.057)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.338 (n=756)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.057)

- **PATRÓN** `ibs_20min` < `0.0897` → IC=+0.187 (n=1217)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.0897 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` > `0.3333` → IC=+0.159 (n=597)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.3333 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` < `0.1384` → IC=+0.150 (n=2169)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1384 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` < `0.8322` → IC=+0.160 (n=1537)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8322 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.210 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` < `1.7755` → IC=+0.153 (n=1479)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.7755 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` > `2.1466` → IC=+0.158 (n=1006)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.1466 (IC base=+0.049)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.188 (n=139)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=738)

- **FILTRO** `ibs_20min` < `0.2615` → IC=-0.174 (n=219)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2615
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=658)

- **FILTRO** `ibs_20min` > `0.2` → IC=-0.133 (n=4587)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=2266)

- **FILTRO** `sigma_ewma_delta_pct` > `8.292` → IC=-0.225 (n=736)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.292
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=6117)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.179 (n=300)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.75 (IC base=+0.019)

- **PATRÓN** `dist_vwap_pct` > `0.9554` → IC=+0.278 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9554 (IC base=+0.019)

- **PATRÓN** `dist_vwap_pct` < `0.4558` → IC=+0.271 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4558 (IC base=+0.019)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.993` → IC=+0.160 (n=207)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 4.993 (IC base=+0.019)

- **PATRÓN** `volumen_regimen` > `0.6285` → IC=+0.285 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6285 (IC base=+0.019)

- **PATRÓN** `volumen_pendiente_norm` < `0.0791` → IC=+0.285 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0791 (IC base=+0.019)

- **PATRÓN** `volumen_spike_ratio` < `2.4693` → IC=+0.283 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4693 (IC base=+0.019)

- **PATRÓN** `volumen_spike_ratio` > `1.5401` → IC=+0.270 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5401 (IC base=+0.019)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.275 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.019)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.154 (n=2266)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.2 (IC base=-0.038)

- **PATRÓN** `dist_vwap_pct` > `0.219` → IC=+0.286 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.219 (IC base=-0.038)

- **PATRÓN** `volumen_regimen` < `0.7017` → IC=+0.302 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7017 (IC base=-0.038)

- **PATRÓN** `volumen_pendiente_norm` > `0.0793` → IC=+0.301 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0793 (IC base=-0.038)

- **PATRÓN** `volumen_spike_ratio` < `2.4773` → IC=+0.300 (n=935)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4773 (IC base=-0.038)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7818` → IC=-0.153 (n=3474)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7818
  - _Potencial_: sin este filtro IC_bueno=+0.123 (n=1791)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.170 (n=1155)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=4110)

- **FILTRO** `ibs_20min` > `0.7423` → IC=-0.194 (n=1830)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7423
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=5493)

- **PATRÓN** `ibs_20min` > `0.7818` → IC=+0.123 (n=1791)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` > 0.7818 (IC base=-0.059)

- **PATRÓN** `dist_vwap_pct` > `1.0084` → IC=+0.361 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0084 (IC base=-0.059)

- **PATRÓN** `dist_vwap_pct` < `0.2486` → IC=+0.303 (n=896)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2486 (IC base=-0.059)

- **PATRÓN** `volumen_regimen` > `0.7043` → IC=+0.318 (n=903)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7043 (IC base=-0.059)

- **PATRÓN** `volumen_pendiente_norm` < `0.1078` → IC=+0.305 (n=961)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1078 (IC base=-0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.1692` → IC=+0.302 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1692 (IC base=-0.059)

- **PATRÓN** `volumen_spike_ratio` < `1.5875` → IC=+0.307 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5875 (IC base=-0.059)

- **PATRÓN** `volumen_spike_ratio` > `2.5309` → IC=+0.325 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5309 (IC base=-0.059)

- **PATRÓN** `dist_vwap_pct` > `0.806` → IC=+0.276 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.806 (IC base=+0.002)

- **PATRÓN** `dist_vwap_pct` < `0.2214` → IC=+0.263 (n=2107)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2214 (IC base=+0.002)

- **PATRÓN** `volumen_regimen` < `0.6409` → IC=+0.271 (n=709)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6409 (IC base=+0.002)

- **PATRÓN** `volumen_regimen` > `1.0638` → IC=+0.284 (n=964)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0638 (IC base=+0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.1067` → IC=+0.281 (n=760)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1067 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` < `2.1776` → IC=+0.266 (n=1761)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1776 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` > `1.4426` → IC=+0.269 (n=2001)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4426 (IC base=+0.002)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.198 (n=7418)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0106 (IC base=+0.088)

- **PATRÓN** `ibs_20min` > `0.8696` → IC=+0.287 (n=10075)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8696 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.9379` → IC=+0.301 (n=1595)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9379 (IC base=+0.088)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.481` → IC=+0.168 (n=9940)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.481 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` > `0.693` → IC=+0.276 (n=7285)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.693 (IC base=+0.088)

- **PATRÓN** `volumen_pendiente_norm` > `0.2943` → IC=+0.292 (n=1846)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2943 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` > `2.6561` → IC=+0.286 (n=4296)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6561 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.308 (n=12505)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.088)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.158 (n=7147)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0101 (IC base=+0.081)

- **PATRÓN** `ibs_20min` < `0.6416` → IC=+0.154 (n=21398)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.6416 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` < `0.2545` → IC=+0.278 (n=7205)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2545 (IC base=+0.081)

- **PATRÓN** `volumen_regimen` < `0.6996` → IC=+0.280 (n=3095)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6996 (IC base=+0.081)

- **PATRÓN** `volumen_regimen` > `1.1918` → IC=+0.279 (n=2347)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1918 (IC base=+0.081)

- **PATRÓN** `volumen_pendiente_norm` > `0.2946` → IC=+0.324 (n=1568)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2946 (IC base=+0.081)

- **PATRÓN** `volumen_spike_ratio` < `1.4543` → IC=+0.304 (n=3455)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4543 (IC base=+0.081)

- **PATRÓN** `volumen_spike_ratio` > `2.283` → IC=+0.300 (n=4697)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.283 (IC base=+0.081)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.309 (n=10335)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 73.0 (IC base=+0.081)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8012` → IC=-0.126 (n=3954)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8012
  - _Potencial_: sin este filtro IC_bueno=+0.297 (n=2038)

- **FILTRO** `ibs_20min` > `0.7197` → IC=-0.234 (n=1312)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7197
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=3944)

- **FILTRO** `sigma_ewma_delta_pct` > `4.118` → IC=-0.231 (n=1132)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.118
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=4124)

- **PATRÓN** `ibs_20min` > `0.9348` → IC=+0.337 (n=1498)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9348 (IC base=+0.018)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.983` → IC=+0.189 (n=2002)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 2.983 (IC base=+0.018)

- **PATRÓN** `volumen_pendiente_norm` > `0.2287` → IC=+0.327 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2287 (IC base=+0.018)

- **PATRÓN** `volumen_spike_ratio` < `1.4469` → IC=+0.279 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4469 (IC base=+0.018)

- **PATRÓN** `volumen_spike_ratio` > `2.2395` → IC=+0.302 (n=870)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2395 (IC base=+0.018)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.316 (n=1300)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.018)

- **PATRÓN** `ibs_20min` < `0.1728` → IC=+0.164 (n=1315)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.1728 (IC base=-0.025)

- **PATRÓN** `volumen_pendiente_norm` < `0.1514` → IC=+0.401 (n=978)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1514 (IC base=-0.025)

- **PATRÓN** `volumen_spike_ratio` < `1.4194` → IC=+0.424 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4194 (IC base=-0.025)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.398 (n=974)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=-0.025)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.2967` → IC=+0.224 (n=731)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2967 (IC base=+0.012)

- **PATRÓN** `volumen_regimen` < `1.1951` → IC=+0.209 (n=2172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1951 (IC base=+0.012)

- **PATRÓN** `volumen_regimen` > `0.6949` → IC=+0.215 (n=1940)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6949 (IC base=+0.012)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.243 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=+0.012)

- **PATRÓN** `volumen_spike_ratio` < `1.4174` → IC=+0.232 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4174 (IC base=+0.012)

- **PATRÓN** `ballena_activa_n` < `263.0` → IC=+0.245 (n=1429)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 263.0 (IC base=+0.012)

- **PATRÓN** `dist_vwap_pct` < `0.1296` → IC=+0.255 (n=1538)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1296 (IC base=-0.004)

- **PATRÓN** `volumen_regimen` > `0.6188` → IC=+0.251 (n=1501)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6188 (IC base=-0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2697` → IC=+0.305 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2697 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` < `1.5262` → IC=+0.255 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5262 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` > `2.1487` → IC=+0.260 (n=657)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1487 (IC base=-0.004)

- **PATRÓN** `ballena_activa_n` < `212.0` → IC=+0.269 (n=642)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 212.0 (IC base=-0.004)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.319 (n=2089)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.283)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.291 (n=3135)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.283)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.324 (n=1709)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.59` → IC=+0.305 (n=2091)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.59 (IC base=+0.283)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.296 (n=2749)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.283)

- **PATRÓN** `volumen_spike_ratio` > `1.6063` → IC=+0.290 (n=3041)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6063 (IC base=+0.283)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.293 (n=3756)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `2026.8956` → IC=+0.296 (n=1044)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2026.8956 (IC base=+0.283)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.309 (n=1902)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.283)

- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.324 (n=2526)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0074 (IC base=+0.305)

- **PATRÓN** `drift_60min` |x|≤ `0.1771` → IC=+0.324 (n=1244)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1771 (IC base=+0.305)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.327 (n=1084)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.305)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.307 (n=1276)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.305)

- **PATRÓN** `ibs_20min` > `0.1429` → IC=+0.316 (n=1888)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1429 (IC base=+0.305)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.171` → IC=+0.312 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.171 (IC base=+0.305)

- **PATRÓN** `volumen_pendiente_norm` < `0.1999` → IC=+0.306 (n=2778)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1999 (IC base=+0.305)

- **PATRÓN** `volumen_pendiente_norm` > `0.3455` → IC=+0.311 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3455 (IC base=+0.305)

- **PATRÓN** `volumen_spike_ratio` < `1.595` → IC=+0.307 (n=909)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.595 (IC base=+0.305)

- **PATRÓN** `volumen_spike_ratio` > `2.7408` → IC=+0.320 (n=1235)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7408 (IC base=+0.305)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.308 (n=1437)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.305)

- **PATRÓN** `libro_liquidez` > `1910.02` → IC=+0.315 (n=1281)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1910.02 (IC base=+0.305)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.312 (n=2365)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.305)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7265` → IC=-0.182 (n=1394)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7265
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=4185)

- **PATRÓN** `ibs_20min` > `0.8479` → IC=+0.160 (n=1368)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.8479 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` > `0.1419` → IC=+0.234 (n=1021)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1419 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` < `0.3574` → IC=+0.235 (n=1936)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3574 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` < `1.1628` → IC=+0.234 (n=1972)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1628 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` > `0.6735` → IC=+0.231 (n=1761)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6735 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` < `0.1628` → IC=+0.235 (n=2070)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1628 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.0761` → IC=+0.237 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0761 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` < `2.4616` → IC=+0.239 (n=1911)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4616 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` > `1.5077` → IC=+0.233 (n=1707)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5077 (IC base=+0.022)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.254 (n=1953)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` < `0.3477` → IC=+0.251 (n=1570)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3477 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` < `1.193` → IC=+0.255 (n=1415)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.193 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2817` → IC=+0.309 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2817 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.5218` → IC=+0.295 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5218 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` > `2.426` → IC=+0.276 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.426 (IC base=+0.005)

- **PATRÓN** `ballena_activa_n` < `99.0` → IC=+0.281 (n=1216)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 99.0 (IC base=+0.005)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7407` → IC=-0.246 (n=2297)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7407
  - _Potencial_: sin este filtro IC_bueno=+0.312 (n=2303)

- **FILTRO** `ibs_20min` > `0.6216` → IC=-0.229 (n=1092)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6216
  - _Potencial_: sin este filtro IC_bueno=+0.149 (n=3279)

- **FILTRO** `sigma_ewma_delta_pct` > `8.272` → IC=-0.253 (n=499)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.272
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=3872)

- **PATRÓN** `ibs_20min` > `0.7407` → IC=+0.312 (n=2303)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7407 (IC base=+0.033)

- **PATRÓN** `dist_vwap_pct` > `1.043` → IC=+0.356 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.043 (IC base=+0.033)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.444` → IC=+0.153 (n=1862)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 2.444 (IC base=+0.033)

- **PATRÓN** `volumen_regimen` < `0.8458` → IC=+0.341 (n=1117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8458 (IC base=+0.033)

- **PATRÓN** `volumen_regimen` > `0.6986` → IC=+0.335 (n=1497)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6986 (IC base=+0.033)

- **PATRÓN** `volumen_pendiente_norm` < `0.1567` → IC=+0.335 (n=1731)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1567 (IC base=+0.033)

- **PATRÓN** `volumen_pendiente_norm` > `0.2747` → IC=+0.362 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2747 (IC base=+0.033)

- **PATRÓN** `volumen_spike_ratio` < `1.4306` → IC=+0.362 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4306 (IC base=+0.033)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.352 (n=1110)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.033)

- **PATRÓN** `ibs_20min` < `0.6216` → IC=+0.149 (n=3279)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.6216 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` > `0.7696` → IC=+0.258 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7696 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` < `0.3042` → IC=+0.260 (n=1659)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3042 (IC base=+0.054)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.024` → IC=+0.129 (n=3081)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 3.024 (IC base=+0.054)

- **PATRÓN** `volumen_regimen` < `0.6945` → IC=+0.281 (n=716)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6945 (IC base=+0.054)

- **PATRÓN** `volumen_pendiente_norm` > `0.0706` → IC=+0.282 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0706 (IC base=+0.054)

- **PATRÓN** `volumen_spike_ratio` < `1.808` → IC=+0.276 (n=1049)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.808 (IC base=+0.054)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.280 (n=1411)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.054)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.359 (n=2090)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.316)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.318 (n=2365)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.316)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.317 (n=1108)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.316)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.344 (n=2339)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.316)

- **PATRÓN** `dist_vwap_pct` > `0.2108` → IC=+0.339 (n=1283)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2108 (IC base=+0.316)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.802` → IC=+0.334 (n=1127)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.802 (IC base=+0.316)

- **PATRÓN** `volumen_regimen` > `0.8706` → IC=+0.335 (n=1558)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8706 (IC base=+0.316)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.347 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.316)

- **PATRÓN** `volumen_spike_ratio` > `1.4314` → IC=+0.327 (n=2250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4314 (IC base=+0.316)

- **PATRÓN** `libro_liquidez` > `2978.1339` → IC=+0.327 (n=779)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2978.1339 (IC base=+0.316)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.344 (n=1855)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.316)

- **PATRÓN** `sigma_h` > `0.0153` → IC=+0.349 (n=1662)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0153 (IC base=+0.317)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.324 (n=1268)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.317)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.317 (n=1206)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.317)

- **PATRÓN** `ibs_20min` < `0.38` → IC=+0.335 (n=2495)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.38 (IC base=+0.317)

- **PATRÓN** `dist_vwap_pct` < `0.2414` → IC=+0.322 (n=2421)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2414 (IC base=+0.317)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.628` → IC=+0.329 (n=929)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.628 (IC base=+0.317)

- **PATRÓN** `volumen_regimen` < `0.7185` → IC=+0.321 (n=1097)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7185 (IC base=+0.317)

- **PATRÓN** `volumen_regimen` > `1.213` → IC=+0.346 (n=831)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.213 (IC base=+0.317)

- **PATRÓN** `volumen_pendiente_norm` > `0.2306` → IC=+0.363 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2306 (IC base=+0.317)

- **PATRÓN** `volumen_spike_ratio` < `1.412` → IC=+0.325 (n=771)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.412 (IC base=+0.317)

- **PATRÓN** `volumen_spike_ratio` > `2.1376` → IC=+0.317 (n=1048)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1376 (IC base=+0.317)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.224 (n=5541)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0124 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.1216` → IC=+0.191 (n=7301)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1216 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=17219)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `0.5393` → IC=+0.231 (n=16589)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5393 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` > `0.161` → IC=+0.205 (n=6382)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.161 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.805` → IC=+0.257 (n=3226)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.805 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` < `1.1825` → IC=+0.154 (n=11039)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.1825 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` > `0.6258` → IC=+0.153 (n=11040)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.6258 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.2944` → IC=+0.204 (n=2410)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2944 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `2.6104` → IC=+0.189 (n=5377)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6104 (IC base=+0.174)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.193 (n=15534)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 88.0 (IC base=+0.174)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.191 (n=7162)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0058 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.0799` → IC=+0.220 (n=5417)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0799 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.210 (n=6137)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.5244` → IC=+0.239 (n=16246)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5244 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` < `0.1805` → IC=+0.176 (n=11760)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1805 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.557` → IC=+0.191 (n=2589)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 9.557 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.519` → IC=+0.189 (n=14460)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 2.519 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `1.1817` → IC=+0.163 (n=11574)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1817 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2939` → IC=+0.216 (n=2432)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2939 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` < `1.56` → IC=+0.181 (n=6796)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.56 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.635` → IC=+0.191 (n=5148)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.635 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.202 (n=13437)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 59.0 (IC base=+0.182)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.228 (n=912)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.228)

- **PATRÓN** `drift_60min` |x|≤ `0.1044` → IC=+0.258 (n=1202)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1044 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=2845)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.228)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.230 (n=1854)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` > `0.9423` → IC=+0.298 (n=1821)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9423 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.521` → IC=+0.331 (n=886)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.521 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.295 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` < `1.8322` → IC=+0.224 (n=1736)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8322 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `1.4336` → IC=+0.228 (n=2605)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4336 (IC base=+0.228)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.238 (n=3030)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.228)

- **PATRÓN** `sigma_h` < `0.0096` → IC=+0.257 (n=2206)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0096 (IC base=+0.255)

- **PATRÓN** `sigma_h` > `0.0087` → IC=+0.256 (n=1000)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0087 (IC base=+0.255)

- **PATRÓN** `drift_60min` |x|≤ `0.097` → IC=+0.311 (n=971)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.097 (IC base=+0.255)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.260 (n=2277)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.255)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.258 (n=2009)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.255)

- **PATRÓN** `ibs_20min` < `0.0497` → IC=+0.300 (n=970)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0497 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` < `0.0993` → IC=+0.258 (n=1935)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0993 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` > `0.3015` → IC=+0.270 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3015 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` < `1.4457` → IC=+0.276 (n=703)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4457 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` > `2.6989` → IC=+0.257 (n=703)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6989 (IC base=+0.255)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.259 (n=2543)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `1783.3979` → IC=+0.262 (n=1470)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1783.3979 (IC base=+0.255)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.254 (n=1869)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.255)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.199 (n=849)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.0644` → IC=+0.180 (n=842)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.0644 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=2645)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` > `0.2641` → IC=+0.209 (n=2524)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2641 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` > `0.1829` → IC=+0.212 (n=1276)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1829 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.711` → IC=+0.207 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.711 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `0.6953` → IC=+0.139 (n=1111)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.6953 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` > `1.058` → IC=+0.136 (n=1145)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 1.058 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.174 (n=394)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` < `1.5043` → IC=+0.140 (n=1091)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.5043 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `2.4691` → IC=+0.148 (n=827)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 2.4691 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `401.0` → IC=+0.136 (n=2448)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 401.0 (IC base=+0.131)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.173 (n=2671)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0064 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.301` → IC=+0.164 (n=2671)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.301 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.180 (n=1278)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` < `0.6089` → IC=+0.207 (n=2671)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6089 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.871` → IC=+0.176 (n=501)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 10.871 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.979` → IC=+0.151 (n=2330)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 3.979 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `1.2004` → IC=+0.159 (n=2671)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.2004 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` < `0.0937` → IC=+0.148 (n=2311)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.0937 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.4631` → IC=+0.151 (n=2547)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4631 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `212.0` → IC=+0.186 (n=1097)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 212.0 (IC base=+0.146)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.233 (n=1281)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.2466` → IC=+0.233 (n=1880)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2466 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.233 (n=1024)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.293 (n=1496)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.089` → IC=+0.303 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.089 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` < `0.0992` → IC=+0.211 (n=2449)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0992 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.3534` → IC=+0.234 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3534 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.7154` → IC=+0.226 (n=1247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7154 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.216 (n=3407)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `1913.32` → IC=+0.223 (n=1278)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1913.32 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0107` → IC=+0.248 (n=2173)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0107 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.4117` → IC=+0.260 (n=2172)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4117 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.280 (n=948)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.0364` → IC=+0.289 (n=1086)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0364 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.034` → IC=+0.280 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.034 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.3581` → IC=+0.283 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3581 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.7757` → IC=+0.240 (n=1048)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7757 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `2.189` → IC=+0.249 (n=1587)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.189 (IC base=+0.238)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.238 (n=1266)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `1899.6204` → IC=+0.250 (n=1119)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1899.6204 (IC base=+0.238)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.242 (n=1594)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.238)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.207 (n=909)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.0775` → IC=+0.183 (n=910)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.0775 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.140 (n=2822)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` > `0.2536` → IC=+0.192 (n=2725)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.2536 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` > `0.1379` → IC=+0.186 (n=1585)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1379 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.277` → IC=+0.199 (n=469)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 11.277 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.8447` → IC=+0.137 (n=1818)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8447 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.2887` → IC=+0.172 (n=412)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2887 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `1.8246` → IC=+0.129 (n=1779)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.8246 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `2.5215` → IC=+0.148 (n=890)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 2.5215 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `6814.3405` → IC=+0.197 (n=1235)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 6814.3405 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `128.0` → IC=+0.134 (n=2671)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 128.0 (IC base=+0.130)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.164 (n=2554)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0066 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.3915` → IC=+0.144 (n=2900)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3915 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.164 (n=1395)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.6746` → IC=+0.185 (n=2900)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6746 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` < `0.1591` → IC=+0.156 (n=2925)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1591 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.266` → IC=+0.140 (n=693)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 9.266 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.8509` → IC=+0.150 (n=1934)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8509 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2948` → IC=+0.177 (n=431)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2948 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.8021` → IC=+0.131 (n=1832)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.8021 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `2.5328` → IC=+0.131 (n=916)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.5328 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `6239.7898` → IC=+0.189 (n=1315)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 6239.7898 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.148 (n=918)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 49.0 (IC base=+0.128)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.168 (n=1382)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0112 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.159 (n=1449)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 15.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.4722` → IC=+0.206 (n=3043)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4722 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `0.1947` → IC=+0.188 (n=1662)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1947 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.014` → IC=+0.289 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.014 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `1.1741` → IC=+0.132 (n=3042)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.1741 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` > `0.704` → IC=+0.122 (n=2717)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` > 0.704 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` < `0.163` → IC=+0.127 (n=3098)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.163 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `1.4374` → IC=+0.132 (n=985)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.4374 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.122 (n=3182)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2981.4431` → IC=+0.206 (n=1014)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2981.4431 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.144 (n=1303)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 20.0 (IC base=+0.121)

- **PATRÓN** `sigma_h` < `0.0118` → IC=+0.140 (n=3176)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0118 (IC base=+0.117)

- **PATRÓN** `drift_60min` |x|≤ `0.1109` → IC=+0.161 (n=1059)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1109 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.132 (n=3248)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.6522` → IC=+0.218 (n=3178)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6522 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` < `0.2118` → IC=+0.141 (n=3105)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.2118 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.257` → IC=+0.137 (n=2807)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 2.257 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `1.1734` → IC=+0.125 (n=3176)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.1734 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.2745` → IC=+0.140 (n=437)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.2745 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `1.4336` → IC=+0.131 (n=1000)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.4336 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2536.5467` → IC=+0.182 (n=1440)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2536.5467 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.122 (n=1977)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 27.0 (IC base=+0.117)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0131` → IC=+0.248 (n=2458)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0131 (IC base=+0.225)

- **PATRÓN** `drift_60min` |x|≤ `0.1667` → IC=+0.238 (n=1211)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1667 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.229 (n=2858)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=2480)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.256 (n=2753)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` > `0.1805` → IC=+0.234 (n=1709)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1805 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.58` → IC=+0.255 (n=1236)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.58 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` > `0.6235` → IC=+0.234 (n=2750)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6235 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.2353` → IC=+0.267 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2353 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` < `2.4732` → IC=+0.228 (n=2682)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4732 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `1.8165` → IC=+0.231 (n=1788)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8165 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `2840.3304` → IC=+0.230 (n=1247)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2840.3304 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.0129` → IC=+0.241 (n=1247)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0129 (IC base=+0.240)

- **PATRÓN** `sigma_h` > `0.0229` → IC=+0.250 (n=1282)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0229 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.5706` → IC=+0.248 (n=2828)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5706 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.252 (n=1395)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.246 (n=1260)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.44` → IC=+0.264 (n=2836)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.44 (IC base=+0.240)

- **PATRÓN** `dist_vwap_pct` > `1.1245` → IC=+0.255 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1245 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.033` → IC=+0.266 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.033 (IC base=+0.240)

- **PATRÓN** `volumen_regimen` < `0.8636` → IC=+0.245 (n=1886)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8636 (IC base=+0.240)

- **PATRÓN** `volumen_regimen` > `0.6399` → IC=+0.243 (n=2828)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6399 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.292 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `2.527` → IC=+0.237 (n=2663)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.527 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `1.436` → IC=+0.240 (n=2663)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.436 (IC base=+0.240)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.208 (n=1428)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.162)

- **PATRÓN** `drift_60min` |x|≤ `0.1323` → IC=+0.176 (n=1878)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.1323 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.174 (n=4475)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` > `0.31` → IC=+0.198 (n=4268)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.31 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` > `0.817` → IC=+0.189 (n=677)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.817 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.628` → IC=+0.211 (n=697)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.628 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` < `0.8616` → IC=+0.172 (n=2595)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.8616 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` > `1.1929` → IC=+0.171 (n=1297)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 1.1929 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` > `0.098` → IC=+0.173 (n=1526)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.098 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` < `1.5292` → IC=+0.167 (n=1830)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.5292 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` > `1.8117` → IC=+0.164 (n=2772)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.8117 (IC base=+0.162)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.163 (n=4780)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.02 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `7981.3983` → IC=+0.185 (n=1935)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 7981.3983 (IC base=+0.162)

- **PATRÓN** `ibs_20min` < `0.386` → IC=+0.170 (n=3077)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.386 (IC base=+0.092)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.135 (n=1989)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 25.0 (IC base=+0.092)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.196 (n=1128)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0061 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.3283` → IC=+0.198 (n=1126)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.3283 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.213 (n=1017)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.6075` → IC=+0.236 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6075 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.3086` → IC=+0.213 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3086 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.956` → IC=+0.206 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.956 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.8803` → IC=+0.193 (n=753)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.8803 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.0703` → IC=+0.192 (n=443)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.0703 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` < `2.1671` → IC=+0.195 (n=971)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.1671 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `15815.8495` → IC=+0.191 (n=510)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 15815.8495 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.162 (n=465)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0031 (IC base=+0.088)

- **PATRÓN** `ibs_20min` < `0.1986` → IC=+0.202 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1986 (IC base=+0.088)

- **PATRÓN** `volumen_pendiente_norm` > `0.1609` → IC=+0.134 (n=364)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.1609 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `162.0` → IC=+0.179 (n=599)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 162.0 (IC base=+0.088)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.237 (n=583)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.2084` → IC=+0.167 (n=883)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.2084 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.182 (n=1378)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `0.8019` → IC=+0.263 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8019 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.8169` → IC=+0.190 (n=224)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.8169 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.864` → IC=+0.214 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.864 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `0.8304` → IC=+0.175 (n=883)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.8304 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` > `1.1537` → IC=+0.164 (n=442)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 1.1537 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.2192` → IC=+0.208 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2192 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` > `2.4761` → IC=+0.185 (n=436)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.4761 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `8223.8718` → IC=+0.172 (n=601)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 8223.8718 (IC base=+0.164)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.120 (n=862)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.0052 (IC base=+0.084)

- **PATRÓN** `ibs_20min` < `0.0884` → IC=+0.198 (n=431)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.0884 (IC base=+0.084)

- **PATRÓN** `libro_liquidez` > `5151.7169` → IC=+0.134 (n=862)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 5151.7169 (IC base=+0.084)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.124 (n=549)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 42.0 (IC base=+0.084)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.143 (n=948)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0106 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.172 (n=758)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 11.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` > `0.4571` → IC=+0.185 (n=1078)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.4571 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` > `0.9339` → IC=+0.183 (n=184)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.9339 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.848` → IC=+0.231 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.848 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `1.0478` → IC=+0.139 (n=947)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.0478 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` > `0.7037` → IC=+0.142 (n=962)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.7037 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.2259` → IC=+0.160 (n=195)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.2259 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` < `2.4017` → IC=+0.135 (n=1040)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.4017 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `1.8035` → IC=+0.132 (n=693)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 1.8035 (IC base=+0.131)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.134 (n=1130)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.02 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `2725.2893` → IC=+0.167 (n=488)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2725.2893 (IC base=+0.131)

- **PATRÓN** `ibs_20min` < `0.3684` → IC=+0.180 (n=789)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.3684 (IC base=+0.065)

- **PATRÓN** `libro_liquidez` > `2866.3451` → IC=+0.162 (n=394)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2866.3451 (IC base=+0.065)

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

- **PATRÓN** `sigma_h` > `0.0242` → IC=+0.183 (n=181)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0242 (IC base=+0.144)

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
- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.230 (n=7243)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0124 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=22657)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.4312` → IC=+0.228 (n=21709)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4312 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.879` → IC=+0.212 (n=2616)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.879 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.951` → IC=+0.255 (n=5312)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.951 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `1.2159` → IC=+0.159 (n=14615)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2159 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2415` → IC=+0.207 (n=3905)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2415 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.622` → IC=+0.194 (n=7063)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.622 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `103.0` → IC=+0.202 (n=20333)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 103.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.198 (n=8767)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.006 (IC base=+0.193)

- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.203 (n=6633)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.4792` → IC=+0.197 (n=19901)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.4792 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=7439)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` < `0.5918` → IC=+0.243 (n=19909)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5918 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` < `0.1776` → IC=+0.175 (n=12503)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1776 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.419` → IC=+0.195 (n=2692)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 9.419 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.378` → IC=+0.199 (n=19388)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 3.378 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` < `0.7025` → IC=+0.174 (n=5882)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.7025 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.2927` → IC=+0.250 (n=2739)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2927 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.6308` → IC=+0.204 (n=6342)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6308 (IC base=+0.193)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.209 (n=18818)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 92.0 (IC base=+0.193)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.251 (n=1686)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.236 (n=2339)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` > `0.8656` → IC=+0.302 (n=2316)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8656 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.534` → IC=+0.335 (n=1132)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.534 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.2321` → IC=+0.300 (n=623)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2321 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.2842` → IC=+0.242 (n=1521)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2842 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.251 (n=3810)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `2045.8902` → IC=+0.237 (n=1158)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2045.8902 (IC base=+0.236)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.254 (n=2198)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.236)

- **PATRÓN** `sigma_h` < `0.0101` → IC=+0.270 (n=3084)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0101 (IC base=+0.267)

- **PATRÓN** `drift_60min` |x|≤ `0.1214` → IC=+0.294 (n=1357)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1214 (IC base=+0.267)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.270 (n=2848)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.267)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.269 (n=2792)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.267)

- **PATRÓN** `ibs_20min` < `0.5449` → IC=+0.285 (n=3083)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5449 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` < `0.0974` → IC=+0.271 (n=2803)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0974 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` > `0.289` → IC=+0.281 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.289 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` < `1.5591` → IC=+0.270 (n=1300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5591 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` > `2.6471` → IC=+0.276 (n=985)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6471 (IC base=+0.267)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.269 (n=3547)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.267)

- **PATRÓN** `libro_liquidez` > `1781.3992` → IC=+0.274 (n=2055)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1781.3992 (IC base=+0.267)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.276 (n=1061)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.267)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.179 (n=1188)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0031 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.0781` → IC=+0.150 (n=1184)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.0781 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.147 (n=3703)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.1994` → IC=+0.189 (n=3549)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.1994 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.3177` → IC=+0.201 (n=1175)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3177 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.329` → IC=+0.160 (n=743)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 9.329 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.6348` → IC=+0.155 (n=1184)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6348 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `1.0681` → IC=+0.141 (n=1610)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 1.0681 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2716` → IC=+0.178 (n=504)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2716 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.1664` → IC=+0.141 (n=3066)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.1664 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.5184` → IC=+0.141 (n=3112)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.5184 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `303.0` → IC=+0.151 (n=2289)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 303.0 (IC base=+0.137)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.162 (n=3043)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0063 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.3218` → IC=+0.146 (n=3040)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3218 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.166 (n=1116)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.6799` → IC=+0.185 (n=3040)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6799 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.975` → IC=+0.139 (n=2748)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 3.975 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.0497` → IC=+0.149 (n=2675)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.0497 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2196` → IC=+0.194 (n=564)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2196 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.4295` → IC=+0.142 (n=2930)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.4295 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.7707` → IC=+0.141 (n=1953)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.7707 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=3948)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `226.0` → IC=+0.154 (n=955)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 226.0 (IC base=+0.137)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.244 (n=2420)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.236 (n=3796)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.228)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.229 (n=3239)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=1359)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.01` → IC=+0.324 (n=806)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.01 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` < `0.132` → IC=+0.229 (n=3424)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.132 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `2.7388` → IC=+0.243 (n=1605)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7388 (IC base=+0.228)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.234 (n=4371)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.228)

- **PATRÓN** `libro_liquidez` > `1917.74` → IC=+0.239 (n=1642)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1917.74 (IC base=+0.228)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.249 (n=3036)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0109 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.1771` → IC=+0.265 (n=1518)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1771 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.263 (n=1312)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.243)

- **PATRÓN** `ibs_20min` < `0.0588` → IC=+0.303 (n=1153)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0588 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.108` → IC=+0.301 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.108 (IC base=+0.243)

- **PATRÓN** `volumen_pendiente_norm` > `0.349` → IC=+0.302 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.349 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` > `2.177` → IC=+0.253 (n=2213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.177 (IC base=+0.243)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.251 (n=1762)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.243)

- **PATRÓN** `libro_liquidez` > `2006.1448` → IC=+0.254 (n=1150)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2006.1448 (IC base=+0.243)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.253 (n=2253)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.243)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.195 (n=1255)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0037 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.4286` → IC=+0.144 (n=3756)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.4286 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.148 (n=3901)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.8896` → IC=+0.273 (n=1252)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8896 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.1935` → IC=+0.167 (n=1714)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1935 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.948` → IC=+0.155 (n=1668)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 2.948 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.86` → IC=+0.149 (n=2504)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.86 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2332` → IC=+0.185 (n=669)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2332 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.52` → IC=+0.150 (n=1616)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.52 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `2.1813` → IC=+0.144 (n=1665)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.1813 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `5516.0856` → IC=+0.226 (n=1703)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5516.0856 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.143 (n=2423)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 88.0 (IC base=+0.137)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.169 (n=2769)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0067 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.4329` → IC=+0.154 (n=3139)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4329 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=1156)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` < `0.5771` → IC=+0.210 (n=2763)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5771 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` < `0.1516` → IC=+0.158 (n=2931)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1516 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.832` → IC=+0.153 (n=462)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 10.832 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.044` → IC=+0.147 (n=2738)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 3.044 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `0.6895` → IC=+0.159 (n=1382)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.6895 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.2929` → IC=+0.209 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2929 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `2.2086` → IC=+0.146 (n=2666)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.2086 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `1.5334` → IC=+0.151 (n=2707)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.5334 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `6325.8714` → IC=+0.217 (n=1047)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6325.8714 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.156 (n=2073)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 92.0 (IC base=+0.143)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.150 (n=1729)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0112 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.148 (n=2697)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 11.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.4286` → IC=+0.189 (n=3826)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4286 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `1.0027` → IC=+0.201 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0027 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.245` → IC=+0.268 (n=968)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.245 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.8768` → IC=+0.131 (n=2541)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 0.8768 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` < `0.1016` → IC=+0.120 (n=3613)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_pendiente_norm` < 0.1016 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `2.4921` → IC=+0.120 (n=3723)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_spike_ratio` < 2.4921 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2709.074` → IC=+0.240 (n=1270)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2709.074 (IC base=+0.117)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.152 (n=3155)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0108 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.1362` → IC=+0.153 (n=1196)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1362 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.161 (n=1687)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 15.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.6667` → IC=+0.214 (n=3600)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6667 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` < `0.2159` → IC=+0.140 (n=3241)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.2159 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.03` → IC=+0.148 (n=3472)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 3.03 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `0.6383` → IC=+0.150 (n=1197)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6383 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2271` → IC=+0.178 (n=626)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2271 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.4357` → IC=+0.157 (n=1134)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.4357 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2607.8221` → IC=+0.207 (n=1195)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2607.8221 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.137 (n=3059)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 43.0 (IC base=+0.125)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0139` → IC=+0.260 (n=3127)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0139 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.243 (n=3662)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.243 (n=2334)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` > `0.615` → IC=+0.271 (n=3127)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.615 (IC base=+0.237)

- **PATRÓN** `dist_vwap_pct` > `0.1935` → IC=+0.252 (n=1825)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1935 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.208` → IC=+0.285 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.208 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` < `1.2177` → IC=+0.239 (n=3499)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2177 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` > `0.6434` → IC=+0.242 (n=3500)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6434 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2391` → IC=+0.254 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2391 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.5041` → IC=+0.257 (n=1140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5041 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `2968.8332` → IC=+0.242 (n=1167)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2968.8332 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0259` → IC=+0.270 (n=1202)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0259 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.6238` → IC=+0.243 (n=3604)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6238 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.247 (n=3402)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.243)

- **PATRÓN** `ibs_20min` < `0.5208` → IC=+0.273 (n=3605)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5208 (IC base=+0.243)

- **PATRÓN** `dist_vwap_pct` < `0.2982` → IC=+0.248 (n=3553)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2982 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.148` → IC=+0.280 (n=701)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.148 (IC base=+0.243)

- **PATRÓN** `volumen_regimen` < `0.7152` → IC=+0.243 (n=1587)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7152 (IC base=+0.243)

- **PATRÓN** `volumen_regimen` > `1.2188` → IC=+0.264 (n=1202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2188 (IC base=+0.243)

- **PATRÓN** `volumen_pendiente_norm` > `0.2859` → IC=+0.306 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2859 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` > `1.4354` → IC=+0.246 (n=3394)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4354 (IC base=+0.243)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=5791)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.246 (n=2012)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.5031` → IC=+0.227 (n=5984)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5031 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.232 (n=2167)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `0.9348` → IC=+0.256 (n=1996)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9348 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` < `0.4266` → IC=+0.221 (n=4359)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4266 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.557` → IC=+0.227 (n=1965)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.557 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` < `0.7092` → IC=+0.230 (n=1943)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7092 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` > `0.8836` → IC=+0.219 (n=2944)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8836 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` < `0.105` → IC=+0.219 (n=5581)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.105 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.1652` → IC=+0.225 (n=1686)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1652 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` < `2.256` → IC=+0.223 (n=5183)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.256 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.224 (n=4657)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `3756.3742` → IC=+0.227 (n=3989)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3756.3742 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.237 (n=1454)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.49` → IC=+0.211 (n=4355)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.49 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=1466)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.213 (n=1925)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.187` → IC=+0.210 (n=1917)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.187 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `0.6568` → IC=+0.209 (n=747)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6568 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.764` → IC=+0.211 (n=3910)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.764 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `1.0948` → IC=+0.205 (n=3654)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0948 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` < `0.0978` → IC=+0.200 (n=4012)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0978 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.0735` → IC=+0.201 (n=1942)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0735 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `1.5315` → IC=+0.203 (n=1889)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5315 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `2.1859` → IC=+0.206 (n=1946)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1859 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.200 (n=5791)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `ballena_activa_n` < `65.0` → IC=+0.214 (n=2864)

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

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.295 (n=42)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.228)

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
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.220 (n=1451)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.007 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.1453` → IC=+0.218 (n=726)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1453 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.222 (n=580)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` < `0.4974` → IC=+0.219 (n=1100)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4974 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `0.8549` → IC=+0.208 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8549 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` < `0.2044` → IC=+0.215 (n=1466)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2044 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.508` → IC=+0.211 (n=1674)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.508 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` < `0.8752` → IC=+0.210 (n=1100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8752 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` < `0.1024` → IC=+0.209 (n=1517)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1024 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` < `2.4495` → IC=+0.213 (n=1613)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4495 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.244 (n=455)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.484` → IC=+0.221 (n=1359)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.484 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.209 (n=514)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.217 (n=918)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` < `0.4058` → IC=+0.202 (n=906)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4058 (IC base=+0.201)

- **PATRÓN** `ibs_20min` > `0.0909` → IC=+0.204 (n=1359)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0909 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `0.6225` → IC=+0.219 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6225 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.834` → IC=+0.202 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.834 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.345` → IC=+0.205 (n=1239)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.345 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` < `0.6391` → IC=+0.225 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6391 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.0737` → IC=+0.228 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0737 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` < `2.1859` → IC=+0.206 (n=1172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1859 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `6404.3016` → IC=+0.207 (n=1214)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6404.3016 (IC base=+0.201)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.202 (n=1349)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 98.0 (IC base=+0.201)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0098` → IC=+0.223 (n=637)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0098 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.235 (n=670)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.271 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `0.7666` → IC=+0.240 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7666 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.202` → IC=+0.224 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.202 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `0.6421` → IC=+0.248 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6421 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` < `0.1056` → IC=+0.208 (n=860)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1056 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.0795` → IC=+0.206 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0795 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `2.1469` → IC=+0.206 (n=817)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1469 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `1.4745` → IC=+0.204 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4745 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.208 (n=1125)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `4320.729` → IC=+0.244 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4320.729 (IC base=+0.199)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.205 (n=828)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.199)

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
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.147 (n=721)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0037 (IC base=+0.052)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.184 (n=1394)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.75 (IC base=+0.052)

- **PATRÓN** `dist_vwap_pct` > `0.1429` → IC=+0.140 (n=1034)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.1429 (IC base=+0.052)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.442` → IC=+0.148 (n=461)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 10.442 (IC base=+0.052)

- **PATRÓN** `ibs_20min` < `0.0617` → IC=+0.268 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0617 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` > `0.147` → IC=+0.140 (n=392)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.147 (IC base=+0.046)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.537` → IC=-0.124 (n=288)

  - _Acción_: SKIP cuando `ibs_20min` < 0.537
  - _Potencial_: sin este filtro IC_bueno=+0.164 (n=587)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.126 (n=605)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0051 (IC base=+0.069)

- **PATRÓN** `ibs_20min` > `0.537` → IC=+0.164 (n=587)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.537 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` > `0.119` → IC=+0.167 (n=316)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.119 (IC base=+0.069)

- **PATRÓN** `ibs_20min` < `0.0742` → IC=+0.274 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0742 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` > `0.2172` → IC=+0.167 (n=112)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2172 (IC base=+0.046)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.6857` → IC=-0.175 (n=152)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6857
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=459)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.126 (n=469)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0051 (IC base=+0.070)

- **PATRÓN** `ibs_20min` > `0.7783` → IC=+0.219 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7783 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.1265` → IC=+0.173 (n=328)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1265 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.677` → IC=+0.202 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.677 (IC base=+0.070)

- **PATRÓN** `ibs_20min` < `0.0289` → IC=+0.274 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0289 (IC base=+0.023)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.592` → IC=+0.200 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.592 (IC base=+0.023)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.7241` → IC=+0.137 (n=497)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 0.7241 (IC base=+0.020)

- **PATRÓN** `dist_vwap_pct` > `0.4645` → IC=+0.121 (n=249)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` > 0.4645 (IC base=+0.020)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.664` → IC=+0.136 (n=163)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 8.664 (IC base=+0.020)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.147 (n=378)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0112 (IC base=+0.071)

- **PATRÓN** `ibs_20min` < `0.3415` → IC=+0.200 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3415 (IC base=+0.071)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.838` → IC=+0.283 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.838 (IC base=+0.071)

- **PATRÓN** `volumen_regimen` > `1.082` → IC=+0.167 (n=133)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 1.082 (IC base=+0.071)

- **PATRÓN** `volumen_pendiente_norm` > `0.1555` → IC=+0.172 (n=114)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1555 (IC base=+0.071)

- **PATRÓN** `volumen_spike_ratio` > `1.8571` → IC=+0.136 (n=248)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.8571 (IC base=+0.071)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` < `0.0058` → IC=-0.239 (n=186)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0058
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=187)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.300 (n=93)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=280)

- **FILTRO** `dist_vwap_pct` > `0.2352` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2352
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=357)

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
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=61)

- **FILTRO** `sigma_ewma_delta_pct` > `9.679` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.679
  - _Potencial_: sin este filtro IC_bueno=-0.234 (n=92)

- **FILTRO** `volumen_regimen` < `0.89` → IC=-0.328 (n=27)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.89
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=82)

- **FILTRO** `sigma_h` < `0.0033` → IC=-0.257 (n=72)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=74)

- **FILTRO** `hora_utc` < `13.0` → IC=-0.300 (n=73)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=73)

- **FILTRO** `ibs_20min` > `0.7502` → IC=-0.265 (n=49)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7502
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=97)

- **FILTRO** `volumen_regimen` > `0.805` → IC=-0.316 (n=36)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.232 (n=110)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.5857` → IC=-0.471 (n=32)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5857
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=98)

- **FILTRO** `volumen_regimen` > `1.0679` → IC=-0.174 (n=44)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.0679
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=86)

- **FILTRO** `sigma_h` > `0.0054` → IC=-0.375 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0054
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=97)

- **FILTRO** `ibs_20min` > `0.681` → IC=-0.389 (n=43)

  - _Acción_: SKIP cuando `ibs_20min` > 0.681
  - _Potencial_: sin este filtro IC_bueno=-0.256 (n=84)

- **FILTRO** `volumen_spike_ratio` < `1.4324` → IC=-0.380 (n=23)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.4324
  - _Potencial_: sin este filtro IC_bueno=-0.289 (n=69)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.298 (n=112)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `5.0` → IC=-0.344 (n=43)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=91)

- **FILTRO** `volumen_spike_ratio` > `2.3401` → IC=-0.269 (n=37)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.3401
  - _Potencial_: sin este filtro IC_bueno=-0.216 (n=72)

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
- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.242 (n=231)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.191 (n=360)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 15.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.6757` → IC=+0.181 (n=693)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.6757 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.7967` → IC=+0.280 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7967 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.614` → IC=+0.155 (n=381)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 3.614 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `0.6244` → IC=+0.182 (n=231)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6244 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` < `0.0701` → IC=+0.175 (n=512)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` < 0.0701 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `1.3956` → IC=+0.187 (n=196)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.3956 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.53` → IC=+0.156 (n=190)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 10.53 (IC base=+0.033)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.7805` → IC=-0.126 (n=89)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7805
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=183)

- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.157 (n=68)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0062 (IC base=+0.036)

- **PATRÓN** `ibs_20min` > `0.9071` → IC=+0.123 (n=136)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` > 0.9071 (IC base=+0.036)

- **PATRÓN** `dist_vwap_pct` > `0.6135` → IC=+0.207 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6135 (IC base=+0.036)

- **PATRÓN** `ibs_20min` < `0.215` → IC=+0.147 (n=383)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.215 (IC base=+0.088)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.339` → IC=+0.133 (n=88)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 11.339 (IC base=+0.088)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1848` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1848
  - _Potencial_: sin este filtro IC_bueno=+0.145 (n=246)

- **FILTRO** `ibs_20min` > `0.1452` → IC=-0.126 (n=137)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1452
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=267)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.126 (n=204)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0056 (IC base=+0.117)

- **PATRÓN** `drift_60min` |x|≤ `0.1024` → IC=+0.135 (n=102)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.1024 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.163 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 18.0 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.128 (n=111)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 8.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.8899` → IC=+0.181 (n=155)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.8899 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` < `0.0953` → IC=+0.144 (n=192)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.0953 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.38` → IC=+0.146 (n=241)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 9.38 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.6249` → IC=+0.163 (n=78)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.6249 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` < `0.1848` → IC=+0.145 (n=246)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` < 0.1848 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `2.0767` → IC=+0.152 (n=179)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.0767 (IC base=+0.117)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.129 (n=200)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.584` → IC=+0.210 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.584 (IC base=+0.012)

- **PATRÓN** `volumen_pendiente_norm` > `0.2839` → IC=+0.130 (n=44)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` > 0.2839 (IC base=+0.012)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.2` → IC=-0.233 (n=58)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=128)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.295 (n=183)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.281 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` > `0.6943` → IC=+0.387 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6943 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.832` → IC=+0.357 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.832 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` < `0.5849` → IC=+0.295 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5849 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.308 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` < `1.4812` → IC=+0.324 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4812 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `2.3425` → IC=+0.297 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3425 (IC base=+0.244)

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
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.121 (n=1435)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.5 (IC base=+0.097)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.121 (n=1435)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.5 (IC base=+0.097)

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
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=741)

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
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=3907)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=139)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=96)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=126)

- **FILTRO** `ballena_activa_n` > `21.0` → IC=-0.160 (n=92)

  - _Acción_: SKIP cuando `ballena_activa_n` > 21.0
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=34)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.278 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=-0.080)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.141 (n=51)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=146)

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
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.333 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.267)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.269 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.5 (IC base=+0.267)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=1594)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=1548)

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
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=727)

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
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=442)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=423)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.145 (n=187)

  - _Acción_: Kelly boost +0.73€ cuando `py_entrada` < 0.495 (IC base=+0.022)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=982)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=982)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=1209)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=1209)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=274)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=274)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.146 (n=63)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=336)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=384)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=297)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=396)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=396)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.120 (n=185)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=241)

- **FILTRO** `libro_liquidez` < `550.099` → IC=-0.139 (n=106)

  - _Acción_: SKIP cuando `libro_liquidez` < 550.099
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=320)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=347)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **FILTRO** `py_entrada` > `0.59` → IC=-0.141 (n=37)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=72)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.196 (n=77)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=95)

- **FILTRO** `hora_utc` > `14.0` → IC=-0.167 (n=79)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=93)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.159 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=45)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.241 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=59)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.128 (n=264)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=680)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.51` → IC=+0.131 (n=315)

  - _Acción_: Kelly boost +0.65€ cuando `py_entrada` < 0.51 (IC base=-0.009)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.152 (n=159)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=339)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.121 (n=336)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=351)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` > `0.58` → IC=-0.122 (n=329)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=391)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.164 (n=144)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=641)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=529)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=280)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.138 (n=114)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=353)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.141 (n=471)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=473)

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

- **FILTRO** `py_entrada` > `0.505` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=2289)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=1413)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.46` → IC=-0.172 (n=7676)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=24609)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.175 (n=8190)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=25086)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.182 (n=1477)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=4494)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.149 (n=1985)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=3913)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.133 (n=1547)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` > 1.0 (IC base=+0.042)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.125 (n=3001)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.505 (IC base=+0.012)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.171 (n=1062)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=3444)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.180 (n=1171)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=3519)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.203 (n=1465)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=4573)

- **PATRÓN** `ibs_20min` > `0.963` → IC=+0.134 (n=2032)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 0.963 (IC base=+0.035)

- **PATRÓN** `libro_liquidez` > `1747.5976` → IC=+0.122 (n=2029)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1747.5976 (IC base=+0.035)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` > `0.58` → IC=-0.181 (n=1110)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=3641)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.158 (n=1485)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=4518)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2432)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=2356)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=973)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=3022)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=3974)

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
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=1063)

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
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=360)

- **FILTRO** `ballena_activa_n` > `84.0` → IC=-0.179 (n=157)

  - _Acción_: SKIP cuando `ballena_activa_n` > 84.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=308)

- **FILTRO** `libro_liquidez` < `3222.056` → IC=-0.183 (n=156)

  - _Acción_: SKIP cuando `libro_liquidez` < 3222.056
  - _Potencial_: sin este filtro IC_bueno=-0.096 (n=317)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=968)

- **FILTRO** `ballena_activa_n` > `23.0` → IC=-0.191 (n=390)

  - _Acción_: SKIP cuando `ballena_activa_n` > 23.0
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=782)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.134 (n=21935)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=49512)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.297 (n=17066)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=54381)

- **FILTRO** `ibs_7min` < `0.2193` → IC=-0.232 (n=17859)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2193
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=53588)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.152 (n=23416)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=48031)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.251 (n=20901)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=68550)

- **FILTRO** `ibs_7min` > `0.283` → IC=-0.184 (n=22357)

  - _Acción_: SKIP cuando `ibs_7min` > 0.283
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=67094)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.155 (n=3075)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=9635)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.318 (n=3127)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=9583)

- **FILTRO** `ibs_7min` < `0.7115` → IC=-0.250 (n=4192)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7115
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=8518)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.152 (n=2766)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=9944)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.276 (n=3763)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=11690)

- **FILTRO** `ibs_7min` > `0.777` → IC=-0.211 (n=3862)

  - _Acción_: SKIP cuando `ibs_7min` > 0.777
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=11591)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.262 (n=2865)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=9038)

- **FILTRO** `ibs_7min` < `0.7149` → IC=-0.207 (n=2975)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7149
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=8928)

- **FILTRO** `ballena_activa_n` > `155.0` → IC=-0.199 (n=2961)

  - _Acción_: SKIP cuando `ballena_activa_n` > 155.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=8942)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.269 (n=2796)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=9370)

- **FILTRO** `ibs_7min` > `0.2666` → IC=-0.195 (n=3041)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2666
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=9125)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.182 (n=3034)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=9132)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.165 (n=2929)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=9224)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.323 (n=2879)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=9274)

- **FILTRO** `ibs_7min` < `0.29` → IC=-0.249 (n=4010)

  - _Acción_: SKIP cuando `ibs_7min` < 0.29
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=8143)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.200 (n=2461)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=9692)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.258 (n=3956)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=12410)

- **FILTRO** `ibs_7min` > `0.7326` → IC=-0.183 (n=4091)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7326
  - _Potencial_: sin este filtro IC_bueno=-0.000 (n=12275)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.261 (n=2855)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=8706)

- **FILTRO** `ibs_7min` < `0.7161` → IC=-0.195 (n=2890)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7161
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=8671)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.188 (n=2822)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=8739)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.259 (n=2787)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=9261)

- **FILTRO** `ibs_7min` > `0.2743` → IC=-0.177 (n=3011)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2743
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=9037)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.170 (n=2944)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=9104)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.297 (n=2698)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=8770)

- **FILTRO** `ibs_7min` < `0.7027` → IC=-0.230 (n=3781)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7027
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=7687)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.216 (n=2840)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=8628)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.198 (n=4194)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=13115)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.131 (n=3741)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=7911)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.308 (n=2759)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=8893)

- **FILTRO** `ibs_7min` < `0.1667` → IC=-0.230 (n=2909)

  - _Acción_: SKIP cuando `ibs_7min` < 0.1667
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=8743)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.204 (n=2595)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=9057)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.233 (n=3743)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=12366)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=121)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.160 (n=301)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=1010)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=1296)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=887)

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

- **FILTRO** `py_entrada` > `0.58` → IC=-0.216 (n=192)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=578)

- **FILTRO** `libro_liquidez` < `3302.3462` → IC=-0.155 (n=192)

  - _Acción_: SKIP cuando `libro_liquidez` < 3302.3462
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=578)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=394)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4307` → IC=+0.152 (n=671)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio` |x|> 0.4307 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.131 (n=756)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 6.0 (IC base=+0.123)

- **PATRÓN** `total_vol_5m` < `418.1817` → IC=+0.163 (n=493)

  - _Acción_: Kelly boost +0.81€ cuando `total_vol_5m` < 418.1817 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `2321.735` → IC=+0.132 (n=1320)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2321.735 (IC base=+0.123)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.178 (n=178)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 14.0 (IC base=+0.132)

- **PATRÓN** `total_vol_5m` < `375.759` → IC=+0.158 (n=311)

  - _Acción_: Kelly boost +0.79€ cuando `total_vol_5m` < 375.759 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `2517.123` → IC=+0.242 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2517.123 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.135 (n=168)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 6.0 (IC base=+0.132)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.4378` → IC=+0.154 (n=102)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.77€ cuando `delta_ratio` |x|> 0.4378 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.140 (n=281)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 15.0 (IC base=+0.118)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.125 (n=366)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.04 (IC base=+0.118)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4165` → IC=+0.184 (n=185)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.92€ cuando `delta_ratio` |x|> 0.4165 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.177 (n=97)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 15.0 (IC base=+0.128)

- **PATRÓN** `total_vol_5m` < `655.7381` → IC=+0.159 (n=244)

  - _Acción_: Kelly boost +0.79€ cuando `total_vol_5m` < 655.7381 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.180 (n=95)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 59.0 (IC base=+0.128)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4318` → IC=+0.209 (n=115)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4318 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.178 (n=181)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 12.0 (IC base=+0.143)

- **PATRÓN** `total_vol_5m` < `4608.276` → IC=+0.178 (n=169)

  - _Acción_: Kelly boost +0.89€ cuando `total_vol_5m` < 4608.276 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `3698.2852` → IC=+0.167 (n=169)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3698.2852 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.147 (n=114)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 27.0 (IC base=+0.143)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `13.0` → IC=+0.124 (n=259)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 13.0 (IC base=+0.095)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=201)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.095)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.4417` → IC=-0.272 (n=55)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.4417
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=167)

- **FILTRO** `pct_vs_K` |x|> `3.4135` → IC=-0.195 (n=283)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.4135
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=550)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.150 (n=275)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0045 (IC base=-0.075)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0049` → IC=-0.184 (n=166)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0049
  - _Potencial_: sin este filtro IC_bueno=+0.277 (n=83)

- **FILTRO** `T_h` > `88.1766` → IC=-0.234 (n=62)

  - _Acción_: SKIP cuando `T_h` > 88.1766
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=187)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.277 (n=83)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.030)

- **PATRÓN** `pct_vs_K` |x|≤ `1.7112` → IC=+0.171 (n=83)

  - _Acción_: Kelly boost +0.85€ cuando `pct_vs_K` |x|≤ 1.7112 (IC base=-0.030)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `T_h` < `251.7955` → IC=-0.210 (n=60)

  - _Acción_: SKIP cuando `T_h` < 251.7955
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=21)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0151` → IC=-0.207 (n=39)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0151
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=119)

- **FILTRO** `T_h` < `66.2576` → IC=-0.185 (n=52)

  - _Acción_: SKIP cuando `T_h` < 66.2576
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=106)

### PRICE_TARGET_GBM#SOL#reach
- **FILTRO** `T_h` < `146.0708` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `T_h` < 146.0708
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0102` → IC=-0.235 (n=504)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0102
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=260)

- **FILTRO** `T_h` > `70.1154` → IC=-0.227 (n=511)

  - _Acción_: SKIP cuando `T_h` > 70.1154
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=253)

- **FILTRO** `pct_vs_K` |x|> `3.0893` → IC=-0.410 (n=164)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.0893
  - _Potencial_: sin este filtro IC_bueno=-0.122 (n=493)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0082` → IC=-0.207 (n=165)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0082
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=86)

- **FILTRO** `sigma_h` > `0.0062` → IC=-0.256 (n=121)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0062
  - _Potencial_: sin este filtro IC_bueno=-0.169 (n=122)

- **FILTRO** `T_h` > `143.4358` → IC=-0.258 (n=60)

  - _Acción_: SKIP cuando `T_h` > 143.4358
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=183)

- **FILTRO** `T_h` < `88.1777` → IC=-0.244 (n=80)

  - _Acción_: SKIP cuando `T_h` < 88.1777
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=163)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `sigma_h` > `0.0043` → IC=-0.300 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0043
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=13)

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
- **FILTRO** `sigma_h` < `0.0097` → IC=-0.310 (n=140)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=74)

- **FILTRO** `T_h` > `95.4524` → IC=-0.287 (n=106)

  - _Acción_: SKIP cuando `T_h` > 95.4524
  - _Potencial_: sin este filtro IC_bueno=-0.264 (n=108)

- **FILTRO** `sigma_h` > `0.0091` → IC=-0.365 (n=50)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=151)

- **FILTRO** `T_h` > `57.2198` → IC=-0.235 (n=134)

  - _Acción_: SKIP cuando `T_h` > 57.2198
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=67)

- **PATRÓN** `pct_vs_K` |x|≤ `0.8095` → IC=+0.198 (n=51)

  - _Acción_: Kelly boost +0.99€ cuando `pct_vs_K` |x|≤ 0.8095 (IC base=-0.160)

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
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=162)

- **FILTRO** `T_h` > `66.1685` → IC=-0.224 (n=161)

  - _Acción_: SKIP cuando `T_h` > 66.1685
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=54)

- **FILTRO** `sigma_h` > `0.0142` → IC=-0.304 (n=49)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0142
  - _Potencial_: sin este filtro IC_bueno=-0.163 (n=96)

- **FILTRO** `sigma_h` < `0.0085` → IC=-0.263 (n=36)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=109)

- **FILTRO** `T_h` < `89.2641` → IC=-0.232 (n=95)

  - _Acción_: SKIP cuando `T_h` < 89.2641
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=50)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1195` → IC=+0.461 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1195 (IC base=+0.333)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.383 (n=75)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.333)

- **PATRÓN** `T_h` < `0.3261` → IC=+0.400 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.3261 (IC base=+0.333)

- **PATRÓN** `T_h` > `0.8789` → IC=+0.368 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8789 (IC base=+0.333)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.481 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.333)

- **PATRÓN** `edge` > `0.1` → IC=+0.429 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1 (IC base=+0.394)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.400 (n=88)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.394)

- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.410 (n=176)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.394)

- **PATRÓN** `T_h` > `1.4832` → IC=+0.400 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4832 (IC base=+0.394)

- **PATRÓN** `dist_50` > `0.3717` → IC=+0.444 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3717 (IC base=+0.394)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.412 (n=326)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.394)

### RESOLUTION_SNIPER#BTC#sniper
- **PATRÓN** `edge` > `0.1235` → IC=+0.268 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1235 (IC base=+0.179)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.269 (n=37)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.179)

- **PATRÓN** `T_h` > `1.484` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.484 (IC base=+0.179)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.263 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.219 (n=55)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.179)

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

- **PATRÓN** `edge` > `0.2008` → IC=+0.471 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2008 (IC base=+0.463)

- **PATRÓN** `sigma_h` < `0.0157` → IC=+0.474 (n=151)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0157 (IC base=+0.463)

- **PATRÓN** `T_h` < `0.8102` → IC=+0.457 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.8102 (IC base=+0.463)

- **PATRÓN** `T_h` > `1.486` → IC=+0.481 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.486 (IC base=+0.463)

- **PATRÓN** `dist_50` > `0.4597` → IC=+0.493 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4597 (IC base=+0.463)

- **PATRÓN** `hora_utc` < `2.0` → IC=+0.485 (n=63)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 2.0 (IC base=+0.463)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=406)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=474)

- **PATRÓN** `streak_estiramiento` < `0.2752` → IC=+0.148 (n=103)

  - _Acción_: Kelly boost +0.74€ cuando `streak_estiramiento` < 0.2752 (IC base=+0.027)

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
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=161)

- **PATRÓN** `streak_estiramiento` < `0.2206` → IC=+0.135 (n=61)

  - _Acción_: Kelly boost +0.67€ cuando `streak_estiramiento` < 0.2206 (IC base=+0.032)

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

- **FILTRO** `libro_spread` > `0.01` → IC=-0.136 (n=31)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=35)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=1061)

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
- **FILTRO** `hora_utc` < `15.0` → IC=-0.167 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=26)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=4803)

### STRUCT_NO_15M#ETH#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.167 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=26)

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
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=2778)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.191 (n=1712)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0053 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.2179` → IC=+0.160 (n=5133)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.2179 (IC base=+0.145)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3578` → IC=+0.154 (n=4782)

  - _Acción_: Kelly boost +0.77€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3578 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.154 (n=4752)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 6.0 (IC base=+0.145)

- **PATRÓN** `ibs_15` > `0.5833` → IC=+0.231 (n=4601)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5833 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.1322` → IC=+0.137 (n=2444)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.1322 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` < `0.4956` → IC=+0.131 (n=4784)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.4956 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.295` → IC=+0.255 (n=978)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.295 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=2986)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `4612.7985` → IC=+0.170 (n=1711)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 4612.7985 (IC base=+0.145)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1951)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.221 (n=775)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.0598` → IC=+0.258 (n=258)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0598 (IC base=+0.202)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2676` → IC=+0.219 (n=258)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2676 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.220 (n=808)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.202)

- **PATRÓN** `ibs_15` > `0.7086` → IC=+0.276 (n=774)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7086 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.3722` → IC=+0.228 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3722 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` < `0.5105` → IC=+0.206 (n=872)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5105 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.54` → IC=+0.307 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.54 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=1001)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `11859.2402` → IC=+0.218 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11859.2402 (IC base=+0.202)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.147 (n=954)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0069 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.1091` → IC=+0.144 (n=636)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.1091 (IC base=+0.131)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1407` → IC=+0.134 (n=637)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio_macro` |x|> 0.1407 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.136 (n=874)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 6.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.134 (n=1005)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 17.0 (IC base=+0.131)

- **PATRÓN** `ibs_15` > `0.4934` → IC=+0.216 (n=954)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.4934 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` > `0.1163` → IC=+0.151 (n=599)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.1163 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.4255` → IC=+0.131 (n=1010)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.4255 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.81` → IC=+0.283 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.81 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `5879.8519` → IC=+0.162 (n=433)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 5879.8519 (IC base=+0.131)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `ibs_15` > `0.2521` → IC=-0.122 (n=199)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.2521
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=389)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.6` → IC=+0.135 (n=936)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.68€ cuando `ibs_15` > 0.6 (IC base=+0.061)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` < `0.0255` → IC=+0.170 (n=1265)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0255 (IC base=+0.158)

- **PATRÓN** `drift_60min` |x|≤ `0.2207` → IC=+0.175 (n=1265)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2207 (IC base=+0.158)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0989` → IC=+0.215 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0989 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.162 (n=1162)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 6.0 (IC base=+0.158)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.165 (n=1121)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 14.0 (IC base=+0.158)

- **PATRÓN** `ibs_15` > `0.5455` → IC=+0.236 (n=1134)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5455 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `0.5172` → IC=+0.198 (n=313)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.5172 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.989` → IC=+0.206 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.989 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `2716.8736` → IC=+0.189 (n=843)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 2716.8736 (IC base=+0.158)

- **PATRÓN** `ibs_15` < `0.1111` → IC=+0.157 (n=985)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.78€ cuando `ibs_15` < 0.1111 (IC base=+0.068)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.388 (n=247)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.363)

- **PATRÓN** `drift_60min` |x|≤ `0.1119` → IC=+0.365 (n=493)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1119 (IC base=+0.363)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1501` → IC=+0.377 (n=492)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1501 (IC base=+0.363)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1074` → IC=+0.377 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1074 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.371 (n=781)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.363)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.363 (n=496)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.363)

- **PATRÓN** `ibs_15` > `0.7903` → IC=+0.393 (n=739)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7903 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` > `0.1529` → IC=+0.379 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1529 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.963` → IC=+0.398 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.963 (IC base=+0.363)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.367 (n=899)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.363)

- **PATRÓN** `libro_liquidez` > `9740.6649` → IC=+0.381 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9740.6649 (IC base=+0.363)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.371 (n=122)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2194` → IC=+0.374 (n=165)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2194 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1436` → IC=+0.397 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1436 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.379 (n=338)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.8112` → IC=+0.385 (n=364)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8112 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.3743` → IC=+0.391 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3743 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.114` → IC=+0.389 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.114 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `15217.9578` → IC=+0.386 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15217.9578 (IC base=+0.362)

- **PATRÓN** `ballena_activa_n` < `489.0` → IC=+0.404 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 489.0 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.368 (n=376)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.362)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.378 (n=170)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.362)

- **PATRÓN** `drift_60min` |x|≤ `0.108` → IC=+0.366 (n=252)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.108 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0824` → IC=+0.372 (n=335)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0824 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.373 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.365 (n=377)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.362)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.374 (n=173)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.762` → IC=+0.391 (n=375)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.762 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.1215` → IC=+0.370 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1215 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` < `0.2797` → IC=+0.365 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2797 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.991` → IC=+0.402 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.991 (IC base=+0.362)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.366 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `4142.643` → IC=+0.378 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4142.643 (IC base=+0.362)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0074` → IC=-0.193 (n=2651)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0074
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=2655)

- **FILTRO** `drift_15min` |x|> `0.9088` → IC=-0.145 (n=1326)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9088
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=3979)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.216 (n=2220)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3086)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1398` → IC=+0.221 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1398 (IC base=-0.080)

- **PATRÓN** `ibs_15` > `0.6296` → IC=+0.279 (n=1208)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6296 (IC base=-0.080)

- **PATRÓN** `dist_vwap_pct` > `0.1102` → IC=+0.204 (n=707)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1102 (IC base=-0.080)

- **PATRÓN** `dist_vwap_pct` < `0.5564` → IC=+0.200 (n=1277)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5564 (IC base=-0.080)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2353` → IC=+0.270 (n=1594)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2353 (IC base=-0.005)

- **PATRÓN** `ibs_15` < `0.3682` → IC=+0.284 (n=4783)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3682 (IC base=-0.005)

- **PATRÓN** `dist_vwap_pct` > `0.6474` → IC=+0.279 (n=677)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6474 (IC base=-0.005)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0316` → IC=-0.222 (n=2487)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0316
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=830)

- **FILTRO** `sigma_h` < `0.0037` → IC=-0.220 (n=829)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0037
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=2488)

- **FILTRO** `sigma_ewma_delta_pct` > `22.22` → IC=-0.258 (n=473)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.22
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=2844)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.154 (n=322)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.003 (IC base=+0.072)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2673` → IC=+0.282 (n=140)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2673 (IC base=+0.072)

- **PATRÓN** `ibs_15` > `0.7593` → IC=+0.326 (n=418)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7593 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` > `0.1023` → IC=+0.277 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1023 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` < `0.4912` → IC=+0.286 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4912 (IC base=+0.072)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.337` → IC=+0.148 (n=217)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 22.337 (IC base=+0.072)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0742` → IC=+0.224 (n=74)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0742 (IC base=-0.187)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0866` → IC=+0.308 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0866 (IC base=-0.187)

- **PATRÓN** `ibs_15` < `0.6255` → IC=+0.289 (n=74)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6255 (IC base=-0.187)

- **PATRÓN** `dist_vwap_pct` < `0.0453` → IC=+0.303 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0453 (IC base=-0.187)

- **PATRÓN** `ballena_activa_n` < `393.0` → IC=+0.300 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 393.0 (IC base=-0.187)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.153 (n=791)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.159 (n=607)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0065 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.0733` → IC=+0.181 (n=268)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.0733 (IC base=+0.147)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3048` → IC=+0.195 (n=474)

  - _Acción_: Kelly boost +0.98€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3048 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.161 (n=435)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 11.0 (IC base=+0.147)

- **PATRÓN** `ibs_15` > `0.5679` → IC=+0.242 (n=606)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5679 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.6362` → IC=+0.158 (n=112)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.6362 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.2696` → IC=+0.152 (n=567)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.2696 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.973` → IC=+0.265 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.973 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=791)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `8988.4246` → IC=+0.162 (n=202)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 8988.4246 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.249 (n=1819)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0081 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.3542` → IC=+0.247 (n=1601)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3542 (IC base=+0.242)

- **PATRÓN** `drift_15min` |x|≤ `0.774` → IC=+0.258 (n=1601)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.774 (IC base=+0.242)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2147` → IC=+0.264 (n=825)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2147 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.253 (n=674)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.243 (n=1238)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.242)

- **PATRÓN** `ibs_15` < `0.3799` → IC=+0.273 (n=1819)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3799 (IC base=+0.242)

- **PATRÓN** `dist_vwap_pct` > `0.3779` → IC=+0.267 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3779 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.253` → IC=+0.245 (n=709)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.253 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.182` → IC=+0.248 (n=1899)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.182 (IC base=+0.242)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1822` → IC=-0.261 (n=307)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1822
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=923)

- **FILTRO** `drift_60min` |x|> `0.1722` → IC=-0.259 (n=417)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1722
  - _Potencial_: sin este filtro IC_bueno=-0.163 (n=813)

- **FILTRO** `drift_15min` |x|> `0.9075` → IC=-0.282 (n=306)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9075
  - _Potencial_: sin este filtro IC_bueno=-0.166 (n=924)

- **FILTRO** `sigma_ewma_delta_pct` > `6.133` → IC=-0.199 (n=284)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.133
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=946)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.214 (n=243)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=987)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1455` → IC=+0.188 (n=46)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.1455 (IC base=-0.196)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.196)

- **PATRÓN** `dist_vwap_pct` > `0.2752` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.2752 (IC base=-0.196)

- **PATRÓN** `dist_vwap_pct` < `0.4298` → IC=+0.154 (n=76)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.4298 (IC base=-0.196)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0642` → IC=+0.233 (n=812)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0642 (IC base=-0.032)

- **PATRÓN** `ibs_15` < `0.383` → IC=+0.294 (n=812)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.383 (IC base=-0.032)

- **PATRÓN** `dist_vwap_pct` > `0.6758` → IC=+0.240 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6758 (IC base=-0.032)

- **PATRÓN** `dist_vwap_pct` < `0.1929` → IC=+0.244 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1929 (IC base=-0.032)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0133` → IC=-0.242 (n=1125)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0133
  - _Potencial_: sin este filtro IC_bueno=-0.138 (n=376)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.215 (n=1482)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.216)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.216)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0941` → IC=+0.296 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0941 (IC base=-0.017)

- **PATRÓN** `ibs_15` < `0.1333` → IC=+0.310 (n=751)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1333 (IC base=-0.017)

- **PATRÓN** `dist_vwap_pct` > `0.7602` → IC=+0.337 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7602 (IC base=-0.017)

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

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.299 (n=441)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.283)

- **PATRÓN** `drift_60min` |x|≤ `0.0733` → IC=+0.310 (n=583)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0733 (IC base=+0.283)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1522` → IC=+0.286 (n=880)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1522 (IC base=+0.283)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2235` → IC=+0.291 (n=803)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2235 (IC base=+0.283)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.297 (n=1364)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.283)

- **PATRÓN** `ibs_15` > `0.8385` → IC=+0.312 (n=1320)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8385 (IC base=+0.283)

- **PATRÓN** `dist_vwap_pct` > `0.262` → IC=+0.313 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.262 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.932` → IC=+0.389 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.932 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `13286.7566` → IC=+0.305 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13286.7566 (IC base=+0.283)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.305 (n=234)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.277)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.278 (n=318)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.277)

- **PATRÓN** `drift_60min` |x|≤ `0.0596` → IC=+0.314 (n=234)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0596 (IC base=+0.277)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3961` → IC=+0.282 (n=628)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3961 (IC base=+0.277)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.296 (n=733)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.277)

- **PATRÓN** `ibs_15` > `0.8292` → IC=+0.304 (n=701)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8292 (IC base=+0.277)

- **PATRÓN** `dist_vwap_pct` > `0.2467` → IC=+0.309 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2467 (IC base=+0.277)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.806` → IC=+0.392 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.806 (IC base=+0.277)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.278 (n=905)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.277)

- **PATRÓN** `libro_liquidez` > `14783.8555` → IC=+0.306 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14783.8555 (IC base=+0.277)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.304 (n=620)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.0506` → IC=+0.313 (n=207)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0506 (IC base=+0.290)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0654` → IC=+0.291 (n=620)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0654 (IC base=+0.290)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1009` → IC=+0.326 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1009 (IC base=+0.290)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.302 (n=594)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.290)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.295 (n=569)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.290)

- **PATRÓN** `ibs_15` > `0.8489` → IC=+0.318 (n=620)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8489 (IC base=+0.290)

- **PATRÓN** `dist_vwap_pct` > `0.1233` → IC=+0.307 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1233 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.164` → IC=+0.379 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.164 (IC base=+0.290)

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
- **PATRÓN** `ratio` < `0.9704` → IC=+0.398 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9704 (IC base=+0.175)

- **PATRÓN** `T_h` > `120.2753` → IC=+0.355 (n=2753)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 120.2753 (IC base=+0.337)

- **PATRÓN** `ratio` > `1.0221` → IC=+0.390 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0221 (IC base=+0.337)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `111.9936` → IC=+0.145 (n=260)

  - _Acción_: Kelly boost +0.73€ cuando `T_h` > 111.9936 (IC base=+0.133)

- **PATRÓN** `ratio` < `0.9933` → IC=+0.268 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9933 (IC base=+0.133)

- **PATRÓN** `T_h` > `111.9836` → IC=+0.318 (n=990)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9836 (IC base=+0.303)

- **PATRÓN** `ratio` > `1.0187` → IC=+0.361 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0187 (IC base=+0.303)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `85.7585` → IC=+0.225 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 85.7585 (IC base=+0.223)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.405 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.223)

- **PATRÓN** `T_h` > `111.9969` → IC=+0.356 (n=997)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9969 (IC base=+0.324)

- **PATRÓN** `ratio` > `1.0314` → IC=+0.401 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0314 (IC base=+0.324)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0788` → IC=+0.419 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0788 (IC base=+0.397)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5833 sube el IC de +0.145 a +0.231 en UPDOWN_GBM#15min (n=4601). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7086 sube el IC de +0.202 a +0.276 en UPDOWN_GBM#BTC#15min (n=774). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.4934 sube el IC de +0.131 a +0.216 en UPDOWN_GBM#ETH#15min (n=954). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5455 sube el IC de +0.158 a +0.236 en UPDOWN_GBM#XRP#15min (n=1134). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1111 sube el IC de +0.068 a +0.157 en UPDOWN_GBM#XRP#15min (n=985). Ya aplicado como kelly_boost=+0.78€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6296 sube el IC de -0.080 a +0.279 en UPDOWN_GBM_15M_TARDIO (n=1208). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3682 sube el IC de -0.005 a +0.284 en UPDOWN_GBM_15M_TARDIO (n=4783). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7593 sube el IC de +0.072 a +0.326 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=418). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6255 sube el IC de -0.187 a +0.289 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=74). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5679 sube el IC de +0.147 a +0.242 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=606). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3799 sube el IC de +0.242 a +0.273 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1819). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.196 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.383 sube el IC de -0.032 a +0.294 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=812). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.216 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.1333 sube el IC de -0.017 a +0.310 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=751). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.097 a +0.340 en UPDOWN_GBM_ETH_15M_HORA7 (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.097 a +0.340 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8385 sube el IC de +0.283 a +0.312 en UPDOWN_GBM_IBS_ALTO (n=1320). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8292 sube el IC de +0.277 a +0.304 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=701). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.290 a +0.318 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=620). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7903 sube el IC de +0.363 a +0.393 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=739). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8112 sube el IC de +0.362 a +0.385 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=364). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.762 sube el IC de +0.362 a +0.391 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=375). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2163 | +0.085 | +236.67€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2163 | +0.085 | +236.67€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1758 | +0.085 | +197.39€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1758 | +0.085 | +197.39€ | 1 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 284 | +0.070 | +11.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 284 | +0.070 | +11.30€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 90 | +0.130 | +28.32€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 90 | +0.130 | +28.32€ | 1 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 1106 | -0.022 | +70.19€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 1106 | -0.022 | +70.19€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 853 | -0.037 | +55.32€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 853 | -0.037 | +55.32€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 169 | +0.056 | +17.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 169 | +0.056 | +17.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 77 | -0.032 | -6.17€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 77 | -0.032 | -6.17€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 46532 | -0.086 | -5963.05€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2832 | +0.064 | -294.29€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 43700 | -0.096 | -5668.75€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4774 | -0.112 | -804.36€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4774 | -0.112 | -804.36€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2832 | +0.064 | -294.29€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2832 | +0.064 | -294.29€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4831 | -0.108 | -933.46€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4831 | -0.108 | -933.46€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 12667 | -0.043 | -1169.37€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 12667 | -0.043 | -1169.37€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 12655 | -0.115 | -1335.08€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 12655 | -0.115 | -1335.08€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 8773 | -0.128 | -1426.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 8773 | -0.128 | -1426.49€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 47399 | -0.012 | +2901.22€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 12250 | +0.005 | +1541.98€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 35149 | -0.018 | +1359.24€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 47399 | -0.012 | +2901.22€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 12250 | +0.005 | +1541.98€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 35149 | -0.018 | +1359.24€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 182993 | +0.113 | -7648.95€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 21456 | +0.180 | -691.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 838 | +0.005 | -78.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 150206 | +0.105 | -6502.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 10493 | +0.093 | -376.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 24893 | +0.102 | -1761.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 75 | -0.175 | +11.25€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 24803 | +0.104 | -1761.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 34779 | +0.124 | -584.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5594 | +0.179 | -224.57€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 24870 | +0.120 | -184.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4273 | +0.079 | -153.37€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 24941 | +0.097 | -1843.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 84 | -0.116 | +5.91€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 24842 | +0.098 | -1837.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 39069 | +0.123 | -826.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 9874 | +0.177 | -245.21€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 25257 | +0.105 | -522.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3926 | +0.103 | -50.19€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 34395 | +0.112 | -1522.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5744 | +0.199 | -246.93€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 741 | +0.032 | -25.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 25616 | +0.096 | -1078.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2294 | +0.102 | -172.46€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO#XRP | 24916 | +0.106 | -1110.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 85 | -0.121 | +7.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 24818 | +0.107 | -1117.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 29650 | +0.193 | -2006.64€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 29650 | +0.193 | -2006.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 6706 | +0.172 | -657.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 6706 | +0.172 | -657.86€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 4228 | +0.198 | -151.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 4228 | +0.198 | -151.22€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 6592 | +0.177 | -563.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 6592 | +0.177 | -563.17€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 5550 | +0.250 | -201.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 5550 | +0.250 | -201.45€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 6495 | +0.185 | -446.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 6495 | +0.185 | -446.70€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1215 | +0.426 | -43.85€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1215 | +0.426 | -43.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 498 | +0.440 | -3.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 498 | +0.440 | -3.80€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 490 | +0.425 | -17.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 490 | +0.425 | -17.81€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 213 | +0.398 | -18.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 213 | +0.398 | -18.37€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 104751 | +0.199 | -7751.97€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 104751 | +0.199 | -7751.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 18095 | +0.179 | -2045.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 18095 | +0.179 | -2045.59€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 16890 | +0.224 | -570.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 16890 | +0.224 | -570.69€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 17985 | +0.180 | -1923.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 17985 | +0.180 | -1923.76€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 17023 | +0.218 | -684.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 17023 | +0.218 | -684.61€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 17316 | +0.202 | -1111.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 17316 | +0.202 | -1111.26€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 17442 | +0.196 | -1416.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 17442 | +0.196 | -1416.06€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 40285 | +0.117 | +324.68€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 40285 | +0.117 | +324.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 20058 | +0.117 | +197.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 20058 | +0.117 | +197.10€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 20227 | +0.116 | +127.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 20227 | +0.116 | +127.58€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2525 | +0.292 | -12.95€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2525 | +0.292 | -12.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1156 | +0.279 | -35.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1156 | +0.279 | -35.01€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1231 | +0.298 | +17.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1231 | +0.298 | +17.01€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 138 | +0.343 | +5.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 138 | +0.343 | +5.05€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 1160 | +0.440 | -0.58€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 1160 | +0.440 | -0.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 557 | +0.432 | -10.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 557 | +0.432 | -10.69€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 552 | +0.448 | +8.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 552 | +0.448 | +8.85€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 51 | +0.406 | +1.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 51 | +0.406 | +1.25€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1914 | +0.068 | -84.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1189 | +0.081 | -20.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1480 | +0.076 | -39.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1189 | +0.081 | -20.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 81501 | +0.101 | -1960.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 6566 | +0.096 | +130.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 74935 | +0.101 | -2091.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 44572 | +0.105 | -455.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 6566 | +0.096 | +130.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 38006 | +0.107 | -585.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 17258 | +0.109 | -103.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 17258 | +0.109 | -103.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 19671 | +0.082 | -1402.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 19671 | +0.082 | -1402.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ GBM_LATE_15M | 55275 | +0.099 | +30626.78€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 55275 | +0.099 | +30626.78€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 9152 | +0.226 | +7902.36€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 9152 | +0.226 | +7902.36€ | 0 | 22 |
| ✅ GBM_LATE_15M#BTC | 8419 | +0.175 | +6558.97€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 8419 | +0.175 | +6558.97€ | 0 | 22 |
| ✅ GBM_LATE_15M#DOGE | 9928 | +0.207 | +7826.50€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 9928 | +0.207 | +7826.50€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 7458 | +0.052 | +2335.64€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 7458 | +0.052 | +2335.64€ | 1 | 18 |
| ✅ GBM_LATE_15M#SOL | 7730 | -0.032 | +1998.72€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 7730 | -0.032 | +1998.72€ | 4 | 14 |
| ✅ GBM_LATE_15M#XRP | 12588 | -0.023 | +4004.60€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 12588 | -0.023 | +4004.60€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 58137 | +0.085 | +33664.84€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 58137 | +0.085 | +33664.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 11248 | -0.002 | +6034.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 11248 | -0.002 | +6034.37€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 12487 | +0.004 | +3290.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 12487 | +0.004 | +3290.99€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 7941 | +0.294 | +9039.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 7941 | +0.294 | +9039.78€ | 0 | 22 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 11051 | +0.013 | +3405.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 11051 | +0.013 | +3405.37€ | 1 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 8971 | +0.044 | +4004.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 8971 | +0.044 | +4004.17€ | 3 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 6439 | +0.316 | +7890.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 6439 | +0.316 | +7890.16€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 43776 | +0.178 | +36031.14€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 43776 | +0.178 | +36031.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 6581 | +0.240 | +6139.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 6581 | +0.240 | +6139.81€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 6926 | +0.139 | +5097.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 6926 | +0.139 | +5097.08€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 7046 | +0.224 | +6100.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 7046 | +0.224 | +6100.86€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 7498 | +0.129 | +5788.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 7498 | +0.129 | +5788.52€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 8289 | +0.119 | +6191.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 8289 | +0.119 | +6191.25€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 7436 | +0.233 | +6713.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 7436 | +0.233 | +6713.62€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 11841 | +0.126 | +5910.41€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 11841 | +0.126 | +5910.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 468 | +0.157 | +308.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 468 | +0.157 | +308.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3353 | +0.129 | +1818.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3353 | +0.129 | +1818.18€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 505 | +0.159 | +279.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 505 | +0.159 | +279.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 3488 | +0.125 | +1679.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 3488 | +0.125 | +1679.92€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 3006 | +0.096 | +1193.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 3006 | +0.096 | +1193.89€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1021 | +0.169 | +630.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1021 | +0.169 | +630.22€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 55475 | +0.187 | +45461.21€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 55475 | +0.187 | +45461.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 8742 | +0.251 | +8480.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 8742 | +0.251 | +8480.44€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 8784 | +0.137 | +6022.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 8784 | +0.137 | +6022.48€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 9427 | +0.235 | +8517.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 9427 | +0.235 | +8517.55€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 9192 | +0.139 | +6747.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 9192 | +0.139 | +6747.14€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 9860 | +0.121 | +6933.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 9860 | +0.121 | +6933.61€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 9470 | +0.240 | +8759.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 9470 | +0.240 | +8759.99€ | 0 | 21 |
| ✅ GBM_LATE_5M | 13784 | +0.210 | +11172.25€ | 1 | 27 |
| ✅ GBM_LATE_5M#5min | 13784 | +0.210 | +11172.25€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1054 | +0.246 | +1000.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1054 | +0.246 | +1000.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3257 | +0.211 | +2804.80€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3257 | +0.211 | +2804.80€ | 0 | 25 |
| ✅ GBM_LATE_5M#DOGE | 1305 | +0.204 | +1010.70€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1305 | +0.204 | +1010.70€ | 0 | 19 |
| ✅ GBM_LATE_5M#ETH | 4009 | +0.203 | +2999.82€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 4009 | +0.203 | +2999.82€ | 0 | 24 |
| ✅ GBM_LATE_5M#SOL | 2200 | +0.208 | +1819.52€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2200 | +0.208 | +1819.52€ | 0 | 26 |
| ✅ GBM_LATE_5M#XRP | 1959 | +0.209 | +1537.13€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1959 | +0.209 | +1537.13€ | 0 | 0 |
| ✅ GBM_LATE_60M | 4884 | +0.050 | +1330.00€ | 0 | 6 |
| ✅ GBM_LATE_60M#60min | 4884 | +0.050 | +1330.00€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1705 | +0.058 | +526.24€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1705 | +0.058 | +526.24€ | 1 | 5 |
| ✅ GBM_LATE_60M#ETH | 1574 | +0.051 | +485.83€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1574 | +0.051 | +485.83€ | 1 | 6 |
| ✅ GBM_LATE_60M#SOL | 1605 | +0.038 | +317.93€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1605 | +0.038 | +317.93€ | 0 | 9 |
| 🚫 GBM_LATE_60M_FADE | 699 | -0.249 | -35.65€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 699 | -0.249 | -35.65€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 255 | -0.251 | -20.81€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 255 | -0.251 | -20.81€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 257 | -0.241 | -5.52€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 257 | -0.241 | -5.52€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 187 | -0.251 | -9.32€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 187 | -0.251 | -9.32€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 2023 | +0.082 | +527.51€ | 0 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 2023 | +0.082 | +527.51€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 782 | +0.070 | +191.01€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 782 | +0.070 | +191.01€ | 1 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 713 | +0.058 | +140.50€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 713 | +0.058 | +140.50€ | 2 | 13 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 528 | +0.132 | +196.00€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 528 | +0.132 | +196.00€ | 1 | 8 |
| ✅ LATE_WINDOW_5MIN | 225 | +0.293 | +252.39€ | 1 | 13 |
| ✅ LATE_WINDOW_5MIN#5min | 225 | +0.293 | +252.39€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 225 | +0.293 | +252.39€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 225 | +0.293 | +252.39€ | 1 | 13 |
| ✅ LEADLAG_BTC_XRP_15M | 4282 | +0.097 | +971.49€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4282 | +0.097 | +971.49€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4282 | +0.097 | +971.49€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4282 | +0.097 | +971.49€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 1021 | -0.014 | +10.77€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 1021 | -0.014 | +10.77€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 56 | +0.017 | +0.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 56 | +0.017 | +0.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 269 | -0.013 | +5.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 269 | -0.013 | +5.42€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 35 | -0.149 | -5.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 35 | -0.149 | -5.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 273 | +0.016 | +16.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 273 | +0.016 | +16.82€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 306 | -0.013 | +1.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 306 | -0.013 | +1.32€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 82 | -0.083 | -7.78€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 82 | -0.083 | -7.78€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4152 | +0.017 | +126.32€ | 5 | 1 |
| ✅ LIQUIDACIONES_5M#5min | 4152 | +0.017 | +126.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 203 | +0.022 | -1.78€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 203 | +0.022 | -1.78€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 825 | +0.015 | +40.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 825 | +0.015 | +40.47€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 238 | +0.029 | +28.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 238 | +0.029 | +28.31€ | 0 | 2 |
| ✅ LIQUIDACIONES_5M#ETH | 1646 | +0.019 | +27.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1646 | +0.019 | +27.39€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 768 | +0.012 | +2.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 768 | +0.012 | +2.40€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 472 | +0.015 | +29.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 472 | +0.015 | +29.54€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2286 | -0.033 | -10.38€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2286 | -0.033 | -10.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 688 | -0.032 | -12.44€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 688 | -0.032 | -12.44€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 810 | -0.009 | +17.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 810 | -0.009 | +17.93€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 788 | -0.059 | -15.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 788 | -0.059 | -15.86€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 14561 | -0.031 | -116.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 6987 | -0.033 | -75.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 7574 | -0.030 | -41.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 520 | -0.052 | -29.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 264 | -0.023 | +3.43€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 256 | -0.081 | -32.61€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 3803 | -0.025 | -6.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1811 | -0.023 | +3.31€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1992 | -0.026 | -10.10€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1441 | -0.028 | +13.44€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 736 | -0.033 | +0.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 705 | -0.023 | +13.20€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 3285 | -0.033 | -48.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1545 | -0.035 | -31.66€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1740 | -0.031 | -16.42€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 2800 | -0.025 | +27.49€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1355 | -0.029 | -1.54€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1445 | -0.020 | +29.03€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 2712 | -0.042 | -73.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1276 | -0.050 | -49.02€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1436 | -0.035 | -24.74€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 65561 | -0.000 | +3536.25€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 65561 | -0.000 | +3536.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 11869 | +0.027 | +1623.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 11869 | +0.027 | +1623.03€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 9196 | -0.036 | -115.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 9196 | -0.036 | -115.44€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 12004 | +0.025 | +1311.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 12004 | +0.025 | +1311.62€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 9114 | -0.051 | -202.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 9114 | -0.051 | -202.94€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 11168 | -0.004 | +318.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 11168 | -0.004 | +318.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 12210 | +0.017 | +601.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 12210 | +0.017 | +601.29€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7124 | -0.055 | -118.40€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7124 | -0.055 | -118.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1244 | -0.002 | -15.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1244 | -0.002 | -15.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1971 | -0.065 | -28.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1971 | -0.065 | -28.34€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 72 | -0.013 | +0.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 72 | -0.013 | +0.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 807 | -0.119 | -34.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 807 | -0.119 | -34.96€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2168 | -0.068 | -12.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2168 | -0.068 | -12.52€ | 2 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 160898 | -0.078 | +2327.04€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 160898 | -0.078 | +2327.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 28163 | -0.078 | +1631.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 28163 | -0.078 | +1631.25€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 24069 | -0.101 | -1203.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 24069 | -0.101 | -1203.73€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 28519 | -0.068 | +1434.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 28519 | -0.068 | +1434.94€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 23609 | -0.098 | -696.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 23609 | -0.098 | -696.65€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 28777 | -0.058 | +339.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 28777 | -0.058 | +339.63€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 27761 | -0.069 | +821.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 27761 | -0.069 | +821.60€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9015 | -0.035 | -181.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9015 | -0.035 | -181.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1002 | -0.017 | -19.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1002 | -0.017 | -19.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2086 | -0.046 | -26.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2086 | -0.046 | -26.91€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2638 | -0.025 | -38.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2638 | -0.025 | -38.20€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1270 | -0.065 | -32.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1270 | -0.065 | -32.51€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1010 | -0.031 | -32.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1010 | -0.031 | -32.49€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 2105 | +0.119 | +832.96€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 1969 | +0.123 | +820.36€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 471 | +0.132 | +226.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 471 | +0.132 | +226.04€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 401 | +0.118 | +139.50€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 401 | +0.118 | +139.50€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#ETH | 369 | +0.128 | +169.75€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 369 | +0.128 | +169.75€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 337 | +0.143 | +175.10€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 337 | +0.143 | +175.10€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 391 | +0.095 | +109.97€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 391 | +0.095 | +109.97€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 2108 | -0.017 | -23.90€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2108 | -0.017 | -23.90€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 391 | +0.014 | +25.31€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 391 | +0.014 | +25.31€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 386 | -0.049 | -28.84€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 386 | -0.049 | -28.84€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 530 | -0.036 | -28.34€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 530 | -0.036 | -28.34€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 432 | -0.002 | -0.65€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 432 | -0.002 | -0.65€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 369 | -0.007 | +8.61€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 369 | -0.007 | +8.61€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1122 | -0.075 | -43.18€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 516 | -0.108 | -77.10€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 404 | -0.123 | -58.64€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 112 | -0.053 | -18.46€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 394 | -0.035 | +25.03€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 283 | -0.019 | +34.47€ | 2 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 111 | -0.075 | -9.44€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 212 | -0.065 | +8.89€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 176 | -0.062 | +7.05€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 36 | -0.079 | +1.84€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 863 | -0.077 | -17.11€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 259 | -0.067 | -26.07€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1421 | -0.207 | -90.14€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 561 | -0.205 | -49.85€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 494 | -0.204 | -45.54€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 67 | -0.210 | -4.31€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 473 | -0.212 | -39.07€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 415 | -0.222 | -45.98€ | 4 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 58 | -0.133 | +6.91€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 387 | -0.202 | -1.22€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 360 | -0.199 | -3.62€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 27 | -0.224 | +2.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 1269 | -0.209 | -95.14€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 152 | -0.188 | +5.00€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 535 | +0.377 | +503.19€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#BTC | 107 | +0.151 | +88.66€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 107 | +0.151 | +88.66€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#ETH | 123 | +0.364 | +103.53€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 123 | +0.364 | +103.53€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#SOL | 305 | +0.458 | +311.00€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 305 | +0.458 | +311.00€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 535 | +0.377 | +503.19€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 918 | +0.045 | +84.35€ | 2 | 3 |
| ✅ STREAK_FADE_15M#15min | 918 | +0.045 | +84.35€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 345 | +0.030 | +9.90€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 345 | +0.030 | +9.90€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 71 | +0.007 | +0.21€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 71 | +0.007 | +0.21€ | 1 | 1 |
| ✅ STREAK_FADE_15M#SOL | 83 | +0.018 | +6.06€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 83 | +0.018 | +6.06€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 419 | +0.068 | +68.18€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 419 | +0.068 | +68.18€ | 1 | 4 |
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
| ✅ STREAK_MOM_5M | 11481 | +0.014 | +73.45€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11481 | +0.014 | +73.45€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2994 | +0.018 | +23.87€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2994 | +0.018 | +23.87€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2991 | +0.017 | +35.72€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2991 | +0.017 | +35.72€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2917 | +0.008 | -3.28€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2917 | +0.008 | -3.28€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2579 | +0.013 | +17.14€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2579 | +0.013 | +17.14€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 11623 | +0.016 | -22.07€ | 4 | 0 |
| ✅ STRUCT_NO_15M#15min | 11623 | +0.016 | -22.07€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 4822 | +0.021 | +3.88€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 4822 | +0.021 | +3.88€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3989 | +0.015 | -12.21€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3989 | +0.015 | -12.21€ | 4 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2812 | +0.010 | -13.74€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2812 | +0.010 | -13.74€ | 1 | 0 |
| ✅ UPDOWN_GBM | 103057 | +0.060 | +9871.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 25087 | +0.080 | +5159.62€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 3078 | +0.000 | +33.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 68453 | +0.062 | +4569.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 6082 | -0.000 | +112.30€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 8499 | +0.105 | +1574.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1781 | +0.164 | +820.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 6628 | +0.091 | +755.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 23501 | +0.057 | +2070.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 3355 | +0.080 | +762.00€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 872 | +0.001 | +15.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 16420 | +0.066 | +1214.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2724 | -0.003 | +74.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 130 | -0.061 | +4.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 11202 | +0.080 | +1310.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1761 | +0.154 | +738.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 9355 | +0.066 | +573.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 24504 | +0.050 | +1710.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 5932 | +0.072 | +902.42€ | 0 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 840 | +0.005 | +16.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 15379 | +0.051 | +758.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2234 | +0.002 | +31.83€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 119 | -0.103 | +1.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 21992 | +0.040 | +1270.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 6661 | +0.031 | +435.52€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 793 | -0.009 | +5.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 13308 | +0.051 | +831.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1124 | +0.003 | +6.45€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 106 | -0.139 | -7.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 13357 | +0.073 | +1936.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 5597 | +0.095 | +1501.04€ | 0 | 10 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 7363 | +0.060 | +437.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 355 | -0.099 | -1.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 985 | +0.363 | +356.66€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 985 | +0.363 | +356.66€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 485 | +0.362 | +169.66€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 485 | +0.362 | +169.66€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 500 | +0.362 | +187.00€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 500 | +0.362 | +187.00€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 24723 | -0.021 | +6106.80€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 24723 | -0.021 | +6106.80€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 4604 | -0.114 | +232.00€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 4604 | -0.114 | +232.00€ | 3 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1071 | +0.222 | +899.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1071 | +0.222 | +899.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 3233 | +0.219 | +2059.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 3233 | +0.219 | +2059.85€ | 1 | 20 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 6996 | -0.061 | +1038.18€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 6996 | -0.061 | +1038.18€ | 5 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 6838 | -0.061 | +1315.72€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 6838 | -0.061 | +1315.72€ | 2 | 5 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 299 | +0.061 | +23.77€ | 0 | 7 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 299 | +0.061 | +23.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 299 | +0.061 | +23.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 299 | +0.061 | +23.77€ | 0 | 7 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1760 | +0.283 | +1475.06€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1760 | +0.283 | +1475.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 934 | +0.277 | +733.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 934 | +0.277 | +733.65€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 826 | +0.290 | +741.40€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 826 | +0.290 | +741.40€ | 0 | 9 |
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
| ✅ WEEKLY_PRICE | 4560 | +0.303 | +2099.95€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 1730 | +0.260 | +234.76€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1756 | +0.297 | +758.75€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 1074 | +0.381 | +1106.43€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.021 n=1274 — no justifica filtro, seguir monitorizando
  - _Datos_: n=1274 IC=+0.021 PNL=+62.00€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 796 celda(s) pasan gate riguroso completo de 2867 evaluadas (n>=40) y 3990 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.032 < 0.08 — monitorear
  - _Datos_: n=6655 IC=+0.032 PNL=+434.50€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1756/15 IC=+0.297 PNL=+758.75€ | BTC: n=1730/15 IC=+0.260 PNL=+234.76€ | SOL: n=1074/15 IC=+0.381 PNL=+1106.43€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.141 n=1041/60 | contraria IC=+0.184 n=1094 | gap=-0.043 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=575, boost estimado=+0.014. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=2233/40 IC=+0.003 PNL=+32.34€ | BTC#60min: n=2723/40 IC=-0.003 PNL=+74.54€ | SOL#60min: n=1123/40 IC=+0.002 PNL=+5.91€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.045 n=710135 | tras_1loss IC=+0.099 n=538981 | tras_2loss IC=+0.069 n=215993/40 | gap=-0.024 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.167 > 0.08 con n=1020 PNL=+641.76€
  - _Datos_: n=1020 IC=+0.167 PNL=+641.76€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.136 > 0.08 con n=1216 PNL=+589.16€
  - _Datos_: n=1216 IC=+0.136 PNL=+589.16€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.140 > 0.08 con n=84 PNL=+37.51€
  - _Datos_: n=84 IC=+0.140 PNL=+37.51€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.335 > 0.1 con n=3714 PNL=+2080.44€
  - _Datos_: n=3714 IC=+0.335 PNL=+2080.44€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=1043 IC=+0.064 PNL=+99.80€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1043 IC=+0.064 PNL=+99.80€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=104 IC=+0.179 PNL=+68.26€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=104 IC=+0.179 PNL=+68.26€

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
  - _Estado_: n=4074 IC=+0.002 PNL=-14.54€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4074 IC=+0.002 PNL=-14.54€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=2005 IC=-0.004 PNL=+127.32€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=2005 IC=-0.004 PNL=+127.32€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=1274 IC=+0.021 PNL=+62.00€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=1274 IC=+0.021 PNL=+62.00€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.145 > 0.1 con n=6837 PNL=+3537.68€
  - _Datos_: n=6837 IC=+0.145 PNL=+3537.68€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=3354 IC=+0.080 PNL=+762.51€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=3354 IC=+0.080 PNL=+762.51€

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
  - _Estado_: n=1321 IC=+0.036 PNL=+102.06€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=1321 IC=+0.036 PNL=+102.06€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=169 IC=-0.021 PNL=-4.14€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=169 IC=-0.021 PNL=-4.14€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.119 > 0.02 con n=1234 PNL=+498.80€
  - _Datos_: n=1234 IC=+0.119 PNL=+498.80€

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
  - _Estado_: n=42197 IC=+0.074 PNL=+5928.11€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=42197 IC=+0.074 PNL=+5928.11€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.136 < -0.1 con n=732 PNL=+101.66€
  - _Datos_: n=732 IC=-0.136 PNL=+101.66€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=3908 IC=+0.068 PNL=+503.22€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=3908 IC=+0.068 PNL=+503.22€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=184 IC=-0.102 PNL=-0.48€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=184 IC=-0.102 PNL=-0.48€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.102 > 0.1 con n=1070 PNL=+272.18€
  - _Datos_: n=1070 IC=+0.102 PNL=+272.18€

**⏳ H-CUSTOM-ETH15-BUYNO-PRECIO-ALTO** — ETH#15min BUY_NO con precio_yes>0.55 pierde (NO longshot contra favorito)
  - _Hipótesis_: Detectado 2026-07-02: ult.60 shadow ETH15 BUY_NO — py_mkt~0.5 wr=0.67 PNL=+29.3 (n=49); py_mkt 0.6-0.8 wr 0.33-0 PNL=-5.75 (n=9). Filtro RETURN NONE (no SKIP) aplicado en shadow_predict.py (PY_MKT_MAX_BUY_NO_ETH15=0.55) el mismo dia -- bloquea la GENERACIÓN de la fila, no solo la decisión. Esta hipotesis trackea la zona filtrada: si las ops que HABRIAN caido aqui siguen apareciendo en otras estrategias o el IC forward de la zona se vuelve positivo, revisar el filtro. CAVEAT: n=9, muestra chica — el filtro se aplico por asimetria de riesgo (afecta a dinero live), no por significancia. ⚠️ 05-Ago (fix): la clave del filtro decía 'py_mkt', que NUNCA existió ni en features de UPDOWN_GBM (T_h/delta_ratio_macro/drift_15min/drift_60min/pct_spot_vs_ref/sigma_h) ni como columna top-level de results.csv -- corregida a 'precio_yes_mercado' (columna real). Aun así, con la clave correcta esta hipótesis NUNCA podrá acumular n mientras el filtro RETURN NONE siga activo -- es el mismo patrón 'frozen by design' que H-CUSTOM-LATE15-PHOTO-FINISH (más abajo): la propia protección impide generar los datos necesarios para volver a evaluarla. Para monitorearla de verdad haría falta un logger separado que capture la señal SIN aplicar el filtro (mismo patrón que gate_bucket_propio con data/markets histórico) -- no construido, pendiente decisión.
  - _Umbral_: 20
  - _Acción_: Si IC forward de la zona >0 con n>=20 → retirar filtro; si confirma negativo → considerar extender a BTC/SOL 15min
  - _Estado_: 7/20 ops en el filtro definido (IC actual=-0.058 PNL=-1.16€)
  - _Datos_: n=7 IC=-0.058 PNL=-1.16€
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: PY_MKT_MAX_BUY_NO_ETH15=0.55 en shadow_predict.py hace RETURN NONE (bloquea generación, no solo decisión) -- nunca podrá acumular n mientras siga activo. Haría falta un logger separado sin el filtro para monitorear de verdad (no construido, 26-Ago)

**〰️ H-PRECIO-YES-BARATO** — BUY_YES con precio de mercado 0.30-0.40 — mercado infravalora YES
  - _Hipótesis_: Detectado 2026-07-03 en benchmark de calibración del mercado (7d, estrategias GBM): en el bucket precio_yes_mercado [0.3-0.4) la frecuencia real de YES fue 0.45 vs 0.35 implícito (+0.10, n=38). Posible sesgo favorito-longshot suave en binarios de 15min (complemento del LONGSHOT ya activo para BUY_NO con py<0.20). Si se confirma, BUY_YES comprado en esa banda lleva viento de cola estructural del propio mercado, independiente del modelo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → kelly_boost ×1.1 para BUY_YES con precio_yes_mercado en [0.30,0.40), simétrico al longshot BUY_NO existente
  - _Estado_: n=42049 IC=-0.137 PNL=+2724.30€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=42049 IC=-0.137 PNL=+2724.30€

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
  - _Estado_: n=4339 IC=+0.129 PNL=+2807.32€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=4339 IC=+0.129 PNL=+2807.32€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=10594 IC=+0.059 PNL=+944.00€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=10594 IC=+0.059 PNL=+944.00€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.101 > 0.08 con n=4497 PNL=+2544.98€
  - _Datos_: n=4497 IC=+0.101 PNL=+2544.98€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.219 < -0.1 con n=4587 PNL=-366.72€
  - _Datos_: n=4587 IC=-0.219 PNL=-366.72€

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
  - _Estado_: n=102 IC=+0.038 PNL=+16.32€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=102 IC=+0.038 PNL=+16.32€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.096 n=2171) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=2171 IC=+0.096 PNL=+437.17€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.413 n=678) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=678 IC=+0.413 PNL=+987.06€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=18086 IC=+0.179 PNL=-2042.40€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=18086 IC=+0.179 PNL=-2042.40€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.234 > 0.1 con n=284 PNL=+201.16€
  - _Datos_: n=284 IC=+0.234 PNL=+201.16€
