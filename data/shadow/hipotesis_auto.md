# Hipótesis automáticas — 2026-11-23 01:03 UTC
_Generado por shadow_postmortem.py sobre 1458756 resoluciones (PNL=+206235.06€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.5` → IC=-0.317 (n=195)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=749)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.196 (n=1103)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.505 (IC base=+0.123)

- **PATRÓN** `n_total_lado` > `61.0` → IC=+0.171 (n=348)

  - _Acción_: Kelly boost +0.86€ cuando `n_total_lado` > 61.0 (IC base=+0.123)

- **PATRÓN** `banda_hit_calibrado` > `0.8118` → IC=+0.270 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8118 (IC base=+0.123)

- **PATRÓN** `banda_z` > `8.273` → IC=+0.195 (n=346)

  - _Acción_: Kelly boost +0.98€ cuando `banda_z` > 8.273 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.130 (n=1047)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 6.0 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=1130)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.123)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.280 (n=171)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=538)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.194 (n=966)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.505 (IC base=+0.125)

- **PATRÓN** `n_total_lado` > `63.0` → IC=+0.180 (n=307)

  - _Acción_: Kelly boost +0.90€ cuando `n_total_lado` > 63.0 (IC base=+0.125)

- **PATRÓN** `banda_hit_calibrado` > `0.8113` → IC=+0.265 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8113 (IC base=+0.125)

- **PATRÓN** `banda_z` > `8.339` → IC=+0.194 (n=302)

  - _Acción_: Kelly boost +0.97€ cuando `banda_z` > 8.339 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.134 (n=919)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 6.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.125 (n=641)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.129 (n=1030)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `8603.4597` → IC=+0.127 (n=242)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 8603.4597 (IC base=+0.015)

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
- **FILTRO** `restante_s_al_confirmar` < `130.37` → IC=-0.221 (n=12811)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.37
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=38438)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `122.97` → IC=-0.263 (n=1272)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 122.97
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3816)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `114.34` → IC=-0.279 (n=1276)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 114.34
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=3829)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `115.59` → IC=-0.164 (n=3545)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 115.59
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=10638)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `147.06` → IC=-0.257 (n=3526)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 147.06
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=10578)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `127.79` → IC=-0.268 (n=2355)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.79
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=7067)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.209 (n=30330)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `10760.7327` → IC=+0.163 (n=1817)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 10760.7327 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.128 (n=26965)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=32409)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.225 (n=24313)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=8804)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `6318.4906` → IC=+0.139 (n=3445)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 6318.4906 (IC base=+0.124)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=2223)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.358 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.175)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.178 (n=2720)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.01 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `16256.7192` → IC=+0.181 (n=707)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 16256.7192 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.186 (n=1943)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 7.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.182 (n=2173)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 17.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.328 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.181 (n=2781)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `16038.5479` → IC=+0.186 (n=718)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 16038.5479 (IC base=+0.178)

### FAVORITO_CONFIRMADO#BTC#60min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.335 (n=95)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=2412)

- **PATRÓN** `py_entrada` > `0.61` → IC=+0.174 (n=669)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` > 0.61 (IC base=+0.075)

- **PATRÓN** `libro_liquidez` > `6825.0558` → IC=+0.130 (n=152)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 6825.0558 (IC base=+0.075)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.153 (n=1572)

  - _Acción_: Kelly boost +0.77€ cuando `py_entrada` < 0.44 (IC base=+0.088)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.172 (n=5556)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 6.0 (IC base=+0.169)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.175 (n=2710)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 8.0 (IC base=+0.169)

- **PATRÓN** `py_entrada` > `0.78` → IC=+0.377 (n=1880)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.78 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.201 (n=2662)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.333 (n=996)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.200 (n=3103)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.195)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.143 (n=717)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 15.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.142 (n=961)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 11.0 (IC base=+0.138)

- **PATRÓN** `py_entrada` > `0.65` → IC=+0.245 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.65 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=1199)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `2050.81` → IC=+0.140 (n=960)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 2050.81 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `4420.281` → IC=+0.152 (n=156)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4420.281 (IC base=+0.076)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.254 (n=996)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.230)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.229 (n=2019)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.230)

- **PATRÓN** `py_entrada` > `0.84` → IC=+0.427 (n=1335)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.84 (IC base=+0.230)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.143 (n=1476)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 7.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.153 (n=754)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.143)

- **PATRÓN** `py_entrada` < `0.315` → IC=+0.295 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.315 (IC base=+0.143)

### FAVORITO_CONFIRMADO#SOL#60min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.306 (n=153)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=484)

- **PATRÓN** `py_entrada` > `0.55` → IC=+0.161 (n=484)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` > 0.55 (IC base=+0.048)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.139 (n=538)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.136 (n=1044)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 12.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.256 (n=494)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.126)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` < `7.0` → IC=-0.259 (n=114)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.254 (n=116)

- **FILTRO** `py_entrada` > `0.755` → IC=-0.299 (n=152)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=78)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.200 (n=25454)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=22619)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.224 (n=8525)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.338 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `8407.3041` → IC=+0.345 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8407.3041 (IC base=+0.193)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.169 (n=6117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 5.0 (IC base=+0.163)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.176 (n=5936)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.74 (IC base=+0.163)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.210 (n=3773)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.206 (n=2507)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.245 (n=1815)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.204)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.183 (n=5653)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 6.0 (IC base=+0.173)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.174 (n=5040)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 15.0 (IC base=+0.173)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.175 (n=6116)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.73 (IC base=+0.173)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.182 (n=4685)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.71 (IC base=+0.173)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.257 (n=4717)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.252)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.252 (n=2286)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.252)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.362 (n=1625)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=5829)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.188 (n=4929)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 15.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.200 (n=1895)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.185)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.428 (n=1025)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.424)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.426 (n=1019)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.424)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.437 (n=1032)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.424)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.429 (n=1103)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.424)

- **PATRÓN** `libro_liquidez` > `14027.0561` → IC=+0.449 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14027.0561 (IC base=+0.424)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.437 (n=424)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.438)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.444 (n=375)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.438)

- **PATRÓN** `libro_liquidez` > `15243.1529` → IC=+0.444 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15243.1529 (IC base=+0.438)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.428 (n=372)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.421)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.423 (n=399)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.421)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.430 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.421)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.426 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.421)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.403 (n=152)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.400)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.406 (n=147)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.400)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.416 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.400)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `14.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=38)

- **FILTRO** `py_entrada` > `0.765` → IC=-0.306 (n=34)

  - _Acción_: SKIP cuando `py_entrada` > 0.765
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=19)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=37)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.211 (n=30236)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.239 (n=34584)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.186 (n=5271)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 18.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.177 (n=11236)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 12.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.186 (n=16174)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.176)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.227 (n=14659)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.276 (n=6241)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.197 (n=5184)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 18.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.199 (n=12405)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.72 (IC base=+0.181)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.855` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.855
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.230 (n=4934)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.221 (n=5635)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.258 (n=6033)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.218)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `py_entrada` < `0.775` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `libro_liquidez` < `3197.0694` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 3197.0694
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.218 (n=4988)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.256 (n=4988)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.206)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.206 (n=5028)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.198 (n=5810)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.246 (n=5898)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=12625)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.140 (n=13787)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.29` → IC=+0.141 (n=11782)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 2.29 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=6144)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.144 (n=6263)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.126 (n=7782)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.77` → IC=+0.142 (n=7720)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 3.77 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=6481)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.136 (n=8322)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.95 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.9` → IC=+0.136 (n=7776)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 2.9 (IC base=+0.116)

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

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.317 (n=714)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.297)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.301 (n=1037)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.297)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.395 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.297)

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
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.440 (n=665)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.438)

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
- **FILTRO** `hora_utc` < `5.0` → IC=-0.269 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=109)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.265 (n=66)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=67)

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
- **PATRÓN** `drift_60min` |x|≤ `0.5051` → IC=+0.140 (n=20125)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.5051 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.129 (n=20408)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 6.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.127 (n=13969)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.9742` → IC=+0.246 (n=6709)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9742 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `0.8809` → IC=+0.292 (n=1120)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8809 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.459` → IC=+0.190 (n=10089)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 3.459 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.6958` → IC=+0.269 (n=5498)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6958 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.3034` → IC=+0.256 (n=2082)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3034 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.7408` → IC=+0.234 (n=4860)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7408 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=9726)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `4891.8148` → IC=+0.152 (n=6708)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4891.8148 (IC base=+0.124)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.123 (n=12702)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0066 (IC base=+0.087)

- **PATRÓN** `ibs_20min` < `0.564` → IC=+0.145 (n=25399)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.564 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.676` → IC=+0.191 (n=1751)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.676 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` < `0.1771` → IC=+0.195 (n=10362)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.1771 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` < `0.8568` → IC=+0.196 (n=7062)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.8568 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2963` → IC=+0.231 (n=2570)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2963 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `1.4565` → IC=+0.210 (n=17945)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4565 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.229 (n=17909)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.087)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.246 (n=1425)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.3032` → IC=+0.215 (n=3757)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3032 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.216 (n=4494)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.213 (n=2852)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.9825` → IC=+0.274 (n=1936)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9825 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.797` → IC=+0.291 (n=1014)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.797 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.2345` → IC=+0.259 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2345 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.4408` → IC=+0.212 (n=4101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4408 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.221 (n=4598)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2046.02` → IC=+0.216 (n=1423)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2046.02 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.220 (n=3502)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.211)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.245 (n=2573)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.0955` → IC=+0.268 (n=1289)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0955 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.240 (n=4021)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.249 (n=1761)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0778` → IC=+0.279 (n=1287)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0778 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` < `0.0726` → IC=+0.242 (n=3330)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0726 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.2889` → IC=+0.250 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2889 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `1.8601` → IC=+0.244 (n=2464)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8601 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.244 (n=2638)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.240)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.233 (n=1220)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.1145` → IC=+0.246 (n=1606)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1145 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=3831)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `0.8912` → IC=+0.257 (n=1216)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8912 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` > `0.7549` → IC=+0.235 (n=651)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7549 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.733` → IC=+0.266 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.733 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` > `0.6973` → IC=+0.229 (n=3259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6973 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.2776` → IC=+0.270 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2776 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.4426` → IC=+0.247 (n=1202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4426 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.152 (n=4009)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0069 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.083` → IC=+0.158 (n=1338)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.083 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.152 (n=1509)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.7083` → IC=+0.172 (n=4009)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.7083 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.1547` → IC=+0.151 (n=3909)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1547 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.954` → IC=+0.142 (n=3689)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 3.954 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `0.6279` → IC=+0.154 (n=1338)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6279 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.0979` → IC=+0.161 (n=1453)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.0979 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `2.4465` → IC=+0.143 (n=3878)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.4465 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=5208)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.187 (n=1272)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 166.0 (IC base=+0.135)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.207 (n=2053)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=4763)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.253 (n=1741)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.879` → IC=+0.278 (n=997)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.879 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` < `0.0969` → IC=+0.194 (n=4059)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0969 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.3496` → IC=+0.222 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3496 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.7296` → IC=+0.208 (n=2004)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7296 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=5508)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `2027.3432` → IC=+0.203 (n=1507)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2027.3432 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.225 (n=1866)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.3058` → IC=+0.230 (n=2825)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3058 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.242 (n=1612)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.228 (n=1920)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` < `0.052` → IC=+0.270 (n=1413)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.052 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.688` → IC=+0.269 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.688 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.3463` → IC=+0.253 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3463 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` < `1.7627` → IC=+0.220 (n=1801)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7627 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.1568` → IC=+0.233 (n=2728)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1568 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.224 (n=2025)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `1893.8504` → IC=+0.223 (n=1921)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1893.8504 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.224 (n=4087)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.222)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=241)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=5460)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.135 (n=970)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0047 (IC base=+0.069)

- **PATRÓN** `ibs_20min` > `0.9435` → IC=+0.251 (n=734)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9435 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` > `0.1604` → IC=+0.352 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1604 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` < `0.5998` → IC=+0.343 (n=952)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5998 (IC base=+0.069)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.197` → IC=+0.216 (n=1616)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.197 (IC base=+0.069)

- **PATRÓN** `volumen_regimen` > `1.1075` → IC=+0.363 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1075 (IC base=+0.069)

- **PATRÓN** `volumen_pendiente_norm` < `0.1669` → IC=+0.348 (n=727)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1669 (IC base=+0.069)

- **PATRÓN** `volumen_pendiente_norm` > `0.3033` → IC=+0.355 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3033 (IC base=+0.069)

- **PATRÓN** `volumen_spike_ratio` < `1.4207` → IC=+0.361 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4207 (IC base=+0.069)

- **PATRÓN** `volumen_spike_ratio` > `2.2831` → IC=+0.355 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2831 (IC base=+0.069)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.351 (n=888)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.069)

- **PATRÓN** `ibs_20min` < `0.0868` → IC=+0.191 (n=1426)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.0868 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` > `0.3644` → IC=+0.158 (n=725)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.3644 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` < `0.1523` → IC=+0.158 (n=2647)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1523 (IC base=+0.059)

- **PATRÓN** `volumen_regimen` < `0.8265` → IC=+0.164 (n=1869)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8265 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.2782` → IC=+0.199 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2782 (IC base=+0.059)

- **PATRÓN** `volumen_spike_ratio` > `2.4323` → IC=+0.173 (n=900)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.4323 (IC base=+0.059)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.181 (n=161)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=884)

- **FILTRO** `ibs_20min` < `0.2727` → IC=-0.177 (n=261)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2727
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=784)

- **FILTRO** `ibs_20min` > `0.1944` → IC=-0.127 (n=5357)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1944
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=2642)

- **FILTRO** `sigma_ewma_delta_pct` > `8.242` → IC=-0.231 (n=867)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.242
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=7132)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.172 (n=358)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.75 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` > `0.9754` → IC=+0.265 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9754 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` < `1.3465` → IC=+0.268 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 1.3465 (IC base=+0.021)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.67` → IC=+0.171 (n=165)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 6.67 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` > `1.0067` → IC=+0.318 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0067 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` < `0.0757` → IC=+0.279 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0757 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` < `2.1915` → IC=+0.282 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1915 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` > `1.4528` → IC=+0.258 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4528 (IC base=+0.021)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.265 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.021)

- **PATRÓN** `ibs_20min` < `0.1944` → IC=+0.159 (n=2642)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.1944 (IC base=-0.033)

- **PATRÓN** `dist_vwap_pct` > `0.235` → IC=+0.295 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.235 (IC base=-0.033)

- **PATRÓN** `dist_vwap_pct` < `0.3206` → IC=+0.293 (n=1287)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3206 (IC base=-0.033)

- **PATRÓN** `volumen_regimen` < `0.6932` → IC=+0.301 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6932 (IC base=-0.033)

- **PATRÓN** `volumen_regimen` > `1.043` → IC=+0.296 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.043 (IC base=-0.033)

- **PATRÓN** `volumen_pendiente_norm` > `0.0787` → IC=+0.319 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0787 (IC base=-0.033)

