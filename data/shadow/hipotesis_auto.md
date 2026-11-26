# Hipótesis automáticas — 2026-11-26 15:35 UTC
_Generado por shadow_postmortem.py sobre 1504143 resoluciones (PNL=+213554.49€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.239 (n=236)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=735)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.195 (n=1120)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.505 (IC base=+0.124)

- **PATRÓN** `n_total_lado` > `60.0` → IC=+0.173 (n=362)

  - _Acción_: Kelly boost +0.87€ cuando `n_total_lado` > 60.0 (IC base=+0.124)

- **PATRÓN** `banda_hit_calibrado` > `0.8116` → IC=+0.266 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8116 (IC base=+0.124)

- **PATRÓN** `banda_z` > `8.202` → IC=+0.193 (n=353)

  - _Acción_: Kelly boost +0.96€ cuando `banda_z` > 8.202 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.131 (n=1068)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 6.0 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=1149)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.124)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.280 (n=171)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=565)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.193 (n=983)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.505 (IC base=+0.126)

- **PATRÓN** `n_total_lado` > `62.0` → IC=+0.184 (n=315)

  - _Acción_: Kelly boost +0.92€ cuando `n_total_lado` > 62.0 (IC base=+0.126)

- **PATRÓN** `banda_hit_calibrado` > `0.817` → IC=+0.280 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.817 (IC base=+0.126)

- **PATRÓN** `banda_z` > `8.273` → IC=+0.196 (n=310)

  - _Acción_: Kelly boost +0.98€ cuando `banda_z` > 8.273 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.138 (n=838)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 8.0 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.129 (n=1049)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `5101.7817` → IC=+0.130 (n=420)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 5101.7817 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `8586.1585` → IC=+0.129 (n=251)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 8586.1585 (IC base=+0.018)

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
- **FILTRO** `restante_s_al_confirmar` < `130.46` → IC=-0.218 (n=12954)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.46
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=38865)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `122.97` → IC=-0.263 (n=1272)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 122.97
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3816)

### BALLENAS_TARDIAS#BTC#15min
- **PATRÓN** `restante_s_al_confirmar` < `641.33` → IC=+0.136 (n=2566)

  - _Acción_: Kelly boost +0.68€ cuando `restante_s_al_confirmar` < 641.33 (IC base=+0.093)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `114.34` → IC=-0.279 (n=1281)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 114.34
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=3848)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `116.04` → IC=-0.159 (n=3652)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 116.04
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=10957)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.208 (n=31166)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `7702.5889` → IC=+0.151 (n=2532)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 7702.5889 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.127 (n=27727)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.129 (n=33665)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.123)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.224 (n=25073)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=8989)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.123)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.182 (n=2243)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.358 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.174)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.176 (n=2745)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.01 (IC base=+0.174)

- **PATRÓN** `libro_liquidez` > `16184.2491` → IC=+0.182 (n=713)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 16184.2491 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.184 (n=1960)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 7.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.181 (n=2196)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 17.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.328 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.177)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.180 (n=2806)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `15988.2314` → IC=+0.185 (n=725)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 15988.2314 (IC base=+0.177)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.172 (n=692)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` > 0.61 (IC base=+0.074)

- **PATRÓN** `libro_liquidez` > `6825.0558` → IC=+0.126 (n=153)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 6825.0558 (IC base=+0.074)

- **PATRÓN** `py_entrada` < `0.45` → IC=+0.122 (n=2250)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.45 (IC base=+0.087)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.172 (n=5735)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 6.0 (IC base=+0.169)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.174 (n=2801)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 8.0 (IC base=+0.169)

- **PATRÓN** `py_entrada` > `0.78` → IC=+0.377 (n=1934)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.78 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.199 (n=2753)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 7.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.329 (n=1013)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.196 (n=3199)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.01 (IC base=+0.192)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=1563)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.142 (n=993)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 11.0 (IC base=+0.137)

- **PATRÓN** `py_entrada` > `0.65` → IC=+0.244 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.65 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=1217)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `2033.6955` → IC=+0.137 (n=992)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2033.6955 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `4420.281` → IC=+0.152 (n=156)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4420.281 (IC base=+0.077)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.253 (n=998)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.230)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.230 (n=2050)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.230)

- **PATRÓN** `py_entrada` > `0.837` → IC=+0.428 (n=1346)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.837 (IC base=+0.230)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.145 (n=1498)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 7.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.154 (n=766)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.144)

- **PATRÓN** `py_entrada` < `0.315` → IC=+0.295 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.315 (IC base=+0.144)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `py_entrada` > `0.55` → IC=+0.163 (n=490)

  - _Acción_: Kelly boost +0.81€ cuando `py_entrada` > 0.55 (IC base=+0.050)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.139 (n=555)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.136 (n=1083)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 12.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.255 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.125)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.295 (n=76)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=158)

- **FILTRO** `libro_liquidez` < `8957.4571` → IC=-0.263 (n=175)

  - _Acción_: SKIP cuando `libro_liquidez` < 8957.4571
  - _Potencial_: sin este filtro IC_bueno=-0.238 (n=59)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.197 (n=27819)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.192 (n=17588)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.220 (n=8828)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.336 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `8407.3041` → IC=+0.341 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8407.3041 (IC base=+0.191)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.165 (n=6334)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.160)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.161 (n=4001)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 11.0 (IC base=+0.160)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.173 (n=6123)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.209 (n=3943)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.204 (n=2632)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.244 (n=1874)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.203)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.179 (n=6170)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.172 (n=5230)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 15.0 (IC base=+0.171)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.174 (n=6326)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.73 (IC base=+0.171)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.180 (n=4858)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` > 0.71 (IC base=+0.171)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.256 (n=4874)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.251)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.251 (n=2363)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.251)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.362 (n=1680)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.8 (IC base=+0.251)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.251)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=6021)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.188 (n=3830)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 11.0 (IC base=+0.184)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.197 (n=1944)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.73 (IC base=+0.184)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.427 (n=1052)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.424)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.425 (n=1048)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.424)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=1059)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.424)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.430 (n=1121)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.424)

- **PATRÓN** `libro_liquidez` > `14027.0561` → IC=+0.450 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14027.0561 (IC base=+0.424)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.437 (n=459)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.438)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.443 (n=451)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.450 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.438)

- **PATRÓN** `libro_liquidez` > `15243.1529` → IC=+0.445 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15243.1529 (IC base=+0.438)

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
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.404 (n=164)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.395)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.396 (n=161)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.395)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.416 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.395)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.207 (n=36229)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.237 (n=35664)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.199)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.184 (n=5421)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 18.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.175 (n=11676)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 12.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.184 (n=16786)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.174)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.227 (n=15157)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.276 (n=6389)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.223)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.190 (n=6216)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.196 (n=12842)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.72 (IC base=+0.180)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.855` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.855
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.229 (n=5898)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.220 (n=5854)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.259 (n=6178)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.218)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `py_entrada` < `0.775` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `libro_liquidez` < `3197.0694` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 3197.0694
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.211 (n=13799)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.252 (n=6497)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.206)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.203 (n=6043)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.199 (n=6041)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.239 (n=7469)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=13032)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.138 (n=14370)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `3.31` → IC=+0.138 (n=16055)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.31 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=6334)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.143 (n=6537)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.126 (n=8085)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.73` → IC=+0.142 (n=8003)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 3.73 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=6698)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.115)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.134 (n=8650)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` > 4.95 (IC base=+0.115)

- **PATRÓN** `lag_apertura_s` < `2.87` → IC=+0.134 (n=8061)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 2.87 (IC base=+0.115)

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
- **FILTRO** `hora_utc` < `5.0` → IC=-0.286 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=133)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.275 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.163 (n=81)

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
- **FILTRO** `hora_utc` < `5.0` → IC=-0.286 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=133)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.275 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.163 (n=81)

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
- **PATRÓN** `drift_60min` |x|≤ `0.5109` → IC=+0.140 (n=20864)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.5109 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.128 (n=21138)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.126 (n=14539)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.973` → IC=+0.247 (n=6959)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.973 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.8853` → IC=+0.289 (n=1149)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8853 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.462` → IC=+0.189 (n=10465)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 3.462 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.6936` → IC=+0.267 (n=5710)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6936 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.3027` → IC=+0.254 (n=2155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3027 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.739` → IC=+0.233 (n=5048)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.739 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=10009)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `4970.6874` → IC=+0.150 (n=6955)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 4970.6874 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.123 (n=13231)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0067 (IC base=+0.087)

- **PATRÓN** `ibs_20min` < `0.5641` → IC=+0.144 (n=26408)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.5641 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.6835` → IC=+0.193 (n=1806)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.6835 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` < `0.1797` → IC=+0.194 (n=10862)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.1797 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` < `0.6922` → IC=+0.199 (n=4860)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 0.6922 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2962` → IC=+0.230 (n=2679)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2962 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.2838` → IC=+0.212 (n=8492)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2838 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.227 (n=18719)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.087)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3057` → IC=+0.213 (n=3897)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3057 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.214 (n=4660)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.209)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.212 (n=2965)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` > `0.9812` → IC=+0.273 (n=2007)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9812 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.43` → IC=+0.272 (n=1977)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.43 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.2335` → IC=+0.258 (n=774)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2335 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `1.4375` → IC=+0.212 (n=4258)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4375 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.221 (n=4618)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `2059.025` → IC=+0.213 (n=1476)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2059.025 (IC base=+0.209)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.244 (n=1830)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.0971` → IC=+0.266 (n=1345)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0971 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.238 (n=4198)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.243 (n=1853)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.0818` → IC=+0.274 (n=1345)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0818 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.955` → IC=+0.241 (n=4140)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.955 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.0727` → IC=+0.239 (n=3491)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0727 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2885` → IC=+0.246 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2885 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `1.8557` → IC=+0.242 (n=2578)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8557 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.241 (n=4344)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.237)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.232 (n=1272)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.1161` → IC=+0.244 (n=1673)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1161 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.231 (n=3993)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.220 (n=2718)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` > `0.8889` → IC=+0.246 (n=1268)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8889 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` > `0.2058` → IC=+0.228 (n=1651)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2058 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` < `0.5797` → IC=+0.220 (n=4198)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5797 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.687` → IC=+0.260 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.687 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` > `0.6957` → IC=+0.227 (n=3399)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6957 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.2761` → IC=+0.261 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2761 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `2.4328` → IC=+0.243 (n=1253)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4328 (IC base=+0.219)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.158 (n=3666)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0062 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.3652` → IC=+0.144 (n=4166)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3652 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.151 (n=1561)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.5915` → IC=+0.180 (n=3666)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.5915 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.7782` → IC=+0.142 (n=5034)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.7782 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.586` → IC=+0.139 (n=651)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 10.586 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.969` → IC=+0.142 (n=3839)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 3.969 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.6276` → IC=+0.157 (n=1389)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.6276 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.0977` → IC=+0.158 (n=1513)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.0977 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.443` → IC=+0.144 (n=4034)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.443 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=5412)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.186 (n=1337)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 166.0 (IC base=+0.136)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.210 (n=2130)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0119 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=4943)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.252 (n=1812)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.879` → IC=+0.276 (n=1038)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.879 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` < `0.0969` → IC=+0.193 (n=4210)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0969 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.3499` → IC=+0.223 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3499 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.7298` → IC=+0.210 (n=2081)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7298 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=5543)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `1902.1784` → IC=+0.201 (n=2127)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1902.1784 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.226 (n=1946)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.220)

- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.221 (n=1998)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.3084` → IC=+0.229 (n=2939)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3084 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.240 (n=1661)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.226 (n=2008)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` < `0.0544` → IC=+0.268 (n=1470)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0544 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.611` → IC=+0.266 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.611 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.3459` → IC=+0.252 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3459 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` < `1.7598` → IC=+0.218 (n=1875)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7598 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.1534` → IC=+0.231 (n=2841)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1534 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.223 (n=2041)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `1882.5784` → IC=+0.223 (n=1998)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1882.5784 (IC base=+0.220)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.220 (n=4228)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=+0.220)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.165 (n=261)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=5665)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.138 (n=761)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0041 (IC base=+0.070)

- **PATRÓN** `ibs_20min` > `0.9414` → IC=+0.247 (n=761)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9414 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.1609` → IC=+0.348 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1609 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` < `0.3787` → IC=+0.342 (n=897)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3787 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.225` → IC=+0.216 (n=1673)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.225 (IC base=+0.070)

- **PATRÓN** `volumen_regimen` < `0.8693` → IC=+0.342 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8693 (IC base=+0.070)

- **PATRÓN** `volumen_regimen` > `1.2469` → IC=+0.360 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2469 (IC base=+0.070)

- **PATRÓN** `volumen_pendiente_norm` < `0.1649` → IC=+0.347 (n=762)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1649 (IC base=+0.070)

- **PATRÓN** `volumen_pendiente_norm` > `0.2994` → IC=+0.357 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2994 (IC base=+0.070)

- **PATRÓN** `volumen_spike_ratio` < `1.4165` → IC=+0.367 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4165 (IC base=+0.070)

- **PATRÓN** `volumen_spike_ratio` > `2.2709` → IC=+0.349 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2709 (IC base=+0.070)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.348 (n=929)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 143.0 (IC base=+0.070)

- **PATRÓN** `ibs_20min` < `0.0862` → IC=+0.187 (n=1482)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.0862 (IC base=+0.060)

- **PATRÓN** `dist_vwap_pct` > `0.3684` → IC=+0.157 (n=735)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.3684 (IC base=+0.060)

- **PATRÓN** `dist_vwap_pct` < `0.1556` → IC=+0.155 (n=2801)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1556 (IC base=+0.060)

- **PATRÓN** `volumen_regimen` < `0.8255` → IC=+0.162 (n=1955)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8255 (IC base=+0.060)

- **PATRÓN** `volumen_pendiente_norm` > `0.278` → IC=+0.197 (n=374)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.278 (IC base=+0.060)

- **PATRÓN** `volumen_spike_ratio` > `2.4311` → IC=+0.170 (n=942)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.4311 (IC base=+0.060)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.181 (n=164)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=913)

- **FILTRO** `ibs_20min` < `0.275` → IC=-0.183 (n=269)

  - _Acción_: SKIP cuando `ibs_20min` < 0.275
  - _Potencial_: sin este filtro IC_bueno=+0.090 (n=808)

- **FILTRO** `ibs_20min` > `0.1923` → IC=-0.124 (n=5560)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1923
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=2752)

- **FILTRO** `sigma_ewma_delta_pct` > `8.311` → IC=-0.228 (n=901)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.311
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=7411)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.179 (n=369)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.75 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` > `0.993` → IC=+0.279 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.993 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` < `1.3876` → IC=+0.266 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 1.3876 (IC base=+0.022)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.289` → IC=+0.144 (n=363)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 2.289 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` > `1.0067` → IC=+0.323 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0067 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` < `0.0778` → IC=+0.280 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0778 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` < `2.1712` → IC=+0.279 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1712 (IC base=+0.022)

- **PATRÓN** `ibs_20min` < `0.1923` → IC=+0.159 (n=2752)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1923 (IC base=-0.030)

- **PATRÓN** `dist_vwap_pct` > `0.841` → IC=+0.296 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.841 (IC base=-0.030)

- **PATRÓN** `dist_vwap_pct` < `0.2407` → IC=+0.292 (n=1304)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2407 (IC base=-0.030)

- **PATRÓN** `volumen_regimen` < `0.6948` → IC=+0.309 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6948 (IC base=-0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.0783` → IC=+0.319 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0783 (IC base=-0.030)

