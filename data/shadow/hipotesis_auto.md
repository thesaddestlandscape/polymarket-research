# Hipótesis automáticas — 2026-11-22 02:04 UTC
_Generado por shadow_postmortem.py sobre 1444824 resoluciones (PNL=+203658.22€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.5` → IC=-0.317 (n=195)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=734)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.195 (n=1091)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.505 (IC base=+0.123)

- **PATRÓN** `n_total_lado` > `61.0` → IC=+0.171 (n=348)

  - _Acción_: Kelly boost +0.86€ cuando `n_total_lado` > 61.0 (IC base=+0.123)

- **PATRÓN** `banda_hit_calibrado` > `0.8121` → IC=+0.269 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8121 (IC base=+0.123)

- **PATRÓN** `banda_z` > `8.3` → IC=+0.193 (n=343)

  - _Acción_: Kelly boost +0.96€ cuando `banda_z` > 8.3 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.140 (n=378)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=1119)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.123)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.280 (n=171)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=523)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.194 (n=954)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.505 (IC base=+0.125)

- **PATRÓN** `n_total_lado` > `64.0` → IC=+0.180 (n=298)

  - _Acción_: Kelly boost +0.90€ cuando `n_total_lado` > 64.0 (IC base=+0.125)

- **PATRÓN** `banda_hit_calibrado` > `0.8114` → IC=+0.268 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8114 (IC base=+0.125)

- **PATRÓN** `banda_z` > `8.502` → IC=+0.197 (n=298)

  - _Acción_: Kelly boost +0.98€ cuando `banda_z` > 8.502 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.135 (n=812)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 8.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.126 (n=631)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.129 (n=1019)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `8808.1502` → IC=+0.130 (n=236)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 8808.1502 (IC base=+0.014)

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
- **FILTRO** `restante_s_al_confirmar` < `130.37` → IC=-0.221 (n=12749)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.37
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=38253)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `122.97` → IC=-0.263 (n=1272)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 122.97
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3816)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `114.34` → IC=-0.280 (n=1272)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 114.34
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=3819)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `115.48` → IC=-0.164 (n=3526)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 115.48
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=10583)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `147.52` → IC=-0.255 (n=3506)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 147.52
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=10519)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `127.73` → IC=-0.267 (n=2345)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.73
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=7035)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.209 (n=30149)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `10787.2419` → IC=+0.162 (n=1809)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 10787.2419 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.128 (n=26703)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=32161)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.225 (n=24149)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=8767)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `6331.5198` → IC=+0.139 (n=3425)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 6331.5198 (IC base=+0.125)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=2220)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.358 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.175)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.178 (n=2718)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.01 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `16269.5677` → IC=+0.181 (n=706)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 16269.5677 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.185 (n=1940)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 7.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.182 (n=2167)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 17.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.328 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.181 (n=2775)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `16044.722` → IC=+0.186 (n=717)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 16044.722 (IC base=+0.178)

### FAVORITO_CONFIRMADO#BTC#60min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.335 (n=95)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=2395)

- **PATRÓN** `py_entrada` > `0.61` → IC=+0.174 (n=666)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` > 0.61 (IC base=+0.075)

- **PATRÓN** `libro_liquidez` > `6825.0558` → IC=+0.130 (n=152)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 6825.0558 (IC base=+0.075)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.153 (n=1558)

  - _Acción_: Kelly boost +0.77€ cuando `py_entrada` < 0.44 (IC base=+0.088)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.171 (n=5503)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 6.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.175 (n=2686)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 8.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` > `0.78` → IC=+0.377 (n=1868)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.78 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.202 (n=2641)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.332 (n=992)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.200 (n=3080)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.195)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.142 (n=710)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 15.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.141 (n=953)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 11.0 (IC base=+0.138)

- **PATRÓN** `py_entrada` > `0.645` → IC=+0.235 (n=688)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.645 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=1191)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `2053.6258` → IC=+0.141 (n=951)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2053.6258 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `4420.281` → IC=+0.152 (n=156)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4420.281 (IC base=+0.076)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.252 (n=988)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.229)

- **PATRÓN** `py_entrada` > `0.835` → IC=+0.428 (n=1323)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.835 (IC base=+0.229)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.155 (n=749)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.144)

- **PATRÓN** `py_entrada` < `0.345` → IC=+0.278 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.345 (IC base=+0.144)

### FAVORITO_CONFIRMADO#SOL#60min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.306 (n=153)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.160 (n=483)

- **PATRÓN** `py_entrada` > `0.55` → IC=+0.160 (n=483)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` > 0.55 (IC base=+0.047)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.130 (n=1355)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 7.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.135 (n=1034)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 12.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.257 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.125)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.299 (n=152)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=78)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.198 (n=26600)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=22424)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.223 (n=8454)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.338 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `4915.142` → IC=+0.339 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4915.142 (IC base=+0.192)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=6064)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.162)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.175 (n=5890)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.74 (IC base=+0.162)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.209 (n=3726)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.207 (n=2479)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.245 (n=1797)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.204)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.181 (n=5912)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.174 (n=5001)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 15.0 (IC base=+0.173)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.175 (n=6066)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.73 (IC base=+0.173)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.181 (n=4650)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.71 (IC base=+0.173)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.256 (n=4667)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.252)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.252 (n=2266)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.252)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.362 (n=1612)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=5778)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.191 (n=3666)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 11.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.200 (n=1878)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.185)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.427 (n=1018)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.424)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.426 (n=1011)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.424)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.437 (n=1024)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.424)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.429 (n=1095)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.424)

- **PATRÓN** `libro_liquidez` > `14011.0969` → IC=+0.449 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14011.0969 (IC base=+0.424)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.436 (n=418)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.437)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.442 (n=431)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.448 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.437)

- **PATRÓN** `libro_liquidez` > `15265.4378` → IC=+0.443 (n=278)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.402 (n=162)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.399)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.405 (n=146)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.399)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.414 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.399)

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

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.211 (n=29946)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.239 (n=34350)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.186 (n=5221)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 18.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.176 (n=11146)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 12.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=16031)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.176)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=14522)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.275 (n=6189)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.223)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.197 (n=5133)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 18.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.199 (n=12302)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.181)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` > `0.775` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.229 (n=4885)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.221 (n=5592)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.259 (n=5996)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.218)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `py_entrada` < `0.775` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `libro_liquidez` < `3197.0694` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 3197.0694
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.217 (n=4940)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.256 (n=4956)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.206)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.206 (n=4982)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.199 (n=5767)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.247 (n=5858)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=12537)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.140 (n=13623)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.29` → IC=+0.142 (n=11642)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 2.29 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=6105)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.144 (n=6186)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.125 (n=7714)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.79` → IC=+0.142 (n=7646)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 3.79 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=6432)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.137 (n=8231)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.95 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.92` → IC=+0.137 (n=7706)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.92 (IC base=+0.116)

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
- **PATRÓN** `drift_60min` |x|≤ `0.5049` → IC=+0.140 (n=19903)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.5049 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.128 (n=20162)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.126 (n=13824)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.975` → IC=+0.247 (n=6634)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.975 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.8708` → IC=+0.293 (n=1092)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8708 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.47` → IC=+0.191 (n=9990)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 3.47 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.6959` → IC=+0.268 (n=5432)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6959 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.3035` → IC=+0.256 (n=2062)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3035 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.7408` → IC=+0.233 (n=4807)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7408 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=9646)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `4842.107` → IC=+0.151 (n=6634)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 4842.107 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.123 (n=12591)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0065 (IC base=+0.087)

- **PATRÓN** `ibs_20min` < `0.5641` → IC=+0.145 (n=25143)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.5641 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.6708` → IC=+0.192 (n=1705)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.6708 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` < `0.1757` → IC=+0.195 (n=10275)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.1757 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` < `0.8575` → IC=+0.196 (n=6985)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.8575 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2958` → IC=+0.232 (n=2550)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2958 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `1.4559` → IC=+0.209 (n=17753)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4559 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.229 (n=17724)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.087)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.242 (n=1412)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.3021` → IC=+0.215 (n=3719)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3021 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.224 (n=2055)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.212 (n=2827)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.9828` → IC=+0.274 (n=1915)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9828 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.806` → IC=+0.292 (n=1002)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.806 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.2348` → IC=+0.259 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2348 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `1.4413` → IC=+0.211 (n=4057)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4413 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.221 (n=4598)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2044.3` → IC=+0.216 (n=1408)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2044.3 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.219 (n=3453)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.210)

- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.247 (n=1732)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.0952` → IC=+0.269 (n=1274)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0952 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.241 (n=3981)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.249 (n=1743)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0765` → IC=+0.281 (n=1274)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0765 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` < `0.0725` → IC=+0.243 (n=3296)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0725 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.2889` → IC=+0.250 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2889 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `1.8591` → IC=+0.245 (n=2440)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8591 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.244 (n=2637)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.240)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.233 (n=1207)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.222)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.222 (n=1203)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.1135` → IC=+0.246 (n=1587)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1135 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=3784)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.221 (n=2572)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `0.8926` → IC=+0.258 (n=1203)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8926 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` > `0.7455` → IC=+0.235 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7455 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` < `0.5654` → IC=+0.222 (n=3980)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5654 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.741` → IC=+0.265 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.741 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` > `0.697` → IC=+0.229 (n=3224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.697 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.2772` → IC=+0.271 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2772 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.4423` → IC=+0.249 (n=1188)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4423 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.153 (n=3965)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0069 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.2763` → IC=+0.147 (n=3485)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.2763 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.147 (n=2824)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 11.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.7084` → IC=+0.172 (n=3962)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.7084 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.1532` → IC=+0.151 (n=3881)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1532 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.944` → IC=+0.142 (n=3639)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 3.944 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.6285` → IC=+0.155 (n=1321)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6285 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.0977` → IC=+0.160 (n=1441)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.0977 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.4465` → IC=+0.143 (n=3830)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.4465 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.4194` → IC=+0.137 (n=3830)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.4194 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=5146)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.187 (n=1257)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 166.0 (IC base=+0.136)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.206 (n=2033)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=4713)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.254 (n=1726)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.907` → IC=+0.282 (n=987)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.907 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` < `0.0968` → IC=+0.192 (n=4018)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.0968 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.3497` → IC=+0.225 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3497 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.7284` → IC=+0.208 (n=1985)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7284 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.197 (n=5454)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `1906.4295` → IC=+0.198 (n=2030)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 1906.4295 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.0125` → IC=+0.223 (n=4195)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0125 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.3057` → IC=+0.229 (n=2797)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3057 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.240 (n=1596)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.227 (n=1901)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` < `0.0499` → IC=+0.271 (n=1399)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0499 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.712` → IC=+0.270 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.712 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.3454` → IC=+0.255 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3454 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.151` → IC=+0.232 (n=2701)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.151 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.223 (n=2017)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `1890.9784` → IC=+0.224 (n=1902)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1890.9784 (IC base=+0.221)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.224 (n=4041)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.221)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.170 (n=237)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=5414)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.145 (n=727)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.004 (IC base=+0.067)

- **PATRÓN** `ibs_20min` > `0.9436` → IC=+0.251 (n=724)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9436 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` > `0.1555` → IC=+0.349 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1555 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` < `0.5901` → IC=+0.343 (n=946)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5901 (IC base=+0.067)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.174` → IC=+0.214 (n=1595)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.174 (IC base=+0.067)

- **PATRÓN** `volumen_regimen` > `1.1103` → IC=+0.362 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1103 (IC base=+0.067)

- **PATRÓN** `volumen_pendiente_norm` < `0.1672` → IC=+0.347 (n=719)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1672 (IC base=+0.067)

- **PATRÓN** `volumen_pendiente_norm` > `0.3033` → IC=+0.354 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3033 (IC base=+0.067)

- **PATRÓN** `volumen_spike_ratio` < `1.4175` → IC=+0.359 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4175 (IC base=+0.067)

- **PATRÓN** `volumen_spike_ratio` > `2.2812` → IC=+0.353 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2812 (IC base=+0.067)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.350 (n=880)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.067)

- **PATRÓN** `ibs_20min` < `0.087` → IC=+0.190 (n=1413)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.087 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` > `0.3617` → IC=+0.158 (n=708)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.3617 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` < `0.1509` → IC=+0.158 (n=2635)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1509 (IC base=+0.059)

- **PATRÓN** `volumen_regimen` < `0.8288` → IC=+0.163 (n=1853)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8288 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.2783` → IC=+0.201 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2783 (IC base=+0.059)

- **PATRÓN** `volumen_spike_ratio` > `2.4331` → IC=+0.173 (n=892)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.4331 (IC base=+0.059)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.189 (n=159)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=874)

- **FILTRO** `ibs_20min` < `0.2727` → IC=-0.177 (n=258)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2727
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=775)

- **FILTRO** `ibs_20min` > `0.1944` → IC=-0.127 (n=5306)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1944
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=2617)

- **FILTRO** `sigma_ewma_delta_pct` > `8.266` → IC=-0.232 (n=857)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.266
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=7066)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.171 (n=354)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.75 (IC base=+0.019)

- **PATRÓN** `dist_vwap_pct` > `0.9817` → IC=+0.270 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9817 (IC base=+0.019)

- **PATRÓN** `dist_vwap_pct` < `1.3529` → IC=+0.269 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 1.3529 (IC base=+0.019)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.67` → IC=+0.173 (n=163)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 6.67 (IC base=+0.019)

- **PATRÓN** `volumen_regimen` > `1.005` → IC=+0.306 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.005 (IC base=+0.019)

- **PATRÓN** `volumen_pendiente_norm` < `0.1591` → IC=+0.273 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1591 (IC base=+0.019)

- **PATRÓN** `volumen_spike_ratio` < `2.1989` → IC=+0.283 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1989 (IC base=+0.019)

- **PATRÓN** `volumen_spike_ratio` > `1.5438` → IC=+0.258 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5438 (IC base=+0.019)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.266 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.019)

- **PATRÓN** `ibs_20min` < `0.1944` → IC=+0.159 (n=2617)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1944 (IC base=-0.032)

- **PATRÓN** `dist_vwap_pct` > `0.2353` → IC=+0.294 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2353 (IC base=-0.032)

- **PATRÓN** `dist_vwap_pct` < `1.0482` → IC=+0.291 (n=1478)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 1.0482 (IC base=-0.032)

- **PATRÓN** `volumen_regimen` < `0.6932` → IC=+0.300 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6932 (IC base=-0.032)

- **PATRÓN** `volumen_regimen` > `1.0428` → IC=+0.294 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0428 (IC base=-0.032)

- **PATRÓN** `volumen_pendiente_norm` > `0.0783` → IC=+0.317 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0783 (IC base=-0.032)

- **PATRÓN** `volumen_spike_ratio` < `2.4326` → IC=+0.303 (n=1126)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4326 (IC base=-0.032)

- **PATRÓN** `volumen_spike_ratio` > `1.417` → IC=+0.299 (n=1125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.417 (IC base=-0.032)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.8` → IC=-0.158 (n=4090)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=2109)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.179 (n=1261)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=4938)

- **FILTRO** `ibs_20min` > `0.725` → IC=-0.190 (n=2136)

  - _Acción_: SKIP cuando `ibs_20min` > 0.725
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=6413)

- **PATRÓN** `ibs_20min` > `0.8` → IC=+0.143 (n=2109)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.8 (IC base=-0.056)

- **PATRÓN** `dist_vwap_pct` > `0.4523` → IC=+0.348 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4523 (IC base=-0.056)

