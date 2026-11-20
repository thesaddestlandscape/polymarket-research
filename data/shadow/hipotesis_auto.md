# Hipótesis automáticas — 2026-11-20 21:41 UTC
_Generado por shadow_postmortem.py sobre 1427547 resoluciones (PNL=+200660.77€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.5` → IC=-0.317 (n=195)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=729)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.192 (n=1079)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.505 (IC base=+0.121)

- **PATRÓN** `n_total_lado` > `61.0` → IC=+0.171 (n=348)

  - _Acción_: Kelly boost +0.86€ cuando `n_total_lado` > 61.0 (IC base=+0.121)

- **PATRÓN** `banda_hit_calibrado` > `0.8122` → IC=+0.269 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8122 (IC base=+0.121)

- **PATRÓN** `banda_z` > `8.316` → IC=+0.192 (n=339)

  - _Acción_: Kelly boost +0.96€ cuando `banda_z` > 8.316 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.137 (n=375)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 17.0 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.132 (n=1108)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.121)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.280 (n=171)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=518)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.190 (n=942)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.505 (IC base=+0.123)

- **PATRÓN** `n_total_lado` > `64.0` → IC=+0.180 (n=298)

  - _Acción_: Kelly boost +0.90€ cuando `n_total_lado` > 64.0 (IC base=+0.123)

- **PATRÓN** `banda_hit_calibrado` > `0.8119` → IC=+0.269 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8119 (IC base=+0.123)

- **PATRÓN** `banda_z` > `8.555` → IC=+0.200 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.555 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.132 (n=805)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 8.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.124 (n=620)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 12.0 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.128 (n=1008)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `8821.377` → IC=+0.133 (n=235)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 8821.377 (IC base=+0.014)

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
- **FILTRO** `restante_s_al_confirmar` < `130.62` → IC=-0.220 (n=12644)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.62
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=37939)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `122.91` → IC=-0.263 (n=1267)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 122.91
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3802)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `114.14` → IC=-0.280 (n=1269)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 114.14
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=3809)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `115.17` → IC=-0.168 (n=3478)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 115.17
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=10440)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `149.83` → IC=-0.247 (n=3476)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 149.83
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=10428)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `128.04` → IC=-0.267 (n=2336)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.04
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=7010)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.210 (n=29933)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `7933.5954` → IC=+0.153 (n=2444)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 7933.5954 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.128 (n=26345)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=31798)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.225 (n=23934)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=8706)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `6360.3108` → IC=+0.141 (n=3394)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 6360.3108 (IC base=+0.125)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=2215)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.358 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.176)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.179 (n=2710)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `16269.689` → IC=+0.181 (n=704)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 16269.689 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.186 (n=1930)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 7.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.182 (n=2158)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 17.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.328 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.179)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.181 (n=2765)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `16056.4395` → IC=+0.186 (n=714)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 16056.4395 (IC base=+0.179)

### FAVORITO_CONFIRMADO#BTC#60min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.335 (n=95)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=2371)

- **PATRÓN** `py_entrada` > `0.61` → IC=+0.172 (n=660)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` > 0.61 (IC base=+0.075)

- **PATRÓN** `libro_liquidez` > `6825.0558` → IC=+0.130 (n=152)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 6825.0558 (IC base=+0.075)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.152 (n=1547)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` < 0.44 (IC base=+0.089)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.171 (n=5443)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 6.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.175 (n=2656)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 8.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` > `0.78` → IC=+0.377 (n=1848)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.78 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.203 (n=2605)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.332 (n=988)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.201 (n=3042)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.197)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.142 (n=700)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 15.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.141 (n=943)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 11.0 (IC base=+0.138)

- **PATRÓN** `py_entrada` > `0.675` → IC=+0.251 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.675 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=1182)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `4420.281` → IC=+0.152 (n=156)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4420.281 (IC base=+0.077)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.251 (n=982)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.228)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.421 (n=1384)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.146 (n=1462)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 7.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.155 (n=749)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.146)

- **PATRÓN** `py_entrada` < `0.345` → IC=+0.278 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.345 (IC base=+0.146)

### FAVORITO_CONFIRMADO#SOL#60min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.306 (n=153)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.160 (n=483)

- **PATRÓN** `py_entrada` > `0.55` → IC=+0.160 (n=483)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` > 0.55 (IC base=+0.047)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.130 (n=1340)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 7.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.134 (n=1025)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 12.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.255 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.124)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.299 (n=152)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=78)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.198 (n=26295)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=22179)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.224 (n=8352)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.338 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `4915.142` → IC=+0.338 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4915.142 (IC base=+0.192)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=5998)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.162 (n=5971)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 18.0 (IC base=+0.162)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.175 (n=5845)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.74 (IC base=+0.162)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.210 (n=3666)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.209 (n=2441)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.246 (n=1773)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.205)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.180 (n=5847)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.173 (n=4949)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 15.0 (IC base=+0.172)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.173 (n=5998)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.73 (IC base=+0.172)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.180 (n=4594)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` > 0.71 (IC base=+0.172)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.256 (n=4620)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.251)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.251 (n=2243)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.251)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.363 (n=1599)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=5717)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.190 (n=3628)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 11.0 (IC base=+0.184)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.193 (n=4232)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.184)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.427 (n=1015)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.424)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.426 (n=1006)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.424)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.436 (n=1021)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.424)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.429 (n=1092)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.424)

- **PATRÓN** `libro_liquidez` > `14011.0969` → IC=+0.448 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14011.0969 (IC base=+0.424)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.436 (n=417)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.437)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.442 (n=428)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.448 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.437)

- **PATRÓN** `libro_liquidez` > `15265.4378` → IC=+0.442 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15265.4378 (IC base=+0.437)

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
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.401 (n=150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.398)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.404 (n=144)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.398)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.414 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.398)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.207 (n=34432)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.239 (n=34043)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.185 (n=5153)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 18.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.177 (n=11013)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 12.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.186 (n=15841)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.176)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=14356)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.276 (n=6135)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.223)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.190 (n=5907)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.199 (n=12187)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.72 (IC base=+0.181)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` > `0.775` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.229 (n=4819)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.222 (n=5521)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.259 (n=5956)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.218)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `py_entrada` < `0.775` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `libro_liquidez` < `3197.0694` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 3197.0694
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.217 (n=4876)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.257 (n=4903)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.205)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.204 (n=5730)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.199 (n=5691)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.246 (n=5805)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.197)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=12412)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.140 (n=13452)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.29` → IC=+0.142 (n=11497)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 2.29 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.195 (n=6051)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.145 (n=6106)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.124 (n=7622)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.81` → IC=+0.142 (n=7562)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 3.81 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=6361)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.137 (n=8129)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.95 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.93` → IC=+0.137 (n=7619)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.93 (IC base=+0.116)

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

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.441)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.441 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.441)

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
- **PATRÓN** `drift_60min` |x|≤ `0.5018` → IC=+0.139 (n=19645)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.5018 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.127 (n=19898)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.126 (n=13656)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.9749` → IC=+0.246 (n=6548)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9749 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.8425` → IC=+0.288 (n=1045)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8425 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.477` → IC=+0.190 (n=9865)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 3.477 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.697` → IC=+0.268 (n=5348)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.697 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.3033` → IC=+0.253 (n=2039)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3033 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.7407` → IC=+0.232 (n=4744)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7407 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=9554)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `4794.6651` → IC=+0.151 (n=6548)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4794.6651 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.123 (n=12427)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0065 (IC base=+0.087)

- **PATRÓN** `ibs_20min` < `0.563` → IC=+0.146 (n=24820)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.563 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.6565` → IC=+0.191 (n=1628)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.6565 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` < `0.1731` → IC=+0.195 (n=10171)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.1731 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` < `0.8596` → IC=+0.196 (n=6887)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.8596 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.296` → IC=+0.233 (n=2514)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.296 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `1.4565` → IC=+0.210 (n=17504)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4565 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `99.0` → IC=+0.230 (n=17440)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 99.0 (IC base=+0.087)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.243 (n=1393)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0108 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.3003` → IC=+0.213 (n=3676)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3003 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.223 (n=2031)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.209)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.211 (n=2798)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` > `0.9828` → IC=+0.273 (n=1894)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9828 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.799` → IC=+0.293 (n=992)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.799 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.2345` → IC=+0.257 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2345 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `1.4416` → IC=+0.210 (n=4011)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4416 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.221 (n=4592)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `2040.9902` → IC=+0.215 (n=1393)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2040.9902 (IC base=+0.209)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.218 (n=3400)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.209)

- **PATRÓN** `sigma_h` > `0.008` → IC=+0.246 (n=2514)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.008 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.0944` → IC=+0.271 (n=1257)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0944 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.241 (n=3929)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.248 (n=1721)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0756` → IC=+0.281 (n=1257)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0756 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.961` → IC=+0.245 (n=3860)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.961 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` < `0.0726` → IC=+0.244 (n=3256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0726 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.2904` → IC=+0.249 (n=505)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2904 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.4488` → IC=+0.241 (n=1203)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4488 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `1.8601` → IC=+0.244 (n=2405)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8601 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.244 (n=2633)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.240)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.233 (n=1192)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.222)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.225 (n=1188)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.1133` → IC=+0.247 (n=1566)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1133 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=3733)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.222 (n=2537)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `0.8935` → IC=+0.257 (n=1188)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8935 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` > `0.1981` → IC=+0.233 (n=1546)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1981 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.747` → IC=+0.263 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.747 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` > `0.6976` → IC=+0.229 (n=3180)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6976 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.2772` → IC=+0.267 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2772 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.4428` → IC=+0.251 (n=1172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4428 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `15793.6462` → IC=+0.223 (n=1187)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15793.6462 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.154 (n=3901)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0069 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.275` → IC=+0.148 (n=3430)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.275 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.147 (n=2781)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 11.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.7084` → IC=+0.173 (n=3898)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.7084 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.1494` → IC=+0.151 (n=3839)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1494 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.569` → IC=+0.136 (n=618)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 10.569 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.942` → IC=+0.141 (n=3575)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 3.942 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `0.6304` → IC=+0.153 (n=1300)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6304 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.0982` → IC=+0.161 (n=1418)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.0982 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `2.4481` → IC=+0.143 (n=3767)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.4481 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=5065)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `167.0` → IC=+0.186 (n=1244)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 167.0 (IC base=+0.135)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.013` → IC=+0.203 (n=1477)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.013 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=4660)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.192)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.253 (n=1701)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.913` → IC=+0.280 (n=977)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.913 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` < `0.0968` → IC=+0.191 (n=3973)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.0968 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` > `0.3497` → IC=+0.221 (n=572)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3497 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` > `2.7283` → IC=+0.207 (n=1962)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7283 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.196 (n=5390)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.04 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `1904.5482` → IC=+0.196 (n=2008)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 1904.5482 (IC base=+0.192)

- **PATRÓN** `sigma_h` < `0.0113` → IC=+0.224 (n=3650)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0113 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.305` → IC=+0.230 (n=2764)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.305 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.241 (n=1574)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.227 (n=1878)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` < `0.0488` → IC=+0.272 (n=1382)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0488 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.738` → IC=+0.269 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.738 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.3453` → IC=+0.254 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3453 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.152` → IC=+0.232 (n=2669)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.152 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.223 (n=2002)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `1886.9572` → IC=+0.226 (n=1880)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1886.9572 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.225 (n=3984)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.222)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.168 (n=233)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=5352)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.145 (n=713)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.004 (IC base=+0.066)

- **PATRÓN** `ibs_20min` > `0.9436` → IC=+0.249 (n=714)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9436 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` > `0.1538` → IC=+0.345 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1538 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` < `0.5788` → IC=+0.342 (n=935)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5788 (IC base=+0.066)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.174` → IC=+0.214 (n=1573)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.174 (IC base=+0.066)

- **PATRÓN** `volumen_regimen` > `1.1208` → IC=+0.364 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1208 (IC base=+0.066)

- **PATRÓN** `volumen_pendiente_norm` < `0.1672` → IC=+0.345 (n=707)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1672 (IC base=+0.066)

- **PATRÓN** `volumen_pendiente_norm` > `0.3024` → IC=+0.351 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3024 (IC base=+0.066)

- **PATRÓN** `volumen_spike_ratio` < `1.421` → IC=+0.357 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.421 (IC base=+0.066)

- **PATRÓN** `volumen_spike_ratio` > `2.2799` → IC=+0.348 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2799 (IC base=+0.066)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.348 (n=868)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.066)

- **PATRÓN** `ibs_20min` < `0.0867` → IC=+0.191 (n=1397)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.0867 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` > `0.3561` → IC=+0.160 (n=684)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.3561 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` < `0.1486` → IC=+0.158 (n=2611)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1486 (IC base=+0.059)

- **PATRÓN** `volumen_regimen` < `0.8315` → IC=+0.164 (n=1829)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8315 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.2783` → IC=+0.203 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2783 (IC base=+0.059)

- **PATRÓN** `volumen_spike_ratio` > `2.4323` → IC=+0.175 (n=880)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.4323 (IC base=+0.059)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.188 (n=158)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=860)

- **FILTRO** `ibs_20min` > `0.1951` → IC=-0.126 (n=5243)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1951
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=2585)

- **FILTRO** `sigma_ewma_delta_pct` > `8.292` → IC=-0.233 (n=845)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.292
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=6983)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.174 (n=351)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.75 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` > `0.9754` → IC=+0.273 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9754 (IC base=+0.022)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.712` → IC=+0.175 (n=161)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 6.712 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` > `0.6233` → IC=+0.284 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6233 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` < `0.0752` → IC=+0.280 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0752 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` < `2.1989` → IC=+0.288 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1989 (IC base=+0.022)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.268 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.022)

- **PATRÓN** `ibs_20min` < `0.1951` → IC=+0.161 (n=2585)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1951 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` > `0.2322` → IC=+0.291 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2322 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` < `0.3191` → IC=+0.292 (n=1270)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3191 (IC base=-0.031)

- **PATRÓN** `volumen_regimen` < `0.6948` → IC=+0.301 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6948 (IC base=-0.031)

- **PATRÓN** `volumen_regimen` > `1.0477` → IC=+0.292 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0477 (IC base=-0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.0781` → IC=+0.315 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0781 (IC base=-0.031)

- **PATRÓN** `volumen_spike_ratio` < `2.4253` → IC=+0.303 (n=1110)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4253 (IC base=-0.031)

- **PATRÓN** `volumen_spike_ratio` > `1.4131` → IC=+0.298 (n=1110)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4131 (IC base=-0.031)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7964` → IC=-0.159 (n=4030)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7964
  - _Potencial_: sin este filtro IC_bueno=+0.141 (n=2077)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.177 (n=1251)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=4856)

- **FILTRO** `ibs_20min` > `0.7288` → IC=-0.190 (n=2109)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7288
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=6335)

- **PATRÓN** `ibs_20min` > `0.7964` → IC=+0.141 (n=2077)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` > 0.7964 (IC base=-0.057)

- **PATRÓN** `dist_vwap_pct` > `0.4451` → IC=+0.335 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4451 (IC base=-0.057)

- **PATRÓN** `volumen_regimen` > `0.7065` → IC=+0.318 (n=1108)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7065 (IC base=-0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.1727` → IC=+0.308 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1727 (IC base=-0.057)

- **PATRÓN** `volumen_spike_ratio` > `2.5275` → IC=+0.313 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5275 (IC base=-0.057)

- **PATRÓN** `dist_vwap_pct` > `1.0843` → IC=+0.294 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0843 (IC base=+0.007)

- **PATRÓN** `volumen_regimen` < `0.7214` → IC=+0.275 (n=1103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7214 (IC base=+0.007)

- **PATRÓN** `volumen_regimen` > `1.064` → IC=+0.279 (n=1136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.064 (IC base=+0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.237` → IC=+0.283 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.237 (IC base=+0.007)

- **PATRÓN** `volumen_spike_ratio` < `2.486` → IC=+0.265 (n=2378)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.486 (IC base=+0.007)

- **PATRÓN** `volumen_spike_ratio` > `1.442` → IC=+0.271 (n=2378)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.442 (IC base=+0.007)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.188 (n=8595)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.011 (IC base=+0.086)

- **PATRÓN** `ibs_20min` > `0.8654` → IC=+0.283 (n=11684)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8654 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` > `0.9762` → IC=+0.301 (n=1756)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9762 (IC base=+0.086)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.464` → IC=+0.167 (n=11615)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 3.464 (IC base=+0.086)

- **PATRÓN** `volumen_regimen` > `0.6935` → IC=+0.279 (n=8542)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6935 (IC base=+0.086)

- **PATRÓN** `volumen_pendiente_norm` > `0.2925` → IC=+0.295 (n=2116)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2925 (IC base=+0.086)

- **PATRÓN** `volumen_spike_ratio` > `2.6384` → IC=+0.286 (n=4982)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6384 (IC base=+0.086)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.308 (n=14606)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 88.0 (IC base=+0.086)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.153 (n=11373)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0091 (IC base=+0.088)

- **PATRÓN** `ibs_20min` < `0.5161` → IC=+0.175 (n=22068)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.5161 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` < `0.2752` → IC=+0.283 (n=8855)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2752 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` < `0.6972` → IC=+0.281 (n=3744)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6972 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` > `1.1905` → IC=+0.285 (n=2837)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1905 (IC base=+0.088)

- **PATRÓN** `volumen_pendiente_norm` > `0.2944` → IC=+0.323 (n=1879)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2944 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` < `1.5737` → IC=+0.304 (n=5569)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5737 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` > `2.2694` → IC=+0.304 (n=5737)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2694 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.312 (n=12629)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 70.0 (IC base=+0.088)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8111` → IC=-0.145 (n=4570)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8111
  - _Potencial_: sin este filtro IC_bueno=+0.309 (n=2355)

- **FILTRO** `ibs_20min` > `0.701` → IC=-0.239 (n=1555)

  - _Acción_: SKIP cuando `ibs_20min` > 0.701
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=4666)