- **PATRÓN** `volumen_spike_ratio` < `2.4353` → IC=+0.305 (n=1135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4353 (IC base=-0.033)

- **PATRÓN** `volumen_spike_ratio` > `1.4175` → IC=+0.299 (n=1134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4175 (IC base=-0.033)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.8` → IC=-0.158 (n=4138)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8
  - _Potencial_: sin este filtro IC_bueno=+0.145 (n=2132)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.178 (n=1271)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=4999)

- **FILTRO** `ibs_20min` > `0.7228` → IC=-0.190 (n=2159)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7228
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=6478)

- **PATRÓN** `ibs_20min` > `0.8` → IC=+0.145 (n=2132)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.8 (IC base=-0.055)

- **PATRÓN** `dist_vwap_pct` > `0.4517` → IC=+0.346 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4517 (IC base=-0.055)

- **PATRÓN** `volumen_regimen` > `0.7043` → IC=+0.321 (n=1149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7043 (IC base=-0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.3065` → IC=+0.325 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3065 (IC base=-0.055)

- **PATRÓN** `volumen_spike_ratio` > `2.5272` → IC=+0.320 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5272 (IC base=-0.055)

- **PATRÓN** `dist_vwap_pct` > `1.0999` → IC=+0.286 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0999 (IC base=+0.007)

- **PATRÓN** `volumen_regimen` < `0.6385` → IC=+0.275 (n=859)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6385 (IC base=+0.007)

- **PATRÓN** `volumen_regimen` > `1.2109` → IC=+0.279 (n=859)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2109 (IC base=+0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.2384` → IC=+0.279 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2384 (IC base=+0.007)

- **PATRÓN** `volumen_spike_ratio` < `2.4899` → IC=+0.264 (n=2446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4899 (IC base=+0.007)

- **PATRÓN** `volumen_spike_ratio` > `1.443` → IC=+0.270 (n=2446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.443 (IC base=+0.007)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.189 (n=8789)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0112 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.8658` → IC=+0.285 (n=11945)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8658 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.9997` → IC=+0.304 (n=1848)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9997 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.453` → IC=+0.167 (n=11869)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.453 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `0.693` → IC=+0.280 (n=8752)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.693 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2927` → IC=+0.297 (n=2171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2927 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.6444` → IC=+0.289 (n=5097)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6444 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.310 (n=14947)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 88.0 (IC base=+0.087)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.153 (n=11609)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0092 (IC base=+0.088)

- **PATRÓN** `ibs_20min` < `0.5161` → IC=+0.175 (n=22531)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.5161 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` < `0.2035` → IC=+0.284 (n=8677)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2035 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` < `0.8576` → IC=+0.279 (n=5817)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8576 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` > `1.1879` → IC=+0.287 (n=2909)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1879 (IC base=+0.088)

- **PATRÓN** `volumen_pendiente_norm` > `0.295` → IC=+0.323 (n=1931)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.295 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` < `1.4531` → IC=+0.303 (n=4324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4531 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` > `2.2745` → IC=+0.305 (n=5881)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2745 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.313 (n=12963)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 71.0 (IC base=+0.088)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.815` → IC=-0.146 (n=4668)

  - _Acción_: SKIP cuando `ibs_20min` < 0.815
  - _Potencial_: sin este filtro IC_bueno=+0.313 (n=2406)

- **FILTRO** `ibs_20min` > `0.7008` → IC=-0.243 (n=1592)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7008
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=4778)

- **FILTRO** `sigma_ewma_delta_pct` > `4.048` → IC=-0.239 (n=1342)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.048
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=5028)

- **PATRÓN** `ibs_20min` > `0.815` → IC=+0.313 (n=2406)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.815 (IC base=+0.010)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.134` → IC=+0.174 (n=2641)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 2.134 (IC base=+0.010)

- **PATRÓN** `volumen_pendiente_norm` > `0.2301` → IC=+0.334 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2301 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` < `1.4451` → IC=+0.292 (n=742)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4451 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` > `2.2304` → IC=+0.315 (n=1009)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2304 (IC base=+0.010)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.316 (n=1992)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.010)

- **PATRÓN** `ibs_20min` < `0.1707` → IC=+0.172 (n=1594)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.1707 (IC base=-0.015)

- **PATRÓN** `volumen_pendiente_norm` < `0.1562` → IC=+0.389 (n=1409)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1562 (IC base=-0.015)

- **PATRÓN** `volumen_spike_ratio` < `2.6708` → IC=+0.395 (n=1355)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6708 (IC base=-0.015)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1827` → IC=+0.230 (n=1091)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1827 (IC base=+0.010)

- **PATRÓN** `volumen_regimen` > `0.6955` → IC=+0.221 (n=2297)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6955 (IC base=+0.010)

- **PATRÓN** `volumen_pendiente_norm` > `0.2741` → IC=+0.248 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2741 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` < `1.4154` → IC=+0.229 (n=847)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4154 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` > `2.4611` → IC=+0.220 (n=847)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4611 (IC base=+0.010)

- **PATRÓN** `ballena_activa_n` < `368.0` → IC=+0.233 (n=2539)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 368.0 (IC base=+0.010)

- **PATRÓN** `dist_vwap_pct` < `0.574` → IC=+0.257 (n=2292)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.574 (IC base=+0.004)

- **PATRÓN** `volumen_regimen` > `1.018` → IC=+0.268 (n=870)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.018 (IC base=+0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2703` → IC=+0.287 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2703 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` < `1.5317` → IC=+0.255 (n=822)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5317 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` > `2.1503` → IC=+0.262 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1503 (IC base=+0.004)

- **PATRÓN** `ballena_activa_n` < `197.0` → IC=+0.273 (n=830)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 197.0 (IC base=+0.004)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0116` → IC=+0.318 (n=1638)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0116 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.295 (n=3632)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.285)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.323 (n=1959)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.579` → IC=+0.305 (n=2452)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.579 (IC base=+0.285)

- **PATRÓN** `volumen_pendiente_norm` < `0.1306` → IC=+0.293 (n=3364)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1306 (IC base=+0.285)

- **PATRÓN** `volumen_spike_ratio` > `3.2547` → IC=+0.300 (n=1173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.2547 (IC base=+0.285)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.292 (n=4367)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `2024.331` → IC=+0.299 (n=1204)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2024.331 (IC base=+0.285)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.303 (n=2221)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.285)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.338 (n=2239)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.309)

- **PATRÓN** `drift_60min` |x|≤ `0.1877` → IC=+0.329 (n=1479)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1877 (IC base=+0.309)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.326 (n=1291)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.309)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.312 (n=1521)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.309)

- **PATRÓN** `ibs_20min` < `0.3939` → IC=+0.309 (n=3358)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3939 (IC base=+0.309)

- **PATRÓN** `ibs_20min` > `0.1554` → IC=+0.319 (n=2240)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1554 (IC base=+0.309)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.029` → IC=+0.319 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.029 (IC base=+0.309)

- **PATRÓN** `volumen_pendiente_norm` < `0.1991` → IC=+0.310 (n=3335)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1991 (IC base=+0.309)

- **PATRÓN** `volumen_pendiente_norm` > `0.3446` → IC=+0.317 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3446 (IC base=+0.309)

- **PATRÓN** `volumen_spike_ratio` > `2.7444` → IC=+0.326 (n=1475)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7444 (IC base=+0.309)

- **PATRÓN** `libro_liquidez` > `2008.2098` → IC=+0.319 (n=1120)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2008.2098 (IC base=+0.309)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.313 (n=2263)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.309)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **PATRÓN** `dist_vwap_pct` > `0.1595` → IC=+0.240 (n=1203)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1595 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` < `0.6407` → IC=+0.236 (n=2631)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6407 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` < `1.1675` → IC=+0.238 (n=2404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1675 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` > `0.596` → IC=+0.235 (n=2404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.596 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` < `0.163` → IC=+0.238 (n=2524)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.163 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.1031` → IC=+0.243 (n=785)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1031 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `2.4118` → IC=+0.244 (n=2335)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4118 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `113.0` → IC=+0.254 (n=2388)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 113.0 (IC base=+0.026)

- **PATRÓN** `ibs_20min` < `0.0918` → IC=+0.151 (n=1663)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.0918 (IC base=+0.012)

- **PATRÓN** `dist_vwap_pct` < `0.3886` → IC=+0.262 (n=1935)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3886 (IC base=+0.012)

- **PATRÓN** `volumen_regimen` < `1.1802` → IC=+0.263 (n=1756)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1802 (IC base=+0.012)

- **PATRÓN** `volumen_regimen` > `0.6147` → IC=+0.259 (n=1756)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6147 (IC base=+0.012)

- **PATRÓN** `volumen_pendiente_norm` < `0.1015` → IC=+0.266 (n=1649)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1015 (IC base=+0.012)

- **PATRÓN** `volumen_pendiente_norm` > `0.2817` → IC=+0.283 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2817 (IC base=+0.012)

- **PATRÓN** `volumen_spike_ratio` < `1.7831` → IC=+0.283 (n=1130)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7831 (IC base=+0.012)

- **PATRÓN** `volumen_spike_ratio` > `2.4256` → IC=+0.273 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4256 (IC base=+0.012)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.282 (n=1718)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.012)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.75` → IC=-0.248 (n=2707)

  - _Acción_: SKIP cuando `ibs_20min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.315 (n=2718)

- **FILTRO** `ibs_20min` > `0.6061` → IC=-0.238 (n=1275)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6061
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=3828)

- **FILTRO** `sigma_ewma_delta_pct` > `8.218` → IC=-0.263 (n=585)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.218
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=4518)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.315 (n=2718)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.75 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` > `1.1052` → IC=+0.351 (n=395)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1052 (IC base=+0.034)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.441` → IC=+0.158 (n=2214)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 2.441 (IC base=+0.034)

- **PATRÓN** `volumen_regimen` < `0.8456` → IC=+0.349 (n=1326)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8456 (IC base=+0.034)

- **PATRÓN** `volumen_regimen` > `0.6974` → IC=+0.336 (n=1776)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6974 (IC base=+0.034)

- **PATRÓN** `volumen_pendiente_norm` < `0.0993` → IC=+0.339 (n=1874)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0993 (IC base=+0.034)

- **PATRÓN** `volumen_pendiente_norm` > `0.2741` → IC=+0.369 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2741 (IC base=+0.034)

- **PATRÓN** `volumen_spike_ratio` < `1.7864` → IC=+0.354 (n=1290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7864 (IC base=+0.034)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.355 (n=1733)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.034)

- **PATRÓN** `ibs_20min` < `0.6061` → IC=+0.167 (n=3828)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.6061 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` < `0.3246` → IC=+0.276 (n=2056)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3246 (IC base=+0.066)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.728` → IC=+0.133 (n=4000)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 4.728 (IC base=+0.066)

- **PATRÓN** `volumen_regimen` < `0.6895` → IC=+0.285 (n=879)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6895 (IC base=+0.066)

- **PATRÓN** `volumen_pendiente_norm` > `0.0717` → IC=+0.302 (n=800)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0717 (IC base=+0.066)

- **PATRÓN** `volumen_spike_ratio` < `1.8006` → IC=+0.285 (n=1291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8006 (IC base=+0.066)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.293 (n=1970)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 45.0 (IC base=+0.066)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.354 (n=2535)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.314)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.318 (n=2867)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.314)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.316 (n=2975)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.314)

- **PATRÓN** `ibs_20min` > `0.651` → IC=+0.339 (n=2835)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.651 (IC base=+0.314)

- **PATRÓN** `dist_vwap_pct` > `0.2195` → IC=+0.337 (n=1518)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2195 (IC base=+0.314)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.795` → IC=+0.338 (n=1110)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.795 (IC base=+0.314)

- **PATRÓN** `volumen_regimen` > `0.6286` → IC=+0.326 (n=2835)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6286 (IC base=+0.314)

- **PATRÓN** `volumen_pendiente_norm` > `0.2844` → IC=+0.346 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2844 (IC base=+0.314)

- **PATRÓN** `volumen_spike_ratio` > `1.5345` → IC=+0.327 (n=2447)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5345 (IC base=+0.314)

- **PATRÓN** `libro_liquidez` > `3005.1574` → IC=+0.322 (n=945)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3005.1574 (IC base=+0.314)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.331 (n=3057)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.314)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.316 (n=3061)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.314)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.314 (n=3062)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.314)

- **PATRÓN** `ibs_20min` < `0.3895` → IC=+0.329 (n=3057)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3895 (IC base=+0.314)

- **PATRÓN** `dist_vwap_pct` > `1.2929` → IC=+0.322 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2929 (IC base=+0.314)

- **PATRÓN** `dist_vwap_pct` < `0.2563` → IC=+0.317 (n=3016)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2563 (IC base=+0.314)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.129` → IC=+0.325 (n=563)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.129 (IC base=+0.314)

- **PATRÓN** `volumen_regimen` < `0.715` → IC=+0.316 (n=1345)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.715 (IC base=+0.314)

- **PATRÓN** `volumen_regimen` > `1.2096` → IC=+0.340 (n=1019)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2096 (IC base=+0.314)

- **PATRÓN** `volumen_pendiente_norm` > `0.2879` → IC=+0.364 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2879 (IC base=+0.314)

- **PATRÓN** `volumen_spike_ratio` < `1.4149` → IC=+0.324 (n=957)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4149 (IC base=+0.314)

- **PATRÓN** `volumen_spike_ratio` > `2.151` → IC=+0.318 (n=1302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.151 (IC base=+0.314)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.222 (n=6440)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0127 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.1266` → IC=+0.194 (n=8496)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1266 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=20106)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.5366` → IC=+0.229 (n=19305)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5366 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.1703` → IC=+0.207 (n=7305)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1703 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.724` → IC=+0.260 (n=3774)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.724 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `1.1749` → IC=+0.152 (n=12872)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1749 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `0.6211` → IC=+0.152 (n=12871)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6211 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.293` → IC=+0.207 (n=2784)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.293 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.6002` → IC=+0.186 (n=6269)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.6002 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.192 (n=18268)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 85.0 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.194 (n=8470)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0061 (IC base=+0.186)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.187 (n=12821)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0082 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.0849` → IC=+0.222 (n=6407)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0849 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.207 (n=9245)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` < `0.5257` → IC=+0.239 (n=19221)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5257 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` < `0.196` → IC=+0.180 (n=14013)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.196 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.415` → IC=+0.190 (n=3031)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 9.415 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.489` → IC=+0.193 (n=17169)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 2.489 (IC base=+0.186)

- **PATRÓN** `volumen_regimen` < `0.7005` → IC=+0.174 (n=5993)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.7005 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.2954` → IC=+0.220 (n=2889)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2954 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `2.6341` → IC=+0.198 (n=6128)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.6341 (IC base=+0.186)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.200 (n=18190)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 89.0 (IC base=+0.186)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.266 (n=1057)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.230)

- **PATRÓN** `drift_60min` |x|≤ `0.1073` → IC=+0.261 (n=1396)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1073 (IC base=+0.230)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.237 (n=3318)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.230)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.230 (n=2146)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.230)

- **PATRÓN** `ibs_20min` > `0.9416` → IC=+0.293 (n=2114)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9416 (IC base=+0.230)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.453` → IC=+0.328 (n=1042)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.453 (IC base=+0.230)

- **PATRÓN** `volumen_pendiente_norm` > `0.2319` → IC=+0.282 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2319 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` < `1.8322` → IC=+0.227 (n=2024)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8322 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` > `1.4364` → IC=+0.229 (n=3035)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4364 (IC base=+0.230)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=3423)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.230)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.257 (n=2664)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.253)

- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.261 (n=1779)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0078 (IC base=+0.253)

- **PATRÓN** `drift_60min` |x|≤ `0.1001` → IC=+0.306 (n=1171)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1001 (IC base=+0.253)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.258 (n=2744)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.253)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.259 (n=2420)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.253)

- **PATRÓN** `ibs_20min` < `0.0036` → IC=+0.311 (n=888)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0036 (IC base=+0.253)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.934` → IC=+0.258 (n=2630)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.934 (IC base=+0.253)

- **PATRÓN** `volumen_pendiente_norm` < `0.1005` → IC=+0.256 (n=2346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1005 (IC base=+0.253)

- **PATRÓN** `volumen_pendiente_norm` > `0.3008` → IC=+0.267 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3008 (IC base=+0.253)

- **PATRÓN** `volumen_spike_ratio` < `1.5544` → IC=+0.264 (n=1125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5544 (IC base=+0.253)

- **PATRÓN** `volumen_spike_ratio` > `2.6903` → IC=+0.257 (n=853)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6903 (IC base=+0.253)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.261 (n=1833)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.253)

- **PATRÓN** `libro_liquidez` > `1929.5344` → IC=+0.255 (n=1207)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1929.5344 (IC base=+0.253)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.190 (n=991)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0033 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.0674` → IC=+0.175 (n=985)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0674 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=3086)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.2517` → IC=+0.204 (n=2950)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2517 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.197` → IC=+0.211 (n=1449)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.197 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.547` → IC=+0.207 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.547 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.8532` → IC=+0.134 (n=1967)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.8532 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` > `1.0485` → IC=+0.131 (n=1338)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 1.0485 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.174 (n=452)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.5081` → IC=+0.130 (n=1278)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.5081 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `2.4598` → IC=+0.143 (n=968)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.4598 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `387.0` → IC=+0.132 (n=2873)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 387.0 (IC base=+0.127)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.182 (n=2806)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.006 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.2547` → IC=+0.176 (n=2802)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2547 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.180 (n=1521)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` < `0.6113` → IC=+0.212 (n=3183)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6113 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` < `0.1619` → IC=+0.180 (n=3349)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.1619 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.904` → IC=+0.179 (n=587)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 10.904 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.001` → IC=+0.157 (n=2796)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 4.001 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `1.2086` → IC=+0.163 (n=3183)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2086 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` < `0.0719` → IC=+0.155 (n=2660)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.0719 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.1601` → IC=+0.155 (n=968)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.1601 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `2.1397` → IC=+0.159 (n=2689)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1397 (IC base=+0.154)

- **PATRÓN** `ballena_activa_n` < `204.0` → IC=+0.194 (n=1330)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 204.0 (IC base=+0.154)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.231 (n=1481)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.2565` → IC=+0.234 (n=2175)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2565 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.220 (n=3416)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.287 (n=1727)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.987` → IC=+0.304 (n=773)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.987 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` < `0.0987` → IC=+0.210 (n=2849)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0987 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.3485` → IC=+0.229 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3485 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.7115` → IC=+0.223 (n=1447)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7115 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.213 (n=3968)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2019.6184` → IC=+0.224 (n=1088)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2019.6184 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0123` → IC=+0.245 (n=2944)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0123 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.2518` → IC=+0.268 (n=1961)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2518 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.276 (n=1120)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.0426` → IC=+0.296 (n=1295)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0426 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.793` → IC=+0.287 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.793 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.3537` → IC=+0.286 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3537 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `1.6034` → IC=+0.242 (n=951)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6034 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `2.1818` → IC=+0.255 (n=1901)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1818 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `1884.62` → IC=+0.249 (n=1334)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1884.62 (IC base=+0.241)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.240 (n=2833)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.241)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.195 (n=1070)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0039 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.0817` → IC=+0.173 (n=1065)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.0817 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=3308)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.2452` → IC=+0.189 (n=3186)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.2452 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.1492` → IC=+0.189 (n=1811)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1492 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.186` → IC=+0.204 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.186 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.8368` → IC=+0.139 (n=2124)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.8368 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` > `1.1756` → IC=+0.128 (n=1062)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 1.1756 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2872` → IC=+0.178 (n=479)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2872 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.5168` → IC=+0.128 (n=1373)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.5168 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `2.5013` → IC=+0.137 (n=1040)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.5013 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `6924.3049` → IC=+0.196 (n=1444)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 6924.3049 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `123.0` → IC=+0.128 (n=3127)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 123.0 (IC base=+0.127)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.161 (n=2996)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0071 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.4293` → IC=+0.149 (n=3404)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4293 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.165 (n=1635)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.6677` → IC=+0.190 (n=3404)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.6677 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` < `0.1718` → IC=+0.157 (n=3471)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1718 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.521` → IC=+0.141 (n=1164)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 6.521 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.8525` → IC=+0.152 (n=2270)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8525 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.2919` → IC=+0.170 (n=516)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2919 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `2.1879` → IC=+0.135 (n=2854)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.1879 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.4078` → IC=+0.136 (n=3243)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4078 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `6675.8703` → IC=+0.193 (n=1543)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 6675.8703 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.154 (n=1096)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 48.0 (IC base=+0.134)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.013` → IC=+0.175 (n=1186)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.013 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=3657)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.4722` → IC=+0.206 (n=3549)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4722 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.7947` → IC=+0.213 (n=909)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7947 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.957` → IC=+0.284 (n=748)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.957 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `1.1668` → IC=+0.132 (n=3550)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.1668 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.6253` → IC=+0.124 (n=3549)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.6253 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1625` → IC=+0.124 (n=3625)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1625 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2792` → IC=+0.123 (n=494)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` > 0.2792 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.5431` → IC=+0.129 (n=1516)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.5431 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2720.4695` → IC=+0.200 (n=1609)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2720.4695 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.128 (n=2271)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 27.0 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.151 (n=3274)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0112 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.1185` → IC=+0.170 (n=1239)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1185 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.140 (n=3793)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.6429` → IC=+0.223 (n=3717)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6429 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` < `0.227` → IC=+0.147 (n=3683)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.227 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.229` → IC=+0.147 (n=3290)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 2.229 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.1798` → IC=+0.130 (n=3717)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1798 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` > `0.859` → IC=+0.126 (n=2478)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.859 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` < `0.1633` → IC=+0.127 (n=3676)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1633 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2767` → IC=+0.147 (n=520)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2767 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.4387` → IC=+0.141 (n=1178)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4387 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `2.4456` → IC=+0.134 (n=1178)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.4456 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2620.7147` → IC=+0.192 (n=1685)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2620.7147 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.132 (n=3529)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 43.0 (IC base=+0.125)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.246 (n=3187)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.169` → IC=+0.242 (n=1403)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.169 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=3321)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=2876)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.256 (n=3187)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.186` → IC=+0.234 (n=1962)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.186 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` < `0.8292` → IC=+0.228 (n=3283)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8292 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.439` → IC=+0.271 (n=779)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.439 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `0.6174` → IC=+0.236 (n=3188)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6174 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2888` → IC=+0.266 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2888 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `2.1647` → IC=+0.228 (n=2738)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1647 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.8285` → IC=+0.229 (n=2074)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8285 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2625.8761` → IC=+0.232 (n=2125)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2625.8761 (IC base=+0.226)