- **PATRÓN** `volumen_spike_ratio` < `2.4493` → IC=+0.305 (n=1193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4493 (IC base=-0.030)

- **PATRÓN** `volumen_spike_ratio` > `1.525` → IC=+0.299 (n=1066)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.525 (IC base=-0.030)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7949` → IC=-0.161 (n=4275)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7949
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=2204)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.175 (n=1363)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=5116)

- **FILTRO** `ibs_20min` > `0.72` → IC=-0.191 (n=2237)

  - _Acción_: SKIP cuando `ibs_20min` > 0.72
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=6728)

- **PATRÓN** `ibs_20min` > `0.7949` → IC=+0.146 (n=2204)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.7949 (IC base=-0.056)

- **PATRÓN** `dist_vwap_pct` > `0.4523` → IC=+0.341 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4523 (IC base=-0.056)

- **PATRÓN** `volumen_regimen` > `0.7043` → IC=+0.317 (n=1181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7043 (IC base=-0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.3085` → IC=+0.320 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3085 (IC base=-0.056)

- **PATRÓN** `volumen_spike_ratio` > `2.5366` → IC=+0.316 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5366 (IC base=-0.056)

- **PATRÓN** `dist_vwap_pct` > `1.1135` → IC=+0.292 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1135 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` < `0.6362` → IC=+0.274 (n=896)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6362 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` > `1.2109` → IC=+0.276 (n=895)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2109 (IC base=+0.008)

- **PATRÓN** `volumen_pendiente_norm` > `0.2924` → IC=+0.277 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2924 (IC base=+0.008)

- **PATRÓN** `volumen_spike_ratio` > `1.4453` → IC=+0.267 (n=2553)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4453 (IC base=+0.008)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.185 (n=9147)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0113 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.8662` → IC=+0.283 (n=12417)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8662 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `1.0129` → IC=+0.304 (n=1895)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0129 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.455` → IC=+0.168 (n=12348)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.455 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `0.6925` → IC=+0.279 (n=9142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6925 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2925` → IC=+0.294 (n=2266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2925 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.6455` → IC=+0.289 (n=5307)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6455 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.308 (n=15577)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 88.0 (IC base=+0.087)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.152 (n=12102)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0094 (IC base=+0.089)

- **PATRÓN** `ibs_20min` < `0.5156` → IC=+0.174 (n=23452)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.5156 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` < `0.2076` → IC=+0.282 (n=9131)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2076 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` < `0.6921` → IC=+0.279 (n=4023)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6921 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` > `1.1872` → IC=+0.285 (n=3046)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1872 (IC base=+0.089)

- **PATRÓN** `volumen_pendiente_norm` > `0.2951` → IC=+0.322 (n=2009)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2951 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` < `1.4543` → IC=+0.302 (n=4536)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4543 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` > `2.2751` → IC=+0.304 (n=6169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2751 (IC base=+0.089)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.311 (n=13592)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 70.0 (IC base=+0.089)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8182` → IC=-0.148 (n=4843)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8182
  - _Potencial_: sin este filtro IC_bueno=+0.314 (n=2495)

- **FILTRO** `ibs_20min` > `0.6977` → IC=-0.241 (n=1664)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6977
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=4993)

- **FILTRO** `sigma_ewma_delta_pct` > `4.053` → IC=-0.239 (n=1393)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.053
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=5264)

- **PATRÓN** `ibs_20min` > `0.8182` → IC=+0.314 (n=2495)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8182 (IC base=+0.009)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.159` → IC=+0.176 (n=2732)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 2.159 (IC base=+0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.2295` → IC=+0.331 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2295 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` < `1.4461` → IC=+0.296 (n=767)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4461 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` > `2.227` → IC=+0.317 (n=1043)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.227 (IC base=+0.009)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.324 (n=1529)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.009)

- **PATRÓN** `ibs_20min` < `0.1699` → IC=+0.172 (n=1665)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.1699 (IC base=-0.013)

- **PATRÓN** `volumen_pendiente_norm` < `0.1559` → IC=+0.383 (n=1515)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1559 (IC base=-0.013)

- **PATRÓN** `volumen_spike_ratio` < `2.6481` → IC=+0.388 (n=1453)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6481 (IC base=-0.013)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1841` → IC=+0.228 (n=1113)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1841 (IC base=+0.010)

- **PATRÓN** `dist_vwap_pct` < `0.5284` → IC=+0.213 (n=2967)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5284 (IC base=+0.010)

- **PATRÓN** `volumen_regimen` > `0.694` → IC=+0.222 (n=2390)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.694 (IC base=+0.010)

- **PATRÓN** `volumen_pendiente_norm` > `0.2725` → IC=+0.242 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2725 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` < `1.4146` → IC=+0.230 (n=882)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4146 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` > `2.4477` → IC=+0.223 (n=882)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4477 (IC base=+0.010)

- **PATRÓN** `ballena_activa_n` < `367.0` → IC=+0.232 (n=2650)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 367.0 (IC base=+0.010)

- **PATRÓN** `dist_vwap_pct` < `0.5804` → IC=+0.257 (n=2388)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5804 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` > `1.0152` → IC=+0.267 (n=904)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0152 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2707` → IC=+0.280 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2707 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.5311` → IC=+0.258 (n=853)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5311 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` > `2.1516` → IC=+0.259 (n=879)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1516 (IC base=+0.005)

- **PATRÓN** `ballena_activa_n` < `175.0` → IC=+0.276 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 175.0 (IC base=+0.005)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.317 (n=1694)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.294 (n=3752)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.285)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.323 (n=2026)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.564` → IC=+0.306 (n=2545)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.564 (IC base=+0.285)

- **PATRÓN** `volumen_pendiente_norm` < `0.1304` → IC=+0.294 (n=3472)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1304 (IC base=+0.285)

- **PATRÓN** `volumen_spike_ratio` > `2.1652` → IC=+0.296 (n=2425)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1652 (IC base=+0.285)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.293 (n=4389)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `2014.8641` → IC=+0.299 (n=1245)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2014.8641 (IC base=+0.285)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.301 (n=2371)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.285)

- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.341 (n=1162)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.307)

- **PATRÓN** `drift_60min` |x|≤ `0.1888` → IC=+0.328 (n=1535)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1888 (IC base=+0.307)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.322 (n=1335)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.307)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.311 (n=1579)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.307)

- **PATRÓN** `ibs_20min` < `0.0315` → IC=+0.309 (n=1534)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0315 (IC base=+0.307)

- **PATRÓN** `ibs_20min` > `0.1573` → IC=+0.321 (n=2324)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1573 (IC base=+0.307)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.955` → IC=+0.321 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.955 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` < `0.1986` → IC=+0.308 (n=3467)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1986 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` > `0.3448` → IC=+0.314 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3448 (IC base=+0.307)

- **PATRÓN** `volumen_spike_ratio` > `2.7493` → IC=+0.325 (n=1534)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7493 (IC base=+0.307)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.308 (n=1625)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.307)

- **PATRÓN** `libro_liquidez` > `1994.9752` → IC=+0.320 (n=1162)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1994.9752 (IC base=+0.307)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.309 (n=2996)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.307)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **PATRÓN** `dist_vwap_pct` > `0.1612` → IC=+0.237 (n=1236)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1612 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` < `0.6451` → IC=+0.232 (n=2774)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6451 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` < `1.1739` → IC=+0.235 (n=2522)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1739 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` > `0.5972` → IC=+0.232 (n=2522)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5972 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` < `0.1621` → IC=+0.235 (n=2648)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1621 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.0763` → IC=+0.235 (n=938)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0763 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `2.4059` → IC=+0.239 (n=2451)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4059 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `114.0` → IC=+0.250 (n=2502)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 114.0 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` < `0.3919` → IC=+0.261 (n=2052)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3919 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` < `1.176` → IC=+0.262 (n=1851)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.176 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` > `0.6129` → IC=+0.258 (n=1851)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6129 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` < `0.1001` → IC=+0.264 (n=1742)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1001 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.285 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` < `1.776` → IC=+0.282 (n=1191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.776 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` > `2.4197` → IC=+0.268 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4197 (IC base=+0.014)

- **PATRÓN** `ballena_activa_n` < `97.0` → IC=+0.285 (n=1595)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 97.0 (IC base=+0.014)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.75` → IC=-0.248 (n=2797)

  - _Acción_: SKIP cuando `ibs_20min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.316 (n=2831)

- **FILTRO** `ibs_20min` > `0.6` → IC=-0.234 (n=1330)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.168 (n=3995)

- **FILTRO** `sigma_ewma_delta_pct` > `8.256` → IC=-0.260 (n=610)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.256
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=4715)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.316 (n=2831)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.75 (IC base=+0.036)

- **PATRÓN** `dist_vwap_pct` > `1.1251` → IC=+0.354 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1251 (IC base=+0.036)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.449` → IC=+0.160 (n=2307)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 2.449 (IC base=+0.036)

- **PATRÓN** `volumen_regimen` < `0.8439` → IC=+0.351 (n=1383)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8439 (IC base=+0.036)

- **PATRÓN** `volumen_pendiente_norm` < `0.1003` → IC=+0.338 (n=1954)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1003 (IC base=+0.036)

- **PATRÓN** `volumen_pendiente_norm` > `0.2752` → IC=+0.369 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2752 (IC base=+0.036)

- **PATRÓN** `volumen_spike_ratio` < `1.7921` → IC=+0.356 (n=1345)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7921 (IC base=+0.036)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.356 (n=1795)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.036)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.168 (n=3995)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.6 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` < `0.2467` → IC=+0.274 (n=2088)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2467 (IC base=+0.068)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.725` → IC=+0.135 (n=4176)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 4.725 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` < `0.6872` → IC=+0.284 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6872 (IC base=+0.068)

- **PATRÓN** `volumen_pendiente_norm` > `0.0724` → IC=+0.298 (n=844)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0724 (IC base=+0.068)

- **PATRÓN** `volumen_spike_ratio` < `1.8091` → IC=+0.282 (n=1366)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8091 (IC base=+0.068)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.289 (n=2087)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.068)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.349 (n=2649)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.312)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.315 (n=2992)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.312)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.314 (n=3115)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.312)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.336 (n=2968)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.312)

- **PATRÓN** `dist_vwap_pct` > `0.2216` → IC=+0.336 (n=1577)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2216 (IC base=+0.312)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.735` → IC=+0.342 (n=1175)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.735 (IC base=+0.312)

- **PATRÓN** `volumen_regimen` > `0.6286` → IC=+0.323 (n=2965)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6286 (IC base=+0.312)

- **PATRÓN** `volumen_pendiente_norm` > `0.2876` → IC=+0.341 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2876 (IC base=+0.312)

- **PATRÓN** `volumen_spike_ratio` > `1.5386` → IC=+0.325 (n=2562)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5386 (IC base=+0.312)

- **PATRÓN** `libro_liquidez` > `2998.2516` → IC=+0.320 (n=989)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2998.2516 (IC base=+0.312)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.330 (n=3191)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.313)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.316 (n=3197)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.313)

- **PATRÓN** `ibs_20min` < `0.39` → IC=+0.327 (n=3190)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.39 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` > `1.313` → IC=+0.321 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.313 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` < `0.2609` → IC=+0.316 (n=3150)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2609 (IC base=+0.313)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.035` → IC=+0.328 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.035 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` < `0.6351` → IC=+0.317 (n=1063)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6351 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` > `1.2103` → IC=+0.340 (n=1063)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2103 (IC base=+0.313)

- **PATRÓN** `volumen_pendiente_norm` > `0.2891` → IC=+0.358 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2891 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` < `1.4162` → IC=+0.323 (n=1000)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4162 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` > `2.1624` → IC=+0.318 (n=1360)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1624 (IC base=+0.313)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.218 (n=6671)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0129 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.1284` → IC=+0.193 (n=8806)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1284 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=20823)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.534` → IC=+0.228 (n=20015)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.534 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.1719` → IC=+0.205 (n=7497)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1719 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.686` → IC=+0.260 (n=3923)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.686 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `1.1734` → IC=+0.152 (n=13355)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1734 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `0.6201` → IC=+0.151 (n=13355)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6201 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.2935` → IC=+0.206 (n=2884)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2935 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.6037` → IC=+0.185 (n=6503)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.6037 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.191 (n=18980)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 85.0 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.193 (n=8809)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0062 (IC base=+0.185)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.185 (n=13366)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0083 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.0863` → IC=+0.222 (n=6678)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0863 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.206 (n=9571)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` < `0.5283` → IC=+0.236 (n=20022)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5283 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` < `0.2001` → IC=+0.179 (n=14653)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.2001 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.38` → IC=+0.190 (n=3141)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 9.38 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.484` → IC=+0.191 (n=17919)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 2.484 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` < `1.1894` → IC=+0.166 (n=14166)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1894 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.296` → IC=+0.217 (n=3003)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.296 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` < `1.5641` → IC=+0.185 (n=8432)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.5641 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `2.6394` → IC=+0.196 (n=6388)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6394 (IC base=+0.185)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.198 (n=18988)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 89.0 (IC base=+0.185)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.076` → IC=+0.266 (n=1096)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.076 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=3433)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.228)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.229 (n=2226)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` > `0.9412` → IC=+0.291 (n=2189)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9412 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.473` → IC=+0.325 (n=1077)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.473 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` > `0.2818` → IC=+0.284 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2818 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` < `1.8284` → IC=+0.225 (n=2097)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8284 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `1.4336` → IC=+0.227 (n=3146)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4336 (IC base=+0.228)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=3438)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.228)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.252 (n=2791)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.250)

- **PATRÓN** `drift_60min` |x|≤ `0.1024` → IC=+0.307 (n=1229)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1024 (IC base=+0.250)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.254 (n=2876)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.250)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.254 (n=2549)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.250)

- **PATRÓN** `ibs_20min` < `0.0072` → IC=+0.307 (n=931)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0072 (IC base=+0.250)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.95` → IC=+0.254 (n=2767)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.95 (IC base=+0.250)

- **PATRÓN** `volumen_pendiente_norm` < `0.1008` → IC=+0.253 (n=2472)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1008 (IC base=+0.250)

- **PATRÓN** `volumen_pendiente_norm` > `0.3015` → IC=+0.263 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3015 (IC base=+0.250)