- **FILTRO** `sigma_ewma_delta_pct` > `4.065` → IC=-0.240 (n=1312)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.065
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=4909)

- **PATRÓN** `ibs_20min` > `0.8111` → IC=+0.309 (n=2355)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8111 (IC base=+0.010)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.955` → IC=+0.182 (n=2316)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 2.955 (IC base=+0.010)

- **PATRÓN** `volumen_pendiente_norm` > `0.2295` → IC=+0.333 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2295 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` < `1.4467` → IC=+0.288 (n=725)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4467 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` > `2.2327` → IC=+0.313 (n=986)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2327 (IC base=+0.010)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.320 (n=1477)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.010)

- **PATRÓN** `ibs_20min` < `0.1702` → IC=+0.174 (n=1557)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.1702 (IC base=-0.014)

- **PATRÓN** `volumen_pendiente_norm` < `0.1559` → IC=+0.390 (n=1364)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1559 (IC base=-0.014)

- **PATRÓN** `volumen_spike_ratio` < `2.6476` → IC=+0.394 (n=1308)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6476 (IC base=-0.014)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1775` → IC=+0.227 (n=1050)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1775 (IC base=+0.010)

- **PATRÓN** `volumen_regimen` > `0.6955` → IC=+0.221 (n=2245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6955 (IC base=+0.010)

- **PATRÓN** `volumen_pendiente_norm` > `0.2739` → IC=+0.246 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2739 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` < `1.4151` → IC=+0.231 (n=828)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4151 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` > `2.4483` → IC=+0.223 (n=828)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4483 (IC base=+0.010)

- **PATRÓN** `ballena_activa_n` < `370.0` → IC=+0.233 (n=2484)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 370.0 (IC base=+0.010)

- **PATRÓN** `dist_vwap_pct` < `0.1519` → IC=+0.265 (n=1940)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1519 (IC base=+0.004)

- **PATRÓN** `volumen_regimen` < `0.6851` → IC=+0.252 (n=821)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6851 (IC base=+0.004)

- **PATRÓN** `volumen_regimen` > `1.0208` → IC=+0.265 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0208 (IC base=+0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2707` → IC=+0.298 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2707 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` < `1.4236` → IC=+0.259 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4236 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` > `2.1523` → IC=+0.266 (n=821)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1523 (IC base=+0.004)

- **PATRÓN** `ballena_activa_n` < `197.0` → IC=+0.276 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 197.0 (IC base=+0.004)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.318 (n=1609)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.293 (n=3562)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.284)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.322 (n=1910)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.584` → IC=+0.305 (n=2403)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.584 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` < `0.1308` → IC=+0.292 (n=3302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1308 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` > `3.2355` → IC=+0.300 (n=1152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.2355 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.291 (n=4290)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `2015.7584` → IC=+0.294 (n=1183)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2015.7584 (IC base=+0.284)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.301 (n=2180)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.336 (n=2204)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0092 (IC base=+0.307)

- **PATRÓN** `drift_60min` |x|≤ `0.1861` → IC=+0.327 (n=1454)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1861 (IC base=+0.307)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.324 (n=1269)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.307)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.309 (n=1494)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.307)

- **PATRÓN** `ibs_20min` < `0.0285` → IC=+0.308 (n=1454)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0285 (IC base=+0.307)

- **PATRÓN** `ibs_20min` > `0.1532` → IC=+0.319 (n=2202)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1532 (IC base=+0.307)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.064` → IC=+0.317 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.064 (IC base=+0.307)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.411` → IC=+0.308 (n=3422)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.411 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` < `0.1986` → IC=+0.309 (n=3281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1986 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` > `0.3437` → IC=+0.314 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3437 (IC base=+0.307)

- **PATRÓN** `volumen_spike_ratio` > `2.7347` → IC=+0.325 (n=1451)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7347 (IC base=+0.307)

- **PATRÓN** `libro_liquidez` > `1999.178` → IC=+0.317 (n=1101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1999.178 (IC base=+0.307)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.311 (n=2219)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.307)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **PATRÓN** `dist_vwap_pct` > `0.1552` → IC=+0.236 (n=1154)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1552 (IC base=+0.023)

- **PATRÓN** `dist_vwap_pct` < `0.6151` → IC=+0.235 (n=2583)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6151 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` < `1.1687` → IC=+0.235 (n=2341)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1687 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` > `0.5973` → IC=+0.234 (n=2340)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5973 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` < `0.1635` → IC=+0.237 (n=2458)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1635 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` > `0.103` → IC=+0.240 (n=765)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.103 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` < `2.4135` → IC=+0.241 (n=2273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4135 (IC base=+0.023)

- **PATRÓN** `ballena_activa_n` < `112.0` → IC=+0.251 (n=2318)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 112.0 (IC base=+0.023)

- **PATRÓN** `ibs_20min` < `0.0913` → IC=+0.152 (n=1624)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.0913 (IC base=+0.012)

- **PATRÓN** `dist_vwap_pct` < `0.3722` → IC=+0.262 (n=1906)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3722 (IC base=+0.012)

- **PATRÓN** `volumen_regimen` < `1.1824` → IC=+0.264 (n=1704)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1824 (IC base=+0.012)

- **PATRÓN** `volumen_regimen` > `0.6165` → IC=+0.258 (n=1704)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6165 (IC base=+0.012)

- **PATRÓN** `volumen_pendiente_norm` > `0.282` → IC=+0.292 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.282 (IC base=+0.012)

- **PATRÓN** `volumen_spike_ratio` < `1.7842` → IC=+0.285 (n=1095)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7842 (IC base=+0.012)

- **PATRÓN** `volumen_spike_ratio` > `2.4204` → IC=+0.280 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4204 (IC base=+0.012)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.283 (n=1673)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.012)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.75` → IC=-0.246 (n=2657)

  - _Acción_: SKIP cuando `ibs_20min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.312 (n=2661)

- **FILTRO** `ibs_20min` > `0.6087` → IC=-0.238 (n=1256)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6087
  - _Potencial_: sin este filtro IC_bueno=+0.165 (n=3774)

- **FILTRO** `sigma_ewma_delta_pct` > `8.26` → IC=-0.268 (n=575)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.26
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=4455)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.312 (n=2661)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.75 (IC base=+0.033)

- **PATRÓN** `dist_vwap_pct` > `1.0858` → IC=+0.349 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0858 (IC base=+0.033)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.441` → IC=+0.157 (n=2172)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 2.441 (IC base=+0.033)

- **PATRÓN** `volumen_regimen` < `0.8453` → IC=+0.347 (n=1297)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8453 (IC base=+0.033)

- **PATRÓN** `volumen_regimen` > `0.6972` → IC=+0.334 (n=1738)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6972 (IC base=+0.033)

- **PATRÓN** `volumen_pendiente_norm` < `0.0995` → IC=+0.336 (n=1834)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0995 (IC base=+0.033)

- **PATRÓN** `volumen_pendiente_norm` > `0.2738` → IC=+0.360 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2738 (IC base=+0.033)

- **PATRÓN** `volumen_spike_ratio` < `1.7809` → IC=+0.354 (n=1261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7809 (IC base=+0.033)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.352 (n=1698)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.033)

- **PATRÓN** `ibs_20min` < `0.6087` → IC=+0.165 (n=3774)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.6087 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` < `0.2383` → IC=+0.276 (n=1938)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2383 (IC base=+0.064)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.737` → IC=+0.133 (n=3942)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 4.737 (IC base=+0.064)

- **PATRÓN** `volumen_regimen` < `0.6912` → IC=+0.285 (n=860)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6912 (IC base=+0.064)

- **PATRÓN** `volumen_pendiente_norm` > `0.0706` → IC=+0.298 (n=781)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0706 (IC base=+0.064)

- **PATRÓN** `volumen_spike_ratio` < `2.1202` → IC=+0.282 (n=1668)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1202 (IC base=+0.064)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.291 (n=1931)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 45.0 (IC base=+0.064)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.351 (n=2470)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.312)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.315 (n=2791)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.312)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.315 (n=2904)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.312)

- **PATRÓN** `ibs_20min` > `0.6512` → IC=+0.337 (n=2765)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6512 (IC base=+0.312)

- **PATRÓN** `dist_vwap_pct` > `0.2191` → IC=+0.335 (n=1470)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2191 (IC base=+0.312)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.823` → IC=+0.336 (n=1080)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.823 (IC base=+0.312)

- **PATRÓN** `volumen_regimen` > `0.6293` → IC=+0.324 (n=2765)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6293 (IC base=+0.312)

- **PATRÓN** `volumen_pendiente_norm` > `0.2834` → IC=+0.345 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2834 (IC base=+0.312)

- **PATRÓN** `volumen_spike_ratio` > `1.5317` → IC=+0.324 (n=2386)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5317 (IC base=+0.312)

- **PATRÓN** `libro_liquidez` > `2681.708` → IC=+0.318 (n=1843)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2681.708 (IC base=+0.312)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.332 (n=2989)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.313)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.316 (n=2997)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.313)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.315 (n=2996)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.313)

- **PATRÓN** `ibs_20min` < `0.3888` → IC=+0.330 (n=2989)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3888 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` > `0.3471` → IC=+0.316 (n=911)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3471 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` < `0.2551` → IC=+0.316 (n=2954)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2551 (IC base=+0.313)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.195` → IC=+0.325 (n=551)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.195 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` < `0.7178` → IC=+0.317 (n=1317)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7178 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` > `1.2103` → IC=+0.340 (n=996)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2103 (IC base=+0.313)

- **PATRÓN** `volumen_pendiente_norm` > `0.2867` → IC=+0.364 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2867 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` < `1.4149` → IC=+0.324 (n=935)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4149 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` > `2.1503` → IC=+0.316 (n=1271)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1503 (IC base=+0.313)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.218 (n=6284)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.1256` → IC=+0.192 (n=8299)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1256 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=19596)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `0.5365` → IC=+0.228 (n=18847)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5365 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.1674` → IC=+0.205 (n=7083)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1674 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.987` → IC=+0.254 (n=4941)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.987 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `1.1739` → IC=+0.151 (n=12569)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1739 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` > `0.6223` → IC=+0.151 (n=12570)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6223 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.2927` → IC=+0.204 (n=2722)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2927 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `2.5941` → IC=+0.182 (n=6119)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.5941 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.190 (n=17812)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 85.0 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.194 (n=8315)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0061 (IC base=+0.186)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.188 (n=12567)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0081 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.0849` → IC=+0.222 (n=6284)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0849 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.207 (n=9040)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` < `0.4` → IC=+0.247 (n=16610)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.442` → IC=+0.191 (n=2974)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 9.442 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.493` → IC=+0.193 (n=16804)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 2.493 (IC base=+0.186)

- **PATRÓN** `volumen_regimen` < `1.1916` → IC=+0.166 (n=13344)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1916 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.2949` → IC=+0.220 (n=2833)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2949 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `2.6319` → IC=+0.198 (n=6000)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.6319 (IC base=+0.186)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.200 (n=17823)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 89.0 (IC base=+0.186)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.257 (n=1032)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.2833` → IC=+0.243 (n=2723)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2833 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=3228)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.227 (n=2103)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.9421` → IC=+0.293 (n=2063)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9421 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.461` → IC=+0.328 (n=1019)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.461 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2316` → IC=+0.281 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2316 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `1.8334` → IC=+0.226 (n=1973)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8334 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `1.4374` → IC=+0.226 (n=2958)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4374 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=3416)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0101` → IC=+0.255 (n=2609)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0101 (IC base=+0.253)

- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.262 (n=1740)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0077 (IC base=+0.253)

- **PATRÓN** `drift_60min` |x|≤ `0.1007` → IC=+0.307 (n=1148)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1007 (IC base=+0.253)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.257 (n=2698)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.253)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.259 (n=2375)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.253)

- **PATRÓN** `ibs_20min` < `0.4419` → IC=+0.271 (n=2608)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4419 (IC base=+0.253)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.245` → IC=+0.259 (n=2913)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.245 (IC base=+0.253)

- **PATRÓN** `volumen_pendiente_norm` < `0.0741` → IC=+0.257 (n=2173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0741 (IC base=+0.253)

- **PATRÓN** `volumen_pendiente_norm` > `0.3006` → IC=+0.267 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3006 (IC base=+0.253)

- **PATRÓN** `volumen_spike_ratio` < `2.2687` → IC=+0.258 (n=2205)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2687 (IC base=+0.253)

- **PATRÓN** `volumen_spike_ratio` > `2.6858` → IC=+0.255 (n=835)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6858 (IC base=+0.253)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.262 (n=1829)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.253)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.190 (n=960)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0033 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.0668` → IC=+0.175 (n=961)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0668 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.144 (n=3011)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `0.2519` → IC=+0.205 (n=2880)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2519 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `0.1921` → IC=+0.211 (n=1398)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1921 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.561` → IC=+0.204 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.561 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.8532` → IC=+0.134 (n=1920)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.8532 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` > `1.0468` → IC=+0.134 (n=1306)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` > 1.0468 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2765` → IC=+0.170 (n=441)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2765 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.7716` → IC=+0.129 (n=1890)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.7716 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `2.4553` → IC=+0.142 (n=945)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.4553 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `390.0` → IC=+0.133 (n=2804)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 390.0 (IC base=+0.128)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.181 (n=2741)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0059 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.2532` → IC=+0.176 (n=2736)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2532 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.181 (n=1486)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.6109` → IC=+0.212 (n=3109)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6109 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.214` → IC=+0.176 (n=3393)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.214 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.871` → IC=+0.183 (n=578)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 10.871 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.995` → IC=+0.157 (n=2723)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 3.995 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `1.2096` → IC=+0.163 (n=3109)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2096 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` < `0.0722` → IC=+0.155 (n=2591)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.0722 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.4814` → IC=+0.157 (n=2982)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4814 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `204.0` → IC=+0.194 (n=1294)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 204.0 (IC base=+0.153)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.223 (n=1445)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.2549` → IC=+0.232 (n=2126)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2549 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.216 (n=3331)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.288 (n=1686)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.04` → IC=+0.305 (n=757)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.04 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.3501` → IC=+0.232 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3501 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `2.7088` → IC=+0.221 (n=1413)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7088 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.211 (n=3874)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `2009.4584` → IC=+0.220 (n=1063)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2009.4584 (IC base=+0.208)

- **PATRÓN** `sigma_h` < `0.0121` → IC=+0.245 (n=2884)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0121 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.2526` → IC=+0.270 (n=1922)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2526 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.277 (n=1094)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.0415` → IC=+0.296 (n=1270)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0415 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.854` → IC=+0.286 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.854 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.3529` → IC=+0.285 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3529 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `1.7663` → IC=+0.242 (n=1229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7663 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `2.1786` → IC=+0.254 (n=1862)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1786 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `1880.6384` → IC=+0.253 (n=1308)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1880.6384 (IC base=+0.241)

- **PATRÓN** `ballena_activa_n` < `4.0` → IC=+0.241 (n=924)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 4.0 (IC base=+0.241)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.194 (n=1038)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0039 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.0809` → IC=+0.173 (n=1038)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0809 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.136 (n=3224)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.2458` → IC=+0.187 (n=3111)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.2458 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `0.1478` → IC=+0.187 (n=1751)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1478 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.231` → IC=+0.201 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.231 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `0.838` → IC=+0.137 (n=2075)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.838 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2873` → IC=+0.172 (n=467)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2873 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.517` → IC=+0.128 (n=1341)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.517 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `2.5003` → IC=+0.134 (n=1016)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.5003 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `6951.1879` → IC=+0.196 (n=1411)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 6951.1879 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `123.0` → IC=+0.126 (n=3059)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 123.0 (IC base=+0.125)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.174 (n=2232)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0057 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.4282` → IC=+0.149 (n=3340)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4282 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.165 (n=1601)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.6686` → IC=+0.189 (n=3339)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.6686 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.1682` → IC=+0.157 (n=3423)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1682 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.508` → IC=+0.141 (n=1142)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 6.508 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.053` → IC=+0.133 (n=2974)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 4.053 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.8551` → IC=+0.152 (n=2226)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8551 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.2937` → IC=+0.176 (n=504)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2937 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.1878` → IC=+0.135 (n=2797)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.1878 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.4105` → IC=+0.136 (n=3178)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4105 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `6662.7463` → IC=+0.191 (n=1514)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 6662.7463 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.160 (n=1051)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 47.0 (IC base=+0.133)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0128` → IC=+0.172 (n=1156)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0128 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.134 (n=3565)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` > `0.5938` → IC=+0.224 (n=3095)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5938 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `0.781` → IC=+0.212 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.781 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.014` → IC=+0.286 (n=732)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.014 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.1665` → IC=+0.130 (n=3465)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1665 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.1617` → IC=+0.123 (n=3538)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1617 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.7845` → IC=+0.127 (n=2242)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.7845 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2709.6836` → IC=+0.196 (n=1571)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2709.6836 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.127 (n=2210)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 27.0 (IC base=+0.120)