- **PATRÓN** `sigma_h` > `0.0163` → IC=+0.248 (n=2211)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0163 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.616` → IC=+0.248 (n=3317)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.616 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.249 (n=1633)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.243 (n=1494)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.0385` → IC=+0.299 (n=1462)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0385 (IC base=+0.239)

- **PATRÓN** `dist_vwap_pct` > `1.1734` → IC=+0.248 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1734 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.718` → IC=+0.274 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.718 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` < `0.8667` → IC=+0.242 (n=2212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8667 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` > `1.0478` → IC=+0.244 (n=1504)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0478 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2863` → IC=+0.297 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2863 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.8524` → IC=+0.236 (n=2098)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8524 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `1.5556` → IC=+0.239 (n=2811)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5556 (IC base=+0.239)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.203 (n=1692)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.1437` → IC=+0.171 (n=2228)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1437 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.166 (n=5291)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.6587` → IC=+0.222 (n=3374)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6587 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.91` → IC=+0.179 (n=786)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.91 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.501` → IC=+0.210 (n=816)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.501 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `0.8565` → IC=+0.164 (n=3070)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8565 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` > `1.1893` → IC=+0.157 (n=1535)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 1.1893 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.1558` → IC=+0.170 (n=1309)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.1558 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.5265` → IC=+0.160 (n=2173)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.5265 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.156 (n=5573)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.02 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `7163.8599` → IC=+0.195 (n=2294)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 7163.8599 (IC base=+0.154)

- **PATRÓN** `ibs_20min` < `0.3871` → IC=+0.179 (n=3682)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.3871 (IC base=+0.102)

- **PATRÓN** `volumen_pendiente_norm` > `0.2281` → IC=+0.123 (n=952)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` > 0.2281 (IC base=+0.102)

- **PATRÓN** `ballena_activa_n` < `136.0` → IC=+0.121 (n=5365)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 136.0 (IC base=+0.102)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.207 (n=1207)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0063 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.1055` → IC=+0.234 (n=531)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1055 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.230 (n=1091)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` > `0.6264` → IC=+0.260 (n=805)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6264 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` > `0.3252` → IC=+0.233 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3252 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.927` → IC=+0.226 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.927 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` < `0.6975` → IC=+0.228 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6975 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` < `0.1482` → IC=+0.199 (n=1270)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.1482 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.0903` → IC=+0.214 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0903 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` < `2.1519` → IC=+0.211 (n=1043)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1519 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` > `1.4016` → IC=+0.199 (n=1185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4016 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `13762.5784` → IC=+0.206 (n=805)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13762.5784 (IC base=+0.198)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.148 (n=668)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0036 (IC base=+0.067)

- **PATRÓN** `ibs_20min` < `0.2207` → IC=+0.188 (n=665)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.2207 (IC base=+0.067)

- **PATRÓN** `ballena_activa_n` < `171.0` → IC=+0.164 (n=652)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 171.0 (IC base=+0.067)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.237 (n=520)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.1323` → IC=+0.157 (n=685)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1323 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=1619)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `0.7657` → IC=+0.257 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7657 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.157` → IC=+0.164 (n=746)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.157 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.952` → IC=+0.183 (n=219)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 9.952 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `0.8308` → IC=+0.155 (n=1037)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8308 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.2178` → IC=+0.184 (n=273)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2178 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `2.4693` → IC=+0.167 (n=511)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.4693 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `7873.3573` → IC=+0.179 (n=705)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 7873.3573 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.150 (n=515)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 30.0 (IC base=+0.144)

- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.122 (n=1547)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0081 (IC base=+0.111)

- **PATRÓN** `ibs_20min` < `0.4066` → IC=+0.182 (n=1032)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.4066 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `0.6743` → IC=+0.146 (n=681)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.6743 (IC base=+0.111)

- **PATRÓN** `volumen_pendiente_norm` > `0.223` → IC=+0.134 (n=266)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.223 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `5536.0285` → IC=+0.149 (n=1031)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 5536.0285 (IC base=+0.111)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.150 (n=664)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 40.0 (IC base=+0.111)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.152 (n=464)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0071 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.137 (n=1390)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 6.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.5312` → IC=+0.183 (n=1240)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.5312 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `1.0436` → IC=+0.151 (n=247)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 1.0436 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.867` → IC=+0.228 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.867 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `1.0452` → IC=+0.126 (n=1221)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.0452 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.2221` → IC=+0.139 (n=236)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.2221 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `1.4182` → IC=+0.147 (n=449)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.4182 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `3060.0718` → IC=+0.154 (n=463)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 3060.0718 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.5526` → IC=+0.170 (n=1344)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.5526 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `2773.9701` → IC=+0.164 (n=692)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2773.9701 (IC base=+0.092)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.122 (n=1312)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 27.0 (IC base=+0.092)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0151` → IC=+0.239 (n=304)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0151 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.220 (n=212)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` < `0.8476` → IC=+0.181 (n=402)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.8476 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `0.5119` → IC=+0.198 (n=408)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.5119 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.9129` → IC=+0.199 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9129 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.495` → IC=+0.192 (n=459)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 5.495 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` > `1.2017` → IC=+0.253 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2017 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` < `0.2469` → IC=+0.196 (n=488)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.2469 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.0806` → IC=+0.204 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0806 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` < `2.4312` → IC=+0.195 (n=427)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.4312 (IC base=+0.179)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.191 (n=480)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.03 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `2722.5042` → IC=+0.203 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2722.5042 (IC base=+0.179)

- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.174 (n=504)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0105 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.3414` → IC=+0.169 (n=336)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.3414 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.206 (n=250)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` < `0.3471` → IC=+0.169 (n=336)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.3471 (IC base=+0.159)

- **PATRÓN** `ibs_20min` > `0.0991` → IC=+0.165 (n=503)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.0991 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` > `1.1805` → IC=+0.278 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1805 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.009` → IC=+0.161 (n=485)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 3.009 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` < `0.8883` → IC=+0.192 (n=336)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.8883 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` > `0.2375` → IC=+0.203 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2375 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` < `1.4941` → IC=+0.195 (n=162)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4941 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` > `2.6474` → IC=+0.177 (n=162)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.6474 (IC base=+0.159)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.176 (n=485)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 20.0 (IC base=+0.159)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0128` → IC=+0.228 (n=8500)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0128 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.192 (n=26650)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `0.9667` → IC=+0.302 (n=8501)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9667 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` > `0.9487` → IC=+0.217 (n=2988)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9487 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.884` → IC=+0.261 (n=6228)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.884 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `1.2131` → IC=+0.161 (n=17178)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2131 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2407` → IC=+0.215 (n=4549)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2407 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.6265` → IC=+0.194 (n=8301)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6265 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.201 (n=24112)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.182)

- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.208 (n=7897)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.1537` → IC=+0.202 (n=10418)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1537 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.217 (n=8890)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.4877` → IC=+0.253 (n=20829)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4877 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` < `0.1911` → IC=+0.182 (n=15077)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.1911 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.503` → IC=+0.205 (n=22066)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.503 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `0.6278` → IC=+0.180 (n=5289)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.6278 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.2937` → IC=+0.256 (n=3259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2937 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `2.6258` → IC=+0.212 (n=7593)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6258 (IC base=+0.199)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.215 (n=22555)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.199)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.278 (n=1359)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.3781` → IC=+0.237 (n=4064)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3781 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.241 (n=4276)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.235 (n=2727)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` > `0.8623` → IC=+0.294 (n=2709)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8623 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.026` → IC=+0.302 (n=2666)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.026 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.2328` → IC=+0.288 (n=720)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2328 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.2863` → IC=+0.241 (n=1784)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2863 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.247 (n=4361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `2045.93` → IC=+0.241 (n=1355)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2045.93 (IC base=+0.235)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.246 (n=3356)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.235)

- **PATRÓN** `sigma_h` < `0.0107` → IC=+0.268 (n=3709)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0107 (IC base=+0.265)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.266 (n=2478)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.265)

- **PATRÓN** `drift_60min` |x|≤ `0.1277` → IC=+0.292 (n=1635)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1277 (IC base=+0.265)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.266 (n=3859)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.265)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.269 (n=3337)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.265)

- **PATRÓN** `ibs_20min` < `0.4687` → IC=+0.287 (n=3264)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4687 (IC base=+0.265)

- **PATRÓN** `volumen_pendiente_norm` < `0.0989` → IC=+0.268 (n=3380)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0989 (IC base=+0.265)

- **PATRÓN** `volumen_pendiente_norm` > `0.2925` → IC=+0.286 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2925 (IC base=+0.265)

- **PATRÓN** `volumen_spike_ratio` < `1.5688` → IC=+0.266 (n=1573)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5688 (IC base=+0.265)

- **PATRÓN** `volumen_spike_ratio` > `2.6455` → IC=+0.273 (n=1192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6455 (IC base=+0.265)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.271 (n=2533)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.265)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.272 (n=1323)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.265)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.173 (n=1406)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0033 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.0831` → IC=+0.145 (n=1398)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.0831 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.152 (n=4376)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.3005` → IC=+0.203 (n=3742)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3005 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.7388` → IC=+0.211 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7388 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.252` → IC=+0.172 (n=866)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 9.252 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.6348` → IC=+0.155 (n=1397)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6348 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `1.067` → IC=+0.143 (n=1899)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.067 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.272` → IC=+0.193 (n=587)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.272 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.1703` → IC=+0.144 (n=3626)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.1703 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.5203` → IC=+0.145 (n=3681)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.5203 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `290.0` → IC=+0.153 (n=2731)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 290.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.171 (n=3268)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.006 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.0836` → IC=+0.172 (n=1239)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.0836 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=1376)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` < `0.6801` → IC=+0.192 (n=3714)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.6801 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.1553` → IC=+0.162 (n=3634)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1553 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.201` → IC=+0.150 (n=3796)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 6.201 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `1.0414` → IC=+0.156 (n=3268)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.0414 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.2215` → IC=+0.198 (n=677)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2215 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.4357` → IC=+0.150 (n=3603)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4357 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `1.7706` → IC=+0.152 (n=2402)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.7706 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.147 (n=4823)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `212.0` → IC=+0.179 (n=1186)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 212.0 (IC base=+0.146)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.012` → IC=+0.237 (n=1921)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.012 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.236 (n=4452)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.300 (n=1570)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.941` → IC=+0.314 (n=941)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.941 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.205` → IC=+0.232 (n=1126)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.205 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.7615` → IC=+0.240 (n=1881)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7615 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.230 (n=5152)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `2026.8956` → IC=+0.240 (n=1412)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2026.8956 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0082` → IC=+0.249 (n=1804)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0082 (IC base=+0.246)

- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.246 (n=1366)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.246)

- **PATRÓN** `drift_60min` |x|≤ `0.1853` → IC=+0.260 (n=1803)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1853 (IC base=+0.246)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.264 (n=1561)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.246)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.250 (n=1863)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.246)

- **PATRÓN** `ibs_20min` < `0.0681` → IC=+0.299 (n=1367)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0681 (IC base=+0.246)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.933` → IC=+0.305 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.933 (IC base=+0.246)

- **PATRÓN** `volumen_pendiente_norm` > `0.3469` → IC=+0.302 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3469 (IC base=+0.246)

- **PATRÓN** `volumen_spike_ratio` > `2.1738` → IC=+0.257 (n=2644)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1738 (IC base=+0.246)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.249 (n=1970)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.246)

- **PATRÓN** `libro_liquidez` > `2006.245` → IC=+0.253 (n=1366)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2006.245 (IC base=+0.246)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.248 (n=3928)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 27.0 (IC base=+0.246)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.190 (n=1473)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0039 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.3544` → IC=+0.148 (n=3877)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3544 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.152 (n=4585)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.8775` → IC=+0.268 (n=1469)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8775 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.1503` → IC=+0.170 (n=2196)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1503 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.181` → IC=+0.172 (n=875)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 9.181 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `0.8567` → IC=+0.155 (n=2938)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8567 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.2783` → IC=+0.202 (n=588)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2783 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `1.5173` → IC=+0.157 (n=1896)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.5173 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `2.1553` → IC=+0.146 (n=1952)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 2.1553 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `5876.4965` → IC=+0.233 (n=1997)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5876.4965 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.143 (n=2866)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 85.0 (IC base=+0.141)

- **PATRÓN** `sigma_h` < `0.0082` → IC=+0.169 (n=3723)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0082 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.4606` → IC=+0.160 (n=3721)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.4606 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=1377)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` < `0.5691` → IC=+0.214 (n=3275)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5691 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` < `0.641` → IC=+0.157 (n=4297)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.641 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.044` → IC=+0.154 (n=743)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 9.044 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.02` → IC=+0.154 (n=3241)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 3.02 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `0.8507` → IC=+0.162 (n=2482)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8507 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.2916` → IC=+0.205 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2916 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `2.1974` → IC=+0.156 (n=3175)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.1974 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `1.524` → IC=+0.159 (n=3222)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.524 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `6742.936` → IC=+0.216 (n=1241)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6742.936 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.172 (n=1240)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 57.0 (IC base=+0.152)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.156 (n=1498)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0132 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.150 (n=3186)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.697` → IC=+0.257 (n=2993)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.697 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `1.0536` → IC=+0.201 (n=750)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0536 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.195` → IC=+0.270 (n=1143)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.195 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `1.2098` → IC=+0.127 (n=4487)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.2098 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` < `0.101` → IC=+0.123 (n=4276)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.101 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.139 (n=560)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `2.4956` → IC=+0.125 (n=4382)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.4956 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2488.3554` → IC=+0.226 (n=2034)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2488.3554 (IC base=+0.121)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.160 (n=3677)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0112 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.1425` → IC=+0.154 (n=1390)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1425 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.149 (n=4295)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.6667` → IC=+0.226 (n=4203)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6667 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.2242` → IC=+0.153 (n=3832)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.2242 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.021` → IC=+0.161 (n=4051)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` < 3.021 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.6369` → IC=+0.154 (n=1390)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6369 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2312` → IC=+0.202 (n=727)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2312 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.4384` → IC=+0.164 (n=1327)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.4384 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.4815` → IC=+0.144 (n=1327)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.4815 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `2659.8486` → IC=+0.222 (n=1390)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2659.8486 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.151 (n=4002)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 48.0 (IC base=+0.138)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.257 (n=4099)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.244 (n=4292)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.241 (n=2737)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` > `0.9873` → IC=+0.307 (n=1368)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9873 (IC base=+0.237)

