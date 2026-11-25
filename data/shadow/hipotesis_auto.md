# Hipótesis automáticas — 2026-11-25 08:30 UTC
_Generado por shadow_postmortem.py sobre 1488127 resoluciones (PNL=+211117.11€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.239 (n=236)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=725)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.194 (n=1117)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.505 (IC base=+0.123)

- **PATRÓN** `n_total_lado` > `60.0` → IC=+0.173 (n=362)

  - _Acción_: Kelly boost +0.87€ cuando `n_total_lado` > 60.0 (IC base=+0.123)

- **PATRÓN** `banda_hit_calibrado` > `0.8182` → IC=+0.287 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8182 (IC base=+0.123)

- **PATRÓN** `banda_z` > `8.226` → IC=+0.194 (n=351)

  - _Acción_: Kelly boost +0.97€ cuando `banda_z` > 8.226 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.145 (n=387)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=1145)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.123)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.280 (n=171)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=555)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.193 (n=980)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.505 (IC base=+0.125)

- **PATRÓN** `n_total_lado` > `63.0` → IC=+0.181 (n=308)

  - _Acción_: Kelly boost +0.90€ cuando `n_total_lado` > 63.0 (IC base=+0.125)

- **PATRÓN** `banda_hit_calibrado` > `0.8173` → IC=+0.280 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8173 (IC base=+0.125)

- **PATRÓN** `banda_z` > `8.315` → IC=+0.193 (n=307)

  - _Acción_: Kelly boost +0.96€ cuando `banda_z` > 8.315 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.134 (n=935)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 6.0 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.129 (n=1045)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `5101.7817` → IC=+0.131 (n=418)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 5101.7817 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `8596.0083` → IC=+0.127 (n=247)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 8596.0083 (IC base=+0.018)

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
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=109)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=108)

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
- **PATRÓN** `py_entrada` > `0.495` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `py_entrada` > 0.495 (IC base=+0.153)

- **PATRÓN** `n_ballena_banda` > `26.0` → IC=+0.241 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `n_ballena_banda` > 26.0 (IC base=+0.153)

- **PATRÓN** `n_total_lado` > `38.0` → IC=+0.232 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 38.0 (IC base=+0.153)

- **PATRÓN** `banda_hit_calibrado` > `0.6072` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `banda_hit_calibrado` > 0.6072 (IC base=+0.153)

- **PATRÓN** `banda_z` > `2.517` → IC=+0.227 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 2.517 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.225 (n=38)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.154 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.198 (n=41)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.02 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `2738.3784` → IC=+0.203 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2738.3784 (IC base=+0.153)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `130.45` → IC=-0.219 (n=12897)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.45
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=38692)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `122.97` → IC=-0.263 (n=1272)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 122.97
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3816)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `114.34` → IC=-0.279 (n=1281)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 114.34
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=3848)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `115.97` → IC=-0.159 (n=3602)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 115.97
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=10808)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `146.81` → IC=-0.256 (n=3533)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 146.81
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=10602)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `128.04` → IC=-0.267 (n=2359)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.04
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=7078)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.208 (n=30897)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `7761.8428` → IC=+0.151 (n=2509)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 7761.8428 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.128 (n=27447)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.129 (n=33357)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.224 (n=24776)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.137 (n=8915)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `6260.5276` → IC=+0.136 (n=3507)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 6260.5276 (IC base=+0.124)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=2234)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.358 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.174)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.177 (n=2736)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.01 (IC base=+0.174)

- **PATRÓN** `libro_liquidez` > `16195.2715` → IC=+0.182 (n=711)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 16195.2715 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.186 (n=1951)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 7.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.182 (n=2185)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 17.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.328 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.181 (n=2795)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `16011.3723` → IC=+0.185 (n=722)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 16011.3723 (IC base=+0.178)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.169 (n=684)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.61 (IC base=+0.073)

- **PATRÓN** `libro_liquidez` > `6825.0558` → IC=+0.126 (n=153)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 6825.0558 (IC base=+0.073)

- **PATRÓN** `py_entrada` < `0.45` → IC=+0.122 (n=2230)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.45 (IC base=+0.090)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.173 (n=5657)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 6.0 (IC base=+0.169)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.174 (n=2774)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 8.0 (IC base=+0.169)

- **PATRÓN** `py_entrada` > `0.78` → IC=+0.377 (n=1913)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.78 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.200 (n=2714)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.330 (n=1009)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.198 (n=3161)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.193)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.136 (n=1543)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.140 (n=982)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 11.0 (IC base=+0.135)

- **PATRÓN** `py_entrada` > `0.65` → IC=+0.242 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.65 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=1209)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `2042.6788` → IC=+0.138 (n=979)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2042.6788 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `4420.281` → IC=+0.152 (n=156)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4420.281 (IC base=+0.079)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.253 (n=998)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.230)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.230 (n=2046)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.230)

- **PATRÓN** `py_entrada` > `0.84` → IC=+0.428 (n=1345)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.84 (IC base=+0.230)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.145 (n=1488)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 7.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.155 (n=763)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.144)

- **PATRÓN** `py_entrada` < `0.315` → IC=+0.295 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.315 (IC base=+0.144)

### FAVORITO_CONFIRMADO#SOL#60min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.306 (n=153)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.162 (n=486)

- **PATRÓN** `py_entrada` > `0.55` → IC=+0.162 (n=486)

  - _Acción_: Kelly boost +0.81€ cuando `py_entrada` > 0.55 (IC base=+0.049)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.141 (n=550)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.136 (n=1073)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 12.0 (IC base=+0.127)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.255 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.127)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.295 (n=76)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=158)

- **FILTRO** `libro_liquidez` < `8957.4571` → IC=-0.263 (n=175)

  - _Acción_: SKIP cuando `libro_liquidez` < 8957.4571
  - _Potencial_: sin este filtro IC_bueno=-0.238 (n=59)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.197 (n=27449)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.192 (n=17372)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.219 (n=8762)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.338 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `8407.3041` → IC=+0.345 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8407.3041 (IC base=+0.191)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.166 (n=6255)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.160)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.160 (n=3956)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 11.0 (IC base=+0.160)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.174 (n=6036)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.74 (IC base=+0.160)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.210 (n=3872)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.204 (n=2592)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.242 (n=1850)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.203)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.180 (n=6090)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.172 (n=5161)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 15.0 (IC base=+0.172)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.175 (n=6238)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.73 (IC base=+0.172)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.180 (n=4802)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` > 0.71 (IC base=+0.172)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.257 (n=4808)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.252)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.363 (n=1659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.8 (IC base=+0.252)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.252)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=5952)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.189 (n=3785)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 11.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.196 (n=1936)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.73 (IC base=+0.183)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.429 (n=1039)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.425)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.427 (n=1034)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.425)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=1045)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.430 (n=1113)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.425)

- **PATRÓN** `libro_liquidez` > `14011.0969` → IC=+0.450 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14011.0969 (IC base=+0.425)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` < `14.0` → IC=+0.445 (n=381)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.450 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `15243.1529` → IC=+0.444 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15243.1529 (IC base=+0.439)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.428 (n=402)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.421)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.423 (n=399)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.421)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.430 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.421)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.426 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.421)

- **PATRÓN** `libro_liquidez` > `4833.5247` → IC=+0.425 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4833.5247 (IC base=+0.421)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.406 (n=157)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.400)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.419 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.400)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.765` → IC=-0.306 (n=34)

  - _Acción_: SKIP cuando `py_entrada` > 0.765
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=19)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=37)

- **FILTRO** `libro_liquidez` < `6428.7632` → IC=-0.281 (n=39)

  - _Acción_: SKIP cuando `libro_liquidez` < 6428.7632
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=14)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.207 (n=35874)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.238 (n=35307)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.199)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.184 (n=5368)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 18.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.176 (n=11531)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 12.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.184 (n=16564)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.174)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=14955)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.276 (n=6337)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.223)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.189 (n=6158)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.197 (n=12683)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.72 (IC base=+0.180)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.855` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.855
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.229 (n=5024)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.221 (n=5798)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.259 (n=6124)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.218)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `py_entrada` < `0.775` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `libro_liquidez` < `3197.0694` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 3197.0694
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=5922)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.251 (n=6436)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.205)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.203 (n=5982)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.199 (n=5980)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.239 (n=7385)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=12871)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.139 (n=14148)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.28` → IC=+0.140 (n=12007)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 2.28 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=6259)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.143 (n=6428)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.126 (n=8012)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.75` → IC=+0.142 (n=7894)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 3.75 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=6612)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.135 (n=8525)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` > 4.95 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.88` → IC=+0.135 (n=7954)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 2.88 (IC base=+0.116)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.307 (n=1464)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.294)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.390 (n=749)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.294)

- **PATRÓN** `libro_liquidez` > `4014.7683` → IC=+0.295 (n=924)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4014.7683 (IC base=+0.294)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.302 (n=311)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.283)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.370 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `3967.4956` → IC=+0.294 (n=933)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3967.4956 (IC base=+0.283)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.317 (n=714)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.297)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.301 (n=1037)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.297)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.395 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.297)

- **PATRÓN** `libro_liquidez` > `1486.6908` → IC=+0.307 (n=999)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1486.6908 (IC base=+0.297)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` < `16.0` → IC=+0.369 (n=97)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.347)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.393 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.347)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.384 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.347)

- **PATRÓN** `libro_liquidez` > `745.0217` → IC=+0.378 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 745.0217 (IC base=+0.347)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.441 (n=998)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=959)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.438)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.438 (n=1166)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.438)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.440 (n=464)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.439 (n=326)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.434 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.435)

- **PATRÓN** `libro_liquidez` > `5550.9682` → IC=+0.437 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5550.9682 (IC base=+0.435)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.448 (n=324)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.91` → IC=+0.444 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.91 (IC base=+0.441)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.441 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.441)

- **PATRÓN** `libro_liquidez` > `1961.5764` → IC=+0.441 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1961.5764 (IC base=+0.441)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.421 (n=36)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.407)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.397 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.407)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.447 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.407)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.735` → IC=-0.370 (n=44)

  - _Acción_: SKIP cuando `py_entrada` > 0.735
  - _Potencial_: sin este filtro IC_bueno=-0.138 (n=103)

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
- **FILTRO** `py_entrada` > `0.735` → IC=-0.370 (n=44)

  - _Acción_: SKIP cuando `py_entrada` > 0.735
  - _Potencial_: sin este filtro IC_bueno=-0.138 (n=103)

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
- **PATRÓN** `drift_60min` |x|≤ `0.5085` → IC=+0.140 (n=20575)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.5085 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.129 (n=20817)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.126 (n=14330)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.9731` → IC=+0.247 (n=6858)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9731 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `0.8791` → IC=+0.293 (n=1126)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8791 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.461` → IC=+0.190 (n=10320)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 3.461 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.6943` → IC=+0.268 (n=5624)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6943 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.3031` → IC=+0.256 (n=2124)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3031 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.739` → IC=+0.234 (n=4974)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.739 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=9892)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `4925.847` → IC=+0.151 (n=6858)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4925.847 (IC base=+0.124)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.122 (n=13051)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0066 (IC base=+0.088)

- **PATRÓN** `ibs_20min` < `0.564` → IC=+0.145 (n=26060)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.564 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.681` → IC=+0.193 (n=1765)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.681 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` < `0.1789` → IC=+0.195 (n=10700)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.1789 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` < `0.8563` → IC=+0.197 (n=7260)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.8563 (IC base=+0.088)

- **PATRÓN** `volumen_pendiente_norm` > `0.296` → IC=+0.230 (n=2641)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.296 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` > `2.2835` → IC=+0.212 (n=8370)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2835 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.228 (n=18447)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.088)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3042` → IC=+0.213 (n=3840)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3042 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.215 (n=4589)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.213 (n=2924)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.9813` → IC=+0.273 (n=1978)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9813 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.8` → IC=+0.288 (n=1038)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.8 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.2339` → IC=+0.260 (n=760)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2339 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.4379` → IC=+0.213 (n=4194)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4379 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.221 (n=4615)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2054.04` → IC=+0.214 (n=1455)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2054.04 (IC base=+0.211)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.245 (n=1805)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.0968` → IC=+0.271 (n=1325)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0968 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.239 (n=4132)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.245 (n=1830)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.0796` → IC=+0.276 (n=1325)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0796 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.955` → IC=+0.243 (n=4075)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.955 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` < `0.0962` → IC=+0.240 (n=3621)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0962 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2889` → IC=+0.246 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2889 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.554` → IC=+0.238 (n=1676)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.554 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `1.8557` → IC=+0.242 (n=2539)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8557 (IC base=+0.238)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.241 (n=4340)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.238)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.233 (n=1252)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.1156` → IC=+0.245 (n=1646)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1156 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=3923)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` > `0.8901` → IC=+0.251 (n=1247)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8901 (IC base=+0.221)

- **PATRÓN** `dist_vwap_pct` > `0.7553` → IC=+0.235 (n=655)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7553 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.712` → IC=+0.260 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.712 (IC base=+0.221)

- **PATRÓN** `volumen_regimen` > `0.696` → IC=+0.228 (n=3341)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.696 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.2768` → IC=+0.266 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2768 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.4332` → IC=+0.246 (n=1232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4332 (IC base=+0.221)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.158 (n=3619)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0061 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.3625` → IC=+0.144 (n=4111)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3625 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.151 (n=1545)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.7101` → IC=+0.172 (n=4112)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.7101 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.1565` → IC=+0.152 (n=4034)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1565 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.601` → IC=+0.136 (n=647)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 10.601 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.967` → IC=+0.142 (n=3792)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 3.967 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.6283` → IC=+0.158 (n=1371)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.6283 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.0977` → IC=+0.159 (n=1492)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.0977 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.4459` → IC=+0.144 (n=3980)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.4459 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=5341)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.188 (n=1313)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 166.0 (IC base=+0.136)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.212 (n=2102)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0119 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=4872)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.252 (n=1782)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.873` → IC=+0.276 (n=1024)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.873 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` < `0.097` → IC=+0.193 (n=4153)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.097 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.3499` → IC=+0.223 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3499 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.7298` → IC=+0.208 (n=2053)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7298 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=5540)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `1905.8784` → IC=+0.201 (n=2098)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1905.8784 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.227 (n=1925)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.3081` → IC=+0.229 (n=2902)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3081 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.239 (n=1647)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.226 (n=1989)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` < `0.0537` → IC=+0.267 (n=1452)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0537 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.629` → IC=+0.266 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.629 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.3458` → IC=+0.250 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3458 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.1533` → IC=+0.230 (n=2804)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1533 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.223 (n=2041)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `1887.4035` → IC=+0.223 (n=1973)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1887.4035 (IC base=+0.220)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.220 (n=4154)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=+0.220)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.168 (n=257)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=5593)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.141 (n=749)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0041 (IC base=+0.070)

- **PATRÓN** `ibs_20min` > `0.9416` → IC=+0.250 (n=749)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9416 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.1574` → IC=+0.351 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1574 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` < `0.6014` → IC=+0.343 (n=980)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6014 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.222` → IC=+0.217 (n=1647)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.222 (IC base=+0.070)

- **PATRÓN** `volumen_regimen` > `1.2469` → IC=+0.364 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2469 (IC base=+0.070)

- **PATRÓN** `volumen_pendiente_norm` < `0.165` → IC=+0.348 (n=746)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.165 (IC base=+0.070)

- **PATRÓN** `volumen_pendiente_norm` > `0.3009` → IC=+0.358 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3009 (IC base=+0.070)

- **PATRÓN** `volumen_spike_ratio` < `1.4165` → IC=+0.364 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4165 (IC base=+0.070)

- **PATRÓN** `volumen_spike_ratio` > `2.2709` → IC=+0.356 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2709 (IC base=+0.070)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.350 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.070)

- **PATRÓN** `ibs_20min` < `0.0866` → IC=+0.187 (n=1463)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.0866 (IC base=+0.060)

- **PATRÓN** `dist_vwap_pct` > `0.3671` → IC=+0.157 (n=727)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.3671 (IC base=+0.060)

- **PATRÓN** `dist_vwap_pct` < `0.1552` → IC=+0.156 (n=2759)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1552 (IC base=+0.060)

- **PATRÓN** `volumen_regimen` < `0.8265` → IC=+0.163 (n=1927)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8265 (IC base=+0.060)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.193 (n=366)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=+0.060)

- **PATRÓN** `volumen_spike_ratio` > `2.431` → IC=+0.170 (n=929)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.431 (IC base=+0.060)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.183 (n=162)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=903)

- **FILTRO** `ibs_20min` < `0.2727` → IC=-0.179 (n=266)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2727
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=799)

- **FILTRO** `ibs_20min` > `0.1923` → IC=-0.124 (n=5496)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1923
  - _Potencial_: sin este filtro IC_bueno=+0.160 (n=2710)

- **FILTRO** `sigma_ewma_delta_pct` > `8.29` → IC=-0.230 (n=889)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.29
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=7317)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.174 (n=363)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.75 (IC base=+0.019)

- **PATRÓN** `dist_vwap_pct` > `0.9838` → IC=+0.270 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9838 (IC base=+0.019)

- **PATRÓN** `dist_vwap_pct` < `0.6322` → IC=+0.261 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6322 (IC base=+0.019)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.712` → IC=+0.172 (n=169)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 6.712 (IC base=+0.019)

- **PATRÓN** `volumen_regimen` > `1.0067` → IC=+0.321 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0067 (IC base=+0.019)

- **PATRÓN** `volumen_pendiente_norm` < `0.1597` → IC=+0.271 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1597 (IC base=+0.019)

- **PATRÓN** `volumen_spike_ratio` < `2.1712` → IC=+0.276 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1712 (IC base=+0.019)

- **PATRÓN** `ibs_20min` < `0.1923` → IC=+0.160 (n=2710)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1923 (IC base=-0.030)

- **PATRÓN** `dist_vwap_pct` > `0.841` → IC=+0.292 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.841 (IC base=-0.030)

- **PATRÓN** `dist_vwap_pct` < `0.2378` → IC=+0.293 (n=1282)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2378 (IC base=-0.030)

- **PATRÓN** `volumen_regimen` < `0.6932` → IC=+0.306 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6932 (IC base=-0.030)

- **PATRÓN** `volumen_regimen` > `1.0412` → IC=+0.294 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0412 (IC base=-0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.0789` → IC=+0.319 (n=568)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0789 (IC base=-0.030)

- **PATRÓN** `volumen_spike_ratio` < `1.7983` → IC=+0.310 (n=784)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7983 (IC base=-0.030)

- **PATRÓN** `volumen_spike_ratio` > `1.525` → IC=+0.299 (n=1050)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.525 (IC base=-0.030)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7964` → IC=-0.160 (n=4224)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7964
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=2176)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.177 (n=1323)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=5077)

- **FILTRO** `ibs_20min` > `0.7204` → IC=-0.189 (n=2211)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7204
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=6636)

- **PATRÓN** `ibs_20min` > `0.7964` → IC=+0.146 (n=2176)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.7964 (IC base=-0.056)