- **PATRÓN** `sigma_h` < `0.0123` → IC=+0.144 (n=3645)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0123 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.1187` → IC=+0.166 (n=1216)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1187 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.140 (n=3723)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.4872` → IC=+0.239 (n=3207)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4872 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.232` → IC=+0.147 (n=3221)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 2.232 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.1823` → IC=+0.131 (n=3643)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1823 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` > `0.8596` → IC=+0.127 (n=2429)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.8596 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` < `0.1628` → IC=+0.128 (n=3599)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1628 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2758` → IC=+0.148 (n=507)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2758 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.4363` → IC=+0.144 (n=1153)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4363 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `2.4427` → IC=+0.136 (n=1153)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.4427 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2609.1217` → IC=+0.190 (n=1652)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2609.1217 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.131 (n=3460)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 43.0 (IC base=+0.125)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.246 (n=3115)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.225)

- **PATRÓN** `drift_60min` |x|≤ `0.1681` → IC=+0.240 (n=1370)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1681 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.231 (n=3237)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=2815)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `0.6647` → IC=+0.256 (n=3114)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6647 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` > `0.1844` → IC=+0.233 (n=1914)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1844 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` < `0.817` → IC=+0.227 (n=3213)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.817 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.529` → IC=+0.261 (n=1454)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.529 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` > `0.6198` → IC=+0.236 (n=3114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6198 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.2871` → IC=+0.265 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2871 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` < `2.4697` → IC=+0.229 (n=3040)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4697 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `1.8243` → IC=+0.227 (n=2027)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8243 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `2625.8761` → IC=+0.232 (n=2076)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2625.8761 (IC base=+0.225)

- **PATRÓN** `sigma_h` > `0.0165` → IC=+0.248 (n=2169)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0165 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.6132` → IC=+0.247 (n=3254)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6132 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.248 (n=1604)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.241 (n=1457)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.038` → IC=+0.297 (n=1432)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.038 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` > `1.1626` → IC=+0.251 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1626 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.064` → IC=+0.270 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.064 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` < `0.8693` → IC=+0.240 (n=2171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8693 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` > `1.0483` → IC=+0.243 (n=1475)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0483 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2837` → IC=+0.293 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2837 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.8442` → IC=+0.237 (n=2056)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8442 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `1.5529` → IC=+0.238 (n=2754)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5529 (IC base=+0.238)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.205 (n=1655)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.1427` → IC=+0.172 (n=2182)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1427 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.166 (n=5170)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.6608` → IC=+0.219 (n=3304)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6608 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.2333` → IC=+0.170 (n=1855)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.2333 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.538` → IC=+0.208 (n=803)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.538 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `0.8588` → IC=+0.163 (n=3002)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8588 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` > `1.1914` → IC=+0.159 (n=1501)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 1.1914 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.0972` → IC=+0.168 (n=1756)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.0972 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.5247` → IC=+0.160 (n=2128)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.5247 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.159 (n=4184)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `7272.8833` → IC=+0.192 (n=2247)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 7272.8833 (IC base=+0.154)

- **PATRÓN** `ibs_20min` < `0.3864` → IC=+0.179 (n=3616)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.3864 (IC base=+0.102)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.147 (n=2389)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 22.0 (IC base=+0.102)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.206 (n=1194)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0063 (IC base=+0.195)

- **PATRÓN** `drift_60min` |x|≤ `0.1039` → IC=+0.231 (n=525)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1039 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.227 (n=1077)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `0.6225` → IC=+0.255 (n=795)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6225 (IC base=+0.195)

- **PATRÓN** `dist_vwap_pct` > `0.3199` → IC=+0.223 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3199 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.923` → IC=+0.223 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.923 (IC base=+0.195)

- **PATRÓN** `volumen_regimen` < `0.7016` → IC=+0.223 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7016 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.0908` → IC=+0.212 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0908 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` < `2.1519` → IC=+0.208 (n=1030)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1519 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `13767.6452` → IC=+0.203 (n=795)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13767.6452 (IC base=+0.195)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.157 (n=500)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0032 (IC base=+0.071)

- **PATRÓN** `ibs_20min` < `0.2163` → IC=+0.193 (n=655)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.2163 (IC base=+0.071)

- **PATRÓN** `ballena_activa_n` < `170.0` → IC=+0.164 (n=643)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 170.0 (IC base=+0.071)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.239 (n=507)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.1318` → IC=+0.159 (n=670)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1318 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.169 (n=1579)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.7759` → IC=+0.263 (n=689)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7759 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.8774` → IC=+0.185 (n=233)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.8774 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.945` → IC=+0.190 (n=217)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 9.945 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.8342` → IC=+0.163 (n=1013)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8342 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.2192` → IC=+0.185 (n=268)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2192 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.7716` → IC=+0.164 (n=999)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.7716 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `7954.048` → IC=+0.177 (n=689)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 7954.048 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.150 (n=656)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 37.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.134 (n=670)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0044 (IC base=+0.106)

- **PATRÓN** `ibs_20min` < `0.1841` → IC=+0.199 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1841 (IC base=+0.106)

- **PATRÓN** `volumen_regimen` < `0.6756` → IC=+0.141 (n=670)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.6756 (IC base=+0.106)

- **PATRÓN** `volumen_pendiente_norm` > `0.0768` → IC=+0.125 (n=558)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` > 0.0768 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `5598.5419` → IC=+0.149 (n=1014)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 5598.5419 (IC base=+0.106)

- **PATRÓN** `ballena_activa_n` < `80.0` → IC=+0.129 (n=1301)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 80.0 (IC base=+0.106)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.150 (n=447)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.007 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.148 (n=943)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 11.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` > `0.7143` → IC=+0.208 (n=900)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7143 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` > `0.2127` → IC=+0.125 (n=625)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` > 0.2127 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.88` → IC=+0.213 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.88 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.2186` → IC=+0.134 (n=230)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.2186 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` < `1.4125` → IC=+0.147 (n=434)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4125 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `3057.1568` → IC=+0.144 (n=447)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 3057.1568 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.5517` → IC=+0.171 (n=1306)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.5517 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `2764.626` → IC=+0.165 (n=673)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2764.626 (IC base=+0.092)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.120 (n=1275)

  - _Acción_: Kelly boost +0.60€ cuando `ballena_activa_n` < 27.0 (IC base=+0.092)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0152` → IC=+0.238 (n=300)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0152 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.222 (n=210)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` < `0.8608` → IC=+0.181 (n=396)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.8608 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `0.5179` → IC=+0.196 (n=402)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.5179 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.931` → IC=+0.199 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.931 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.507` → IC=+0.193 (n=450)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 5.507 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` > `1.1874` → IC=+0.250 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1874 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` < `0.1731` → IC=+0.188 (n=446)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` < 0.1731 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.0792` → IC=+0.205 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0792 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` < `2.1265` → IC=+0.195 (n=369)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.1265 (IC base=+0.179)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.191 (n=474)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.03 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `2727.8122` → IC=+0.202 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2727.8122 (IC base=+0.179)

- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.173 (n=496)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0105 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.3414` → IC=+0.164 (n=331)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.3414 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.201 (n=242)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` < `0.35` → IC=+0.161 (n=334)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.35 (IC base=+0.156)

- **PATRÓN** `ibs_20min` > `0.1049` → IC=+0.163 (n=496)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.1049 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `1.1964` → IC=+0.275 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1964 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `0.8885` → IC=+0.191 (n=331)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.8885 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` < `0.1134` → IC=+0.172 (n=461)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` < 0.1134 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.2375` → IC=+0.200 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2375 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `1.4907` → IC=+0.191 (n=160)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.4907 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `2.6321` → IC=+0.173 (n=160)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.6321 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `2694.7519` → IC=+0.158 (n=331)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2694.7519 (IC base=+0.156)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.172 (n=476)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 20.0 (IC base=+0.156)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.225 (n=8302)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=26013)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.9675` → IC=+0.302 (n=8300)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9675 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.9202` → IC=+0.216 (n=2837)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9202 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.926` → IC=+0.260 (n=6104)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.926 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `1.2144` → IC=+0.159 (n=16778)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2144 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2919` → IC=+0.214 (n=3268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2919 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6206` → IC=+0.192 (n=8110)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6206 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.199 (n=23534)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.209 (n=7719)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0124 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.5084` → IC=+0.201 (n=23147)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5084 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=8669)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.4848` → IC=+0.253 (n=20374)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4848 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` < `0.1878` → IC=+0.183 (n=14830)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.1878 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.351` → IC=+0.204 (n=22631)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.351 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `0.6304` → IC=+0.180 (n=5174)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.6304 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.2936` → IC=+0.255 (n=3185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2936 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `2.6212` → IC=+0.212 (n=7419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6212 (IC base=+0.199)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.215 (n=22051)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.199)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.272 (n=1325)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.3744` → IC=+0.234 (n=3973)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3744 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.239 (n=4172)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.233)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.234 (n=2673)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` > `0.8618` → IC=+0.293 (n=2648)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8618 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.026` → IC=+0.301 (n=2610)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.026 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.2328` → IC=+0.287 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2328 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.2907` → IC=+0.240 (n=1743)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2907 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.247 (n=4354)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `2040.64` → IC=+0.241 (n=1324)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2040.64 (IC base=+0.233)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.267 (n=3628)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.266)

- **PATRÓN** `sigma_h` > `0.008` → IC=+0.269 (n=2418)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.008 (IC base=+0.266)

- **PATRÓN** `drift_60min` |x|≤ `0.1265` → IC=+0.292 (n=1594)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1265 (IC base=+0.266)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.268 (n=3770)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.266)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.271 (n=3261)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.266)

- **PATRÓN** `ibs_20min` < `0.4651` → IC=+0.287 (n=3188)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4651 (IC base=+0.266)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.718` → IC=+0.268 (n=3930)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.718 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` < `0.0989` → IC=+0.270 (n=3300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0989 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` > `0.293` → IC=+0.284 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.293 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` < `1.5659` → IC=+0.270 (n=1535)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5659 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` > `2.6526` → IC=+0.273 (n=1163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6526 (IC base=+0.266)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.271 (n=2528)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.266)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.274 (n=1262)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.266)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.174 (n=1366)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0033 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.0816` → IC=+0.146 (n=1363)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.0816 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=4270)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.3033` → IC=+0.202 (n=3655)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3033 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.3399` → IC=+0.200 (n=1278)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3399 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.27` → IC=+0.169 (n=855)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 9.27 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.635` → IC=+0.155 (n=1363)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.635 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `1.2254` → IC=+0.147 (n=1363)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.2254 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2719` → IC=+0.190 (n=572)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2719 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.1654` → IC=+0.143 (n=3538)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.1654 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.5201` → IC=+0.146 (n=3591)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.5201 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `290.0` → IC=+0.153 (n=2649)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 290.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.172 (n=3183)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.006 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.0828` → IC=+0.175 (n=1206)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0828 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=1335)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` < `0.6808` → IC=+0.192 (n=3616)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.6808 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.1518` → IC=+0.161 (n=3575)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1518 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.205` → IC=+0.150 (n=3685)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 6.205 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `1.0448` → IC=+0.156 (n=3182)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.0448 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.2214` → IC=+0.195 (n=660)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2214 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.437` → IC=+0.150 (n=3505)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.437 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `1.7747` → IC=+0.152 (n=2336)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.7747 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.147 (n=4696)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `212.0` → IC=+0.179 (n=1140)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 212.0 (IC base=+0.146)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0133` → IC=+0.236 (n=1383)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0133 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=4352)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.298 (n=1535)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.973` → IC=+0.313 (n=925)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.973 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.2058` → IC=+0.232 (n=1105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2058 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.7509` → IC=+0.238 (n=1840)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7509 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.228 (n=5036)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `1902.6696` → IC=+0.232 (n=1879)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1902.6696 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.250 (n=3532)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0112 (IC base=+0.245)

- **PATRÓN** `drift_60min` |x|≤ `0.1839` → IC=+0.260 (n=1766)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1839 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.263 (n=1525)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.249 (n=1822)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.0667` → IC=+0.300 (n=1340)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0667 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.968` → IC=+0.303 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.968 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.3465` → IC=+0.301 (n=605)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3465 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `2.1705` → IC=+0.258 (n=2585)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1705 (IC base=+0.245)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.248 (n=1949)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `1993.6256` → IC=+0.257 (n=1337)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1993.6256 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.249 (n=3417)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.245)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.191 (n=1439)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0039 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.3516` → IC=+0.146 (n=3790)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3516 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=4475)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.8799` → IC=+0.268 (n=1436)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8799 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.1477` → IC=+0.167 (n=2121)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1477 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.187` → IC=+0.167 (n=861)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 9.187 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.8584` → IC=+0.153 (n=2871)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8584 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.278` → IC=+0.200 (n=574)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.278 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.5166` → IC=+0.156 (n=1853)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.5166 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `2.1517` → IC=+0.143 (n=1908)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.1517 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `5836.8126` → IC=+0.233 (n=1952)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5836.8126 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.142 (n=2811)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 85.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0082` → IC=+0.169 (n=3642)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0082 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.4562` → IC=+0.159 (n=3641)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.4562 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=1341)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.5689` → IC=+0.214 (n=3204)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5689 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `0.1644` → IC=+0.163 (n=3462)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1644 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.014` → IC=+0.153 (n=730)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 9.014 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.007` → IC=+0.154 (n=3169)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 3.007 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.8545` → IC=+0.164 (n=2429)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8545 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.293` → IC=+0.209 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.293 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.523` → IC=+0.159 (n=3152)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.523 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `6734.0692` → IC=+0.215 (n=1214)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6734.0692 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.172 (n=1231)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 57.0 (IC base=+0.151)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.155 (n=1461)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0129 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.148 (n=3104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 11.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.697` → IC=+0.255 (n=2920)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.697 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `1.0393` → IC=+0.203 (n=708)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0393 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.242` → IC=+0.270 (n=1116)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.242 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `1.2118` → IC=+0.125 (n=4378)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.2118 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` < `0.1008` → IC=+0.121 (n=4167)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1008 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.129 (n=550)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `2.4914` → IC=+0.123 (n=4273)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.4914 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2474.7486` → IC=+0.220 (n=1985)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2474.7486 (IC base=+0.119)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.160 (n=3602)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0111 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.1423` → IC=+0.154 (n=1364)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1423 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.173 (n=1934)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 15.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.5375` → IC=+0.247 (n=3599)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5375 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.2223` → IC=+0.154 (n=3784)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.2223 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.048` → IC=+0.162 (n=3972)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 3.048 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.6383` → IC=+0.156 (n=1364)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6383 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2303` → IC=+0.200 (n=719)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2303 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.4363` → IC=+0.165 (n=1301)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.4363 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.4772` → IC=+0.142 (n=1301)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.4772 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `2653.0738` → IC=+0.223 (n=1364)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2653.0738 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.152 (n=3920)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 48.0 (IC base=+0.138)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.256 (n=4006)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.242 (n=4191)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.241 (n=2681)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` > `0.9882` → IC=+0.307 (n=1336)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9882 (IC base=+0.236)

- **PATRÓN** `dist_vwap_pct` > `0.2017` → IC=+0.250 (n=2030)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2017 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.051` → IC=+0.294 (n=712)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.051 (IC base=+0.236)

- **PATRÓN** `volumen_regimen` < `1.2144` → IC=+0.236 (n=4006)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2144 (IC base=+0.236)

- **PATRÓN** `volumen_regimen` > `0.6435` → IC=+0.243 (n=4007)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6435 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.0791` → IC=+0.253 (n=1598)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0791 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.505` → IC=+0.254 (n=1308)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.505 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `3003.3623` → IC=+0.238 (n=1336)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3003.3623 (IC base=+0.236)

- **PATRÓN** `sigma_h` > `0.0249` → IC=+0.270 (n=1391)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0249 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.250 (n=3932)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.244 (n=4193)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` < `0.1351` → IC=+0.307 (n=1835)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1351 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` > `1.1697` → IC=+0.244 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1697 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` < `0.2291` → IC=+0.249 (n=4026)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2291 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.011` → IC=+0.278 (n=785)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.011 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` < `0.7156` → IC=+0.247 (n=1835)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7156 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` > `1.2196` → IC=+0.265 (n=1391)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2196 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` > `0.2863` → IC=+0.310 (n=572)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2863 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `1.4339` → IC=+0.248 (n=3957)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4339 (IC base=+0.244)

- **PATRÓN** `libro_liquidez` > `2989.268` → IC=+0.245 (n=1390)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2989.268 (IC base=+0.244)

### GBM_LATE_5M
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.239 (n=2392)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.5362` → IC=+0.232 (n=7170)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5362 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.231 (n=7221)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `0.9296` → IC=+0.260 (n=2391)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9296 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` < `0.9421` → IC=+0.225 (n=5876)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9421 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.464` → IC=+0.231 (n=2384)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.464 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` < `0.7082` → IC=+0.230 (n=2237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7082 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` > `0.8821` → IC=+0.223 (n=3389)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8821 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` < `0.1043` → IC=+0.224 (n=6717)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1043 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.1652` → IC=+0.230 (n=2007)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1652 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` < `1.4483` → IC=+0.235 (n=2352)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4483 (IC base=+0.223)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.227 (n=5147)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `3737.5847` → IC=+0.230 (n=4780)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3737.5847 (IC base=+0.223)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.231 (n=1690)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.5327` → IC=+0.219 (n=5067)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5327 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.221 (n=1973)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.224 (n=2265)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` < `0.7292` → IC=+0.217 (n=5069)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7292 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.6984` → IC=+0.220 (n=848)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6984 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` < `0.1872` → IC=+0.205 (n=4328)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1872 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.745` → IC=+0.224 (n=4590)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.745 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` < `1.0971` → IC=+0.215 (n=4081)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0971 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` < `0.098` → IC=+0.213 (n=4675)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.098 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.5312` → IC=+0.215 (n=2195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5312 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.1879` → IC=+0.221 (n=2262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1879 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.238 (n=2253)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.211)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.279 (n=831)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.270)