- **PATRÓN** `volumen_spike_ratio` < `1.5533` → IC=+0.263 (n=1181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5533 (IC base=+0.250)

- **PATRÓN** `volumen_spike_ratio` > `2.6782` → IC=+0.255 (n=895)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6782 (IC base=+0.250)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.254 (n=3026)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.250)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.191 (n=1029)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0034 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.0954` → IC=+0.167 (n=1353)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.0954 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=3207)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.2428` → IC=+0.200 (n=3072)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2428 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.1987` → IC=+0.210 (n=1474)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1987 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.516` → IC=+0.203 (n=551)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.516 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8512` → IC=+0.135 (n=2049)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.8512 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` > `1.1915` → IC=+0.128 (n=1024)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 1.1915 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2749` → IC=+0.167 (n=469)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2749 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.5077` → IC=+0.130 (n=1332)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.5077 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.4536` → IC=+0.138 (n=1009)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.4536 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `383.0` → IC=+0.130 (n=2998)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 383.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.181 (n=2930)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0061 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.2622` → IC=+0.176 (n=2930)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2622 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.176 (n=1587)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 15.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` < `0.6183` → IC=+0.210 (n=3330)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6183 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` < `0.2269` → IC=+0.176 (n=3621)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.2269 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.86` → IC=+0.179 (n=614)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 10.86 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.021` → IC=+0.156 (n=2931)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 4.021 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `1.2049` → IC=+0.163 (n=3330)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2049 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` < `0.0974` → IC=+0.155 (n=2930)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.0974 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `2.1459` → IC=+0.160 (n=2817)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1459 (IC base=+0.154)

- **PATRÓN** `ballena_activa_n` < `202.0` → IC=+0.196 (n=1382)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 202.0 (IC base=+0.154)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.012` → IC=+0.231 (n=1534)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.012 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.2597` → IC=+0.235 (n=2252)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2597 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.219 (n=3538)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.286 (n=1795)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.987` → IC=+0.304 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.987 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.3496` → IC=+0.235 (n=477)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3496 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.1684` → IC=+0.219 (n=2204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1684 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.213 (n=3994)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2012.7984` → IC=+0.224 (n=1126)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2012.7984 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0124` → IC=+0.242 (n=3066)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0124 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.1413` → IC=+0.275 (n=1347)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1413 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.273 (n=1150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.0455` → IC=+0.289 (n=1347)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0455 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.689` → IC=+0.280 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.689 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.3531` → IC=+0.281 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3531 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.7638` → IC=+0.242 (n=1307)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7638 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.1795` → IC=+0.249 (n=1980)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1795 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1878.8048` → IC=+0.247 (n=1388)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1878.8048 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.236 (n=2958)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.237)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.190 (n=1107)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.004 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.0834` → IC=+0.170 (n=1102)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.0834 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=3425)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.2427` → IC=+0.187 (n=3302)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.2427 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.1502` → IC=+0.188 (n=1850)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1502 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.172` → IC=+0.198 (n=560)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 11.172 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8361` → IC=+0.138 (n=2202)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.8361 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2869` → IC=+0.179 (n=496)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2869 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.5148` → IC=+0.125 (n=1423)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.5148 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.4975` → IC=+0.137 (n=1078)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.4975 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `6912.002` → IC=+0.195 (n=1497)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 6912.002 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `123.0` → IC=+0.127 (n=3246)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 123.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.173 (n=2361)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0058 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.4379` → IC=+0.151 (n=3535)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4379 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.164 (n=1692)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.6686` → IC=+0.188 (n=3535)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.6686 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` < `0.1748` → IC=+0.157 (n=3632)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1748 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.497` → IC=+0.141 (n=1203)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 6.497 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.851` → IC=+0.151 (n=2357)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.851 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.2925` → IC=+0.168 (n=534)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.2925 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `1.7897` → IC=+0.136 (n=2248)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.7897 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.4078` → IC=+0.135 (n=3371)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4078 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `6675.8703` → IC=+0.190 (n=1603)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 6675.8703 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.155 (n=1134)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 48.0 (IC base=+0.134)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.176 (n=1228)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0132 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=3786)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.4719` → IC=+0.205 (n=3679)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4719 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.8043` → IC=+0.213 (n=935)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8043 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.884` → IC=+0.282 (n=772)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.884 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `1.1669` → IC=+0.132 (n=3679)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.1669 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.6242` → IC=+0.125 (n=3679)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.6242 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1634` → IC=+0.125 (n=3757)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1634 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.282` → IC=+0.130 (n=512)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` > 0.282 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.7966` → IC=+0.126 (n=2384)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.7966 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2711.1262` → IC=+0.197 (n=1668)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2711.1262 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.128 (n=2324)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 26.0 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0113` → IC=+0.153 (n=3403)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0113 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.1194` → IC=+0.170 (n=1290)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1194 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=3944)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.6442` → IC=+0.221 (n=3865)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6442 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` < `0.2307` → IC=+0.147 (n=3846)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.2307 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.229` → IC=+0.147 (n=3425)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 2.229 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.1824` → IC=+0.130 (n=3865)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1824 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` > `0.704` → IC=+0.125 (n=3452)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.704 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2783` → IC=+0.151 (n=543)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.2783 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.4415` → IC=+0.142 (n=1226)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4415 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `2.4676` → IC=+0.138 (n=1226)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.4676 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2611.9184` → IC=+0.193 (n=1752)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2611.9184 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.133 (n=3668)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 42.0 (IC base=+0.125)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.248 (n=2952)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0124 (IC base=+0.225)

- **PATRÓN** `drift_60min` |x|≤ `0.4644` → IC=+0.232 (n=2906)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4644 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.230 (n=3434)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=2983)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `0.6656` → IC=+0.254 (n=3302)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6656 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` > `0.1879` → IC=+0.232 (n=2030)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1879 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` < `0.846` → IC=+0.227 (n=3415)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.846 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.498` → IC=+0.264 (n=1557)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.498 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` > `0.6172` → IC=+0.233 (n=3303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6172 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.2897` → IC=+0.265 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2897 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` < `1.833` → IC=+0.227 (n=2151)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.833 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `1.5378` → IC=+0.227 (n=2881)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5378 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.226 (n=4228)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `2627.0905` → IC=+0.228 (n=2201)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2627.0905 (IC base=+0.225)

- **PATRÓN** `sigma_h` > `0.0159` → IC=+0.247 (n=2293)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0159 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.6225` → IC=+0.247 (n=3438)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6225 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.250 (n=1681)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.242 (n=1546)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.0385` → IC=+0.297 (n=1513)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0385 (IC base=+0.237)

- **PATRÓN** `dist_vwap_pct` > `1.2002` → IC=+0.253 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2002 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.989` → IC=+0.272 (n=651)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.989 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` < `0.8653` → IC=+0.243 (n=2293)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8653 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` > `1.0491` → IC=+0.238 (n=1559)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0491 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2884` → IC=+0.300 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2884 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.8573` → IC=+0.236 (n=2176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8573 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `1.5598` → IC=+0.237 (n=2915)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5598 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=4374)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.237)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.202 (n=1755)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.1457` → IC=+0.168 (n=2310)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.1457 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.165 (n=5488)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.2963` → IC=+0.189 (n=5246)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.2963 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.9231` → IC=+0.180 (n=794)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.9231 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.514` → IC=+0.209 (n=844)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.514 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `0.8537` → IC=+0.163 (n=3194)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8537 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` > `1.1856` → IC=+0.158 (n=1597)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 1.1856 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.1551` → IC=+0.172 (n=1348)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1551 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `1.5253` → IC=+0.157 (n=2254)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.5253 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.8058` → IC=+0.155 (n=3415)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.8058 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.156 (n=5773)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.02 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `7288.7345` → IC=+0.191 (n=2378)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 7288.7345 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.7092` → IC=+0.141 (n=5771)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.7092 (IC base=+0.099)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.140 (n=2544)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 22.0 (IC base=+0.099)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.210 (n=859)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.0817` → IC=+0.234 (n=430)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0817 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.225 (n=1165)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `0.6075` → IC=+0.251 (n=858)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6075 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` > `0.6976` → IC=+0.237 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6976 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.833` → IC=+0.227 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.833 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` < `0.623` → IC=+0.220 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.623 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.0877` → IC=+0.215 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0877 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` < `2.1509` → IC=+0.204 (n=1113)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1509 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `1.3995` → IC=+0.196 (n=1264)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.3995 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `11293.6414` → IC=+0.199 (n=1150)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 11293.6414 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.154 (n=542)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0033 (IC base=+0.072)

- **PATRÓN** `ibs_20min` < `0.218` → IC=+0.187 (n=713)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.218 (IC base=+0.072)

- **PATRÓN** `ballena_activa_n` < `165.0` → IC=+0.167 (n=700)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 165.0 (IC base=+0.072)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.241 (n=538)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.1349` → IC=+0.155 (n=712)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1349 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=1678)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` > `0.7614` → IC=+0.258 (n=732)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7614 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.1582` → IC=+0.166 (n=764)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1582 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.035` → IC=+0.184 (n=229)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 10.035 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `0.8289` → IC=+0.153 (n=1076)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8289 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.1553` → IC=+0.181 (n=412)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.1553 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `1.7716` → IC=+0.156 (n=1061)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.7716 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `7804.5378` → IC=+0.174 (n=732)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 7804.5378 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.143 (n=530)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 30.0 (IC base=+0.143)

- **PATRÓN** `sigma_h` < `0.0082` → IC=+0.123 (n=1611)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0082 (IC base=+0.107)

- **PATRÓN** `ibs_20min` < `0.1814` → IC=+0.207 (n=709)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1814 (IC base=+0.107)

- **PATRÓN** `volumen_regimen` < `0.6746` → IC=+0.136 (n=709)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.6746 (IC base=+0.107)

- **PATRÓN** `volumen_pendiente_norm` > `0.2228` → IC=+0.130 (n=274)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` > 0.2228 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `7738.3514` → IC=+0.161 (n=730)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 7738.3514 (IC base=+0.107)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.145 (n=689)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 40.0 (IC base=+0.107)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.150 (n=470)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0073 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.140 (n=1413)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 6.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.7273` → IC=+0.222 (n=940)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7273 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `1.0624` → IC=+0.149 (n=249)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 1.0624 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.856` → IC=+0.226 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.856 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `1.0426` → IC=+0.131 (n=1241)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.0426 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` > `0.7012` → IC=+0.126 (n=1259)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.7012 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.2221` → IC=+0.146 (n=241)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.2221 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `1.4192` → IC=+0.149 (n=457)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4192 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.122 (n=1426)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `3048.7157` → IC=+0.148 (n=470)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 3048.7157 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.131 (n=470)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 10.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` < `0.6875` → IC=+0.144 (n=1576)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.6875 (IC base=+0.081)

- **PATRÓN** `libro_liquidez` > `2750.9096` → IC=+0.164 (n=713)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2750.9096 (IC base=+0.081)

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

- **PATRÓN** `volumen_regimen` < `0.8755` → IC=+0.200 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8755 (IC base=+0.163)

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

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.177 (n=460)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 15.0 (IC base=+0.163)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.225 (n=8831)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0129 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=27674)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.9655` → IC=+0.298 (n=8834)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9655 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.9624` → IC=+0.216 (n=3059)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9624 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.866` → IC=+0.259 (n=6477)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.866 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.8659` → IC=+0.163 (n=11904)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8659 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2922` → IC=+0.216 (n=3472)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2922 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6284` → IC=+0.193 (n=8633)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6284 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `1765.74` → IC=+0.180 (n=26474)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 1765.74 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `99.0` → IC=+0.199 (n=25099)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 99.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.199 (n=8241)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0056 (IC base=+0.199)

- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.208 (n=8218)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.1142` → IC=+0.203 (n=8221)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1142 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=9185)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.4897` → IC=+0.251 (n=21692)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4897 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` < `0.1948` → IC=+0.182 (n=15780)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.1948 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.327` → IC=+0.204 (n=24153)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.327 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `0.6263` → IC=+0.181 (n=5507)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.6263 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.294` → IC=+0.255 (n=3387)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.294 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `2.6273` → IC=+0.211 (n=7913)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6273 (IC base=+0.199)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.220 (n=20799)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 58.0 (IC base=+0.199)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3096` → IC=+0.235 (n=3711)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3096 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.239 (n=4435)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.233)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.235 (n=2835)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.315 (n=1668)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.038` → IC=+0.298 (n=2776)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.038 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.232` → IC=+0.288 (n=747)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.232 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.2767` → IC=+0.241 (n=1855)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2767 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.246 (n=4380)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `2059.05` → IC=+0.236 (n=1406)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2059.05 (IC base=+0.233)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.267 (n=1293)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.263)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.264 (n=1759)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.263)

- **PATRÓN** `drift_60min` |x|≤ `0.1298` → IC=+0.289 (n=1706)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1298 (IC base=+0.263)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.265 (n=4026)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.263)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.265 (n=3503)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.263)

- **PATRÓN** `ibs_20min` < `0.4704` → IC=+0.283 (n=3411)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4704 (IC base=+0.263)

- **PATRÓN** `volumen_pendiente_norm` < `0.099` → IC=+0.265 (n=3545)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.099 (IC base=+0.263)

- **PATRÓN** `volumen_pendiente_norm` > `0.2909` → IC=+0.286 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2909 (IC base=+0.263)

- **PATRÓN** `volumen_spike_ratio` < `1.5656` → IC=+0.263 (n=1645)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5656 (IC base=+0.263)

- **PATRÓN** `volumen_spike_ratio` > `2.6411` → IC=+0.271 (n=1246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6411 (IC base=+0.263)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.266 (n=4179)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.263)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.265 (n=1307)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 6.0 (IC base=+0.263)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.174 (n=1456)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0034 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.0845` → IC=+0.147 (n=1454)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.0845 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.152 (n=4547)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.1867` → IC=+0.186 (n=4359)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.1867 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.7449` → IC=+0.210 (n=744)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7449 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.003` → IC=+0.174 (n=682)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 11.003 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.6328` → IC=+0.156 (n=1454)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6328 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `1.0636` → IC=+0.141 (n=1977)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 1.0636 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2716` → IC=+0.189 (n=609)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2716 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.1654` → IC=+0.142 (n=3776)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.1654 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.5184` → IC=+0.144 (n=3833)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.5184 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `288.0` → IC=+0.150 (n=2831)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 288.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.169 (n=3390)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0062 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.0846` → IC=+0.175 (n=1284)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0846 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=1420)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.3243` → IC=+0.234 (n=2568)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3243 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.1573` → IC=+0.163 (n=3792)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1573 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.0` → IC=+0.148 (n=1815)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 3.0 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.19` → IC=+0.151 (n=3934)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 6.19 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.0397` → IC=+0.157 (n=3390)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.0397 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.2216` → IC=+0.198 (n=704)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2216 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.4305` → IC=+0.152 (n=3739)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4305 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.7717` → IC=+0.152 (n=2493)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.7717 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=5002)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `211.0` → IC=+0.185 (n=1219)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 211.0 (IC base=+0.147)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.242 (n=1996)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=4627)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.224 (n=3935)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.297 (n=1631)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.897` → IC=+0.314 (n=979)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.897 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2044` → IC=+0.233 (n=1166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2044 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.7573` → IC=+0.240 (n=1957)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7573 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.229 (n=5186)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `1899.7798` → IC=+0.238 (n=1996)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1899.7798 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.249 (n=1877)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.244)

- **PATRÓN** `drift_60min` |x|≤ `0.1863` → IC=+0.259 (n=1874)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1863 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.262 (n=1608)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.247 (n=1949)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` < `0.0698` → IC=+0.295 (n=1420)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0698 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.862` → IC=+0.302 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.862 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` > `0.3463` → IC=+0.298 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3463 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `2.1705` → IC=+0.256 (n=2750)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1705 (IC base=+0.244)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.249 (n=1985)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.244)

- **PATRÓN** `libro_liquidez` > `1994.6284` → IC=+0.252 (n=1419)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1994.6284 (IC base=+0.244)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.247 (n=3609)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.244)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.188 (n=1535)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.004 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.3603` → IC=+0.147 (n=4028)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3603 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=4760)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.8747` → IC=+0.261 (n=1528)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8747 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.1525` → IC=+0.169 (n=2241)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1525 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.963` → IC=+0.162 (n=1993)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 2.963 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.8566` → IC=+0.154 (n=3052)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8566 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2778` → IC=+0.199 (n=609)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2778 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.5167` → IC=+0.154 (n=1970)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.5167 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `2.1501` → IC=+0.144 (n=2030)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.1501 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `5904.382` → IC=+0.229 (n=2075)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5904.382 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.142 (n=2987)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 85.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.170 (n=3886)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0083 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.4665` → IC=+0.162 (n=3881)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.4665 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=1424)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` < `0.5726` → IC=+0.212 (n=3416)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5726 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` < `0.6462` → IC=+0.158 (n=4496)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.6462 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.038` → IC=+0.156 (n=774)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 9.038 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.028` → IC=+0.155 (n=3384)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 3.028 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `0.8502` → IC=+0.162 (n=2588)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8502 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.29` → IC=+0.209 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.29 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `2.4824` → IC=+0.156 (n=3764)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4824 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `1.5224` → IC=+0.158 (n=3363)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.5224 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `6737.5602` → IC=+0.216 (n=1294)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6737.5602 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.171 (n=1281)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 57.0 (IC base=+0.152)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0133` → IC=+0.156 (n=1556)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0133 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.150 (n=3295)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.6957` → IC=+0.255 (n=3111)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6957 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `0.8213` → IC=+0.196 (n=1029)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.8213 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.193` → IC=+0.269 (n=1189)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.193 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `0.8707` → IC=+0.133 (n=3109)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.8707 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` < `0.1017` → IC=+0.124 (n=4443)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1017 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.2791` → IC=+0.142 (n=587)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.2791 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `2.5079` → IC=+0.125 (n=4556)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 2.5079 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2776.8203` → IC=+0.238 (n=1554)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2776.8203 (IC base=+0.121)

- **PATRÓN** `sigma_h` < `0.0114` → IC=+0.159 (n=3836)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0114 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.1438` → IC=+0.151 (n=1453)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.1438 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.149 (n=4487)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.5417` → IC=+0.246 (n=3834)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5417 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.2293` → IC=+0.152 (n=4030)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.2293 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.022` → IC=+0.161 (n=4235)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 3.022 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.1935` → IC=+0.142 (n=4358)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.1935 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2805` → IC=+0.203 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2805 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.4386` → IC=+0.162 (n=1389)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.4386 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `2.4941` → IC=+0.143 (n=1388)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.4941 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `2648.8968` → IC=+0.225 (n=1453)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2648.8968 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.150 (n=4181)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 47.0 (IC base=+0.137)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.255 (n=4258)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.241 (n=4458)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.239 (n=2855)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` > `0.9873` → IC=+0.301 (n=1423)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9873 (IC base=+0.235)

- **PATRÓN** `dist_vwap_pct` > `0.2049` → IC=+0.251 (n=2158)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2049 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.925` → IC=+0.298 (n=767)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.925 (IC base=+0.235)

- **PATRÓN** `volumen_regimen` < `1.2159` → IC=+0.235 (n=4258)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2159 (IC base=+0.235)

- **PATRÓN** `volumen_regimen` > `0.6404` → IC=+0.241 (n=4259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6404 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.0802` → IC=+0.253 (n=1692)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0802 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.5246` → IC=+0.255 (n=1391)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5246 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=5435)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `2645.2402` → IC=+0.238 (n=2839)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2645.2402 (IC base=+0.235)

- **PATRÓN** `sigma_h` > `0.0246` → IC=+0.270 (n=1477)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0246 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.251 (n=4165)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.14` → IC=+0.305 (n=1953)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.14 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` > `1.2042` → IC=+0.250 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2042 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` < `0.2334` → IC=+0.249 (n=4266)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2334 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.914` → IC=+0.281 (n=821)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.914 (IC base=+0.245)

- **PATRÓN** `volumen_regimen` < `0.6362` → IC=+0.248 (n=1476)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6362 (IC base=+0.245)

- **PATRÓN** `volumen_regimen` > `1.2193` → IC=+0.265 (n=1476)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2193 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.2886` → IC=+0.311 (n=607)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2886 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `1.4357` → IC=+0.249 (n=4210)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4357 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.245 (n=3672)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.245)