- **PATRÓN** `volumen_regimen` > `0.7044` → IC=+0.319 (n=1133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7044 (IC base=-0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.3056` → IC=+0.313 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3056 (IC base=-0.056)

- **PATRÓN** `volumen_spike_ratio` > `1.8941` → IC=+0.312 (n=829)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8941 (IC base=-0.056)

- **PATRÓN** `dist_vwap_pct` > `1.1048` → IC=+0.283 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1048 (IC base=+0.007)

- **PATRÓN** `volumen_regimen` < `0.7185` → IC=+0.273 (n=1119)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7185 (IC base=+0.007)

- **PATRÓN** `volumen_regimen` > `1.064` → IC=+0.278 (n=1152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.064 (IC base=+0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.2379` → IC=+0.281 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2379 (IC base=+0.007)

- **PATRÓN** `volumen_spike_ratio` < `2.4868` → IC=+0.264 (n=2413)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4868 (IC base=+0.007)

- **PATRÓN** `volumen_spike_ratio` > `1.4427` → IC=+0.270 (n=2412)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4427 (IC base=+0.007)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.188 (n=8708)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0111 (IC base=+0.086)

- **PATRÓN** `ibs_20min` > `0.8657` → IC=+0.284 (n=11830)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8657 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` > `0.9982` → IC=+0.301 (n=1809)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9982 (IC base=+0.086)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.46` → IC=+0.167 (n=11763)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.46 (IC base=+0.086)

- **PATRÓN** `volumen_regimen` > `0.693` → IC=+0.279 (n=8658)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.693 (IC base=+0.086)

- **PATRÓN** `volumen_pendiente_norm` > `0.2931` → IC=+0.297 (n=2149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2931 (IC base=+0.086)

- **PATRÓN** `volumen_spike_ratio` > `2.6418` → IC=+0.288 (n=5044)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6418 (IC base=+0.086)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.308 (n=14786)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 88.0 (IC base=+0.086)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.153 (n=11508)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0092 (IC base=+0.088)

- **PATRÓN** `ibs_20min` < `0.516` → IC=+0.175 (n=22310)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.516 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` < `0.2018` → IC=+0.283 (n=8597)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2018 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` < `0.8588` → IC=+0.279 (n=5752)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8588 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` > `1.1879` → IC=+0.285 (n=2878)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1879 (IC base=+0.088)

- **PATRÓN** `volumen_pendiente_norm` > `0.2948` → IC=+0.323 (n=1908)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2948 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` < `1.4528` → IC=+0.303 (n=4276)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4528 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` > `2.2697` → IC=+0.304 (n=5814)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2697 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.312 (n=12833)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 71.0 (IC base=+0.088)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8122` → IC=-0.145 (n=4619)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8122
  - _Potencial_: sin este filtro IC_bueno=+0.310 (n=2382)

- **FILTRO** `ibs_20min` > `0.7` → IC=-0.239 (n=1571)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=4726)

- **FILTRO** `sigma_ewma_delta_pct` > `4.054` → IC=-0.241 (n=1328)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.054
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=4969)

- **PATRÓN** `ibs_20min` > `0.8122` → IC=+0.310 (n=2382)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8122 (IC base=+0.010)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.142` → IC=+0.173 (n=2612)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 2.142 (IC base=+0.010)

- **PATRÓN** `volumen_pendiente_norm` > `0.2297` → IC=+0.336 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2297 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` < `1.4461` → IC=+0.289 (n=733)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4461 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` > `2.2304` → IC=+0.315 (n=996)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2304 (IC base=+0.010)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.321 (n=1497)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.010)

- **PATRÓN** `ibs_20min` < `0.1702` → IC=+0.173 (n=1576)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.1702 (IC base=-0.014)

- **PATRÓN** `volumen_pendiente_norm` < `0.1559` → IC=+0.390 (n=1388)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1559 (IC base=-0.014)

- **PATRÓN** `volumen_spike_ratio` < `2.6658` → IC=+0.394 (n=1333)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6658 (IC base=-0.014)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.18` → IC=+0.226 (n=1069)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.18 (IC base=+0.010)

- **PATRÓN** `volumen_regimen` > `0.6955` → IC=+0.219 (n=2270)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6955 (IC base=+0.010)

- **PATRÓN** `volumen_pendiente_norm` > `0.274` → IC=+0.246 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.274 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` < `1.4146` → IC=+0.229 (n=838)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4146 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` > `2.4496` → IC=+0.220 (n=837)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4496 (IC base=+0.010)

- **PATRÓN** `ballena_activa_n` < `370.0` → IC=+0.232 (n=2513)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 370.0 (IC base=+0.010)

- **PATRÓN** `dist_vwap_pct` < `0.7352` → IC=+0.257 (n=2335)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7352 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` > `1.018` → IC=+0.265 (n=858)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.018 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2713` → IC=+0.290 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2713 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.5339` → IC=+0.256 (n=809)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5339 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` > `2.1516` → IC=+0.262 (n=833)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1516 (IC base=+0.005)

- **PATRÓN** `ballena_activa_n` < `197.0` → IC=+0.277 (n=818)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 197.0 (IC base=+0.005)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0116` → IC=+0.318 (n=1625)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0116 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.294 (n=3598)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.284)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.323 (n=1935)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.586` → IC=+0.306 (n=2431)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.586 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` < `0.1307` → IC=+0.292 (n=3335)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1307 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` > `3.2535` → IC=+0.300 (n=1163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.2535 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.292 (n=4333)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `2018.8832` → IC=+0.296 (n=1195)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2018.8832 (IC base=+0.284)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.302 (n=2209)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.336 (n=2225)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.308)

- **PATRÓN** `drift_60min` |x|≤ `0.1874` → IC=+0.328 (n=1468)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1874 (IC base=+0.308)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.325 (n=1281)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.308)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.311 (n=1508)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.308)

- **PATRÓN** `ibs_20min` < `0.3929` → IC=+0.308 (n=3334)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3929 (IC base=+0.308)

- **PATRÓN** `ibs_20min` > `0.1538` → IC=+0.318 (n=2223)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1538 (IC base=+0.308)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.057` → IC=+0.318 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.057 (IC base=+0.308)

- **PATRÓN** `volumen_pendiente_norm` < `0.1991` → IC=+0.309 (n=3311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1991 (IC base=+0.308)

- **PATRÓN** `volumen_pendiente_norm` > `0.3441` → IC=+0.316 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3441 (IC base=+0.308)

- **PATRÓN** `volumen_spike_ratio` > `2.7404` → IC=+0.325 (n=1464)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7404 (IC base=+0.308)

- **PATRÓN** `libro_liquidez` > `2004.4248` → IC=+0.318 (n=1111)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2004.4248 (IC base=+0.308)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.312 (n=2243)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.308)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **PATRÓN** `dist_vwap_pct` > `0.1571` → IC=+0.236 (n=1180)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1571 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` < `0.6284` → IC=+0.236 (n=2609)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6284 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` < `1.1664` → IC=+0.236 (n=2375)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1664 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` > `0.5961` → IC=+0.234 (n=2376)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5961 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` < `0.1635` → IC=+0.236 (n=2494)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1635 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.1032` → IC=+0.243 (n=776)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1032 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` < `2.4147` → IC=+0.241 (n=2306)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4147 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` > `1.4963` → IC=+0.235 (n=2061)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4963 (IC base=+0.024)

- **PATRÓN** `ballena_activa_n` < `113.0` → IC=+0.252 (n=2362)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 113.0 (IC base=+0.024)

- **PATRÓN** `ibs_20min` < `0.0913` → IC=+0.152 (n=1645)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.0913 (IC base=+0.012)

- **PATRÓN** `dist_vwap_pct` < `0.381` → IC=+0.261 (n=1921)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.381 (IC base=+0.012)

- **PATRÓN** `volumen_regimen` < `1.1802` → IC=+0.264 (n=1732)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1802 (IC base=+0.012)

- **PATRÓN** `volumen_regimen` > `0.6147` → IC=+0.259 (n=1732)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6147 (IC base=+0.012)

- **PATRÓN** `volumen_pendiente_norm` < `0.1017` → IC=+0.266 (n=1627)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1017 (IC base=+0.012)

- **PATRÓN** `volumen_pendiente_norm` > `0.1623` → IC=+0.285 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1623 (IC base=+0.012)

- **PATRÓN** `volumen_spike_ratio` < `1.7847` → IC=+0.283 (n=1114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7847 (IC base=+0.012)

- **PATRÓN** `volumen_spike_ratio` > `2.4256` → IC=+0.276 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4256 (IC base=+0.012)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.282 (n=1698)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.012)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.75` → IC=-0.247 (n=2686)

  - _Acción_: SKIP cuando `ibs_20min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.314 (n=2691)

- **FILTRO** `ibs_20min` > `0.6078` → IC=-0.238 (n=1267)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6078
  - _Potencial_: sin este filtro IC_bueno=+0.165 (n=3803)

- **FILTRO** `sigma_ewma_delta_pct` > `8.236` → IC=-0.265 (n=580)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.236
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=4490)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.314 (n=2691)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.75 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` > `1.1116` → IC=+0.352 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1116 (IC base=+0.034)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.439` → IC=+0.158 (n=2199)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 2.439 (IC base=+0.034)

- **PATRÓN** `volumen_regimen` < `0.8445` → IC=+0.349 (n=1312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8445 (IC base=+0.034)

- **PATRÓN** `volumen_regimen` > `0.6972` → IC=+0.335 (n=1758)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6972 (IC base=+0.034)

- **PATRÓN** `volumen_pendiente_norm` < `0.0993` → IC=+0.337 (n=1854)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0993 (IC base=+0.034)

- **PATRÓN** `volumen_pendiente_norm` > `0.2747` → IC=+0.367 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2747 (IC base=+0.034)

- **PATRÓN** `volumen_spike_ratio` < `1.4314` → IC=+0.362 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4314 (IC base=+0.034)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.353 (n=1718)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.034)

- **PATRÓN** `ibs_20min` < `0.6078` → IC=+0.165 (n=3803)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.6078 (IC base=+0.065)

- **PATRÓN** `dist_vwap_pct` < `0.3259` → IC=+0.274 (n=2040)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3259 (IC base=+0.065)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.728` → IC=+0.133 (n=3973)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 4.728 (IC base=+0.065)

- **PATRÓN** `volumen_regimen` < `0.6899` → IC=+0.287 (n=870)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6899 (IC base=+0.065)

- **PATRÓN** `volumen_pendiente_norm` > `0.0716` → IC=+0.299 (n=791)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0716 (IC base=+0.065)

- **PATRÓN** `volumen_spike_ratio` < `1.7979` → IC=+0.284 (n=1279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7979 (IC base=+0.065)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.292 (n=1952)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 45.0 (IC base=+0.065)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.353 (n=2510)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.313)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.317 (n=2834)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.313)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.316 (n=2946)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.313)

- **PATRÓN** `ibs_20min` > `0.651` → IC=+0.338 (n=2806)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.651 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` > `0.2197` → IC=+0.337 (n=1503)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2197 (IC base=+0.313)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.817` → IC=+0.337 (n=1099)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.817 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` > `0.629` → IC=+0.325 (n=2806)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.629 (IC base=+0.313)

- **PATRÓN** `volumen_pendiente_norm` > `0.2844` → IC=+0.347 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2844 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` > `1.5322` → IC=+0.325 (n=2421)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5322 (IC base=+0.313)

- **PATRÓN** `libro_liquidez` > `3007.7146` → IC=+0.322 (n=936)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3007.7146 (IC base=+0.313)

- **PATRÓN** `sigma_h` > `0.0141` → IC=+0.349 (n=2018)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0141 (IC base=+0.313)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.316 (n=3034)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.313)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.314 (n=3032)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.313)

- **PATRÓN** `ibs_20min` < `0.3889` → IC=+0.328 (n=3028)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3889 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` > `1.3008` → IC=+0.322 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.3008 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` < `0.2571` → IC=+0.316 (n=2981)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2571 (IC base=+0.313)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.169` → IC=+0.325 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.169 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` < `0.7156` → IC=+0.315 (n=1334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7156 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` > `1.2096` → IC=+0.340 (n=1009)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2096 (IC base=+0.313)

- **PATRÓN** `volumen_pendiente_norm` > `0.2864` → IC=+0.365 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2864 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` < `1.4133` → IC=+0.323 (n=948)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4133 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` > `2.1457` → IC=+0.316 (n=1288)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1457 (IC base=+0.313)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.220 (n=6371)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0127 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.1261` → IC=+0.193 (n=8410)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1261 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=19877)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.5357` → IC=+0.229 (n=19115)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5357 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.1693` → IC=+0.206 (n=7215)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1693 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.742` → IC=+0.260 (n=3741)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.742 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `1.1739` → IC=+0.152 (n=12742)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1739 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `0.6215` → IC=+0.151 (n=12742)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6215 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.293` → IC=+0.207 (n=2752)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.293 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.598` → IC=+0.184 (n=6203)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.598 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.191 (n=18071)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 85.0 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.194 (n=8403)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0061 (IC base=+0.186)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.186 (n=12718)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0082 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.0849` → IC=+0.222 (n=6356)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0849 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.207 (n=9166)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` < `0.526` → IC=+0.238 (n=19060)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.526 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` < `0.1952` → IC=+0.180 (n=13913)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.1952 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.428` → IC=+0.191 (n=3011)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 9.428 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.489` → IC=+0.192 (n=17023)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 2.489 (IC base=+0.186)

- **PATRÓN** `volumen_regimen` < `1.1891` → IC=+0.166 (n=13507)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1891 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.2952` → IC=+0.219 (n=2863)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2952 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `2.6325` → IC=+0.197 (n=6075)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.6325 (IC base=+0.186)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.200 (n=18035)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 89.0 (IC base=+0.186)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.263 (n=1045)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.228)

- **PATRÓN** `drift_60min` |x|≤ `0.0748` → IC=+0.264 (n=1045)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0748 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.236 (n=3275)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.228)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.229 (n=2127)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` > `0.9416` → IC=+0.293 (n=2090)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9416 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.458` → IC=+0.328 (n=1029)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.458 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` > `0.2318` → IC=+0.281 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2318 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` < `1.8314` → IC=+0.226 (n=2000)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8314 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `1.4374` → IC=+0.228 (n=3001)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4374 (IC base=+0.228)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=3423)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.228)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.256 (n=2639)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.253)

- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.262 (n=1761)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0078 (IC base=+0.253)

- **PATRÓN** `drift_60min` |x|≤ `0.1001` → IC=+0.306 (n=1161)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1001 (IC base=+0.253)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.257 (n=2724)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.253)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.259 (n=2402)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.253)

- **PATRÓN** `ibs_20min` < `0.4432` → IC=+0.271 (n=2639)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4432 (IC base=+0.253)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.934` → IC=+0.258 (n=2610)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.934 (IC base=+0.253)

- **PATRÓN** `volumen_pendiente_norm` < `0.0741` → IC=+0.257 (n=2198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0741 (IC base=+0.253)

- **PATRÓN** `volumen_pendiente_norm` > `0.3008` → IC=+0.266 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3008 (IC base=+0.253)

- **PATRÓN** `volumen_spike_ratio` < `1.5528` → IC=+0.264 (n=1116)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5528 (IC base=+0.253)

- **PATRÓN** `volumen_spike_ratio` > `2.6907` → IC=+0.256 (n=846)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6907 (IC base=+0.253)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.262 (n=1832)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.253)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.188 (n=975)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0033 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.0673` → IC=+0.174 (n=975)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0673 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.144 (n=3052)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.2517` → IC=+0.204 (n=2920)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2517 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.1942` → IC=+0.210 (n=1424)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1942 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.547` → IC=+0.205 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.547 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.8528` → IC=+0.132 (n=1947)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.8528 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` > `1.1961` → IC=+0.132 (n=974)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 1.1961 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.173 (n=447)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.5077` → IC=+0.130 (n=1265)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.5077 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `2.4553` → IC=+0.142 (n=958)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.4553 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `389.0` → IC=+0.131 (n=2845)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 389.0 (IC base=+0.127)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.174 (n=3155)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0069 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.254` → IC=+0.175 (n=2776)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.254 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.180 (n=1509)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.6119` → IC=+0.211 (n=3155)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6119 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.2181` → IC=+0.177 (n=3424)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.2181 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.904` → IC=+0.179 (n=583)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 10.904 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.998` → IC=+0.157 (n=2768)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 3.998 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `1.2053` → IC=+0.162 (n=3155)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2053 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` < `0.0719` → IC=+0.155 (n=2635)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.0719 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.4814` → IC=+0.157 (n=3028)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4814 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `203.0` → IC=+0.194 (n=1303)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 203.0 (IC base=+0.153)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.226 (n=1467)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.2556` → IC=+0.233 (n=2155)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2556 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.218 (n=3381)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.288 (n=1713)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.023` → IC=+0.305 (n=766)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.023 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.3498` → IC=+0.236 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3498 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `2.7105` → IC=+0.222 (n=1433)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7105 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.213 (n=3931)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `2014.5756` → IC=+0.221 (n=1078)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2014.5756 (IC base=+0.209)