- **PATRÓN** `dist_vwap_pct` > `0.455` → IC=+0.342 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.455 (IC base=-0.056)

- **PATRÓN** `volumen_regimen` > `0.7043` → IC=+0.319 (n=1168)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7043 (IC base=-0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.3083` → IC=+0.319 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3083 (IC base=-0.056)

- **PATRÓN** `volumen_spike_ratio` > `2.531` → IC=+0.318 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.531 (IC base=-0.056)

- **PATRÓN** `dist_vwap_pct` > `1.1087` → IC=+0.286 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1087 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` < `0.6362` → IC=+0.276 (n=882)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6362 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` > `1.2113` → IC=+0.277 (n=881)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2113 (IC base=+0.008)

- **PATRÓN** `volumen_pendiente_norm` > `0.2915` → IC=+0.279 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2915 (IC base=+0.008)

- **PATRÓN** `volumen_spike_ratio` > `1.4435` → IC=+0.268 (n=2511)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4435 (IC base=+0.008)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.187 (n=9005)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0113 (IC base=+0.086)

- **PATRÓN** `ibs_20min` > `0.8655` → IC=+0.283 (n=12245)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8655 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` > `1.0097` → IC=+0.306 (n=1856)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0097 (IC base=+0.086)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.453` → IC=+0.167 (n=12158)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.453 (IC base=+0.086)

- **PATRÓN** `volumen_regimen` > `0.6927` → IC=+0.279 (n=8991)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6927 (IC base=+0.086)

- **PATRÓN** `volumen_pendiente_norm` > `0.2925` → IC=+0.297 (n=2222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2925 (IC base=+0.086)

- **PATRÓN** `volumen_spike_ratio` > `2.6447` → IC=+0.288 (n=5223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6447 (IC base=+0.086)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.309 (n=15325)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 88.0 (IC base=+0.086)

- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.162 (n=8761)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0108 (IC base=+0.090)

- **PATRÓN** `ibs_20min` < `0.5156` → IC=+0.175 (n=23119)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.5156 (IC base=+0.090)

- **PATRÓN** `dist_vwap_pct` < `0.2066` → IC=+0.284 (n=8986)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2066 (IC base=+0.090)

- **PATRÓN** `volumen_regimen` < `0.6934` → IC=+0.280 (n=3962)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6934 (IC base=+0.090)

- **PATRÓN** `volumen_regimen` > `1.1877` → IC=+0.287 (n=3000)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1877 (IC base=+0.090)

- **PATRÓN** `volumen_pendiente_norm` > `0.2949` → IC=+0.322 (n=1988)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2949 (IC base=+0.090)

- **PATRÓN** `volumen_spike_ratio` < `1.4532` → IC=+0.303 (n=4464)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4532 (IC base=+0.090)

- **PATRÓN** `volumen_spike_ratio` > `2.272` → IC=+0.305 (n=6071)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.272 (IC base=+0.090)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.312 (n=13411)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 71.0 (IC base=+0.090)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8155` → IC=-0.148 (n=4777)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8155
  - _Potencial_: sin este filtro IC_bueno=+0.312 (n=2465)

- **FILTRO** `ibs_20min` > `0.698` → IC=-0.242 (n=1637)

  - _Acción_: SKIP cuando `ibs_20min` > 0.698
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=4913)

- **FILTRO** `sigma_ewma_delta_pct` > `4.054` → IC=-0.238 (n=1372)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.054
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=5178)

- **PATRÓN** `ibs_20min` > `0.8155` → IC=+0.312 (n=2465)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8155 (IC base=+0.009)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.155` → IC=+0.175 (n=2692)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 2.155 (IC base=+0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.2294` → IC=+0.333 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2294 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` < `1.4466` → IC=+0.293 (n=757)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4466 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` > `2.2137` → IC=+0.316 (n=1029)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2137 (IC base=+0.009)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.315 (n=2051)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.009)

- **PATRÓN** `ibs_20min` < `0.1702` → IC=+0.173 (n=1639)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.1702 (IC base=-0.013)

- **PATRÓN** `volumen_pendiente_norm` < `0.1553` → IC=+0.385 (n=1479)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1553 (IC base=-0.013)

- **PATRÓN** `volumen_spike_ratio` < `2.6476` → IC=+0.391 (n=1420)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6476 (IC base=-0.013)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1838` → IC=+0.230 (n=1102)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1838 (IC base=+0.009)

- **PATRÓN** `volumen_regimen` < `1.1961` → IC=+0.215 (n=2636)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1961 (IC base=+0.009)

- **PATRÓN** `volumen_regimen` > `0.6948` → IC=+0.222 (n=2355)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6948 (IC base=+0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.2732` → IC=+0.247 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2732 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` < `1.4147` → IC=+0.230 (n=869)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4147 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` > `2.4483` → IC=+0.221 (n=869)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4483 (IC base=+0.009)

- **PATRÓN** `ballena_activa_n` < `367.0` → IC=+0.233 (n=2604)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 367.0 (IC base=+0.009)

- **PATRÓN** `dist_vwap_pct` < `0.5756` → IC=+0.259 (n=2358)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5756 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` > `0.8353` → IC=+0.265 (n=1311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8353 (IC base=+0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.2697` → IC=+0.285 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2697 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` < `1.5317` → IC=+0.257 (n=843)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5317 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` > `2.1506` → IC=+0.262 (n=867)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1506 (IC base=+0.006)

- **PATRÓN** `ballena_activa_n` < `196.0` → IC=+0.275 (n=848)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 196.0 (IC base=+0.006)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.319 (n=1674)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.294 (n=3700)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.284)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.322 (n=1997)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.574` → IC=+0.305 (n=2506)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.574 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` < `0.1302` → IC=+0.293 (n=3430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1302 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` > `2.1663` → IC=+0.295 (n=2393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1663 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.293 (n=4386)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `2019.0984` → IC=+0.298 (n=1229)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2019.0984 (IC base=+0.284)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.301 (n=2307)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.340 (n=1148)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.307)

- **PATRÓN** `drift_60min` |x|≤ `0.1888` → IC=+0.329 (n=1515)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1888 (IC base=+0.307)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.322 (n=1323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.307)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.312 (n=1565)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.307)

- **PATRÓN** `ibs_20min` < `0.0306` → IC=+0.307 (n=1515)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0306 (IC base=+0.307)

- **PATRÓN** `ibs_20min` > `0.1563` → IC=+0.321 (n=2295)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1563 (IC base=+0.307)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.962` → IC=+0.319 (n=395)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.962 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` < `0.1985` → IC=+0.308 (n=3422)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1985 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` > `0.3447` → IC=+0.312 (n=556)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3447 (IC base=+0.307)

- **PATRÓN** `volumen_spike_ratio` > `2.7414` → IC=+0.325 (n=1514)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7414 (IC base=+0.307)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.308 (n=1625)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.307)

- **PATRÓN** `libro_liquidez` > `1586.9556` → IC=+0.314 (n=3076)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1586.9556 (IC base=+0.307)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.309 (n=2938)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.307)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **PATRÓN** `dist_vwap_pct` > `0.1607` → IC=+0.240 (n=1219)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1607 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.6425` → IC=+0.234 (n=2724)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6425 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `1.1733` → IC=+0.236 (n=2476)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1733 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` > `0.5982` → IC=+0.234 (n=2476)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5982 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` < `0.1618` → IC=+0.236 (n=2600)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1618 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.1024` → IC=+0.242 (n=805)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1024 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `2.4071` → IC=+0.242 (n=2405)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4071 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `114.0` → IC=+0.252 (n=2456)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 114.0 (IC base=+0.025)

- **PATRÓN** `ibs_20min` < `0.092` → IC=+0.151 (n=1705)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.092 (IC base=+0.014)

- **PATRÓN** `dist_vwap_pct` < `0.3902` → IC=+0.262 (n=2018)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3902 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` < `1.176` → IC=+0.264 (n=1819)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.176 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` > `0.6142` → IC=+0.261 (n=1819)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6142 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` < `0.1002` → IC=+0.267 (n=1709)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1002 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` > `0.2812` → IC=+0.284 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2812 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` < `1.7734` → IC=+0.283 (n=1170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7734 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` > `2.4157` → IC=+0.272 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4157 (IC base=+0.014)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.282 (n=1780)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.014)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.75` → IC=-0.249 (n=2765)

  - _Acción_: SKIP cuando `ibs_20min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.317 (n=2785)

- **FILTRO** `ibs_20min` > `0.6038` → IC=-0.236 (n=1308)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6038
  - _Potencial_: sin este filtro IC_bueno=+0.170 (n=3934)

- **FILTRO** `sigma_ewma_delta_pct` > `8.218` → IC=-0.260 (n=602)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.218
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=4640)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.317 (n=2785)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.75 (IC base=+0.035)

- **PATRÓN** `dist_vwap_pct` > `1.1199` → IC=+0.355 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1199 (IC base=+0.035)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.448` → IC=+0.161 (n=2269)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 2.448 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` < `0.8446` → IC=+0.352 (n=1359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8446 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` < `0.0998` → IC=+0.339 (n=1921)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0998 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.370 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` < `1.7945` → IC=+0.358 (n=1323)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7945 (IC base=+0.035)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.354 (n=1791)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.035)

- **PATRÓN** `ibs_20min` < `0.6038` → IC=+0.170 (n=3934)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.6038 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` < `0.2463` → IC=+0.277 (n=2046)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2463 (IC base=+0.068)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.727` → IC=+0.136 (n=4112)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 4.727 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` < `0.6872` → IC=+0.289 (n=911)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6872 (IC base=+0.068)

- **PATRÓN** `volumen_pendiente_norm` > `0.0724` → IC=+0.300 (n=829)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0724 (IC base=+0.068)

- **PATRÓN** `volumen_spike_ratio` < `1.8068` → IC=+0.285 (n=1341)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8068 (IC base=+0.068)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.293 (n=2036)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.068)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.351 (n=2608)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.312)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.315 (n=2941)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.312)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.315 (n=3058)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.312)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.336 (n=2919)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.312)

- **PATRÓN** `dist_vwap_pct` > `0.2211` → IC=+0.336 (n=1549)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2211 (IC base=+0.312)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.764` → IC=+0.340 (n=1151)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.764 (IC base=+0.312)

- **PATRÓN** `volumen_regimen` > `0.6285` → IC=+0.324 (n=2916)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6285 (IC base=+0.312)

- **PATRÓN** `volumen_pendiente_norm` > `0.2866` → IC=+0.344 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2866 (IC base=+0.312)

- **PATRÓN** `volumen_spike_ratio` > `1.5369` → IC=+0.324 (n=2519)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5369 (IC base=+0.312)

- **PATRÓN** `libro_liquidez` > `3002.7004` → IC=+0.321 (n=972)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3002.7004 (IC base=+0.312)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.329 (n=3147)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.313)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.316 (n=3144)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.313)

- **PATRÓN** `ibs_20min` < `0.39` → IC=+0.327 (n=3144)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.39 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` > `1.3123` → IC=+0.321 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.3123 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` < `0.2603` → IC=+0.315 (n=3105)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2603 (IC base=+0.313)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.689` → IC=+0.327 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.689 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` < `0.636` → IC=+0.317 (n=1048)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.636 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` > `1.2104` → IC=+0.340 (n=1048)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2104 (IC base=+0.313)

- **PATRÓN** `volumen_pendiente_norm` > `0.2886` → IC=+0.362 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2886 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` < `1.4153` → IC=+0.324 (n=986)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4153 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` > `2.1571` → IC=+0.318 (n=1340)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1571 (IC base=+0.313)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0128` → IC=+0.219 (n=6583)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0128 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.1275` → IC=+0.194 (n=8677)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1275 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=20515)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.5345` → IC=+0.229 (n=19723)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5345 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.1718` → IC=+0.206 (n=7402)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1718 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.694` → IC=+0.261 (n=3864)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.694 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `1.1736` → IC=+0.152 (n=13163)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1736 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `0.6203` → IC=+0.151 (n=13162)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6203 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.2935` → IC=+0.208 (n=2840)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2935 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.6046` → IC=+0.185 (n=6406)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.6046 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.191 (n=18681)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 85.0 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.193 (n=8719)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0062 (IC base=+0.186)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.187 (n=13194)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0083 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.0862` → IC=+0.223 (n=6591)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0862 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.207 (n=9495)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` < `0.5273` → IC=+0.237 (n=19767)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5273 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` < `0.1988` → IC=+0.180 (n=14450)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.1988 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.369` → IC=+0.190 (n=3100)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 9.369 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.484` → IC=+0.192 (n=17696)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 2.484 (IC base=+0.186)

- **PATRÓN** `volumen_regimen` < `0.6996` → IC=+0.175 (n=6158)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6996 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.2957` → IC=+0.216 (n=2958)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2957 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` < `1.5641` → IC=+0.185 (n=8324)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.5641 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `2.6397` → IC=+0.196 (n=6306)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6397 (IC base=+0.186)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.199 (n=18749)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 89.0 (IC base=+0.186)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.0757` → IC=+0.268 (n=1079)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0757 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.236 (n=3379)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.229)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.230 (n=2194)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` > `0.8131` → IC=+0.270 (n=2887)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8131 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.46` → IC=+0.327 (n=1062)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.46 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` > `0.2317` → IC=+0.284 (n=622)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2317 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` < `1.8293` → IC=+0.226 (n=2063)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8293 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` > `1.4343` → IC=+0.229 (n=3096)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4343 (IC base=+0.229)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=3435)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.229)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.254 (n=2756)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.251)

- **PATRÓN** `drift_60min` |x|≤ `0.1018` → IC=+0.308 (n=1212)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1018 (IC base=+0.251)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.256 (n=2832)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.251)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.256 (n=2506)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.251)

- **PATRÓN** `ibs_20min` < `0.0068` → IC=+0.309 (n=919)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0068 (IC base=+0.251)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.947` → IC=+0.257 (n=2726)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.947 (IC base=+0.251)

- **PATRÓN** `volumen_pendiente_norm` < `0.0741` → IC=+0.255 (n=2299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0741 (IC base=+0.251)

- **PATRÓN** `volumen_pendiente_norm` > `0.3015` → IC=+0.262 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3015 (IC base=+0.251)

- **PATRÓN** `volumen_spike_ratio` < `1.5528` → IC=+0.265 (n=1165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5528 (IC base=+0.251)

- **PATRÓN** `volumen_spike_ratio` > `2.6858` → IC=+0.254 (n=883)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6858 (IC base=+0.251)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.261 (n=1848)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.251)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.191 (n=1008)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0033 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.0944` → IC=+0.169 (n=1330)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.0944 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=3154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.2457` → IC=+0.201 (n=3023)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2457 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.1981` → IC=+0.211 (n=1460)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1981 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.538` → IC=+0.204 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.538 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8521` → IC=+0.133 (n=2016)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.8521 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` > `1.1931` → IC=+0.130 (n=1008)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 1.1931 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2757` → IC=+0.170 (n=459)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2757 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.5085` → IC=+0.129 (n=1311)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.5085 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.4541` → IC=+0.140 (n=993)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 2.4541 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `384.0` → IC=+0.130 (n=2948)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 384.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.182 (n=2891)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0061 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.2603` → IC=+0.176 (n=2888)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2603 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.177 (n=1567)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 15.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` < `0.6153` → IC=+0.210 (n=3280)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6153 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` < `0.2251` → IC=+0.176 (n=3564)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.2251 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.885` → IC=+0.177 (n=602)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 10.885 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.013` → IC=+0.157 (n=2889)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 4.013 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `1.2053` → IC=+0.163 (n=3280)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2053 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` < `0.0968` → IC=+0.156 (n=2884)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.0968 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `2.1477` → IC=+0.159 (n=2774)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1477 (IC base=+0.154)

- **PATRÓN** `ballena_activa_n` < `202.0` → IC=+0.197 (n=1358)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 202.0 (IC base=+0.154)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.012` → IC=+0.231 (n=1509)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.012 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.2576` → IC=+0.234 (n=2221)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2576 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.219 (n=3486)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.286 (n=1764)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.981` → IC=+0.304 (n=790)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.981 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.3494` → IC=+0.236 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3494 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.7134` → IC=+0.221 (n=1476)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7134 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.213 (n=3992)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2017.401` → IC=+0.221 (n=1110)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2017.401 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.244 (n=2664)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0112 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.1416` → IC=+0.275 (n=1332)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1416 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.272 (n=1146)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.0445` → IC=+0.289 (n=1332)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0445 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.722` → IC=+0.279 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.722 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.3531` → IC=+0.278 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3531 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.7663` → IC=+0.240 (n=1292)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7663 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.1795` → IC=+0.248 (n=1957)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1795 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1881.0154` → IC=+0.248 (n=1372)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1881.0154 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.235 (n=2911)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.237)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.193 (n=1087)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.004 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.0826` → IC=+0.172 (n=1086)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.0826 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=3374)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.2432` → IC=+0.188 (n=3255)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.2432 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.1493` → IC=+0.189 (n=1828)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1493 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.175` → IC=+0.200 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.175 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.8362` → IC=+0.139 (n=2171)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.8362 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2867` → IC=+0.179 (n=490)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2867 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.515` → IC=+0.124 (n=1403)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.515 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `2.4982` → IC=+0.138 (n=1063)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.4982 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `6891.5439` → IC=+0.196 (n=1476)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 6891.5439 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `123.0` → IC=+0.128 (n=3197)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 123.0 (IC base=+0.127)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.161 (n=3074)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0071 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.4328` → IC=+0.151 (n=3493)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4328 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.165 (n=1676)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.6687` → IC=+0.189 (n=3493)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.6687 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` < `0.1739` → IC=+0.157 (n=3585)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1739 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.5` → IC=+0.142 (n=1189)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 6.5 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.851` → IC=+0.153 (n=2330)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.851 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.2377` → IC=+0.164 (n=719)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.2377 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `2.1878` → IC=+0.136 (n=2931)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.1878 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.4074` → IC=+0.136 (n=3329)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4074 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `6679.82` → IC=+0.191 (n=1584)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 6679.82 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.156 (n=1128)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 48.0 (IC base=+0.134)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0131` → IC=+0.175 (n=1210)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0131 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=3731)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.205 (n=3634)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4706 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.8033` → IC=+0.212 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8033 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.884` → IC=+0.283 (n=760)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.884 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `1.1668` → IC=+0.131 (n=3627)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1668 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.6239` → IC=+0.124 (n=3627)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.6239 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1631` → IC=+0.124 (n=3702)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1631 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2819` → IC=+0.130 (n=504)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` > 0.2819 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.5443` → IC=+0.128 (n=1550)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.5443 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2714.6923` → IC=+0.199 (n=1644)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2714.6923 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.127 (n=2348)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 27.0 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0113` → IC=+0.154 (n=3363)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0113 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.1194` → IC=+0.172 (n=1274)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1194 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.140 (n=3893)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.6429` → IC=+0.223 (n=3819)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6429 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` < `0.2305` → IC=+0.149 (n=3795)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.2305 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.225` → IC=+0.148 (n=3388)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 2.225 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `1.1804` → IC=+0.131 (n=3818)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.1804 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` > `0.8584` → IC=+0.126 (n=2546)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.8584 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` < `0.1643` → IC=+0.128 (n=3783)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1643 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2784` → IC=+0.149 (n=533)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2784 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.4407` → IC=+0.143 (n=1211)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4407 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.4653` → IC=+0.139 (n=1210)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 2.4653 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `2613.7824` → IC=+0.192 (n=1731)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2613.7824 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.135 (n=3606)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 42.0 (IC base=+0.126)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.248 (n=2911)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0124 (IC base=+0.225)

- **PATRÓN** `drift_60min` |x|≤ `0.1692` → IC=+0.239 (n=1434)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1692 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.230 (n=3391)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=2942)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `0.6656` → IC=+0.254 (n=3258)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6656 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` > `0.1879` → IC=+0.232 (n=1997)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1879 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` < `0.8443` → IC=+0.227 (n=3373)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8443 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.436` → IC=+0.272 (n=800)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.436 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` > `0.6171` → IC=+0.233 (n=3260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6171 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.2895` → IC=+0.270 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2895 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `1.4372` → IC=+0.228 (n=3181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4372 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.226 (n=4199)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `2621.4552` → IC=+0.229 (n=2172)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2621.4552 (IC base=+0.225)

- **PATRÓN** `sigma_h` > `0.0161` → IC=+0.247 (n=2267)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0161 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.6207` → IC=+0.249 (n=3400)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6207 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.250 (n=1672)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.243 (n=1537)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.0388` → IC=+0.298 (n=1496)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0388 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` > `1.1974` → IC=+0.249 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1974 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.994` → IC=+0.271 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.994 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` < `0.8643` → IC=+0.245 (n=2267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8643 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` > `1.0472` → IC=+0.240 (n=1541)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0472 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.300 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.855` → IC=+0.236 (n=2152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.855 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `1.5577` → IC=+0.239 (n=2881)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5577 (IC base=+0.238)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.204 (n=1737)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.145` → IC=+0.169 (n=2287)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.145 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.165 (n=5437)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.4133` → IC=+0.199 (n=4646)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4133 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.9188` → IC=+0.177 (n=788)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.9188 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.538` → IC=+0.208 (n=834)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.538 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `0.8553` → IC=+0.162 (n=3164)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8553 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` > `1.1862` → IC=+0.159 (n=1581)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 1.1862 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.1554` → IC=+0.171 (n=1337)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1554 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.5271` → IC=+0.158 (n=2233)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.5271 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `1.8073` → IC=+0.155 (n=3383)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.8073 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.156 (n=5715)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.02 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `7247.6703` → IC=+0.191 (n=2357)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 7247.6703 (IC base=+0.154)

- **PATRÓN** `ibs_20min` < `0.5911` → IC=+0.153 (n=5026)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.5911 (IC base=+0.101)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.144 (n=2519)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 22.0 (IC base=+0.101)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.212 (n=848)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.194)