- **PATRÓN** `drift_60min` |x|≤ `0.0855` → IC=+0.302 (n=316)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0855 (IC base=+0.270)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.283 (n=483)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.270)

- **PATRÓN** `ibs_20min` < `0.1414` → IC=+0.295 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1414 (IC base=+0.270)

- **PATRÓN** `dist_vwap_pct` < `0.2003` → IC=+0.281 (n=871)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2003 (IC base=+0.270)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.129` → IC=+0.296 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.129 (IC base=+0.270)

- **PATRÓN** `volumen_regimen` < `1.2271` → IC=+0.275 (n=945)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2271 (IC base=+0.270)

- **PATRÓN** `volumen_regimen` > `0.8769` → IC=+0.288 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8769 (IC base=+0.270)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.341 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.270)

- **PATRÓN** `volumen_spike_ratio` < `2.4917` → IC=+0.278 (n=940)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4917 (IC base=+0.270)

- **PATRÓN** `libro_liquidez` > `12915.1097` → IC=+0.282 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12915.1097 (IC base=+0.270)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.265 (n=513)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.3876` → IC=+0.188 (n=1537)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.3876 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=567)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.179 (n=577)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 5.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` < `0.1382` → IC=+0.194 (n=678)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.1382 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` > `0.7` → IC=+0.188 (n=139)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.7 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.106` → IC=+0.197 (n=1346)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 4.106 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` < `1.2377` → IC=+0.184 (n=1537)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 1.2377 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.1521` → IC=+0.190 (n=469)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.1521 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` < `1.4126` → IC=+0.191 (n=510)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.4126 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `2.1732` → IC=+0.178 (n=693)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 2.1732 (IC base=+0.174)

- **PATRÓN** `libro_liquidez` > `14608.6008` → IC=+0.175 (n=697)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 14608.6008 (IC base=+0.174)

- **PATRÓN** `ballena_activa_n` < `696.0` → IC=+0.187 (n=1492)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 696.0 (IC base=+0.174)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.221 (n=932)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0078 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.6119` → IC=+0.214 (n=1043)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6119 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.229 (n=959)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` < `0.711` → IC=+0.212 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.711 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `0.9934` → IC=+0.251 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9934 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.281` → IC=+0.242 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.281 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` < `0.3529` → IC=+0.209 (n=1240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.3529 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.2044` → IC=+0.241 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2044 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` < `3.3613` → IC=+0.208 (n=1039)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.3613 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `1.7942` → IC=+0.215 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7942 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `2397.6695` → IC=+0.227 (n=695)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2397.6695 (IC base=+0.208)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.215 (n=1059)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `0.2025` → IC=+0.289 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2025 (IC base=+0.260)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.241` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.241 (IC base=+0.260)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.278` → IC=+0.257 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.278 (IC base=+0.260)

- **PATRÓN** `volumen_pendiente_norm` < `0.1317` → IC=+0.306 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1317 (IC base=+0.260)

- **PATRÓN** `volumen_spike_ratio` < `1.6141` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6141 (IC base=+0.260)

- **PATRÓN** `volumen_spike_ratio` > `1.8074` → IC=+0.276 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8074 (IC base=+0.260)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.333 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.260)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0086` → IC=+0.221 (n=1933)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0086 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.4696` → IC=+0.219 (n=1932)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4696 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.234 (n=678)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` < `0.4713` → IC=+0.222 (n=1288)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4713 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.1451` → IC=+0.213 (n=1932)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1451 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` < `0.4078` → IC=+0.224 (n=1948)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4078 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.972` → IC=+0.220 (n=1757)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.972 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` < `0.8685` → IC=+0.216 (n=1288)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8685 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` < `0.1011` → IC=+0.214 (n=1790)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1011 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.403` → IC=+0.231 (n=629)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.403 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.4937` → IC=+0.211 (n=1684)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4937 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.211 (n=1939)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0085` → IC=+0.217 (n=1552)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0085 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.5101` → IC=+0.222 (n=1552)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5101 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.213 (n=579)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.218 (n=1114)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `0.0847` → IC=+0.213 (n=1552)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0847 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `0.6767` → IC=+0.215 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6767 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` < `0.4215` → IC=+0.208 (n=1675)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4215 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.281` → IC=+0.212 (n=1413)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.281 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` < `1.2588` → IC=+0.214 (n=1552)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2588 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` > `0.7217` → IC=+0.208 (n=1387)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7217 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.0715` → IC=+0.231 (n=642)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0715 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `1.5076` → IC=+0.211 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5076 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `1.7739` → IC=+0.209 (n=1013)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7739 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.209 (n=2050)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `7832.992` → IC=+0.215 (n=1035)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7832.992 (IC base=+0.207)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.209 (n=1542)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 96.0 (IC base=+0.207)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.227 (n=845)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.213)

- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.221 (n=575)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.239 (n=1192)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.213)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.214 (n=1164)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `0.9855` → IC=+0.295 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9855 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` > `1.1073` → IC=+0.244 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1073 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.218` → IC=+0.249 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.218 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` < `0.6428` → IC=+0.246 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6428 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` > `1.2457` → IC=+0.213 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2457 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` < `0.1056` → IC=+0.216 (n=1162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1056 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.2732` → IC=+0.230 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2732 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `2.1576` → IC=+0.223 (n=1087)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1576 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.222 (n=1485)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `4456.3994` → IC=+0.246 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4456.3994 (IC base=+0.213)

- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.261 (n=629)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.249)

- **PATRÓN** `drift_60min` |x|≤ `0.6875` → IC=+0.263 (n=942)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6875 (IC base=+0.249)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.249 (n=875)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.249)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.270 (n=646)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.249)

- **PATRÓN** `ibs_20min` < `0.7347` → IC=+0.273 (n=942)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7347 (IC base=+0.249)

- **PATRÓN** `dist_vwap_pct` > `0.6006` → IC=+0.252 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6006 (IC base=+0.249)

- **PATRÓN** `dist_vwap_pct` < `0.3374` → IC=+0.261 (n=833)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3374 (IC base=+0.249)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.988` → IC=+0.267 (n=892)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.988 (IC base=+0.249)

- **PATRÓN** `volumen_regimen` < `0.6688` → IC=+0.266 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6688 (IC base=+0.249)

- **PATRÓN** `volumen_pendiente_norm` < `0.1037` → IC=+0.261 (n=843)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1037 (IC base=+0.249)

- **PATRÓN** `volumen_spike_ratio` > `2.1901` → IC=+0.276 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1901 (IC base=+0.249)

- **PATRÓN** `libro_liquidez` > `4596.385` → IC=+0.282 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4596.385 (IC base=+0.249)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.281 (n=832)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.249)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.150 (n=857)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0041 (IC base=+0.060)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.187 (n=1655)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.75 (IC base=+0.060)

- **PATRÓN** `dist_vwap_pct` > `0.1542` → IC=+0.147 (n=1181)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.1542 (IC base=+0.060)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.425` → IC=+0.138 (n=536)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 10.425 (IC base=+0.060)

- **PATRÓN** `ibs_20min` < `0.5919` → IC=+0.164 (n=1870)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.5919 (IC base=+0.077)

- **PATRÓN** `volumen_pendiente_norm` > `0.1511` → IC=+0.177 (n=518)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1511 (IC base=+0.077)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.5412` → IC=-0.122 (n=329)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5412
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=670)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.181 (n=261)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0029 (IC base=+0.066)

- **PATRÓN** `ibs_20min` > `0.5412` → IC=+0.159 (n=670)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.5412 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` > `0.1285` → IC=+0.166 (n=348)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1285 (IC base=+0.066)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.129 (n=311)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0036 (IC base=+0.053)

- **PATRÓN** `ibs_20min` < `0.0659` → IC=+0.247 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0659 (IC base=+0.053)

- **PATRÓN** `volumen_pendiente_norm` > `0.071` → IC=+0.142 (n=297)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.071 (IC base=+0.053)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` < `0.5189` → IC=-0.121 (n=341)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5189
  - _Potencial_: sin este filtro IC_bueno=+0.160 (n=695)

- **FILTRO** `ibs_20min` > `0.6307` → IC=-0.149 (n=183)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6307
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=550)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.154 (n=359)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0043 (IC base=+0.064)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.122 (n=405)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 15.0 (IC base=+0.064)

- **PATRÓN** `ibs_20min` > `0.9259` → IC=+0.258 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9259 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` > `0.1341` → IC=+0.160 (n=371)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1341 (IC base=+0.064)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.755` → IC=+0.182 (n=168)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 11.755 (IC base=+0.064)

- **PATRÓN** `ibs_20min` < `0.0953` → IC=+0.279 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0953 (IC base=+0.042)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.9861` → IC=+0.199 (n=290)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.9861 (IC base=+0.035)

- **PATRÓN** `dist_vwap_pct` > `0.7456` → IC=+0.165 (n=204)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.7456 (IC base=+0.035)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.168 (n=378)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.01 (IC base=+0.097)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.190 (n=543)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.5 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.982` → IC=+0.266 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.982 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` > `1.126` → IC=+0.191 (n=179)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 1.126 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` > `0.1089` → IC=+0.173 (n=200)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1089 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` > `1.4597` → IC=+0.139 (n=505)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.4597 (IC base=+0.097)

### GBM_LATE_60M#XRP#60min
- **PATRÓN** `sigma_h` < `0.0135` → IC=+0.344 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0135 (IC base=+0.308)

- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.300 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.308)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.447 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.308)

- **PATRÓN** `ibs_20min` < `0.118` → IC=+0.382 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.118 (IC base=+0.308)

- **PATRÓN** `volumen_regimen` > `0.9567` → IC=+0.340 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9567 (IC base=+0.308)

- **PATRÓN** `volumen_spike_ratio` < `1.5212` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5212 (IC base=+0.308)

- **PATRÓN** `volumen_spike_ratio` > `2.0601` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.0601 (IC base=+0.308)

- **PATRÓN** `libro_liquidez` > `37.2` → IC=+0.340 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 37.2 (IC base=+0.308)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` < `0.006` → IC=-0.247 (n=200)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.006
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=203)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.310 (n=98)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=305)

- **FILTRO** `dist_vwap_pct` > `0.2422` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2422
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=388)

- **FILTRO** `sigma_h` < `0.007` → IC=-0.286 (n=269)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=90)

- **FILTRO** `dist_vwap_pct` > `0.4497` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4497
  - _Potencial_: sin este filtro IC_bueno=-0.263 (n=335)

- **FILTRO** `sigma_ewma_delta_pct` > `9.318` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.318
  - _Potencial_: sin este filtro IC_bueno=-0.264 (n=329)

- **FILTRO** `volumen_pendiente_norm` > `0.046` → IC=-0.375 (n=30)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.046
  - _Potencial_: sin este filtro IC_bueno=-0.251 (n=235)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.312 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.234 (n=92)

- **FILTRO** `ibs_20min` < `0.1017` → IC=-0.286 (n=40)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1017
  - _Potencial_: sin este filtro IC_bueno=-0.238 (n=82)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.278 (n=70)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.222 (n=77)

- **FILTRO** `ibs_20min` > `0.7502` → IC=-0.265 (n=49)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7502
  - _Potencial_: sin este filtro IC_bueno=-0.240 (n=98)

- **FILTRO** `volumen_regimen` > `0.805` → IC=-0.316 (n=36)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.226 (n=111)

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

- **FILTRO** `hora_utc` > `11.0` → IC=-0.361 (n=63)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=74)

- **FILTRO** `volumen_spike_ratio` < `1.4481` → IC=-0.389 (n=25)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.4481
  - _Potencial_: sin este filtro IC_bueno=-0.285 (n=77)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.298 (n=122)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `5.0` → IC=-0.344 (n=43)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=101)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.250 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.241 (n=114)

- **FILTRO** `sigma_ewma_delta_pct` > `4.378` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.378
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=50)

- **FILTRO** `volumen_regimen` < `0.9175` → IC=-0.457 (n=21)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9175
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=45)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=43)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.2365` → IC=-0.150 (n=312)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2365
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=939)

- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.255 (n=366)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0079 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.204 (n=319)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` > `0.6818` → IC=+0.198 (n=807)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.6818 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` > `0.8341` → IC=+0.313 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8341 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.618` → IC=+0.180 (n=448)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 3.618 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.407` → IC=+0.162 (n=821)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 8.407 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` < `0.6242` → IC=+0.190 (n=269)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.6242 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` < `0.0678` → IC=+0.189 (n=605)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` < 0.0678 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` < `1.3996` → IC=+0.206 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3996 (IC base=+0.162)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.7306` → IC=-0.171 (n=77)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7306
  - _Potencial_: sin este filtro IC_bueno=+0.133 (n=232)

- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.154 (n=79)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0065 (IC base=+0.056)

- **PATRÓN** `ibs_20min` > `0.7306` → IC=+0.133 (n=232)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` > 0.7306 (IC base=+0.056)

- **PATRÓN** `dist_vwap_pct` > `0.6482` → IC=+0.217 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6482 (IC base=+0.056)

- **PATRÓN** `ibs_20min` < `0.2418` → IC=+0.133 (n=431)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.2418 (IC base=+0.075)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `ibs_20min` > `0.2338` → IC=-0.152 (n=113)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2338
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=340)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.136 (n=174)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0045 (IC base=+0.133)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.174 (n=87)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.007 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.111` → IC=+0.136 (n=116)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.111 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.173 (n=96)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 18.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.146 (n=94)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 6.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` > `0.798` → IC=+0.177 (n=233)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.798 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `0.7852` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.7852 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.1055` → IC=+0.161 (n=213)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.1055 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.232` → IC=+0.154 (n=270)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 9.232 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.6229` → IC=+0.185 (n=87)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.6229 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` > `1.1865` → IC=+0.174 (n=87)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 1.1865 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` < `0.052` → IC=+0.190 (n=217)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.052 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `1.7116` → IC=+0.181 (n=155)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.7116 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=221)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.315` → IC=+0.131 (n=101)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 9.315 (IC base=+0.001)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.0526` → IC=-0.226 (n=111)

  - _Acción_: SKIP cuando `ibs_20min` > 0.0526
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=112)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.281 (n=322)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.263)

- **PATRÓN** `ibs_20min` > `0.8571` → IC=+0.307 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8571 (IC base=+0.263)