- **PATRÓN** `sigma_h` < `0.0122` → IC=+0.245 (n=2917)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0122 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.2512` → IC=+0.268 (n=1944)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2512 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.276 (n=1108)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0417` → IC=+0.295 (n=1284)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0417 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.837` → IC=+0.288 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.837 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.3531` → IC=+0.285 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3531 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.7655` → IC=+0.242 (n=1244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7655 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.1747` → IC=+0.254 (n=1884)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1747 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1882.5784` → IC=+0.249 (n=1322)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1882.5784 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.238 (n=1868)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=+0.240)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.194 (n=1052)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0039 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.0814` → IC=+0.172 (n=1051)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.0814 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=3269)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.2448` → IC=+0.188 (n=3153)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.2448 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.1481` → IC=+0.187 (n=1783)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1481 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.231` → IC=+0.203 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.231 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8368` → IC=+0.138 (n=2102)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.8368 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2874` → IC=+0.176 (n=473)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2874 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.5176` → IC=+0.127 (n=1358)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.5176 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.5044` → IC=+0.136 (n=1029)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.5044 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `6938.502` → IC=+0.196 (n=1430)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 6938.502 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `123.0` → IC=+0.127 (n=3098)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 123.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.174 (n=2253)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0057 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.4286` → IC=+0.149 (n=3378)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4286 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.165 (n=1623)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.6682` → IC=+0.189 (n=3378)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.6682 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.17` → IC=+0.157 (n=3451)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.17 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.508` → IC=+0.141 (n=1155)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 6.508 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.853` → IC=+0.152 (n=2252)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.853 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.2937` → IC=+0.170 (n=510)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2937 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.189` → IC=+0.135 (n=2832)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.189 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.4105` → IC=+0.136 (n=3216)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4105 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `6675.8703` → IC=+0.191 (n=1532)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 6675.8703 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.155 (n=1092)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 48.0 (IC base=+0.133)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.013` → IC=+0.172 (n=1171)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.013 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.136 (n=3617)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.5937` → IC=+0.225 (n=3140)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5937 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `0.7969` → IC=+0.213 (n=897)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7969 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.0` → IC=+0.285 (n=741)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.0 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `1.1668` → IC=+0.131 (n=3515)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.1668 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` > `0.6273` → IC=+0.123 (n=3513)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.6273 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` < `0.1628` → IC=+0.124 (n=3591)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1628 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `1.7887` → IC=+0.127 (n=2274)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.7887 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2712.4658` → IC=+0.197 (n=1593)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2712.4658 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.129 (n=1192)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 16.0 (IC base=+0.121)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.151 (n=3251)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0111 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.1187` → IC=+0.167 (n=1231)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1187 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=3766)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` < `0.6442` → IC=+0.222 (n=3688)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6442 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` < `0.2269` → IC=+0.147 (n=3660)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.2269 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.229` → IC=+0.146 (n=3264)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 2.229 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `1.1798` → IC=+0.130 (n=3688)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1798 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.8596` → IC=+0.126 (n=2459)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.8596 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` < `0.1632` → IC=+0.127 (n=3648)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1632 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2764` → IC=+0.148 (n=512)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2764 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.437` → IC=+0.142 (n=1168)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.437 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.4431` → IC=+0.135 (n=1168)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.4431 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `2611.9184` → IC=+0.190 (n=1672)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2611.9184 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.131 (n=3505)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 43.0 (IC base=+0.124)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.246 (n=3156)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.1682` → IC=+0.242 (n=1389)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1682 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=3283)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=2849)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.6647` → IC=+0.256 (n=3156)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6647 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.1865` → IC=+0.235 (n=1945)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1865 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` < `0.8391` → IC=+0.228 (n=3248)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8391 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.475` → IC=+0.271 (n=774)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.475 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `0.6192` → IC=+0.236 (n=3156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6192 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2874` → IC=+0.268 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2874 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `2.4732` → IC=+0.228 (n=3080)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4732 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.8264` → IC=+0.229 (n=2053)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8264 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2627.6354` → IC=+0.233 (n=2104)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2627.6354 (IC base=+0.226)

- **PATRÓN** `sigma_h` > `0.0164` → IC=+0.248 (n=2191)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0164 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.615` → IC=+0.248 (n=3286)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.615 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.248 (n=1620)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.242 (n=1477)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.0381` → IC=+0.297 (n=1446)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0381 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` > `0.3257` → IC=+0.245 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3257 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.046` → IC=+0.272 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.046 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` < `0.8668` → IC=+0.241 (n=2191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8668 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` > `1.0472` → IC=+0.243 (n=1490)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0472 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2847` → IC=+0.293 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2847 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.8474` → IC=+0.236 (n=2077)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8474 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `1.5546` → IC=+0.239 (n=2783)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5546 (IC base=+0.238)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.203 (n=1682)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.1435` → IC=+0.172 (n=2211)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1435 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.166 (n=5253)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.6608` → IC=+0.221 (n=3350)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6608 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.908` → IC=+0.179 (n=778)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.908 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.514` → IC=+0.210 (n=813)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.514 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `0.8564` → IC=+0.164 (n=3047)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8564 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` > `1.1883` → IC=+0.158 (n=1524)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 1.1883 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.1555` → IC=+0.171 (n=1298)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.1555 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.5258` → IC=+0.160 (n=2158)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.5258 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.157 (n=5546)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.02 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `7207.1498` → IC=+0.194 (n=2278)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 7207.1498 (IC base=+0.154)

- **PATRÓN** `ibs_20min` < `0.3878` → IC=+0.178 (n=3655)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.3878 (IC base=+0.102)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.148 (n=2414)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 22.0 (IC base=+0.102)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.206 (n=1204)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0063 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.1055` → IC=+0.234 (n=531)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1055 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.229 (n=1088)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` > `0.6264` → IC=+0.260 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6264 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` > `0.3251` → IC=+0.232 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3251 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.927` → IC=+0.226 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.927 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` < `0.6261` → IC=+0.230 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6261 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.0903` → IC=+0.213 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0903 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` < `2.1519` → IC=+0.211 (n=1039)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1519 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `13762.5784` → IC=+0.205 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13762.5784 (IC base=+0.197)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.156 (n=504)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0032 (IC base=+0.069)

- **PATRÓN** `ibs_20min` < `0.2186` → IC=+0.191 (n=661)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.2186 (IC base=+0.069)

- **PATRÓN** `ballena_activa_n` < `171.0` → IC=+0.163 (n=651)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 171.0 (IC base=+0.069)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.239 (n=519)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.1323` → IC=+0.158 (n=680)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1323 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=1609)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.77` → IC=+0.260 (n=701)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.77 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.1568` → IC=+0.168 (n=739)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1568 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.947` → IC=+0.186 (n=218)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 9.947 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.8322` → IC=+0.158 (n=1031)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8322 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.2177` → IC=+0.185 (n=271)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2177 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.4693` → IC=+0.169 (n=508)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.4693 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `7908.6344` → IC=+0.180 (n=701)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 7908.6344 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.150 (n=515)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 30.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.121 (n=1542)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0081 (IC base=+0.109)

- **PATRÓN** `ibs_20min` < `0.0885` → IC=+0.215 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0885 (IC base=+0.109)

- **PATRÓN** `volumen_regimen` < `0.6743` → IC=+0.144 (n=678)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.6743 (IC base=+0.109)

- **PATRÓN** `volumen_pendiente_norm` > `0.2229` → IC=+0.130 (n=263)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` > 0.2229 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `5598.5419` → IC=+0.151 (n=1026)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 5598.5419 (IC base=+0.109)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.150 (n=664)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 40.0 (IC base=+0.109)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.154 (n=458)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0071 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.152 (n=972)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 11.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` > `0.5312` → IC=+0.181 (n=1227)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.5312 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` > `1.0555` → IC=+0.148 (n=245)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 1.0555 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.873` → IC=+0.225 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.873 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` < `1.0461` → IC=+0.126 (n=1208)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.0461 (IC base=+0.116)

- **PATRÓN** `volumen_pendiente_norm` > `0.2221` → IC=+0.136 (n=234)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.2221 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` < `1.4134` → IC=+0.148 (n=444)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.4134 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `3060.0718` → IC=+0.152 (n=458)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3060.0718 (IC base=+0.116)

- **PATRÓN** `ibs_20min` < `0.5536` → IC=+0.170 (n=1330)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.5536 (IC base=+0.091)

- **PATRÓN** `libro_liquidez` > `2772.6331` → IC=+0.166 (n=686)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2772.6331 (IC base=+0.091)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.121 (n=1301)

  - _Acción_: Kelly boost +0.60€ cuando `ballena_activa_n` < 27.0 (IC base=+0.091)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0152` → IC=+0.238 (n=300)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0152 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.223 (n=211)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` < `0.8608` → IC=+0.182 (n=397)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.8608 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `0.5179` → IC=+0.196 (n=402)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.5179 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.931` → IC=+0.199 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.931 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` < `1.146` → IC=+0.181 (n=516)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 1.146 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.516` → IC=+0.193 (n=451)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 5.516 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` > `1.1874` → IC=+0.250 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1874 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` < `0.2439` → IC=+0.195 (n=483)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.2439 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.0802` → IC=+0.211 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0802 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` < `2.129` → IC=+0.196 (n=370)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.129 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `1.4145` → IC=+0.187 (n=420)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 1.4145 (IC base=+0.179)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.192 (n=475)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.03 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `2727.8122` → IC=+0.202 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2727.8122 (IC base=+0.179)

- **PATRÓN** `sigma_h` < `0.0261` → IC=+0.161 (n=496)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0261 (IC base=+0.156)

- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.173 (n=496)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0105 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.3414` → IC=+0.164 (n=331)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.3414 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.201 (n=242)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` < `0.6082` → IC=+0.171 (n=496)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.6082 (IC base=+0.156)

- **PATRÓN** `ibs_20min` > `0.1049` → IC=+0.163 (n=496)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.1049 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `1.1964` → IC=+0.275 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1964 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` < `0.2927` → IC=+0.158 (n=460)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.2927 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.153` → IC=+0.160 (n=601)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` < 9.153 (IC base=+0.156)

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

- **PATRÓN** `libro_liquidez` > `2269.2904` → IC=+0.161 (n=443)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2269.2904 (IC base=+0.156)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.172 (n=476)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 20.0 (IC base=+0.156)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0128` → IC=+0.227 (n=8410)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0128 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=26354)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.967` → IC=+0.301 (n=8407)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.967 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.9466` → IC=+0.216 (n=2934)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9466 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.912` → IC=+0.261 (n=6174)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.912 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.2131` → IC=+0.160 (n=17005)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2131 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2922` → IC=+0.216 (n=3310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2922 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6243` → IC=+0.193 (n=8214)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6243 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.200 (n=23853)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.207 (n=7816)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.1533` → IC=+0.202 (n=10315)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1533 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=8795)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.4865` → IC=+0.253 (n=20626)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4865 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` < `0.1901` → IC=+0.182 (n=14963)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.1901 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.504` → IC=+0.205 (n=21838)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.504 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `0.6284` → IC=+0.179 (n=5239)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.6284 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.2936` → IC=+0.255 (n=3226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2936 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `2.6209` → IC=+0.211 (n=7514)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6209 (IC base=+0.199)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.214 (n=22331)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.199)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.274 (n=1344)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.3766` → IC=+0.235 (n=4021)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3766 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.240 (n=4226)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.235 (n=2703)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` > `0.8611` → IC=+0.294 (n=2682)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8611 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.026` → IC=+0.301 (n=2638)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.026 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.233` → IC=+0.288 (n=711)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.233 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.288` → IC=+0.240 (n=1765)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.288 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.247 (n=4361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `2043.5843` → IC=+0.241 (n=1341)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2043.5843 (IC base=+0.234)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.267 (n=3675)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.266)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.268 (n=2449)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.266)

- **PATRÓN** `drift_60min` |x|≤ `0.1273` → IC=+0.292 (n=1616)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1273 (IC base=+0.266)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.267 (n=3820)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.266)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.270 (n=3302)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.266)

- **PATRÓN** `ibs_20min` < `0.4667` → IC=+0.287 (n=3231)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4667 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` < `0.0984` → IC=+0.269 (n=3346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0984 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` > `0.2925` → IC=+0.284 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2925 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` < `1.5672` → IC=+0.267 (n=1556)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5672 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` > `2.6471` → IC=+0.274 (n=1179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6471 (IC base=+0.266)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.271 (n=2532)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.266)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.272 (n=1300)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.266)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.174 (n=1391)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0033 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.082` → IC=+0.146 (n=1383)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.082 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=4327)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.3022` → IC=+0.202 (n=3703)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3022 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.3441` → IC=+0.201 (n=1310)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3441 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.267` → IC=+0.171 (n=863)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 9.267 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.6348` → IC=+0.155 (n=1382)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6348 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `1.2251` → IC=+0.145 (n=1382)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.2251 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2719` → IC=+0.194 (n=582)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2719 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.1664` → IC=+0.144 (n=3587)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.1664 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.5201` → IC=+0.144 (n=3641)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.5201 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `290.0` → IC=+0.152 (n=2691)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 290.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.171 (n=3229)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.006 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.0834` → IC=+0.175 (n=1224)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.0834 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=1357)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` < `0.6806` → IC=+0.192 (n=3670)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.6806 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.1541` → IC=+0.162 (n=3612)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1541 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.205` → IC=+0.151 (n=3745)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 6.205 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `1.0404` → IC=+0.156 (n=3229)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.0404 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.2211` → IC=+0.197 (n=671)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2211 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.4323` → IC=+0.150 (n=3559)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4323 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `1.7707` → IC=+0.151 (n=2373)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.7707 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.147 (n=4765)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `212.0` → IC=+0.178 (n=1164)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 212.0 (IC base=+0.146)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0134` → IC=+0.239 (n=1398)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0134 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=4403)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.300 (n=1555)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.973` → IC=+0.315 (n=933)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.973 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.3485` → IC=+0.234 (n=551)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3485 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.7559` → IC=+0.239 (n=1862)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7559 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.229 (n=5099)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `1904.7172` → IC=+0.235 (n=1901)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1904.7172 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0113` → IC=+0.248 (n=3570)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0113 (IC base=+0.245)

- **PATRÓN** `drift_60min` |x|≤ `0.1843` → IC=+0.258 (n=1785)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1843 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.263 (n=1545)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.249 (n=1845)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.0676` → IC=+0.299 (n=1356)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0676 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.949` → IC=+0.304 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.949 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.3466` → IC=+0.300 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3466 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `2.1697` → IC=+0.257 (n=2617)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1697 (IC base=+0.245)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.248 (n=1962)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `2000.6` → IC=+0.253 (n=1352)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2000.6 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.248 (n=3463)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.245)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.191 (n=1459)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0039 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.3536` → IC=+0.147 (n=3839)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3536 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=4536)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.8785` → IC=+0.268 (n=1454)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8785 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.1486` → IC=+0.166 (n=2162)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1486 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.181` → IC=+0.169 (n=869)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 9.181 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.8575` → IC=+0.153 (n=2909)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8575 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2786` → IC=+0.200 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2786 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.5168` → IC=+0.156 (n=1876)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.5168 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `2.1553` → IC=+0.143 (n=1933)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.1553 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `5838.1861` → IC=+0.231 (n=1978)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5838.1861 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.143 (n=2846)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 85.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0082` → IC=+0.168 (n=3692)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0082 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.4585` → IC=+0.160 (n=3687)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.4585 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=1361)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.5696` → IC=+0.214 (n=3244)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5696 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `0.6317` → IC=+0.157 (n=4268)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.6317 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.022` → IC=+0.153 (n=739)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 9.022 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.018` → IC=+0.154 (n=3208)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 3.018 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.852` → IC=+0.162 (n=2458)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.852 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.2929` → IC=+0.205 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2929 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.1971` → IC=+0.154 (n=3143)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.1971 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.5242` → IC=+0.158 (n=3191)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.5242 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `6725.1528` → IC=+0.215 (n=1229)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6725.1528 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.171 (n=1236)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 57.0 (IC base=+0.151)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0131` → IC=+0.158 (n=1480)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0131 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.149 (n=3150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` > `0.6966` → IC=+0.256 (n=2958)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6966 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `1.0616` → IC=+0.201 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0616 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.219` → IC=+0.271 (n=1131)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.219 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.2099` → IC=+0.126 (n=4438)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.2099 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.1011` → IC=+0.122 (n=4226)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1011 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.137 (n=555)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.5569` → IC=+0.135 (n=1906)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.5569 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2477.3162` → IC=+0.223 (n=2012)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2477.3162 (IC base=+0.120)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.159 (n=3645)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0112 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.1427` → IC=+0.151 (n=1379)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.1427 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.149 (n=4260)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.5394` → IC=+0.247 (n=3640)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5394 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.2241` → IC=+0.153 (n=3811)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.2241 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.03` → IC=+0.161 (n=4017)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` < 3.03 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.193` → IC=+0.142 (n=4137)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.193 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2308` → IC=+0.201 (n=724)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2308 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.4366` → IC=+0.163 (n=1316)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.4366 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `2.4772` → IC=+0.141 (n=1316)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.4772 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `2653.9292` → IC=+0.222 (n=1379)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2653.9292 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.151 (n=3968)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 48.0 (IC base=+0.137)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.256 (n=4061)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.243 (n=4247)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.242 (n=2712)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` > `0.9873` → IC=+0.306 (n=1356)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9873 (IC base=+0.237)