- **PATRÓN** `dist_vwap_pct` > `0.2024` → IC=+0.251 (n=2087)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2024 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.005` → IC=+0.295 (n=725)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.005 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` < `1.2153` → IC=+0.238 (n=4099)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2153 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` > `0.6415` → IC=+0.244 (n=4099)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6415 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.0792` → IC=+0.255 (n=1628)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0792 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.5125` → IC=+0.260 (n=1338)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5125 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `2644.3693` → IC=+0.242 (n=2732)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2644.3693 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0248` → IC=+0.270 (n=1421)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0248 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.250 (n=4015)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` < `0.1387` → IC=+0.307 (n=1876)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1387 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` > `1.1802` → IC=+0.248 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1802 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` < `0.2306` → IC=+0.249 (n=4106)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2306 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.962` → IC=+0.280 (n=798)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.962 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` < `0.7144` → IC=+0.247 (n=1877)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7144 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` > `1.2196` → IC=+0.265 (n=1422)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2196 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` > `0.2872` → IC=+0.313 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2872 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `1.4346` → IC=+0.249 (n=4047)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4346 (IC base=+0.244)

### GBM_LATE_5M
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.242 (n=2455)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.5367` → IC=+0.232 (n=7350)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5367 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=7395)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.9283` → IC=+0.258 (n=2450)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9283 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` < `0.961` → IC=+0.226 (n=5989)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.961 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.424` → IC=+0.231 (n=2448)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.424 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` < `0.7081` → IC=+0.228 (n=2288)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7081 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `0.8815` → IC=+0.225 (n=3466)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8815 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.1643` → IC=+0.233 (n=2061)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1643 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` < `1.4493` → IC=+0.234 (n=2410)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4493 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.228 (n=5253)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `3756.177` → IC=+0.231 (n=4899)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3756.177 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.230 (n=1755)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.212)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.214 (n=2380)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.5318` → IC=+0.221 (n=5251)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5318 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.225 (n=1774)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.226 (n=2353)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.7292` → IC=+0.218 (n=5253)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7292 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.7156` → IC=+0.221 (n=908)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7156 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` < `0.2565` → IC=+0.205 (n=4616)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2565 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.72` → IC=+0.226 (n=4766)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.72 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `1.25` → IC=+0.211 (n=4764)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.25 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` < `0.0983` → IC=+0.216 (n=4850)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0983 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.5322` → IC=+0.217 (n=2275)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5322 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `1.8167` → IC=+0.219 (n=3447)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8167 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.237 (n=3457)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 50.0 (IC base=+0.212)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.279 (n=836)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.271)

- **PATRÓN** `drift_60min` |x|≤ `0.0857` → IC=+0.302 (n=317)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0857 (IC base=+0.271)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.281 (n=950)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.271)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.271 (n=953)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.271)

- **PATRÓN** `ibs_20min` < `0.4658` → IC=+0.286 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4658 (IC base=+0.271)

- **PATRÓN** `dist_vwap_pct` < `0.5307` → IC=+0.280 (n=1050)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5307 (IC base=+0.271)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.129` → IC=+0.298 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.129 (IC base=+0.271)

- **PATRÓN** `volumen_regimen` < `1.2303` → IC=+0.276 (n=949)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2303 (IC base=+0.271)

- **PATRÓN** `volumen_regimen` > `0.8786` → IC=+0.292 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8786 (IC base=+0.271)

- **PATRÓN** `volumen_pendiente_norm` > `0.2874` → IC=+0.341 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2874 (IC base=+0.271)

- **PATRÓN** `volumen_spike_ratio` < `2.4917` → IC=+0.279 (n=943)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4917 (IC base=+0.271)

- **PATRÓN** `libro_liquidez` > `12915.1097` → IC=+0.282 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12915.1097 (IC base=+0.271)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.263 (n=516)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.3878` → IC=+0.187 (n=1543)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.3878 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=569)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.178 (n=579)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 5.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` < `0.1382` → IC=+0.192 (n=680)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.1382 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.3612` → IC=+0.175 (n=333)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.3612 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` < `0.5564` → IC=+0.173 (n=1850)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.5564 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.315` → IC=+0.194 (n=1516)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 6.315 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `1.0909` → IC=+0.185 (n=1358)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 1.0909 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.1519` → IC=+0.188 (n=472)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.1519 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` < `1.4122` → IC=+0.191 (n=512)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.4122 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `2.1732` → IC=+0.176 (n=696)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.1732 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `14608.6008` → IC=+0.174 (n=700)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 14608.6008 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `699.0` → IC=+0.188 (n=1498)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 699.0 (IC base=+0.172)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `drift_60min` |x|≤ `0.6129` → IC=+0.216 (n=1075)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6129 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.230 (n=982)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` < `0.7107` → IC=+0.215 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7107 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `0.9865` → IC=+0.250 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9865 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.277` → IC=+0.245 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.277 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.2054` → IC=+0.246 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2054 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` < `3.3701` → IC=+0.209 (n=1071)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.3701 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `1.7971` → IC=+0.216 (n=957)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7971 (IC base=+0.208)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.219 (n=727)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.208)

- **PATRÓN** `sigma_h` > `0.0143` → IC=+0.333 (n=46)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0143 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.313 (n=105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.288)

- **PATRÓN** `ibs_20min` < `0.4413` → IC=+0.329 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4413 (IC base=+0.288)

- **PATRÓN** `ibs_20min` > `0.1655` → IC=+0.298 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1655 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.081` → IC=+0.357 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.081 (IC base=+0.288)

- **PATRÓN** `volumen_pendiente_norm` < `0.1194` → IC=+0.327 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1194 (IC base=+0.288)

- **PATRÓN** `volumen_pendiente_norm` > `0.266` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.266 (IC base=+0.288)

- **PATRÓN** `volumen_spike_ratio` < `2.4003` → IC=+0.300 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4003 (IC base=+0.288)

- **PATRÓN** `volumen_spike_ratio` > `1.9136` → IC=+0.304 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9136 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `3287.219` → IC=+0.389 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3287.219 (IC base=+0.288)

- **PATRÓN** `ballena_activa_n` < `4.0` → IC=+0.372 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 4.0 (IC base=+0.288)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0086` → IC=+0.221 (n=2010)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0086 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.4713` → IC=+0.219 (n=2008)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4713 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.225 (n=1795)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` < `0.4724` → IC=+0.226 (n=1339)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4724 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `0.8348` → IC=+0.216 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8348 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` < `0.4243` → IC=+0.223 (n=2000)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4243 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.911` → IC=+0.222 (n=1827)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.911 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` < `0.8665` → IC=+0.216 (n=1339)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8665 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` > `1.2314` → IC=+0.216 (n=671)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2314 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` < `0.0991` → IC=+0.215 (n=1859)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0991 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.1599` → IC=+0.213 (n=574)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1599 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `1.4057` → IC=+0.226 (n=654)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4057 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `1.4954` → IC=+0.215 (n=1751)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4954 (IC base=+0.213)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.244 (n=544)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.5081` → IC=+0.223 (n=1631)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5081 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.216 (n=615)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.223 (n=727)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `0.0842` → IC=+0.215 (n=1631)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0842 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `0.7306` → IC=+0.221 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7306 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.261` → IC=+0.212 (n=1480)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.261 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` < `1.2528` → IC=+0.213 (n=1631)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2528 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` > `0.7194` → IC=+0.211 (n=1457)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7194 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.0731` → IC=+0.227 (n=676)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0731 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` < `2.1647` → IC=+0.209 (n=1404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1647 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `1.7757` → IC=+0.212 (n=1064)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7757 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.210 (n=2145)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.208)

- **PATRÓN** `ballena_activa_n` < `95.0` → IC=+0.213 (n=1622)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 95.0 (IC base=+0.208)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.230 (n=856)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.215)

- **PATRÓN** `sigma_h` > `0.0135` → IC=+0.221 (n=428)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0135 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.245 (n=1147)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` > `0.9855` → IC=+0.297 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9855 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` > `1.1012` → IC=+0.244 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1012 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.958` → IC=+0.265 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.958 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` < `0.6434` → IC=+0.244 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6434 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` > `1.2446` → IC=+0.216 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2446 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` < `0.1056` → IC=+0.218 (n=1174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1056 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.2735` → IC=+0.236 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2735 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `2.4925` → IC=+0.223 (n=1249)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4925 (IC base=+0.215)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.224 (n=1503)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.215)

- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.258 (n=643)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.248)

- **PATRÓN** `drift_60min` |x|≤ `0.6877` → IC=+0.262 (n=964)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6877 (IC base=+0.248)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.270 (n=664)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.248)

- **PATRÓN** `ibs_20min` < `0.7347` → IC=+0.271 (n=964)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7347 (IC base=+0.248)

- **PATRÓN** `dist_vwap_pct` > `0.5875` → IC=+0.250 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5875 (IC base=+0.248)

- **PATRÓN** `dist_vwap_pct` < `0.332` → IC=+0.258 (n=853)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.332 (IC base=+0.248)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.99` → IC=+0.268 (n=911)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.99 (IC base=+0.248)

- **PATRÓN** `volumen_regimen` < `0.7517` → IC=+0.261 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7517 (IC base=+0.248)

- **PATRÓN** `volumen_pendiente_norm` < `0.1037` → IC=+0.259 (n=865)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1037 (IC base=+0.248)

- **PATRÓN** `volumen_spike_ratio` > `1.8438` → IC=+0.265 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8438 (IC base=+0.248)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.248 (n=1197)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.248)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.278 (n=850)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.248)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.146 (n=900)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0042 (IC base=+0.066)

- **PATRÓN** `ibs_20min` > `0.5484` → IC=+0.150 (n=2327)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` > 0.5484 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` > `0.1583` → IC=+0.151 (n=1243)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.1583 (IC base=+0.066)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.416` → IC=+0.143 (n=564)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 10.416 (IC base=+0.066)

- **PATRÓN** `ibs_20min` < `0.5918` → IC=+0.168 (n=1997)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.5918 (IC base=+0.085)

- **PATRÓN** `volumen_pendiente_norm` > `0.1502` → IC=+0.174 (n=554)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1502 (IC base=+0.085)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.5456` → IC=-0.121 (n=336)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5456
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=683)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.177 (n=267)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0029 (IC base=+0.068)

- **PATRÓN** `ibs_20min` > `0.5456` → IC=+0.161 (n=683)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.5456 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.129` → IC=+0.165 (n=362)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.129 (IC base=+0.068)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.124 (n=320)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0037 (IC base=+0.052)

- **PATRÓN** `ibs_20min` < `0.0674` → IC=+0.250 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0674 (IC base=+0.052)

- **PATRÓN** `volumen_pendiente_norm` > `0.0703` → IC=+0.138 (n=305)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.0703 (IC base=+0.052)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.5122` → IC=-0.126 (n=257)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5122
  - _Potencial_: sin este filtro IC_bueno=+0.145 (n=503)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.155 (n=363)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0043 (IC base=+0.066)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.120 (n=417)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 15.0 (IC base=+0.066)

- **PATRÓN** `ibs_20min` > `0.5205` → IC=+0.161 (n=709)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.5205 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` > `0.1356` → IC=+0.155 (n=384)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1356 (IC base=+0.066)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.939` → IC=+0.174 (n=173)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 11.939 (IC base=+0.066)

- **PATRÓN** `ibs_20min` < `0.1005` → IC=+0.279 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1005 (IC base=+0.040)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.7241` → IC=+0.146 (n=599)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.7241 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` > `0.7614` → IC=+0.152 (n=219)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.7614 (IC base=+0.034)

- **PATRÓN** `sigma_h` < `0.0102` → IC=+0.172 (n=395)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0102 (IC base=+0.098)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.193 (n=565)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.5 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` < `0.2159` → IC=+0.150 (n=556)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.2159 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.907` → IC=+0.250 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.907 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` > `1.1084` → IC=+0.188 (n=187)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` > 1.1084 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.182 (n=146)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` < `2.193` → IC=+0.129 (n=467)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 2.193 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` > `1.4591` → IC=+0.136 (n=531)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4591 (IC base=+0.098)

### GBM_LATE_60M#XRP#60min
- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.357 (n=47)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.281)

- **PATRÓN** `drift_60min` |x|≤ `0.2821` → IC=+0.326 (n=21)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2821 (IC base=+0.281)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.350 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.281)

- **PATRÓN** `ibs_20min` > `0.6246` → IC=+0.337 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6246 (IC base=+0.281)

- **PATRÓN** `dist_vwap_pct` > `0.2852` → IC=+0.371 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2852 (IC base=+0.281)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.549` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.549 (IC base=+0.281)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.688` → IC=+0.284 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.688 (IC base=+0.281)

- **PATRÓN** `volumen_regimen` < `0.942` → IC=+0.291 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.942 (IC base=+0.281)

- **PATRÓN** `volumen_regimen` > `0.5711` → IC=+0.296 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5711 (IC base=+0.281)

- **PATRÓN** `volumen_pendiente_norm` < `0.0521` → IC=+0.309 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0521 (IC base=+0.281)

- **PATRÓN** `volumen_spike_ratio` < `2.5614` → IC=+0.312 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5614 (IC base=+0.281)

- **PATRÓN** `volumen_spike_ratio` > `2.1108` → IC=+0.318 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1108 (IC base=+0.281)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.281)

- **PATRÓN** `sigma_h` < `0.0135` → IC=+0.365 (n=50)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0135 (IC base=+0.331)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.331 (n=57)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.331)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.387 (n=51)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.331)

- **PATRÓN** `ibs_20min` < `0.0242` → IC=+0.357 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0242 (IC base=+0.331)

- **PATRÓN** `ibs_20min` > `0.4103` → IC=+0.357 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4103 (IC base=+0.331)

- **PATRÓN** `dist_vwap_pct` < `0.499` → IC=+0.364 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.499 (IC base=+0.331)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.545` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.545 (IC base=+0.331)

- **PATRÓN** `volumen_regimen` > `0.5601` → IC=+0.364 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5601 (IC base=+0.331)

- **PATRÓN** `volumen_pendiente_norm` > `0.0735` → IC=+0.423 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0735 (IC base=+0.331)

- **PATRÓN** `volumen_spike_ratio` < `2.0601` → IC=+0.340 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0601 (IC base=+0.331)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.405 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.331)

- **PATRÓN** `libro_liquidez` > `40.0` → IC=+0.405 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 40.0 (IC base=+0.331)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` < `0.0061` → IC=-0.249 (n=205)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0061
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=206)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.310 (n=98)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=313)

- **FILTRO** `volumen_regimen` < `0.872` → IC=-0.303 (n=135)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.872
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=275)

- **FILTRO** `sigma_h` < `0.0075` → IC=-0.279 (n=279)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0075
  - _Potencial_: sin este filtro IC_bueno=-0.216 (n=93)

- **FILTRO** `dist_vwap_pct` > `0.4617` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4617
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=340)

- **FILTRO** `sigma_ewma_delta_pct` > `9.308` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.308
  - _Potencial_: sin este filtro IC_bueno=-0.262 (n=342)

- **FILTRO** `volumen_pendiente_norm` > `0.0463` → IC=-0.375 (n=30)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0463
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=247)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.312 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.232 (n=95)

- **FILTRO** `ibs_20min` < `0.0068` → IC=-0.288 (n=31)

  - _Acción_: SKIP cuando `ibs_20min` < 0.0068
  - _Potencial_: sin este filtro IC_bueno=-0.240 (n=94)

- **FILTRO** `volumen_regimen` > `0.8025` → IC=-0.295 (n=37)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8025
  - _Potencial_: sin este filtro IC_bueno=-0.230 (n=113)

- **FILTRO** `volumen_spike_ratio` > `1.3344` → IC=-0.300 (n=78)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.3344
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=39)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_h` < `0.003` → IC=-0.250 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.003
  - _Potencial_: sin este filtro IC_bueno=-0.148 (n=103)

- **FILTRO** `hora_utc` < `2.0` → IC=-0.179 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 2.0
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=111)

- **FILTRO** `ibs_20min` < `0.6002` → IC=-0.472 (n=34)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6002
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=103)

- **FILTRO** `volumen_regimen` < `0.7594` → IC=-0.250 (n=34)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7594
  - _Potencial_: sin este filtro IC_bueno=-0.148 (n=103)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.372 (n=37)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.275 (n=100)

- **FILTRO** `ibs_20min` > `0.7492` → IC=-0.389 (n=34)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7492
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=103)

- **FILTRO** `volumen_spike_ratio` < `1.4481` → IC=-0.389 (n=25)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.4481
  - _Potencial_: sin este filtro IC_bueno=-0.285 (n=77)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.298 (n=122)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `drift_60min` |x|> `0.2367` → IC=-0.368 (n=36)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2367
  - _Potencial_: sin este filtro IC_bueno=-0.208 (n=111)

- **FILTRO** `volumen_spike_ratio` < `1.57` → IC=-0.312 (n=30)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.57
  - _Potencial_: sin este filtro IC_bueno=-0.234 (n=92)

- **FILTRO** `sigma_h` < `0.0126` → IC=-0.311 (n=51)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0126
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **FILTRO** `sigma_ewma_delta_pct` > `4.378` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.378
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=52)

- **FILTRO** `volumen_regimen` < `0.9188` → IC=-0.458 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9188
  - _Potencial_: sin este filtro IC_bueno=-0.104 (n=46)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.253 (n=383)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.206 (n=386)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `0.6852` → IC=+0.205 (n=843)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6852 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.8606` → IC=+0.326 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8606 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.4` → IC=+0.195 (n=198)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 10.4 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `0.6244` → IC=+0.196 (n=281)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.6244 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` > `1.2031` → IC=+0.167 (n=280)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 1.2031 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` < `0.0675` → IC=+0.195 (n=631)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.0675 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.3986` → IC=+0.213 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3986 (IC base=+0.167)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.171 (n=80)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0066 (IC base=+0.067)

- **PATRÓN** `ibs_20min` > `0.7986` → IC=+0.151 (n=213)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.7986 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` > `0.6723` → IC=+0.240 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6723 (IC base=+0.067)

- **PATRÓN** `ibs_20min` < `0.2563` → IC=+0.131 (n=440)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.2563 (IC base=+0.070)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.181 (n=89)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0072 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.1196` → IC=+0.142 (n=118)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.1196 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.170 (n=98)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 18.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.143 (n=96)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 6.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.8015` → IC=+0.183 (n=238)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.8015 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.8267` → IC=+0.211 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8267 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.1088` → IC=+0.156 (n=216)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1088 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.217` → IC=+0.153 (n=275)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 9.217 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.6229` → IC=+0.192 (n=89)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.6229 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `1.1834` → IC=+0.170 (n=89)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 1.1834 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` < `0.0508` → IC=+0.189 (n=220)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.0508 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.7116` → IC=+0.183 (n=159)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.7116 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=223)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `1847.9955` → IC=+0.175 (n=238)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 1847.9955 (IC base=+0.136)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `volumen_pendiente_norm` < `0.0947` → IC=-0.145 (n=105)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.0947
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=87)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.287 (n=331)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.269)