- **PATRÓN** `dist_vwap_pct` > `0.7432` → IC=+0.393 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7432 (IC base=+0.263)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.992` → IC=+0.351 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.992 (IC base=+0.263)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.292 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.263)

- **PATRÓN** `volumen_pendiente_norm` > `0.092` → IC=+0.315 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.092 (IC base=+0.263)

- **PATRÓN** `volumen_spike_ratio` < `1.4833` → IC=+0.326 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4833 (IC base=+0.263)

- **PATRÓN** `volumen_spike_ratio` > `2.3741` → IC=+0.295 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3741 (IC base=+0.263)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.268 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.263)

- **PATRÓN** `libro_liquidez` > `684.9428` → IC=+0.263 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 684.9428 (IC base=+0.263)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.333 (n=178)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3645` → IC=+0.339 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3645 (IC base=+0.336)

- **PATRÓN** `elapsed_s` > `209.2` → IC=+0.393 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 209.2 (IC base=+0.336)

- **PATRÓN** `drift_15min` |x|≤ `1.0369` → IC=+0.375 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0369 (IC base=+0.336)

- **PATRÓN** `drift_60min` |x|≤ `0.9795` → IC=+0.377 (n=136)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9795 (IC base=+0.336)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.392 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.336)

- **PATRÓN** `ballena_activa_n` < `1044.0` → IC=+0.417 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1044.0 (IC base=+0.336)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3499` → IC=+0.297 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3499 (IC base=+0.292)

- **PATRÓN** `elapsed_s` > `230.5` → IC=+0.365 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 230.5 (IC base=+0.292)

- **PATRÓN** `drift_15min` |x|≤ `2.3354` → IC=+0.332 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3354 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.9045` → IC=+0.317 (n=129)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9045 (IC base=+0.292)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.333 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.292)

- **PATRÓN** `ballena_activa_n` < `1330.0` → IC=+0.380 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1330.0 (IC base=+0.292)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.333 (n=178)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3645` → IC=+0.339 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3645 (IC base=+0.336)

- **PATRÓN** `elapsed_s` > `209.2` → IC=+0.393 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 209.2 (IC base=+0.336)

- **PATRÓN** `drift_15min` |x|≤ `1.0369` → IC=+0.375 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0369 (IC base=+0.336)

- **PATRÓN** `drift_60min` |x|≤ `0.9795` → IC=+0.377 (n=136)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9795 (IC base=+0.336)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.392 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.336)

- **PATRÓN** `ballena_activa_n` < `1044.0` → IC=+0.417 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1044.0 (IC base=+0.336)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3499` → IC=+0.297 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3499 (IC base=+0.292)

- **PATRÓN** `elapsed_s` > `230.5` → IC=+0.365 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 230.5 (IC base=+0.292)

- **PATRÓN** `drift_15min` |x|≤ `2.3354` → IC=+0.332 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3354 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.9045` → IC=+0.317 (n=129)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9045 (IC base=+0.292)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.333 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.292)

- **PATRÓN** `ballena_activa_n` < `1330.0` → IC=+0.380 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1330.0 (IC base=+0.292)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=287)

- **FILTRO** `py_entrada` < `0.415` → IC=-0.171 (n=71)

  - _Acción_: SKIP cuando `py_entrada` < 0.415
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=232)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=287)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=1339)

### LIQUIDACIONES_15M#BNB#15min
- **PATRÓN** `liq_n` > `2.0` → IC=+0.199 (n=71)

  - _Acción_: Kelly boost +0.99€ cuando `liq_n` > 2.0 (IC base=+0.093)

- **PATRÓN** `liq_usd_total` > `2348.39` → IC=+0.211 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 2348.39 (IC base=+0.093)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.135 (n=72)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` > 0.5 (IC base=+0.093)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.141 (n=101)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.03 (IC base=+0.093)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `11686.6395` → IC=-0.167 (n=40)

  - _Acción_: SKIP cuando `libro_liquidez` < 11686.6395
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=120)

### LIQUIDACIONES_15M#DOGE#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.180 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.188 (n=75)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=83)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.188 (n=75)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 10.0 (IC base=+0.100)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.147 (n=83)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` > 0.5 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `1868.861` → IC=+0.167 (n=34)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 1868.861 (IC base=+0.100)

- **PATRÓN** `ballena_activa_n` < `4.0` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 4.0 (IC base=+0.100)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.188 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=31)

- **FILTRO** `py_entrada` < `0.425` → IC=-0.309 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.425
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=42)

- **PATRÓN** `liq_usd_total` > `4633.28` → IC=+0.121 (n=159)

  - _Acción_: Kelly boost +0.61€ cuando `liq_usd_total` > 4633.28 (IC base=+0.059)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=27)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=275)

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
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=4185)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=230)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=187)

- **FILTRO** `ballena_activa_n` > `17.0` → IC=-0.124 (n=107)

  - _Acción_: SKIP cuando `ballena_activa_n` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=110)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.214 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.010)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=22)

- **FILTRO** `libro_liquidez` < `13988.6712` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 13988.6712
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.132 (n=286)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` < 0.495 (IC base=+0.021)

### LIQUIDACIONES_5M#DOGE#5min
- **PATRÓN** `liq_n` > `3.0` → IC=+0.333 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 3.0 (IC base=+0.202)

- **PATRÓN** `liq_usd_total` > `3798.53` → IC=+0.330 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 3798.53 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.216 (n=107)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.233 (n=73)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.210 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `3279.111` → IC=+0.223 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3279.111 (IC base=+0.202)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.222 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.202)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=1634)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=1588)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.286 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=747)

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
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=1117)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=1117)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=1478)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=1478)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=342)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=342)

- **FILTRO** `py_entrada` < `0.43` → IC=-0.143 (n=113)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=244)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.136 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=402)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=451)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=329)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=431)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=431)

- **FILTRO** `libro_liquidez` < `693.7144` → IC=-0.130 (n=152)

  - _Acción_: SKIP cuando `libro_liquidez` < 693.7144
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=309)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=418)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.125 (n=3379)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=8779)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.133 (n=115)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=135)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=55)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.153 (n=399)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=978)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.149 (n=317)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=861)

- **PATRÓN** `py_entrada` < `0.51` → IC=+0.145 (n=412)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.51 (IC base=-0.009)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.134 (n=192)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=433)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.121 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=735)

- **PATRÓN** `py_entrada` < `0.51` → IC=+0.131 (n=323)

  - _Acción_: Kelly boost +0.65€ cuando `py_entrada` < 0.51 (IC base=-0.019)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.138 (n=346)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=734)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.124 (n=751)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=393)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.133 (n=608)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=700)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.178 (n=8987)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=27993)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.169 (n=9366)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=29007)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.199 (n=1674)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=5220)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.143 (n=2294)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=4512)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.137 (n=3203)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.5 (IC base=+0.016)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.178 (n=1262)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=3804)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.176 (n=1316)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=4056)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.195 (n=1707)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.090 (n=5279)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.132 (n=2119)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` > 1.0 (IC base=+0.031)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `ibs_20min` < `0.7658` → IC=-0.152 (n=1238)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7658
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=3715)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.177 (n=1350)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=4130)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.162 (n=1718)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=5195)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=2452)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2376)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=973)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=3257)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=4209)

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
  - _Potencial_: sin este filtro IC_bueno=-0.000 (n=1181)

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
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=371)

- **FILTRO** `drift_20min_pct` |x|> `0.2017` → IC=-0.131 (n=120)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.2017
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=364)

- **FILTRO** `libro_liquidez` < `3247.9585` → IC=-0.183 (n=159)

  - _Acción_: SKIP cuando `libro_liquidez` < 3247.9585
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=325)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=983)

- **FILTRO** `ibs_20min` > `0.875` → IC=-0.131 (n=602)

  - _Acción_: SKIP cuando `ibs_20min` > 0.875
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=622)

- **FILTRO** `libro_liquidez` < `1611.167` → IC=-0.149 (n=306)

  - _Acción_: SKIP cuando `libro_liquidez` < 1611.167
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=918)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.136 (n=25044)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=56972)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.301 (n=20020)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=61996)

- **FILTRO** `ibs_7min` < `0.7273` → IC=-0.225 (n=27012)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7273
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=55004)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.155 (n=27533)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=54483)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.246 (n=25466)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=77204)

- **FILTRO** `ibs_7min` > `0.2788` → IC=-0.183 (n=25660)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2788
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=77010)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.161 (n=3509)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=11271)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.321 (n=3687)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=11093)

- **FILTRO** `ibs_7min` < `0.7078` → IC=-0.256 (n=4877)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7078
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=9903)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.279 (n=4297)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=13484)

- **FILTRO** `ibs_7min` > `0.7652` → IC=-0.211 (n=4445)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7652
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=13336)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.125 (n=3257)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=10285)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.267 (n=3322)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=10220)

- **FILTRO** `ibs_7min` < `0.711` → IC=-0.216 (n=3385)

  - _Acción_: SKIP cuando `ibs_7min` < 0.711
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=10157)

- **FILTRO** `ballena_activa_n` > `157.0` → IC=-0.206 (n=3380)

  - _Acción_: SKIP cuando `ballena_activa_n` > 157.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=10162)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.268 (n=3153)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=10710)

- **FILTRO** `ibs_7min` > `0.2644` → IC=-0.193 (n=3465)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2644
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=10398)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.179 (n=3452)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=10411)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.169 (n=3373)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=10796)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.329 (n=3400)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=10769)

- **FILTRO** `ibs_7min` < `0.2857` → IC=-0.255 (n=4657)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=9512)

- **FILTRO** `ballena_activa_n` > `4.0` → IC=-0.174 (n=3422)

  - _Acción_: SKIP cuando `ballena_activa_n` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=10747)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.261 (n=4518)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=14286)

- **FILTRO** `ibs_7min` > `0.7222` → IC=-0.186 (n=4699)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7222
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=14105)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.276 (n=3004)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=10216)

- **FILTRO** `ibs_7min` < `0.7119` → IC=-0.203 (n=3305)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7119
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=9915)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.195 (n=3299)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=9921)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.259 (n=3204)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=10530)

- **FILTRO** `ibs_7min` > `0.2719` → IC=-0.180 (n=3432)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2719
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=10302)

- **FILTRO** `ballena_activa_n` > `23.0` → IC=-0.168 (n=3420)

  - _Acción_: SKIP cuando `ballena_activa_n` > 23.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=10314)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.302 (n=3183)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=9883)

- **FILTRO** `ibs_7min` < `0.2941` → IC=-0.234 (n=4291)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2941
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=8775)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.218 (n=3213)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=9853)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.200 (n=4710)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=15172)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.134 (n=4278)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=8961)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.315 (n=3259)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=9980)

- **FILTRO** `ibs_7min` < `0.72` → IC=-0.231 (n=4364)

  - _Acción_: SKIP cuando `ibs_7min` < 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=8875)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.196 (n=3303)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=9936)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.231 (n=4555)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=14051)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=121)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.163 (n=304)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1025)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=1314)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.167 (n=181)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=653)

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
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=923)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.127 (n=234)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=279)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=463)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.216 (n=192)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=592)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.124 (n=107)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=677)

- **FILTRO** `libro_liquidez` < `3306.8101` → IC=-0.146 (n=196)

  - _Acción_: SKIP cuando `libro_liquidez` < 3306.8101
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=588)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=56)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=548)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4306` → IC=+0.145 (n=748)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.73€ cuando `delta_ratio` |x|> 0.4306 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.128 (n=1494)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 14.0 (IC base=+0.124)

- **PATRÓN** `total_vol_5m` < `446.7366` → IC=+0.167 (n=550)

  - _Acción_: Kelly boost +0.83€ cuando `total_vol_5m` < 446.7366 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `3657.1308` → IC=+0.135 (n=748)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 3657.1308 (IC base=+0.124)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.187 (n=193)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 14.0 (IC base=+0.141)

- **PATRÓN** `total_vol_5m` < `499.459` → IC=+0.159 (n=382)

  - _Acción_: Kelly boost +0.79€ cuando `total_vol_5m` < 499.459 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.157 (n=263)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 9.0 (IC base=+0.141)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3992` → IC=+0.128 (n=345)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.64€ cuando `delta_ratio` |x|> 0.3992 (IC base=+0.116)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.153 (n=145)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 4.0 (IC base=+0.116)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4162` → IC=+0.170 (n=204)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.85€ cuando `delta_ratio` |x|> 0.4162 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.153 (n=283)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.127)

- **PATRÓN** `total_vol_5m` < `699.4537` → IC=+0.165 (n=270)

  - _Acción_: Kelly boost +0.83€ cuando `total_vol_5m` < 699.4537 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.183 (n=102)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 58.0 (IC base=+0.127)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4183` → IC=+0.198 (n=187)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.99€ cuando `delta_ratio` |x|> 0.4183 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.173 (n=111)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 5.0 (IC base=+0.136)

- **PATRÓN** `total_vol_5m` < `4761.643` → IC=+0.179 (n=188)

  - _Acción_: Kelly boost +0.89€ cuando `total_vol_5m` < 4761.643 (IC base=+0.136)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `13.0` → IC=+0.133 (n=298)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 13.0 (IC base=+0.100)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.132 (n=210)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.100)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `6.3582` → IC=-0.218 (n=83)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 6.3582
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=163)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.159 (n=323)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0046 (IC base=-0.026)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `pct_vs_K` |x|> `4.2688` → IC=-0.237 (n=74)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.2688
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=225)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.262 (n=99)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.002)

- **PATRÓN** `pct_vs_K` |x|≤ `1.9196` → IC=+0.203 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 1.9196 (IC base=+0.002)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `pct_vs_K` |x|> `6.4329` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 6.4329
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=59)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `T_h` < `73.7179` → IC=-0.172 (n=62)

  - _Acción_: SKIP cuando `T_h` < 73.7179
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=126)

### PRICE_TARGET_GBM#SOL#reach
- **FILTRO** `sigma_h` < `0.0164` → IC=-0.192 (n=24)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0164
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `T_h` < `146.0708` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `T_h` < 146.0708
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `T_h` < `113.7298` → IC=-0.250 (n=562)

  - _Acción_: SKIP cuando `T_h` < 113.7298
  - _Potencial_: sin este filtro IC_bueno=-0.226 (n=290)

- **FILTRO** `sigma_h` < `0.0056` → IC=-0.187 (n=196)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0056
  - _Potencial_: sin este filtro IC_bueno=-0.096 (n=590)

- **FILTRO** `pct_vs_K` |x|> `2.9641` → IC=-0.379 (n=196)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9641
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=590)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `49.2927` → IC=-0.235 (n=209)

  - _Acción_: SKIP cuando `T_h` > 49.2927
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=72)

- **FILTRO** `sigma_h` < `0.0075` → IC=-0.170 (n=192)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0075
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=100)

- **FILTRO** `pct_vs_K` |x|> `2.3606` → IC=-0.322 (n=99)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.3606
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=193)

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
- **FILTRO** `sigma_h` < `0.0095` → IC=-0.325 (n=124)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.270 (n=124)

- **FILTRO** `T_h` > `49.9834` → IC=-0.302 (n=185)

  - _Acción_: SKIP cuando `T_h` > 49.9834
  - _Potencial_: sin este filtro IC_bueno=-0.285 (n=63)

- **FILTRO** `sigma_h` < `0.0057` → IC=-0.172 (n=59)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0057
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=180)

- **FILTRO** `pct_vs_K` |x|> `2.7205` → IC=-0.392 (n=81)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.7205
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=158)

- **PATRÓN** `pct_vs_K` |x|≤ `1.89` → IC=+0.164 (n=120)

  - _Acción_: Kelly boost +0.82€ cuando `pct_vs_K` |x|≤ 1.89 (IC base=-0.102)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `sigma_h` < `0.0095` → IC=-0.152 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

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

- **FILTRO** `T_h` < `87.9882` → IC=-0.225 (n=118)

  - _Acción_: SKIP cuando `T_h` < 87.9882
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=119)

- **FILTRO** `sigma_h` < `0.0091` → IC=-0.261 (n=44)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=132)

- **FILTRO** `T_h` > `36.4645` → IC=-0.139 (n=131)

  - _Acción_: SKIP cuando `T_h` > 36.4645
  - _Potencial_: sin este filtro IC_bueno=-0.096 (n=45)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1152` → IC=+0.446 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1152 (IC base=+0.334)

- **PATRÓN** `sigma_h` < `0.013` → IC=+0.345 (n=108)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.013 (IC base=+0.334)

- **PATRÓN** `sigma_h` > `0.013` → IC=+0.345 (n=56)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.013 (IC base=+0.334)

- **PATRÓN** `T_h` < `0.3439` → IC=+0.384 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.3439 (IC base=+0.334)

- **PATRÓN** `T_h` > `0.4704` → IC=+0.357 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4704 (IC base=+0.334)

- **PATRÓN** `dist_50` > `0.4666` → IC=+0.483 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4666 (IC base=+0.334)

- **PATRÓN** `edge` > `0.1` → IC=+0.425 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1 (IC base=+0.391)

- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.405 (n=135)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.391)

- **PATRÓN** `dist_50` > `0.3751` → IC=+0.439 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3751 (IC base=+0.391)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.411 (n=346)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.391)

### RESOLUTION_SNIPER#BTC#sniper
- **PATRÓN** `edge` > `0.1161` → IC=+0.278 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1161 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.265 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.196)

- **PATRÓN** `T_h` < `0.7285` → IC=+0.269 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.7285 (IC base=+0.196)

- **PATRÓN** `T_h` > `1.4804` → IC=+0.235 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4804 (IC base=+0.196)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.274 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.235 (n=66)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.196)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1023` → IC=+0.466 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1023 (IC base=+0.412)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.424 (n=64)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.412)