- **PATRÓN** `drift_60min` |x|≤ `0.0802` → IC=+0.236 (n=422)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0802 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.226 (n=1142)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `0.6148` → IC=+0.255 (n=843)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6148 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` > `0.6892` → IC=+0.238 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6892 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.849` → IC=+0.228 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.849 (IC base=+0.194)

- **PATRÓN** `volumen_regimen` < `0.6238` → IC=+0.224 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6238 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.0895` → IC=+0.213 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0895 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` < `2.1509` → IC=+0.207 (n=1093)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1509 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `1.4021` → IC=+0.196 (n=1242)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4021 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `13762.5784` → IC=+0.204 (n=843)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13762.5784 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.150 (n=701)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0037 (IC base=+0.071)

- **PATRÓN** `ibs_20min` < `0.2185` → IC=+0.186 (n=699)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.2185 (IC base=+0.071)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.173 (n=686)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 166.0 (IC base=+0.071)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.239 (n=535)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.1334` → IC=+0.158 (n=703)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1334 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=1660)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` > `0.765` → IC=+0.257 (n=725)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.765 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.157` → IC=+0.166 (n=759)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.157 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.954` → IC=+0.183 (n=225)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 9.954 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `0.8304` → IC=+0.154 (n=1066)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8304 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.2175` → IC=+0.187 (n=279)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2175 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `1.7714` → IC=+0.159 (n=1051)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.7714 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `7831.4295` → IC=+0.174 (n=725)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 7831.4295 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.142 (n=529)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 30.0 (IC base=+0.143)

- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.123 (n=1597)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0081 (IC base=+0.110)

- **PATRÓN** `ibs_20min` < `0.4108` → IC=+0.182 (n=1065)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.4108 (IC base=+0.110)

- **PATRÓN** `volumen_regimen` < `0.6748` → IC=+0.140 (n=704)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.6748 (IC base=+0.110)

- **PATRÓN** `volumen_pendiente_norm` > `0.2224` → IC=+0.137 (n=271)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.2224 (IC base=+0.110)

- **PATRÓN** `volumen_spike_ratio` < `1.3987` → IC=+0.139 (n=519)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.3987 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `5563.2153` → IC=+0.148 (n=1065)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 5563.2153 (IC base=+0.110)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.148 (n=686)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 40.0 (IC base=+0.110)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.151 (n=468)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0072 (IC base=+0.120)

- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.131 (n=467)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` > 0.0129 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.139 (n=1404)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 6.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` > `0.5333` → IC=+0.187 (n=1255)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.5333 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `0.5074` → IC=+0.145 (n=446)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.5074 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.862` → IC=+0.227 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.862 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.0438` → IC=+0.129 (n=1233)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.0438 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2221` → IC=+0.143 (n=239)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.2221 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.4182` → IC=+0.149 (n=454)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4182 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.121 (n=1418)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `3055.1957` → IC=+0.150 (n=467)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3055.1957 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.6809` → IC=+0.148 (n=1555)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.6809 (IC base=+0.084)

- **PATRÓN** `libro_liquidez` > `2761.0504` → IC=+0.166 (n=705)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2761.0504 (IC base=+0.084)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0146` → IC=+0.236 (n=320)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0146 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.3166` → IC=+0.175 (n=321)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.3166 (IC base=+0.173)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.217 (n=224)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` < `0.8448` → IC=+0.173 (n=423)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.8448 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.3805` → IC=+0.187 (n=480)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.3805 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.2422` → IC=+0.188 (n=229)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.2422 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.534` → IC=+0.188 (n=482)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 5.534 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `1.1972` → IC=+0.253 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1972 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` < `0.2469` → IC=+0.191 (n=516)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.2469 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.0806` → IC=+0.191 (n=176)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.0806 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` < `2.5077` → IC=+0.193 (n=451)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.5077 (IC base=+0.173)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.190 (n=485)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.03 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `2678.1143` → IC=+0.199 (n=320)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2678.1143 (IC base=+0.173)

- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.177 (n=537)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0105 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.5762` → IC=+0.169 (n=472)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.5762 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.214 (n=180)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.174 (n=474)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.5 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `0.1848` → IC=+0.168 (n=480)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.1848 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `1.2297` → IC=+0.300 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2297 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.028` → IC=+0.165 (n=521)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 3.028 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `1.2424` → IC=+0.183 (n=537)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 1.2424 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` < `0.1149` → IC=+0.179 (n=503)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` < 0.1149 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.2409` → IC=+0.198 (n=94)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2409 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `1.4975` → IC=+0.214 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4975 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` > `2.6655` → IC=+0.180 (n=173)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 2.6655 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `2230.8308` → IC=+0.166 (n=480)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2230.8308 (IC base=+0.163)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.177 (n=518)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 19.0 (IC base=+0.163)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.227 (n=8706)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0129 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=27255)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.9655` → IC=+0.299 (n=8707)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9655 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.9587` → IC=+0.218 (n=2996)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9587 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.866` → IC=+0.260 (n=6388)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.866 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `0.8667` → IC=+0.162 (n=11731)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8667 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2406` → IC=+0.215 (n=4650)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2406 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6276` → IC=+0.193 (n=8504)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6276 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.200 (n=24738)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.208 (n=8115)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.1137` → IC=+0.203 (n=8112)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1137 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.217 (n=9095)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.594` → IC=+0.245 (n=24319)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.594 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` < `0.1942` → IC=+0.183 (n=15558)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.1942 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.333` → IC=+0.204 (n=23829)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.333 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `0.864` → IC=+0.179 (n=10863)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.864 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.2938` → IC=+0.254 (n=3338)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2938 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `2.6269` → IC=+0.211 (n=7804)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6269 (IC base=+0.199)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.214 (n=23236)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.199)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3826` → IC=+0.235 (n=4156)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3826 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.240 (n=4367)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.235 (n=2796)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` > `0.8601` → IC=+0.292 (n=2770)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8601 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.038` → IC=+0.299 (n=2735)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.038 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2321` → IC=+0.289 (n=736)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2321 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.2784` → IC=+0.243 (n=1825)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2784 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.246 (n=4377)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `2054.47` → IC=+0.238 (n=1385)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2054.47 (IC base=+0.234)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.266 (n=3825)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0109 (IC base=+0.264)

- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.265 (n=1733)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.264)

- **PATRÓN** `drift_60min` |x|≤ `0.1294` → IC=+0.291 (n=1682)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1294 (IC base=+0.264)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.266 (n=3963)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.264)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.267 (n=3445)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.264)

- **PATRÓN** `ibs_20min` < `0.4698` → IC=+0.286 (n=3362)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4698 (IC base=+0.264)

- **PATRÓN** `volumen_pendiente_norm` < `0.0988` → IC=+0.267 (n=3485)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0988 (IC base=+0.264)

- **PATRÓN** `volumen_pendiente_norm` > `0.292` → IC=+0.285 (n=533)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.292 (IC base=+0.264)

- **PATRÓN** `volumen_spike_ratio` < `1.5651` → IC=+0.266 (n=1620)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5651 (IC base=+0.264)

- **PATRÓN** `volumen_spike_ratio` > `2.6427` → IC=+0.271 (n=1228)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6427 (IC base=+0.264)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.271 (n=2552)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.264)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.272 (n=1232)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 6.0 (IC base=+0.264)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.172 (n=1432)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0034 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.0841` → IC=+0.147 (n=1434)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.0841 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.152 (n=4476)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.1887` → IC=+0.187 (n=4294)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.1887 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.7398` → IC=+0.212 (n=731)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7398 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.003` → IC=+0.175 (n=674)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 11.003 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.6329` → IC=+0.156 (n=1432)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6329 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `1.2204` → IC=+0.142 (n=1432)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.2204 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2716` → IC=+0.191 (n=599)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2716 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.1654` → IC=+0.143 (n=3719)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.1654 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.5201` → IC=+0.145 (n=3775)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.5201 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `351.0` → IC=+0.148 (n=3672)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 351.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.170 (n=3347)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0061 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.0841` → IC=+0.172 (n=1268)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.0841 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=1405)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.6821` → IC=+0.191 (n=3805)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.6821 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.1571` → IC=+0.163 (n=3743)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1571 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.0` → IC=+0.148 (n=1787)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 3.0 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.205` → IC=+0.151 (n=3886)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 6.205 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.0413` → IC=+0.157 (n=3347)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.0413 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.2217` → IC=+0.198 (n=693)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2217 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.4321` → IC=+0.152 (n=3692)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4321 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.7751` → IC=+0.153 (n=2461)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.7751 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=4940)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `212.0` → IC=+0.181 (n=1222)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 212.0 (IC base=+0.147)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.242 (n=1967)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=4556)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.298 (n=1605)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.908` → IC=+0.314 (n=965)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.908 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.3486` → IC=+0.234 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3486 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.7631` → IC=+0.238 (n=1928)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7631 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.229 (n=5183)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `1904.2584` → IC=+0.238 (n=1967)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1904.2584 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.248 (n=1854)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.244)

- **PATRÓN** `drift_60min` |x|≤ `0.1863` → IC=+0.259 (n=1851)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1863 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.261 (n=1595)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.247 (n=1931)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` < `0.0693` → IC=+0.296 (n=1402)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0693 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.871` → IC=+0.304 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.871 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` > `0.3457` → IC=+0.295 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3457 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `2.1697` → IC=+0.256 (n=2715)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1697 (IC base=+0.244)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.249 (n=1985)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.244)

- **PATRÓN** `libro_liquidez` > `2000.6` → IC=+0.251 (n=1402)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2000.6 (IC base=+0.244)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.246 (n=4023)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.244)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.190 (n=1506)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.004 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.3573` → IC=+0.148 (n=3970)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3573 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.152 (n=4688)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.8757` → IC=+0.265 (n=1504)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8757 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.1512` → IC=+0.170 (n=2217)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1512 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.963` → IC=+0.162 (n=1968)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 2.963 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.8566` → IC=+0.153 (n=3008)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8566 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.2321` → IC=+0.201 (n=793)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2321 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `1.5167` → IC=+0.155 (n=1941)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.5167 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `2.1497` → IC=+0.144 (n=2000)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.1497 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `5881.5817` → IC=+0.231 (n=2045)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5881.5817 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.142 (n=2941)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 85.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.170 (n=3831)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0083 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.4638` → IC=+0.162 (n=3829)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.4638 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=1410)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.5719` → IC=+0.213 (n=3369)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5719 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.6435` → IC=+0.159 (n=4437)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.6435 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.056` → IC=+0.158 (n=762)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 9.056 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.033` → IC=+0.155 (n=3339)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 3.033 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `0.8502` → IC=+0.163 (n=2553)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8502 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.2899` → IC=+0.206 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2899 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.4824` → IC=+0.157 (n=3712)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.4824 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.5218` → IC=+0.159 (n=3316)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.5218 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `6741.2976` → IC=+0.215 (n=1276)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6741.2976 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.173 (n=1273)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 57.0 (IC base=+0.153)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.154 (n=1532)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0132 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.149 (n=3251)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.6949` → IC=+0.256 (n=3063)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6949 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `0.8173` → IC=+0.195 (n=1016)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.8173 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.192` → IC=+0.269 (n=1173)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.192 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `1.2098` → IC=+0.126 (n=4596)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.2098 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` < `0.1013` → IC=+0.123 (n=4375)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1013 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.2794` → IC=+0.143 (n=575)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.2794 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `1.5602` → IC=+0.133 (n=1976)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.5602 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2472.9793` → IC=+0.224 (n=2083)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2472.9793 (IC base=+0.121)

- **PATRÓN** `sigma_h` < `0.0113` → IC=+0.161 (n=3780)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0113 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.1438` → IC=+0.154 (n=1431)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1438 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.171 (n=2031)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 15.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.5408` → IC=+0.247 (n=3778)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5408 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.2286` → IC=+0.154 (n=3965)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.2286 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.019` → IC=+0.162 (n=4173)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 3.019 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.1927` → IC=+0.144 (n=4293)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.1927 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.232` → IC=+0.199 (n=749)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.232 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.4384` → IC=+0.165 (n=1367)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.4384 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.4912` → IC=+0.146 (n=1367)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 2.4912 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `2653.9292` → IC=+0.224 (n=1431)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2653.9292 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.152 (n=4154)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 48.0 (IC base=+0.138)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.255 (n=4198)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.241 (n=4393)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.240 (n=2811)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` > `0.9873` → IC=+0.302 (n=1400)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9873 (IC base=+0.235)

- **PATRÓN** `dist_vwap_pct` > `0.2049` → IC=+0.251 (n=2123)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2049 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.943` → IC=+0.297 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.943 (IC base=+0.235)

- **PATRÓN** `volumen_regimen` < `1.2153` → IC=+0.236 (n=4198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2153 (IC base=+0.235)

- **PATRÓN** `volumen_regimen` > `0.6408` → IC=+0.242 (n=4197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6408 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.2415` → IC=+0.258 (n=726)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2415 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.5218` → IC=+0.255 (n=1371)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5218 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=5394)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `2643.9324` → IC=+0.239 (n=2798)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2643.9324 (IC base=+0.235)

- **PATRÓN** `sigma_h` > `0.0247` → IC=+0.272 (n=1457)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0247 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.251 (n=4106)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.14` → IC=+0.304 (n=1931)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.14 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` > `1.1991` → IC=+0.251 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1991 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` < `0.2331` → IC=+0.249 (n=4214)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2331 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.929` → IC=+0.281 (n=814)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.929 (IC base=+0.245)

- **PATRÓN** `volumen_regimen` < `0.6365` → IC=+0.248 (n=1457)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6365 (IC base=+0.245)

- **PATRÓN** `volumen_regimen` > `1.2188` → IC=+0.266 (n=1458)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2188 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.2882` → IC=+0.310 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2882 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `1.4345` → IC=+0.248 (n=4154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4345 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.245 (n=3597)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.245)

### GBM_LATE_5M
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.241 (n=2484)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.225)

- **PATRÓN** `drift_60min` |x|≤ `0.5394` → IC=+0.233 (n=7431)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5394 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=7455)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `0.9282` → IC=+0.258 (n=2477)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9282 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` < `0.9671` → IC=+0.228 (n=6085)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9671 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.432` → IC=+0.235 (n=2480)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.432 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` < `0.7054` → IC=+0.230 (n=2319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7054 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` > `0.8787` → IC=+0.228 (n=3513)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8787 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.164` → IC=+0.235 (n=2086)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.164 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` < `1.4491` → IC=+0.235 (n=2437)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4491 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.229 (n=5311)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `3756.477` → IC=+0.233 (n=4954)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3756.477 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.230 (n=1777)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.212)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.212 (n=2413)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.4179` → IC=+0.222 (n=4675)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4179 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.226 (n=1789)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.224 (n=2403)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.6151` → IC=+0.215 (n=4675)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6151 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.7161` → IC=+0.219 (n=912)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7161 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` < `0.2571` → IC=+0.204 (n=4678)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2571 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.683` → IC=+0.225 (n=4825)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.683 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `1.2515` → IC=+0.211 (n=4818)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2515 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` < `0.0981` → IC=+0.214 (n=4909)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0981 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.5317` → IC=+0.216 (n=2302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5317 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `1.8163` → IC=+0.218 (n=3488)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8163 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.237 (n=3503)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 50.0 (IC base=+0.212)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.278 (n=841)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.273)

- **PATRÓN** `drift_60min` |x|≤ `0.0857` → IC=+0.304 (n=319)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0857 (IC base=+0.273)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.282 (n=956)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.273)

- **PATRÓN** `ibs_20min` < `0.4661` → IC=+0.287 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4661 (IC base=+0.273)

- **PATRÓN** `dist_vwap_pct` < `0.3337` → IC=+0.284 (n=973)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3337 (IC base=+0.273)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.122` → IC=+0.298 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.122 (IC base=+0.273)

- **PATRÓN** `volumen_regimen` < `1.2269` → IC=+0.277 (n=955)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2269 (IC base=+0.273)

- **PATRÓN** `volumen_regimen` > `0.8786` → IC=+0.293 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8786 (IC base=+0.273)

- **PATRÓN** `volumen_pendiente_norm` > `0.2862` → IC=+0.341 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2862 (IC base=+0.273)

- **PATRÓN** `volumen_spike_ratio` < `2.4907` → IC=+0.281 (n=950)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4907 (IC base=+0.273)

- **PATRÓN** `libro_liquidez` > `12917.5095` → IC=+0.284 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12917.5095 (IC base=+0.273)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.263 (n=516)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.3891` → IC=+0.186 (n=1548)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.3891 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=569)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.175 (n=582)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 5.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` < `0.1382` → IC=+0.191 (n=681)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.1382 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` > `0.3609` → IC=+0.175 (n=333)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.3609 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` < `0.5549` → IC=+0.171 (n=1854)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.5549 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.329` → IC=+0.193 (n=1521)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 6.329 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `1.091` → IC=+0.184 (n=1361)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 1.091 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.1518` → IC=+0.187 (n=474)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.1518 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `2.4957` → IC=+0.177 (n=1539)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 2.4957 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `1.8071` → IC=+0.174 (n=1026)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.8071 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `14616.0048` → IC=+0.171 (n=702)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 14616.0048 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `701.0` → IC=+0.187 (n=1503)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 701.0 (IC base=+0.171)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `drift_60min` |x|≤ `0.6134` → IC=+0.217 (n=1086)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6134 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.230 (n=983)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` < `0.7107` → IC=+0.218 (n=724)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7107 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.988` → IC=+0.253 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.988 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.256` → IC=+0.247 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.256 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.2053` → IC=+0.248 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2053 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.7957` → IC=+0.218 (n=967)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7957 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.221 (n=968)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.211)