- **PATRÓN** `ibs_20min` > `0.6852` → IC=+0.301 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6852 (IC base=+0.269)

- **PATRÓN** `dist_vwap_pct` > `0.4789` → IC=+0.391 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4789 (IC base=+0.269)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.922` → IC=+0.354 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.922 (IC base=+0.269)

- **PATRÓN** `volumen_regimen` < `0.7975` → IC=+0.298 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7975 (IC base=+0.269)

- **PATRÓN** `volumen_pendiente_norm` > `0.092` → IC=+0.317 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.092 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` < `1.4854` → IC=+0.332 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4854 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` > `2.3741` → IC=+0.302 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3741 (IC base=+0.269)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.275 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.269)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.320 (n=192)

- **PATRÓN** `drift_ventana_pct` |x|> `0.5446` → IC=+0.346 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.5446 (IC base=+0.337)

- **PATRÓN** `elapsed_s` > `209.2` → IC=+0.402 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 209.2 (IC base=+0.337)

- **PATRÓN** `drift_15min` |x|≤ `1.3457` → IC=+0.370 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.3457 (IC base=+0.337)

- **PATRÓN** `drift_60min` |x|≤ `1.0314` → IC=+0.363 (n=151)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 1.0314 (IC base=+0.337)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.389 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.337)

- **PATRÓN** `ballena_activa_n` < `1044.0` → IC=+0.424 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1044.0 (IC base=+0.337)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3488` → IC=+0.297 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3488 (IC base=+0.282)

- **PATRÓN** `elapsed_s` > `231.9` → IC=+0.373 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 231.9 (IC base=+0.282)

- **PATRÓN** `drift_15min` |x|≤ `2.3354` → IC=+0.314 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3354 (IC base=+0.282)

- **PATRÓN** `drift_60min` |x|≤ `0.9125` → IC=+0.300 (n=138)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9125 (IC base=+0.282)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.320 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.282)

- **PATRÓN** `ballena_activa_n` < `1286.0` → IC=+0.360 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1286.0 (IC base=+0.282)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.320 (n=192)

- **PATRÓN** `drift_ventana_pct` |x|> `0.5446` → IC=+0.346 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.5446 (IC base=+0.337)

- **PATRÓN** `elapsed_s` > `209.2` → IC=+0.402 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 209.2 (IC base=+0.337)

- **PATRÓN** `drift_15min` |x|≤ `1.3457` → IC=+0.370 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.3457 (IC base=+0.337)

- **PATRÓN** `drift_60min` |x|≤ `1.0314` → IC=+0.363 (n=151)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 1.0314 (IC base=+0.337)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.389 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.337)

- **PATRÓN** `ballena_activa_n` < `1044.0` → IC=+0.424 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1044.0 (IC base=+0.337)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3488` → IC=+0.297 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3488 (IC base=+0.282)

- **PATRÓN** `elapsed_s` > `231.9` → IC=+0.373 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 231.9 (IC base=+0.282)

- **PATRÓN** `drift_15min` |x|≤ `2.3354` → IC=+0.314 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3354 (IC base=+0.282)

- **PATRÓN** `drift_60min` |x|≤ `0.9125` → IC=+0.300 (n=138)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9125 (IC base=+0.282)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.320 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.282)

- **PATRÓN** `ballena_activa_n` < `1286.0` → IC=+0.360 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1286.0 (IC base=+0.282)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=288)

- **FILTRO** `py_entrada` < `0.415` → IC=-0.171 (n=71)

  - _Acción_: SKIP cuando `py_entrada` < 0.415
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=233)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=288)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=1453)

### LIQUIDACIONES_15M#BNB#15min
- **PATRÓN** `liq_n` > `2.0` → IC=+0.179 (n=79)

  - _Acción_: Kelly boost +0.90€ cuando `liq_n` > 2.0 (IC base=+0.092)

- **PATRÓN** `liq_usd_total` > `152.22` → IC=+0.133 (n=145)

  - _Acción_: Kelly boost +0.66€ cuando `liq_usd_total` > 152.22 (IC base=+0.092)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.141 (n=76)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` > 0.5 (IC base=+0.092)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.141 (n=101)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.03 (IC base=+0.092)

### LIQUIDACIONES_15M#DOGE#15min
- **FILTRO** `hora_utc` > `8.0` → IC=-0.150 (n=38)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.210 (n=74)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.126 (n=97)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.210 (n=74)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.088)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.126 (n=97)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` > 0.5 (IC base=+0.088)

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
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=281)

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
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=4220)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=239)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=196)

- **FILTRO** `ballena_activa_n` > `68.0` → IC=-0.179 (n=76)

  - _Acción_: SKIP cuando `ballena_activa_n` > 68.0
  - _Potencial_: sin este filtro IC_bueno=+0.165 (n=150)

- **PATRÓN** `ballena_activa_n` < `68.0` → IC=+0.165 (n=150)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 68.0 (IC base=+0.011)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=22)

- **FILTRO** `libro_liquidez` < `13988.6712` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 13988.6712
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.137 (n=293)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.495 (IC base=+0.024)

### LIQUIDACIONES_5M#DOGE#5min
- **PATRÓN** `liq_n` > `3.0` → IC=+0.333 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 3.0 (IC base=+0.190)

- **PATRÓN** `liq_usd_total` > `996.91` → IC=+0.292 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 996.91 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.234 (n=77)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.196 (n=110)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.03 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `3279.111` → IC=+0.206 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3279.111 (IC base=+0.190)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.201 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.190)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=1652)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=1606)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.286 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

- **FILTRO** `ballena_activa_n` > `133.0` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `ballena_activa_n` > 133.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=756)

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
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=1133)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=1133)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=1531)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=1531)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=354)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=354)

- **FILTRO** `py_entrada` < `0.43` → IC=-0.141 (n=115)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=254)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.136 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=408)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=457)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=332)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `libro_liquidez` < `693.7144` → IC=-0.130 (n=152)

  - _Acción_: SKIP cuando `libro_liquidez` < 693.7144
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=310)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=428)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.127 (n=3494)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=9081)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.152 (n=44)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=92)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.139 (n=117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=143)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=88)

- **FILTRO** `restante_min` < `3.99` → IC=-0.125 (n=70)

  - _Acción_: SKIP cuando `restante_min` < 3.99
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=35)

- **FILTRO** `hora_utc` < `17.0` → IC=-0.138 (n=78)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=27)

- **FILTRO** `lag_apertura_s` > `60.89` → IC=-0.125 (n=70)

  - _Acción_: SKIP cuando `lag_apertura_s` > 60.89
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=35)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.160 (n=421)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=1016)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.152 (n=334)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=908)

- **PATRÓN** `py_entrada` < `0.51` → IC=+0.148 (n=436)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` < 0.51 (IC base=-0.007)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.136 (n=196)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=447)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.122 (n=331)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=670)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.122 (n=718)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=763)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.137 (n=356)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=760)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.128 (n=337)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=918)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.121 (n=571)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=607)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.127 (n=623)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=714)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.178 (n=9191)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=28741)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.171 (n=9572)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=29639)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.197 (n=1716)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=5360)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.147 (n=2355)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=4602)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.139 (n=1813)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` > 1.0 (IC base=+0.039)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.136 (n=3271)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.5 (IC base=+0.014)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.184 (n=1196)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=3989)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.176 (n=1351)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=4135)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.197 (n=1738)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=5398)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.134 (n=2170)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 1.0 (IC base=+0.032)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `ibs_20min` < `0.7651` → IC=-0.150 (n=1269)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7651
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=3808)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.179 (n=1378)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=4209)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.162 (n=1745)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=5353)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=2452)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2376)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=973)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=3320)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=4272)

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
- **FILTRO** `py_entrada` > `0.495` → IC=-0.146 (n=80)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=254)

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
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=373)

- **FILTRO** `drift_20min_pct` |x|> `0.1999` → IC=-0.134 (n=121)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1999
  - _Potencial_: sin este filtro IC_bueno=-0.116 (n=365)

- **FILTRO** `libro_liquidez` < `3248.8853` → IC=-0.185 (n=160)

  - _Acción_: SKIP cuando `libro_liquidez` < 3248.8853
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=326)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=983)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.224 (n=310)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=934)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `14.0` → IC=-0.141 (n=76)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=229)

### MOMENTUM_IBS_5M#BNB#5min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=45)

- **PATRÓN** `drift_7min_pct` |x|≤ `0.0331` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_7min_pct` |x|≤ 0.0331 (IC base=-0.026)

### MOMENTUM_IBS_5M#BTC#5min
- **FILTRO** `hora_utc` > `18.0` → IC=-0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 18.0
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=93)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.147 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 15.0 (IC base=+0.023)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.137 (n=25566)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=58315)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.302 (n=20440)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=63441)

- **FILTRO** `ibs_7min` < `0.7273` → IC=-0.225 (n=27575)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7273
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=56306)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.155 (n=28193)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=55688)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.247 (n=25991)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=78919)

- **FILTRO** `ibs_7min` > `0.2781` → IC=-0.183 (n=26226)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2781
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=78684)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.164 (n=3588)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=11547)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.327 (n=3581)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=11554)

- **FILTRO** `ibs_7min` < `0.7089` → IC=-0.256 (n=4993)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7089
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=10142)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.279 (n=4420)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=13752)

- **FILTRO** `ibs_7min` > `0.7692` → IC=-0.211 (n=4539)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7692
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=13633)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.127 (n=3314)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.104 (n=10520)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.267 (n=3385)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=10449)

- **FILTRO** `ibs_7min` < `0.7111` → IC=-0.214 (n=3457)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7111
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=10377)

- **FILTRO** `ballena_activa_n` > `157.0` → IC=-0.204 (n=3447)

  - _Acción_: SKIP cuando `ballena_activa_n` > 157.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=10387)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.267 (n=3225)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=10935)

- **FILTRO** `ibs_7min` > `0.2637` → IC=-0.191 (n=3539)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2637
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=10621)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.178 (n=3535)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=10625)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.169 (n=3450)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=11056)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.329 (n=3464)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=11042)

- **FILTRO** `ibs_7min` < `0.291` → IC=-0.255 (n=4786)

  - _Acción_: SKIP cuando `ibs_7min` < 0.291
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=9720)

- **FILTRO** `ballena_activa_n` > `4.0` → IC=-0.174 (n=3471)

  - _Acción_: SKIP cuando `ballena_activa_n` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=11035)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.261 (n=4598)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=14609)

- **FILTRO** `ibs_7min` > `0.7222` → IC=-0.185 (n=4796)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7222
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=14411)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.276 (n=3071)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=10445)

- **FILTRO** `ibs_7min` < `0.7115` → IC=-0.202 (n=3378)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7115
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=10138)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.200 (n=3280)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=10236)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.259 (n=3267)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=10762)

- **FILTRO** `ibs_7min` > `0.2717` → IC=-0.178 (n=3506)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2717
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=10523)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.173 (n=3381)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=10648)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.304 (n=3253)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=10089)

- **FILTRO** `ibs_7min` < `0.2941` → IC=-0.235 (n=4386)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2941
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=8956)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.202 (n=4815)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=15476)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.315 (n=3316)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=10232)

- **FILTRO** `ibs_7min` < `0.72` → IC=-0.232 (n=4451)

  - _Acción_: SKIP cuando `ibs_7min` < 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=9097)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.196 (n=3370)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=10178)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.231 (n=4633)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=14418)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=121)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.163 (n=304)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=1036)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=1325)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.165 (n=183)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=677)

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
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=927)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.127 (n=234)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=279)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=463)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.216 (n=192)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=593)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.124 (n=107)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=678)

- **FILTRO** `libro_liquidez` < `3306.8101` → IC=-0.146 (n=196)

  - _Acción_: SKIP cuando `libro_liquidez` < 3306.8101
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=589)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=56)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=555)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4305` → IC=+0.143 (n=763)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio` |x|> 0.4305 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.128 (n=1521)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 14.0 (IC base=+0.123)

- **PATRÓN** `total_vol_5m` < `451.687` → IC=+0.166 (n=561)

  - _Acción_: Kelly boost +0.83€ cuando `total_vol_5m` < 451.687 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `4201.4208` → IC=+0.131 (n=561)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 4201.4208 (IC base=+0.123)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.184 (n=194)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 14.0 (IC base=+0.142)

- **PATRÓN** `total_vol_5m` < `287.798` → IC=+0.174 (n=259)

  - _Acción_: Kelly boost +0.87€ cuando `total_vol_5m` < 287.798 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.142 (n=353)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.04 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.156 (n=271)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 9.0 (IC base=+0.142)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3988` → IC=+0.129 (n=351)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.64€ cuando `delta_ratio` |x|> 0.3988 (IC base=+0.113)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.134 (n=329)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 15.0 (IC base=+0.113)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.416` → IC=+0.165 (n=207)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio` |x|> 0.416 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.155 (n=285)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.129)

- **PATRÓN** `total_vol_5m` < `699.4537` → IC=+0.169 (n=273)

  - _Acción_: Kelly boost +0.85€ cuando `total_vol_5m` < 699.4537 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.186 (n=103)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 58.0 (IC base=+0.129)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4317` → IC=+0.218 (n=129)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4317 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.153 (n=194)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 11.0 (IC base=+0.133)

- **PATRÓN** `total_vol_5m` < `4761.643` → IC=+0.181 (n=189)

  - _Acción_: Kelly boost +0.90€ cuando `total_vol_5m` < 4761.643 (IC base=+0.133)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `14.0` → IC=+0.127 (n=320)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 14.0 (IC base=+0.098)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=216)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.098)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `6.3582` → IC=-0.218 (n=83)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 6.3582
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=163)

- **FILTRO** `pct_vs_K` |x|> `3.4135` → IC=-0.152 (n=340)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.4135
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=661)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.158 (n=331)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0047 (IC base=-0.028)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0073` → IC=-0.170 (n=104)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0073
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=202)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.257 (n=101)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.003)

- **PATRÓN** `pct_vs_K` |x|≤ `1.9196` → IC=+0.209 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 1.9196 (IC base=+0.003)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `pct_vs_K` |x|> `6.4329` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 6.4329
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=59)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0154` → IC=-0.194 (n=47)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0154
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=145)

- **FILTRO** `T_h` < `75.099` → IC=-0.177 (n=63)

  - _Acción_: SKIP cuando `T_h` < 75.099
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=129)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `T_h` < `113.9353` → IC=-0.250 (n=566)

  - _Acción_: SKIP cuando `T_h` < 113.9353
  - _Potencial_: sin este filtro IC_bueno=-0.232 (n=293)

- **FILTRO** `sigma_h` < `0.0057` → IC=-0.185 (n=201)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0057
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=606)

- **FILTRO** `pct_vs_K` |x|> `2.9641` → IC=-0.377 (n=201)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9641
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=606)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` > `0.007` → IC=-0.241 (n=141)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=143)

- **FILTRO** `T_h` < `61.9882` → IC=-0.226 (n=93)

  - _Acción_: SKIP cuando `T_h` < 61.9882
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=191)

- **FILTRO** `pct_vs_K` |x|> `2.368` → IC=-0.325 (n=101)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.368
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=201)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `T_h` < `139.5329` → IC=-0.340 (n=23)

  - _Acción_: SKIP cuando `T_h` < 139.5329
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=13)

- **FILTRO** `sigma_h` < `0.0085` → IC=-0.260 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=12)

- **FILTRO** `T_h` > `144.6658` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `T_h` > 144.6658
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.0096` → IC=-0.328 (n=126)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0096
  - _Potencial_: sin este filtro IC_bueno=-0.273 (n=126)

- **FILTRO** `T_h` > `133.1543` → IC=-0.312 (n=62)

  - _Acción_: SKIP cuando `T_h` > 133.1543
  - _Potencial_: sin este filtro IC_bueno=-0.297 (n=190)

- **FILTRO** `sigma_h` > `0.0092` → IC=-0.159 (n=83)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0092
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=162)

- **FILTRO** `sigma_h` < `0.0058` → IC=-0.167 (n=61)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0058
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=184)

- **PATRÓN** `pct_vs_K` |x|≤ `1.9843` → IC=+0.164 (n=123)

  - _Acción_: Kelly boost +0.82€ cuando `pct_vs_K` |x|≤ 1.9843 (IC base=-0.099)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `T_h` < `132.3532` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `T_h` < 132.3532
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=10)

- **FILTRO** `sigma_h` < `0.0098` → IC=-0.237 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0098
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **FILTRO** `T_h` > `109.7804` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `T_h` > 109.7804
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=12)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.01` → IC=-0.237 (n=78)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=159)

- **FILTRO** `T_h` > `61.9454` → IC=-0.221 (n=177)

  - _Acción_: SKIP cuando `T_h` > 61.9454
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=60)

- **FILTRO** `sigma_h` > `0.0139` → IC=-0.309 (n=61)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0139
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=120)

- **FILTRO** `sigma_h` < `0.0095` → IC=-0.266 (n=45)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=136)

- **FILTRO** `T_h` < `70.6336` → IC=-0.141 (n=90)

  - _Acción_: SKIP cuando `T_h` < 70.6336
  - _Potencial_: sin este filtro IC_bueno=-0.124 (n=91)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1171` → IC=+0.447 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1171 (IC base=+0.336)

- **PATRÓN** `sigma_h` < `0.0147` → IC=+0.349 (n=124)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0147 (IC base=+0.336)

- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.347 (n=57)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=+0.336)