- **PATRÓN** `T_h` < `1.2028` → IC=+0.439 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.2028 (IC base=+0.412)

- **PATRÓN** `dist_50` > `0.4134` → IC=+0.483 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4134 (IC base=+0.412)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.444 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.412)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.1581` → IC=+0.486 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1581 (IC base=+0.439)

- **PATRÓN** `sigma_h` < `0.0155` → IC=+0.469 (n=63)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0155 (IC base=+0.439)

- **PATRÓN** `T_h` > `0.3968` → IC=+0.460 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.3968 (IC base=+0.439)

- **PATRÓN** `dist_50` > `0.3419` → IC=+0.473 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3419 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.441 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.439)

- **PATRÓN** `edge` > `0.177` → IC=+0.472 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.177 (IC base=+0.464)

- **PATRÓN** `sigma_h` < `0.0157` → IC=+0.475 (n=157)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0157 (IC base=+0.464)

- **PATRÓN** `T_h` > `1.4857` → IC=+0.482 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4857 (IC base=+0.464)

- **PATRÓN** `dist_50` > `0.4568` → IC=+0.493 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4568 (IC base=+0.464)

- **PATRÓN** `hora_utc` < `2.0` → IC=+0.485 (n=63)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 2.0 (IC base=+0.464)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=476)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=511)

- **PATRÓN** `streak_estiramiento` < `0.2938` → IC=+0.139 (n=120)

  - _Acción_: Kelly boost +0.70€ cuando `streak_estiramiento` < 0.2938 (IC base=+0.017)

- **PATRÓN** `streak_estiramiento` < `0.836` → IC=+0.122 (n=353)

  - _Acción_: Kelly boost +0.61€ cuando `streak_estiramiento` < 0.836 (IC base=+0.058)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.122 (n=265)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 29.0 (IC base=+0.058)

### STREAK_FADE_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.136 (n=20)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.495 (IC base=+0.071)

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
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=217)

- **PATRÓN** `streak_estiramiento` < `0.2115` → IC=+0.161 (n=60)

  - _Acción_: Kelly boost +0.81€ cuando `streak_estiramiento` < 0.2115 (IC base=+0.033)

- **PATRÓN** `streak_estiramiento` < `0.5959` → IC=+0.157 (n=176)

  - _Acción_: Kelly boost +0.79€ cuando `streak_estiramiento` < 0.5959 (IC base=+0.085)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.151 (n=167)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 30.0 (IC base=+0.085)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.194 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=95)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=56)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.136 (n=31)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=41)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=826)

### STREAK_FADE_60M
- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=25)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=25)

- **FILTRO** `streak_estiramiento` > `0.6751` → IC=-0.121 (n=56)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.6751
  - _Potencial_: sin este filtro IC_bueno=+0.145 (n=29)

- **PATRÓN** `streak_estiramiento` < `0.5703` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `streak_estiramiento` < 0.5703 (IC base=-0.016)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=1097)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1350)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1244)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=1312)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=5386)

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
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=3204)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.186 (n=2082)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0057 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.2307` → IC=+0.158 (n=6244)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2307 (IC base=+0.132)

- **PATRÓN** `drift_15min` |x|≤ `1.1107` → IC=+0.133 (n=6244)

  - _Acción_: Kelly boost +0.67€ cuando `drift_15min` |x|≤ 1.1107 (IC base=+0.132)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0649` → IC=+0.132 (n=6243)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio_macro` |x|> 0.0649 (IC base=+0.132)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1332` → IC=+0.142 (n=2591)

  - _Acción_: Kelly boost +0.71€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1332 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.143 (n=5789)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 6.0 (IC base=+0.132)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.210 (n=5579)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.181` → IC=+0.231 (n=1167)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.181 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=3352)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `4367.9561` → IC=+0.172 (n=2081)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 4367.9561 (IC base=+0.132)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=2430)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.251 (n=287)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.0769` → IC=+0.248 (n=379)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0769 (IC base=+0.205)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2678` → IC=+0.227 (n=287)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2678 (IC base=+0.205)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2264` → IC=+0.218 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2264 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.232 (n=796)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.205)

- **PATRÓN** `ibs_15` > `0.7058` → IC=+0.275 (n=861)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7058 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `0.387` → IC=+0.220 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.387 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` < `0.5427` → IC=+0.208 (n=972)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5427 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.133` → IC=+0.302 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.133 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=1116)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `11862.3083` → IC=+0.224 (n=574)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11862.3083 (IC base=+0.205)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.165 (n=482)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0047 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.109` → IC=+0.145 (n=730)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.109 (IC base=+0.130)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0863` → IC=+0.135 (n=978)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio_macro` |x|> 0.0863 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.143 (n=776)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 11.0 (IC base=+0.130)

- **PATRÓN** `ibs_15` > `0.4851` → IC=+0.217 (n=1095)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.4851 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` > `0.1236` → IC=+0.142 (n=686)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.1236 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` < `0.6408` → IC=+0.133 (n=1245)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.6408 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.997` → IC=+0.288 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.997 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `6114.254` → IC=+0.169 (n=497)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 6114.254 (IC base=+0.130)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.8462` → IC=+0.144 (n=631)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.72€ cuando `ibs_15` > 0.8462 (IC base=+0.045)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` < `0.0138` → IC=+0.141 (n=695)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0138 (IC base=+0.139)

- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.144 (n=1581)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0119 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.2367` → IC=+0.176 (n=1580)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2367 (IC base=+0.139)

- **PATRÓN** `delta_ratio_macro` |x|> `0.058` → IC=+0.142 (n=1580)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.71€ cuando `delta_ratio_macro` |x|> 0.058 (IC base=+0.139)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.093` → IC=+0.190 (n=492)

  - _Acción_: Kelly boost +0.95€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.093 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.145 (n=1450)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 6.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.141 (n=1461)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 15.0 (IC base=+0.139)

- **PATRÓN** `ibs_15` > `0.5274` → IC=+0.204 (n=1412)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5274 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.2095` → IC=+0.150 (n=718)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.2095 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.8827` → IC=+0.142 (n=1833)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.8827 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.44` → IC=+0.183 (n=361)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 17.44 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `2950.6032` → IC=+0.181 (n=717)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2950.6032 (IC base=+0.139)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `drift_60min` |x|≤ `0.1089` → IC=+0.364 (n=527)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1089 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1497` → IC=+0.379 (n=526)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1497 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.107` → IC=+0.377 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.107 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.372 (n=730)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.7903` → IC=+0.398 (n=789)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7903 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.4149` → IC=+0.383 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4149 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.787` → IC=+0.398 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.787 (IC base=+0.364)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.367 (n=963)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `9641.0136` → IC=+0.383 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9641.0136 (IC base=+0.364)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.368 (n=127)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.366)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2194` → IC=+0.379 (n=172)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2194 (IC base=+0.366)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1453` → IC=+0.401 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1453 (IC base=+0.366)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.384 (n=350)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.366)

- **PATRÓN** `ibs_15` > `0.8112` → IC=+0.387 (n=378)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8112 (IC base=+0.366)

- **PATRÓN** `dist_vwap_pct` > `0.2485` → IC=+0.391 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2485 (IC base=+0.366)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.98` → IC=+0.392 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.98 (IC base=+0.366)

- **PATRÓN** `libro_liquidez` > `15195.4571` → IC=+0.385 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15195.4571 (IC base=+0.366)

- **PATRÓN** `ballena_activa_n` < `412.0` → IC=+0.392 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 412.0 (IC base=+0.366)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.365 (n=412)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.362)

- **PATRÓN** `drift_60min` |x|≤ `0.1062` → IC=+0.363 (n=275)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1062 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0833` → IC=+0.376 (n=368)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0833 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.371 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.379 (n=188)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.362)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.374 (n=189)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.7632` → IC=+0.398 (n=411)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7632 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.1243` → IC=+0.365 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1243 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` < `0.6628` → IC=+0.364 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6628 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.861` → IC=+0.397 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.861 (IC base=+0.362)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.364 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `4286.0807` → IC=+0.368 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4286.0807 (IC base=+0.362)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0108` → IC=-0.235 (n=2007)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0108
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=3898)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.223 (n=2578)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=3327)

- **FILTRO** `libro_liquidez` < `4378.065` → IC=-0.172 (n=3897)

  - _Acción_: SKIP cuando `libro_liquidez` < 4378.065
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=2008)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1411` → IC=+0.215 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1411 (IC base=-0.089)

- **PATRÓN** `ibs_15` > `0.6306` → IC=+0.278 (n=1306)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6306 (IC base=-0.089)

- **PATRÓN** `dist_vwap_pct` > `0.115` → IC=+0.203 (n=768)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.115 (IC base=-0.089)

- **PATRÓN** `dist_vwap_pct` < `0.5827` → IC=+0.199 (n=1387)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5827 (IC base=-0.089)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2294` → IC=+0.271 (n=1907)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2294 (IC base=+0.002)

- **PATRÓN** `ibs_15` < `0.375` → IC=+0.285 (n=5727)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.375 (IC base=+0.002)

- **PATRÓN** `dist_vwap_pct` > `0.6882` → IC=+0.269 (n=800)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6882 (IC base=+0.002)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0736` → IC=-0.244 (n=1921)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0736
  - _Potencial_: sin este filtro IC_bueno=-0.121 (n=1929)

- **FILTRO** `sigma_h` < `0.0039` → IC=-0.215 (n=962)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0039
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=2888)

- **FILTRO** `sigma_ewma_delta_pct` > `22.185` → IC=-0.246 (n=545)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.185
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=3305)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.146 (n=357)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0032 (IC base=+0.064)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2675` → IC=+0.279 (n=156)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2675 (IC base=+0.064)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1446` → IC=+0.277 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1446 (IC base=+0.064)

- **PATRÓN** `ibs_15` > `0.7609` → IC=+0.318 (n=466)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7609 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` > `0.1043` → IC=+0.277 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1043 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` < `0.5244` → IC=+0.284 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5244 (IC base=+0.064)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.895` → IC=+0.139 (n=236)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 21.895 (IC base=+0.064)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0758` → IC=+0.225 (n=78)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0758 (IC base=-0.182)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0902` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0902 (IC base=-0.182)

- **PATRÓN** `ibs_15` < `0.6255` → IC=+0.287 (n=78)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6255 (IC base=-0.182)

- **PATRÓN** `dist_vwap_pct` < `0.0459` → IC=+0.294 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0459 (IC base=-0.182)

- **PATRÓN** `ballena_activa_n` < `393.0` → IC=+0.310 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 393.0 (IC base=-0.182)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.151 (n=856)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.158 (n=655)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0066 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.159` → IC=+0.160 (n=577)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.159 (IC base=+0.146)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3021` → IC=+0.190 (n=517)

  - _Acción_: Kelly boost +0.95€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3021 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.167 (n=470)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 11.0 (IC base=+0.146)

- **PATRÓN** `ibs_15` > `0.5659` → IC=+0.241 (n=655)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5659 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.1197` → IC=+0.150 (n=409)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.1197 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.1604` → IC=+0.147 (n=503)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1604 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.835` → IC=+0.260 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.835 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=856)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `5128.1918` → IC=+0.161 (n=437)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 5128.1918 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.259 (n=985)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.4744` → IC=+0.243 (n=2237)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4744 (IC base=+0.239)

- **PATRÓN** `drift_15min` |x|≤ `0.8178` → IC=+0.254 (n=1968)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.8178 (IC base=+0.239)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2036` → IC=+0.259 (n=1015)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2036 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.246 (n=825)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.242 (n=986)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.239)

- **PATRÓN** `ibs_15` < `0.3879` → IC=+0.271 (n=2236)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3879 (IC base=+0.239)

- **PATRÓN** `dist_vwap_pct` > `0.1632` → IC=+0.255 (n=844)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1632 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.514` → IC=+0.244 (n=967)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.514 (IC base=+0.239)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.2006` → IC=-0.294 (n=352)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.2006
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=1060)

- **FILTRO** `drift_15min` |x|> `0.9949` → IC=-0.302 (n=352)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9949
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=1060)

- **FILTRO** `sigma_ewma_delta_pct` > `6.088` → IC=-0.208 (n=310)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.088
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=1102)

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

- **PATRÓN** `ibs_15` < `0.381` → IC=+0.295 (n=961)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.381 (IC base=-0.025)

- **PATRÓN** `dist_vwap_pct` < `0.4621` → IC=+0.254 (n=1033)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4621 (IC base=-0.025)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1211` → IC=-0.269 (n=832)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1211
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=836)

- **FILTRO** `drift_60min` |x|> `0.1572` → IC=-0.254 (n=416)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1572
  - _Potencial_: sin este filtro IC_bueno=-0.212 (n=1252)

- **FILTRO** `drift_15min` |x|> `1.3082` → IC=-0.282 (n=416)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.3082
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=1252)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.222 (n=1647)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.223)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.223)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0714` → IC=+0.284 (n=1197)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0714 (IC base=-0.008)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1182` → IC=+0.292 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1182 (IC base=-0.008)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.296 (n=1348)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.008)

- **PATRÓN** `dist_vwap_pct` > `0.7717` → IC=+0.335 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7717 (IC base=-0.008)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.135 (n=61)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0068 (IC base=+0.085)

- **PATRÓN** `drift_60min` |x|≤ `0.1126` → IC=+0.128 (n=41)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.1126 (IC base=+0.085)

- **PATRÓN** `drift_15min` |x|≤ `0.7362` → IC=+0.151 (n=61)

  - _Acción_: Kelly boost +0.75€ cuando `drift_15min` |x|≤ 0.7362 (IC base=+0.085)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2386` → IC=+0.150 (n=38)

  - _Acción_: Kelly boost +0.75€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2386 (IC base=+0.085)

- **PATRÓN** `ibs_15` > `0.8358` → IC=+0.300 (n=28)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8358 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` < `0.0974` → IC=+0.203 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0974 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.113` → IC=+0.132 (n=17)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 13.113 (IC base=+0.085)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 49.0 (IC base=+0.085)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.135 (n=61)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0068 (IC base=+0.085)

- **PATRÓN** `drift_60min` |x|≤ `0.1126` → IC=+0.128 (n=41)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.1126 (IC base=+0.085)

- **PATRÓN** `drift_15min` |x|≤ `0.7362` → IC=+0.151 (n=61)

  - _Acción_: Kelly boost +0.75€ cuando `drift_15min` |x|≤ 0.7362 (IC base=+0.085)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2386` → IC=+0.150 (n=38)

  - _Acción_: Kelly boost +0.75€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2386 (IC base=+0.085)

- **PATRÓN** `ibs_15` > `0.8358` → IC=+0.300 (n=28)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8358 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` < `0.0974` → IC=+0.203 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0974 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.113` → IC=+0.132 (n=17)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 13.113 (IC base=+0.085)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 49.0 (IC base=+0.085)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.299 (n=486)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.297 (n=485)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0065 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.053` → IC=+0.311 (n=486)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.053 (IC base=+0.284)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1511` → IC=+0.285 (n=970)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1511 (IC base=+0.284)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2201` → IC=+0.291 (n=892)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2201 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.299 (n=1321)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.284)

- **PATRÓN** `ibs_15` > `0.8368` → IC=+0.311 (n=1456)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8368 (IC base=+0.284)

- **PATRÓN** `dist_vwap_pct` > `0.2738` → IC=+0.314 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2738 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.703` → IC=+0.386 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.703 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.284 (n=1727)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `13112.4613` → IC=+0.301 (n=485)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13112.4613 (IC base=+0.284)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.306 (n=256)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.279)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.279 (n=256)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.279)

- **PATRÓN** `drift_60min` |x|≤ `0.0764` → IC=+0.303 (n=338)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0764 (IC base=+0.279)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2702` → IC=+0.279 (n=256)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2702 (IC base=+0.279)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2292` → IC=+0.287 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2292 (IC base=+0.279)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.303 (n=708)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.279)

- **PATRÓN** `ibs_15` > `0.8572` → IC=+0.310 (n=686)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8572 (IC base=+0.279)