- **PATRÓN** `dist_vwap_pct` > `0.204` → IC=+0.252 (n=2069)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.204 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.05` → IC=+0.295 (n=720)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.05 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` < `1.2138` → IC=+0.237 (n=4059)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2138 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` > `0.6424` → IC=+0.243 (n=4059)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6424 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.0792` → IC=+0.255 (n=1614)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0792 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.5093` → IC=+0.257 (n=1325)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5093 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `3000.2954` → IC=+0.239 (n=1353)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3000.2954 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0249` → IC=+0.270 (n=1408)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0249 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.250 (n=3976)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` < `0.1374` → IC=+0.306 (n=1857)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1374 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` > `1.1899` → IC=+0.249 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1899 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` < `0.2307` → IC=+0.249 (n=4058)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2307 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.981` → IC=+0.278 (n=791)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.981 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` < `0.7152` → IC=+0.247 (n=1858)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7152 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` > `1.2189` → IC=+0.265 (n=1407)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2189 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` > `0.2864` → IC=+0.312 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2864 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `1.4331` → IC=+0.248 (n=4006)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4331 (IC base=+0.244)

- **PATRÓN** `libro_liquidez` > `2986.2232` → IC=+0.244 (n=1407)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2986.2232 (IC base=+0.244)

### GBM_LATE_5M
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.240 (n=2420)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.5355` → IC=+0.232 (n=7248)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5355 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.231 (n=7295)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `0.9293` → IC=+0.260 (n=2416)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9293 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` < `0.9533` → IC=+0.225 (n=5902)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9533 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.446` → IC=+0.231 (n=2412)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.446 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` < `0.707` → IC=+0.230 (n=2251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.707 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` > `0.8813` → IC=+0.224 (n=3410)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8813 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` < `0.104` → IC=+0.224 (n=6789)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.104 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.165` → IC=+0.231 (n=2029)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.165 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` < `1.4485` → IC=+0.235 (n=2377)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4485 (IC base=+0.223)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.227 (n=5182)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `3729.2688` → IC=+0.231 (n=4832)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3729.2688 (IC base=+0.223)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.229 (n=1723)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.212)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.214 (n=3437)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.5302` → IC=+0.220 (n=5152)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5302 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.226 (n=1741)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.223 (n=2301)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.7292` → IC=+0.217 (n=5155)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7292 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.7039` → IC=+0.219 (n=880)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7039 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` < `0.1883` → IC=+0.204 (n=4347)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1883 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.732` → IC=+0.225 (n=4681)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.732 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `1.2493` → IC=+0.211 (n=4679)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2493 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.215 (n=4767)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.5304` → IC=+0.217 (n=2233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5304 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `1.8123` → IC=+0.218 (n=3384)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8123 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.236 (n=3391)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 51.0 (IC base=+0.212)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.280 (n=833)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.270)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.272 (n=946)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0033 (IC base=+0.270)

- **PATRÓN** `drift_60min` |x|≤ `0.0855` → IC=+0.302 (n=316)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0855 (IC base=+0.270)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.280 (n=949)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.270)

- **PATRÓN** `ibs_20min` < `0.4633` → IC=+0.285 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4633 (IC base=+0.270)

- **PATRÓN** `dist_vwap_pct` < `0.6801` → IC=+0.278 (n=1103)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6801 (IC base=+0.270)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.129` → IC=+0.298 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.129 (IC base=+0.270)

- **PATRÓN** `volumen_regimen` < `1.2271` → IC=+0.275 (n=946)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2271 (IC base=+0.270)

- **PATRÓN** `volumen_regimen` > `0.8769` → IC=+0.288 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8769 (IC base=+0.270)

- **PATRÓN** `volumen_pendiente_norm` > `0.2875` → IC=+0.341 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2875 (IC base=+0.270)

- **PATRÓN** `volumen_spike_ratio` < `2.4917` → IC=+0.278 (n=941)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4917 (IC base=+0.270)

- **PATRÓN** `volumen_spike_ratio` > `1.4175` → IC=+0.272 (n=941)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4175 (IC base=+0.270)

- **PATRÓN** `libro_liquidez` > `12913.0263` → IC=+0.282 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12913.0263 (IC base=+0.270)

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

- **PATRÓN** `volumen_pendiente_norm` < `0.272` → IC=+0.176 (n=1820)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` < 0.272 (IC base=+0.172)

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
- **PATRÓN** `drift_60min` |x|≤ `0.6167` → IC=+0.215 (n=1057)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6167 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.230 (n=960)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` < `0.7078` → IC=+0.211 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7078 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `0.988` → IC=+0.251 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.988 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.32` → IC=+0.245 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.32 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.2054` → IC=+0.245 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2054 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `1.7962` → IC=+0.215 (n=941)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7962 (IC base=+0.208)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.218 (n=933)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.208)

- **PATRÓN** `sigma_h` > `0.0179` → IC=+0.371 (n=29)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0179 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `19.0` → IC=+0.389 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 19.0 (IC base=+0.288)

- **PATRÓN** `ibs_20min` < `0.4483` → IC=+0.303 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4483 (IC base=+0.288)

- **PATRÓN** `ibs_20min` > `0.1912` → IC=+0.309 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1912 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.341` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.341 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.368` → IC=+0.291 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.368 (IC base=+0.288)

- **PATRÓN** `volumen_pendiente_norm` > `0.2913` → IC=+0.382 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2913 (IC base=+0.288)

- **PATRÓN** `volumen_spike_ratio` < `1.6184` → IC=+0.306 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6184 (IC base=+0.288)

- **PATRÓN** `volumen_spike_ratio` > `1.8484` → IC=+0.300 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8484 (IC base=+0.288)

- **PATRÓN** `ballena_activa_n` < `5.0` → IC=+0.379 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 5.0 (IC base=+0.288)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0086` → IC=+0.222 (n=1960)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0086 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.4664` → IC=+0.219 (n=1959)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4664 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.223 (n=1754)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` < `0.472` → IC=+0.223 (n=1306)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.472 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.147` → IC=+0.213 (n=1959)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.147 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` < `0.4154` → IC=+0.223 (n=1961)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4154 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.936` → IC=+0.222 (n=1780)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.936 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` < `0.8667` → IC=+0.217 (n=1306)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8667 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` < `0.1006` → IC=+0.214 (n=1816)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1006 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.0746` → IC=+0.211 (n=818)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0746 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.4029` → IC=+0.228 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4029 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.4939` → IC=+0.212 (n=1708)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4939 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.241 (n=527)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.5077` → IC=+0.222 (n=1581)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5077 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.216 (n=607)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.216 (n=1123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `0.0841` → IC=+0.214 (n=1581)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0841 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `0.6904` → IC=+0.220 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6904 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.284` → IC=+0.211 (n=1440)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.284 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` < `1.2516` → IC=+0.214 (n=1581)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2516 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` > `0.7209` → IC=+0.210 (n=1412)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7209 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.0715` → IC=+0.228 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0715 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `1.5069` → IC=+0.210 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5069 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `1.7691` → IC=+0.210 (n=1032)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7691 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=2083)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `7886.4805` → IC=+0.216 (n=1054)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7886.4805 (IC base=+0.207)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.210 (n=1576)

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

- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.258 (n=631)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.249)

- **PATRÓN** `drift_60min` |x|≤ `0.6877` → IC=+0.262 (n=945)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6877 (IC base=+0.249)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.249 (n=877)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.249)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.270 (n=649)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.249)

- **PATRÓN** `ibs_20min` < `0.7347` → IC=+0.272 (n=946)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7347 (IC base=+0.249)

- **PATRÓN** `dist_vwap_pct` > `0.6006` → IC=+0.252 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6006 (IC base=+0.249)

- **PATRÓN** `dist_vwap_pct` < `1.2199` → IC=+0.256 (n=1082)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 1.2199 (IC base=+0.249)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.987` → IC=+0.267 (n=895)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.987 (IC base=+0.249)

- **PATRÓN** `volumen_regimen` < `0.6688` → IC=+0.263 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6688 (IC base=+0.249)

- **PATRÓN** `volumen_pendiente_norm` < `0.1033` → IC=+0.259 (n=846)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1033 (IC base=+0.249)

- **PATRÓN** `volumen_spike_ratio` > `2.1886` → IC=+0.276 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1886 (IC base=+0.249)

- **PATRÓN** `libro_liquidez` > `4602.0324` → IC=+0.279 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4602.0324 (IC base=+0.249)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.280 (n=833)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.249)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.150 (n=879)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0041 (IC base=+0.063)

- **PATRÓN** `ibs_20min` > `0.7505` → IC=+0.191 (n=1696)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.7505 (IC base=+0.063)

- **PATRÓN** `dist_vwap_pct` > `0.157` → IC=+0.149 (n=1217)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.157 (IC base=+0.063)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.425` → IC=+0.143 (n=556)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 10.425 (IC base=+0.063)

- **PATRÓN** `ibs_20min` < `0.5926` → IC=+0.166 (n=1935)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.5926 (IC base=+0.082)

- **PATRÓN** `volumen_pendiente_norm` > `0.1502` → IC=+0.176 (n=541)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1502 (IC base=+0.082)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.5427` → IC=-0.121 (n=333)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5427
  - _Potencial_: sin este filtro IC_bueno=+0.160 (n=678)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.174 (n=265)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0029 (IC base=+0.067)

- **PATRÓN** `ibs_20min` > `0.5427` → IC=+0.160 (n=678)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.5427 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` > `0.1288` → IC=+0.166 (n=357)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1288 (IC base=+0.067)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.128 (n=318)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0037 (IC base=+0.052)

- **PATRÓN** `ibs_20min` < `0.0659` → IC=+0.247 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0659 (IC base=+0.052)

- **PATRÓN** `volumen_pendiente_norm` > `0.0703` → IC=+0.142 (n=300)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.0703 (IC base=+0.052)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.6272` → IC=-0.149 (n=186)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6272
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=562)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.156 (n=361)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0043 (IC base=+0.064)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.129 (n=316)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.064)

- **PATRÓN** `ibs_20min` > `0.9316` → IC=+0.251 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9316 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` > `0.135` → IC=+0.158 (n=378)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.135 (IC base=+0.064)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.755` → IC=+0.176 (n=171)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 11.755 (IC base=+0.064)

- **PATRÓN** `ibs_20min` < `0.0953` → IC=+0.279 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0953 (IC base=+0.040)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.7222` → IC=+0.145 (n=590)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.7222 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` > `0.7614` → IC=+0.151 (n=213)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.7614 (IC base=+0.034)

- **PATRÓN** `sigma_h` < `0.0101` → IC=+0.168 (n=387)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0101 (IC base=+0.099)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.192 (n=554)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.5 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` < `0.2139` → IC=+0.150 (n=547)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.2139 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.967` → IC=+0.246 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.967 (IC base=+0.099)

- **PATRÓN** `volumen_regimen` > `1.1167` → IC=+0.192 (n=183)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` > 1.1167 (IC base=+0.099)

- **PATRÓN** `volumen_pendiente_norm` > `0.1605` → IC=+0.180 (n=145)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.1605 (IC base=+0.099)

- **PATRÓN** `volumen_spike_ratio` < `2.1906` → IC=+0.130 (n=457)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 2.1906 (IC base=+0.099)

- **PATRÓN** `volumen_spike_ratio` > `1.4564` → IC=+0.139 (n=519)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.4564 (IC base=+0.099)

### GBM_LATE_60M#XRP#60min
- **PATRÓN** `sigma_h` > `0.0144` → IC=+0.352 (n=25)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0144 (IC base=+0.304)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.324 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.304)

- **PATRÓN** `ibs_20min` > `0.7025` → IC=+0.357 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7025 (IC base=+0.304)

- **PATRÓN** `dist_vwap_pct` > `0.4912` → IC=+0.380 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4912 (IC base=+0.304)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.797` → IC=+0.318 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.797 (IC base=+0.304)

- **PATRÓN** `volumen_regimen` < `0.9596` → IC=+0.329 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9596 (IC base=+0.304)

- **PATRÓN** `volumen_regimen` > `0.6921` → IC=+0.300 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6921 (IC base=+0.304)

- **PATRÓN** `volumen_pendiente_norm` < `0.0725` → IC=+0.329 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0725 (IC base=+0.304)

- **PATRÓN** `volumen_spike_ratio` < `1.8927` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8927 (IC base=+0.304)

- **PATRÓN** `volumen_spike_ratio` > `2.2573` → IC=+0.346 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2573 (IC base=+0.304)

- **PATRÓN** `libro_spread` < `0.07` → IC=+0.306 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.07 (IC base=+0.304)

- **PATRÓN** `libro_liquidez` > `34.6896` → IC=+0.300 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 34.6896 (IC base=+0.304)

- **PATRÓN** `sigma_h` < `0.0124` → IC=+0.344 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0124 (IC base=+0.320)

- **PATRÓN** `sigma_h` > `0.011` → IC=+0.333 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.320)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.420 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.320)

- **PATRÓN** `ibs_20min` < `0.1481` → IC=+0.409 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1481 (IC base=+0.320)

- **PATRÓN** `ibs_20min` > `0.3972` → IC=+0.326 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3972 (IC base=+0.320)

- **PATRÓN** `volumen_regimen` > `0.6483` → IC=+0.333 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6483 (IC base=+0.320)

- **PATRÓN** `volumen_pendiente_norm` > `0.0801` → IC=+0.409 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0801 (IC base=+0.320)

- **PATRÓN** `volumen_spike_ratio` < `1.501` → IC=+0.357 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.501 (IC base=+0.320)

- **PATRÓN** `libro_liquidez` > `39.7` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 39.7 (IC base=+0.320)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` < `0.0061` → IC=-0.248 (n=204)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0061
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=204)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.310 (n=98)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=310)

- **FILTRO** `volumen_regimen` < `0.871` → IC=-0.309 (n=134)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.871
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=274)

- **FILTRO** `sigma_h` < `0.0073` → IC=-0.286 (n=274)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0073
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

- **FILTRO** `dist_vwap_pct` > `0.4614` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4614
  - _Potencial_: sin este filtro IC_bueno=-0.262 (n=338)

- **FILTRO** `sigma_ewma_delta_pct` > `9.308` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.308
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=336)

- **FILTRO** `volumen_pendiente_norm` > `0.046` → IC=-0.375 (n=30)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.046
  - _Potencial_: sin este filtro IC_bueno=-0.245 (n=241)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.312 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.240 (n=94)

- **FILTRO** `ibs_20min` < `0.1017` → IC=-0.286 (n=40)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1017
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=84)