- **PATRÓN** `T_h` < `0.3491` → IC=+0.364 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.3491 (IC base=+0.336)

- **PATRÓN** `T_h` > `0.4449` → IC=+0.358 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4449 (IC base=+0.336)

- **PATRÓN** `dist_50` > `0.4594` → IC=+0.483 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4594 (IC base=+0.336)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.355 (n=150)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.336)

- **PATRÓN** `edge` > `0.1` → IC=+0.426 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1 (IC base=+0.392)

- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.419 (n=196)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.392)

- **PATRÓN** `dist_50` > `0.3751` → IC=+0.439 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3751 (IC base=+0.392)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.411 (n=347)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.392)

### RESOLUTION_SNIPER#BTC#sniper
- **PATRÓN** `edge` > `0.1161` → IC=+0.278 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1161 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.265 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.196)

- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.278 (n=25)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.196)

- **PATRÓN** `T_h` < `0.7285` → IC=+0.269 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.7285 (IC base=+0.196)

- **PATRÓN** `T_h` > `1.4804` → IC=+0.235 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4804 (IC base=+0.196)

- **PATRÓN** `dist_50` > `0.3328` → IC=+0.292 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3328 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.231 (n=65)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.235 (n=66)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.196)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1015` → IC=+0.467 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1015 (IC base=+0.414)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.426 (n=66)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.414)

- **PATRÓN** `T_h` < `1.2028` → IC=+0.441 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.2028 (IC base=+0.414)

- **PATRÓN** `dist_50` > `0.4134` → IC=+0.484 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4134 (IC base=+0.414)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.444 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.414)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.1581` → IC=+0.487 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1581 (IC base=+0.441)

- **PATRÓN** `sigma_h` < `0.0155` → IC=+0.470 (n=65)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0155 (IC base=+0.441)

- **PATRÓN** `T_h` > `0.5804` → IC=+0.455 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.5804 (IC base=+0.441)

- **PATRÓN** `dist_50` > `0.3326` → IC=+0.473 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3326 (IC base=+0.441)

- **PATRÓN** `edge` > `0.1937` → IC=+0.472 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1937 (IC base=+0.465)

- **PATRÓN** `sigma_h` < `0.0162` → IC=+0.475 (n=159)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0162 (IC base=+0.465)

- **PATRÓN** `T_h` < `0.8021` → IC=+0.458 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.8021 (IC base=+0.465)

- **PATRÓN** `T_h` > `1.4857` → IC=+0.482 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4857 (IC base=+0.465)

- **PATRÓN** `dist_50` > `0.4557` → IC=+0.493 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4557 (IC base=+0.465)

- **PATRÓN** `hora_utc` < `2.0` → IC=+0.485 (n=63)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 2.0 (IC base=+0.465)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=482)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=522)

- **PATRÓN** `streak_estiramiento` < `0.2938` → IC=+0.145 (n=122)

  - _Acción_: Kelly boost +0.73€ cuando `streak_estiramiento` < 0.2938 (IC base=+0.019)

- **PATRÓN** `streak_estiramiento` < `0.829` → IC=+0.123 (n=361)

  - _Acción_: Kelly boost +0.61€ cuando `streak_estiramiento` < 0.829 (IC base=+0.058)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.144 (n=133)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 14.0 (IC base=+0.058)

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
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=25)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.495 (IC base=+0.048)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `regimen_ma_toques` < `2.0` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `regimen_ma_toques` < 2.0
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=223)

- **PATRÓN** `streak_estiramiento` < `0.4576` → IC=+0.122 (n=162)

  - _Acción_: Kelly boost +0.61€ cuando `streak_estiramiento` < 0.4576 (IC base=+0.036)

- **PATRÓN** `streak_estiramiento` < `0.5965` → IC=+0.156 (n=184)

  - _Acción_: Kelly boost +0.78€ cuando `streak_estiramiento` < 0.5965 (IC base=+0.082)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.136 (n=196)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 35.0 (IC base=+0.082)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.194 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=97)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=57)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.136 (n=31)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=42)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=826)

### STREAK_FADE_60M
- **FILTRO** `py_entrada` < `0.515` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=32)

- **FILTRO** `streak_estiramiento` > `0.6393` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.6393
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=30)

- **PATRÓN** `py_entrada` > `0.515` → IC=+0.147 (n=32)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` > 0.515 (IC base=+0.009)

- **PATRÓN** `streak_estiramiento` < `0.6393` → IC=+0.250 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.6393 (IC base=+0.010)

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
- **PATRÓN** `streak_estiramiento` < `0.6279` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.6279 (IC base=+0.032)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=1102)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1352)

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
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=5506)

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
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=3328)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.185 (n=2163)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0058 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.2325` → IC=+0.158 (n=6487)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2325 (IC base=+0.132)

- **PATRÓN** `drift_15min` |x|≤ `1.1199` → IC=+0.134 (n=6487)

  - _Acción_: Kelly boost +0.67€ cuando `drift_15min` |x|≤ 1.1199 (IC base=+0.132)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0645` → IC=+0.133 (n=6487)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio_macro` |x|> 0.0645 (IC base=+0.132)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1336` → IC=+0.144 (n=2695)

  - _Acción_: Kelly boost +0.72€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1336 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.144 (n=6019)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 6.0 (IC base=+0.132)

- **PATRÓN** `ibs_15` > `0.5556` → IC=+0.208 (n=5796)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5556 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.995` → IC=+0.232 (n=1213)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.995 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=3415)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `4318.6976` → IC=+0.172 (n=2163)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 4318.6976 (IC base=+0.132)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=2482)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.253 (n=293)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.0772` → IC=+0.248 (n=387)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0772 (IC base=+0.207)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2674` → IC=+0.228 (n=292)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2674 (IC base=+0.207)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2251` → IC=+0.221 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2251 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.233 (n=812)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.207)

- **PATRÓN** `ibs_15` > `0.7036` → IC=+0.276 (n=876)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7036 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `0.3946` → IC=+0.235 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3946 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` < `0.5513` → IC=+0.209 (n=984)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5513 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.088` → IC=+0.302 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.088 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.210 (n=1137)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `11835.8417` → IC=+0.225 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11835.8417 (IC base=+0.207)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.148 (n=992)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0067 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.1093` → IC=+0.147 (n=752)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.1093 (IC base=+0.134)

- **PATRÓN** `delta_ratio_macro` |x|> `0.084` → IC=+0.138 (n=1007)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio_macro` |x|> 0.084 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.146 (n=800)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 11.0 (IC base=+0.134)

- **PATRÓN** `ibs_15` > `0.4832` → IC=+0.219 (n=1127)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.4832 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `0.1243` → IC=+0.146 (n=710)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.1243 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` < `0.6708` → IC=+0.134 (n=1276)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.6708 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.949` → IC=+0.286 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.949 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `6122.7931` → IC=+0.174 (n=511)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 6122.7931 (IC base=+0.134)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.8372` → IC=+0.148 (n=668)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.74€ cuando `ibs_15` > 0.8372 (IC base=+0.047)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.143 (n=1647)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` > 0.0119 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.2389` → IC=+0.173 (n=1647)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2389 (IC base=+0.136)

- **PATRÓN** `delta_ratio_macro` |x|> `0.058` → IC=+0.140 (n=1648)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio_macro` |x|> 0.058 (IC base=+0.136)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.093` → IC=+0.189 (n=515)

  - _Acción_: Kelly boost +0.94€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.093 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.143 (n=1510)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 6.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.138 (n=1517)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.136)

- **PATRÓN** `ibs_15` > `0.7` → IC=+0.232 (n=1098)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.2121` → IC=+0.146 (n=750)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.2121 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.9051` → IC=+0.139 (n=1900)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.9051 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.0` → IC=+0.189 (n=380)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 17.0 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `2940.5394` → IC=+0.177 (n=747)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2940.5394 (IC base=+0.136)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `drift_60min` |x|≤ `0.1103` → IC=+0.365 (n=539)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1103 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1455` → IC=+0.376 (n=538)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1455 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1057` → IC=+0.376 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1057 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.373 (n=854)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.7881` → IC=+0.395 (n=808)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7881 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.4233` → IC=+0.383 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4233 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.787` → IC=+0.397 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.787 (IC base=+0.364)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.366 (n=986)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `9610.6074` → IC=+0.378 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9610.6074 (IC base=+0.364)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.366 (n=170)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.363)

- **PATRÓN** `drift_60min` |x|≤ `0.1523` → IC=+0.365 (n=340)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1523 (IC base=+0.363)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2175` → IC=+0.376 (n=175)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2175 (IC base=+0.363)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1441` → IC=+0.397 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1441 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.381 (n=359)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.363)

- **PATRÓN** `ibs_15` > `0.8066` → IC=+0.384 (n=387)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8066 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` > `0.2515` → IC=+0.394 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2515 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.785` → IC=+0.383 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.785 (IC base=+0.363)

- **PATRÓN** `libro_liquidez` > `15150.2605` → IC=+0.388 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15150.2605 (IC base=+0.363)

- **PATRÓN** `ballena_activa_n` < `409.0` → IC=+0.386 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 409.0 (IC base=+0.363)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.363 (n=422)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.363)

- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.376 (n=192)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.363)

- **PATRÓN** `drift_60min` |x|≤ `0.1062` → IC=+0.366 (n=282)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1062 (IC base=+0.363)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1264` → IC=+0.376 (n=281)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1264 (IC base=+0.363)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2951` → IC=+0.371 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2951 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.368 (n=422)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.363)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.374 (n=197)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.363)

- **PATRÓN** `ibs_15` > `0.7632` → IC=+0.399 (n=422)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7632 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` > `0.4608` → IC=+0.378 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4608 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` < `0.6782` → IC=+0.365 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6782 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.857` → IC=+0.399 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.857 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.666` → IC=+0.364 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.666 (IC base=+0.363)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.365 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.363)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `libro_spread` > `0.01` → IC=-0.220 (n=2677)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=3384)

- **FILTRO** `libro_liquidez` < `4381.0798` → IC=-0.172 (n=4000)

  - _Acción_: SKIP cuando `libro_liquidez` < 4381.0798
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=2061)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1411` → IC=+0.216 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1411 (IC base=-0.087)

- **PATRÓN** `ibs_15` > `0.6285` → IC=+0.279 (n=1335)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6285 (IC base=-0.087)

- **PATRÓN** `dist_vwap_pct` > `0.117` → IC=+0.208 (n=794)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.117 (IC base=-0.087)

- **PATRÓN** `dist_vwap_pct` < `0.4335` → IC=+0.198 (n=1319)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.4335 (IC base=-0.087)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2287` → IC=+0.269 (n=1976)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2287 (IC base=+0.001)

- **PATRÓN** `ibs_15` < `0.375` → IC=+0.283 (n=5943)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.375 (IC base=+0.001)

- **PATRÓN** `dist_vwap_pct` > `0.7089` → IC=+0.264 (n=857)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7089 (IC base=+0.001)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0738` → IC=-0.241 (n=1978)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0738
  - _Potencial_: sin este filtro IC_bueno=-0.121 (n=1979)

- **FILTRO** `sigma_h` < `0.004` → IC=-0.209 (n=989)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.004
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=2968)

- **FILTRO** `sigma_ewma_delta_pct` > `22.22` → IC=-0.242 (n=560)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.22
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=3397)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.146 (n=365)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0032 (IC base=+0.066)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2673` → IC=+0.278 (n=160)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2673 (IC base=+0.066)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1441` → IC=+0.284 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1441 (IC base=+0.066)

- **PATRÓN** `ibs_15` > `0.7566` → IC=+0.319 (n=478)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7566 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` > `0.1067` → IC=+0.287 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1067 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` < `0.5501` → IC=+0.284 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5501 (IC base=+0.066)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.729` → IC=+0.145 (n=240)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 21.729 (IC base=+0.066)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0758` → IC=+0.232 (n=80)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0758 (IC base=-0.181)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1335` → IC=+0.306 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1335 (IC base=-0.181)

- **PATRÓN** `ibs_15` < `0.6283` → IC=+0.293 (n=80)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6283 (IC base=-0.181)

- **PATRÓN** `dist_vwap_pct` < `0.0469` → IC=+0.300 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0469 (IC base=-0.181)

- **PATRÓN** `ballena_activa_n` < `393.0` → IC=+0.317 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 393.0 (IC base=-0.181)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=879)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.161 (n=673)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0066 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.159` → IC=+0.161 (n=593)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.159 (IC base=+0.148)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3006` → IC=+0.189 (n=531)

  - _Acción_: Kelly boost +0.94€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3006 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.184 (n=308)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.148)

- **PATRÓN** `ibs_15` > `0.5657` → IC=+0.243 (n=672)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5657 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.6856` → IC=+0.184 (n=131)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.6856 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.827` → IC=+0.256 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.827 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=879)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `5202.7167` → IC=+0.167 (n=448)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 5202.7167 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.256 (n=1012)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.4786` → IC=+0.241 (n=2299)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4786 (IC base=+0.237)

- **PATRÓN** `drift_15min` |x|≤ `0.8178` → IC=+0.250 (n=2023)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.8178 (IC base=+0.237)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2` → IC=+0.257 (n=1043)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.243 (n=854)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.241 (n=1013)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.237)

- **PATRÓN** `ibs_15` < `0.3893` → IC=+0.269 (n=2299)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3893 (IC base=+0.237)

- **PATRÓN** `dist_vwap_pct` > `0.2392` → IC=+0.250 (n=793)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2392 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.549` → IC=+0.245 (n=996)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.549 (IC base=+0.237)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1999` → IC=-0.297 (n=363)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1999
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=1092)

- **FILTRO** `drift_60min` |x|> `0.1729` → IC=-0.282 (n=493)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1729
  - _Potencial_: sin este filtro IC_bueno=-0.165 (n=962)

- **FILTRO** `drift_15min` |x|> `1.0097` → IC=-0.305 (n=363)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.0097
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=1092)

- **FILTRO** `sigma_ewma_delta_pct` > `5.934` → IC=-0.213 (n=319)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.934
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=1136)

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

- **PATRÓN** `ibs_15` < `0.381` → IC=+0.296 (n=990)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.381 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` < `0.199` → IC=+0.256 (n=901)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.199 (IC base=-0.026)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.1226` → IC=-0.245 (n=579)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1226
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=1125)

- **FILTRO** `drift_15min` |x|> `1.3077` → IC=-0.284 (n=425)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.3077
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=1279)

- **FILTRO** `sigma_ewma_delta_pct` > `7.249` → IC=-0.225 (n=515)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.249
  - _Potencial_: sin este filtro IC_bueno=-0.218 (n=1189)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.219 (n=1683)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.220)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.220)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0706` → IC=+0.284 (n=1238)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0706 (IC base=-0.008)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1183` → IC=+0.287 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1183 (IC base=-0.008)

- **PATRÓN** `ibs_15` < `0.3297` → IC=+0.292 (n=1386)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3297 (IC base=-0.008)

- **PATRÓN** `dist_vwap_pct` > `0.786` → IC=+0.325 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.786 (IC base=-0.008)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.146 (n=63)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0068 (IC base=+0.088)

- **PATRÓN** `drift_60min` |x|≤ `0.1106` → IC=+0.159 (n=42)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1106 (IC base=+0.088)

- **PATRÓN** `drift_15min` |x|≤ `0.7315` → IC=+0.146 (n=63)

  - _Acción_: Kelly boost +0.73€ cuando `drift_15min` |x|≤ 0.7315 (IC base=+0.088)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.235` → IC=+0.143 (n=40)

  - _Acción_: Kelly boost +0.71€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.235 (IC base=+0.088)

- **PATRÓN** `ibs_15` > `0.8357` → IC=+0.306 (n=29)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8357 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` < `0.0951` → IC=+0.218 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0951 (IC base=+0.088)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.113` → IC=+0.132 (n=17)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 13.113 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 49.0 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.2049` → IC=+0.134 (n=91)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.2049 (IC base=+0.047)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.146 (n=63)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0068 (IC base=+0.088)

- **PATRÓN** `drift_60min` |x|≤ `0.1106` → IC=+0.159 (n=42)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1106 (IC base=+0.088)

- **PATRÓN** `drift_15min` |x|≤ `0.7315` → IC=+0.146 (n=63)

  - _Acción_: Kelly boost +0.73€ cuando `drift_15min` |x|≤ 0.7315 (IC base=+0.088)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.235` → IC=+0.143 (n=40)

  - _Acción_: Kelly boost +0.71€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.235 (IC base=+0.088)

- **PATRÓN** `ibs_15` > `0.8357` → IC=+0.306 (n=29)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8357 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` < `0.0951` → IC=+0.218 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0951 (IC base=+0.088)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.113` → IC=+0.132 (n=17)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 13.113 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 49.0 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.2049` → IC=+0.134 (n=91)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.2049 (IC base=+0.047)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.302 (n=494)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.285)

- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.294 (n=494)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0066 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.0533` → IC=+0.311 (n=495)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0533 (IC base=+0.285)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0688` → IC=+0.285 (n=1479)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0688 (IC base=+0.285)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.218` → IC=+0.290 (n=909)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.218 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.296 (n=1540)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.285)

- **PATRÓN** `ibs_15` > `0.8368` → IC=+0.312 (n=1480)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8368 (IC base=+0.285)

- **PATRÓN** `dist_vwap_pct` > `0.2757` → IC=+0.317 (n=642)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2757 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.707` → IC=+0.386 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.707 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `13074.8557` → IC=+0.300 (n=494)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13074.8557 (IC base=+0.285)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.308 (n=259)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.279)