### GBM_LATE_5M
- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.233 (n=6611)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0109 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.5399` → IC=+0.234 (n=7509)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5399 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=7528)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.9282` → IC=+0.259 (n=2503)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9282 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` < `0.9695` → IC=+0.229 (n=6172)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9695 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.437` → IC=+0.236 (n=2505)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.437 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` < `0.7051` → IC=+0.231 (n=2355)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7051 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` > `0.8776` → IC=+0.229 (n=3565)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8776 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.1639` → IC=+0.236 (n=2103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1639 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `1.4491` → IC=+0.237 (n=2464)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4491 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.230 (n=5365)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `3769.122` → IC=+0.234 (n=5006)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3769.122 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.229 (n=1798)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.212)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.212 (n=2442)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.4184` → IC=+0.222 (n=4736)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4184 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.226 (n=1802)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.223 (n=2440)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.6124` → IC=+0.215 (n=4736)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6124 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.7166` → IC=+0.218 (n=925)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7166 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` < `0.2585` → IC=+0.204 (n=4756)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2585 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.671` → IC=+0.225 (n=4893)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.671 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `1.2537` → IC=+0.211 (n=4886)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2537 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` > `0.7288` → IC=+0.204 (n=4365)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7288 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` < `0.0983` → IC=+0.214 (n=4978)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0983 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.5338` → IC=+0.217 (n=2332)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5338 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `1.8202` → IC=+0.220 (n=3534)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8202 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.236 (n=3541)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 49.0 (IC base=+0.212)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.279 (n=843)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.273)

- **PATRÓN** `drift_60min` |x|≤ `0.0863` → IC=+0.304 (n=320)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0863 (IC base=+0.273)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.282 (n=958)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.273)

- **PATRÓN** `ibs_20min` < `0.4706` → IC=+0.288 (n=639)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4706 (IC base=+0.273)

- **PATRÓN** `dist_vwap_pct` < `0.3336` → IC=+0.284 (n=977)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3336 (IC base=+0.273)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.118` → IC=+0.300 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.118 (IC base=+0.273)

- **PATRÓN** `volumen_regimen` < `1.2269` → IC=+0.278 (n=958)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2269 (IC base=+0.273)

- **PATRÓN** `volumen_regimen` > `0.8784` → IC=+0.292 (n=639)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8784 (IC base=+0.273)

- **PATRÓN** `volumen_pendiente_norm` > `0.2861` → IC=+0.342 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2861 (IC base=+0.273)

- **PATRÓN** `volumen_spike_ratio` < `2.4907` → IC=+0.281 (n=953)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4907 (IC base=+0.273)

- **PATRÓN** `libro_liquidez` > `12936.1422` → IC=+0.285 (n=639)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12936.1422 (IC base=+0.273)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.260 (n=519)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.3891` → IC=+0.187 (n=1549)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.3891 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=569)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.175 (n=582)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 5.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` < `0.1382` → IC=+0.192 (n=683)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.1382 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` > `0.3612` → IC=+0.175 (n=333)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.3612 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` < `0.5564` → IC=+0.172 (n=1858)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.5564 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.334` → IC=+0.192 (n=1522)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 6.334 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `1.091` → IC=+0.185 (n=1363)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 1.091 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.1521` → IC=+0.186 (n=473)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.1521 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `2.496` → IC=+0.177 (n=1541)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 2.496 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `2.1732` → IC=+0.175 (n=699)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.1732 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `14616.0048` → IC=+0.171 (n=703)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 14616.0048 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `701.0` → IC=+0.187 (n=1504)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 701.0 (IC base=+0.171)

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
- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.224 (n=1836)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0076 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.4741` → IC=+0.221 (n=2083)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4741 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.244 (n=725)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` < `0.4677` → IC=+0.231 (n=1389)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4677 (IC base=+0.215)

- **PATRÓN** `ibs_20min` > `0.8315` → IC=+0.215 (n=694)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8315 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` < `0.4283` → IC=+0.225 (n=2095)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4283 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.938` → IC=+0.222 (n=1891)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.938 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` < `0.8625` → IC=+0.217 (n=1389)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8625 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` > `1.2299` → IC=+0.221 (n=694)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2299 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` < `0.0981` → IC=+0.217 (n=1936)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0981 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.1592` → IC=+0.215 (n=588)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1592 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `1.4017` → IC=+0.233 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4017 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `1.4931` → IC=+0.216 (n=1817)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4931 (IC base=+0.215)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.247 (n=563)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.511` → IC=+0.220 (n=1685)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.511 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.216 (n=625)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.217 (n=1130)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` > `0.0847` → IC=+0.214 (n=1685)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0847 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `0.7294` → IC=+0.221 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7294 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.199` → IC=+0.211 (n=1539)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.199 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` < `1.1036` → IC=+0.213 (n=1483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1036 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` > `0.7178` → IC=+0.211 (n=1505)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7178 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.0726` → IC=+0.229 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0726 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` < `2.1617` → IC=+0.208 (n=1452)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1617 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `1.7691` → IC=+0.210 (n=1100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7691 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.209 (n=2182)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.210 (n=1681)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 96.0 (IC base=+0.206)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.232 (n=882)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.221)

- **PATRÓN** `sigma_h` > `0.0135` → IC=+0.231 (n=440)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0135 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.252 (n=1183)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.221 (n=1213)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` > `0.9919` → IC=+0.303 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9919 (IC base=+0.221)

- **PATRÓN** `dist_vwap_pct` > `1.102` → IC=+0.252 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.102 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.019` → IC=+0.275 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.019 (IC base=+0.221)

- **PATRÓN** `volumen_regimen` < `0.6421` → IC=+0.251 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6421 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` < `0.106` → IC=+0.224 (n=1208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.106 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.2742` → IC=+0.245 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2742 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` < `2.5073` → IC=+0.230 (n=1288)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5073 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.228 (n=1536)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `3372.8412` → IC=+0.246 (n=1179)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3372.8412 (IC base=+0.221)

- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.255 (n=667)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.247)

- **PATRÓN** `drift_60min` |x|≤ `0.6851` → IC=+0.259 (n=998)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6851 (IC base=+0.247)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.248 (n=922)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.247)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.267 (n=696)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.247)

- **PATRÓN** `ibs_20min` < `0.6429` → IC=+0.271 (n=878)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6429 (IC base=+0.247)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.991` → IC=+0.267 (n=945)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.991 (IC base=+0.247)

- **PATRÓN** `volumen_regimen` < `0.7555` → IC=+0.260 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7555 (IC base=+0.247)

- **PATRÓN** `volumen_pendiente_norm` < `0.1037` → IC=+0.258 (n=901)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1037 (IC base=+0.247)

- **PATRÓN** `volumen_spike_ratio` < `1.4771` → IC=+0.246 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4771 (IC base=+0.247)

- **PATRÓN** `volumen_spike_ratio` > `2.2116` → IC=+0.270 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2116 (IC base=+0.247)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.249 (n=1218)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.247)

- **PATRÓN** `libro_liquidez` > `4038.512` → IC=+0.269 (n=665)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4038.512 (IC base=+0.247)

- **PATRÓN** `ballena_activa_n` < `32.0` → IC=+0.276 (n=872)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 32.0 (IC base=+0.247)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.146 (n=966)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0043 (IC base=+0.076)

- **PATRÓN** `ibs_20min` > `0.4203` → IC=+0.140 (n=2805)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` > 0.4203 (IC base=+0.076)

- **PATRÓN** `dist_vwap_pct` > `0.1603` → IC=+0.160 (n=1298)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1603 (IC base=+0.076)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.361` → IC=+0.149 (n=611)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 10.361 (IC base=+0.076)

- **PATRÓN** `ibs_20min` < `0.5777` → IC=+0.180 (n=2229)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.5777 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.548` → IC=+0.133 (n=991)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 2.548 (IC base=+0.099)

- **PATRÓN** `volumen_pendiente_norm` > `0.1518` → IC=+0.183 (n=629)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1518 (IC base=+0.099)

- **PATRÓN** `volumen_spike_ratio` < `2.1572` → IC=+0.122 (n=1888)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.1572 (IC base=+0.099)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.5547` → IC=-0.122 (n=347)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5547
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=705)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.187 (n=276)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0029 (IC base=+0.067)

- **PATRÓN** `ibs_20min` > `0.5547` → IC=+0.161 (n=705)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.5547 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` > `0.1288` → IC=+0.166 (n=366)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1288 (IC base=+0.067)

- **PATRÓN** `ibs_20min` < `0.0621` → IC=+0.248 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0621 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.071` → IC=+0.142 (n=325)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.071 (IC base=+0.057)

### GBM_LATE_60M#ETH#60min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.161 (n=375)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0044 (IC base=+0.066)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.132 (n=327)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 17.0 (IC base=+0.066)

- **PATRÓN** `ibs_20min` > `0.5307` → IC=+0.161 (n=733)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.5307 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` > `0.1362` → IC=+0.157 (n=391)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1362 (IC base=+0.066)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.996` → IC=+0.172 (n=181)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 11.996 (IC base=+0.066)

- **PATRÓN** `ibs_20min` < `0.3123` → IC=+0.223 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3123 (IC base=+0.047)

- **PATRÓN** `volumen_pendiente_norm` > `0.2584` → IC=+0.140 (n=84)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.2584 (IC base=+0.047)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.7143` → IC=+0.143 (n=631)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.7143 (IC base=+0.041)

- **PATRÓN** `dist_vwap_pct` > `0.7736` → IC=+0.159 (n=227)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.7736 (IC base=+0.041)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.992` → IC=+0.126 (n=265)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` > 6.992 (IC base=+0.041)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.179 (n=428)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0103 (IC base=+0.100)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.198 (n=610)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.5 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` < `0.2242` → IC=+0.152 (n=608)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.2242 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.077` → IC=+0.247 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.077 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` > `1.1218` → IC=+0.188 (n=203)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` > 1.1218 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` > `0.1605` → IC=+0.181 (n=158)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.1605 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` > `1.8607` → IC=+0.142 (n=386)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.8607 (IC base=+0.100)

### GBM_LATE_60M#XRP#60min
- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.368 (n=74)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.304)

- **PATRÓN** `drift_60min` |x|≤ `0.1918` → IC=+0.300 (n=28)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1918 (IC base=+0.304)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.400 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.304)

- **PATRÓN** `ibs_20min` > `0.5721` → IC=+0.347 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5721 (IC base=+0.304)

- **PATRÓN** `dist_vwap_pct` > `0.4912` → IC=+0.400 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4912 (IC base=+0.304)

- **PATRÓN** `volumen_regimen` < `1.0085` → IC=+0.313 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0085 (IC base=+0.304)

- **PATRÓN** `volumen_regimen` > `0.6557` → IC=+0.316 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6557 (IC base=+0.304)

- **PATRÓN** `volumen_pendiente_norm` > `0.1805` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1805 (IC base=+0.304)

- **PATRÓN** `volumen_spike_ratio` < `2.8251` → IC=+0.345 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.8251 (IC base=+0.304)

- **PATRÓN** `libro_spread` < `0.07` → IC=+0.308 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.07 (IC base=+0.304)

- **PATRÓN** `libro_liquidez` > `559.0842` → IC=+0.300 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 559.0842 (IC base=+0.304)

- **PATRÓN** `sigma_h` < `0.0097` → IC=+0.409 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0097 (IC base=+0.340)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.374 (n=93)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.340)

- **PATRÓN** `ibs_20min` < `0.0274` → IC=+0.379 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0274 (IC base=+0.340)

- **PATRÓN** `ibs_20min` > `0.3512` → IC=+0.364 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3512 (IC base=+0.340)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.683` → IC=+0.463 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.683 (IC base=+0.340)

- **PATRÓN** `volumen_regimen` > `0.5619` → IC=+0.374 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5619 (IC base=+0.340)

- **PATRÓN** `volumen_pendiente_norm` > `0.098` → IC=+0.407 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.098 (IC base=+0.340)

- **PATRÓN** `volumen_spike_ratio` < `1.5307` → IC=+0.381 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5307 (IC base=+0.340)

- **PATRÓN** `volumen_spike_ratio` > `3.1184` → IC=+0.406 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.1184 (IC base=+0.340)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.368 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.340)

- **PATRÓN** `libro_liquidez` > `36.95` → IC=+0.359 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 36.95 (IC base=+0.340)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` < `0.0063` → IC=-0.248 (n=212)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.212 (n=213)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.310 (n=98)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=327)

- **FILTRO** `volumen_regimen` < `0.8808` → IC=-0.307 (n=138)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8808
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=283)

- **FILTRO** `sigma_h` < `0.0065` → IC=-0.295 (n=261)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0065
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=135)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.292 (n=118)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.246 (n=278)

- **FILTRO** `dist_vwap_pct` > `0.4704` → IC=-0.450 (n=18)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4704
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=361)

- **FILTRO** `sigma_ewma_delta_pct` > `9.318` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.318
  - _Potencial_: sin este filtro IC_bueno=-0.258 (n=366)

- **FILTRO** `volumen_pendiente_norm` > `0.0453` → IC=-0.375 (n=30)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0453
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=271)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.312 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.233 (n=103)

- **FILTRO** `ibs_20min` < `0.0328` → IC=-0.300 (n=33)

  - _Acción_: SKIP cuando `ibs_20min` < 0.0328
  - _Potencial_: sin este filtro IC_bueno=-0.235 (n=100)

- **FILTRO** `volumen_spike_ratio` > `1.8166` → IC=-0.260 (n=73)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.8166
  - _Potencial_: sin este filtro IC_bueno=-0.218 (n=37)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.260 (n=77)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=77)

- **FILTRO** `drift_60min` |x|> `0.132` → IC=-0.330 (n=51)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.132
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=101)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_h` < `0.003` → IC=-0.250 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.003
  - _Potencial_: sin este filtro IC_bueno=-0.151 (n=104)

- **FILTRO** `ibs_20min` < `0.6002` → IC=-0.472 (n=34)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6002
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=104)

- **FILTRO** `volumen_regimen` < `0.7594` → IC=-0.250 (n=34)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7594
  - _Potencial_: sin este filtro IC_bueno=-0.151 (n=104)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.372 (n=37)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=106)

- **FILTRO** `volumen_spike_ratio` > `2.2319` → IC=-0.342 (n=36)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.2319
  - _Potencial_: sin este filtro IC_bueno=-0.297 (n=72)

- **FILTRO** `volumen_spike_ratio` < `1.4507` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.4507
  - _Potencial_: sin este filtro IC_bueno=-0.295 (n=81)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.300 (n=128)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `drift_60min` |x|> `0.2366` → IC=-0.346 (n=37)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2366
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=112)

- **FILTRO** `volumen_spike_ratio` < `1.5734` → IC=-0.288 (n=31)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.5734
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=93)

- **FILTRO** `sigma_ewma_delta_pct` > `4.698` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.698
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=63)

- **FILTRO** `volumen_regimen` < `0.9705` → IC=-0.463 (n=25)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9705
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=53)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=63)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.242` → IC=-0.156 (n=353)

  - _Acción_: SKIP cuando `ibs_20min` > 0.242
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=1060)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.204 (n=363)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `0.6842` → IC=+0.200 (n=931)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6842 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` > `0.8971` → IC=+0.308 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8971 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.305` → IC=+0.183 (n=222)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 10.305 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` < `0.6242` → IC=+0.191 (n=302)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.6242 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` > `1.1943` → IC=+0.178 (n=302)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 1.1943 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` < `0.069` → IC=+0.189 (n=712)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.069 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` < `1.4185` → IC=+0.206 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4185 (IC base=+0.166)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.140 (n=84)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` > 0.0068 (IC base=+0.066)

- **PATRÓN** `ibs_20min` > `0.7306` → IC=+0.136 (n=251)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 0.7306 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` > `0.3329` → IC=+0.216 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3329 (IC base=+0.066)

- **PATRÓN** `ibs_20min` < `0.2563` → IC=+0.134 (n=463)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.2563 (IC base=+0.074)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
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
- **FILTRO** `ibs_20min` > `0.0556` → IC=-0.233 (n=118)

  - _Acción_: SKIP cuando `ibs_20min` > 0.0556
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=121)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.293 (n=346)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.274)

- **PATRÓN** `ibs_20min` > `0.6111` → IC=+0.296 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6111 (IC base=+0.274)