- **FILTRO** `sigma_h` < `0.0033` → IC=-0.253 (n=75)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.240 (n=75)

- **FILTRO** `drift_60min` |x|> `0.1301` → IC=-0.308 (n=50)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1301
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=98)

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

- **FILTRO** `volumen_spike_ratio` > `2.5392` → IC=-0.315 (n=25)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.5392
  - _Potencial_: sin este filtro IC_bueno=-0.310 (n=77)

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
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=110)

- **FILTRO** `volumen_spike_ratio` < `1.57` → IC=-0.312 (n=30)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.57
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=91)

- **FILTRO** `sigma_h` < `0.0123` → IC=-0.304 (n=49)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0123
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=17)

- **FILTRO** `sigma_ewma_delta_pct` > `4.378` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.378
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=50)

- **FILTRO** `volumen_regimen` < `0.9175` → IC=-0.457 (n=21)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9175
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=45)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.260 (n=373)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.209 (n=325)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `0.6842` → IC=+0.204 (n=823)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6842 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.8606` → IC=+0.326 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8606 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.408` → IC=+0.191 (n=192)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 10.408 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.407` → IC=+0.167 (n=839)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` < 8.407 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `0.6243` → IC=+0.196 (n=274)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.6243 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` > `1.1989` → IC=+0.167 (n=274)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 1.1989 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` < `0.0678` → IC=+0.194 (n=618)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0678 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.498` → IC=+0.207 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.498 (IC base=+0.167)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.159 (n=80)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0065 (IC base=+0.062)

- **PATRÓN** `ibs_20min` > `0.7315` → IC=+0.137 (n=235)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 0.7315 (IC base=+0.062)

- **PATRÓN** `dist_vwap_pct` > `0.6628` → IC=+0.229 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6628 (IC base=+0.062)

- **PATRÓN** `ibs_20min` < `0.2471` → IC=+0.133 (n=434)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.2471 (IC base=+0.074)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.137 (n=177)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0045 (IC base=+0.137)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.181 (n=89)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0071 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.1124` → IC=+0.139 (n=117)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.1124 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.177 (n=97)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 18.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.143 (n=96)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 6.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.7994` → IC=+0.186 (n=237)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.7994 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.8076` → IC=+0.189 (n=43)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.8076 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.1088` → IC=+0.156 (n=216)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1088 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.169` → IC=+0.156 (n=274)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 9.169 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.6229` → IC=+0.192 (n=89)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.6229 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `1.1834` → IC=+0.170 (n=89)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 1.1834 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` < `0.0503` → IC=+0.189 (n=220)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.0503 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.7116` → IC=+0.188 (n=158)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.7116 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=223)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.315` → IC=+0.135 (n=102)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 9.315 (IC base=+0.002)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.15` → IC=-0.240 (n=75)

  - _Acción_: SKIP cuando `ibs_20min` > 0.15
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=151)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.285 (n=328)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.267)

- **PATRÓN** `ibs_20min` > `0.6842` → IC=+0.297 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6842 (IC base=+0.267)

- **PATRÓN** `dist_vwap_pct` > `0.7508` → IC=+0.399 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7508 (IC base=+0.267)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.922` → IC=+0.353 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.922 (IC base=+0.267)

- **PATRÓN** `volumen_regimen` < `0.7968` → IC=+0.296 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7968 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.315 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` < `1.4907` → IC=+0.331 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4907 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` > `2.0543` → IC=+0.302 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.0543 (IC base=+0.267)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.273 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.267)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.329 (n=185)

- **PATRÓN** `drift_ventana_pct` |x|> `0.5455` → IC=+0.343 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.5455 (IC base=+0.333)

- **PATRÓN** `elapsed_s` > `208.3` → IC=+0.380 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 208.3 (IC base=+0.333)

- **PATRÓN** `drift_15min` |x|≤ `1.1328` → IC=+0.382 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.1328 (IC base=+0.333)

- **PATRÓN** `drift_60min` |x|≤ `0.6616` → IC=+0.380 (n=98)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6616 (IC base=+0.333)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.386 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.333)

- **PATRÓN** `ballena_activa_n` < `1046.0` → IC=+0.422 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1046.0 (IC base=+0.333)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3507` → IC=+0.297 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3507 (IC base=+0.289)

- **PATRÓN** `elapsed_s` > `230.8` → IC=+0.387 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 230.8 (IC base=+0.289)

- **PATRÓN** `drift_15min` |x|≤ `2.3607` → IC=+0.324 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3607 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.9468` → IC=+0.309 (n=134)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9468 (IC base=+0.289)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.329 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.289)

- **PATRÓN** `ballena_activa_n` < `1325.0` → IC=+0.375 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1325.0 (IC base=+0.289)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.329 (n=185)

- **PATRÓN** `drift_ventana_pct` |x|> `0.5455` → IC=+0.343 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.5455 (IC base=+0.333)

- **PATRÓN** `elapsed_s` > `208.3` → IC=+0.380 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 208.3 (IC base=+0.333)

- **PATRÓN** `drift_15min` |x|≤ `1.1328` → IC=+0.382 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.1328 (IC base=+0.333)

- **PATRÓN** `drift_60min` |x|≤ `0.6616` → IC=+0.380 (n=98)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6616 (IC base=+0.333)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.386 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.333)

- **PATRÓN** `ballena_activa_n` < `1046.0` → IC=+0.422 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1046.0 (IC base=+0.333)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3507` → IC=+0.297 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3507 (IC base=+0.289)

- **PATRÓN** `elapsed_s` > `230.8` → IC=+0.387 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 230.8 (IC base=+0.289)

- **PATRÓN** `drift_15min` |x|≤ `2.3607` → IC=+0.324 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3607 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.9468` → IC=+0.309 (n=134)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9468 (IC base=+0.289)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.329 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.289)

- **PATRÓN** `ballena_activa_n` < `1325.0` → IC=+0.375 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1325.0 (IC base=+0.289)

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
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=1394)

### LIQUIDACIONES_15M#BNB#15min
- **PATRÓN** `liq_n` > `2.0` → IC=+0.171 (n=77)

  - _Acción_: Kelly boost +0.85€ cuando `liq_n` > 2.0 (IC base=+0.084)

- **PATRÓN** `liq_usd_total` > `1042.48` → IC=+0.171 (n=71)

  - _Acción_: Kelly boost +0.86€ cuando `liq_usd_total` > 1042.48 (IC base=+0.084)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.136 (n=75)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` > 0.5 (IC base=+0.084)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.141 (n=101)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.03 (IC base=+0.084)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `11686.6395` → IC=-0.167 (n=40)

  - _Acción_: SKIP cuando `libro_liquidez` < 11686.6395
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=120)

### LIQUIDACIONES_15M#DOGE#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.180 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.179 (n=82)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.141 (n=90)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.179 (n=82)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 10.0 (IC base=+0.098)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.141 (n=90)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` > 0.5 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `1870.8824` → IC=+0.184 (n=36)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 1870.8824 (IC base=+0.098)

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
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=277)

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
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=4194)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=235)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=192)

- **FILTRO** `ballena_activa_n` > `69.0` → IC=-0.175 (n=75)

  - _Acción_: SKIP cuando `ballena_activa_n` > 69.0
  - _Potencial_: sin este filtro IC_bueno=+0.151 (n=147)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.151 (n=147)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 69.0 (IC base=+0.004)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=22)

- **FILTRO** `libro_liquidez` < `13988.6712` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 13988.6712
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.135 (n=288)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.495 (IC base=+0.022)

### LIQUIDACIONES_5M#DOGE#5min
- **PATRÓN** `liq_n` > `3.0` → IC=+0.333 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 3.0 (IC base=+0.183)

- **PATRÓN** `liq_usd_total` > `1165.64` → IC=+0.289 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 1165.64 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.227 (n=75)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.194 (n=109)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.03 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `3279.111` → IC=+0.200 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3279.111 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.192 (n=102)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 14.0 (IC base=+0.183)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=1639)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=1593)

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
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=748)

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
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=1125)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=1125)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=1502)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=1502)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=348)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=348)

- **FILTRO** `py_entrada` < `0.43` → IC=-0.138 (n=114)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=249)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.136 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=405)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=454)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=331)

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
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=422)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.125 (n=3447)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=8978)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.152 (n=44)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=91)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.136 (n=116)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=142)

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
- **FILTRO** `py_entrada` < `0.4` → IC=-0.154 (n=411)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=1004)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.151 (n=330)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=890)

- **PATRÓN** `py_entrada` < `0.51` → IC=+0.149 (n=426)

  - _Acción_: Kelly boost +0.75€ cuando `py_entrada` < 0.51 (IC base=-0.006)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.135 (n=195)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=441)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.122 (n=326)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=656)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.120 (n=712)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=750)

- **PATRÓN** `py_entrada` < `0.51` → IC=+0.129 (n=332)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.51 (IC base=-0.020)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.138 (n=354)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=749)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.122 (n=767)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=399)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.128 (n=619)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=709)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.178 (n=9122)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=28394)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.170 (n=9481)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=29334)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.198 (n=1698)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=5298)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.145 (n=2323)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=4563)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.138 (n=1795)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 1.0 (IC base=+0.039)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.136 (n=3244)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.5 (IC base=+0.015)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.185 (n=1184)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=3951)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.176 (n=1336)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=4096)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.197 (n=1724)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.090 (n=5341)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.133 (n=2153)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 1.0 (IC base=+0.032)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `ibs_20min` < `0.7651` → IC=-0.152 (n=1256)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7651
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=3770)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.177 (n=1365)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=4169)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.161 (n=1736)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=5279)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=2452)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2376)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=973)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=3288)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=4240)

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
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=372)

- **FILTRO** `drift_20min_pct` |x|> `0.1999` → IC=-0.134 (n=121)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1999
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=364)

- **FILTRO** `libro_liquidez` < `3248.8853` → IC=-0.185 (n=160)

  - _Acción_: SKIP cuando `libro_liquidez` < 3248.8853
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=325)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=983)

- **FILTRO** `libro_liquidez` < `2015.008` → IC=-0.137 (n=406)

  - _Acción_: SKIP cuando `libro_liquidez` < 2015.008
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=827)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.137 (n=25369)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=57705)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.302 (n=20250)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=62824)

- **FILTRO** `ibs_7min` < `0.7273` → IC=-0.225 (n=27316)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7273
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=55758)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.154 (n=27885)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=55189)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.247 (n=25757)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=78166)

- **FILTRO** `ibs_7min` > `0.2785` → IC=-0.183 (n=25978)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2785
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=77945)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.162 (n=3556)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=11419)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.321 (n=3741)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=11234)

- **FILTRO** `ibs_7min` < `0.7083` → IC=-0.255 (n=4936)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7083
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=10039)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.279 (n=4365)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=13637)

- **FILTRO** `ibs_7min` > `0.7679` → IC=-0.211 (n=4500)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7679
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=13502)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.267 (n=3360)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=10343)

- **FILTRO** `ibs_7min` < `0.7112` → IC=-0.216 (n=3425)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7112
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=10278)

- **FILTRO** `ballena_activa_n` > `157.0` → IC=-0.205 (n=3419)

  - _Acción_: SKIP cuando `ballena_activa_n` > 157.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=10284)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.266 (n=3195)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=10833)

- **FILTRO** `ibs_7min` > `0.2644` → IC=-0.191 (n=3504)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2644
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=10524)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.178 (n=3497)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=10531)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.169 (n=3421)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=10937)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.330 (n=3428)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=10930)

- **FILTRO** `ibs_7min` < `0.29` → IC=-0.255 (n=4737)

  - _Acción_: SKIP cuando `ibs_7min` < 0.29
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=9621)

- **FILTRO** `ballena_activa_n` > `4.0` → IC=-0.174 (n=3449)

  - _Acción_: SKIP cuando `ballena_activa_n` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=10909)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.261 (n=4558)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=14475)

- **FILTRO** `ibs_7min` > `0.7222` → IC=-0.186 (n=4750)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7222
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=14283)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.277 (n=3043)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=10346)

- **FILTRO** `ibs_7min` < `0.7115` → IC=-0.203 (n=3346)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7115
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=10043)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.200 (n=3232)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=10157)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.259 (n=3238)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=10655)

- **FILTRO** `ibs_7min` > `0.2719` → IC=-0.179 (n=3473)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2719
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=10420)

- **FILTRO** `ballena_activa_n` > `23.0` → IC=-0.168 (n=3458)

  - _Acción_: SKIP cuando `ballena_activa_n` > 23.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=10435)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.303 (n=3222)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=9999)

- **FILTRO** `ibs_7min` < `0.2941` → IC=-0.235 (n=4347)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2941
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=8874)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.218 (n=3269)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=9952)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.202 (n=4770)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=15348)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.315 (n=3292)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=10136)

- **FILTRO** `ibs_7min` < `0.72` → IC=-0.231 (n=4412)

  - _Acción_: SKIP cuando `ibs_7min` < 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=9016)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.196 (n=3335)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=10093)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.231 (n=4605)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=14244)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=121)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.163 (n=304)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=1033)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=1322)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.167 (n=181)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=668)

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
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=925)

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
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=554)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4305` → IC=+0.144 (n=757)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio` |x|> 0.4305 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.130 (n=609)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 4.0 (IC base=+0.124)

- **PATRÓN** `total_vol_5m` < `451.7672` → IC=+0.166 (n=555)

  - _Acción_: Kelly boost +0.83€ cuando `total_vol_5m` < 451.7672 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `3665.592` → IC=+0.131 (n=754)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 3665.592 (IC base=+0.124)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.187 (n=193)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 14.0 (IC base=+0.141)

- **PATRÓN** `total_vol_5m` < `381.982` → IC=+0.165 (n=338)

  - _Acción_: Kelly boost +0.82€ cuando `total_vol_5m` < 381.982 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.157 (n=266)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 9.0 (IC base=+0.141)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3987` → IC=+0.130 (n=347)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.65€ cuando `delta_ratio` |x|> 0.3987 (IC base=+0.114)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.153 (n=145)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 4.0 (IC base=+0.114)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4162` → IC=+0.172 (n=205)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.86€ cuando `delta_ratio` |x|> 0.4162 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.153 (n=283)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `total_vol_5m` < `705.9846` → IC=+0.167 (n=271)

  - _Acción_: Kelly boost +0.83€ cuando `total_vol_5m` < 705.9846 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.184 (n=112)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 59.0 (IC base=+0.126)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4317` → IC=+0.215 (n=128)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4317 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.164 (n=135)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 6.0 (IC base=+0.134)

- **PATRÓN** `total_vol_5m` < `4761.643` → IC=+0.179 (n=188)

  - _Acción_: Kelly boost +0.89€ cuando `total_vol_5m` < 4761.643 (IC base=+0.134)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `13.0` → IC=+0.131 (n=304)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 13.0 (IC base=+0.101)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.137 (n=213)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.101)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `6.3582` → IC=-0.218 (n=83)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 6.3582
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=163)

- **FILTRO** `sigma_h` > `0.0074` → IC=-0.145 (n=336)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0074
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=654)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.157 (n=327)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0047 (IC base=-0.026)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0059` → IC=-0.147 (n=151)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0059
  - _Potencial_: sin este filtro IC_bueno=+0.156 (n=152)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.265 (n=100)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.005)

- **PATRÓN** `pct_vs_K` |x|≤ `1.9196` → IC=+0.206 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 1.9196 (IC base=+0.005)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `pct_vs_K` |x|> `6.4329` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 6.4329
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=59)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `T_h` < `73.7179` → IC=-0.172 (n=62)

  - _Acción_: SKIP cuando `T_h` < 73.7179
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=128)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `T_h` < `87.9956` → IC=-0.251 (n=428)

  - _Acción_: SKIP cuando `T_h` < 87.9956
  - _Potencial_: sin este filtro IC_bueno=-0.235 (n=429)

- **FILTRO** `sigma_h` < `0.0057` → IC=-0.187 (n=199)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0057
  - _Potencial_: sin este filtro IC_bueno=-0.096 (n=597)