- **PATRÓN** `dist_vwap_pct` > `0.2565` → IC=+0.312 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2565 (IC base=+0.279)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.41` → IC=+0.395 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.41 (IC base=+0.279)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.280 (n=994)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `15655.8789` → IC=+0.314 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15655.8789 (IC base=+0.279)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.297 (n=303)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.0501` → IC=+0.319 (n=230)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0501 (IC base=+0.289)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0659` → IC=+0.294 (n=688)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0659 (IC base=+0.289)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.101` → IC=+0.311 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.101 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.297 (n=663)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.289)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.290 (n=488)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.8448` → IC=+0.313 (n=688)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8448 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.2911` → IC=+0.310 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2911 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` < `0.6569` → IC=+0.289 (n=777)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6569 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.914` → IC=+0.379 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.914 (IC base=+0.289)

### UPDOWN_OU_5M
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1089` → IC=-0.160 (n=233)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1089
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=115)

- **FILTRO** `ballena_activa_n` > `46.0` → IC=-0.143 (n=239)

  - _Acción_: SKIP cuando `ballena_activa_n` > 46.0
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=119)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.14` → IC=-0.149 (n=55)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.14
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=168)

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
- **FILTRO** `sigma_h` < `0.008` → IC=-0.177 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.008
  - _Potencial_: sin este filtro IC_bueno=-0.156 (n=30)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.075` → IC=-0.250 (n=34)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.075
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=18)

- **FILTRO** `sigma_h` < `0.0062` → IC=-0.227 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0062
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=31)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0764` → IC=-0.210 (n=29)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0764
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### WEEKLY_PRICE
- **PATRÓN** `ratio` < `0.9868` → IC=+0.257 (n=569)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9868 (IC base=+0.126)

- **PATRÓN** `T_h` > `115.6465` → IC=+0.356 (n=3174)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 115.6465 (IC base=+0.338)

- **PATRÓN** `ratio` > `1.0178` → IC=+0.389 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0178 (IC base=+0.338)

### WEEKLY_PRICE#BTC
- **PATRÓN** `ratio` < `0.9763` → IC=+0.193 (n=210)

  - _Acción_: Kelly boost +0.97€ cuando `ratio` < 0.9763 (IC base=+0.069)

- **PATRÓN** `T_h` > `110.5638` → IC=+0.328 (n=1162)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 110.5638 (IC base=+0.310)

- **PATRÓN** `ratio` > `1.0152` → IC=+0.377 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0152 (IC base=+0.310)

### WEEKLY_PRICE#ETH
- **PATRÓN** `ratio` < `0.9793` → IC=+0.366 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9793 (IC base=+0.187)

- **PATRÓN** `T_h` > `111.9957` → IC=+0.353 (n=1162)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9957 (IC base=+0.321)