- **PATRÓN** `drift_60min` |x|≤ `0.0763` → IC=+0.302 (n=342)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0763 (IC base=+0.279)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2292` → IC=+0.288 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2292 (IC base=+0.279)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.295 (n=818)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.279)

- **PATRÓN** `ibs_15` > `0.9658` → IC=+0.340 (n=354)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9658 (IC base=+0.279)

- **PATRÓN** `dist_vwap_pct` > `0.2607` → IC=+0.311 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2607 (IC base=+0.279)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.43` → IC=+0.391 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.43 (IC base=+0.279)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.281 (n=1006)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `15635.3169` → IC=+0.312 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15635.3169 (IC base=+0.279)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.298 (n=310)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.0504` → IC=+0.323 (n=235)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0504 (IC base=+0.290)

- **PATRÓN** `delta_ratio_macro` |x|> `0.065` → IC=+0.293 (n=704)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.065 (IC base=+0.290)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.101` → IC=+0.311 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.101 (IC base=+0.290)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.300 (n=677)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.290)

- **PATRÓN** `ibs_15` > `0.8447` → IC=+0.316 (n=704)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8447 (IC base=+0.290)

- **PATRÓN** `dist_vwap_pct` > `0.2918` → IC=+0.315 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2918 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.001` → IC=+0.381 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.001 (IC base=+0.290)

### UPDOWN_OU_5M
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1089` → IC=-0.161 (n=234)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1089
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=116)

- **FILTRO** `ballena_activa_n` > `44.0` → IC=-0.145 (n=240)

  - _Acción_: SKIP cuando `ballena_activa_n` > 44.0
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=120)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.167 (n=127)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=381)

- **FILTRO** `ballena_activa_n` > `44.0` → IC=-0.220 (n=80)

  - _Acción_: SKIP cuando `ballena_activa_n` > 44.0
  - _Potencial_: sin este filtro IC_bueno=-0.133 (n=167)

### UPDOWN_OU_5M#BNB#5min
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
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=168)

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
- **FILTRO** `sigma_h` < `0.0081` → IC=-0.188 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0081
  - _Potencial_: sin este filtro IC_bueno=-0.156 (n=30)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.103` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.103
  - _Potencial_: sin este filtro IC_bueno=-0.155 (n=27)

- **FILTRO** `sigma_h` < `0.0062` → IC=-0.227 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0062
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=31)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0764` → IC=-0.210 (n=29)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0764
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### WEEKLY_PRICE
- **PATRÓN** `ratio` < `0.9868` → IC=+0.254 (n=575)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9868 (IC base=+0.124)

- **PATRÓN** `T_h` > `116.1269` → IC=+0.357 (n=3235)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 116.1269 (IC base=+0.337)

- **PATRÓN** `ratio` > `1.0177` → IC=+0.392 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0177 (IC base=+0.337)

### WEEKLY_PRICE#BTC
- **PATRÓN** `ratio` < `0.9758` → IC=+0.188 (n=213)

  - _Acción_: Kelly boost +0.94€ cuando `ratio` < 0.9758 (IC base=+0.066)

- **PATRÓN** `T_h` > `110.5638` → IC=+0.330 (n=1188)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 110.5638 (IC base=+0.309)

- **PATRÓN** `ratio` > `1.0134` → IC=+0.377 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0134 (IC base=+0.309)

### WEEKLY_PRICE#ETH
- **PATRÓN** `ratio` < `0.9793` → IC=+0.364 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9793 (IC base=+0.186)

- **PATRÓN** `T_h` > `111.996` → IC=+0.353 (n=1186)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.996 (IC base=+0.320)