- **PATRÓN** `sigma_h` > `0.0144` → IC=+0.343 (n=49)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0144 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.312 (n=110)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.288)

- **PATRÓN** `ibs_20min` < `0.4444` → IC=+0.300 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4444 (IC base=+0.288)

- **PATRÓN** `ibs_20min` > `0.1912` → IC=+0.300 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1912 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.025` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.025 (IC base=+0.288)

- **PATRÓN** `volumen_pendiente_norm` < `0.1188` → IC=+0.327 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1188 (IC base=+0.288)

- **PATRÓN** `volumen_spike_ratio` < `2.3165` → IC=+0.311 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3165 (IC base=+0.288)

- **PATRÓN** `volumen_spike_ratio` > `1.8484` → IC=+0.296 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8484 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `3226.1026` → IC=+0.363 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3226.1026 (IC base=+0.288)

- **PATRÓN** `ballena_activa_n` < `5.0` → IC=+0.368 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 5.0 (IC base=+0.288)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.223 (n=1805)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0076 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.474` → IC=+0.220 (n=2045)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.474 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.241 (n=716)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` < `0.4702` → IC=+0.229 (n=1364)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4702 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `0.8316` → IC=+0.217 (n=683)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8316 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` < `0.4266` → IC=+0.225 (n=2050)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4266 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.936` → IC=+0.222 (n=1859)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.936 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` < `0.8663` → IC=+0.217 (n=1364)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8663 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` > `1.2312` → IC=+0.221 (n=682)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2312 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` < `0.0987` → IC=+0.216 (n=1895)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0987 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.1592` → IC=+0.217 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1592 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` < `1.403` → IC=+0.232 (n=666)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.403 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `1.4939` → IC=+0.215 (n=1784)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4939 (IC base=+0.214)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.244 (n=553)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.5118` → IC=+0.221 (n=1659)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5118 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.217 (n=620)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.222 (n=751)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `0.0842` → IC=+0.215 (n=1659)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0842 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `0.7273` → IC=+0.223 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7273 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.231` → IC=+0.212 (n=1510)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.231 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` < `1.1021` → IC=+0.213 (n=1460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1021 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` > `0.7208` → IC=+0.212 (n=1482)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7208 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.0724` → IC=+0.230 (n=686)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0724 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` < `2.1617` → IC=+0.209 (n=1429)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1617 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `1.7691` → IC=+0.210 (n=1082)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7691 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.210 (n=2168)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.208)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.212 (n=1651)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 96.0 (IC base=+0.208)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.229 (n=864)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.217)

- **PATRÓN** `sigma_h` > `0.0135` → IC=+0.228 (n=432)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0135 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.247 (n=1158)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` > `0.9855` → IC=+0.300 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9855 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` > `1.1022` → IC=+0.246 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1022 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.982` → IC=+0.270 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.982 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` < `0.6422` → IC=+0.246 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6422 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` < `0.1056` → IC=+0.220 (n=1185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1056 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.2735` → IC=+0.240 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2735 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` < `2.5042` → IC=+0.226 (n=1264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5042 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.226 (n=1517)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `3371.442` → IC=+0.243 (n=1158)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3371.442 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.222 (n=1123)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.217)

- **PATRÓN** `sigma_h` < `0.0141` → IC=+0.246 (n=973)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0141 (IC base=+0.246)

- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.252 (n=650)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.246)

- **PATRÓN** `drift_60min` |x|≤ `0.6907` → IC=+0.259 (n=972)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6907 (IC base=+0.246)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.266 (n=672)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.246)

- **PATRÓN** `ibs_20min` < `0.6471` → IC=+0.271 (n=855)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6471 (IC base=+0.246)

- **PATRÓN** `dist_vwap_pct` > `0.5875` → IC=+0.246 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5875 (IC base=+0.246)

- **PATRÓN** `dist_vwap_pct` < `0.332` → IC=+0.255 (n=860)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.332 (IC base=+0.246)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.988` → IC=+0.265 (n=917)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.988 (IC base=+0.246)

- **PATRÓN** `volumen_regimen` < `0.7522` → IC=+0.263 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7522 (IC base=+0.246)

- **PATRÓN** `volumen_pendiente_norm` < `0.104` → IC=+0.257 (n=872)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.104 (IC base=+0.246)

- **PATRÓN** `volumen_spike_ratio` > `1.8448` → IC=+0.262 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8448 (IC base=+0.246)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.248 (n=1199)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.246)

- **PATRÓN** `libro_liquidez` > `4016.482` → IC=+0.269 (n=648)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4016.482 (IC base=+0.246)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.276 (n=858)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.246)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.147 (n=941)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0043 (IC base=+0.069)

- **PATRÓN** `ibs_20min` > `0.4181` → IC=+0.133 (n=2722)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` > 0.4181 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` > `0.1594` → IC=+0.156 (n=1267)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1594 (IC base=+0.069)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.306` → IC=+0.140 (n=590)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 10.306 (IC base=+0.069)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.124 (n=1012)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` > 0.0092 (IC base=+0.100)

- **PATRÓN** `ibs_20min` < `0.5815` → IC=+0.183 (n=2153)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.5815 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.544` → IC=+0.133 (n=956)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 2.544 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` > `0.152` → IC=+0.191 (n=609)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.152 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` < `2.1505` → IC=+0.124 (n=1821)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.1505 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` > `1.7845` → IC=+0.124 (n=1380)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 1.7845 (IC base=+0.100)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.5515` → IC=-0.120 (n=343)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5515
  - _Potencial_: sin este filtro IC_bueno=+0.157 (n=697)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.121 (n=715)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.0057 (IC base=+0.065)

- **PATRÓN** `ibs_20min` > `0.5515` → IC=+0.157 (n=697)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.5515 (IC base=+0.065)

- **PATRÓN** `dist_vwap_pct` > `0.1288` → IC=+0.166 (n=363)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1288 (IC base=+0.065)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.121 (n=333)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.0037 (IC base=+0.058)

- **PATRÓN** `ibs_20min` < `0.0639` → IC=+0.252 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0639 (IC base=+0.058)

- **PATRÓN** `volumen_pendiente_norm` > `0.071` → IC=+0.147 (n=321)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.071 (IC base=+0.058)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` < `0.5274` → IC=-0.120 (n=356)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5274
  - _Potencial_: sin este filtro IC_bueno=+0.156 (n=724)

- **FILTRO** `ibs_20min` > `0.4936` → IC=-0.128 (n=267)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4936
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=520)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.156 (n=370)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0043 (IC base=+0.062)

- **PATRÓN** `ibs_20min` > `0.5274` → IC=+0.156 (n=724)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.5274 (IC base=+0.062)

- **PATRÓN** `dist_vwap_pct` > `0.1909` → IC=+0.157 (n=348)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1909 (IC base=+0.062)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.996` → IC=+0.167 (n=178)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.996 (IC base=+0.062)

- **PATRÓN** `ibs_20min` < `0.3174` → IC=+0.227 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3174 (IC base=+0.048)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.197 (n=308)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 1.0 (IC base=+0.036)

- **PATRÓN** `dist_vwap_pct` > `0.7698` → IC=+0.156 (n=222)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.7698 (IC base=+0.036)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.177 (n=419)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0103 (IC base=+0.102)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.200 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.102)

- **PATRÓN** `dist_vwap_pct` < `0.2261` → IC=+0.155 (n=593)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.2261 (IC base=+0.102)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.149` → IC=+0.240 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.149 (IC base=+0.102)

- **PATRÓN** `volumen_regimen` > `1.1136` → IC=+0.190 (n=198)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 1.1136 (IC base=+0.102)

- **PATRÓN** `volumen_pendiente_norm` > `0.1605` → IC=+0.194 (n=155)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1605 (IC base=+0.102)

- **PATRÓN** `volumen_spike_ratio` < `2.2044` → IC=+0.129 (n=496)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 2.2044 (IC base=+0.102)

- **PATRÓN** `volumen_spike_ratio` > `1.8607` → IC=+0.145 (n=376)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.8607 (IC base=+0.102)

### GBM_LATE_60M#XRP#60min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.387 (n=60)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.313)

- **PATRÓN** `drift_60min` |x|≤ `0.2739` → IC=+0.312 (n=30)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2739 (IC base=+0.313)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.380 (n=23)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.313)

- **PATRÓN** `ibs_20min` > `0.6044` → IC=+0.355 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6044 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` > `0.4912` → IC=+0.400 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4912 (IC base=+0.313)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.323` → IC=+0.342 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.323 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` < `0.7856` → IC=+0.308 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7856 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` > `0.5715` → IC=+0.329 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5715 (IC base=+0.313)

- **PATRÓN** `volumen_pendiente_norm` < `0.0568` → IC=+0.339 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0568 (IC base=+0.313)

- **PATRÓN** `volumen_pendiente_norm` > `0.1841` → IC=+0.342 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1841 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` < `2.7973` → IC=+0.353 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.7973 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` > `2.1072` → IC=+0.326 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1072 (IC base=+0.313)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.353 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.313)

- **PATRÓN** `libro_liquidez` > `34.9205` → IC=+0.312 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 34.9205 (IC base=+0.313)

- **PATRÓN** `sigma_h` < `0.0096` → IC=+0.397 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0096 (IC base=+0.353)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.351 (n=72)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.353)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.400 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.353)

- **PATRÓN** `ibs_20min` < `0.118` → IC=+0.395 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.118 (IC base=+0.353)

- **PATRÓN** `ibs_20min` > `0.4562` → IC=+0.362 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4562 (IC base=+0.353)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.59` → IC=+0.458 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.59 (IC base=+0.353)

- **PATRÓN** `volumen_regimen` > `0.6258` → IC=+0.392 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6258 (IC base=+0.353)

- **PATRÓN** `volumen_pendiente_norm` > `0.0801` → IC=+0.402 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0801 (IC base=+0.353)

- **PATRÓN** `volumen_spike_ratio` < `1.5099` → IC=+0.392 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5099 (IC base=+0.353)

- **PATRÓN** `volumen_spike_ratio` > `3.1184` → IC=+0.429 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.1184 (IC base=+0.353)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.402 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.353)

- **PATRÓN** `libro_liquidez` > `39.35` → IC=+0.393 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 39.35 (IC base=+0.353)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` < `0.0062` → IC=-0.251 (n=211)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0062
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=212)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.310 (n=98)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=325)

- **FILTRO** `volumen_regimen` < `0.8808` → IC=-0.307 (n=138)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8808
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=281)

- **FILTRO** `ibs_20min` > `0.681` → IC=-0.318 (n=130)

  - _Acción_: SKIP cuando `ibs_20min` > 0.681
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=254)

- **FILTRO** `dist_vwap_pct` > `0.4617` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4617
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=348)

- **FILTRO** `sigma_ewma_delta_pct` > `9.288` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.288
  - _Potencial_: sin este filtro IC_bueno=-0.256 (n=354)

- **FILTRO** `volumen_pendiente_norm` > `0.0463` → IC=-0.375 (n=30)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0463
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=259)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `sigma_h` < `0.0069` → IC=-0.253 (n=99)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0069
  - _Potencial_: sin este filtro IC_bueno=-0.243 (n=33)

- **FILTRO** `hora_utc` > `9.0` → IC=-0.312 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=102)

- **FILTRO** `ibs_20min` < `0.0328` → IC=-0.300 (n=33)

  - _Acción_: SKIP cuando `ibs_20min` < 0.0328
  - _Potencial_: sin este filtro IC_bueno=-0.233 (n=99)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.256 (n=76)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=76)

- **FILTRO** `volumen_regimen` > `0.805` → IC=-0.321 (n=37)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=115)

- **FILTRO** `volumen_spike_ratio` > `1.3298` → IC=-0.302 (n=79)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.3298
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=40)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_h` < `0.003` → IC=-0.250 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.003
  - _Potencial_: sin este filtro IC_bueno=-0.148 (n=103)

- **FILTRO** `ibs_20min` < `0.6002` → IC=-0.472 (n=34)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6002
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=103)

- **FILTRO** `volumen_regimen` < `0.7594` → IC=-0.250 (n=34)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7594
  - _Potencial_: sin este filtro IC_bueno=-0.148 (n=103)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.372 (n=37)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=103)

- **FILTRO** `dist_vwap_pct` < `0.3288` → IC=-0.306 (n=127)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.3288
  - _Potencial_: sin este filtro IC_bueno=-0.233 (n=13)

- **FILTRO** `volumen_spike_ratio` < `1.4493` → IC=-0.357 (n=26)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.4493
  - _Potencial_: sin este filtro IC_bueno=-0.290 (n=79)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.295 (n=125)

- **FILTRO** `libro_liquidez` < `2014.9221` → IC=-0.306 (n=70)

  - _Acción_: SKIP cuando `libro_liquidez` < 2014.9221
  - _Potencial_: sin este filtro IC_bueno=-0.292 (n=70)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `sigma_h` < `0.0112` → IC=-0.290 (n=98)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0112
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=52)

- **FILTRO** `drift_60min` |x|> `0.2366` → IC=-0.346 (n=37)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2366
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=112)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.342 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=54)

- **FILTRO** `volumen_regimen` < `0.9252` → IC=-0.460 (n=23)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9252
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=48)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.2542` → IC=-0.151 (n=345)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2542
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=1036)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.251 (n=407)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.200 (n=411)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `0.6818` → IC=+0.200 (n=899)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6818 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `0.9043` → IC=+0.309 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9043 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.379` → IC=+0.191 (n=215)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 10.379 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `0.6229` → IC=+0.196 (n=294)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.6229 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` > `1.1961` → IC=+0.176 (n=294)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 1.1961 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` < `0.0674` → IC=+0.186 (n=680)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.0674 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `1.4016` → IC=+0.206 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4016 (IC base=+0.163)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.135 (n=83)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.0066 (IC base=+0.065)

- **PATRÓN** `ibs_20min` > `0.7306` → IC=+0.139 (n=247)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 0.7306 (IC base=+0.065)

- **PATRÓN** `dist_vwap_pct` > `0.7218` → IC=+0.235 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7218 (IC base=+0.065)

- **PATRÓN** `ibs_20min` < `0.2563` → IC=+0.133 (n=459)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.2563 (IC base=+0.073)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.163 (n=90)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0073 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.1196` → IC=+0.136 (n=119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.1196 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.163 (n=99)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 18.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.136 (n=97)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 6.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` > `0.8015` → IC=+0.175 (n=241)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.8015 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` > `0.8305` → IC=+0.189 (n=43)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.8305 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.1137` → IC=+0.153 (n=217)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1137 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.26` → IC=+0.131 (n=63)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 11.26 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `0.6229` → IC=+0.185 (n=90)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6229 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` > `1.1834` → IC=+0.163 (n=90)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 1.1834 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` < `0.052` → IC=+0.184 (n=223)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.052 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` < `1.7116` → IC=+0.175 (n=161)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.7116 (IC base=+0.131)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=224)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `1704.1785` → IC=+0.175 (n=269)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 1704.1785 (IC base=+0.131)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.2459` → IC=-0.267 (n=58)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2459
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=175)

- **FILTRO** `volumen_spike_ratio` > `1.9711` → IC=-0.132 (n=66)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.9711
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=129)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.289 (n=339)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.271)

- **PATRÓN** `ibs_20min` > `0.8636` → IC=+0.313 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8636 (IC base=+0.271)

- **PATRÓN** `dist_vwap_pct` > `0.7967` → IC=+0.404 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7967 (IC base=+0.271)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.992` → IC=+0.357 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.992 (IC base=+0.271)

- **PATRÓN** `volumen_regimen` < `0.7975` → IC=+0.304 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7975 (IC base=+0.271)

- **PATRÓN** `volumen_pendiente_norm` > `0.089` → IC=+0.313 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.089 (IC base=+0.271)

- **PATRÓN** `volumen_spike_ratio` < `1.485` → IC=+0.321 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.485 (IC base=+0.271)

- **PATRÓN** `volumen_spike_ratio` > `2.0516` → IC=+0.311 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.0516 (IC base=+0.271)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.271 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.271)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.314 (n=202)

- **PATRÓN** `drift_ventana_pct` |x|> `0.5446` → IC=+0.352 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.5446 (IC base=+0.332)

- **PATRÓN** `elapsed_s` > `209.4` → IC=+0.395 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 209.4 (IC base=+0.332)

- **PATRÓN** `drift_15min` |x|≤ `1.0466` → IC=+0.389 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0466 (IC base=+0.332)

- **PATRÓN** `drift_60min` |x|≤ `0.6678` → IC=+0.387 (n=104)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6678 (IC base=+0.332)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.381 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.332)

- **PATRÓN** `ballena_activa_n` < `1039.0` → IC=+0.426 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1039.0 (IC base=+0.332)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3495` → IC=+0.292 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3495 (IC base=+0.278)

- **PATRÓN** `elapsed_s` > `232.0` → IC=+0.360 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 232.0 (IC base=+0.278)

- **PATRÓN** `drift_15min` |x|≤ `2.354` → IC=+0.309 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.354 (IC base=+0.278)

- **PATRÓN** `drift_60min` |x|≤ `0.947` → IC=+0.296 (n=145)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.947 (IC base=+0.278)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.314 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.278)

- **PATRÓN** `ballena_activa_n` < `1275.0` → IC=+0.357 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1275.0 (IC base=+0.278)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.314 (n=202)