- **PATRÓN** `dist_vwap_pct` > `0.7834` → IC=+0.405 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7834 (IC base=+0.274)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.006` → IC=+0.357 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.006 (IC base=+0.274)

- **PATRÓN** `volumen_regimen` < `0.7978` → IC=+0.300 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7978 (IC base=+0.274)

- **PATRÓN** `volumen_pendiente_norm` < `0.2132` → IC=+0.301 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2132 (IC base=+0.274)

- **PATRÓN** `volumen_pendiente_norm` > `0.092` → IC=+0.308 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.092 (IC base=+0.274)

- **PATRÓN** `volumen_spike_ratio` < `1.4907` → IC=+0.327 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4907 (IC base=+0.274)

- **PATRÓN** `volumen_spike_ratio` > `2.0543` → IC=+0.309 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.0543 (IC base=+0.274)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.275 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.274)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.315 (n=209)

- **PATRÓN** `drift_ventana_pct` |x|> `0.5455` → IC=+0.357 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.5455 (IC base=+0.325)

- **PATRÓN** `elapsed_s` > `209.4` → IC=+0.373 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 209.4 (IC base=+0.325)

- **PATRÓN** `drift_15min` |x|≤ `1.0466` → IC=+0.375 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0466 (IC base=+0.325)

- **PATRÓN** `drift_60min` |x|≤ `0.6894` → IC=+0.391 (n=108)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6894 (IC base=+0.325)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.380 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.325)

- **PATRÓN** `ballena_activa_n` < `1039.0` → IC=+0.429 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1039.0 (IC base=+0.325)

- **PATRÓN** `drift_ventana_pct` |x|> `0.445` → IC=+0.314 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.445 (IC base=+0.281)

- **PATRÓN** `elapsed_s` > `232.0` → IC=+0.364 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 232.0 (IC base=+0.281)

- **PATRÓN** `drift_15min` |x|≤ `2.3607` → IC=+0.316 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3607 (IC base=+0.281)

- **PATRÓN** `drift_60min` |x|≤ `0.9999` → IC=+0.303 (n=150)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9999 (IC base=+0.281)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.315 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.281)

- **PATRÓN** `ballena_activa_n` < `1717.0` → IC=+0.326 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1717.0 (IC base=+0.281)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.315 (n=209)

- **PATRÓN** `drift_ventana_pct` |x|> `0.5455` → IC=+0.357 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.5455 (IC base=+0.325)

- **PATRÓN** `elapsed_s` > `209.4` → IC=+0.373 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 209.4 (IC base=+0.325)

- **PATRÓN** `drift_15min` |x|≤ `1.0466` → IC=+0.375 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0466 (IC base=+0.325)

- **PATRÓN** `drift_60min` |x|≤ `0.6894` → IC=+0.391 (n=108)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6894 (IC base=+0.325)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.380 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.325)

- **PATRÓN** `ballena_activa_n` < `1039.0` → IC=+0.429 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1039.0 (IC base=+0.325)

- **PATRÓN** `drift_ventana_pct` |x|> `0.445` → IC=+0.314 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.445 (IC base=+0.281)

- **PATRÓN** `elapsed_s` > `232.0` → IC=+0.364 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 232.0 (IC base=+0.281)

- **PATRÓN** `drift_15min` |x|≤ `2.3607` → IC=+0.316 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3607 (IC base=+0.281)

- **PATRÓN** `drift_60min` |x|≤ `0.9999` → IC=+0.303 (n=150)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9999 (IC base=+0.281)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.315 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.281)

- **PATRÓN** `ballena_activa_n` < `1717.0` → IC=+0.326 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1717.0 (IC base=+0.281)

### LIQUIDACIONES_15M
- **FILTRO** `py_entrada` < `0.415` → IC=-0.171 (n=71)

  - _Acción_: SKIP cuando `py_entrada` < 0.415
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=240)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=295)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=1663)

### LIQUIDACIONES_15M#BNB#15min
- **PATRÓN** `liq_n` > `2.0` → IC=+0.191 (n=95)

  - _Acción_: Kelly boost +0.95€ cuando `liq_n` > 2.0 (IC base=+0.094)

- **PATRÓN** `liq_usd_total` > `99.26` → IC=+0.124 (n=195)

  - _Acción_: Kelly boost +0.62€ cuando `liq_usd_total` > 99.26 (IC base=+0.094)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.185 (n=71)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 6.0 (IC base=+0.094)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.124 (n=107)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.094)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.135 (n=102)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.03 (IC base=+0.094)

### LIQUIDACIONES_15M#DOGE#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=138)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.124 (n=115)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 10.0 (IC base=+0.087)

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
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=286)

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
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=4310)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=268)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=225)

- **FILTRO** `ballena_activa_n` > `39.0` → IC=-0.178 (n=85)

  - _Acción_: SKIP cuando `ballena_activa_n` > 39.0
  - _Potencial_: sin este filtro IC_bueno=+0.180 (n=170)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.180 (n=170)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 39.0 (IC base=+0.026)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.167 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=15)

- **FILTRO** `libro_liquidez` < `13988.6712` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 13988.6712
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.135 (n=299)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.495 (IC base=+0.024)

### LIQUIDACIONES_5M#DOGE#5min
- **PATRÓN** `liq_n` > `3.0` → IC=+0.333 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 3.0 (IC base=+0.184)

- **PATRÓN** `liq_usd_total` > `2729.38` → IC=+0.283 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 2729.38 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.204 (n=133)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.231 (n=91)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.184)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.195 (n=126)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 13.0 (IC base=+0.184)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=1709)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=1663)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.286 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.505` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=773)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=782)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M#XRP#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=591)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=572)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.138 (n=241)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.495 (IC base=-0.001)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=1195)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=1195)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=1628)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=1628)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=376)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=376)

- **FILTRO** `py_entrada` < `0.425` → IC=-0.144 (n=85)

  - _Acción_: SKIP cuando `py_entrada` < 0.425
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=306)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.136 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=426)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=475)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=347)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=457)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=457)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=447)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.131 (n=3811)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=9759)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.147 (n=120)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=149)

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
- **FILTRO** `py_entrada` < `0.4` → IC=-0.165 (n=460)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=1104)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.144 (n=360)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=982)

- **PATRÓN** `py_entrada` < `0.51` → IC=+0.135 (n=461)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.51 (IC base=-0.011)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.127 (n=210)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=484)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.127 (n=231)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=469)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.165 (n=249)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=1347)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.138 (n=387)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=814)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **FILTRO** `py_entrada` < `0.42` → IC=-0.131 (n=591)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=747)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.124 (n=628)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=652)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.134 (n=675)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=776)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.178 (n=9363)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=29104)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.171 (n=9689)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=30145)

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
- **FILTRO** `py_entrada` > `0.57` → IC=-0.173 (n=1415)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=4326)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.197 (n=1749)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=5429)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.134 (n=2186)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 1.0 (IC base=+0.032)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` > `0.575` → IC=-0.181 (n=1433)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=4361)

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
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=3455)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=4407)

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
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=1285)

### MOMENTUM_IBS_15M_FADE#DOGE#15min
- **FILTRO** `ibs_20min` > `0.7158` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7158
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=50)

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
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=381)

- **FILTRO** `libro_liquidez` < `3260.3832` → IC=-0.185 (n=163)

  - _Acción_: SKIP cuando `libro_liquidez` < 3260.3832
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=331)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=983)

- **FILTRO** `ibs_20min` > `0.8625` → IC=-0.129 (n=648)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8625
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=650)

- **FILTRO** `ballena_activa_n` > `21.0` → IC=-0.175 (n=438)

  - _Acción_: SKIP cuando `ballena_activa_n` > 21.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=851)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `14.0` → IC=-0.141 (n=76)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=234)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.137 (n=26091)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=59076)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.302 (n=20743)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=64424)

- **FILTRO** `ibs_7min` < `0.7273` → IC=-0.225 (n=27972)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7273
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=57195)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.154 (n=28000)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=57167)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.247 (n=26340)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=79990)

- **FILTRO** `ibs_7min` > `0.278` → IC=-0.182 (n=26579)

  - _Acción_: SKIP cuando `ibs_7min` > 0.278
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=79751)

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
- **FILTRO** `hora_utc` < `6.0` → IC=-0.128 (n=3455)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.104 (n=10870)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.267 (n=3510)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=10815)

- **FILTRO** `ibs_7min` < `0.7106` → IC=-0.214 (n=3580)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7106
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=10745)

- **FILTRO** `ballena_activa_n` > `157.0` → IC=-0.204 (n=3561)

  - _Acción_: SKIP cuando `ballena_activa_n` > 157.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=10764)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.266 (n=3345)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=11321)

- **FILTRO** `ibs_7min` > `0.2636` → IC=-0.188 (n=3666)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2636
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=11000)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.178 (n=3660)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=11006)

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
- **FILTRO** `py_entrada` < `0.33` → IC=-0.276 (n=3203)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=10813)

- **FILTRO** `ibs_7min` < `0.7115` → IC=-0.201 (n=3504)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7115
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=10512)

- **FILTRO** `ballena_activa_n` > `26.0` → IC=-0.196 (n=3471)

  - _Acción_: SKIP cuando `ballena_activa_n` > 26.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=10545)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.259 (n=3388)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=11141)

- **FILTRO** `ibs_7min` > `0.2716` → IC=-0.177 (n=3626)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2716
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=10903)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.173 (n=3526)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=11003)

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
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1038)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=1327)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.156 (n=187)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=686)

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
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=595)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.162 (n=255)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=504)

- **FILTRO** `libro_liquidez` < `3306.2556` → IC=-0.146 (n=196)

  - _Acción_: SKIP cuando `libro_liquidez` < 3306.2556
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=591)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=56)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=562)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4305` → IC=+0.143 (n=786)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio` |x|> 0.4305 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.130 (n=885)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 6.0 (IC base=+0.124)

- **PATRÓN** `total_vol_5m` < `459.6089` → IC=+0.164 (n=576)

  - _Acción_: Kelly boost +0.82€ cuando `total_vol_5m` < 459.6089 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `3678.0144` → IC=+0.131 (n=784)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 3678.0144 (IC base=+0.124)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.182 (n=196)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 14.0 (IC base=+0.140)

- **PATRÓN** `total_vol_5m` < `292.267` → IC=+0.174 (n=265)

  - _Acción_: Kelly boost +0.87€ cuando `total_vol_5m` < 292.267 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.145 (n=359)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.04 (IC base=+0.140)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3988` → IC=+0.136 (n=363)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio` |x|> 0.3988 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.139 (n=339)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 15.0 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.121 (n=441)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.04 (IC base=+0.119)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.416` → IC=+0.164 (n=209)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.82€ cuando `delta_ratio` |x|> 0.416 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.155 (n=288)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.130)

- **PATRÓN** `total_vol_5m` < `705.9846` → IC=+0.173 (n=276)

  - _Acción_: Kelly boost +0.86€ cuando `total_vol_5m` < 705.9846 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `7706.3933` → IC=+0.130 (n=209)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 7706.3933 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.187 (n=113)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 59.0 (IC base=+0.130)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4318` → IC=+0.213 (n=134)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4318 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.136 (n=105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 17.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.158 (n=118)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 5.0 (IC base=+0.134)

- **PATRÓN** `total_vol_5m` < `4819.793` → IC=+0.180 (n=198)

  - _Acción_: Kelly boost +0.90€ cuando `total_vol_5m` < 4819.793 (IC base=+0.134)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `13.0` → IC=+0.122 (n=318)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` < 13.0 (IC base=+0.095)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.131 (n=220)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.095)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `6.1729` → IC=-0.222 (n=88)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 6.1729
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=172)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.148 (n=345)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0048 (IC base=-0.028)

### PRICE_TARGET_GBM#ETH#atexpiry
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.268 (n=80)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.003)

- **PATRÓN** `pct_vs_K` |x|≤ `2.0091` → IC=+0.220 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 2.0091 (IC base=+0.003)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `T_h` > `76.1623` → IC=-0.125 (n=70)

  - _Acción_: SKIP cuando `T_h` > 76.1623
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=24)

- **FILTRO** `pct_vs_K` |x|> `6.3582` → IC=-0.258 (n=31)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 6.3582
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=63)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0151` → IC=-0.206 (n=49)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0151
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=149)

### PRICE_TARGET_GBM#SOL#reach
- **FILTRO** `sigma_h` < `0.0173` → IC=-0.167 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0173
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` > `0.011` → IC=-0.256 (n=301)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.011
  - _Potencial_: sin este filtro IC_bueno=-0.248 (n=589)

- **FILTRO** `T_h` > `66.9347` → IC=-0.257 (n=595)

  - _Acción_: SKIP cuando `T_h` > 66.9347
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=295)

- **FILTRO** `pct_vs_K` |x|> `3.0008` → IC=-0.368 (n=210)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.0008
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=640)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.01` → IC=-0.230 (n=220)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=75)

- **FILTRO** `T_h` > `49.2217` → IC=-0.249 (n=221)

  - _Acción_: SKIP cuando `T_h` > 49.2217
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=74)

- **FILTRO** `pct_vs_K` |x|> `2.8429` → IC=-0.348 (n=77)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.8429
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=238)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `pct_vs_K` |x|> `2.8218` → IC=-0.233 (n=28)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.8218
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `sigma_h` < `0.0078` → IC=-0.273 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0078
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=21)

- **FILTRO** `T_h` > `139.1329` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `T_h` > 139.1329
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=21)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.0097` → IC=-0.326 (n=130)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.288 (n=130)

- **FILTRO** `T_h` > `95.1632` → IC=-0.317 (n=129)

  - _Acción_: SKIP cuando `T_h` > 95.1632
  - _Potencial_: sin este filtro IC_bueno=-0.297 (n=131)

- **FILTRO** `sigma_h` > `0.0094` → IC=-0.148 (n=86)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0094
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=169)

- **FILTRO** `sigma_h` < `0.0058` → IC=-0.162 (n=63)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0058
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=192)

- **PATRÓN** `pct_vs_K` |x|≤ `1.9861` → IC=+0.157 (n=129)

  - _Acción_: Kelly boost +0.78€ cuando `pct_vs_K` |x|≤ 1.9861 (IC base=-0.095)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `sigma_h` < `0.0095` → IC=-0.180 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `sigma_h` < `0.0098` → IC=-0.214 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0098
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=19)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0132` → IC=-0.226 (n=82)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0132
  - _Potencial_: sin este filtro IC_bueno=-0.218 (n=161)

- **FILTRO** `sigma_h` < `0.0101` → IC=-0.232 (n=80)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0101
  - _Potencial_: sin este filtro IC_bueno=-0.215 (n=163)

- **FILTRO** `T_h` > `61.9454` → IC=-0.228 (n=182)

  - _Acción_: SKIP cuando `T_h` > 61.9454
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=61)

- **FILTRO** `sigma_h` > `0.0139` → IC=-0.303 (n=64)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0139
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=126)

- **FILTRO** `sigma_h` < `0.0097` → IC=-0.255 (n=47)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=143)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.106` → IC=+0.450 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.106 (IC base=+0.329)

- **PATRÓN** `sigma_h` < `0.0148` → IC=+0.343 (n=132)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0148 (IC base=+0.329)

- **PATRÓN** `sigma_h` > `0.0134` → IC=+0.339 (n=60)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0134 (IC base=+0.329)

- **PATRÓN** `T_h` < `0.3439` → IC=+0.391 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.3439 (IC base=+0.329)

- **PATRÓN** `T_h` > `0.7009` → IC=+0.344 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.7009 (IC base=+0.329)

- **PATRÓN** `dist_50` > `0.4594` → IC=+0.484 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4594 (IC base=+0.329)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.345 (n=153)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.329)

- **PATRÓN** `edge` > `0.0992` → IC=+0.424 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.0992 (IC base=+0.392)

- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.406 (n=137)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0124 (IC base=+0.392)

- **PATRÓN** `T_h` < `0.7258` → IC=+0.418 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.7258 (IC base=+0.392)

- **PATRÓN** `dist_50` > `0.368` → IC=+0.441 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.368 (IC base=+0.392)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.412 (n=349)
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
- **PATRÓN** `edge` > `0.1295` → IC=+0.441 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1295 (IC base=+0.271)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.324 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.271)

- **PATRÓN** `dist_50` > `0.4172` → IC=+0.441 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4172 (IC base=+0.271)

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
- **PATRÓN** `edge` > `0.1449` → IC=+0.487 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1449 (IC base=+0.424)

- **PATRÓN** `sigma_h` < `0.0155` → IC=+0.471 (n=67)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0155 (IC base=+0.424)

- **PATRÓN** `T_h` < `1.0409` → IC=+0.427 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.0409 (IC base=+0.424)

- **PATRÓN** `T_h` > `0.3968` → IC=+0.436 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.3968 (IC base=+0.424)

- **PATRÓN** `dist_50` > `0.3288` → IC=+0.474 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3288 (IC base=+0.424)

- **PATRÓN** `edge` > `0.1937` → IC=+0.472 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1937 (IC base=+0.465)

- **PATRÓN** `sigma_h` < `0.0162` → IC=+0.475 (n=161)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0162 (IC base=+0.465)

- **PATRÓN** `T_h` < `0.8021` → IC=+0.459 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.8021 (IC base=+0.465)

- **PATRÓN** `T_h` > `1.4857` → IC=+0.482 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4857 (IC base=+0.465)