- **PATRÓN** `ratio` > `1.0242` → IC=+0.403 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0242 (IC base=+0.321)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0398` → IC=+0.416 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0398 (IC base=+0.396)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de +0.132 a +0.210 en UPDOWN_GBM#15min (n=5579). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7058 sube el IC de +0.205 a +0.275 en UPDOWN_GBM#BTC#15min (n=861). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.4851 sube el IC de +0.130 a +0.217 en UPDOWN_GBM#ETH#15min (n=1095). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5274 sube el IC de +0.139 a +0.204 en UPDOWN_GBM#XRP#15min (n=1412). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6306 sube el IC de -0.089 a +0.278 en UPDOWN_GBM_15M_TARDIO (n=1306). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.375 sube el IC de +0.002 a +0.285 en UPDOWN_GBM_15M_TARDIO (n=5727). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7609 sube el IC de +0.064 a +0.318 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=466). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6255 sube el IC de -0.182 a +0.287 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=78). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5659 sube el IC de +0.146 a +0.241 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=655). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3879 sube el IC de +0.239 a +0.271 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=2236). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.9231 sube el IC de -0.205 a +0.380 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.381 sube el IC de -0.025 a +0.295 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=961). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.223 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.008 a +0.296 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=1348). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8358 sube el IC de +0.085 a +0.300 en UPDOWN_GBM_ETH_15M_HORA7 (n=28). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8358 sube el IC de +0.085 a +0.300 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=28). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8368 sube el IC de +0.284 a +0.311 en UPDOWN_GBM_IBS_ALTO (n=1456). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8572 sube el IC de +0.279 a +0.310 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=686). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8448 sube el IC de +0.289 a +0.313 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=688). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7903 sube el IC de +0.364 a +0.398 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=789). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8112 sube el IC de +0.366 a +0.387 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=378). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7632 sube el IC de +0.362 a +0.398 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=411). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2278 | +0.082 | +226.56€ | 1 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2278 | +0.082 | +226.56€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1866 | +0.082 | +187.07€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1866 | +0.082 | +187.07€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 285 | +0.068 | +10.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 285 | +0.068 | +10.79€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 96 | +0.122 | +29.03€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 96 | +0.122 | +29.03€ | 0 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 1350 | -0.024 | +75.54€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 1350 | -0.024 | +75.54€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 1042 | -0.037 | +62.48€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 1042 | -0.037 | +62.48€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 210 | +0.047 | +20.23€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 210 | +0.047 | +20.23€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 91 | -0.038 | -10.42€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 91 | -0.038 | -10.42€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 50583 | -0.087 | -6436.44€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 3268 | +0.090 | -315.68€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 47315 | -0.099 | -6120.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 5069 | -0.115 | -811.91€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 5069 | -0.115 | -811.91€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 3268 | +0.090 | -315.68€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 3268 | +0.090 | -315.68€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 5078 | -0.108 | -952.08€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 5078 | -0.108 | -952.08€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 13918 | -0.046 | -1321.26€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 13918 | -0.046 | -1321.26€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 13904 | -0.118 | -1493.36€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 13904 | -0.118 | -1493.36€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 9346 | -0.138 | -1542.15€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 9346 | -0.138 | -1542.15€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 54868 | -0.012 | +2780.60€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 14132 | +0.004 | +1478.35€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 40736 | -0.017 | +1302.25€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 54868 | -0.012 | +2780.60€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 14132 | +0.004 | +1478.35€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 40736 | -0.017 | +1302.25€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 205723 | +0.113 | -8334.41€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 22891 | +0.179 | -737.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 959 | +0.017 | -75.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 170200 | +0.106 | -7095.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 11673 | +0.095 | -425.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 28205 | +0.102 | -2003.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 83 | -0.182 | +13.02€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 28102 | +0.103 | -2010.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#60min | 5 | +0.018 | +5.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 38626 | +0.124 | -597.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5669 | +0.177 | -225.72€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 28172 | +0.120 | -181.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4743 | +0.082 | -168.41€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 28251 | +0.099 | -1985.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 95 | -0.119 | +13.37€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 28140 | +0.100 | -1985.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 44000 | +0.124 | -907.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 10966 | +0.178 | -308.45€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 28627 | +0.106 | -516.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 4395 | +0.103 | -73.96€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 38406 | +0.111 | -1644.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5981 | +0.199 | -241.59€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 862 | +0.042 | -21.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 29037 | +0.096 | -1190.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2526 | +0.105 | -190.02€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO#XRP | 28235 | +0.107 | -1196.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 97 | -0.136 | +11.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 28122 | +0.108 | -1210.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 33462 | +0.189 | -2516.61€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 33462 | +0.189 | -2516.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 7587 | +0.162 | -885.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 7587 | +0.162 | -885.32€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 4980 | +0.194 | -208.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 4980 | +0.194 | -208.09€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 7409 | +0.171 | -694.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 7409 | +0.171 | -694.77€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 6141 | +0.251 | -224.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 6141 | +0.251 | -224.73€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 7266 | +0.183 | -517.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 7266 | +0.183 | -517.44€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1308 | +0.424 | -53.67€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1308 | +0.424 | -53.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 552 | +0.437 | -7.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 552 | +0.437 | -7.85€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 528 | +0.421 | -23.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 528 | +0.421 | -23.69€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 214 | +0.398 | -18.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 214 | +0.398 | -18.26€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 118254 | +0.199 | -8640.41€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 118254 | +0.199 | -8640.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 20496 | +0.176 | -2406.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 20496 | +0.176 | -2406.09€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 19059 | +0.223 | -640.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 19059 | +0.223 | -640.18€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 20286 | +0.181 | -2122.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 20286 | +0.181 | -2122.64€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 19229 | +0.217 | -768.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 19229 | +0.217 | -768.79€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 19521 | +0.205 | -1168.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 19521 | +0.205 | -1168.96€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 19663 | +0.197 | -1533.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 19663 | +0.197 | -1533.75€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 45964 | +0.117 | +370.52€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 45964 | +0.117 | +370.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 22890 | +0.117 | +226.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 22890 | +0.117 | +226.63€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 23074 | +0.116 | +143.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 23074 | +0.116 | +143.89€ | 0 | 3 |
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
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 606 | +0.441 | +0.37€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 52 | +0.407 | +1.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 52 | +0.407 | +1.41€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 2024 | +0.064 | -102.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1299 | +0.074 | -37.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1590 | +0.070 | -56.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1299 | +0.074 | -37.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 93692 | +0.101 | -2013.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 7590 | +0.098 | +188.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 86102 | +0.101 | -2201.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 51157 | +0.105 | -444.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 7590 | +0.098 | +188.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 43567 | +0.107 | -632.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 20098 | +0.110 | -45.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 20098 | +0.110 | -45.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 22437 | +0.082 | -1522.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 22437 | +0.082 | -1522.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ GBM_LATE_15M | 63796 | +0.102 | +35836.38€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 63796 | +0.102 | +35836.38€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 10593 | +0.224 | +9078.02€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 10593 | +0.224 | +9078.02€ | 0 | 22 |
| ✅ GBM_LATE_15M#BTC | 9941 | +0.177 | +7965.17€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 9941 | +0.177 | +7965.17€ | 0 | 24 |
| ✅ GBM_LATE_15M#DOGE | 11430 | +0.206 | +8996.51€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 11430 | +0.206 | +8996.51€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 8435 | +0.062 | +2844.49€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 8435 | +0.062 | +2844.49€ | 1 | 17 |
| ✅ GBM_LATE_15M#SOL | 8846 | -0.025 | +2309.53€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 8846 | -0.025 | +2309.53€ | 3 | 15 |
| ✅ GBM_LATE_15M#XRP | 14551 | -0.020 | +4642.65€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 14551 | -0.020 | +4642.65€ | 3 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 67783 | +0.087 | +39569.73€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 67783 | +0.087 | +39569.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 13146 | -0.002 | +6907.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 13146 | -0.002 | +6907.33€ | 3 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 14559 | +0.007 | +4023.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 14559 | +0.007 | +4023.11€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 9136 | +0.295 | +10451.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 9136 | +0.295 | +10451.74€ | 0 | 22 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 12924 | +0.017 | +4131.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 12924 | +0.017 | +4131.60€ | 0 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 10348 | +0.048 | +4748.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 10348 | +0.048 | +4748.07€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 7670 | +0.313 | +9307.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 7670 | +0.313 | +9307.87€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 50240 | +0.179 | +41676.05€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 50240 | +0.179 | +41676.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 7600 | +0.239 | +7044.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 7600 | +0.239 | +7044.95€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 7984 | +0.141 | +5993.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 7984 | +0.141 | +5993.22€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 8092 | +0.223 | +6997.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 8092 | +0.223 | +6997.96€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 8599 | +0.130 | +6701.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 8599 | +0.130 | +6701.93€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 9476 | +0.123 | +7293.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 9476 | +0.123 | +7293.17€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 8489 | +0.232 | +7644.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 8489 | +0.232 | +7644.81€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 13838 | +0.127 | +7059.74€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 13838 | +0.127 | +7059.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 677 | +0.163 | +447.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 677 | +0.163 | +447.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3574 | +0.126 | +1958.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3574 | +0.126 | +1958.15€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 509 | +0.156 | +286.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 509 | +0.156 | +286.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 4053 | +0.128 | +2046.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 4053 | +0.128 | +2046.39€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 3765 | +0.102 | +1534.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 3765 | +0.102 | +1534.19€ | 0 | 11 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1260 | +0.167 | +786.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1260 | +0.167 | +786.94€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO | 64050 | +0.189 | +53210.92€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#15min | 64050 | +0.189 | +53210.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 10123 | +0.249 | +9748.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 10123 | +0.249 | +9748.21€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 10271 | +0.142 | +7398.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 10271 | +0.142 | +7398.26€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 10870 | +0.234 | +9776.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 10870 | +0.234 | +9776.19€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 10595 | +0.144 | +7951.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 10595 | +0.144 | +7951.33€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 11290 | +0.128 | +8243.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 11290 | +0.128 | +8243.77€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 10901 | +0.240 | +10093.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 10901 | +0.240 | +10093.16€ | 0 | 23 |
| ✅ GBM_LATE_5M | 16313 | +0.218 | +13715.19€ | 0 | 26 |
| ✅ GBM_LATE_5M#5min | 16313 | +0.218 | +13715.19€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1862 | +0.251 | +1794.85€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1862 | +0.251 | +1794.85€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3308 | +0.211 | +2849.00€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3308 | +0.211 | +2849.00€ | 0 | 24 |
| ✅ GBM_LATE_5M#DOGE | 1488 | +0.211 | +1196.75€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1488 | +0.211 | +1196.75€ | 0 | 19 |
| ✅ GBM_LATE_5M#ETH | 4644 | +0.209 | +3625.72€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 4644 | +0.209 | +3625.72€ | 0 | 28 |
| ✅ GBM_LATE_5M#SOL | 2944 | +0.229 | +2615.18€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2944 | +0.229 | +2615.18€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 2067 | +0.210 | +1633.69€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 2067 | +0.210 | +1633.69€ | 0 | 0 |
| ✅ GBM_LATE_60M | 6014 | +0.067 | +1824.33€ | 0 | 6 |
| ✅ GBM_LATE_60M#60min | 6014 | +0.067 | +1824.33€ | 0 | 0 |
| ✅ GBM_LATE_60M#BNB | 81 | +0.235 | +70.91€ | 0 | 0 |
| ✅ GBM_LATE_60M#BNB#60min | 81 | +0.235 | +70.91€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1982 | +0.060 | +579.85€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1982 | +0.060 | +579.85€ | 1 | 6 |
| ✅ GBM_LATE_60M#DOGE | 79 | +0.315 | +88.14€ | 0 | 0 |
| ✅ GBM_LATE_60M#DOGE#60min | 79 | +0.315 | +88.14€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH | 1839 | +0.055 | +596.77€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1839 | +0.055 | +596.77€ | 2 | 6 |
| ✅ GBM_LATE_60M#SOL | 1954 | +0.059 | +410.25€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1954 | +0.059 | +410.25€ | 0 | 8 |
| ✅ GBM_LATE_60M#XRP | 79 | +0.290 | +78.41€ | 0 | 0 |
| ✅ GBM_LATE_60M#XRP#60min | 79 | +0.290 | +78.41€ | 0 | 8 |
| 🚫 GBM_LATE_60M_FADE | 762 | -0.247 | -37.41€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 762 | -0.247 | -37.41€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 269 | -0.257 | -22.31€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 269 | -0.257 | -22.31€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 274 | -0.243 | -7.28€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 274 | -0.243 | -7.28€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 210 | -0.245 | -9.40€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 210 | -0.245 | -9.40€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 2327 | +0.087 | +582.44€ | 1 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 2327 | +0.087 | +582.44€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 883 | +0.068 | +199.83€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 883 | +0.068 | +199.83€ | 1 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 800 | +0.059 | +150.81€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 800 | +0.059 | +150.81€ | 1 | 15 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 642 | +0.149 | +231.55€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 642 | +0.149 | +231.55€ | 1 | 10 |
| ✅ LATE_WINDOW_5MIN | 376 | +0.315 | +452.18€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 376 | +0.315 | +452.18€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 376 | +0.315 | +452.18€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 376 | +0.315 | +452.18€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 4753 | +0.095 | +1042.98€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4753 | +0.095 | +1042.98€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4753 | +0.095 | +1042.98€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4753 | +0.095 | +1042.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M | 1663 | +0.021 | +103.00€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 1663 | +0.021 | +103.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 198 | +0.090 | +41.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 198 | +0.090 | +41.42€ | 0 | 4 |
| ✅ LIQUIDACIONES_15M#BTC | 330 | -0.015 | +6.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 330 | -0.015 | +6.39€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 108 | +0.054 | +22.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 108 | +0.054 | +22.69€ | 2 | 4 |
| ✅ LIQUIDACIONES_15M#ETH | 379 | +0.030 | +23.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 379 | +0.030 | +23.57€ | 2 | 1 |
| ✅ LIQUIDACIONES_15M#SOL | 349 | -0.013 | +3.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 349 | -0.013 | +3.33€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 299 | +0.028 | +5.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 299 | +0.028 | +5.60€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4521 | +0.017 | +184.66€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#5min | 4521 | +0.017 | +184.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 240 | +0.004 | -5.65€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 240 | +0.004 | -5.65€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 858 | +0.014 | +45.19€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 858 | +0.014 | +45.19€ | 2 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 329 | +0.068 | +86.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 329 | +0.068 | +86.31€ | 0 | 7 |
| ✅ LIQUIDACIONES_5M#ETH | 1686 | +0.019 | +30.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1686 | +0.019 | +30.36€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 788 | +0.014 | +5.02€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 788 | +0.014 | +5.02€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 620 | -0.006 | +23.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 620 | -0.006 | +23.43€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2690 | -0.034 | -6.49€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2690 | -0.034 | -6.49€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 823 | -0.036 | -15.68€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 823 | -0.036 | -15.68€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 965 | -0.013 | +19.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 965 | -0.013 | +19.94€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 894 | -0.054 | -9.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 894 | -0.054 | -9.83€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#XRP | 5 | -0.018 | -0.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#XRP#60min | 5 | -0.018 | -0.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 19934 | -0.031 | -140.08€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 9621 | -0.033 | -124.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 10313 | -0.029 | -16.03€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 710 | -0.051 | -34.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 357 | -0.035 | -4.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 353 | -0.066 | -29.97€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 5318 | -0.026 | -23.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 2527 | -0.023 | +2.46€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 2791 | -0.029 | -26.03€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1838 | -0.033 | -1.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 935 | -0.043 | -26.94€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 903 | -0.021 | +24.97€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 4554 | -0.030 | -43.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 2190 | -0.029 | -15.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 2364 | -0.032 | -27.87€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 3816 | -0.022 | +58.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1853 | -0.031 | -9.14€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1963 | -0.015 | +67.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 3698 | -0.042 | -95.65€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1759 | -0.049 | -70.59€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1939 | -0.036 | -25.06€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 75353 | -0.000 | +4142.80€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 75353 | -0.000 | +4142.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 13700 | +0.028 | +1923.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 13700 | +0.028 | +1923.39€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 10438 | -0.039 | -161.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 10438 | -0.039 | -161.86€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 13859 | +0.026 | +1573.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 13859 | +0.026 | +1573.08€ | 1 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 10433 | -0.053 | -259.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 10433 | -0.053 | -259.02€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 12845 | -0.004 | +374.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 12845 | -0.004 | +374.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 14078 | +0.019 | +692.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 14078 | +0.019 | +692.41€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7379 | -0.053 | -111.21€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7379 | -0.053 | -111.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1269 | -0.001 | -13.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1269 | -0.001 | -13.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 2089 | -0.060 | -21.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 2089 | -0.060 | -21.68€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 102 | -0.019 | -0.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 102 | -0.019 | -0.22€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 818 | -0.116 | -32.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 818 | -0.116 | -32.47€ | 6 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2231 | -0.067 | -14.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2231 | -0.067 | -14.13€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 870 | -0.019 | -28.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 870 | -0.019 | -28.97€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3384 | +0.003 | -0.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3384 | +0.003 | -0.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 133 | -0.033 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 133 | -0.033 | -0.70€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 199 | +0.007 | -1.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 199 | +0.007 | -1.73€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 139 | -0.004 | -2.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 139 | -0.004 | -2.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1326 | +0.006 | +6.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1326 | +0.006 | +6.37€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1391 | +0.007 | -0.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1391 | +0.007 | -0.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 196 | -0.015 | -1.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 196 | -0.015 | -1.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 184686 | -0.077 | +2320.82€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 184686 | -0.077 | +2320.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 32561 | -0.076 | +1929.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 32561 | -0.076 | +1929.08€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 27405 | -0.102 | -1382.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 27405 | -0.102 | -1382.83€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 32973 | -0.068 | +1622.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 32973 | -0.068 | +1622.75€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 26954 | -0.100 | -902.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 26954 | -0.100 | -902.44€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 32948 | -0.059 | +236.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 32948 | -0.059 | +236.93€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 31845 | -0.069 | +817.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 31845 | -0.069 | +817.33€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9273 | -0.035 | -187.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9273 | -0.035 | -187.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1009 | -0.017 | -19.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1009 | -0.017 | -19.83€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2163 | -0.046 | -28.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2163 | -0.046 | -28.57€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2674 | -0.024 | -33.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2674 | -0.024 | -33.11€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1297 | -0.064 | -32.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1297 | -0.064 | -32.97€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1121 | -0.038 | -41.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1121 | -0.038 | -41.54€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 2335 | +0.120 | +939.53€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 2199 | +0.124 | +926.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 508 | +0.141 | +262.45€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 508 | +0.141 | +262.45€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#DOGE | 459 | +0.116 | +159.96€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 459 | +0.116 | +159.96€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 408 | +0.127 | +185.97€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 408 | +0.127 | +185.97€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 374 | +0.136 | +184.28€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 374 | +0.136 | +184.28€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 450 | +0.100 | +134.27€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 450 | +0.100 | +134.27€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 2463 | -0.023 | -48.30€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2463 | -0.023 | -48.30€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 442 | +0.007 | +20.21€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 442 | +0.007 | +20.21€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 453 | -0.050 | -31.35€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 453 | -0.050 | -31.35€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 600 | -0.046 | -43.47€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 600 | -0.046 | -43.47€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 510 | -0.002 | +1.46€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 510 | -0.002 | +1.46€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 458 | -0.017 | +4.84€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 458 | -0.017 | +4.84€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1291 | -0.041 | +133.53€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 595 | -0.066 | +26.51€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 466 | -0.062 | +50.26€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 129 | -0.080 | -23.75€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 454 | -0.013 | +69.03€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 333 | +0.007 | +77.78€ | 1 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 121 | -0.069 | -8.75€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 242 | -0.033 | +37.99€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 206 | -0.024 | +36.15€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 36 | -0.079 | +1.84€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 1005 | -0.031 | +164.19€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 286 | -0.076 | -30.66€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE | 1638 | -0.183 | -31.56€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 644 | -0.172 | -7.28€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 573 | -0.168 | -3.38€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 71 | -0.199 | -3.91€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH | 550 | -0.196 | -31.93€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 487 | -0.203 | -38.56€ | 4 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 63 | -0.131 | +6.63€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 444 | -0.184 | +7.65€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 413 | -0.179 | +6.01€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 31 | -0.227 | +1.64€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#atexpiry | 1473 | -0.183 | -35.93€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 165 | -0.183 | +4.36€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 584 | +0.375 | +526.07€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#BTC | 132 | +0.172 | +100.16€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 132 | +0.172 | +100.16€ | 0 | 6 |
| ✅ RESOLUTION_SNIPER#ETH | 133 | +0.367 | +106.16€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 133 | +0.367 | +106.16€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#SOL | 319 | +0.460 | +319.75€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 319 | +0.460 | +319.75€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 584 | +0.375 | +526.07€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 1025 | +0.038 | +80.37€ | 2 | 3 |
| ✅ STREAK_FADE_15M#15min | 1025 | +0.038 | +80.37€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 359 | +0.015 | +2.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 359 | +0.015 | +2.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 79 | +0.018 | +0.52€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 79 | +0.018 | +0.52€ | 1 | 1 |
| ✅ STREAK_FADE_15M#SOL | 85 | +0.029 | +7.61€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 85 | +0.029 | +7.61€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 502 | +0.059 | +69.90€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 502 | +0.059 | +69.90€ | 1 | 3 |
| ✅ STREAK_FADE_5M | 3635 | -0.023 | -142.06€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3635 | -0.023 | -142.06€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 624 | -0.029 | -27.52€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 624 | -0.029 | -27.52€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 176 | -0.045 | -15.29€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 176 | -0.045 | -15.29€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1708 | -0.018 | -59.05€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1708 | -0.018 | -59.05€ | 1 | 0 |
| ✅ STREAK_FADE_60M | 131 | -0.026 | -10.42€ | 3 | 1 |
| ✅ STREAK_FADE_60M#60min | 131 | -0.026 | -10.42€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 46 | -0.062 | -3.71€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 46 | -0.062 | -3.71€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 81 | -0.006 | -6.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 81 | -0.006 | -6.44€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 11633 | +0.013 | +68.68€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11633 | +0.013 | +68.68€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 3004 | +0.017 | +22.85€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 3004 | +0.017 | +22.85€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 3093 | +0.014 | +29.48€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 3093 | +0.014 | +29.48€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2938 | +0.008 | -4.57€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2938 | +0.008 | -4.57€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2598 | +0.015 | +20.93€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2598 | +0.015 | +20.93€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 13357 | +0.019 | +16.47€ | 4 | 0 |
| ✅ STRUCT_NO_15M#15min | 13357 | +0.019 | +16.47€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 5405 | +0.020 | +3.44€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 5405 | +0.020 | +3.44€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 4714 | +0.020 | +8.39€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 4714 | +0.020 | +8.39€ | 4 | 0 |
| ✅ STRUCT_NO_15M#SOL | 3238 | +0.017 | +4.64€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 3238 | +0.017 | +4.64€ | 1 | 0 |
| ✅ UPDOWN_GBM | 121599 | +0.060 | +11563.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 30079 | +0.078 | +5908.97€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 3473 | -0.000 | +43.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 80425 | +0.062 | +5488.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 7210 | -0.002 | +129.48€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 10726 | +0.103 | +1961.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1985 | +0.165 | +933.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 8651 | +0.090 | +1029.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 27419 | +0.057 | +2430.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 4022 | +0.082 | +908.66€ | 0 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 1014 | -0.001 | +21.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 18998 | +0.066 | +1415.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 3237 | -0.004 | +79.98€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 148 | -0.067 | +4.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 13579 | +0.074 | +1485.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1963 | +0.155 | +834.78€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 11530 | +0.061 | +651.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 28435 | +0.049 | +2024.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 7001 | +0.071 | +1084.08€ | 0 | 9 |
| ✅ UPDOWN_GBM#ETH#240min | 981 | +0.006 | +16.40€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 17641 | +0.052 | +880.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2674 | -0.001 | +41.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 138 | -0.100 | +2.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 25301 | +0.040 | +1419.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 8144 | +0.033 | +463.54€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 905 | -0.009 | +9.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 14829 | +0.052 | +949.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1299 | +0.004 | +8.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 124 | -0.143 | -10.98€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 16137 | +0.073 | +2243.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 6964 | +0.090 | +1683.98€ | 0 | 12 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 8776 | +0.063 | +560.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 410 | -0.102 | -4.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 1052 | +0.364 | +392.97€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 1052 | +0.364 | +392.97€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 504 | +0.366 | +180.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 504 | +0.366 | +180.39€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 548 | +0.362 | +212.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 548 | +0.362 | +212.59€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 28662 | -0.017 | +7193.81€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 28662 | -0.017 | +7193.81€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 2215 | -0.048 | +599.94€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 2215 | -0.048 | +599.94€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 5276 | -0.116 | +282.15€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 5276 | -0.116 | +282.15€ | 3 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1212 | +0.223 | +1022.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1212 | +0.223 | +1022.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 3854 | +0.218 | +2448.32€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 3854 | +0.218 | +2448.32€ | 1 | 19 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 8103 | -0.056 | +1225.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 8103 | -0.056 | +1225.13€ | 3 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 8002 | -0.053 | +1616.22€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 8002 | -0.053 | +1616.22€ | 4 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 359 | +0.057 | +29.80€ | 0 | 8 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 359 | +0.057 | +29.80€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 359 | +0.057 | +29.80€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 359 | +0.057 | +29.80€ | 0 | 8 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1940 | +0.284 | +1652.69€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1940 | +0.284 | +1652.69€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 1023 | +0.279 | +824.95€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 1023 | +0.279 | +824.95€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 917 | +0.289 | +827.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 917 | +0.289 | +827.74€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 898 | -0.119 | -94.25€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 898 | -0.119 | -94.25€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 289 | -0.084 | -22.53€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 289 | -0.084 | -22.53€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 105 | -0.192 | -14.83€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 105 | -0.192 | -14.83€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 121 | -0.191 | -7.54€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 121 | -0.191 | -7.54€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 5238 | +0.295 | +2340.56€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 2031 | +0.252 | +309.27€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 2029 | +0.288 | +870.05€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 1178 | +0.381 | +1161.24€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.025 n=1490 — no justifica filtro, seguir monitorizando
  - _Datos_: n=1490 IC=+0.025 PNL=+72.07€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 848 celda(s) pasan gate riguroso completo de 3042 evaluadas (n>=40) y 4158 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.033 < 0.08 — monitorear
  - _Datos_: n=8139 IC=+0.033 PNL=+463.93€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=2029/15 IC=+0.288 PNL=+870.05€ | BTC: n=2031/15 IC=+0.252 PNL=+309.27€ | SOL: n=1178/15 IC=+0.381 PNL=+1161.24€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.136 n=1135/60 | contraria IC=+0.186 n=1194 | gap=-0.051 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=638, boost estimado=+0.009. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=2673/40 IC=-0.001 PNL=+41.99€ | BTC#60min: n=3235/40 IC=-0.004 PNL=+79.97€ | SOL#60min: n=1299/40 IC=+0.004 PNL=+8.03€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.044 n=811953 | tras_1loss IC=+0.102 n=614630 | tras_2loss IC=+0.073 n=244394/40 | gap=-0.029 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.151 > 0.08 con n=1229 PNL=+695.08€
  - _Datos_: n=1229 IC=+0.151 PNL=+695.08€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.122 > 0.08 con n=1465 PNL=+641.52€
  - _Datos_: n=1465 IC=+0.122 PNL=+641.52€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.336 > 0.1 con n=4275 PNL=+2471.86€
  - _Datos_: n=4275 IC=+0.336 PNL=+2471.86€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=1224 IC=+0.064 PNL=+122.77€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1224 IC=+0.064 PNL=+122.77€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=115 IC=+0.167 PNL=+70.09€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=115 IC=+0.167 PNL=+70.09€

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
  - _Estado_: n=4724 IC=-0.006 PNL=-50.45€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4724 IC=-0.006 PNL=-50.45€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=2483 IC=+0.007 PNL=+180.43€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=2483 IC=+0.007 PNL=+180.43€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=1490 IC=+0.025 PNL=+72.07€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=1490 IC=+0.025 PNL=+72.07€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.132 > 0.1 con n=8319 PNL=+3933.01€
  - _Datos_: n=8319 IC=+0.132 PNL=+3933.01€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=4017 IC=+0.081 PNL=+907.53€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=4017 IC=+0.081 PNL=+907.53€

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
  - _Estado_: n=1630 IC=+0.045 PNL=+136.16€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=1630 IC=+0.045 PNL=+136.16€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=201 IC=-0.027 PNL=-6.29€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=201 IC=-0.027 PNL=-6.29€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.315 n=376) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=376 IC=+0.315 PNL=+452.18€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.117 > 0.02 con n=1367 PNL=+546.77€
  - _Datos_: n=1367 IC=+0.117 PNL=+546.77€

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
  - _Estado_: n=49869 IC=+0.069 PNL=+6608.67€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=49869 IC=+0.069 PNL=+6608.67€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.129 < -0.1 con n=831 PNL=+131.58€
  - _Datos_: n=831 IC=-0.129 PNL=+131.58€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=4854 IC=+0.069 PNL=+598.84€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=4854 IC=+0.069 PNL=+598.84€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=209 IC=-0.078 PNL=+6.52€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=209 IC=-0.078 PNL=+6.52€

**〰️ H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: n=1290 IC=+0.098 PNL=+317.35€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1290 IC=+0.098 PNL=+317.35€

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
  - _Estado_: n=48484 IC=-0.138 PNL=+2872.98€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=48484 IC=-0.138 PNL=+2872.98€

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
  - _Estado_: n=5193 IC=+0.135 PNL=+3602.53€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=5193 IC=+0.135 PNL=+3602.53€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=12656 IC=+0.057 PNL=+1078.89€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=12656 IC=+0.057 PNL=+1078.89€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.102 > 0.08 con n=5240 PNL=+2942.36€
  - _Datos_: n=5240 IC=+0.102 PNL=+2942.36€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.221 < -0.1 con n=5274 PNL=-440.51€
  - _Datos_: n=5274 IC=-0.221 PNL=-440.51€

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
  - _Estado_: n=133 IC=+0.070 PNL=+22.11€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=133 IC=+0.070 PNL=+22.11€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.097 n=2411) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=2411 IC=+0.097 PNL=+481.20€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.414 n=695) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=695 IC=+0.414 PNL=+1018.76€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=20486 IC=+0.176 PNL=-2401.84€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=20486 IC=+0.176 PNL=-2401.84€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.230 > 0.1 con n=339 PNL=+234.82€
  - _Datos_: n=339 IC=+0.230 PNL=+234.82€