- **PATRÓN** `drift_ventana_pct` |x|> `0.5446` → IC=+0.352 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.5446 (IC base=+0.332)

- **PATRÓN** `elapsed_s` > `209.4` → IC=+0.395 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 209.4 (IC base=+0.332)

- **PATRÓN** `drift_15min` |x|≤ `1.0466` → IC=+0.389 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0466 (IC base=+0.332)

- **PATRÓN** `drift_60min` |x|≤ `0.6678` → IC=+0.387 (n=104)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6678 (IC base=+0.332)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.381 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.332)

- **PATRÓN** `ballena_activa_n` < `1039.0` → IC=+0.426 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1039.0 (IC base=+0.332)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3495` → IC=+0.292 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3495 (IC base=+0.278)

- **PATRÓN** `elapsed_s` > `232.0` → IC=+0.360 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 232.0 (IC base=+0.278)

- **PATRÓN** `drift_15min` |x|≤ `2.354` → IC=+0.309 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.354 (IC base=+0.278)

- **PATRÓN** `drift_60min` |x|≤ `0.947` → IC=+0.296 (n=145)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.947 (IC base=+0.278)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.314 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.278)

- **PATRÓN** `ballena_activa_n` < `1275.0` → IC=+0.357 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1275.0 (IC base=+0.278)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=293)

- **FILTRO** `py_entrada` < `0.415` → IC=-0.171 (n=71)

  - _Acción_: SKIP cuando `py_entrada` < 0.415
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=238)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=293)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=1580)

### LIQUIDACIONES_15M#BNB#15min
- **PATRÓN** `liq_n` > `2.0` → IC=+0.170 (n=89)

  - _Acción_: Kelly boost +0.85€ cuando `liq_n` > 2.0 (IC base=+0.098)

- **PATRÓN** `liq_usd_total` > `101.24` → IC=+0.125 (n=182)

  - _Acción_: Kelly boost +0.62€ cuando `liq_usd_total` > 101.24 (IC base=+0.098)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.214 (n=61)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.098)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.133 (n=96)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` > 0.5 (IC base=+0.098)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.135 (n=102)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.03 (IC base=+0.098)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9866` → IC=-0.143 (n=54)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9866
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=112)

### LIQUIDACIONES_15M#DOGE#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=118)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.136 (n=105)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 9.0 (IC base=+0.078)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `1211.34` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_usd_total` < 1211.34
  - _Potencial_: sin este filtro IC_bueno=-0.104 (n=46)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.188 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=31)

- **FILTRO** `py_entrada` < `0.425` → IC=-0.309 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.425
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=42)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=27)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=283)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=4280)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=258)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=215)

- **FILTRO** `ballena_activa_n` > `45.0` → IC=-0.182 (n=83)

  - _Acción_: SKIP cuando `ballena_activa_n` > 45.0
  - _Potencial_: sin este filtro IC_bueno=+0.195 (n=162)

- **PATRÓN** `liq_imbalance_60min` |x|> `1.0` → IC=+0.122 (n=215)

  - _Acción_: Kelly boost +0.61€ cuando `liq_imbalance_60min` |x|> 1.0 (IC base=+0.030)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.128 (n=154)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.5 (IC base=+0.030)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.195 (n=162)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 45.0 (IC base=+0.030)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=22)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.134 (n=296)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.495 (IC base=+0.023)

### LIQUIDACIONES_5M#DOGE#5min
- **PATRÓN** `liq_n` > `3.0` → IC=+0.324 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 3.0 (IC base=+0.202)

- **PATRÓN** `liq_usd_total` > `782.22` → IC=+0.268 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 782.22 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.222 (n=124)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.235 (n=81)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.202)

- **PATRÓN** `ballena_activa_n` < `3.0` → IC=+0.250 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 3.0 (IC base=+0.202)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=1686)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=1640)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.286 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.505` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=770)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=779)

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
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=590)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=571)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.136 (n=240)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.495 (IC base=-0.002)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=1181)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=1181)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=1587)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=1587)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=371)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=371)

- **FILTRO** `py_entrada` < `0.425` → IC=-0.144 (n=85)

  - _Acción_: SKIP cuando `py_entrada` < 0.425
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=301)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.136 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=418)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=467)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=345)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=450)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=450)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=439)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.129 (n=3711)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=9559)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.145 (n=119)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=147)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.154 (n=50)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=58)

- **FILTRO** `restante_min` < `3.99` → IC=-0.127 (n=73)

  - _Acción_: SKIP cuando `restante_min` < 3.99
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=35)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.214 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=75)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.159 (n=449)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=1073)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.137 (n=351)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=958)

- **PATRÓN** `py_entrada` < `0.51` → IC=+0.141 (n=452)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.51 (IC base=-0.006)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.123 (n=205)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=477)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.123 (n=755)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=809)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.139 (n=375)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=796)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.122 (n=656)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=658)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.121 (n=608)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=643)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.131 (n=659)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=760)

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

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=1413)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.46` → IC=-0.178 (n=9313)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=29020)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.171 (n=9668)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=29998)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.199 (n=1732)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=5388)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.145 (n=2372)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=4627)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.139 (n=1823)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 1.0 (IC base=+0.039)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.136 (n=3292)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.5 (IC base=+0.015)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.173 (n=1410)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=4234)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.197 (n=1749)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=5429)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.134 (n=2186)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 1.0 (IC base=+0.032)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` > `0.575` → IC=-0.179 (n=1414)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=4309)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.156 (n=1781)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=5358)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=2452)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2376)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=973)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=3406)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=4358)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `14.0` → IC=-0.157 (n=135)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=437)

- **FILTRO** `hora_utc` > `20.0` → IC=-0.146 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=447)

### MOMENTUM_IBS_15M_FADE#DOGE#15min
- **FILTRO** `ibs_20min` > `0.7158` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7158
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=48)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `ibs_20min` < `0.1975` → IC=-0.223 (n=110)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1975
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=224)

- **FILTRO** `libro_liquidez` < `3613.7014` → IC=-0.152 (n=110)

  - _Acción_: SKIP cuando `libro_liquidez` < 3613.7014
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=224)

- **FILTRO** `hora_utc` < `7.0` → IC=-0.204 (n=113)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=375)

- **FILTRO** `ballena_activa_n` > `106.0` → IC=-0.172 (n=117)

  - _Acción_: SKIP cuando `ballena_activa_n` > 106.0
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=363)

- **FILTRO** `libro_liquidez` < `3258.4475` → IC=-0.187 (n=161)

  - _Acción_: SKIP cuando `libro_liquidez` < 3258.4475
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=327)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=983)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.224 (n=310)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=971)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `14.0` → IC=-0.141 (n=76)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=231)

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
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=93)

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

### MOMENTUM_IBS_5M_BALLENA
- **FILTRO** `hora_utc` < `8.0` → IC=-0.138 (n=25991)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=58802)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.302 (n=20660)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=64133)

- **FILTRO** `ibs_7min` < `0.7273` → IC=-0.225 (n=27876)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7273
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=56917)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.155 (n=27657)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=57136)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.247 (n=26254)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=79726)

- **FILTRO** `ibs_7min` > `0.2782` → IC=-0.183 (n=26489)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2782
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=79491)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.164 (n=3627)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=11593)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.327 (n=3601)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=11619)

- **FILTRO** `ibs_7min` < `0.7087` → IC=-0.257 (n=5022)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7087
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=10198)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.280 (n=4447)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=13823)

- **FILTRO** `ibs_7min` > `0.7692` → IC=-0.212 (n=4564)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7692
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=13706)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.129 (n=3417)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=10728)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.268 (n=3464)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=10681)

- **FILTRO** `ibs_7min` < `0.711` → IC=-0.214 (n=3536)

  - _Acción_: SKIP cuando `ibs_7min` < 0.711
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=10609)

- **FILTRO** `ballena_activa_n` > `157.0` → IC=-0.205 (n=3524)

  - _Acción_: SKIP cuando `ballena_activa_n` > 157.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=10621)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.265 (n=3300)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=11185)

- **FILTRO** `ibs_7min` > `0.2638` → IC=-0.188 (n=3621)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2638
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=10864)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.177 (n=3602)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=10883)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.169 (n=3485)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=11100)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.329 (n=3483)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=11102)

- **FILTRO** `ibs_7min` < `0.291` → IC=-0.255 (n=4813)

  - _Acción_: SKIP cuando `ibs_7min` < 0.291
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=9772)

- **FILTRO** `ballena_activa_n` > `4.0` → IC=-0.174 (n=3482)

  - _Acción_: SKIP cuando `ballena_activa_n` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=11103)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.261 (n=4625)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=14684)

- **FILTRO** `ibs_7min` > `0.7222` → IC=-0.185 (n=4827)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7222
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=14482)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.121 (n=4544)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.106 (n=9278)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.277 (n=3153)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=10669)

- **FILTRO** `ibs_7min` < `0.7108` → IC=-0.203 (n=3453)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7108
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=10369)

- **FILTRO** `ballena_activa_n` > `26.0` → IC=-0.200 (n=3348)

  - _Acción_: SKIP cuando `ballena_activa_n` > 26.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=10474)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.258 (n=3347)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=11013)

- **FILTRO** `ibs_7min` > `0.2717` → IC=-0.177 (n=3588)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2717
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=10772)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.169 (n=3575)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=10785)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.303 (n=3271)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=10131)

- **FILTRO** `ibs_7min` < `0.2941` → IC=-0.234 (n=4408)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2941
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=8994)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.203 (n=4847)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=15553)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.314 (n=3332)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=10287)

- **FILTRO** `ibs_7min` < `0.72` → IC=-0.232 (n=4483)

  - _Acción_: SKIP cuando `ibs_7min` < 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=9136)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.195 (n=3395)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=10224)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.231 (n=4655)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=14501)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=122)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.163 (n=304)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=1036)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=1325)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.156 (n=187)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=685)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=933)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=251)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=279)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.141 (n=129)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=400)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=480)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.216 (n=192)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=594)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.162 (n=255)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=503)

- **FILTRO** `libro_liquidez` < `3306.2556` → IC=-0.146 (n=196)

  - _Acción_: SKIP cuando `libro_liquidez` < 3306.2556
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=590)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=56)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=560)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4305` → IC=+0.144 (n=779)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio` |x|> 0.4305 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.133 (n=627)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 4.0 (IC base=+0.124)

- **PATRÓN** `total_vol_5m` < `458.564` → IC=+0.164 (n=573)

  - _Acción_: Kelly boost +0.82€ cuando `total_vol_5m` < 458.564 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `3672.897` → IC=+0.131 (n=778)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 3672.897 (IC base=+0.124)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.182 (n=196)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 14.0 (IC base=+0.141)

- **PATRÓN** `total_vol_5m` < `381.605` → IC=+0.164 (n=349)

  - _Acción_: Kelly boost +0.82€ cuando `total_vol_5m` < 381.605 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.147 (n=358)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.04 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.141 (n=260)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 8.0 (IC base=+0.141)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3987` → IC=+0.138 (n=360)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio` |x|> 0.3987 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.141 (n=335)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 15.0 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.123 (n=438)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.04 (IC base=+0.120)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.416` → IC=+0.162 (n=208)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.81€ cuando `delta_ratio` |x|> 0.416 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.153 (n=286)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.128)

- **PATRÓN** `total_vol_5m` < `877.8133` → IC=+0.159 (n=312)

  - _Acción_: Kelly boost +0.80€ cuando `total_vol_5m` < 877.8133 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `7697.7504` → IC=+0.129 (n=208)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 7697.7504 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.187 (n=113)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 59.0 (IC base=+0.128)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4317` → IC=+0.218 (n=133)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4317 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.164 (n=117)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 5.0 (IC base=+0.134)

- **PATRÓN** `total_vol_5m` < `4782.684` → IC=+0.182 (n=196)

  - _Acción_: Kelly boost +0.91€ cuando `total_vol_5m` < 4782.684 (IC base=+0.134)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `13.0` → IC=+0.127 (n=314)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 13.0 (IC base=+0.097)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.132 (n=218)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.097)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `6.1729` → IC=-0.222 (n=88)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 6.1729
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=172)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.152 (n=340)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0047 (IC base=-0.029)

### PRICE_TARGET_GBM#ETH#atexpiry
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.252 (n=103)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.003)

- **PATRÓN** `pct_vs_K` |x|≤ `1.9196` → IC=+0.214 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 1.9196 (IC base=+0.003)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `T_h` > `76.1623` → IC=-0.125 (n=70)

  - _Acción_: SKIP cuando `T_h` > 76.1623
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=24)

- **FILTRO** `pct_vs_K` |x|> `6.3582` → IC=-0.258 (n=31)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 6.3582
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=63)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `T_h` < `75.359` → IC=-0.167 (n=64)

  - _Acción_: SKIP cuando `T_h` < 75.359
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=132)

### PRICE_TARGET_GBM#SOL#reach
- **FILTRO** `sigma_h` < `0.0147` → IC=-0.167 (n=22)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0147
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=12)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0118` → IC=-0.255 (n=659)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0118
  - _Potencial_: sin este filtro IC_bueno=-0.230 (n=220)

- **FILTRO** `T_h` > `66.9347` → IC=-0.254 (n=587)

  - _Acción_: SKIP cuando `T_h` > 66.9347
  - _Potencial_: sin este filtro IC_bueno=-0.238 (n=292)

- **FILTRO** `sigma_h` < `0.0058` → IC=-0.178 (n=209)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0058
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=630)

- **FILTRO** `T_h` > `141.7902` → IC=-0.140 (n=209)

  - _Acción_: SKIP cuando `T_h` > 141.7902
  - _Potencial_: sin este filtro IC_bueno=-0.109 (n=630)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `49.2927` → IC=-0.243 (n=216)

  - _Acción_: SKIP cuando `T_h` > 49.2927
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=74)

- **FILTRO** `sigma_h` < `0.0068` → IC=-0.175 (n=155)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0068
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=156)

- **FILTRO** `pct_vs_K` |x|> `2.3701` → IC=-0.322 (n=105)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.3701
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=206)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `sigma_h` < `0.0078` → IC=-0.273 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0078
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=21)

- **FILTRO** `T_h` > `139.1329` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `T_h` > 139.1329
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=21)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.0096` → IC=-0.323 (n=128)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0096
  - _Potencial_: sin este filtro IC_bueno=-0.286 (n=129)

- **FILTRO** `T_h` < `69.3519` → IC=-0.314 (n=84)

  - _Acción_: SKIP cuando `T_h` < 69.3519
  - _Potencial_: sin este filtro IC_bueno=-0.300 (n=173)

- **FILTRO** `sigma_h` < `0.0058` → IC=-0.156 (n=62)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0058
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=189)

- **PATRÓN** `pct_vs_K` |x|≤ `1.9843` → IC=+0.164 (n=126)

  - _Acción_: Kelly boost +0.82€ cuando `pct_vs_K` |x|≤ 1.9843 (IC base=-0.097)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `sigma_h` < `0.0095` → IC=-0.180 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `T_h` < `138.4503` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `T_h` < 138.4503
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

- **FILTRO** `sigma_h` < `0.0098` → IC=-0.214 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0098
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=19)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0129` → IC=-0.225 (n=158)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0129
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=82)

- **FILTRO** `T_h` > `113.6692` → IC=-0.235 (n=81)

  - _Acción_: SKIP cuando `T_h` > 113.6692
  - _Potencial_: sin este filtro IC_bueno=-0.208 (n=159)

- **FILTRO** `sigma_h` < `0.0097` → IC=-0.250 (n=46)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=141)

- **FILTRO** `T_h` > `46.6251` → IC=-0.138 (n=125)

  - _Acción_: SKIP cuando `T_h` > 46.6251
  - _Potencial_: sin este filtro IC_bueno=-0.109 (n=62)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1072` → IC=+0.449 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1072 (IC base=+0.326)

- **PATRÓN** `sigma_h` < `0.0148` → IC=+0.341 (n=130)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0148 (IC base=+0.326)

- **PATRÓN** `sigma_h` > `0.0134` → IC=+0.336 (n=59)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0134 (IC base=+0.326)

- **PATRÓN** `T_h` < `0.3491` → IC=+0.370 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.3491 (IC base=+0.326)

- **PATRÓN** `T_h` > `0.4307` → IC=+0.339 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4307 (IC base=+0.326)

- **PATRÓN** `dist_50` > `0.4566` → IC=+0.484 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4566 (IC base=+0.326)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.344 (n=152)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.326)

- **PATRÓN** `edge` > `0.0992` → IC=+0.424 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.0992 (IC base=+0.392)

- **PATRÓN** `T_h` < `0.7258` → IC=+0.418 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.7258 (IC base=+0.392)

- **PATRÓN** `dist_50` > `0.368` → IC=+0.440 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.368 (IC base=+0.392)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.411 (n=348)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.392)

### RESOLUTION_SNIPER#BTC#sniper
- **PATRÓN** `edge` > `0.0939` → IC=+0.276 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.0939 (IC base=+0.201)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.271 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.201)

- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.250 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.201)

- **PATRÓN** `T_h` < `0.659` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.659 (IC base=+0.201)

- **PATRÓN** `T_h` > `1.4441` → IC=+0.245 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4441 (IC base=+0.201)

- **PATRÓN** `dist_50` > `0.3235` → IC=+0.303 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3235 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.236 (n=70)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.235 (n=66)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.201)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1011` → IC=+0.468 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1011 (IC base=+0.416)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.438 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0073 (IC base=+0.416)

- **PATRÓN** `T_h` < `1.178` → IC=+0.442 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.178 (IC base=+0.416)

- **PATRÓN** `dist_50` > `0.4122` → IC=+0.484 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4122 (IC base=+0.416)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.405 (n=40)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.416)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.444 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.416)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.15` → IC=+0.487 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.15 (IC base=+0.422)

- **PATRÓN** `sigma_h` < `0.0155` → IC=+0.471 (n=66)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0155 (IC base=+0.422)

- **PATRÓN** `T_h` < `1.0409` → IC=+0.426 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.0409 (IC base=+0.422)

- **PATRÓN** `T_h` > `0.5804` → IC=+0.427 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.5804 (IC base=+0.422)

- **PATRÓN** `dist_50` > `0.325` → IC=+0.474 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.325 (IC base=+0.422)

- **PATRÓN** `edge` > `0.1937` → IC=+0.472 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1937 (IC base=+0.465)

- **PATRÓN** `sigma_h` < `0.0162` → IC=+0.475 (n=160)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0162 (IC base=+0.465)

- **PATRÓN** `T_h` < `0.8021` → IC=+0.459 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.8021 (IC base=+0.465)

- **PATRÓN** `T_h` > `1.4857` → IC=+0.482 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4857 (IC base=+0.465)

- **PATRÓN** `dist_50` > `0.414` → IC=+0.481 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.414 (IC base=+0.465)

- **PATRÓN** `hora_utc` < `2.0` → IC=+0.485 (n=63)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 2.0 (IC base=+0.465)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=496)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=527)

- **PATRÓN** `streak_estiramiento` < `0.3783` → IC=+0.135 (n=165)

  - _Acción_: Kelly boost +0.67€ cuando `streak_estiramiento` < 0.3783 (IC base=+0.021)

- **PATRÓN** `streak_estiramiento` < `0.8333` → IC=+0.124 (n=365)

  - _Acción_: Kelly boost +0.62€ cuando `streak_estiramiento` < 0.8333 (IC base=+0.058)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.140 (n=137)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 14.0 (IC base=+0.058)

### STREAK_FADE_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` < 0.495 (IC base=+0.080)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=30)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.179 (n=26)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.179 (n=26)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.495 (IC base=+0.058)