- **PATRÓN** `dist_50` > `0.414` → IC=+0.482 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.414 (IC base=+0.465)

- **PATRÓN** `hora_utc` < `2.0` → IC=+0.485 (n=63)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 2.0 (IC base=+0.465)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=500)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=534)

- **PATRÓN** `streak_estiramiento` < `0.3787` → IC=+0.137 (n=166)

  - _Acción_: Kelly boost +0.68€ cuando `streak_estiramiento` < 0.3787 (IC base=+0.020)

- **PATRÓN** `streak_estiramiento` < `0.8333` → IC=+0.126 (n=370)

  - _Acción_: Kelly boost +0.63€ cuando `streak_estiramiento` < 0.8333 (IC base=+0.062)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.125 (n=283)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 29.0 (IC base=+0.062)

### STREAK_FADE_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` < 0.495 (IC base=+0.085)

- **PATRÓN** `streak_estiramiento` < `0.5551` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.5551 (IC base=+0.085)

- **PATRÓN** `ballena_activa_n` < `68.0` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 68.0 (IC base=+0.085)

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
- **PATRÓN** `streak_estiramiento` < `0.3854` → IC=+0.127 (n=132)

  - _Acción_: Kelly boost +0.63€ cuando `streak_estiramiento` < 0.3854 (IC base=+0.037)

- **PATRÓN** `streak_estiramiento` < `0.3787` → IC=+0.211 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.3787 (IC base=+0.085)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.139 (n=203)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 35.0 (IC base=+0.085)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.194 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=105)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=62)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.136 (n=31)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=47)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=826)

### STREAK_FADE_60M
- **FILTRO** `py_entrada` < `0.515` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.134 (n=39)

- **PATRÓN** `py_entrada` > `0.515` → IC=+0.134 (n=39)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` > 0.515 (IC base=+0.017)

- **PATRÓN** `streak_estiramiento` < `0.6279` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.6279 (IC base=+0.010)

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
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=1121)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1364)

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
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=5698)

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
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=3418)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.184 (n=2233)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0059 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.2337` → IC=+0.158 (n=6698)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2337 (IC base=+0.131)

- **PATRÓN** `drift_15min` |x|≤ `1.1278` → IC=+0.132 (n=6698)

  - _Acción_: Kelly boost +0.66€ cuando `drift_15min` |x|≤ 1.1278 (IC base=+0.131)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0643` → IC=+0.132 (n=6696)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio_macro` |x|> 0.0643 (IC base=+0.131)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0993` → IC=+0.143 (n=2114)

  - _Acción_: Kelly boost +0.72€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0993 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.143 (n=6208)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 6.0 (IC base=+0.131)

- **PATRÓN** `ibs_15` > `0.55` → IC=+0.206 (n=5990)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.55 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.963` → IC=+0.227 (n=1252)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.963 (IC base=+0.131)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=3500)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `4314.4132` → IC=+0.171 (n=2233)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 4314.4132 (IC base=+0.131)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=2611)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.247 (n=303)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.0772` → IC=+0.247 (n=398)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0772 (IC base=+0.206)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2662` → IC=+0.229 (n=301)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2662 (IC base=+0.206)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2242` → IC=+0.218 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2242 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.232 (n=837)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.206)

- **PATRÓN** `ibs_15` > `0.702` → IC=+0.276 (n=903)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.702 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `0.3997` → IC=+0.233 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3997 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` < `0.5549` → IC=+0.209 (n=1020)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5549 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.968` → IC=+0.302 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.968 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.209 (n=1172)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `11847.0948` → IC=+0.220 (n=602)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11847.0948 (IC base=+0.206)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.147 (n=1025)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0068 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.1093` → IC=+0.146 (n=777)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.1093 (IC base=+0.132)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0831` → IC=+0.138 (n=1041)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio_macro` |x|> 0.0831 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.143 (n=827)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 11.0 (IC base=+0.132)

- **PATRÓN** `ibs_15` > `0.477` → IC=+0.216 (n=1165)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.477 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` > `0.1243` → IC=+0.145 (n=722)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.1243 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` < `0.6708` → IC=+0.131 (n=1322)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.6708 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.945` → IC=+0.284 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.945 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `6122.7931` → IC=+0.174 (n=529)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 6122.7931 (IC base=+0.132)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.143 (n=1692)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` > 0.0118 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.2399` → IC=+0.176 (n=1693)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2399 (IC base=+0.137)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0586` → IC=+0.139 (n=1692)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio_macro` |x|> 0.0586 (IC base=+0.137)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.093` → IC=+0.185 (n=531)

  - _Acción_: Kelly boost +0.92€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.093 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.145 (n=1547)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 6.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.141 (n=1492)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 14.0 (IC base=+0.137)

- **PATRÓN** `ibs_15` > `0.6959` → IC=+0.231 (n=1128)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6959 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.215` → IC=+0.141 (n=775)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.215 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.915` → IC=+0.141 (n=1956)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.915 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.952` → IC=+0.183 (n=392)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 16.952 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `2939.6834` → IC=+0.178 (n=768)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 2939.6834 (IC base=+0.137)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `drift_60min` |x|≤ `0.1103` → IC=+0.365 (n=552)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1103 (IC base=+0.363)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1435` → IC=+0.379 (n=551)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1435 (IC base=+0.363)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.102` → IC=+0.380 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.102 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.373 (n=877)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.363)

- **PATRÓN** `ibs_15` > `0.788` → IC=+0.394 (n=829)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.788 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` > `0.2719` → IC=+0.384 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2719 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.766` → IC=+0.395 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.766 (IC base=+0.363)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.365 (n=1006)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.363)

- **PATRÓN** `libro_liquidez` > `9610.6074` → IC=+0.378 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9610.6074 (IC base=+0.363)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.1527` → IC=+0.366 (n=348)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1527 (IC base=+0.364)

- **PATRÓN** `drift_15min` |x|≤ `0.4181` → IC=+0.364 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4181 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2175` → IC=+0.379 (n=179)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2175 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1436` → IC=+0.400 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1436 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.381 (n=368)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.364)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.364 (n=402)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.8048` → IC=+0.384 (n=396)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8048 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.2552` → IC=+0.394 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2552 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.649` → IC=+0.385 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.649 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `16402.4254` → IC=+0.388 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16402.4254 (IC base=+0.364)

- **PATRÓN** `ballena_activa_n` < `409.0` → IC=+0.386 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 409.0 (IC base=+0.364)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.364 (n=145)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.362)

- **PATRÓN** `drift_60min` |x|≤ `0.1058` → IC=+0.366 (n=290)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1058 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1258` → IC=+0.379 (n=288)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1258 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1009` → IC=+0.383 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1009 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.367 (n=435)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.362)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.372 (n=201)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.762` → IC=+0.396 (n=432)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.762 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.4613` → IC=+0.379 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4613 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` < `0.6907` → IC=+0.361 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6907 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.854` → IC=+0.400 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.854 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.478` → IC=+0.363 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.478 (IC base=+0.362)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.362 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `4937.9359` → IC=+0.370 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4937.9359 (IC base=+0.362)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0079` → IC=-0.204 (n=3101)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0079
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=3102)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.221 (n=2751)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=3452)

- **PATRÓN** `ibs_15` > `0.6288` → IC=+0.278 (n=1364)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6288 (IC base=-0.087)

- **PATRÓN** `dist_vwap_pct` > `0.1169` → IC=+0.207 (n=808)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1169 (IC base=-0.087)

- **PATRÓN** `dist_vwap_pct` < `0.6018` → IC=+0.200 (n=1446)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6018 (IC base=-0.087)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2274` → IC=+0.267 (n=2048)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2274 (IC base=+0.002)

- **PATRÓN** `ibs_15` < `0.3773` → IC=+0.281 (n=6142)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3773 (IC base=+0.002)

- **PATRÓN** `dist_vwap_pct` > `0.7113` → IC=+0.263 (n=889)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7113 (IC base=+0.002)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` < `0.0041` → IC=-0.207 (n=1033)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0041
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=3100)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.185 (n=1932)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=2201)

- **FILTRO** `sigma_ewma_delta_pct` > `22.161` → IC=-0.234 (n=581)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.161
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=3552)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.180 (n=95)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=4038)

- **FILTRO** `libro_liquidez` < `10121.4993` → IC=-0.193 (n=1363)

  - _Acción_: SKIP cuando `libro_liquidez` < 10121.4993
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=2770)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2673` → IC=+0.282 (n=163)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2673 (IC base=+0.065)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1441` → IC=+0.285 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1441 (IC base=+0.065)

- **PATRÓN** `ibs_15` > `0.7533` → IC=+0.317 (n=489)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7533 (IC base=+0.065)

- **PATRÓN** `dist_vwap_pct` > `0.1068` → IC=+0.284 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1068 (IC base=+0.065)

- **PATRÓN** `dist_vwap_pct` < `0.5501` → IC=+0.286 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5501 (IC base=+0.065)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.729` → IC=+0.140 (n=245)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 21.729 (IC base=+0.065)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0758` → IC=+0.221 (n=84)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0758 (IC base=-0.179)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1389` → IC=+0.289 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1389 (IC base=-0.179)

- **PATRÓN** `ibs_15` < `0.6283` → IC=+0.293 (n=85)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6283 (IC base=-0.179)

- **PATRÓN** `dist_vwap_pct` < `0.05` → IC=+0.275 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.05 (IC base=-0.179)

- **PATRÓN** `ballena_activa_n` < `392.0` → IC=+0.302 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 392.0 (IC base=-0.179)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=903)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.161 (n=691)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0067 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.0718` → IC=+0.174 (n=305)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0718 (IC base=+0.149)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.183 (n=547)

  - _Acción_: Kelly boost +0.92€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.173 (n=496)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 11.0 (IC base=+0.149)

- **PATRÓN** `ibs_15` > `0.5653` → IC=+0.240 (n=690)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5653 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.6763` → IC=+0.174 (n=136)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.6763 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.1598` → IC=+0.150 (n=529)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1598 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.357` → IC=+0.254 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.357 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=903)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `5213.5522` → IC=+0.169 (n=460)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 5213.5522 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.250 (n=1618)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.484` → IC=+0.242 (n=2427)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.484 (IC base=+0.234)

- **PATRÓN** `drift_15min` |x|≤ `0.832` → IC=+0.247 (n=2135)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.832 (IC base=+0.234)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1966` → IC=+0.255 (n=1100)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1966 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.238 (n=892)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.239 (n=1080)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.234)

- **PATRÓN** `ibs_15` < `0.1932` → IC=+0.293 (n=1619)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1932 (IC base=+0.234)

- **PATRÓN** `dist_vwap_pct` > `0.2399` → IC=+0.246 (n=824)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2399 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.511` → IC=+0.240 (n=1046)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.511 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.307` → IC=+0.237 (n=2553)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.307 (IC base=+0.234)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.2008` → IC=-0.299 (n=372)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.2008
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=1119)

- **FILTRO** `drift_60min` |x|> `0.2014` → IC=-0.291 (n=372)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2014
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=1119)

- **FILTRO** `drift_15min` |x|> `1.0228` → IC=-0.302 (n=372)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.0228
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=1119)

- **FILTRO** `sigma_ewma_delta_pct` > `6.067` → IC=-0.210 (n=326)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.067
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=1165)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.188 (n=46)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.205)

- **PATRÓN** `ibs_15` > `0.9231` → IC=+0.380 (n=23)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9231 (IC base=-0.205)

- **PATRÓN** `dist_vwap_pct` < `0.4298` → IC=+0.158 (n=77)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.4298 (IC base=-0.205)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 37.0 (IC base=-0.205)

- **PATRÓN** `ibs_15` < `0.381` → IC=+0.295 (n=1013)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.381 (IC base=-0.025)

- **PATRÓN** `dist_vwap_pct` < `0.4722` → IC=+0.253 (n=1086)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4722 (IC base=-0.025)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1213` → IC=-0.272 (n=865)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1213
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=867)

- **FILTRO** `drift_15min` |x|> `1.2903` → IC=-0.283 (n=432)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2903
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=1300)

- **FILTRO** `sigma_ewma_delta_pct` > `7.24` → IC=-0.227 (n=522)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.24
  - _Potencial_: sin este filtro IC_bueno=-0.219 (n=1210)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.250 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=1710)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.222)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.222)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0706` → IC=+0.283 (n=1265)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0706 (IC base=-0.008)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1183` → IC=+0.287 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1183 (IC base=-0.008)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.295 (n=1426)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.008)

- **PATRÓN** `dist_vwap_pct` > `0.7886` → IC=+0.327 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7886 (IC base=-0.008)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.167 (n=58)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0063 (IC base=+0.096)

- **PATRÓN** `drift_15min` |x|≤ `0.7471` → IC=+0.147 (n=66)

  - _Acción_: Kelly boost +0.74€ cuando `drift_15min` |x|≤ 0.7471 (IC base=+0.096)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.235` → IC=+0.159 (n=42)

  - _Acción_: Kelly boost +0.80€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.235 (IC base=+0.096)

- **PATRÓN** `ibs_15` > `0.8357` → IC=+0.312 (n=30)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8357 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` < `0.0949` → IC=+0.214 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0949 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.113` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 13.113 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 52.0 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.1943` → IC=+0.135 (n=94)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.1943 (IC base=+0.050)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.167 (n=58)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0063 (IC base=+0.096)

- **PATRÓN** `drift_15min` |x|≤ `0.7471` → IC=+0.147 (n=66)

  - _Acción_: Kelly boost +0.74€ cuando `drift_15min` |x|≤ 0.7471 (IC base=+0.096)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.235` → IC=+0.159 (n=42)

  - _Acción_: Kelly boost +0.80€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.235 (IC base=+0.096)

- **PATRÓN** `ibs_15` > `0.8357` → IC=+0.312 (n=30)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8357 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` < `0.0949` → IC=+0.214 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0949 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.113` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 13.113 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 52.0 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.1943` → IC=+0.135 (n=94)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.1943 (IC base=+0.050)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.298 (n=508)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0035 (IC base=+0.285)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.293 (n=506)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.0714` → IC=+0.308 (n=669)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0714 (IC base=+0.285)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0674` → IC=+0.287 (n=1518)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0674 (IC base=+0.285)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2166` → IC=+0.288 (n=934)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2166 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.297 (n=1584)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.285)

- **PATRÓN** `ibs_15` > `0.8358` → IC=+0.311 (n=1519)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8358 (IC base=+0.285)

- **PATRÓN** `dist_vwap_pct` > `0.2762` → IC=+0.317 (n=648)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2762 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.577` → IC=+0.388 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.577 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `13043.7974` → IC=+0.301 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13043.7974 (IC base=+0.285)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.306 (n=266)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.280)

- **PATRÓN** `drift_60min` |x|≤ `0.0763` → IC=+0.299 (n=352)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0763 (IC base=+0.280)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2692` → IC=+0.284 (n=266)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2692 (IC base=+0.280)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2266` → IC=+0.292 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2266 (IC base=+0.280)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.303 (n=736)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.280)

- **PATRÓN** `ibs_15` > `0.8545` → IC=+0.308 (n=712)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8545 (IC base=+0.280)

- **PATRÓN** `dist_vwap_pct` > `0.2612` → IC=+0.311 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2612 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.371` → IC=+0.393 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.371 (IC base=+0.280)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.281 (n=1032)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `14412.9472` → IC=+0.310 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14412.9472 (IC base=+0.280)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.300 (n=318)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.290)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.290 (n=241)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.0502` → IC=+0.323 (n=241)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0502 (IC base=+0.290)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0636` → IC=+0.296 (n=722)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0636 (IC base=+0.290)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1009` → IC=+0.311 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1009 (IC base=+0.290)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.299 (n=743)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.290)

- **PATRÓN** `ibs_15` > `0.8447` → IC=+0.316 (n=722)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8447 (IC base=+0.290)