- **FILTRO** `pct_vs_K` |x|> `2.9641` → IC=-0.375 (n=198)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9641
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=598)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` > `0.007` → IC=-0.241 (n=141)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=143)

- **FILTRO** `T_h` < `61.9882` → IC=-0.226 (n=93)

  - _Acción_: SKIP cuando `T_h` < 61.9882
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=191)

- **FILTRO** `pct_vs_K` |x|> `2.368` → IC=-0.324 (n=100)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.368
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=197)

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
- **FILTRO** `sigma_h` < `0.0095` → IC=-0.327 (n=125)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.272 (n=125)

- **FILTRO** `T_h` < `69.3311` → IC=-0.309 (n=82)

  - _Acción_: SKIP cuando `T_h` < 69.3311
  - _Potencial_: sin este filtro IC_bueno=-0.294 (n=168)

- **FILTRO** `sigma_h` > `0.0091` → IC=-0.143 (n=82)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=160)

- **FILTRO** `sigma_h` < `0.0058` → IC=-0.161 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0058
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=182)

- **PATRÓN** `pct_vs_K` |x|≤ `1.9843` → IC=+0.161 (n=122)

  - _Acción_: Kelly boost +0.81€ cuando `pct_vs_K` |x|≤ 1.9843 (IC base=-0.098)

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

- **FILTRO** `sigma_h` > `0.0139` → IC=-0.306 (n=60)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0139
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=118)

- **FILTRO** `sigma_h` < `0.0091` → IC=-0.261 (n=44)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=134)

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

- **PATRÓN** `sigma_h` > `0.0136` → IC=+0.410 (n=98)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0136 (IC base=+0.392)

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
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=477)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=516)

- **PATRÓN** `streak_estiramiento` < `0.3762` → IC=+0.127 (n=159)

  - _Acción_: Kelly boost +0.64€ cuando `streak_estiramiento` < 0.3762 (IC base=+0.018)

- **PATRÓN** `streak_estiramiento` < `0.835` → IC=+0.127 (n=357)

  - _Acción_: Kelly boost +0.63€ cuando `streak_estiramiento` < 0.835 (IC base=+0.060)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.124 (n=269)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 29.0 (IC base=+0.060)

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
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=218)

- **PATRÓN** `streak_estiramiento` < `0.2115` → IC=+0.161 (n=60)

  - _Acción_: Kelly boost +0.81€ cuando `streak_estiramiento` < 0.2115 (IC base=+0.034)

- **PATRÓN** `streak_estiramiento` < `0.5965` → IC=+0.163 (n=179)

  - _Acción_: Kelly boost +0.81€ cuando `streak_estiramiento` < 0.5965 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.142 (n=191)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 35.0 (IC base=+0.087)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.194 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=97)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=118)

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
- **PATRÓN** `streak_estiramiento` < `0.6467` → IC=+0.177 (n=29)

  - _Acción_: Kelly boost +0.89€ cuando `streak_estiramiento` < 0.6467 (IC base=-0.005)

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
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1350)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1244)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=1325)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=5460)

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
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=3273)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.184 (n=2128)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0058 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.232` → IC=+0.158 (n=6379)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.232 (IC base=+0.133)

- **PATRÓN** `drift_15min` |x|≤ `1.1182` → IC=+0.135 (n=6379)

  - _Acción_: Kelly boost +0.67€ cuando `drift_15min` |x|≤ 1.1182 (IC base=+0.133)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0645` → IC=+0.133 (n=6380)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio_macro` |x|> 0.0645 (IC base=+0.133)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1333` → IC=+0.142 (n=2647)

  - _Acción_: Kelly boost +0.71€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1333 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.144 (n=5907)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 6.0 (IC base=+0.133)

- **PATRÓN** `ibs_15` > `0.5581` → IC=+0.209 (n=5699)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5581 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.124` → IC=+0.232 (n=1190)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.124 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=3385)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `4334.8489` → IC=+0.170 (n=2126)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 4334.8489 (IC base=+0.133)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=2459)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.253 (n=290)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.0769` → IC=+0.247 (n=382)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0769 (IC base=+0.205)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2678` → IC=+0.225 (n=289)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2678 (IC base=+0.205)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2266` → IC=+0.217 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2266 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.230 (n=803)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.205)

- **PATRÓN** `ibs_15` > `0.7058` → IC=+0.275 (n=868)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7058 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `0.3902` → IC=+0.224 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3902 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` < `0.5461` → IC=+0.209 (n=978)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5461 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.088` → IC=+0.300 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.088 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=1126)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `11836.5406` → IC=+0.225 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11836.5406 (IC base=+0.205)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.161 (n=491)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0047 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.1091` → IC=+0.146 (n=742)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.1091 (IC base=+0.132)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0842` → IC=+0.136 (n=993)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio_macro` |x|> 0.0842 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.145 (n=789)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 11.0 (IC base=+0.132)

- **PATRÓN** `ibs_15` > `0.4837` → IC=+0.217 (n=1112)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.4837 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` > `0.1236` → IC=+0.144 (n=700)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.1236 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` < `0.6583` → IC=+0.135 (n=1262)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.6583 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.997` → IC=+0.286 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.997 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `6089.1003` → IC=+0.172 (n=504)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 6089.1003 (IC base=+0.132)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.84` → IC=+0.149 (n=651)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.75€ cuando `ibs_15` > 0.84 (IC base=+0.046)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` < `0.0139` → IC=+0.144 (n=711)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0139 (IC base=+0.139)

- **PATRÓN** `sigma_h` > `0.012` → IC=+0.144 (n=1616)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.012 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.2382` → IC=+0.175 (n=1616)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2382 (IC base=+0.139)

- **PATRÓN** `delta_ratio_macro` |x|> `0.058` → IC=+0.142 (n=1617)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.71€ cuando `delta_ratio_macro` |x|> 0.058 (IC base=+0.139)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0929` → IC=+0.190 (n=504)

  - _Acción_: Kelly boost +0.95€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0929 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.146 (n=1479)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 6.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.141 (n=1489)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 15.0 (IC base=+0.139)

- **PATRÓN** `ibs_15` > `0.7` → IC=+0.235 (n=1083)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.2121` → IC=+0.151 (n=740)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.2121 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.9149` → IC=+0.143 (n=1868)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.9149 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.291` → IC=+0.186 (n=371)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 17.291 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `2945.8249` → IC=+0.182 (n=733)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2945.8249 (IC base=+0.139)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `drift_60min` |x|≤ `0.1103` → IC=+0.363 (n=532)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1103 (IC base=+0.363)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1482` → IC=+0.376 (n=531)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1482 (IC base=+0.363)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1073` → IC=+0.378 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1073 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.371 (n=841)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.363)

- **PATRÓN** `ibs_15` > `0.7904` → IC=+0.395 (n=797)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7904 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` > `0.2675` → IC=+0.378 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2675 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.778` → IC=+0.395 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.778 (IC base=+0.363)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.366 (n=973)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.363)

- **PATRÓN** `libro_liquidez` > `9610.6074` → IC=+0.379 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9610.6074 (IC base=+0.363)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.365 (n=168)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.362)

- **PATRÓN** `drift_60min` |x|≤ `0.1514` → IC=+0.363 (n=335)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1514 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2194` → IC=+0.374 (n=173)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2194 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1464` → IC=+0.395 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1464 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.379 (n=353)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.362)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.361 (n=388)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.8112` → IC=+0.383 (n=381)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8112 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.2499` → IC=+0.386 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2499 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.785` → IC=+0.380 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.785 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `15168.2778` → IC=+0.386 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15168.2778 (IC base=+0.362)

- **PATRÓN** `ballena_activa_n` < `412.0` → IC=+0.384 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 412.0 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.364 (n=417)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.362)

- **PATRÓN** `drift_60min` |x|≤ `0.1062` → IC=+0.364 (n=278)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1062 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1274` → IC=+0.379 (n=278)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1274 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.369 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.380 (n=190)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.362)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.372 (n=193)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.7632` → IC=+0.397 (n=417)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7632 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.4608` → IC=+0.375 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4608 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` < `0.6708` → IC=+0.364 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6708 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.857` → IC=+0.397 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.857 (IC base=+0.362)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.364 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `4304.5454` → IC=+0.374 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4304.5454 (IC base=+0.362)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `libro_spread` > `0.01` → IC=-0.223 (n=2640)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=3351)

- **FILTRO** `libro_liquidez` < `4366.1664` → IC=-0.173 (n=3954)

  - _Acción_: SKIP cuando `libro_liquidez` < 4366.1664
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=2037)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1411` → IC=+0.213 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1411 (IC base=-0.089)

- **PATRÓN** `ibs_15` > `0.6306` → IC=+0.278 (n=1317)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6306 (IC base=-0.089)

- **PATRÓN** `dist_vwap_pct` > `0.1154` → IC=+0.205 (n=778)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1154 (IC base=-0.089)

- **PATRÓN** `dist_vwap_pct` < `0.5931` → IC=+0.199 (n=1399)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.5931 (IC base=-0.089)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2286` → IC=+0.270 (n=1945)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2286 (IC base=+0.001)

- **PATRÓN** `ibs_15` < `0.375` → IC=+0.284 (n=5850)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.375 (IC base=+0.001)

- **PATRÓN** `dist_vwap_pct` > `0.7038` → IC=+0.266 (n=837)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7038 (IC base=+0.001)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0736` → IC=-0.241 (n=1954)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0736
  - _Potencial_: sin este filtro IC_bueno=-0.122 (n=1956)

- **FILTRO** `sigma_h` < `0.004` → IC=-0.212 (n=977)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.004
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=2933)

- **FILTRO** `sigma_ewma_delta_pct` > `22.231` → IC=-0.243 (n=554)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.231
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=3356)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.146 (n=360)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0032 (IC base=+0.064)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2678` → IC=+0.274 (n=157)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2678 (IC base=+0.064)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.145` → IC=+0.279 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.145 (IC base=+0.064)

- **PATRÓN** `ibs_15` > `0.7609` → IC=+0.318 (n=470)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7609 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` > `0.1047` → IC=+0.282 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1047 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` < `0.5257` → IC=+0.284 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5257 (IC base=+0.064)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.8` → IC=+0.140 (n=237)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 21.8 (IC base=+0.064)

- **PATRÓN** `delta_ratio_macro` |x|> `0.107` → IC=+0.240 (n=71)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.107 (IC base=-0.181)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0902` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0902 (IC base=-0.181)

- **PATRÓN** `ibs_15` < `0.6255` → IC=+0.290 (n=79)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6255 (IC base=-0.181)

- **PATRÓN** `dist_vwap_pct` < `0.0469` → IC=+0.300 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0469 (IC base=-0.181)

- **PATRÓN** `ballena_activa_n` < `393.0` → IC=+0.315 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 393.0 (IC base=-0.181)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.152 (n=867)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.159 (n=664)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0066 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.0718` → IC=+0.175 (n=293)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0718 (IC base=+0.147)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3015` → IC=+0.190 (n=523)

  - _Acción_: Kelly boost +0.95€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3015 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.170 (n=477)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 11.0 (IC base=+0.147)

- **PATRÓN** `ibs_15` > `0.5659` → IC=+0.243 (n=663)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5659 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.6666` → IC=+0.167 (n=127)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.6666 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.835` → IC=+0.260 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.835 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=867)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `5129.2383` → IC=+0.162 (n=442)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 5129.2383 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.259 (n=999)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.4767` → IC=+0.242 (n=2270)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4767 (IC base=+0.238)

- **PATRÓN** `drift_15min` |x|≤ `0.8203` → IC=+0.251 (n=1998)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.8203 (IC base=+0.238)

- **PATRÓN** `delta_ratio_macro` |x|> `0.202` → IC=+0.258 (n=1029)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.202 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.246 (n=841)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.240 (n=1545)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.238)

- **PATRÓN** `ibs_15` < `0.3887` → IC=+0.270 (n=2270)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3887 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` > `0.1647` → IC=+0.252 (n=870)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1647 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.522` → IC=+0.245 (n=982)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.522 (IC base=+0.238)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.2012` → IC=-0.295 (n=359)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.2012
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=1079)

- **FILTRO** `drift_60min` |x|> `0.173` → IC=-0.283 (n=486)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.173
  - _Potencial_: sin este filtro IC_bueno=-0.168 (n=952)

- **FILTRO** `drift_15min` |x|> `1.0081` → IC=-0.309 (n=359)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.0081
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=1079)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.188 (n=46)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.207)

- **PATRÓN** `ibs_15` > `0.9231` → IC=+0.380 (n=23)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9231 (IC base=-0.207)

- **PATRÓN** `dist_vwap_pct` < `0.4298` → IC=+0.158 (n=77)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.4298 (IC base=-0.207)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 37.0 (IC base=-0.207)

- **PATRÓN** `ibs_15` < `0.3793` → IC=+0.297 (n=975)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3793 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` < `0.1989` → IC=+0.256 (n=892)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1989 (IC base=-0.026)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1213` → IC=-0.270 (n=844)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1213
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=846)

- **FILTRO** `sigma_h` > `0.0145` → IC=-0.252 (n=1132)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0145
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=558)

- **FILTRO** `drift_15min` |x|> `1.3088` → IC=-0.283 (n=422)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.3088
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=1268)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=1669)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.222)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.222)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0705` → IC=+0.283 (n=1219)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0705 (IC base=-0.009)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1182` → IC=+0.291 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1182 (IC base=-0.009)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.294 (n=1376)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.009)

- **PATRÓN** `dist_vwap_pct` > `0.7901` → IC=+0.325 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7901 (IC base=-0.009)

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

- **PATRÓN** `dist_vwap_pct` > `0.2049` → IC=+0.134 (n=91)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.2049 (IC base=+0.053)

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

- **PATRÓN** `dist_vwap_pct` > `0.2049` → IC=+0.134 (n=91)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.2049 (IC base=+0.053)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.301 (n=490)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.295 (n=490)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0066 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.0531` → IC=+0.311 (n=491)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0531 (IC base=+0.284)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0682` → IC=+0.284 (n=1468)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0682 (IC base=+0.284)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.221` → IC=+0.290 (n=901)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.221 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.295 (n=1526)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.284)

- **PATRÓN** `ibs_15` > `0.837` → IC=+0.310 (n=1469)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.837 (IC base=+0.284)

- **PATRÓN** `dist_vwap_pct` > `0.2747` → IC=+0.314 (n=636)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2747 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.686` → IC=+0.384 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.686 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.283 (n=1744)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `13082.2536` → IC=+0.301 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13082.2536 (IC base=+0.284)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.308 (n=258)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.278)

- **PATRÓN** `drift_60min` |x|≤ `0.0763` → IC=+0.301 (n=340)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0763 (IC base=+0.278)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2298` → IC=+0.287 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2298 (IC base=+0.278)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.301 (n=712)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.278)

- **PATRÓN** `ibs_15` > `0.827` → IC=+0.301 (n=773)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.827 (IC base=+0.278)

- **PATRÓN** `dist_vwap_pct` > `0.2573` → IC=+0.309 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2573 (IC base=+0.278)

- **PATRÓN** `dist_vwap_pct` < `0.5693` → IC=+0.278 (n=873)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5693 (IC base=+0.278)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.41` → IC=+0.391 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.41 (IC base=+0.278)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.280 (n=1001)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `15643.6309` → IC=+0.315 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15643.6309 (IC base=+0.278)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.299 (n=307)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.0504` → IC=+0.322 (n=234)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0504 (IC base=+0.289)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0644` → IC=+0.292 (n=696)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0644 (IC base=+0.289)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1013` → IC=+0.304 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1013 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.299 (n=670)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.8452` → IC=+0.315 (n=696)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8452 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.2918` → IC=+0.312 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2918 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.914` → IC=+0.379 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.914 (IC base=+0.289)

### UPDOWN_OU_5M
- **FILTRO** `delta_ratio_macro` |x|≤ `0.126` → IC=-0.163 (n=96)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.126
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=295)

- **FILTRO** `ballena_activa_n` > `44.0` → IC=-0.145 (n=240)

  - _Acción_: SKIP cuando `ballena_activa_n` > 44.0
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

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1045` → IC=-0.222 (n=16)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1045
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=50)

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
- **PATRÓN** `ratio` < `0.9868` → IC=+0.254 (n=572)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9868 (IC base=+0.124)