### STREAK_FADE_15M#XRP#15min
- **PATRÓN** `streak_estiramiento` < `0.3787` → IC=+0.129 (n=130)

  - _Acción_: Kelly boost +0.64€ cuando `streak_estiramiento` < 0.3787 (IC base=+0.038)

- **PATRÓN** `streak_estiramiento` < `0.3698` → IC=+0.209 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.3698 (IC base=+0.080)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.134 (n=200)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 35.0 (IC base=+0.080)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.194 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=104)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=61)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.136 (n=31)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=46)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=826)

### STREAK_FADE_60M
- **FILTRO** `py_entrada` < `0.515` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.134 (n=39)

- **FILTRO** `streak_estiramiento` > `0.6393` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.6393
  - _Potencial_: sin este filtro IC_bueno=+0.258 (n=31)

- **PATRÓN** `py_entrada` > `0.515` → IC=+0.134 (n=39)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` > 0.515 (IC base=+0.017)

- **PATRÓN** `streak_estiramiento` < `0.6393` → IC=+0.258 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.6393 (IC base=+0.015)

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
- **FILTRO** `py_entrada` < `0.525` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.525
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=13)

- **PATRÓN** `streak_estiramiento` < `0.6237` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.6237 (IC base=+0.040)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=1114)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1360)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1244)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=1336)

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
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=5612)

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
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=3395)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.183 (n=2208)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0059 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.2334` → IC=+0.158 (n=6625)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2334 (IC base=+0.132)

- **PATRÓN** `drift_15min` |x|≤ `1.124` → IC=+0.133 (n=6623)

  - _Acción_: Kelly boost +0.66€ cuando `drift_15min` |x|≤ 1.124 (IC base=+0.132)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0644` → IC=+0.132 (n=6622)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio_macro` |x|> 0.0644 (IC base=+0.132)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0996` → IC=+0.143 (n=2087)

  - _Acción_: Kelly boost +0.72€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0996 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.143 (n=6133)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 6.0 (IC base=+0.132)

- **PATRÓN** `ibs_15` > `0.551` → IC=+0.207 (n=5919)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.551 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.963` → IC=+0.229 (n=1239)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.963 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=3474)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `4314.507` → IC=+0.171 (n=2208)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 4314.507 (IC base=+0.132)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=2570)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.226 (n=789)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.0772` → IC=+0.248 (n=395)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0772 (IC base=+0.206)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2662` → IC=+0.228 (n=299)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2662 (IC base=+0.206)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2243` → IC=+0.217 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2243 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.232 (n=829)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.206)

- **PATRÓN** `ibs_15` > `0.702` → IC=+0.275 (n=896)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.702 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `0.4005` → IC=+0.231 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4005 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` < `0.5531` → IC=+0.208 (n=1010)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5531 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.088` → IC=+0.300 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.088 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.209 (n=1162)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `11864.4535` → IC=+0.220 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11864.4535 (IC base=+0.206)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.148 (n=1011)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0067 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.0668` → IC=+0.152 (n=507)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.0668 (IC base=+0.133)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0834` → IC=+0.136 (n=1026)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio_macro` |x|> 0.0834 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.146 (n=815)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 11.0 (IC base=+0.133)

- **PATRÓN** `ibs_15` > `0.4799` → IC=+0.218 (n=1149)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.4799 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `0.1236` → IC=+0.146 (n=716)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.1236 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.6708` → IC=+0.134 (n=1305)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.6708 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.9` → IC=+0.282 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.9 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `6099.7428` → IC=+0.177 (n=521)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 6099.7428 (IC base=+0.133)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.8333` → IC=+0.146 (n=696)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.73€ cuando `ibs_15` > 0.8333 (IC base=+0.044)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.143 (n=1676)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0119 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.2399` → IC=+0.176 (n=1676)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2399 (IC base=+0.137)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0582` → IC=+0.140 (n=1676)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio_macro` |x|> 0.0582 (IC base=+0.137)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.093` → IC=+0.185 (n=525)

  - _Acción_: Kelly boost +0.93€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.093 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.144 (n=1532)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 6.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.138 (n=1551)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.137)

- **PATRÓN** `ibs_15` > `0.697` → IC=+0.232 (n=1117)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.697 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.215` → IC=+0.144 (n=765)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.215 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.9103` → IC=+0.141 (n=1936)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.9103 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.978` → IC=+0.185 (n=388)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 16.978 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `2944.0982` → IC=+0.181 (n=760)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2944.0982 (IC base=+0.137)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `drift_60min` |x|≤ `0.1089` → IC=+0.365 (n=548)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1089 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1426` → IC=+0.376 (n=548)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1426 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1039` → IC=+0.378 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1039 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.371 (n=760)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.7881` → IC=+0.394 (n=821)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7881 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.2713` → IC=+0.383 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2713 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.778` → IC=+0.398 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.778 (IC base=+0.364)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.366 (n=999)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `9657.3043` → IC=+0.377 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9657.3043 (IC base=+0.364)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.1523` → IC=+0.365 (n=346)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1523 (IC base=+0.363)

- **PATRÓN** `drift_15min` |x|≤ `0.4182` → IC=+0.363 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4182 (IC base=+0.363)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2167` → IC=+0.378 (n=178)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2167 (IC base=+0.363)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1441` → IC=+0.399 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1441 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.380 (n=366)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.363)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.363 (n=400)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.363)

- **PATRÓN** `ibs_15` > `0.8057` → IC=+0.384 (n=393)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8057 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` > `0.2555` → IC=+0.393 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2555 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.667` → IC=+0.384 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.667 (IC base=+0.363)

- **PATRÓN** `libro_liquidez` > `15150.2605` → IC=+0.390 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15150.2605 (IC base=+0.363)

- **PATRÓN** `ballena_activa_n` < `409.0` → IC=+0.385 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 409.0 (IC base=+0.363)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.378 (n=194)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.364)

- **PATRÓN** `drift_60min` |x|≤ `0.1058` → IC=+0.368 (n=287)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1058 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1258` → IC=+0.378 (n=285)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1258 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2925` → IC=+0.370 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2925 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.368 (n=430)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.364)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.376 (n=200)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.7632` → IC=+0.398 (n=428)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7632 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.4608` → IC=+0.378 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4608 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` < `0.6782` → IC=+0.365 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6782 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.854` → IC=+0.400 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.854 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.478` → IC=+0.364 (n=395)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.478 (IC base=+0.364)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.365 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.364)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0079` → IC=-0.204 (n=3078)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0079
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=3080)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.221 (n=2726)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=3432)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1387` → IC=+0.216 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1387 (IC base=-0.087)

- **PATRÓN** `ibs_15` > `0.6306` → IC=+0.280 (n=1354)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6306 (IC base=-0.087)

- **PATRÓN** `dist_vwap_pct` > `0.1169` → IC=+0.209 (n=803)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1169 (IC base=-0.087)

- **PATRÓN** `dist_vwap_pct` < `0.602` → IC=+0.200 (n=1436)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.602 (IC base=-0.087)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2276` → IC=+0.267 (n=2027)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2276 (IC base=+0.002)

- **PATRÓN** `ibs_15` < `0.376` → IC=+0.282 (n=6080)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.376 (IC base=+0.002)

- **PATRÓN** `dist_vwap_pct` > `0.7091` → IC=+0.264 (n=872)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7091 (IC base=+0.002)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0745` → IC=-0.239 (n=2033)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0745
  - _Potencial_: sin este filtro IC_bueno=-0.121 (n=2036)

- **FILTRO** `sigma_h` < `0.004` → IC=-0.209 (n=1017)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.004
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=3052)

- **FILTRO** `sigma_ewma_delta_pct` > `22.211` → IC=-0.238 (n=575)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.211
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=3494)

- **FILTRO** `libro_liquidez` < `10168.4909` → IC=-0.194 (n=1342)

  - _Acción_: SKIP cuando `libro_liquidez` < 10168.4909
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=2727)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.147 (n=372)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0033 (IC base=+0.065)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2673` → IC=+0.281 (n=162)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2673 (IC base=+0.065)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1441` → IC=+0.287 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1441 (IC base=+0.065)

- **PATRÓN** `ibs_15` > `0.7545` → IC=+0.318 (n=486)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7545 (IC base=+0.065)

- **PATRÓN** `dist_vwap_pct` > `0.1067` → IC=+0.287 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1067 (IC base=+0.065)

- **PATRÓN** `dist_vwap_pct` < `0.5501` → IC=+0.287 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5501 (IC base=+0.065)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.793` → IC=+0.141 (n=243)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 21.793 (IC base=+0.065)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0742` → IC=+0.221 (n=84)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0742 (IC base=-0.180)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1389` → IC=+0.289 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1389 (IC base=-0.180)

- **PATRÓN** `ibs_15` < `0.6283` → IC=+0.291 (n=84)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6283 (IC base=-0.180)

- **PATRÓN** `dist_vwap_pct` < `0.0474` → IC=+0.271 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0474 (IC base=-0.180)

- **PATRÓN** `ballena_activa_n` < `392.0` → IC=+0.300 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 392.0 (IC base=-0.180)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=894)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.162 (n=684)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0067 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.0718` → IC=+0.177 (n=301)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.0718 (IC base=+0.149)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2988` → IC=+0.187 (n=541)

  - _Acción_: Kelly boost +0.93€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2988 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.186 (n=310)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 15.0 (IC base=+0.149)

- **PATRÓN** `ibs_15` > `0.5657` → IC=+0.243 (n=684)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5657 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.6763` → IC=+0.176 (n=134)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.6763 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.1598` → IC=+0.150 (n=524)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1598 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.241` → IC=+0.254 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.241 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=894)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `5210.4456` → IC=+0.170 (n=456)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 5210.4456 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.255 (n=1051)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.484` → IC=+0.242 (n=2387)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.484 (IC base=+0.235)

- **PATRÓN** `drift_15min` |x|≤ `0.8303` → IC=+0.248 (n=2099)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.8303 (IC base=+0.235)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1972` → IC=+0.256 (n=1082)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1972 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.239 (n=880)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.240 (n=1634)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.235)

- **PATRÓN** `ibs_15` < `0.1923` → IC=+0.296 (n=1591)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1923 (IC base=+0.235)

- **PATRÓN** `dist_vwap_pct` > `0.1669` → IC=+0.245 (n=907)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1669 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.508` → IC=+0.241 (n=1031)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.508 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.307` → IC=+0.238 (n=2509)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.307 (IC base=+0.235)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.2012` → IC=-0.298 (n=369)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.2012
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=1110)

- **FILTRO** `drift_60min` |x|> `0.2016` → IC=-0.295 (n=369)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2016
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=1110)

- **FILTRO** `drift_15min` |x|> `1.0228` → IC=-0.306 (n=369)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.0228
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=1110)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.242 (n=351)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=1128)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.188 (n=46)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.206)

- **PATRÓN** `ibs_15` > `0.9231` → IC=+0.380 (n=23)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9231 (IC base=-0.206)

- **PATRÓN** `dist_vwap_pct` < `0.4298` → IC=+0.158 (n=77)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.4298 (IC base=-0.206)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 37.0 (IC base=-0.206)

- **PATRÓN** `ibs_15` < `0.381` → IC=+0.295 (n=1007)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.381 (IC base=-0.025)

- **PATRÓN** `dist_vwap_pct` < `0.2022` → IC=+0.257 (n=918)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2022 (IC base=-0.025)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0142` → IC=-0.250 (n=1154)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0142
  - _Potencial_: sin este filtro IC_bueno=-0.162 (n=569)

- **FILTRO** `drift_60min` |x|> `0.1231` → IC=-0.244 (n=584)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1231
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=1139)

- **FILTRO** `drift_15min` |x|> `1.2906` → IC=-0.285 (n=430)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2906
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=1293)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=1702)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.221)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.221)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0705` → IC=+0.284 (n=1255)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0705 (IC base=-0.008)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1185` → IC=+0.288 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1185 (IC base=-0.008)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.294 (n=1415)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.008)

- **PATRÓN** `dist_vwap_pct` > `0.786` → IC=+0.325 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.786 (IC base=-0.008)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.161 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0063 (IC base=+0.086)

- **PATRÓN** `drift_15min` |x|≤ `0.7315` → IC=+0.151 (n=64)

  - _Acción_: Kelly boost +0.76€ cuando `drift_15min` |x|≤ 0.7315 (IC base=+0.086)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.235` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.235 (IC base=+0.086)

- **PATRÓN** `ibs_15` > `0.8692` → IC=+0.333 (n=22)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8692 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` < `0.0949` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0949 (IC base=+0.086)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 49.0 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` > `0.1929` → IC=+0.135 (n=94)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.1929 (IC base=+0.050)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.161 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0063 (IC base=+0.086)

- **PATRÓN** `drift_15min` |x|≤ `0.7315` → IC=+0.151 (n=64)

  - _Acción_: Kelly boost +0.76€ cuando `drift_15min` |x|≤ 0.7315 (IC base=+0.086)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.235` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.235 (IC base=+0.086)

- **PATRÓN** `ibs_15` > `0.8692` → IC=+0.333 (n=22)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8692 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` < `0.0949` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0949 (IC base=+0.086)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 49.0 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` > `0.1929` → IC=+0.135 (n=94)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.1929 (IC base=+0.050)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.302 (n=502)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0035 (IC base=+0.285)

- **PATRÓN** `sigma_h` > `0.0067` → IC=+0.292 (n=502)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0067 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.0714` → IC=+0.309 (n=662)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0714 (IC base=+0.285)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1493` → IC=+0.287 (n=1003)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1493 (IC base=+0.285)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2171` → IC=+0.290 (n=926)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2171 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.296 (n=1569)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.285)

- **PATRÓN** `ibs_15` > `0.8361` → IC=+0.311 (n=1505)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8361 (IC base=+0.285)

- **PATRÓN** `dist_vwap_pct` > `0.2755` → IC=+0.315 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2755 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.6` → IC=+0.387 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.6 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `13074.8557` → IC=+0.300 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13074.8557 (IC base=+0.285)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.308 (n=264)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.279)

- **PATRÓN** `drift_60min` |x|≤ `0.076` → IC=+0.300 (n=348)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.076 (IC base=+0.279)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2692` → IC=+0.282 (n=264)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2692 (IC base=+0.279)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2268` → IC=+0.290 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2268 (IC base=+0.279)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.303 (n=729)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.279)

- **PATRÓN** `ibs_15` > `0.8549` → IC=+0.308 (n=707)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8549 (IC base=+0.279)

- **PATRÓN** `dist_vwap_pct` > `0.2612` → IC=+0.310 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2612 (IC base=+0.279)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.43` → IC=+0.393 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.43 (IC base=+0.279)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.281 (n=1024)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `14481.4604` → IC=+0.309 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14481.4604 (IC base=+0.279)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.301 (n=315)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.291)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.292 (n=238)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.0506` → IC=+0.326 (n=239)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0506 (IC base=+0.291)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0644` → IC=+0.295 (n=714)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0644 (IC base=+0.291)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1009` → IC=+0.310 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1009 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.297 (n=639)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.291)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.292 (n=359)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.291)

- **PATRÓN** `ibs_15` > `0.8452` → IC=+0.317 (n=714)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8452 (IC base=+0.291)

- **PATRÓN** `dist_vwap_pct` > `0.2913` → IC=+0.315 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2913 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.851` → IC=+0.382 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.851 (IC base=+0.291)

### UPDOWN_OU_5M
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1078` → IC=-0.161 (n=237)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1078
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=117)

- **FILTRO** `ballena_activa_n` > `31.0` → IC=-0.146 (n=272)

  - _Acción_: SKIP cuando `ballena_activa_n` > 31.0
  - _Potencial_: sin este filtro IC_bueno=-0.096 (n=92)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.162 (n=128)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=385)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.191 (n=166)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.114 (n=86)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `sigma_h` < `0.0065` → IC=-0.447 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0065
  - _Potencial_: sin este filtro IC_bueno=-0.375 (n=6)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1431` → IC=-0.155 (n=56)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1431
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=170)

- **FILTRO** `sigma_h` < `0.006` → IC=-0.167 (n=49)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.006
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=17)

- **FILTRO** `drift_15min` |x|> `0.4064` → IC=-0.278 (n=16)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.4064
  - _Potencial_: sin este filtro IC_bueno=-0.096 (n=50)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1667` → IC=-0.167 (n=22)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1667
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=45)

- **FILTRO** `sigma_h` < `0.0052` → IC=-0.315 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0052
  - _Potencial_: sin este filtro IC_bueno=-0.300 (n=13)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1729` → IC=-0.273 (n=20)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1729
  - _Potencial_: sin este filtro IC_bueno=-0.128 (n=41)

- **FILTRO** `sigma_h` > `0.0115` → IC=-0.265 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0115
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=46)

- **FILTRO** `sigma_h` < `0.0063` → IC=-0.243 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=34)

- **FILTRO** `drift_15min` |x|> `0.5336` → IC=-0.250 (n=22)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.5336
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=45)

### WEEKLY_PRICE
- **PATRÓN** `ratio` < `0.9866` → IC=+0.252 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9866 (IC base=+0.122)

- **PATRÓN** `T_h` > `115.2222` → IC=+0.355 (n=3367)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 115.2222 (IC base=+0.332)

- **PATRÓN** `ratio` > `1.0158` → IC=+0.385 (n=642)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0158 (IC base=+0.332)

### WEEKLY_PRICE#BTC
- **PATRÓN** `ratio` < `0.9756` → IC=+0.190 (n=217)

  - _Acción_: Kelly boost +0.95€ cuando `ratio` < 0.9756 (IC base=+0.064)

- **PATRÓN** `T_h` > `109.838` → IC=+0.327 (n=1233)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 109.838 (IC base=+0.303)

- **PATRÓN** `ratio` > `1.0005` → IC=+0.294 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0005 (IC base=+0.303)

### WEEKLY_PRICE#ETH
- **PATRÓN** `ratio` < `0.9775` → IC=+0.361 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9775 (IC base=+0.185)

- **PATRÓN** `T_h` > `111.9928` → IC=+0.350 (n=1225)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9928 (IC base=+0.315)