- **PATRÓN** `dist_vwap_pct` > `0.2918` → IC=+0.317 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2918 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.835` → IC=+0.377 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.835 (IC base=+0.290)

### UPDOWN_OU_5M
- **FILTRO** `delta_ratio_macro` |x|≤ `0.126` → IC=-0.170 (n=98)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.126
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=300)

- **FILTRO** `ballena_activa_n` > `31.0` → IC=-0.146 (n=272)

  - _Acción_: SKIP cuando `ballena_activa_n` > 31.0
  - _Potencial_: sin este filtro IC_bueno=-0.104 (n=94)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.162 (n=128)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.101 (n=386)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.197 (n=186)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=67)

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
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=171)

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
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1635` → IC=-0.283 (n=21)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1635
  - _Potencial_: sin este filtro IC_bueno=-0.128 (n=41)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.237 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=51)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.0549` → IC=-0.237 (n=17)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.0549
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=51)

### WEEKLY_PRICE
- **PATRÓN** `ratio` < `0.9866` → IC=+0.252 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9866 (IC base=+0.122)

- **PATRÓN** `T_h` > `115.9003` → IC=+0.352 (n=3372)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 115.9003 (IC base=+0.331)

- **PATRÓN** `ratio` > `1.0158` → IC=+0.387 (n=650)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0158 (IC base=+0.331)

### WEEKLY_PRICE#BTC
- **PATRÓN** `ratio` < `0.9756` → IC=+0.190 (n=217)

  - _Acción_: Kelly boost +0.95€ cuando `ratio` < 0.9756 (IC base=+0.064)

- **PATRÓN** `T_h` > `110.2068` → IC=+0.325 (n=1248)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 110.2068 (IC base=+0.302)

- **PATRÓN** `ratio` > `1.0004` → IC=+0.298 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0004 (IC base=+0.302)

### WEEKLY_PRICE#ETH
- **PATRÓN** `ratio` < `0.9775` → IC=+0.361 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9775 (IC base=+0.185)

- **PATRÓN** `T_h` > `111.9957` → IC=+0.347 (n=1241)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9957 (IC base=+0.313)

- **PATRÓN** `ratio` > `1.0221` → IC=+0.406 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0221 (IC base=+0.313)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0398` → IC=+0.409 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0398 (IC base=+0.396)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.55 sube el IC de +0.131 a +0.206 en UPDOWN_GBM#15min (n=5990). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.702 sube el IC de +0.206 a +0.276 en UPDOWN_GBM#BTC#15min (n=903). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.477 sube el IC de +0.132 a +0.216 en UPDOWN_GBM#ETH#15min (n=1165). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.6959 sube el IC de +0.137 a +0.231 en UPDOWN_GBM#XRP#15min (n=1128). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6288 sube el IC de -0.087 a +0.278 en UPDOWN_GBM_15M_TARDIO (n=1364). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3773 sube el IC de +0.002 a +0.281 en UPDOWN_GBM_15M_TARDIO (n=6142). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7533 sube el IC de +0.065 a +0.317 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=489). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6283 sube el IC de -0.179 a +0.293 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=85). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5653 sube el IC de +0.149 a +0.240 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=690). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.1932 sube el IC de +0.234 a +0.293 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1619). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.9231 sube el IC de -0.205 a +0.380 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.381 sube el IC de -0.025 a +0.295 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=1013). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.222 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.008 a +0.295 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=1426). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8357 sube el IC de +0.096 a +0.312 en UPDOWN_GBM_ETH_15M_HORA7 (n=30). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8357 sube el IC de +0.096 a +0.312 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=30). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8358 sube el IC de +0.285 a +0.311 en UPDOWN_GBM_IBS_ALTO (n=1519). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8545 sube el IC de +0.280 a +0.308 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=712). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8447 sube el IC de +0.290 a +0.316 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=722). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.363 a +0.394 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=829). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8048 sube el IC de +0.364 a +0.384 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=396). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.762 sube el IC de +0.362 a +0.396 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=432). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2381 | +0.085 | +263.88€ | 1 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2381 | +0.085 | +263.88€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1969 | +0.086 | +224.39€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1969 | +0.086 | +224.39€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 285 | +0.068 | +10.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 285 | +0.068 | +10.79€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 96 | +0.122 | +29.03€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 96 | +0.122 | +29.03€ | 0 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 1512 | -0.028 | +49.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 1512 | -0.028 | +49.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 1188 | -0.040 | +36.60€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 1188 | -0.040 | +36.60€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 224 | +0.035 | +20.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 224 | +0.035 | +20.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 93 | -0.037 | -10.65€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 93 | -0.037 | -10.65€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 51819 | -0.086 | -6597.19€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 3421 | +0.093 | -322.02€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 48398 | -0.099 | -6275.17€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 5088 | -0.116 | -816.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 5088 | -0.116 | -816.49€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 3421 | +0.093 | -322.02€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 3421 | +0.093 | -322.02€ | 0 | 1 |
| ✅ BALLENAS_TARDIAS#DOGE | 5129 | -0.108 | -957.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 5129 | -0.108 | -957.76€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 14609 | -0.043 | -1330.44€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 14609 | -0.043 | -1330.44€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 14135 | -0.121 | -1627.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 14135 | -0.121 | -1627.38€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 9437 | -0.138 | -1543.09€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 9437 | -0.138 | -1543.09€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 58351 | -0.012 | +2533.18€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 15040 | +0.004 | +1473.85€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 43311 | -0.017 | +1059.34€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 58351 | -0.012 | +2533.18€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 15040 | +0.004 | +1473.85€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 43311 | -0.017 | +1059.34€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 216748 | +0.112 | -8966.39€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#15min | 23733 | +0.178 | -780.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 1014 | +0.023 | -80.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 179708 | +0.104 | -7687.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 12293 | +0.095 | -417.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 29797 | +0.101 | -2140.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 90 | -0.196 | +9.57€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 29670 | +0.102 | -2159.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#60min | 22 | +0.167 | +21.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 40528 | +0.122 | -675.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5749 | +0.175 | -240.43€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 29747 | +0.119 | -239.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4990 | +0.081 | -173.17€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 29848 | +0.098 | -2103.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 114 | -0.103 | +20.42€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 29706 | +0.099 | -2116.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#60min | 13 | -0.065 | +4.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 46427 | +0.123 | -1018.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 11559 | +0.176 | -347.79€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 30231 | +0.105 | -577.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 4625 | +0.103 | -84.22€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 40342 | +0.111 | -1708.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 6121 | +0.200 | -235.47€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 917 | +0.046 | -26.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 30664 | +0.095 | -1258.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2640 | +0.107 | -188.01€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO#XRP | 29806 | +0.106 | -1319.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 100 | -0.137 | +13.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 29690 | +0.107 | -1335.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 35376 | +0.188 | -2720.90€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 35376 | +0.188 | -2720.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 8009 | +0.159 | -969.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 8009 | +0.159 | -969.83€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 5350 | +0.193 | -242.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 5350 | +0.193 | -242.10€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 7814 | +0.171 | -736.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 7814 | +0.171 | -736.48€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 6474 | +0.251 | -236.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 6474 | +0.251 | -236.82€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 7650 | +0.182 | -549.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 7650 | +0.182 | -549.43€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1359 | +0.424 | -56.09€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1359 | +0.424 | -56.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 580 | +0.438 | -6.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 580 | +0.438 | -6.57€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 528 | +0.421 | -23.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 528 | +0.421 | -23.69€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 237 | +0.395 | -21.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 237 | +0.395 | -21.97€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 124990 | +0.199 | -9157.48€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 124990 | +0.199 | -9157.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 21674 | +0.174 | -2585.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 21674 | +0.174 | -2585.47€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 20136 | +0.223 | -670.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 20136 | +0.223 | -670.97€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 21435 | +0.180 | -2261.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 21435 | +0.180 | -2261.71€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 20322 | +0.217 | -790.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 20322 | +0.217 | -790.51€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 20614 | +0.206 | -1201.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 20614 | +0.206 | -1201.92€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 20809 | +0.196 | -1646.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 20809 | +0.196 | -1646.91€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 48626 | +0.116 | +401.09€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 48626 | +0.116 | +401.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 24217 | +0.117 | +265.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 24217 | +0.117 | +265.99€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 24409 | +0.115 | +135.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 24409 | +0.115 | +135.10€ | 0 | 3 |
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
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 2074 | +0.064 | -107.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1349 | +0.073 | -43.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1640 | +0.069 | -62.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1349 | +0.073 | -43.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 99551 | +0.101 | -2096.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 8081 | +0.097 | +194.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 91470 | +0.101 | -2291.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 54303 | +0.105 | -443.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 8081 | +0.097 | +194.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 46222 | +0.106 | -638.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 21448 | +0.109 | -97.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 21448 | +0.109 | -97.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 23800 | +0.083 | -1556.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 23800 | +0.083 | -1556.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 940 | +0.174 | -110.40€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 940 | +0.174 | -110.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 940 | +0.174 | -110.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 940 | +0.174 | -110.40€ | 2 | 4 |
| ✅ GBM_LATE_15M | 67828 | +0.102 | +38193.37€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 67828 | +0.102 | +38193.37€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 11280 | +0.223 | +9602.19€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 11280 | +0.223 | +9602.19€ | 0 | 19 |
| ✅ GBM_LATE_15M#BTC | 10623 | +0.176 | +8584.90€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 10623 | +0.176 | +8584.90€ | 0 | 23 |
| ✅ GBM_LATE_15M#DOGE | 12129 | +0.207 | +9560.82€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 12129 | +0.207 | +9560.82€ | 0 | 22 |
| ✅ GBM_LATE_15M#ETH | 8963 | +0.063 | +3061.72€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 8963 | +0.063 | +3061.72€ | 1 | 18 |
| ✅ GBM_LATE_15M#SOL | 9389 | -0.024 | +2449.87€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 9389 | -0.024 | +2449.87€ | 4 | 14 |
| ✅ GBM_LATE_15M#XRP | 15444 | -0.019 | +4933.88€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 15444 | -0.019 | +4933.88€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 72053 | +0.088 | +42318.53€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 72053 | +0.088 | +42318.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 13995 | -0.002 | +7418.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 13995 | -0.002 | +7418.79€ | 3 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 15476 | +0.008 | +4314.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 15476 | +0.008 | +4314.52€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 9625 | +0.296 | +11030.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 9625 | +0.296 | +11030.35€ | 0 | 22 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 13800 | +0.020 | +4448.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 13800 | +0.020 | +4448.16€ | 0 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 10953 | +0.051 | +5151.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 10953 | +0.051 | +5151.81€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 8204 | +0.313 | +9954.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 8204 | +0.313 | +9954.89€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 53371 | +0.179 | +44386.45€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 53371 | +0.179 | +44386.45€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 8096 | +0.238 | +7466.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 8096 | +0.238 | +7466.93€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 8534 | +0.141 | +6461.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 8534 | +0.141 | +6461.11€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 8584 | +0.223 | +7421.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 8584 | +0.223 | +7421.41€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 9115 | +0.130 | +7166.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 9115 | +0.130 | +7166.17€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 10057 | +0.124 | +7803.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 10057 | +0.124 | +7803.47€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 8985 | +0.231 | +8067.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 8985 | +0.231 | +8067.36€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 14687 | +0.125 | +7456.32€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 14687 | +0.125 | +7456.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 680 | +0.161 | +443.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 680 | +0.161 | +443.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3871 | +0.126 | +2079.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3871 | +0.126 | +2079.00€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 509 | +0.156 | +286.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 509 | +0.156 | +286.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 4297 | +0.125 | +2162.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 4297 | +0.125 | +2162.55€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 3975 | +0.100 | +1625.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 3975 | +0.100 | +1625.47€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1355 | +0.168 | +858.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1355 | +0.168 | +858.78€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 68161 | +0.189 | +56745.06€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 68161 | +0.189 | +56745.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 10790 | +0.247 | +10305.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 10790 | +0.247 | +10305.76€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 10947 | +0.143 | +8010.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 10947 | +0.143 | +8010.49€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 11544 | +0.234 | +10374.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 11544 | +0.234 | +10374.52€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 11276 | +0.145 | +8514.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 11276 | +0.145 | +8514.26€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 12025 | +0.129 | +8815.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 12025 | +0.129 | +8815.93€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 11579 | +0.240 | +10724.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 11579 | +0.240 | +10724.10€ | 0 | 23 |
| ✅ GBM_LATE_5M | 17184 | +0.220 | +14570.34€ | 0 | 27 |
| ✅ GBM_LATE_5M#5min | 17184 | +0.220 | +14570.34€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1948 | +0.253 | +1898.73€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1948 | +0.253 | +1898.73€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3342 | +0.210 | +2860.74€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3342 | +0.210 | +2860.74€ | 0 | 25 |
| ✅ GBM_LATE_5M#DOGE | 1591 | +0.218 | +1323.18€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1591 | +0.218 | +1323.18€ | 0 | 18 |
| ✅ GBM_LATE_5M#ETH | 5022 | +0.211 | +3973.52€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 5022 | +0.211 | +3973.52€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 3089 | +0.232 | +2764.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 3089 | +0.232 | +2764.28€ | 0 | 26 |
| ✅ GBM_LATE_5M#XRP | 2192 | +0.212 | +1749.89€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 2192 | +0.212 | +1749.89€ | 0 | 0 |
| ✅ GBM_LATE_60M | 6934 | +0.086 | +2480.43€ | 0 | 8 |
| ✅ GBM_LATE_60M#60min | 6934 | +0.086 | +2480.43€ | 0 | 0 |
| ✅ GBM_LATE_60M#BNB | 239 | +0.276 | +264.63€ | 0 | 0 |
| ✅ GBM_LATE_60M#BNB#60min | 239 | +0.276 | +264.63€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 2113 | +0.062 | +625.98€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 2113 | +0.062 | +625.98€ | 1 | 5 |
| ✅ GBM_LATE_60M#DOGE | 234 | +0.301 | +272.27€ | 0 | 0 |
| ✅ GBM_LATE_60M#DOGE#60min | 234 | +0.301 | +272.27€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH | 1967 | +0.058 | +606.04€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1967 | +0.058 | +606.04€ | 0 | 7 |
| ✅ GBM_LATE_60M#SOL | 2148 | +0.064 | +425.95€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 2148 | +0.064 | +425.95€ | 0 | 10 |
| ✅ GBM_LATE_60M#XRP | 233 | +0.326 | +285.56€ | 0 | 0 |
| ✅ GBM_LATE_60M#XRP#60min | 233 | +0.326 | +285.56€ | 0 | 22 |
| 🚫 GBM_LATE_60M_FADE | 821 | -0.246 | -38.36€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 821 | -0.246 | -38.36€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#BNB | 12 | +0.000 | +4.05€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#BNB#60min | 12 | +0.000 | +4.05€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 287 | -0.258 | -21.84€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 287 | -0.258 | -21.84€ | 5 | 0 |
| ✅ GBM_LATE_60M_FADE#DOGE | 9 | -0.061 | +0.70€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#DOGE#60min | 9 | -0.061 | +0.70€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 281 | -0.246 | -9.46€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 281 | -0.246 | -9.46€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 228 | -0.243 | -10.83€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 228 | -0.243 | -10.83€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 2652 | +0.091 | +709.25€ | 1 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 2652 | +0.091 | +709.25€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 949 | +0.071 | +241.77€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 949 | +0.071 | +241.77€ | 0 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#DOGE | 59 | +0.205 | +35.64€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#DOGE#60min | 59 | +0.205 | +35.64€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 832 | +0.053 | +160.11€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 832 | +0.053 | +160.11€ | 0 | 13 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 693 | +0.153 | +245.72€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 693 | +0.153 | +245.72€ | 1 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#XRP | 119 | +0.095 | +26.02€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#XRP#60min | 119 | +0.095 | +26.02€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN | 441 | +0.304 | +524.47€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 441 | +0.304 | +524.47€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 441 | +0.304 | +524.47€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 441 | +0.304 | +524.47€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 5106 | +0.094 | +1094.10€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 5106 | +0.094 | +1094.10€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 5106 | +0.094 | +1094.10€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 5106 | +0.094 | +1094.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M | 1995 | +0.020 | +112.46€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 1995 | +0.020 | +112.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 260 | +0.092 | +53.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 260 | +0.092 | +53.55€ | 0 | 5 |
| ✅ LIQUIDACIONES_15M#BTC | 370 | -0.013 | +7.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 370 | -0.013 | +7.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 163 | +0.058 | +25.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 163 | +0.058 | +25.06€ | 1 | 1 |
| ✅ LIQUIDACIONES_15M#ETH | 434 | +0.023 | +21.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 434 | +0.023 | +21.83€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 360 | -0.022 | +0.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 360 | -0.022 | +0.09€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 408 | +0.022 | +4.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 408 | +0.022 | +4.87€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4684 | +0.019 | +218.28€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#5min | 4684 | +0.019 | +218.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 241 | +0.002 | -6.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 241 | +0.002 | -6.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 871 | +0.017 | +51.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 871 | +0.017 | +51.56€ | 2 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 366 | +0.073 | +102.88€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 366 | +0.073 | +102.88€ | 0 | 5 |
| ✅ LIQUIDACIONES_5M#ETH | 1761 | +0.024 | +39.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1761 | +0.024 | +39.46€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 823 | +0.013 | +4.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 823 | +0.013 | +4.42€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 622 | -0.005 | +26.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 622 | -0.005 | +26.11€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2918 | -0.037 | -15.36€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2918 | -0.037 | -15.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 881 | -0.041 | -21.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 881 | -0.041 | -21.22€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 1058 | -0.021 | +13.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 1058 | -0.021 | +13.57€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 949 | -0.051 | -7.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 949 | -0.051 | -7.04€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#XRP | 25 | +0.018 | -0.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#XRP#60min | 25 | +0.018 | -0.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 22346 | -0.033 | -235.18€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 10873 | -0.030 | -56.49€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 11473 | -0.035 | -178.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 779 | -0.052 | -37.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 402 | -0.037 | -4.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 377 | -0.067 | -33.44€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 6054 | -0.026 | -26.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 2893 | -0.021 | +22.27€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 3161 | -0.031 | -49.09€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 2015 | -0.036 | -21.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 1038 | -0.038 | -21.75€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 977 | -0.033 | +0.47€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 5146 | -0.030 | -34.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 2495 | -0.025 | +12.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 2651 | -0.035 | -47.07€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 4248 | -0.027 | +20.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 2079 | -0.028 | +8.31€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 2169 | -0.027 | +12.07€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 4104 | -0.046 | -135.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1966 | -0.049 | -73.50€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 2138 | -0.043 | -61.63€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 78301 | -0.001 | +4158.58€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 78301 | -0.001 | +4158.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 14119 | +0.027 | +1963.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 14119 | +0.027 | +1963.05€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 11108 | -0.038 | -152.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 11108 | -0.038 | -152.51€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 14267 | +0.026 | +1578.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 14267 | +0.026 | +1578.46€ | 1 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 11059 | -0.054 | -310.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 11059 | -0.054 | -310.47€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 13237 | -0.004 | +377.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 13237 | -0.004 | +377.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 14511 | +0.020 | +702.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 14511 | +0.020 | +702.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7577 | -0.053 | -112.74€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7577 | -0.053 | -112.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1271 | -0.002 | -14.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1271 | -0.002 | -14.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 2193 | -0.058 | -19.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 2193 | -0.058 | -19.96€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 105 | -0.033 | -1.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 105 | -0.033 | -1.75€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 828 | -0.118 | -35.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 828 | -0.118 | -35.22€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2305 | -0.065 | -11.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2305 | -0.065 | -11.71€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 875 | -0.020 | -29.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 875 | -0.020 | -29.34€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3637 | +0.004 | +1.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3637 | +0.004 | +1.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 133 | -0.033 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 133 | -0.033 | -0.70€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 449 | +0.010 | -1.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 449 | +0.010 | -1.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE | 139 | -0.004 | -2.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 139 | -0.004 | -2.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1327 | +0.006 | +6.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1327 | +0.006 | +6.88€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1392 | +0.006 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1392 | +0.006 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 197 | -0.013 | -0.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 197 | -0.013 | -0.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 191497 | -0.078 | +2108.68€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 191497 | -0.078 | +2108.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 33490 | -0.076 | +1909.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 33490 | -0.076 | +1909.17€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 28991 | -0.102 | -1442.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 28991 | -0.102 | -1442.99€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 33894 | -0.067 | +1650.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 33894 | -0.067 | +1650.49€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 28545 | -0.101 | -1007.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 28545 | -0.101 | -1007.45€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 33802 | -0.060 | +156.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 33802 | -0.060 | +156.49€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 32775 | -0.068 | +842.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 32775 | -0.068 | +842.98€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9421 | -0.035 | -179.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9421 | -0.035 | -179.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1014 | -0.017 | -18.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1014 | -0.017 | -18.55€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2215 | -0.046 | -27.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2215 | -0.046 | -27.84€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1011 | -0.020 | -29.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1011 | -0.020 | -29.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2684 | -0.023 | -30.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2684 | -0.023 | -30.37€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1317 | -0.062 | -29.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1317 | -0.062 | -29.98€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1180 | -0.039 | -43.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1180 | -0.039 | -43.29€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 2439 | +0.120 | +981.63€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 2303 | +0.124 | +969.03€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 529 | +0.140 | +271.86€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 529 | +0.140 | +271.86€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#DOGE | 484 | +0.119 | +175.44€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 484 | +0.119 | +175.44€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#ETH | 417 | +0.130 | +195.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 417 | +0.130 | +195.87€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 394 | +0.134 | +191.50€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 394 | +0.134 | +191.50€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 479 | +0.095 | +134.36€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 479 | +0.095 | +134.36€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 2593 | -0.024 | -59.52€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2593 | -0.024 | -59.52€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 451 | +0.005 | +20.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 451 | +0.005 | +20.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 469 | -0.052 | -35.46€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 469 | -0.052 | -35.46€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 624 | -0.048 | -50.00€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 624 | -0.048 | -50.00€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 536 | -0.013 | -10.45€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 536 | -0.013 | -10.45€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 513 | -0.005 | +16.31€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 513 | -0.005 | +16.31€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1370 | -0.042 | +144.43€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 634 | -0.068 | +29.00€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 496 | -0.064 | +53.87€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 138 | -0.079 | -24.87€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 482 | -0.008 | +76.04€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 350 | +0.009 | +85.64€ | 0 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 132 | -0.052 | -9.61€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 254 | -0.039 | +39.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 216 | -0.037 | +34.97€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 38 | -0.050 | +4.42€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 1062 | -0.035 | +174.48€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 308 | -0.065 | -30.05€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE | 1740 | -0.185 | -32.94€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 689 | -0.173 | -7.66€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 610 | -0.172 | -4.49€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 79 | -0.179 | -3.17€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH | 584 | -0.198 | -32.28€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 515 | -0.204 | -37.39€ | 4 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 69 | -0.148 | +5.11€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 467 | -0.184 | +7.00€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 433 | -0.180 | +3.86€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 34 | -0.222 | +3.14€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#atexpiry | 1558 | -0.185 | -38.02€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 182 | -0.179 | +5.08€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 610 | +0.374 | +535.17€ | 0 | 12 |
| ✅ RESOLUTION_SNIPER#BTC | 141 | +0.178 | +100.38€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 141 | +0.178 | +100.38€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#ETH | 139 | +0.372 | +108.29€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 139 | +0.372 | +108.29€ | 0 | 9 |
| ✅ RESOLUTION_SNIPER#SOL | 330 | +0.455 | +326.49€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 330 | +0.455 | +326.49€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 610 | +0.374 | +535.17€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 1072 | +0.042 | +93.28€ | 2 | 3 |
| ✅ STREAK_FADE_15M#15min | 1072 | +0.042 | +93.28€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 360 | +0.017 | +3.61€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 360 | +0.017 | +3.61€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 83 | +0.029 | +3.15€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 83 | +0.029 | +3.15€ | 1 | 3 |
| ✅ STREAK_FADE_15M#SOL | 86 | +0.034 | +8.76€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 86 | +0.034 | +8.76€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 543 | +0.061 | +77.76€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 543 | +0.061 | +77.76€ | 0 | 3 |
| ✅ STREAK_FADE_5M | 3678 | -0.022 | -140.03€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3678 | -0.022 | -140.03€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1130 | -0.022 | -39.63€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1130 | -0.022 | -39.63€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 634 | -0.027 | -26.29€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 634 | -0.027 | -26.29€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 182 | -0.038 | -14.19€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 182 | -0.038 | -14.19€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1732 | -0.018 | -59.92€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1732 | -0.018 | -59.92€ | 1 | 0 |
| ✅ STREAK_FADE_60M | 160 | +0.012 | -0.18€ | 1 | 2 |
| ✅ STREAK_FADE_60M#60min | 160 | +0.012 | -0.18€ | 0 | 0 |
| ✅ STREAK_FADE_60M#BNB | 8 | +0.120 | +9.18€ | 0 | 0 |
| ✅ STREAK_FADE_60M#BNB#60min | 8 | +0.120 | +9.18€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 51 | -0.028 | -2.40€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 51 | -0.028 | -2.40€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 89 | +0.005 | -5.00€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 89 | +0.005 | -5.00€ | 1 | 1 |
| ✅ STREAK_FADE_60M#XRP | 8 | +0.000 | -1.78€ | 0 | 0 |
| ✅ STREAK_FADE_60M#XRP#60min | 8 | +0.000 | -1.78€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 11758 | +0.013 | +63.08€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11758 | +0.013 | +63.08€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 3013 | +0.017 | +21.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 3013 | +0.017 | +21.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 3153 | +0.012 | +23.85€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 3153 | +0.012 | +23.85€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2970 | +0.009 | -0.97€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2970 | +0.009 | -0.97€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2622 | +0.014 | +18.81€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2622 | +0.014 | +18.81€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 14254 | +0.019 | +9.24€ | 4 | 0 |
| ✅ STRUCT_NO_15M#15min | 14254 | +0.019 | +9.24€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 5717 | +0.022 | +10.94€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 5717 | +0.022 | +10.94€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 5085 | +0.019 | +2.80€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 5085 | +0.019 | +2.80€ | 4 | 0 |
| ✅ STRUCT_NO_15M#SOL | 3452 | +0.014 | -4.50€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 3452 | +0.014 | -4.50€ | 1 | 0 |
| ✅ UPDOWN_GBM | 128548 | +0.060 | +12265.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 32140 | +0.078 | +6284.06€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 3652 | -0.000 | +40.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 84592 | +0.062 | +5811.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 7724 | -0.002 | +132.12€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 11251 | +0.103 | +2080.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 2134 | +0.164 | +998.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 9027 | +0.090 | +1084.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 29169 | +0.056 | +2568.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 4353 | +0.081 | +980.70€ | 0 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 1080 | +0.000 | +21.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 20092 | +0.065 | +1476.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 3486 | -0.003 | +84.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 158 | -0.062 | +4.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 14322 | +0.074 | +1581.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 2084 | +0.155 | +893.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 12152 | +0.061 | +688.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 30221 | +0.049 | +2145.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 7490 | +0.069 | +1162.07€ | 0 | 9 |
| ✅ UPDOWN_GBM#ETH#240min | 1042 | +0.006 | +15.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 18692 | +0.051 | +926.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2850 | -0.002 | +39.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 147 | -0.097 | +2.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 26457 | +0.041 | +1519.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 8658 | +0.033 | +488.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#240min | 957 | -0.011 | +7.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 15370 | +0.053 | +1023.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1339 | +0.003 | +7.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 133 | -0.137 | -7.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 17126 | +0.073 | +2372.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 7421 | +0.089 | +1760.47€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 9259 | +0.064 | +612.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#60min | 49 | +0.010 | +1.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 438 | -0.098 | -1.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 1103 | +0.363 | +420.35€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 1103 | +0.363 | +420.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 527 | +0.364 | +191.23€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 527 | +0.364 | +191.23€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 576 | +0.362 | +229.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 576 | +0.362 | +229.13€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 30482 | -0.016 | +7695.15€ | 2 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 30482 | -0.016 | +7695.15€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 2408 | -0.045 | +644.34€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 2408 | -0.045 | +644.34€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 5631 | -0.114 | +345.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 5631 | -0.114 | +345.35€ | 5 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1294 | +0.218 | +1063.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1294 | +0.218 | +1063.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 4154 | +0.215 | +2603.07€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 4154 | +0.215 | +2603.07€ | 1 | 20 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 8549 | -0.057 | +1301.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 8549 | -0.057 | +1301.77€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 8446 | -0.051 | +1737.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 8446 | -0.051 | +1737.59€ | 4 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 387 | +0.060 | +38.14€ | 0 | 8 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 387 | +0.060 | +38.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 387 | +0.060 | +38.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 387 | +0.060 | +38.14€ | 0 | 8 |
| ✅ UPDOWN_GBM_IBS_ALTO | 2024 | +0.285 | +1743.64€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 2024 | +0.285 | +1743.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 1062 | +0.280 | +862.75€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 1062 | +0.280 | +862.75€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 962 | +0.290 | +880.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 962 | +0.290 | +880.89€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 912 | -0.124 | -98.89€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 912 | -0.124 | -98.89€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 312 | -0.080 | -36.02€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 312 | -0.080 | -36.02€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 293 | -0.090 | -24.57€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 293 | -0.090 | -24.57€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 105 | -0.192 | -14.83€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 105 | -0.192 | -14.83€ | 2 | 0 |
| 🚫 UPDOWN_OU_5M#SOL | 130 | -0.204 | -9.63€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#SOL#5min | 130 | -0.204 | -9.63€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 5520 | +0.291 | +2401.59€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 2159 | +0.247 | +346.57€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 2139 | +0.283 | +875.85€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 1222 | +0.382 | +1179.17€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.028 n=1557 — no justifica filtro, seguir monitorizando
  - _Datos_: n=1557 IC=+0.028 PNL=+79.73€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 858 celda(s) pasan gate riguroso completo de 3094 evaluadas (n>=40) y 4209 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.033 < 0.08 — monitorear
  - _Datos_: n=8656 IC=+0.033 PNL=+488.03€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=2139/15 IC=+0.283 PNL=+875.85€ | BTC: n=2159/15 IC=+0.247 PNL=+346.57€ | SOL: n=1222/15 IC=+0.382 PNL=+1179.17€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.141 n=1199/60 | contraria IC=+0.186 n=1263 | gap=-0.045 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=663, boost estimado=+0.009. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=2849/40 IC=-0.002 PNL=+39.58€ | BTC#60min: n=3484/40 IC=-0.003 PNL=+84.35€ | SOL#60min: n=1339/40 IC=+0.003 PNL=+7.03€ | XRP#60min: n=49/40 IC=+0.010 PNL=+1.35€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.044 n=856337 | tras_1loss IC=+0.103 n=647181 | tras_2loss IC=+0.074 n=256618/40 | gap=-0.030 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.150 > 0.08 con n=1328 PNL=+743.74€
  - _Datos_: n=1328 IC=+0.150 PNL=+743.74€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.126 > 0.08 con n=1547 PNL=+700.78€
  - _Datos_: n=1547 IC=+0.126 PNL=+700.78€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.329 > 0.1 con n=4540 PNL=+2546.70€
  - _Datos_: n=4540 IC=+0.329 PNL=+2546.70€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=1295 IC=+0.063 PNL=+130.82€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1295 IC=+0.063 PNL=+130.82€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=122 IC=+0.153 PNL=+67.70€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=122 IC=+0.153 PNL=+67.70€

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
  - _Estado_: n=5057 IC=-0.008 PNL=-62.27€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=5057 IC=-0.008 PNL=-62.27€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=2664 IC=+0.010 PNL=+194.58€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=2664 IC=+0.010 PNL=+194.58€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=1557 IC=+0.028 PNL=+79.73€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=1557 IC=+0.028 PNL=+79.73€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.131 > 0.1 con n=8929 PNL=+4205.30€
  - _Datos_: n=8929 IC=+0.131 PNL=+4205.30€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=4353 IC=+0.081 PNL=+980.70€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=4353 IC=+0.081 PNL=+980.70€

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
  - _Estado_: n=1763 IC=+0.044 PNL=+148.76€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=1763 IC=+0.044 PNL=+148.76€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=221 IC=-0.025 PNL=-6.32€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=221 IC=-0.025 PNL=-6.32€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.304 n=441) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=441 IC=+0.304 PNL=+524.47€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.116 > 0.02 con n=1426 PNL=+568.98€
  - _Datos_: n=1426 IC=+0.116 PNL=+568.98€

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
  - _Estado_: n=52932 IC=+0.069 PNL=+7089.44€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=52932 IC=+0.069 PNL=+7089.44€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.117 < -0.1 con n=881 PNL=+159.65€
  - _Datos_: n=881 IC=-0.117 PNL=+159.65€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=5163 IC=+0.068 PNL=+615.49€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=5163 IC=+0.068 PNL=+615.49€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=222 IC=-0.085 PNL=+4.07€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=222 IC=-0.085 PNL=+4.07€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.100 > 0.1 con n=1404 PNL=+342.06€
  - _Datos_: n=1404 IC=+0.100 PNL=+342.06€

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
  - _Estado_: n=51124 IC=-0.137 PNL=+3299.77€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=51124 IC=-0.137 PNL=+3299.77€

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
  - _Estado_: n=5553 IC=+0.136 PNL=+3938.13€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=5553 IC=+0.136 PNL=+3938.13€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=13445 IC=+0.057 PNL=+1161.84€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=13445 IC=+0.057 PNL=+1161.84€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.103 > 0.08 con n=5611 PNL=+3189.99€
  - _Datos_: n=5611 IC=+0.103 PNL=+3189.99€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.218 < -0.1 con n=5638 PNL=-420.58€
  - _Datos_: n=5638 IC=-0.218 PNL=-420.58€

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
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.095 n=2617) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=2617 IC=+0.095 PNL=+506.49€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.412 n=699) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=699 IC=+0.412 PNL=+1020.07€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=21668 IC=+0.174 PNL=-2582.30€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=21668 IC=+0.174 PNL=-2582.30€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.233 > 0.1 con n=357 PNL=+251.01€
  - _Datos_: n=357 IC=+0.233 PNL=+251.01€