- **PATRÓN** `T_h` > `115.9373` → IC=+0.356 (n=3204)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 115.9373 (IC base=+0.337)

- **PATRÓN** `ratio` > `1.0177` → IC=+0.391 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0177 (IC base=+0.337)

### WEEKLY_PRICE#BTC
- **PATRÓN** `ratio` < `0.992` → IC=+0.155 (n=279)

  - _Acción_: Kelly boost +0.77€ cuando `ratio` < 0.992 (IC base=+0.068)

- **PATRÓN** `T_h` > `110.5638` → IC=+0.329 (n=1175)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 110.5638 (IC base=+0.310)

- **PATRÓN** `ratio` > `1.0147` → IC=+0.379 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0147 (IC base=+0.310)

### WEEKLY_PRICE#ETH
- **PATRÓN** `ratio` < `0.9793` → IC=+0.363 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9793 (IC base=+0.185)

- **PATRÓN** `T_h` > `111.996` → IC=+0.353 (n=1174)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.996 (IC base=+0.321)

- **PATRÓN** `ratio` > `1.0238` → IC=+0.404 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0238 (IC base=+0.321)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0386` → IC=+0.415 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0386 (IC base=+0.396)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5581 sube el IC de +0.133 a +0.209 en UPDOWN_GBM#15min (n=5699). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7058 sube el IC de +0.205 a +0.275 en UPDOWN_GBM#BTC#15min (n=868). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.4837 sube el IC de +0.132 a +0.217 en UPDOWN_GBM#ETH#15min (n=1112). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.7 sube el IC de +0.139 a +0.235 en UPDOWN_GBM#XRP#15min (n=1083). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6306 sube el IC de -0.089 a +0.278 en UPDOWN_GBM_15M_TARDIO (n=1317). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.375 sube el IC de +0.001 a +0.284 en UPDOWN_GBM_15M_TARDIO (n=5850). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7609 sube el IC de +0.064 a +0.318 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=470). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6255 sube el IC de -0.181 a +0.290 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=79). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5659 sube el IC de +0.147 a +0.243 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=663). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3887 sube el IC de +0.238 a +0.270 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=2270). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.9231 sube el IC de -0.207 a +0.380 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3793 sube el IC de -0.026 a +0.297 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=975). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.222 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.009 a +0.294 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=1376). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8358 sube el IC de +0.085 a +0.300 en UPDOWN_GBM_ETH_15M_HORA7 (n=28). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8358 sube el IC de +0.085 a +0.300 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=28). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.837 sube el IC de +0.284 a +0.310 en UPDOWN_GBM_IBS_ALTO (n=1469). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.827 sube el IC de +0.278 a +0.301 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=773). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8452 sube el IC de +0.289 a +0.315 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=696). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7904 sube el IC de +0.363 a +0.395 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=797). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8112 sube el IC de +0.362 a +0.383 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=381). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7632 sube el IC de +0.362 a +0.397 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=417). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2298 | +0.084 | +242.60€ | 1 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2298 | +0.084 | +242.60€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1886 | +0.084 | +203.12€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1886 | +0.084 | +203.12€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 285 | +0.068 | +10.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 285 | +0.068 | +10.79€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 96 | +0.122 | +29.03€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 96 | +0.122 | +29.03€ | 0 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 1403 | -0.026 | +74.55€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 1403 | -0.026 | +74.55€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 1084 | -0.040 | +58.46€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 1084 | -0.040 | +58.46€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 220 | +0.045 | +24.32€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 220 | +0.045 | +24.32€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 92 | -0.043 | -11.49€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 92 | -0.043 | -11.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 51002 | -0.087 | -6547.63€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 3309 | +0.092 | -319.87€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 47693 | -0.100 | -6227.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 5088 | -0.116 | -816.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 5088 | -0.116 | -816.49€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 3309 | +0.092 | -319.87€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 3309 | +0.092 | -319.87€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 5091 | -0.108 | -951.84€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 5091 | -0.108 | -951.84€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 14109 | -0.046 | -1352.10€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 14109 | -0.046 | -1352.10€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 14025 | -0.121 | -1582.37€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 14025 | -0.121 | -1582.37€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 9380 | -0.138 | -1524.95€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 9380 | -0.138 | -1524.95€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 55607 | -0.012 | +2744.51€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 14327 | +0.003 | +1474.17€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 41280 | -0.017 | +1270.34€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 55607 | -0.012 | +2744.51€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 14327 | +0.003 | +1474.17€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 41280 | -0.017 | +1270.34€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 207998 | +0.113 | -8359.39€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 23073 | +0.179 | -758.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 970 | +0.018 | -75.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 172158 | +0.106 | -7103.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 11797 | +0.095 | -422.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 28533 | +0.102 | -2009.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 84 | -0.186 | +11.85€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 28426 | +0.104 | -2018.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#60min | 8 | +0.040 | +8.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 39019 | +0.123 | -608.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5688 | +0.177 | -232.75€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 28497 | +0.120 | -181.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4792 | +0.082 | -172.38€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 28579 | +0.099 | -1974.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 97 | -0.116 | +14.79€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 28463 | +0.100 | -1980.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 44505 | +0.123 | -930.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 11093 | +0.177 | -318.18€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 28957 | +0.106 | -527.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 4443 | +0.103 | -76.38€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 38804 | +0.112 | -1646.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 6013 | +0.199 | -247.91€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 873 | +0.043 | -22.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 29371 | +0.096 | -1189.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2547 | +0.106 | -186.77€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO#XRP | 28558 | +0.107 | -1189.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 98 | -0.130 | +14.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 28444 | +0.108 | -1205.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 33847 | +0.189 | -2523.43€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 33847 | +0.189 | -2523.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 7671 | +0.162 | -896.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 7671 | +0.162 | -896.24€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 5059 | +0.193 | -219.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 5059 | +0.193 | -219.83€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 7491 | +0.172 | -689.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 7491 | +0.172 | -689.23€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 6204 | +0.252 | -220.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 6204 | +0.252 | -220.77€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 7343 | +0.184 | -511.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 7343 | +0.184 | -511.11€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1313 | +0.424 | -52.98€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1313 | +0.424 | -52.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 555 | +0.437 | -7.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 555 | +0.437 | -7.45€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 528 | +0.421 | -23.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 528 | +0.421 | -23.69€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 216 | +0.399 | -17.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 216 | +0.399 | -17.98€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 119646 | +0.200 | -8680.28€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 119646 | +0.200 | -8680.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 20742 | +0.176 | -2435.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 20742 | +0.176 | -2435.10€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 19286 | +0.223 | -647.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 19286 | +0.223 | -647.27€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 20518 | +0.181 | -2131.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 20518 | +0.181 | -2131.68€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 19453 | +0.217 | -770.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 19453 | +0.217 | -770.79€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 19745 | +0.205 | -1161.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 19745 | +0.205 | -1161.15€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 19902 | +0.198 | -1534.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 19902 | +0.198 | -1534.30€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 46492 | +0.116 | +354.10€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 46492 | +0.116 | +354.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 23153 | +0.117 | +232.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 23153 | +0.117 | +232.72€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 23339 | +0.116 | +121.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 23339 | +0.116 | +121.37€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2717 | +0.294 | -7.95€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2717 | +0.294 | -7.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1243 | +0.283 | -25.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1243 | +0.283 | -25.31€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1332 | +0.297 | +10.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1332 | +0.297 | +10.63€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 142 | +0.347 | +6.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 142 | +0.347 | +6.73€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 1258 | +0.438 | -5.42€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 1258 | +0.438 | -5.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 600 | +0.435 | -7.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 600 | +0.435 | -7.20€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 606 | +0.441 | +0.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 606 | +0.441 | +0.37€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 52 | +0.407 | +1.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 52 | +0.407 | +1.41€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 2034 | +0.064 | -103.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1309 | +0.074 | -39.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1600 | +0.070 | -58.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1309 | +0.074 | -39.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 94887 | +0.101 | -1991.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 7695 | +0.098 | +187.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 87192 | +0.101 | -2179.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 51805 | +0.105 | -436.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 7695 | +0.098 | +187.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 44110 | +0.107 | -624.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 20371 | +0.110 | -51.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 20371 | +0.110 | -51.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 22711 | +0.083 | -1503.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 22711 | +0.083 | -1503.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ GBM_LATE_15M | 64622 | +0.102 | +36350.58€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 64622 | +0.102 | +36350.58€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 10724 | +0.225 | +9211.85€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 10724 | +0.225 | +9211.85€ | 0 | 20 |
| ✅ GBM_LATE_15M#BTC | 10089 | +0.176 | +8117.01€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 10089 | +0.176 | +8117.01€ | 0 | 24 |
| ✅ GBM_LATE_15M#DOGE | 11563 | +0.207 | +9117.96€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 11563 | +0.207 | +9117.96€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 8542 | +0.062 | +2895.58€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 8542 | +0.062 | +2895.58€ | 1 | 17 |
| ✅ GBM_LATE_15M#SOL | 8956 | -0.026 | +2299.80€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 8956 | -0.026 | +2299.80€ | 4 | 17 |
| ✅ GBM_LATE_15M#XRP | 14748 | -0.019 | +4708.37€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 14748 | -0.019 | +4708.37€ | 3 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 68583 | +0.087 | +40053.41€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 68583 | +0.087 | +40053.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 13298 | -0.002 | +6946.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 13298 | -0.002 | +6946.31€ | 3 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 14741 | +0.007 | +4085.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 14741 | +0.007 | +4085.32€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 9221 | +0.296 | +10565.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 9221 | +0.296 | +10565.44€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 13099 | +0.018 | +4193.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 13099 | +0.018 | +4193.09€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 10447 | +0.049 | +4806.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 10447 | +0.049 | +4806.31€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 7777 | +0.313 | +9456.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 7777 | +0.313 | +9456.94€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 50887 | +0.179 | +42291.28€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 50887 | +0.179 | +42291.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 7697 | +0.240 | +7159.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 7697 | +0.240 | +7159.72€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 8099 | +0.141 | +6074.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 8099 | +0.141 | +6074.25€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 8196 | +0.224 | +7106.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 8196 | +0.224 | +7106.40€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 8706 | +0.130 | +6803.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 8706 | +0.130 | +6803.47€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 9601 | +0.123 | +7402.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 9601 | +0.123 | +7402.29€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 8588 | +0.232 | +7745.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 8588 | +0.232 | +7745.15€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 14008 | +0.127 | +7190.91€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 14008 | +0.127 | +7190.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 677 | +0.163 | +447.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 677 | +0.163 | +447.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3605 | +0.126 | +1969.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3605 | +0.126 | +1969.31€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 509 | +0.156 | +286.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 509 | +0.156 | +286.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 4112 | +0.128 | +2097.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 4112 | +0.128 | +2097.50€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 3844 | +0.103 | +1593.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 3844 | +0.103 | +1593.37€ | 0 | 12 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1261 | +0.168 | +796.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1261 | +0.168 | +796.67€ | 0 | 30 |
| ✅ GBM_LATE_15M_TARDIO | 64869 | +0.189 | +54010.95€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#15min | 64869 | +0.189 | +54010.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 10255 | +0.249 | +9884.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 10255 | +0.249 | +9884.04€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 10418 | +0.142 | +7538.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 10418 | +0.142 | +7538.80€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 10999 | +0.234 | +9905.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 10999 | +0.234 | +9905.80€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 10731 | +0.145 | +8084.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 10731 | +0.145 | +8084.46€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 11430 | +0.128 | +8352.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 11430 | +0.128 | +8352.04€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 11036 | +0.241 | +10245.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 11036 | +0.241 | +10245.81€ | 0 | 22 |
| ✅ GBM_LATE_5M | 16531 | +0.219 | +13933.19€ | 0 | 27 |
| ✅ GBM_LATE_5M#5min | 16531 | +0.219 | +13933.19€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1947 | +0.253 | +1897.59€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1947 | +0.253 | +1897.59€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3318 | +0.210 | +2853.71€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3318 | +0.210 | +2853.71€ | 0 | 28 |
| ✅ GBM_LATE_5M#DOGE | 1524 | +0.214 | +1243.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1524 | +0.214 | +1243.40€ | 0 | 18 |
| ✅ GBM_LATE_5M#ETH | 4718 | +0.209 | +3686.13€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 4718 | +0.209 | +3686.13€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 2948 | +0.229 | +2613.07€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2948 | +0.229 | +2613.07€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 2076 | +0.210 | +1639.29€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 2076 | +0.210 | +1639.29€ | 0 | 0 |
| ✅ GBM_LATE_60M | 6195 | +0.071 | +1943.66€ | 0 | 6 |
| ✅ GBM_LATE_60M#60min | 6195 | +0.071 | +1943.66€ | 0 | 0 |
| ✅ GBM_LATE_60M#BNB | 112 | +0.263 | +113.04€ | 0 | 0 |
| ✅ GBM_LATE_60M#BNB#60min | 112 | +0.263 | +113.04€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 2008 | +0.060 | +580.90€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 2008 | +0.060 | +580.90€ | 1 | 6 |
| ✅ GBM_LATE_60M#DOGE | 109 | +0.329 | +132.75€ | 0 | 0 |
| ✅ GBM_LATE_60M#DOGE#60min | 109 | +0.329 | +132.75€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH | 1865 | +0.054 | +591.70€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1865 | +0.054 | +591.70€ | 1 | 6 |
| ✅ GBM_LATE_60M#SOL | 1993 | +0.059 | +401.58€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1993 | +0.059 | +401.58€ | 0 | 10 |
| ✅ GBM_LATE_60M#XRP | 108 | +0.318 | +123.68€ | 0 | 0 |
| ✅ GBM_LATE_60M#XRP#60min | 108 | +0.318 | +123.68€ | 0 | 21 |
| 🚫 GBM_LATE_60M_FADE | 774 | -0.247 | -36.35€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 774 | -0.247 | -36.35€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#BNB | 6 | +0.037 | +3.77€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#BNB#60min | 6 | +0.037 | +3.77€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 274 | -0.257 | -21.15€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 274 | -0.257 | -21.15€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 274 | -0.243 | -7.28€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 274 | -0.243 | -7.28€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 213 | -0.249 | -10.93€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 213 | -0.249 | -10.93€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 2359 | +0.090 | +599.39€ | 0 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 2359 | +0.090 | +599.39€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 891 | +0.070 | +205.62€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 891 | +0.070 | +205.62€ | 0 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 809 | +0.061 | +155.32€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 809 | +0.061 | +155.32€ | 0 | 15 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 653 | +0.152 | +236.75€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 653 | +0.152 | +236.75€ | 1 | 9 |
| ✅ LATE_WINDOW_5MIN | 397 | +0.312 | +482.97€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 397 | +0.312 | +482.97€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 397 | +0.312 | +482.97€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 397 | +0.312 | +482.97€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 4834 | +0.094 | +1046.73€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4834 | +0.094 | +1046.73€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4834 | +0.094 | +1046.73€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4834 | +0.094 | +1046.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M | 1718 | +0.017 | +96.88€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 1718 | +0.017 | +96.88€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 208 | +0.081 | +37.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 208 | +0.081 | +37.35€ | 0 | 4 |
| ✅ LIQUIDACIONES_15M#BTC | 337 | -0.010 | +7.97€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 337 | -0.010 | +7.97€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 115 | +0.056 | +25.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 115 | +0.056 | +25.23€ | 2 | 3 |
| ✅ LIQUIDACIONES_15M#ETH | 388 | +0.026 | +21.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 388 | +0.026 | +21.75€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 351 | -0.016 | +2.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 351 | -0.016 | +2.31€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 319 | +0.017 | +2.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 319 | +0.017 | +2.26€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4535 | +0.017 | +181.80€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#5min | 4535 | +0.017 | +181.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 241 | +0.002 | -6.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 241 | +0.002 | -6.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 860 | +0.015 | +47.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 860 | +0.015 | +47.72€ | 2 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 334 | +0.062 | +80.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 334 | +0.062 | +80.07€ | 0 | 6 |
| ✅ LIQUIDACIONES_5M#ETH | 1691 | +0.020 | +31.17€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1691 | +0.020 | +31.17€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 789 | +0.015 | +5.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 789 | +0.015 | +5.57€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 620 | -0.006 | +23.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 620 | -0.006 | +23.43€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2722 | -0.034 | -6.14€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2722 | -0.034 | -6.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 832 | -0.034 | -13.44€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 832 | -0.034 | -13.44€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 981 | -0.015 | +18.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 981 | -0.015 | +18.43€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 898 | -0.054 | -10.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 898 | -0.054 | -10.73€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#XRP | 8 | +0.000 | +0.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#XRP#60min | 8 | +0.000 | +0.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 20427 | -0.030 | -130.70€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 9881 | -0.033 | -120.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 10546 | -0.028 | -10.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 731 | -0.050 | -35.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 368 | -0.038 | -6.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 363 | -0.062 | -28.46€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 5490 | -0.025 | -10.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 2609 | -0.023 | +9.18€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 2881 | -0.027 | -20.03€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1866 | -0.032 | -1.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 953 | -0.043 | -29.00€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 913 | -0.020 | +27.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 4670 | -0.031 | -48.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 2251 | -0.029 | -16.40€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 2419 | -0.032 | -31.78€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 3898 | -0.023 | +54.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1899 | -0.030 | -5.58€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1999 | -0.016 | +59.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 3772 | -0.041 | -88.70€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1801 | -0.049 | -71.87€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1971 | -0.034 | -16.83€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 76331 | -0.000 | +4149.94€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 76331 | -0.000 | +4149.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 13882 | +0.027 | +1932.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 13882 | +0.027 | +1932.39€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 10567 | -0.038 | -140.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 10567 | -0.038 | -140.56€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 14036 | +0.026 | +1568.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 14036 | +0.026 | +1568.40€ | 1 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 10560 | -0.054 | -274.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 10560 | -0.054 | -274.37€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 13014 | -0.004 | +366.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 13014 | -0.004 | +366.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 14272 | +0.019 | +697.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 14272 | +0.019 | +697.47€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7410 | -0.052 | -106.46€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7410 | -0.052 | -106.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1270 | -0.002 | -14.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1270 | -0.002 | -14.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 2109 | -0.058 | -16.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 2109 | -0.058 | -16.64€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 102 | -0.019 | -0.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 102 | -0.019 | -0.22€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 819 | -0.116 | -32.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 819 | -0.116 | -32.98€ | 6 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2240 | -0.067 | -13.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2240 | -0.067 | -13.39€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 870 | -0.019 | -28.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 870 | -0.019 | -28.97€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3385 | +0.003 | -0.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3385 | +0.003 | -0.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 133 | -0.033 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 133 | -0.033 | -0.70€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 199 | +0.007 | -1.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 199 | +0.007 | -1.73€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 139 | -0.004 | -2.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 139 | -0.004 | -2.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1326 | +0.006 | +6.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1326 | +0.006 | +6.37€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1392 | +0.006 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1392 | +0.006 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 196 | -0.015 | -1.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 196 | -0.015 | -1.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 186997 | -0.077 | +2255.88€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 186997 | -0.077 | +2255.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 32977 | -0.076 | +1947.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 32977 | -0.076 | +1947.44€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 27731 | -0.101 | -1359.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 27731 | -0.101 | -1359.24€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 33391 | -0.068 | +1604.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 33391 | -0.068 | +1604.27€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 27282 | -0.100 | -938.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 27282 | -0.100 | -938.99€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 33339 | -0.059 | +173.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 33339 | -0.059 | +173.19€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 32277 | -0.069 | +829.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 32277 | -0.069 | +829.21€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9322 | -0.036 | -191.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9322 | -0.036 | -191.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1009 | -0.017 | -19.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1009 | -0.017 | -19.83€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2186 | -0.046 | -28.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2186 | -0.046 | -28.58€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2676 | -0.024 | -31.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2676 | -0.024 | -31.92€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1298 | -0.064 | -32.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1298 | -0.064 | -32.37€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1144 | -0.042 | -46.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1144 | -0.042 | -46.97€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 2353 | +0.120 | +941.65€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 2217 | +0.124 | +929.05€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 511 | +0.141 | +264.33€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 511 | +0.141 | +264.33€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#DOGE | 462 | +0.114 | +157.49€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 462 | +0.114 | +157.49€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 410 | +0.126 | +185.99€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 410 | +0.126 | +185.99€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 375 | +0.134 | +182.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 375 | +0.134 | +182.24€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 459 | +0.101 | +139.00€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 459 | +0.101 | +139.00€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 2496 | -0.023 | -50.22€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2496 | -0.023 | -50.22€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 445 | +0.008 | +22.68€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 445 | +0.008 | +22.68€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 458 | -0.048 | -30.02€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 458 | -0.048 | -30.02€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 606 | -0.046 | -43.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 606 | -0.046 | -43.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 518 | -0.006 | -3.32€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 518 | -0.006 | -3.32€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 469 | -0.016 | +4.07€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 469 | -0.016 | +4.07€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1303 | -0.041 | +136.66€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 601 | -0.066 | +27.55€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 472 | -0.061 | +51.30€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 129 | -0.080 | -23.75€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 458 | -0.011 | +72.15€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 337 | +0.010 | +80.90€ | 1 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 121 | -0.069 | -8.75€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 244 | -0.037 | +36.97€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 208 | -0.029 | +35.13€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 36 | -0.079 | +1.84€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 1017 | -0.031 | +167.33€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 286 | -0.076 | -30.66€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE | 1653 | -0.184 | -31.00€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 652 | -0.173 | -8.02€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 581 | -0.169 | -4.11€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 71 | -0.199 | -3.91€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH | 555 | -0.195 | -29.62€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 492 | -0.202 | -36.25€ | 4 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 63 | -0.131 | +6.63€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 446 | -0.185 | +6.63€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 415 | -0.181 | +4.99€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 31 | -0.227 | +1.64€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#atexpiry | 1488 | -0.184 | -35.37€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 165 | -0.183 | +4.36€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 590 | +0.377 | +533.67€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#BTC | 132 | +0.172 | +100.16€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 132 | +0.172 | +100.16€ | 0 | 6 |
| ✅ RESOLUTION_SNIPER#ETH | 135 | +0.369 | +106.67€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 135 | +0.369 | +106.67€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#SOL | 323 | +0.460 | +326.84€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 323 | +0.460 | +326.84€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 590 | +0.377 | +533.67€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 1031 | +0.040 | +85.25€ | 2 | 3 |
| ✅ STREAK_FADE_15M#15min | 1031 | +0.040 | +85.25€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 359 | +0.015 | +2.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 359 | +0.015 | +2.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 80 | +0.024 | +1.80€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 80 | +0.024 | +1.80€ | 1 | 1 |
| ✅ STREAK_FADE_15M#SOL | 85 | +0.029 | +7.61€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 85 | +0.029 | +7.61€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 507 | +0.062 | +73.50€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 507 | +0.062 | +73.50€ | 1 | 3 |
| ✅ STREAK_FADE_5M | 3644 | -0.023 | -143.55€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3644 | -0.023 | -143.55€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 626 | -0.030 | -28.54€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 626 | -0.030 | -28.54€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 177 | -0.048 | -15.80€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 177 | -0.048 | -15.80€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1714 | -0.018 | -59.02€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1714 | -0.018 | -59.02€ | 1 | 0 |
| ✅ STREAK_FADE_60M | 136 | -0.007 | -5.98€ | 0 | 1 |
| ✅ STREAK_FADE_60M#60min | 136 | -0.007 | -5.98€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 48 | -0.040 | -2.81€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 48 | -0.040 | -2.81€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 82 | +0.000 | -5.49€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 82 | +0.000 | -5.49€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 11665 | +0.013 | +61.62€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11665 | +0.013 | +61.62€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 3007 | +0.017 | +21.32€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 3007 | +0.017 | +21.32€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 3107 | +0.013 | +24.41€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 3107 | +0.013 | +24.41€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2940 | +0.008 | -3.49€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2940 | +0.008 | -3.49€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2611 | +0.014 | +19.37€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2611 | +0.014 | +19.37€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 13591 | +0.019 | +9.29€ | 4 | 0 |
| ✅ STRUCT_NO_15M#15min | 13591 | +0.019 | +9.29€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 5479 | +0.021 | +3.73€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 5479 | +0.021 | +3.73€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 4805 | +0.020 | +7.39€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 4805 | +0.020 | +7.39€ | 4 | 0 |
| ✅ STRUCT_NO_15M#SOL | 3307 | +0.015 | -1.84€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 3307 | +0.015 | -1.84€ | 1 | 0 |
| ✅ UPDOWN_GBM | 123184 | +0.060 | +11771.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 30628 | +0.078 | +6044.67€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 3506 | -0.001 | +40.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 81340 | +0.062 | +5559.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 7292 | -0.002 | +130.98€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 10801 | +0.103 | +1992.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 2028 | +0.166 | +958.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 8683 | +0.090 | +1036.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 27780 | +0.057 | +2462.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 4084 | +0.081 | +921.16€ | 0 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 1027 | -0.001 | +21.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 19232 | +0.066 | +1432.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 3287 | -0.004 | +82.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 150 | -0.066 | +4.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 13813 | +0.074 | +1524.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 2015 | +0.156 | +864.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 11712 | +0.061 | +660.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 28794 | +0.049 | +2060.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 7099 | +0.072 | +1114.57€ | 0 | 9 |
| ✅ UPDOWN_GBM#ETH#240min | 993 | +0.004 | +15.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 17856 | +0.052 | +887.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2706 | -0.001 | +40.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 140 | -0.099 | +2.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 25585 | +0.041 | +1456.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 8298 | +0.033 | +478.13€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 913 | -0.010 | +8.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 14949 | +0.053 | +972.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1299 | +0.004 | +8.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 126 | -0.141 | -10.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 16409 | +0.073 | +2276.32€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 7104 | +0.089 | +1707.82€ | 0 | 12 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 8908 | +0.063 | +570.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 416 | -0.101 | -3.15€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 1062 | +0.363 | +393.44€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 1062 | +0.363 | +393.44€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 507 | +0.362 | +177.09€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 507 | +0.362 | +177.09€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 555 | +0.362 | +216.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 555 | +0.362 | +216.35€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 29116 | -0.017 | +7258.82€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 29116 | -0.017 | +7258.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 2271 | -0.047 | +600.41€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 2271 | -0.047 | +600.41€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 5349 | -0.115 | +304.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 5349 | -0.115 | +304.14€ | 3 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1248 | +0.219 | +1032.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1248 | +0.219 | +1032.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 3910 | +0.217 | +2466.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 3910 | +0.217 | +2466.33€ | 1 | 18 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 8217 | -0.058 | +1217.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 8217 | -0.058 | +1217.29€ | 3 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 8121 | -0.053 | +1638.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 8121 | -0.053 | +1638.27€ | 4 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 362 | +0.060 | +31.26€ | 0 | 9 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 362 | +0.060 | +31.26€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 362 | +0.060 | +31.26€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 362 | +0.060 | +31.26€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1958 | +0.284 | +1671.07€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1958 | +0.284 | +1671.07€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 1030 | +0.278 | +830.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 1030 | +0.278 | +830.29€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 928 | +0.289 | +840.78€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 928 | +0.289 | +840.78€ | 0 | 8 |
| ✅ UPDOWN_OU_5M | 899 | -0.119 | -94.76€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 899 | -0.119 | -94.76€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 289 | -0.084 | -22.53€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 289 | -0.084 | -22.53€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 105 | -0.192 | -14.83€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 105 | -0.192 | -14.83€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 122 | -0.194 | -8.05€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 122 | -0.194 | -8.05€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 5282 | +0.295 | +2363.04€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 2051 | +0.252 | +319.31€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 2045 | +0.287 | +880.07€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 1186 | +0.381 | +1163.66€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.025 n=1505 — no justifica filtro, seguir monitorizando
  - _Datos_: n=1505 IC=+0.025 PNL=+72.88€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 847 celda(s) pasan gate riguroso completo de 3053 evaluadas (n>=40) y 4170 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.033 < 0.08 — monitorear
  - _Datos_: n=8292 IC=+0.033 PNL=+477.64€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=2045/15 IC=+0.287 PNL=+880.07€ | BTC: n=2051/15 IC=+0.252 PNL=+319.31€ | SOL: n=1186/15 IC=+0.381 PNL=+1163.66€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.136 n=1147/60 | contraria IC=+0.185 n=1216 | gap=-0.049 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=641, boost estimado=+0.009. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=2706/40 IC=-0.001 PNL=+40.76€ | BTC#60min: n=3286/40 IC=-0.004 PNL=+81.16€ | SOL#60min: n=1299/40 IC=+0.004 PNL=+8.03€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.044 n=821924 | tras_1loss IC=+0.102 n=621993 | tras_2loss IC=+0.073 n=247195/40 | gap=-0.029 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.151 > 0.08 con n=1247 PNL=+702.09€
  - _Datos_: n=1247 IC=+0.151 PNL=+702.09€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.124 > 0.08 con n=1492 PNL=+660.48€
  - _Datos_: n=1492 IC=+0.124 PNL=+660.48€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.335 > 0.1 con n=4315 PNL=+2500.00€
  - _Datos_: n=4315 IC=+0.335 PNL=+2500.00€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=1240 IC=+0.063 PNL=+123.29€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1240 IC=+0.063 PNL=+123.29€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=116 IC=+0.161 PNL=+68.05€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=116 IC=+0.161 PNL=+68.05€

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
  - _Estado_: n=4779 IC=-0.006 PNL=-49.91€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4779 IC=-0.006 PNL=-49.91€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=2512 IC=+0.007 PNL=+179.85€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=2512 IC=+0.007 PNL=+179.85€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=1505 IC=+0.025 PNL=+72.88€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=1505 IC=+0.025 PNL=+72.88€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.133 > 0.1 con n=8496 PNL=+4045.40€
  - _Datos_: n=8496 IC=+0.133 PNL=+4045.40€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=4083 IC=+0.081 PNL=+920.66€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=4083 IC=+0.081 PNL=+920.66€

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
  - _Estado_: n=1653 IC=+0.041 PNL=+133.58€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=1653 IC=+0.041 PNL=+133.58€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=204 IC=-0.024 PNL=-5.76€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=204 IC=-0.024 PNL=-5.76€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.312 n=397) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=397 IC=+0.312 PNL=+482.97€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.117 > 0.02 con n=1377 PNL=+550.62€
  - _Datos_: n=1377 IC=+0.117 PNL=+550.62€

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
  - _Estado_: n=50583 IC=+0.069 PNL=+6769.52€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=50583 IC=+0.069 PNL=+6769.52€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.126 < -0.1 con n=841 PNL=+138.43€
  - _Datos_: n=841 IC=-0.126 PNL=+138.43€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=4947 IC=+0.067 PNL=+595.30€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=4947 IC=+0.067 PNL=+595.30€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=212 IC=-0.084 PNL=+4.83€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=212 IC=-0.084 PNL=+4.83€

**〰️ H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: n=1324 IC=+0.099 PNL=+321.29€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1324 IC=+0.099 PNL=+321.29€

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
  - _Estado_: n=49137 IC=-0.138 PNL=+3052.20€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=49137 IC=-0.138 PNL=+3052.20€

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
  - _Estado_: n=5277 IC=+0.136 PNL=+3688.63€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=5277 IC=+0.136 PNL=+3688.63€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=12753 IC=+0.057 PNL=+1085.45€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=12753 IC=+0.057 PNL=+1085.45€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.102 > 0.08 con n=5295 PNL=+2999.67€
  - _Datos_: n=5295 IC=+0.102 PNL=+2999.67€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.221 < -0.1 con n=5354 PNL=-442.17€
  - _Datos_: n=5354 IC=-0.221 PNL=-442.17€

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
  - _Estado_: n=135 IC=+0.077 PNL=+23.47€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=135 IC=+0.077 PNL=+23.47€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.094 n=2462) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=2462 IC=+0.094 PNL=+477.53€

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
  - _Estado_: n=20732 IC=+0.176 PNL=-2430.37€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=20732 IC=+0.176 PNL=-2430.37€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.230 > 0.1 con n=343 PNL=+238.17€
  - _Datos_: n=343 IC=+0.230 PNL=+238.17€