- **PATRÓN** `ratio` > `1.0238` → IC=+0.405 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0238 (IC base=+0.320)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0386` → IC=+0.415 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0386 (IC base=+0.396)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5556 sube el IC de +0.132 a +0.208 en UPDOWN_GBM#15min (n=5796). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7036 sube el IC de +0.207 a +0.276 en UPDOWN_GBM#BTC#15min (n=876). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.4832 sube el IC de +0.134 a +0.219 en UPDOWN_GBM#ETH#15min (n=1127). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.7 sube el IC de +0.136 a +0.232 en UPDOWN_GBM#XRP#15min (n=1098). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6285 sube el IC de -0.087 a +0.279 en UPDOWN_GBM_15M_TARDIO (n=1335). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.375 sube el IC de +0.001 a +0.283 en UPDOWN_GBM_15M_TARDIO (n=5943). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7566 sube el IC de +0.066 a +0.319 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=478). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6283 sube el IC de -0.181 a +0.293 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=80). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5657 sube el IC de +0.148 a +0.243 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=672). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3893 sube el IC de +0.237 a +0.269 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=2299). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.9231 sube el IC de -0.205 a +0.380 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.381 sube el IC de -0.026 a +0.296 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=990). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.220 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3297 sube el IC de -0.008 a +0.292 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=1386). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8357 sube el IC de +0.088 a +0.306 en UPDOWN_GBM_ETH_15M_HORA7 (n=29). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8357 sube el IC de +0.088 a +0.306 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=29). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8368 sube el IC de +0.285 a +0.312 en UPDOWN_GBM_IBS_ALTO (n=1480). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.9658 sube el IC de +0.279 a +0.340 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=354). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8447 sube el IC de +0.290 a +0.316 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=704). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7881 sube el IC de +0.364 a +0.395 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=808). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.363 a +0.384 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=387). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7632 sube el IC de +0.363 a +0.399 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=422). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `GBM_LATE_60M_PYCONFIRMADO#XRP#60min` — IC=+0.083 n=34. Faltan ~6 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `GBM_LATE_60M_PYCONFIRMADO#XRP` — IC=+0.083 n=34. Faltan ~6 resoluciones para umbral n≥40. ETA: ~4h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2328 | +0.084 | +250.66€ | 1 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2328 | +0.084 | +250.66€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1916 | +0.085 | +211.17€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1916 | +0.085 | +211.17€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 285 | +0.068 | +10.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 285 | +0.068 | +10.79€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 96 | +0.122 | +29.03€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 96 | +0.122 | +29.03€ | 0 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 1456 | -0.031 | +57.01€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 1456 | -0.031 | +57.01€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 1132 | -0.044 | +44.37€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 1132 | -0.044 | +44.37€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 224 | +0.035 | +20.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 224 | +0.035 | +20.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 93 | -0.037 | -10.65€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 93 | -0.037 | -10.65€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 51249 | -0.087 | -6597.37€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 3347 | +0.095 | -318.48€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 47902 | -0.100 | -6278.89€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 5088 | -0.116 | -816.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 5088 | -0.116 | -816.49€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 3347 | +0.095 | -318.48€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 3347 | +0.095 | -318.48€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 5105 | -0.108 | -954.74€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 5105 | -0.108 | -954.74€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 14183 | -0.045 | -1341.08€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 14183 | -0.045 | -1341.08€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 14104 | -0.121 | -1623.80€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 14104 | -0.121 | -1623.80€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 9422 | -0.138 | -1542.77€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 9422 | -0.138 | -1542.77€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 56196 | -0.012 | +2674.56€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 14486 | +0.004 | +1472.48€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 41710 | -0.017 | +1202.08€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 56196 | -0.012 | +2674.56€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 14486 | +0.004 | +1472.48€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 41710 | -0.017 | +1202.08€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 209809 | +0.113 | -8467.62€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 23216 | +0.179 | -761.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 978 | +0.019 | -78.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 173711 | +0.105 | -7206.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 11904 | +0.095 | -420.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 28800 | +0.102 | -2028.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 85 | -0.190 | +10.68€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 28684 | +0.103 | -2042.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#60min | 16 | +0.133 | +15.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 39324 | +0.123 | -615.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5697 | +0.177 | -229.52€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 28754 | +0.120 | -188.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4831 | +0.082 | -175.35€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 28841 | +0.099 | -2003.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 97 | -0.116 | +14.79€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 28721 | +0.100 | -2006.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#60min | 8 | -0.080 | -1.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 44897 | +0.124 | -926.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 11189 | +0.178 | -314.80€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 29215 | +0.106 | -525.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 4481 | +0.103 | -77.36€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 39130 | +0.111 | -1681.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 6050 | +0.199 | -257.03€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 881 | +0.044 | -24.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 29634 | +0.096 | -1215.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2565 | +0.106 | -184.50€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO#XRP | 28817 | +0.107 | -1212.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 98 | -0.130 | +14.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 28703 | +0.108 | -1229.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 34143 | +0.190 | -2520.92€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 34143 | +0.190 | -2520.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 7732 | +0.163 | -893.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 7732 | +0.163 | -893.81€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 5118 | +0.194 | -219.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 5118 | +0.194 | -219.86€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 7549 | +0.172 | -692.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 7549 | +0.172 | -692.42€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 6264 | +0.252 | -217.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 6264 | +0.252 | -217.04€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 7401 | +0.184 | -511.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 7401 | +0.184 | -511.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1323 | +0.424 | -51.80€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1323 | +0.424 | -51.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 563 | +0.438 | -6.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 563 | +0.438 | -6.45€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 528 | +0.421 | -23.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 528 | +0.421 | -23.69€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 218 | +0.400 | -17.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 218 | +0.400 | -17.80€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 120714 | +0.200 | -8709.09€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 120714 | +0.200 | -8709.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 20924 | +0.176 | -2444.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 20924 | +0.176 | -2444.88€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 19457 | +0.224 | -636.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 19457 | +0.224 | -636.38€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 20694 | +0.181 | -2142.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 20694 | +0.181 | -2142.60€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 19635 | +0.217 | -770.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 19635 | +0.217 | -770.12€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 19922 | +0.206 | -1163.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 19922 | +0.206 | -1163.69€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 20082 | +0.198 | -1551.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 20082 | +0.198 | -1551.43€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 46931 | +0.116 | +369.68€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 46931 | +0.116 | +369.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 23370 | +0.117 | +242.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 23370 | +0.117 | +242.08€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 23561 | +0.116 | +127.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 23561 | +0.116 | +127.60€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2717 | +0.294 | -7.95€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2717 | +0.294 | -7.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1243 | +0.283 | -25.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1243 | +0.283 | -25.31€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1332 | +0.297 | +10.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1332 | +0.297 | +10.63€ | 0 | 3 |
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
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 2040 | +0.065 | -101.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1315 | +0.075 | -37.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1606 | +0.071 | -56.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1315 | +0.075 | -37.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 95842 | +0.101 | -2006.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 7774 | +0.097 | +184.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 88068 | +0.101 | -2191.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 52317 | +0.105 | -435.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 7774 | +0.097 | +184.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 44543 | +0.107 | -620.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 20588 | +0.110 | -64.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 20588 | +0.110 | -64.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 22937 | +0.083 | -1506.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 22937 | +0.083 | -1506.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 914 | +0.186 | -109.27€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 914 | +0.186 | -109.27€ | 2 | 4 |
| ✅ GBM_LATE_15M | 65304 | +0.102 | +36808.71€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 65304 | +0.102 | +36808.71€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 10835 | +0.225 | +9325.85€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 10835 | +0.225 | +9325.85€ | 0 | 20 |
| ✅ GBM_LATE_15M#BTC | 10208 | +0.177 | +8222.29€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 10208 | +0.177 | +8222.29€ | 0 | 20 |
| ✅ GBM_LATE_15M#DOGE | 11676 | +0.207 | +9243.34€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 11676 | +0.207 | +9243.34€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 8634 | +0.063 | +2928.16€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 8634 | +0.063 | +2928.16€ | 1 | 17 |
| ✅ GBM_LATE_15M#SOL | 9044 | -0.026 | +2331.11€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 9044 | -0.026 | +2331.11€ | 4 | 17 |
| ✅ GBM_LATE_15M#XRP | 14907 | -0.019 | +4757.97€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 14907 | -0.019 | +4757.97€ | 3 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 69262 | +0.088 | +40563.27€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 69262 | +0.088 | +40563.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 13444 | -0.002 | +7045.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 13444 | -0.002 | +7045.75€ | 3 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 14904 | +0.007 | +4135.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 14904 | +0.007 | +4135.29€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 9293 | +0.297 | +10682.45€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 9293 | +0.297 | +10682.45€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 13238 | +0.019 | +4237.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 13238 | +0.019 | +4237.44€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 10528 | +0.049 | +4880.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 10528 | +0.049 | +4880.60€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 7855 | +0.314 | +9581.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 7855 | +0.314 | +9581.74€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 51363 | +0.180 | +42815.70€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 51363 | +0.180 | +42815.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 7775 | +0.240 | +7257.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 7775 | +0.240 | +7257.54€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 8176 | +0.141 | +6161.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 8176 | +0.141 | +6161.04€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 8270 | +0.225 | +7195.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 8270 | +0.225 | +7195.61€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 8785 | +0.131 | +6877.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 8785 | +0.131 | +6877.23€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 9686 | +0.123 | +7487.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 9686 | +0.123 | +7487.32€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 8671 | +0.233 | +7836.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 8671 | +0.233 | +7836.96€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 14108 | +0.127 | +7246.81€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 14108 | +0.127 | +7246.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 678 | +0.162 | +445.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 678 | +0.162 | +445.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3624 | +0.125 | +1965.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3624 | +0.125 | +1965.15€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 509 | +0.156 | +286.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 509 | +0.156 | +286.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 4135 | +0.128 | +2110.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 4135 | +0.128 | +2110.66€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 3884 | +0.104 | +1625.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 3884 | +0.104 | +1625.02€ | 0 | 12 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1278 | +0.169 | +813.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1278 | +0.169 | +813.95€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 65528 | +0.190 | +54689.54€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#15min | 65528 | +0.190 | +54689.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 10363 | +0.250 | +10000.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 10363 | +0.250 | +10000.16€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 10536 | +0.142 | +7633.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 10536 | +0.142 | +7633.29€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 11109 | +0.235 | +10044.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 11109 | +0.235 | +10044.32€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 10834 | +0.146 | +8198.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 10834 | +0.146 | +8198.55€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 11540 | +0.129 | +8449.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 11540 | +0.129 | +8449.29€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 11146 | +0.241 | +10363.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 11146 | +0.241 | +10363.94€ | 0 | 21 |
| ✅ GBM_LATE_5M | 16798 | +0.219 | +14178.95€ | 0 | 26 |
| ✅ GBM_LATE_5M#5min | 16798 | +0.219 | +14178.95€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1947 | +0.253 | +1897.59€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1947 | +0.253 | +1897.59€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3321 | +0.210 | +2854.97€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3321 | +0.210 | +2854.97€ | 0 | 26 |
| ✅ GBM_LATE_5M#DOGE | 1567 | +0.216 | +1287.81€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1567 | +0.216 | +1287.81€ | 0 | 20 |
| ✅ GBM_LATE_5M#ETH | 4851 | +0.210 | +3813.49€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 4851 | +0.210 | +3813.49€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 2993 | +0.229 | +2661.25€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2993 | +0.229 | +2661.25€ | 0 | 24 |
| ✅ GBM_LATE_5M#XRP | 2119 | +0.209 | +1663.83€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 2119 | +0.209 | +1663.83€ | 0 | 0 |
| ✅ GBM_LATE_60M | 6356 | +0.074 | +2042.61€ | 0 | 6 |
| ✅ GBM_LATE_60M#60min | 6356 | +0.074 | +2042.61€ | 0 | 0 |
| ✅ GBM_LATE_60M#BNB | 140 | +0.268 | +147.78€ | 0 | 0 |
| ✅ GBM_LATE_60M#BNB#60min | 140 | +0.268 | +147.78€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 2029 | +0.060 | +594.21€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 2029 | +0.060 | +594.21€ | 1 | 6 |
| ✅ GBM_LATE_60M#DOGE | 137 | +0.306 | +155.19€ | 0 | 0 |
| ✅ GBM_LATE_60M#DOGE#60min | 137 | +0.306 | +155.19€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH | 1887 | +0.055 | +590.32€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1887 | +0.055 | +590.32€ | 1 | 6 |
| ✅ GBM_LATE_60M#SOL | 2026 | +0.059 | +398.51€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 2026 | +0.059 | +398.51€ | 0 | 10 |
| ✅ GBM_LATE_60M#XRP | 137 | +0.313 | +156.61€ | 0 | 0 |
| ✅ GBM_LATE_60M#XRP#60min | 137 | +0.313 | +156.61€ | 0 | 25 |
| 🚫 GBM_LATE_60M_FADE | 783 | -0.246 | -34.30€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 783 | -0.246 | -34.30€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#BNB | 7 | +0.019 | +3.26€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#BNB#60min | 7 | +0.019 | +3.26€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 275 | -0.255 | -19.44€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 275 | -0.255 | -19.44€ | 4 | 0 |
| ✅ GBM_LATE_60M_FADE#DOGE | 7 | -0.058 | -0.03€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#DOGE#60min | 7 | -0.058 | -0.03€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 274 | -0.243 | -7.28€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 274 | -0.243 | -7.28€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 216 | -0.248 | -9.83€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 216 | -0.248 | -9.83€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 2427 | +0.087 | +611.47€ | 0 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 2427 | +0.087 | +611.47€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 903 | +0.069 | +210.77€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 903 | +0.069 | +210.77€ | 0 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#DOGE | 8 | +0.000 | +0.42€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#DOGE#60min | 8 | +0.000 | +0.42€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 822 | +0.056 | +158.95€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 822 | +0.056 | +158.95€ | 0 | 14 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 660 | +0.151 | +238.69€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 660 | +0.151 | +238.69€ | 1 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#XRP | 34 | +0.083 | +2.65€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#XRP#60min | 34 | +0.083 | +2.65€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN | 409 | +0.310 | +494.36€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 409 | +0.310 | +494.36€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 409 | +0.310 | +494.36€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 409 | +0.310 | +494.36€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 4879 | +0.095 | +1066.12€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4879 | +0.095 | +1066.12€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4879 | +0.095 | +1066.12€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4879 | +0.095 | +1066.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M | 1778 | +0.020 | +105.21€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 1778 | +0.020 | +105.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 217 | +0.089 | +43.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 217 | +0.089 | +43.76€ | 0 | 4 |
| ✅ LIQUIDACIONES_15M#BTC | 342 | -0.006 | +9.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 342 | -0.006 | +9.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 122 | +0.048 | +23.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 122 | +0.048 | +23.07€ | 2 | 2 |
| ✅ LIQUIDACIONES_15M#ETH | 403 | +0.026 | +22.13€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 403 | +0.026 | +22.13€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 355 | -0.018 | +1.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 355 | -0.018 | +1.43€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 339 | +0.025 | +5.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 339 | +0.025 | +5.10€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4565 | +0.018 | +198.63€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#5min | 4565 | +0.018 | +198.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 241 | +0.002 | -6.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 241 | +0.002 | -6.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 865 | +0.017 | +51.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 865 | +0.017 | +51.51€ | 2 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 337 | +0.066 | +85.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 337 | +0.066 | +85.91€ | 0 | 6 |
| ✅ LIQUIDACIONES_5M#ETH | 1704 | +0.022 | +36.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1704 | +0.022 | +36.00€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 797 | +0.016 | +6.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 797 | +0.016 | +6.57€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 621 | -0.006 | +24.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 621 | -0.006 | +24.80€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2759 | -0.034 | -7.85€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2759 | -0.034 | -7.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 841 | -0.036 | -15.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 841 | -0.036 | -15.85€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 993 | -0.017 | +16.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 993 | -0.017 | +16.94€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 905 | -0.053 | -9.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 905 | -0.053 | -9.84€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#XRP | 15 | +0.066 | +1.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#XRP#60min | 15 | +0.066 | +1.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 20702 | -0.031 | -172.90€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 10025 | -0.033 | -123.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 10677 | -0.029 | -49.19€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 736 | -0.051 | -38.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 371 | -0.039 | -8.29€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 365 | -0.064 | -30.60€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 5587 | -0.026 | -27.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 2657 | -0.024 | +2.59€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 2930 | -0.028 | -29.96€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1882 | -0.032 | -0.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 963 | -0.042 | -26.81€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 919 | -0.021 | +25.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 4740 | -0.033 | -67.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 2287 | -0.030 | -19.65€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 2453 | -0.035 | -47.35€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 3952 | -0.023 | +49.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1927 | -0.029 | -1.23€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 2025 | -0.018 | +50.96€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 3805 | -0.041 | -88.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1820 | -0.048 | -70.32€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1985 | -0.034 | -18.11€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 77143 | -0.000 | +4167.82€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 77143 | -0.000 | +4167.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 14033 | +0.027 | +1938.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 14033 | +0.027 | +1938.79€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 10671 | -0.038 | -144.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 10671 | -0.038 | -144.10€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 14184 | +0.026 | +1580.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 14184 | +0.026 | +1580.25€ | 1 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 10664 | -0.054 | -280.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 10664 | -0.054 | -280.20€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 13160 | -0.004 | +371.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 13160 | -0.004 | +371.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 14431 | +0.020 | +701.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 14431 | +0.020 | +701.98€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7442 | -0.052 | -108.76€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7442 | -0.052 | -108.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1270 | -0.002 | -14.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1270 | -0.002 | -14.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 2129 | -0.058 | -18.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 2129 | -0.058 | -18.26€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 102 | -0.019 | -0.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 102 | -0.019 | -0.22€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 820 | -0.117 | -33.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 820 | -0.117 | -33.49€ | 7 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2251 | -0.067 | -13.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2251 | -0.067 | -13.56€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 870 | -0.019 | -28.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 870 | -0.019 | -28.97€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3386 | +0.003 | +0.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3386 | +0.003 | +0.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 133 | -0.033 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 133 | -0.033 | -0.70€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 199 | +0.007 | -1.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 199 | +0.007 | -1.73€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 139 | -0.004 | -2.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 139 | -0.004 | -2.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1326 | +0.006 | +6.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1326 | +0.006 | +6.37€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1392 | +0.006 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1392 | +0.006 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 197 | -0.013 | -0.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 197 | -0.013 | -0.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 188791 | -0.078 | +2152.01€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 188791 | -0.078 | +2152.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 33307 | -0.076 | +1906.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 33307 | -0.076 | +1906.09€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 27994 | -0.102 | -1408.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 27994 | -0.102 | -1408.70€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 33713 | -0.067 | +1627.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 33713 | -0.067 | +1627.89€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 27545 | -0.101 | -982.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 27545 | -0.101 | -982.02€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 33633 | -0.059 | +183.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 33633 | -0.059 | +183.19€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 32599 | -0.069 | +825.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 32599 | -0.069 | +825.55€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9365 | -0.035 | -188.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9365 | -0.035 | -188.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1012 | -0.017 | -19.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1012 | -0.017 | -19.26€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2200 | -0.046 | -28.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2200 | -0.046 | -28.18€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2678 | -0.024 | -32.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2678 | -0.024 | -32.94€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1298 | -0.064 | -32.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1298 | -0.064 | -32.37€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1168 | -0.039 | -43.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1168 | -0.039 | -43.52€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 2377 | +0.120 | +949.16€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 2241 | +0.123 | +936.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 517 | +0.142 | +268.34€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 517 | +0.142 | +268.34€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 468 | +0.113 | +157.41€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 468 | +0.113 | +157.41€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 413 | +0.129 | +191.99€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 413 | +0.129 | +191.99€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 377 | +0.133 | +182.20€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 377 | +0.133 | +182.20€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 466 | +0.098 | +136.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 466 | +0.098 | +136.62€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 2518 | -0.022 | -48.10€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2518 | -0.022 | -48.10€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 447 | +0.006 | +20.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 447 | +0.006 | +20.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 459 | -0.047 | -29.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 459 | -0.047 | -29.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 612 | -0.044 | -42.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 612 | -0.044 | -42.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 525 | -0.007 | -3.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 525 | -0.007 | -3.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 475 | -0.014 | +7.11€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 475 | -0.014 | +7.11€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1314 | -0.043 | +136.78€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 607 | -0.067 | +27.99€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 478 | -0.062 | +51.74€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 129 | -0.080 | -23.75€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 461 | -0.012 | +72.85€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 340 | +0.009 | +81.60€ | 1 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 121 | -0.069 | -8.75€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 246 | -0.040 | +35.95€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 210 | -0.033 | +34.11€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 36 | -0.079 | +1.84€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 1028 | -0.033 | +167.45€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 286 | -0.076 | -30.66€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE | 1666 | -0.184 | -31.43€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 657 | -0.172 | -7.17€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 586 | -0.168 | -3.27€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 71 | -0.199 | -3.91€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH | 560 | -0.196 | -30.34€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 497 | -0.203 | -36.97€ | 4 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 63 | -0.131 | +6.63€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 449 | -0.185 | +6.08€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 418 | -0.181 | +4.44€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 31 | -0.227 | +1.64€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#atexpiry | 1501 | -0.184 | -35.80€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 165 | -0.183 | +4.36€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 590 | +0.377 | +533.67€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#BTC | 132 | +0.172 | +100.16€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 132 | +0.172 | +100.16€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#ETH | 135 | +0.369 | +106.67€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 135 | +0.369 | +106.67€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#SOL | 323 | +0.460 | +326.84€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 323 | +0.460 | +326.84€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 590 | +0.377 | +533.67€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 1042 | +0.039 | +83.78€ | 2 | 3 |
| ✅ STREAK_FADE_15M#15min | 1042 | +0.039 | +83.78€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 359 | +0.015 | +2.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 359 | +0.015 | +2.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 80 | +0.024 | +1.80€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 80 | +0.024 | +1.80€ | 1 | 1 |
| ✅ STREAK_FADE_15M#SOL | 85 | +0.029 | +7.61€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 85 | +0.029 | +7.61€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 518 | +0.060 | +72.04€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 518 | +0.060 | +72.04€ | 1 | 3 |
| ✅ STREAK_FADE_5M | 3651 | -0.023 | -144.01€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3651 | -0.023 | -144.01€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 626 | -0.030 | -28.54€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 626 | -0.030 | -28.54€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 177 | -0.048 | -15.80€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 177 | -0.048 | -15.80€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1721 | -0.018 | -59.47€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1721 | -0.018 | -59.47€ | 1 | 0 |
| ✅ STREAK_FADE_60M | 147 | +0.010 | -0.15€ | 2 | 2 |
| ✅ STREAK_FADE_60M#60min | 147 | +0.010 | -0.15€ | 0 | 0 |
| ✅ STREAK_FADE_60M#BNB | 6 | +0.075 | +6.38€ | 0 | 0 |
| ✅ STREAK_FADE_60M#BNB#60min | 6 | +0.075 | +6.38€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 49 | -0.029 | -2.10€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 49 | -0.029 | -2.10€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 84 | +0.000 | -5.54€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 84 | +0.000 | -5.54€ | 0 | 1 |
| ✅ STREAK_FADE_60M#XRP | 5 | +0.018 | -0.23€ | 0 | 0 |
| ✅ STREAK_FADE_60M#XRP#60min | 5 | +0.018 | -0.23€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 11688 | +0.013 | +60.17€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11688 | +0.013 | +60.17€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 3008 | +0.017 | +20.81€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 3008 | +0.017 | +20.81€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 3113 | +0.012 | +23.43€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 3113 | +0.012 | +23.43€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2945 | +0.008 | -2.89€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2945 | +0.008 | -2.89€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2622 | +0.014 | +18.81€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2622 | +0.014 | +18.81€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 13771 | +0.018 | +2.19€ | 4 | 0 |
| ✅ STRUCT_NO_15M#15min | 13771 | +0.018 | +2.19€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 5525 | +0.021 | +5.72€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 5525 | +0.021 | +5.72€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 4884 | +0.019 | +0.61€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 4884 | +0.019 | +0.61€ | 4 | 0 |
| ✅ STRUCT_NO_15M#SOL | 3362 | +0.014 | -4.15€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 3362 | +0.014 | -4.15€ | 1 | 0 |
| ✅ UPDOWN_GBM | 124625 | +0.060 | +11915.98€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 31084 | +0.078 | +6097.39€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 3530 | -0.001 | +40.53€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 82228 | +0.062 | +5650.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 7359 | -0.002 | +130.04€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 10863 | +0.103 | +2005.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 2052 | +0.165 | +962.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 8721 | +0.090 | +1044.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 28095 | +0.057 | +2498.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 4138 | +0.081 | +938.22€ | 0 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 1036 | +0.000 | +21.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 19442 | +0.066 | +1451.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 3327 | -0.004 | +82.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 152 | -0.065 | +4.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 14014 | +0.074 | +1549.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 2060 | +0.155 | +882.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 11868 | +0.060 | +667.40€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 29131 | +0.049 | +2086.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 7183 | +0.071 | +1127.15€ | 0 | 9 |
| ✅ UPDOWN_GBM#ETH#240min | 1002 | +0.005 | +15.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 18071 | +0.052 | +901.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2733 | -0.001 | +39.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 142 | -0.097 | +2.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 25844 | +0.041 | +1479.45€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 8428 | +0.033 | +481.68€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 919 | -0.011 | +7.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 15070 | +0.053 | +989.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1299 | +0.004 | +8.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 128 | -0.139 | -7.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 16676 | +0.073 | +2299.53€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 7223 | +0.088 | +1705.72€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 9056 | +0.064 | +595.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 422 | -0.099 | -0.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 1077 | +0.364 | +408.14€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 1077 | +0.364 | +408.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 515 | +0.363 | +183.61€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 515 | +0.363 | +183.61€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 562 | +0.363 | +224.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 562 | +0.363 | +224.53€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 29476 | -0.017 | +7392.06€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 29476 | -0.017 | +7392.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 2308 | -0.046 | +621.07€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 2308 | -0.046 | +621.07€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 5414 | -0.115 | +313.51€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 5414 | -0.115 | +313.51€ | 3 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1277 | +0.217 | +1045.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1277 | +0.217 | +1045.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 3961 | +0.217 | +2496.52€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 3961 | +0.217 | +2496.52€ | 1 | 18 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 8302 | -0.057 | +1252.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 8302 | -0.057 | +1252.71€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 8214 | -0.052 | +1662.49€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 8214 | -0.052 | +1662.49€ | 4 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 368 | +0.057 | +31.71€ | 0 | 9 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 368 | +0.057 | +31.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 368 | +0.057 | +31.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 368 | +0.057 | +31.71€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1973 | +0.285 | +1688.94€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1973 | +0.285 | +1688.94€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 1035 | +0.279 | +837.37€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 1035 | +0.279 | +837.37€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 938 | +0.290 | +851.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 938 | +0.290 | +851.57€ | 0 | 8 |
| ✅ UPDOWN_OU_5M | 900 | -0.120 | -95.27€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 900 | -0.120 | -95.27€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 290 | -0.086 | -23.04€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 290 | -0.086 | -23.04€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 105 | -0.192 | -14.83€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 105 | -0.192 | -14.83€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 122 | -0.194 | -8.05€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 122 | -0.194 | -8.05€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 5328 | +0.294 | +2369.46€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 2071 | +0.251 | +324.32€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 2062 | +0.287 | +879.99€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 1195 | +0.381 | +1165.15€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.025 n=1527 — no justifica filtro, seguir monitorizando
  - _Datos_: n=1527 IC=+0.025 PNL=+72.70€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 852 celda(s) pasan gate riguroso completo de 3059 evaluadas (n>=40) y 4176 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.033 < 0.08 — monitorear
  - _Datos_: n=8425 IC=+0.033 PNL=+480.19€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=2062/15 IC=+0.287 PNL=+879.99€ | BTC: n=2071/15 IC=+0.251 PNL=+324.32€ | SOL: n=1195/15 IC=+0.381 PNL=+1165.15€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.138 n=1162/60 | contraria IC=+0.181 n=1227 | gap=-0.043 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=646, boost estimado=+0.009. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=2733/40 IC=-0.001 PNL=+39.94€ | BTC#60min: n=3325/40 IC=-0.004 PNL=+82.15€ | SOL#60min: n=1299/40 IC=+0.004 PNL=+8.03€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.044 n=829990 | tras_1loss IC=+0.103 n=627859 | tras_2loss IC=+0.073 n=249434/40 | gap=-0.029 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.151 > 0.08 con n=1267 PNL=+710.31€
  - _Datos_: n=1267 IC=+0.151 PNL=+710.31€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.123 > 0.08 con n=1519 PNL=+676.43€
  - _Datos_: n=1519 IC=+0.123 PNL=+676.43€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.335 > 0.1 con n=4357 PNL=+2509.42€
  - _Datos_: n=4357 IC=+0.335 PNL=+2509.42€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=1256 IC=+0.064 PNL=+127.11€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1256 IC=+0.064 PNL=+127.11€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=117 IC=+0.155 PNL=+66.01€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=117 IC=+0.155 PNL=+66.01€

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
  - _Estado_: n=4822 IC=-0.006 PNL=-49.93€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4822 IC=-0.006 PNL=-49.93€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=2535 IC=+0.007 PNL=+180.04€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=2535 IC=+0.007 PNL=+180.04€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=1527 IC=+0.025 PNL=+72.70€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=1527 IC=+0.025 PNL=+72.70€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.133 > 0.1 con n=8645 PNL=+4097.27€
  - _Datos_: n=8645 IC=+0.133 PNL=+4097.27€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=4135 IC=+0.081 PNL=+937.63€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=4135 IC=+0.081 PNL=+937.63€

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
  - _Estado_: n=1676 IC=+0.042 PNL=+136.43€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=1676 IC=+0.042 PNL=+136.43€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=206 IC=-0.019 PNL=-4.76€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=206 IC=-0.019 PNL=-4.76€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.312 n=408) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=408 IC=+0.312 PNL=+496.40€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.116 > 0.02 con n=1389 PNL=+550.84€
  - _Datos_: n=1389 IC=+0.116 PNL=+550.84€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=275 IC=-0.128 PNL=+0.99€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=275 IC=-0.128 PNL=+0.99€

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
  - _Estado_: n=51192 IC=+0.070 PNL=+6887.52€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=51192 IC=+0.070 PNL=+6887.52€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.126 < -0.1 con n=846 PNL=+140.44€
  - _Datos_: n=846 IC=-0.126 PNL=+140.44€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=5025 IC=+0.066 PNL=+594.78€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=5025 IC=+0.066 PNL=+594.78€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=215 IC=-0.090 PNL=+3.25€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=215 IC=-0.090 PNL=+3.25€

**〰️ H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: n=1340 IC=+0.098 PNL=+329.41€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1340 IC=+0.098 PNL=+329.41€

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
  - _Estado_: n=49600 IC=-0.137 PNL=+3101.79€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=49600 IC=-0.137 PNL=+3101.79€

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
  - _Estado_: n=5340 IC=+0.135 PNL=+3729.17€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=5340 IC=+0.135 PNL=+3729.17€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=12909 IC=+0.057 PNL=+1099.70€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=12909 IC=+0.057 PNL=+1099.70€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.103 > 0.08 con n=5358 PNL=+3043.32€
  - _Datos_: n=5358 IC=+0.103 PNL=+3043.32€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.220 < -0.1 con n=5423 PNL=-433.05€
  - _Datos_: n=5423 IC=-0.220 PNL=-433.05€

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
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.095 n=2482) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=2482 IC=+0.095 PNL=+482.66€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.413 n=696) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=696 IC=+0.413 PNL=+1016.72€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=20915 IC=+0.176 PNL=-2442.87€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=20915 IC=+0.176 PNL=-2442.87€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.231 > 0.1 con n=347 PNL=+240.72€
  - _Datos_: n=347 IC=+0.231 PNL=+240.72€