- **PATRÓN** `ratio` > `1.0227` → IC=+0.405 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0227 (IC base=+0.315)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0386` → IC=+0.411 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0386 (IC base=+0.396)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.551 sube el IC de +0.132 a +0.207 en UPDOWN_GBM#15min (n=5919). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.702 sube el IC de +0.206 a +0.275 en UPDOWN_GBM#BTC#15min (n=896). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.4799 sube el IC de +0.133 a +0.218 en UPDOWN_GBM#ETH#15min (n=1149). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.697 sube el IC de +0.137 a +0.232 en UPDOWN_GBM#XRP#15min (n=1117). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6306 sube el IC de -0.087 a +0.280 en UPDOWN_GBM_15M_TARDIO (n=1354). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.376 sube el IC de +0.002 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=6080). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7545 sube el IC de +0.065 a +0.318 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=486). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6283 sube el IC de -0.180 a +0.291 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=84). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5657 sube el IC de +0.149 a +0.243 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=684). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.1923 sube el IC de +0.235 a +0.296 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1591). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.9231 sube el IC de -0.206 a +0.380 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.381 sube el IC de -0.025 a +0.295 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=1007). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.221 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.008 a +0.294 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=1415). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8692 sube el IC de +0.086 a +0.333 en UPDOWN_GBM_ETH_15M_HORA7 (n=22). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8692 sube el IC de +0.086 a +0.333 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=22). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8361 sube el IC de +0.285 a +0.311 en UPDOWN_GBM_IBS_ALTO (n=1505). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8549 sube el IC de +0.279 a +0.308 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=707). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8452 sube el IC de +0.291 a +0.317 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=714). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7881 sube el IC de +0.364 a +0.394 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=821). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8057 sube el IC de +0.363 a +0.384 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=393). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7632 sube el IC de +0.364 a +0.398 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=428). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2365 | +0.084 | +256.55€ | 1 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2365 | +0.084 | +256.55€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1953 | +0.085 | +217.06€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1953 | +0.085 | +217.06€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 285 | +0.068 | +10.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 285 | +0.068 | +10.79€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 96 | +0.122 | +29.03€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 96 | +0.122 | +29.03€ | 0 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 1496 | -0.029 | +52.57€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 1496 | -0.029 | +52.57€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 1172 | -0.041 | +39.92€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 1172 | -0.041 | +39.92€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 224 | +0.035 | +20.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 224 | +0.035 | +20.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 93 | -0.037 | -10.65€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 93 | -0.037 | -10.65€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 51589 | -0.086 | -6583.23€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 3390 | +0.096 | -314.42€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 48199 | -0.099 | -6268.82€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 5088 | -0.116 | -816.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 5088 | -0.116 | -816.49€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 3390 | +0.096 | -314.42€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 3390 | +0.096 | -314.42€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 5129 | -0.108 | -957.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 5129 | -0.108 | -957.76€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 14410 | -0.044 | -1324.09€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 14410 | -0.044 | -1324.09€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 14135 | -0.121 | -1627.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 14135 | -0.121 | -1627.38€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 9437 | -0.138 | -1543.09€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 9437 | -0.138 | -1543.09€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 57566 | -0.012 | +2598.35€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 14845 | +0.004 | +1475.98€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 42721 | -0.017 | +1122.37€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 57566 | -0.012 | +2598.35€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 14845 | +0.004 | +1475.98€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 42721 | -0.017 | +1122.37€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 214238 | +0.112 | -8785.19€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 23547 | +0.179 | -751.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 1000 | +0.022 | -79.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 177535 | +0.105 | -7556.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 12156 | +0.095 | -397.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 29439 | +0.101 | -2104.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 89 | -0.192 | +10.74€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 29313 | +0.102 | -2124.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#60min | 22 | +0.167 | +21.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 40091 | +0.123 | -629.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5729 | +0.176 | -231.53€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 29388 | +0.119 | -212.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4932 | +0.081 | -163.66€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 29487 | +0.098 | -2084.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 110 | -0.098 | +22.87€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 29349 | +0.099 | -2100.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#60min | 13 | -0.065 | +4.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 45863 | +0.123 | -978.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 11416 | +0.177 | -325.60€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 29864 | +0.106 | -561.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 4571 | +0.103 | -82.38€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 39909 | +0.111 | -1690.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 6103 | +0.200 | -241.08€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 903 | +0.046 | -25.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 30288 | +0.095 | -1244.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2615 | +0.108 | -179.27€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO#XRP | 29449 | +0.106 | -1298.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 100 | -0.137 | +13.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 29333 | +0.107 | -1314.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 34934 | +0.188 | -2666.18€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 34934 | +0.188 | -2666.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 7915 | +0.160 | -955.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 7915 | +0.160 | -955.85€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 5263 | +0.193 | -231.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 5263 | +0.193 | -231.85€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 7718 | +0.171 | -720.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 7718 | +0.171 | -720.40€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 6393 | +0.252 | -225.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 6393 | +0.252 | -225.82€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 7566 | +0.182 | -546.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 7566 | +0.182 | -546.01€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1341 | +0.425 | -51.61€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1341 | +0.425 | -51.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 572 | +0.439 | -5.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 572 | +0.439 | -5.23€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 528 | +0.421 | -23.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 528 | +0.421 | -23.69€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 227 | +0.400 | -18.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 227 | +0.400 | -18.82€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 123463 | +0.199 | -9087.70€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 123463 | +0.199 | -9087.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 21409 | +0.174 | -2549.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 21409 | +0.174 | -2549.85€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 19890 | +0.223 | -670.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 19890 | +0.223 | -670.90€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 21171 | +0.180 | -2237.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 21171 | +0.180 | -2237.86€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 20075 | +0.217 | -792.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 20075 | +0.217 | -792.53€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 20364 | +0.205 | -1206.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 20364 | +0.205 | -1206.96€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 20554 | +0.196 | -1629.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 20554 | +0.196 | -1629.61€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 48017 | +0.117 | +416.63€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 48017 | +0.117 | +416.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 23914 | +0.117 | +274.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 23914 | +0.117 | +274.99€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 24103 | +0.116 | +141.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 24103 | +0.116 | +141.64€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2717 | +0.294 | -7.95€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2717 | +0.294 | -7.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1243 | +0.283 | -25.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1243 | +0.283 | -25.31€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1332 | +0.297 | +10.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1332 | +0.297 | +10.63€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 142 | +0.347 | +6.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 142 | +0.347 | +6.73€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 1258 | +0.438 | -5.42€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 1258 | +0.438 | -5.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 600 | +0.435 | -7.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 600 | +0.435 | -7.20€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 606 | +0.441 | +0.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 606 | +0.441 | +0.37€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 52 | +0.407 | +1.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 52 | +0.407 | +1.41€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 2061 | +0.062 | -111.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1336 | +0.071 | -47.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1627 | +0.068 | -66.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1336 | +0.071 | -47.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 98210 | +0.101 | -2066.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 7971 | +0.098 | +196.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 90239 | +0.101 | -2263.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 53582 | +0.105 | -430.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 7971 | +0.098 | +196.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 45611 | +0.106 | -626.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 21138 | +0.110 | -72.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 21138 | +0.110 | -72.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 23490 | +0.082 | -1564.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 23490 | +0.082 | -1564.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 928 | +0.181 | -107.94€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 928 | +0.181 | -107.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 928 | +0.181 | -107.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 928 | +0.181 | -107.94€ | 1 | 4 |
| ✅ GBM_LATE_15M | 66915 | +0.102 | +37733.55€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 66915 | +0.102 | +37733.55€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 11116 | +0.224 | +9520.55€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 11116 | +0.224 | +9520.55€ | 0 | 20 |
| ✅ GBM_LATE_15M#BTC | 10467 | +0.177 | +8477.00€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 10467 | +0.177 | +8477.00€ | 0 | 21 |
| ✅ GBM_LATE_15M#DOGE | 11971 | +0.206 | +9431.14€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 11971 | +0.206 | +9431.14€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 8843 | +0.063 | +3032.51€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 8843 | +0.063 | +3032.51€ | 1 | 17 |
| ✅ GBM_LATE_15M#SOL | 9271 | -0.025 | +2401.52€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 9271 | -0.025 | +2401.52€ | 4 | 15 |
| ✅ GBM_LATE_15M#XRP | 15247 | -0.019 | +4870.83€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 15247 | -0.019 | +4870.83€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 71032 | +0.088 | +41713.16€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 71032 | +0.088 | +41713.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 13792 | -0.001 | +7301.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 13792 | -0.001 | +7301.61€ | 3 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 15272 | +0.008 | +4260.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 15272 | +0.008 | +4260.39€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 9503 | +0.296 | +10891.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 9503 | +0.296 | +10891.43€ | 0 | 22 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 13595 | +0.020 | +4402.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 13595 | +0.020 | +4402.62€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 10792 | +0.051 | +5053.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 10792 | +0.051 | +5053.06€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 8078 | +0.313 | +9804.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 8078 | +0.313 | +9804.05€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 52647 | +0.179 | +43851.33€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 52647 | +0.179 | +43851.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 7978 | +0.239 | +7403.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 7978 | +0.239 | +7403.63€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 8402 | +0.141 | +6352.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 8402 | +0.141 | +6352.60€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 8472 | +0.223 | +7309.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 8472 | +0.223 | +7309.38€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 8995 | +0.131 | +7084.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 8995 | +0.131 | +7084.85€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 9925 | +0.124 | +7713.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 9925 | +0.124 | +7713.95€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 8875 | +0.232 | +7986.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 8875 | +0.232 | +7986.93€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 14545 | +0.126 | +7421.50€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 14545 | +0.126 | +7421.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 678 | +0.162 | +445.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 678 | +0.162 | +445.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3804 | +0.126 | +2049.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3804 | +0.126 | +2049.57€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 509 | +0.156 | +286.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 509 | +0.156 | +286.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 4259 | +0.127 | +2166.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 4259 | +0.127 | +2166.80€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 3940 | +0.101 | +1614.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 3940 | +0.101 | +1614.32€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1355 | +0.168 | +858.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1355 | +0.168 | +858.78€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 67209 | +0.190 | +56091.59€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#15min | 67209 | +0.190 | +56091.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 10633 | +0.249 | +10214.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 10633 | +0.249 | +10214.31€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 10796 | +0.143 | +7905.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 10796 | +0.143 | +7905.63€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 11390 | +0.234 | +10244.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 11390 | +0.234 | +10244.68€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 11118 | +0.146 | +8438.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 11118 | +0.146 | +8438.61€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 11849 | +0.129 | +8701.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 11849 | +0.129 | +8701.83€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 11423 | +0.240 | +10586.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 11423 | +0.240 | +10586.52€ | 0 | 23 |
| ✅ GBM_LATE_5M | 16989 | +0.220 | +14372.85€ | 0 | 26 |
| ✅ GBM_LATE_5M#5min | 16989 | +0.220 | +14372.85€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1948 | +0.253 | +1898.73€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1948 | +0.253 | +1898.73€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3335 | +0.210 | +2849.38€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3335 | +0.210 | +2849.38€ | 0 | 25 |
| ✅ GBM_LATE_5M#DOGE | 1591 | +0.218 | +1323.18€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1591 | +0.218 | +1323.18€ | 0 | 18 |
| ✅ GBM_LATE_5M#ETH | 4937 | +0.211 | +3913.49€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 4937 | +0.211 | +3913.49€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 3022 | +0.230 | +2680.78€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 3022 | +0.230 | +2680.78€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 2156 | +0.210 | +1707.29€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 2156 | +0.210 | +1707.29€ | 0 | 0 |
| ✅ GBM_LATE_60M | 6723 | +0.083 | +2349.08€ | 0 | 10 |
| ✅ GBM_LATE_60M#60min | 6723 | +0.083 | +2349.08€ | 0 | 0 |
| ✅ GBM_LATE_60M#BNB | 203 | +0.271 | +222.33€ | 0 | 0 |
| ✅ GBM_LATE_60M#BNB#60min | 203 | +0.271 | +222.33€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 2084 | +0.062 | +621.60€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 2084 | +0.062 | +621.60€ | 1 | 6 |
| ✅ GBM_LATE_60M#DOGE | 199 | +0.316 | +243.54€ | 0 | 0 |
| ✅ GBM_LATE_60M#DOGE#60min | 199 | +0.316 | +243.54€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH | 1937 | +0.056 | +594.70€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1937 | +0.056 | +594.70€ | 2 | 5 |
| ✅ GBM_LATE_60M#SOL | 2104 | +0.062 | +418.39€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 2104 | +0.062 | +418.39€ | 0 | 10 |
| ✅ GBM_LATE_60M#XRP | 196 | +0.338 | +248.53€ | 0 | 0 |
| ✅ GBM_LATE_60M#XRP#60min | 196 | +0.338 | +248.53€ | 0 | 26 |
| 🚫 GBM_LATE_60M_FADE | 807 | -0.244 | -33.19€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 807 | -0.244 | -33.19€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#BNB | 12 | +0.000 | +4.05€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#BNB#60min | 12 | +0.000 | +4.05€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 284 | -0.255 | -20.31€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 284 | -0.255 | -20.31€ | 6 | 0 |
| ✅ GBM_LATE_60M_FADE#DOGE | 9 | -0.061 | +0.70€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#DOGE#60min | 9 | -0.061 | +0.70€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 277 | -0.242 | -7.42€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 277 | -0.242 | -7.42€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 221 | -0.244 | -9.23€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 221 | -0.244 | -9.23€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 2576 | +0.090 | +677.89€ | 1 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 2576 | +0.090 | +677.89€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 940 | +0.070 | +237.73€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 940 | +0.070 | +237.73€ | 0 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#DOGE | 40 | +0.191 | +18.67€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#DOGE#60min | 40 | +0.191 | +18.67€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 832 | +0.053 | +160.11€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 832 | +0.053 | +160.11€ | 0 | 14 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 676 | +0.153 | +241.85€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 676 | +0.153 | +241.85€ | 2 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#XRP | 88 | +0.100 | +19.53€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#XRP#60min | 88 | +0.100 | +19.53€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN | 425 | +0.306 | +505.51€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 425 | +0.306 | +505.51€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 425 | +0.306 | +505.51€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 425 | +0.306 | +505.51€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 5022 | +0.095 | +1085.77€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 5022 | +0.095 | +1085.77€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 5022 | +0.095 | +1085.77€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 5022 | +0.095 | +1085.77€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M | 1910 | +0.019 | +109.44€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 1910 | +0.019 | +109.44€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 243 | +0.096 | +51.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 243 | +0.096 | +51.83€ | 0 | 5 |
| ✅ LIQUIDACIONES_15M#BTC | 360 | -0.014 | +7.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 360 | -0.014 | +7.00€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 143 | +0.045 | +22.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 143 | +0.045 | +22.85€ | 1 | 1 |
| ✅ LIQUIDACIONES_15M#ETH | 421 | +0.022 | +21.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 421 | +0.022 | +21.22€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 357 | -0.021 | +0.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 357 | -0.021 | +0.41€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 386 | +0.026 | +6.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 386 | +0.026 | +6.12€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4644 | +0.019 | +218.82€ | 4 | 3 |
| ✅ LIQUIDACIONES_5M#5min | 4644 | +0.019 | +218.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 241 | +0.002 | -6.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 241 | +0.002 | -6.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 868 | +0.016 | +50.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 868 | +0.016 | +50.30€ | 1 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 356 | +0.078 | +107.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 356 | +0.078 | +107.08€ | 0 | 5 |
| ✅ LIQUIDACIONES_5M#ETH | 1738 | +0.023 | +37.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1738 | +0.023 | +37.89€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 820 | +0.013 | +4.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 820 | +0.013 | +4.91€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 621 | -0.006 | +24.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 621 | -0.006 | +24.80€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2863 | -0.036 | -13.30€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2863 | -0.036 | -13.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 868 | -0.040 | -19.88€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 868 | -0.040 | -19.88€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 1036 | -0.017 | +17.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 1036 | -0.017 | +17.23€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 934 | -0.054 | -10.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 934 | -0.054 | -10.50€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#XRP | 20 | +0.045 | +0.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#XRP#60min | 20 | +0.045 | +0.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 21827 | -0.032 | -183.67€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 10592 | -0.030 | -64.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 11235 | -0.033 | -119.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 768 | -0.052 | -38.49€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 394 | -0.038 | -5.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 374 | -0.067 | -32.67€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 5899 | -0.024 | -5.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 2814 | -0.020 | +24.99€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 3085 | -0.028 | -30.29€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1978 | -0.034 | -10.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 1017 | -0.038 | -18.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 961 | -0.030 | +8.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 5022 | -0.031 | -45.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 2425 | -0.026 | +4.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 2597 | -0.035 | -50.02€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 4149 | -0.026 | +29.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 2023 | -0.028 | +2.66€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 2126 | -0.024 | +27.14€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 4011 | -0.043 | -114.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1919 | -0.048 | -71.51€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 2092 | -0.039 | -42.62€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 14662 | -0.012 | -218.19€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14662 | -0.012 | -218.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 3379 | -0.021 | -71.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 3379 | -0.021 | -71.38€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 3075 | -0.015 | -29.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 3075 | -0.015 | -29.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 77999 | -0.000 | +4175.95€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 77999 | -0.000 | +4175.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 14119 | +0.027 | +1963.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 14119 | +0.027 | +1963.05€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 10946 | -0.038 | -155.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 10946 | -0.038 | -155.25€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 14267 | +0.026 | +1578.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 14267 | +0.026 | +1578.46€ | 1 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 10919 | -0.054 | -290.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 10919 | -0.054 | -290.36€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 13237 | -0.004 | +377.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 13237 | -0.004 | +377.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 14511 | +0.020 | +702.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 14511 | +0.020 | +702.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7528 | -0.052 | -104.28€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7528 | -0.052 | -104.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1270 | -0.002 | -14.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1270 | -0.002 | -14.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 2174 | -0.058 | -19.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 2174 | -0.058 | -19.13€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 102 | -0.019 | -0.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 102 | -0.019 | -0.22€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 822 | -0.117 | -33.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 822 | -0.117 | -33.34€ | 6 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2288 | -0.065 | -9.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2288 | -0.065 | -9.52€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 872 | -0.018 | -27.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 872 | -0.018 | -27.81€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3388 | +0.003 | +0.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3388 | +0.003 | +0.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 133 | -0.033 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 133 | -0.033 | -0.70€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 200 | +0.005 | -2.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 200 | +0.005 | -2.99€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE | 139 | -0.004 | -2.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 139 | -0.004 | -2.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1327 | +0.006 | +6.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1327 | +0.006 | +6.88€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1392 | +0.006 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1392 | +0.006 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 197 | -0.013 | -0.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 197 | -0.013 | -0.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 190773 | -0.078 | +2104.80€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 190773 | -0.078 | +2104.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 33490 | -0.076 | +1909.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 33490 | -0.076 | +1909.17€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 28630 | -0.102 | -1447.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 28630 | -0.102 | -1447.12€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 33894 | -0.067 | +1650.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 33894 | -0.067 | +1650.49€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 28182 | -0.101 | -1007.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 28182 | -0.101 | -1007.20€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 33802 | -0.060 | +156.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 33802 | -0.060 | +156.49€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 32775 | -0.068 | +842.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 32775 | -0.068 | +842.98€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9411 | -0.035 | -183.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9411 | -0.035 | -183.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1014 | -0.017 | -18.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1014 | -0.017 | -18.55€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2212 | -0.046 | -29.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2212 | -0.046 | -29.54€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1010 | -0.021 | -30.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1010 | -0.021 | -30.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2684 | -0.023 | -30.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2684 | -0.023 | -30.37€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1316 | -0.063 | -30.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1316 | -0.063 | -30.57€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1175 | -0.040 | -43.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1175 | -0.040 | -43.93€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 2424 | +0.121 | +978.69€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 2288 | +0.124 | +966.10€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 528 | +0.141 | +273.90€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 528 | +0.141 | +273.90€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 480 | +0.120 | +175.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 480 | +0.120 | +175.48€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#ETH | 415 | +0.128 | +191.95€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 415 | +0.128 | +191.95€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 391 | +0.134 | +189.37€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 391 | +0.134 | +189.37€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 474 | +0.097 | +135.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 474 | +0.097 | +135.40€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 2553 | -0.022 | -50.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2553 | -0.022 | -50.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 448 | +0.007 | +21.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 448 | +0.007 | +21.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 465 | -0.050 | -34.02€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 465 | -0.050 | -34.02€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 616 | -0.045 | -45.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 616 | -0.045 | -45.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 530 | -0.007 | -4.03€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 530 | -0.007 | -4.03€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 494 | -0.010 | +11.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 494 | -0.010 | +11.40€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1357 | -0.042 | +140.17€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 628 | -0.068 | +27.22€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 490 | -0.065 | +52.09€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 138 | -0.079 | -24.87€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 477 | -0.009 | +74.76€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 346 | +0.009 | +84.45€ | 0 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 131 | -0.056 | -9.68€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 252 | -0.039 | +38.18€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 214 | -0.037 | +33.77€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 38 | -0.050 | +4.42€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 1050 | -0.035 | +170.30€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 307 | -0.066 | -30.13€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE | 1718 | -0.185 | -33.10€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 680 | -0.173 | -7.47€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 601 | -0.172 | -4.30€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 79 | -0.179 | -3.17€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH | 577 | -0.198 | -32.47€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 508 | -0.204 | -37.58€ | 3 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 69 | -0.148 | +5.11€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 461 | -0.185 | +6.84€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 427 | -0.181 | +3.70€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 34 | -0.222 | +3.14€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#atexpiry | 1536 | -0.185 | -38.18€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 182 | -0.179 | +5.08€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 606 | +0.373 | +534.00€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#BTC | 141 | +0.178 | +100.38€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 141 | +0.178 | +100.38€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#ETH | 138 | +0.371 | +107.96€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 138 | +0.371 | +107.96€ | 0 | 6 |
| ✅ RESOLUTION_SNIPER#SOL | 327 | +0.454 | +325.67€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 327 | +0.454 | +325.67€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 606 | +0.373 | +534.00€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 1061 | +0.040 | +86.43€ | 2 | 3 |
| ✅ STREAK_FADE_15M#15min | 1061 | +0.040 | +86.43€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 359 | +0.015 | +2.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 359 | +0.015 | +2.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 80 | +0.024 | +1.80€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 80 | +0.024 | +1.80€ | 1 | 1 |
| ✅ STREAK_FADE_15M#SOL | 86 | +0.034 | +8.76€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 86 | +0.034 | +8.76€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 536 | +0.059 | +73.53€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 536 | +0.059 | +73.53€ | 0 | 3 |
| ✅ STREAK_FADE_5M | 3673 | -0.022 | -141.64€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3673 | -0.022 | -141.64€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1130 | -0.022 | -39.63€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1130 | -0.022 | -39.63€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 633 | -0.028 | -26.83€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 633 | -0.028 | -26.83€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 181 | -0.041 | -14.74€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 181 | -0.041 | -14.74€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1729 | -0.019 | -60.45€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1729 | -0.019 | -60.45€ | 1 | 0 |
| ✅ STREAK_FADE_60M | 155 | +0.016 | +1.10€ | 2 | 2 |
| ✅ STREAK_FADE_60M#60min | 155 | +0.016 | +1.10€ | 0 | 0 |
| ✅ STREAK_FADE_60M#BNB | 7 | +0.097 | +7.39€ | 0 | 0 |
| ✅ STREAK_FADE_60M#BNB#60min | 7 | +0.097 | +7.39€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 51 | -0.028 | -2.40€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 51 | -0.028 | -2.40€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 89 | +0.005 | -5.00€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 89 | +0.005 | -5.00€ | 1 | 1 |
| ✅ STREAK_FADE_60M#XRP | 5 | +0.018 | -0.23€ | 0 | 0 |
| ✅ STREAK_FADE_60M#XRP#60min | 5 | +0.018 | -0.23€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 11729 | +0.013 | +65.36€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11729 | +0.013 | +65.36€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 3011 | +0.017 | +21.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 3011 | +0.017 | +21.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 3139 | +0.013 | +25.79€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 3139 | +0.013 | +25.79€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2957 | +0.009 | -0.63€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2957 | +0.009 | -0.63€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2622 | +0.014 | +18.81€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2622 | +0.014 | +18.81€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 14058 | +0.019 | +11.81€ | 4 | 0 |
| ✅ STRUCT_NO_15M#15min | 14058 | +0.019 | +11.81€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 5631 | +0.021 | +8.66€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 5631 | +0.021 | +8.66€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 4998 | +0.020 | +4.83€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 4998 | +0.020 | +4.83€ | 4 | 0 |
| ✅ STRUCT_NO_15M#SOL | 3429 | +0.015 | -1.68€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 3429 | +0.015 | -1.68€ | 1 | 0 |
| ✅ UPDOWN_GBM | 127204 | +0.060 | +12124.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 31785 | +0.077 | +6216.61€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 3608 | -0.001 | +39.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 83776 | +0.062 | +5744.53€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 7601 | -0.002 | +126.87€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 11118 | +0.103 | +2058.32€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 2111 | +0.165 | +994.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 8917 | +0.090 | +1066.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 28793 | +0.056 | +2533.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 4280 | +0.081 | +960.34€ | 0 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 1064 | +0.000 | +21.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 19862 | +0.065 | +1463.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 3431 | -0.004 | +83.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 156 | -0.063 | +4.33€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 14208 | +0.074 | +1571.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 2084 | +0.155 | +893.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 12038 | +0.060 | +679.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 29835 | +0.049 | +2130.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 7381 | +0.070 | +1158.38€ | 0 | 9 |
| ✅ UPDOWN_GBM#ETH#240min | 1028 | +0.005 | +14.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 18472 | +0.051 | +915.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2809 | -0.002 | +39.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 145 | -0.099 | +2.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 26254 | +0.041 | +1502.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 8582 | +0.032 | +476.66€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 943 | -0.011 | +7.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 15274 | +0.054 | +1021.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1324 | +0.002 | +5.33€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 131 | -0.139 | -8.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 16994 | +0.072 | +2329.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 7347 | +0.088 | +1733.68€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 9213 | +0.063 | +598.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#60min | 37 | -0.013 | -0.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 432 | -0.099 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 1094 | +0.364 | +419.70€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 1094 | +0.364 | +419.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 524 | +0.363 | +189.40€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 524 | +0.363 | +189.40€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 570 | +0.364 | +230.31€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 570 | +0.364 | +230.31€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 30133 | -0.016 | +7609.36€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 30133 | -0.016 | +7609.36€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 2376 | -0.044 | +645.50€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 2376 | -0.044 | +645.50€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 5556 | -0.114 | +334.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 5556 | -0.114 | +334.74€ | 4 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1294 | +0.218 | +1063.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1294 | +0.218 | +1063.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 4091 | +0.216 | +2576.60€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 4091 | +0.216 | +2576.60€ | 1 | 20 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 8460 | -0.057 | +1282.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 8460 | -0.057 | +1282.56€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 8356 | -0.052 | +1706.92€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 8356 | -0.052 | +1706.92€ | 4 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 383 | +0.058 | +34.37€ | 0 | 7 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 383 | +0.058 | +34.37€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 383 | +0.058 | +34.37€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 383 | +0.058 | +34.37€ | 0 | 7 |
| ✅ UPDOWN_GBM_IBS_ALTO | 2006 | +0.285 | +1726.60€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 2006 | +0.285 | +1726.60€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 1054 | +0.279 | +853.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 1054 | +0.279 | +853.06€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 952 | +0.291 | +873.54€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 952 | +0.291 | +873.54€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 909 | -0.122 | -97.36€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 909 | -0.122 | -97.36€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 312 | -0.080 | -36.02€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 312 | -0.080 | -36.02€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 292 | -0.088 | -24.06€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 292 | -0.088 | -24.06€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 105 | -0.192 | -14.83€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 105 | -0.192 | -14.83€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 128 | -0.200 | -8.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 128 | -0.200 | -8.61€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 5471 | +0.291 | +2387.06€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 2139 | +0.247 | +336.00€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 2119 | +0.284 | +876.69€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 1213 | +0.382 | +1174.37€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.026 n=1546 — no justifica filtro, seguir monitorizando
  - _Datos_: n=1546 IC=+0.026 PNL=+76.94€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 857 celda(s) pasan gate riguroso completo de 3086 evaluadas (n>=40) y 4196 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.032 < 0.08 — monitorear
  - _Datos_: n=8579 IC=+0.032 PNL=+477.04€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=2119/15 IC=+0.284 PNL=+876.69€ | BTC: n=2139/15 IC=+0.247 PNL=+336.00€ | SOL: n=1213/15 IC=+0.382 PNL=+1174.37€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.137 n=1182/60 | contraria IC=+0.185 n=1250 | gap=-0.049 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=659, boost estimado=+0.009. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=2808/40 IC=-0.002 PNL=+39.66€ | BTC#60min: n=3429/40 IC=-0.004 PNL=+83.31€ | SOL#60min: n=1323/40 IC=+0.002 PNL=+5.84€ | XRP#60min: n=36/40 IC=+0.000 PNL=-0.31€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.044 n=847008 | tras_1loss IC=+0.103 n=640394 | tras_2loss IC=+0.074 n=254079/40 | gap=-0.030 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.150 > 0.08 con n=1319 PNL=+742.52€
  - _Datos_: n=1319 IC=+0.150 PNL=+742.52€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.124 > 0.08 con n=1533 PNL=+684.52€
  - _Datos_: n=1533 IC=+0.124 PNL=+684.52€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.111 > 0.08 con n=93 PNL=+33.51€
  - _Datos_: n=93 IC=+0.111 PNL=+33.51€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.330 > 0.1 con n=4491 PNL=+2532.17€
  - _Datos_: n=4491 IC=+0.330 PNL=+2532.17€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=1283 IC=+0.063 PNL=+127.63€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1283 IC=+0.063 PNL=+127.63€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=121 IC=+0.159 PNL=+69.74€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=121 IC=+0.159 PNL=+69.74€

**⏳ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: 30
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-OF-02H-BTCSOL** — ORDER_FLOW H=02h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 02h está en el blacklist basado en TODOS los pares. Con BTC+SOL solo, el historial muestra 4/5 (80%) IC=+0.054. ¿Se confirma la señal positiva con más datos?
  - _Umbral_: 15
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 02h del blacklist ORDER_FLOW
  - _Estado_: 7/15 ops en el filtro definido (IC actual=+0.097 PNL=+9.02€)
  - _Datos_: n=7 IC=+0.097 PNL=+9.02€

**⏳ H-CUSTOM-OF-07H-BTCSOL** — ORDER_FLOW H=07h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 07h está en el blacklist. Con BTC+SOL solo, el historial muestra 7/12 (58%) IC=+0.043. El blacklist puede estar basado en pares negativos que ya están excluidos.
  - _Umbral_: 20
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 07h del blacklist ORDER_FLOW
  - _Estado_: 3/20 ops en el filtro definido (IC actual=-0.015 PNL=-2.12€)
  - _Datos_: n=3 IC=-0.015 PNL=-2.12€
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: 07h sigue en ORDER_FLOW_BLACKLIST_HOURS -- mientras siga ahí, nunca genera fila para volver a evaluarse (26-Ago, triage candidatas estancadas)

**〰️ H-CUSTOM-GBM-60MIN-BUYYES** — GBM 60min BUY_YES — ¿edge superior al BUY_NO?
  - _Hipótesis_: Análisis actual muestra BUY_YES 60min: 22/36 (61%) IC=+0.105 vs BUY_NO 60min: 8/14 (57%) IC=+0.044. En 60min parece que BUY_YES es la dirección dominante, al contrario que en 15min.
  - _Umbral_: n≥30 y IC>+0.08
  - _Acción_: Si BUY_YES 60min confirma IC≥0.10 n≥40 → prioridad live por encima de BUY_NO
  - _Estado_: n=4973 IC=-0.010 PNL=-71.35€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4973 IC=-0.010 PNL=-71.35€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=2623 IC=+0.012 PNL=+199.84€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=2623 IC=+0.012 PNL=+199.84€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=1546 IC=+0.026 PNL=+76.94€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=1546 IC=+0.026 PNL=+76.94€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.132 > 0.1 con n=8828 PNL=+4168.71€
  - _Datos_: n=8828 IC=+0.132 PNL=+4168.71€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=4278 IC=+0.081 PNL=+960.33€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=4278 IC=+0.081 PNL=+960.33€

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
  - _Estado_: n=1722 IC=+0.042 PNL=+140.19€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=1722 IC=+0.042 PNL=+140.19€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=214 IC=-0.023 PNL=-5.78€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=214 IC=-0.023 PNL=-5.78€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.306 n=425) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=425 IC=+0.306 PNL=+505.51€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.117 > 0.02 con n=1414 PNL=+564.30€
  - _Datos_: n=1414 IC=+0.117 PNL=+564.30€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=289 IC=-0.122 PNL=+2.67€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=289 IC=-0.122 PNL=+2.67€

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
  - _Estado_: n=52303 IC=+0.069 PNL=+6981.19€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=52303 IC=+0.069 PNL=+6981.19€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.120 < -0.1 con n=869 PNL=+151.79€
  - _Datos_: n=869 IC=-0.120 PNL=+151.79€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=5111 IC=+0.066 PNL=+600.96€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=5111 IC=+0.066 PNL=+600.96€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=219 IC=-0.093 PNL=+1.81€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=219 IC=-0.093 PNL=+1.81€

**〰️ H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: n=1384 IC=+0.100 PNL=+332.76€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1384 IC=+0.100 PNL=+332.76€

**⏳ H-CUSTOM-ETH15-BUYNO-PRECIO-ALTO** — ETH#15min BUY_NO con precio_yes>0.55 pierde (NO longshot contra favorito)
  - _Hipótesis_: Detectado 2026-07-02: ult.60 shadow ETH15 BUY_NO — py_mkt~0.5 wr=0.67 PNL=+29.3 (n=49); py_mkt 0.6-0.8 wr 0.33-0 PNL=-5.75 (n=9). Filtro RETURN NONE (no SKIP) aplicado en shadow_predict.py (PY_MKT_MAX_BUY_NO_ETH15=0.55) el mismo dia -- bloquea la GENERACIÓN de la fila, no solo la decisión. Esta hipotesis trackea la zona filtrada: si las ops que HABRIAN caido aqui siguen apareciendo en otras estrategias o el IC forward de la zona se vuelve positivo, revisar el filtro. CAVEAT: n=9, muestra chica — el filtro se aplico por asimetria de riesgo (afecta a dinero live), no por significancia. ⚠️ 05-Ago (fix): la clave del filtro decía 'py_mkt', que NUNCA existió ni en features de UPDOWN_GBM (T_h/delta_ratio_macro/drift_15min/drift_60min/pct_spot_vs_ref/sigma_h) ni como columna top-level de results.csv -- corregida a 'precio_yes_mercado' (columna real). Aun así, con la clave correcta esta hipótesis NUNCA podrá acumular n mientras el filtro RETURN NONE siga activo -- es el mismo patrón 'frozen by design' que H-CUSTOM-LATE15-PHOTO-FINISH (más abajo): la propia protección impide generar los datos necesarios para volver a evaluarla. Para monitorearla de verdad haría falta un logger separado que capture la señal SIN aplicar el filtro (mismo patrón que gate_bucket_propio con data/markets histórico) -- no construido, pendiente decisión.
  - _Umbral_: 20
  - _Acción_: Si IC forward de la zona >0 con n>=20 → retirar filtro; si confirma negativo → considerar extender a BTC/SOL 15min
  - _Estado_: 8/20 ops en el filtro definido (IC actual=-0.040 PNL=-0.55€)
  - _Datos_: n=8 IC=-0.040 PNL=-0.55€
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: PY_MKT_MAX_BUY_NO_ETH15=0.55 en shadow_predict.py hace RETURN NONE (bloquea generación, no solo decisión) -- nunca podrá acumular n mientras siga activo. Haría falta un logger separado sin el filtro para monitorear de verdad (no construido, 26-Ago)

**〰️ H-PRECIO-YES-BARATO** — BUY_YES con precio de mercado 0.30-0.40 — mercado infravalora YES
  - _Hipótesis_: Detectado 2026-07-03 en benchmark de calibración del mercado (7d, estrategias GBM): en el bucket precio_yes_mercado [0.3-0.4) la frecuencia real de YES fue 0.45 vs 0.35 implícito (+0.10, n=38). Posible sesgo favorito-longshot suave en binarios de 15min (complemento del LONGSHOT ya activo para BUY_NO con py<0.20). Si se confirma, BUY_YES comprado en esa banda lleva viento de cola estructural del propio mercado, independiente del modelo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → kelly_boost ×1.1 para BUY_YES con precio_yes_mercado en [0.30,0.40), simétrico al longshot BUY_NO existente
  - _Estado_: n=50673 IC=-0.137 PNL=+3273.52€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=50673 IC=-0.137 PNL=+3273.52€

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
  - _Estado_: n=5479 IC=+0.136 PNL=+3879.61€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=5479 IC=+0.136 PNL=+3879.61€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=13321 IC=+0.057 PNL=+1150.48€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=13321 IC=+0.057 PNL=+1150.48€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.103 > 0.08 con n=5548 PNL=+3154.57€
  - _Datos_: n=5548 IC=+0.103 PNL=+3154.57€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.219 < -0.1 con n=5555 PNL=-427.87€
  - _Datos_: n=5555 IC=-0.219 PNL=-427.87€

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
  - _Estado_: n=137 IC=+0.075 PNL=+23.44€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=137 IC=+0.075 PNL=+23.44€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.096 n=2568) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=2568 IC=+0.096 PNL=+504.61€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.411 n=698) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=698 IC=+0.411 PNL=+1017.29€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=21400 IC=+0.175 PNL=-2544.88€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=21400 IC=+0.175 PNL=-2544.88€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.229 > 0.1 con n=352 PNL=+242.40€
  - _Datos_: n=352 IC=+0.229 PNL=+242.40€
