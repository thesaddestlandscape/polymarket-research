# Hipótesis automáticas — 2026-11-22 10:48 UTC
_Generado por shadow_postmortem.py sobre 1450106 resoluciones (PNL=+204756.61€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.5` → IC=-0.317 (n=195)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=738)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.195 (n=1098)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.505 (IC base=+0.122)

- **PATRÓN** `n_total_lado` > `61.0` → IC=+0.171 (n=348)

  - _Acción_: Kelly boost +0.86€ cuando `n_total_lado` > 61.0 (IC base=+0.122)

- **PATRÓN** `banda_hit_calibrado` > `0.8119` → IC=+0.271 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8119 (IC base=+0.122)

- **PATRÓN** `banda_z` > `8.273` → IC=+0.195 (n=346)

  - _Acción_: Kelly boost +0.98€ cuando `banda_z` > 8.273 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.129 (n=1041)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=1126)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.122)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.280 (n=171)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=527)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.193 (n=961)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.505 (IC base=+0.124)

- **PATRÓN** `n_total_lado` > `63.0` → IC=+0.180 (n=307)

  - _Acción_: Kelly boost +0.90€ cuando `n_total_lado` > 63.0 (IC base=+0.124)

- **PATRÓN** `banda_hit_calibrado` > `0.8113` → IC=+0.265 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8113 (IC base=+0.124)

- **PATRÓN** `banda_z` > `8.346` → IC=+0.196 (n=301)

  - _Acción_: Kelly boost +0.98€ cuando `banda_z` > 8.346 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.133 (n=913)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 6.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.125 (n=640)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 12.0 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.128 (n=1026)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `8750.1763` → IC=+0.125 (n=238)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 8750.1763 (IC base=+0.014)

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
- **FILTRO** `restante_s_al_confirmar` < `130.32` → IC=-0.221 (n=12780)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.32
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=38348)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `122.97` → IC=-0.263 (n=1272)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 122.97
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3816)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `114.34` → IC=-0.280 (n=1272)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 114.34
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=3819)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `115.52` → IC=-0.164 (n=3536)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 115.52
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=10611)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `147.3` → IC=-0.257 (n=3519)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 147.3
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=10560)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `127.7` → IC=-0.267 (n=2350)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.7
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=7051)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.210 (n=30217)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `10773.8906` → IC=+0.162 (n=1811)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 10773.8906 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.128 (n=26704)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=32385)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.225 (n=24218)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=8781)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `6328.062` → IC=+0.139 (n=3434)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 6328.062 (IC base=+0.125)

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

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.186 (n=1942)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 7.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.182 (n=2171)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 17.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.328 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.181 (n=2779)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `16038.5479` → IC=+0.186 (n=718)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 16038.5479 (IC base=+0.178)

### FAVORITO_CONFIRMADO#BTC#60min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.335 (n=95)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=2402)

- **PATRÓN** `py_entrada` > `0.61` → IC=+0.173 (n=668)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` > 0.61 (IC base=+0.075)

- **PATRÓN** `libro_liquidez` > `6825.0558` → IC=+0.130 (n=152)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 6825.0558 (IC base=+0.075)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.153 (n=1562)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` < 0.44 (IC base=+0.088)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.171 (n=5518)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 6.0 (IC base=+0.169)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.175 (n=2708)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 8.0 (IC base=+0.169)

- **PATRÓN** `py_entrada` > `0.78` → IC=+0.377 (n=1872)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.78 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.201 (n=2647)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.332 (n=994)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.200 (n=3088)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.195)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.142 (n=710)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 15.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.142 (n=960)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 11.0 (IC base=+0.138)

- **PATRÓN** `py_entrada` > `0.65` → IC=+0.244 (n=650)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.65 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=1193)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `2045.2696` → IC=+0.141 (n=955)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 2045.2696 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `4420.281` → IC=+0.152 (n=156)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4420.281 (IC base=+0.076)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.252 (n=988)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.230)

- **PATRÓN** `py_entrada` > `0.837` → IC=+0.428 (n=1327)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.837 (IC base=+0.230)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.154 (n=753)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.143)

- **PATRÓN** `py_entrada` < `0.345` → IC=+0.278 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.345 (IC base=+0.143)

### FAVORITO_CONFIRMADO#SOL#60min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.306 (n=153)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.160 (n=483)

- **PATRÓN** `py_entrada` > `0.55` → IC=+0.160 (n=483)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` > 0.55 (IC base=+0.047)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.137 (n=533)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.135 (n=1042)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 12.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.255 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.125)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.299 (n=152)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=78)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.199 (n=26674)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=22532)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.224 (n=8476)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.338 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `4915.142` → IC=+0.339 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4915.142 (IC base=+0.193)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=6078)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.163 (n=3847)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 11.0 (IC base=+0.162)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.176 (n=5908)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.210 (n=3737)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.207 (n=2500)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.245 (n=1803)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.204)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.182 (n=5927)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.174 (n=5023)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 15.0 (IC base=+0.173)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.175 (n=6086)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.73 (IC base=+0.173)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.181 (n=4661)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.71 (IC base=+0.173)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.257 (n=4680)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.252)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.253 (n=2285)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.252)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.362 (n=1617)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=5794)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.191 (n=3688)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 11.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.200 (n=1884)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.185)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.428 (n=1021)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.424)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.426 (n=1017)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.424)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.437 (n=1029)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.424)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.429 (n=1101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.424)

- **PATRÓN** `libro_liquidez` > `14030.2627` → IC=+0.449 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14030.2627 (IC base=+0.424)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.443 (n=436)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.438)

- **PATRÓN** `libro_liquidez` > `15265.4378` → IC=+0.443 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15265.4378 (IC base=+0.438)

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
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.402 (n=151)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.400)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.406 (n=147)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.400)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.415 (n=151)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=34881)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.239 (n=34428)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.186 (n=5221)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 18.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.177 (n=11208)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 12.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.186 (n=16077)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.176)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=14558)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.276 (n=6208)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.223)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.190 (n=5984)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.199 (n=12335)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.181)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` > `0.775` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.229 (n=4885)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.221 (n=5628)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.259 (n=6009)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.218)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `py_entrada` < `0.775` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `libro_liquidez` < `3197.0694` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 3197.0694
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.210 (n=13252)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.256 (n=4969)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.206)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.205 (n=5810)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.198 (n=5805)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.246 (n=5875)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=12574)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.140 (n=13687)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.29` → IC=+0.142 (n=11692)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 2.29 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=6123)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.144 (n=6220)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.126 (n=7772)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.77` → IC=+0.142 (n=7669)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 3.77 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=6451)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.136 (n=8264)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.95 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.92` → IC=+0.137 (n=7737)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 2.92 (IC base=+0.116)

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
- **PATRÓN** `drift_60min` |x|≤ `0.5058` → IC=+0.140 (n=19987)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.5058 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.129 (n=20225)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.127 (n=13930)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.9744` → IC=+0.247 (n=6661)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9744 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `0.8716` → IC=+0.294 (n=1093)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8716 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.465` → IC=+0.191 (n=10021)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 3.465 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.6963` → IC=+0.269 (n=5453)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6963 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.3035` → IC=+0.257 (n=2068)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3035 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.741` → IC=+0.234 (n=4824)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.741 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=9679)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `4866.653` → IC=+0.151 (n=6660)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4866.653 (IC base=+0.124)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.123 (n=12630)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0066 (IC base=+0.087)

- **PATRÓN** `ibs_20min` < `0.564` → IC=+0.145 (n=25238)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.564 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.6724` → IC=+0.194 (n=1706)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.6724 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` < `0.1762` → IC=+0.195 (n=10326)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.1762 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` < `0.8577` → IC=+0.195 (n=7014)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.8577 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.296` → IC=+0.232 (n=2560)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.296 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `1.4565` → IC=+0.210 (n=17827)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4565 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.229 (n=17793)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.087)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.243 (n=1416)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.3029` → IC=+0.215 (n=3731)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3029 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.215 (n=4456)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.213 (n=2846)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.9828` → IC=+0.274 (n=1922)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9828 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.803` → IC=+0.292 (n=1006)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.803 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.2345` → IC=+0.259 (n=737)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2345 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.4401` → IC=+0.212 (n=4071)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4401 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.221 (n=4598)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2044.4902` → IC=+0.216 (n=1413)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2044.4902 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.220 (n=3467)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.211)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.247 (n=2559)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.0954` → IC=+0.269 (n=1279)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0954 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.241 (n=3992)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.250 (n=1758)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0769` → IC=+0.280 (n=1281)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0769 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` < `0.0727` → IC=+0.243 (n=3310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0727 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.2898` → IC=+0.249 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2898 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `1.8604` → IC=+0.245 (n=2449)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8604 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.244 (n=2637)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.240)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.233 (n=1217)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.222)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.222 (n=1208)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.1138` → IC=+0.246 (n=1595)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1138 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=3797)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.222 (n=2591)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `0.8919` → IC=+0.259 (n=1207)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8919 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` > `0.748` → IC=+0.235 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.748 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` < `0.5678` → IC=+0.222 (n=4001)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5678 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.741` → IC=+0.265 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.741 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` > `0.6977` → IC=+0.229 (n=3236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6977 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.2772` → IC=+0.270 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2772 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.4399` → IC=+0.249 (n=1193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4399 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.152 (n=3979)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0069 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.0826` → IC=+0.158 (n=1327)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.0826 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.147 (n=2824)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 11.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.7083` → IC=+0.173 (n=3979)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.7083 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.1534` → IC=+0.152 (n=3904)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1534 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.964` → IC=+0.142 (n=3659)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 3.964 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.6288` → IC=+0.155 (n=1327)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6288 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.0977` → IC=+0.160 (n=1445)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.0977 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.4465` → IC=+0.143 (n=3849)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.4465 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.4188` → IC=+0.137 (n=3849)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.4188 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=5170)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `167.0` → IC=+0.185 (n=1278)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 167.0 (IC base=+0.136)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.207 (n=2039)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=4726)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.254 (n=1730)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.899` → IC=+0.280 (n=990)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.899 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` < `0.0966` → IC=+0.193 (n=4035)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.0966 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.3497` → IC=+0.225 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3497 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.7296` → IC=+0.210 (n=1992)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7296 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=5471)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `1907.4384` → IC=+0.199 (n=2037)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1907.4384 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0082` → IC=+0.224 (n=1856)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0082 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.3066` → IC=+0.229 (n=2808)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3066 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.240 (n=1596)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.228 (n=1917)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` < `0.0502` → IC=+0.271 (n=1404)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0502 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.704` → IC=+0.268 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.704 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.3459` → IC=+0.255 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3459 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.152` → IC=+0.232 (n=2712)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.152 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.223 (n=2021)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `1891.6276` → IC=+0.224 (n=1909)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1891.6276 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.224 (n=4056)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.222)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.168 (n=239)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=5434)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.144 (n=728)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.004 (IC base=+0.068)

- **PATRÓN** `ibs_20min` > `0.9422` → IC=+0.248 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9422 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.156` → IC=+0.349 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.156 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` < `0.5912` → IC=+0.343 (n=951)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5912 (IC base=+0.068)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.17` → IC=+0.215 (n=1603)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.17 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` > `1.1103` → IC=+0.362 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1103 (IC base=+0.068)

- **PATRÓN** `volumen_pendiente_norm` < `0.1672` → IC=+0.347 (n=723)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1672 (IC base=+0.068)

- **PATRÓN** `volumen_pendiente_norm` > `0.3037` → IC=+0.354 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3037 (IC base=+0.068)

- **PATRÓN** `volumen_spike_ratio` < `1.4207` → IC=+0.360 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4207 (IC base=+0.068)

- **PATRÓN** `volumen_spike_ratio` > `2.2831` → IC=+0.354 (n=395)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2831 (IC base=+0.068)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.350 (n=883)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.068)

- **PATRÓN** `ibs_20min` < `0.0871` → IC=+0.189 (n=1419)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.0871 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` > `0.3626` → IC=+0.157 (n=709)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.3626 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` < `0.1512` → IC=+0.158 (n=2644)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1512 (IC base=+0.059)

- **PATRÓN** `volumen_regimen` < `0.8287` → IC=+0.162 (n=1858)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8287 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.2782` → IC=+0.202 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2782 (IC base=+0.059)

- **PATRÓN** `volumen_spike_ratio` > `2.4331` → IC=+0.173 (n=895)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.4331 (IC base=+0.059)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.189 (n=159)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=874)

- **FILTRO** `ibs_20min` < `0.2727` → IC=-0.177 (n=258)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2727
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=775)

- **FILTRO** `ibs_20min` > `0.194` → IC=-0.127 (n=5326)

  - _Acción_: SKIP cuando `ibs_20min` > 0.194
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=2624)

- **FILTRO** `sigma_ewma_delta_pct` > `8.253` → IC=-0.232 (n=860)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.253
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=7090)

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

- **PATRÓN** `ibs_20min` < `0.194` → IC=+0.159 (n=2624)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.194 (IC base=-0.032)

- **PATRÓN** `dist_vwap_pct` > `0.2353` → IC=+0.294 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2353 (IC base=-0.032)

- **PATRÓN** `dist_vwap_pct` < `0.3228` → IC=+0.292 (n=1282)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3228 (IC base=-0.032)

- **PATRÓN** `volumen_regimen` < `0.6936` → IC=+0.300 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6936 (IC base=-0.032)

- **PATRÓN** `volumen_regimen` > `1.043` → IC=+0.295 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.043 (IC base=-0.032)

- **PATRÓN** `volumen_pendiente_norm` > `0.0783` → IC=+0.317 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0783 (IC base=-0.032)

- **PATRÓN** `volumen_spike_ratio` < `2.4341` → IC=+0.304 (n=1129)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4341 (IC base=-0.032)

- **PATRÓN** `volumen_spike_ratio` > `1.4174` → IC=+0.299 (n=1128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4174 (IC base=-0.032)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7993` → IC=-0.158 (n=4109)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7993
  - _Potencial_: sin este filtro IC_bueno=+0.144 (n=2118)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.178 (n=1267)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=4960)

- **FILTRO** `ibs_20min` > `0.7246` → IC=-0.190 (n=2144)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7246
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=6437)

- **PATRÓN** `ibs_20min` > `0.7993` → IC=+0.144 (n=2118)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.7993 (IC base=-0.055)

- **PATRÓN** `dist_vwap_pct` > `0.4559` → IC=+0.348 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4559 (IC base=-0.055)

- **PATRÓN** `volumen_regimen` > `0.7044` → IC=+0.319 (n=1137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7044 (IC base=-0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.3064` → IC=+0.319 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3064 (IC base=-0.055)

- **PATRÓN** `volumen_spike_ratio` > `1.8941` → IC=+0.313 (n=832)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8941 (IC base=-0.055)

- **PATRÓN** `dist_vwap_pct` > `1.1048` → IC=+0.283 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1048 (IC base=+0.007)

- **PATRÓN** `volumen_regimen` < `0.7188` → IC=+0.271 (n=1125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7188 (IC base=+0.007)

- **PATRÓN** `volumen_regimen` > `1.2131` → IC=+0.280 (n=852)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2131 (IC base=+0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.238` → IC=+0.282 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.238 (IC base=+0.007)

- **PATRÓN** `volumen_spike_ratio` < `2.488` → IC=+0.263 (n=2427)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.488 (IC base=+0.007)

- **PATRÓN** `volumen_spike_ratio` > `1.4427` → IC=+0.270 (n=2427)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4427 (IC base=+0.007)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.188 (n=8733)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0112 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.8655` → IC=+0.285 (n=11875)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8655 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.9969` → IC=+0.302 (n=1817)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9969 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.457` → IC=+0.167 (n=11804)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.457 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `0.6932` → IC=+0.279 (n=8691)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6932 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2928` → IC=+0.297 (n=2155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2928 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.6437` → IC=+0.289 (n=5062)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6437 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.309 (n=14843)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 88.0 (IC base=+0.087)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.154 (n=11551)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0092 (IC base=+0.088)

- **PATRÓN** `ibs_20min` < `0.5158` → IC=+0.175 (n=22392)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.5158 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` < `0.2023` → IC=+0.283 (n=8643)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2023 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` < `0.8591` → IC=+0.279 (n=5779)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8591 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` > `1.1889` → IC=+0.286 (n=2890)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1889 (IC base=+0.088)

- **PATRÓN** `volumen_pendiente_norm` > `0.295` → IC=+0.323 (n=1917)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.295 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` < `1.4528` → IC=+0.303 (n=4295)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4528 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` > `2.2717` → IC=+0.305 (n=5841)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2717 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.313 (n=12882)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 71.0 (IC base=+0.088)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8132` → IC=-0.146 (n=4639)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8132
  - _Potencial_: sin este filtro IC_bueno=+0.311 (n=2391)

- **FILTRO** `ibs_20min` > `0.7` → IC=-0.240 (n=1578)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=4745)

- **FILTRO** `sigma_ewma_delta_pct` > `4.051` → IC=-0.240 (n=1334)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.051
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=4989)

- **PATRÓN** `ibs_20min` > `0.8132` → IC=+0.311 (n=2391)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8132 (IC base=+0.010)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.132` → IC=+0.174 (n=2624)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 2.132 (IC base=+0.010)

- **PATRÓN** `volumen_pendiente_norm` > `0.2297` → IC=+0.335 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2297 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` < `1.4461` → IC=+0.290 (n=736)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4461 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` > `2.2281` → IC=+0.315 (n=1001)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2281 (IC base=+0.010)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.321 (n=1503)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.010)

- **PATRÓN** `ibs_20min` < `0.1702` → IC=+0.173 (n=1583)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.1702 (IC base=-0.014)

- **PATRÓN** `volumen_pendiente_norm` < `0.1562` → IC=+0.390 (n=1396)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1562 (IC base=-0.014)

- **PATRÓN** `volumen_spike_ratio` < `2.6693` → IC=+0.394 (n=1342)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6693 (IC base=-0.014)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1814` → IC=+0.229 (n=1069)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1814 (IC base=+0.010)

- **PATRÓN** `volumen_regimen` > `0.6957` → IC=+0.220 (n=2278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6957 (IC base=+0.010)

- **PATRÓN** `volumen_pendiente_norm` > `0.2738` → IC=+0.248 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2738 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` < `1.4148` → IC=+0.230 (n=841)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4148 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` > `2.4483` → IC=+0.221 (n=841)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4483 (IC base=+0.010)

- **PATRÓN** `ballena_activa_n` < `369.0` → IC=+0.232 (n=2519)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 369.0 (IC base=+0.010)

- **PATRÓN** `dist_vwap_pct` < `0.155` → IC=+0.265 (n=1975)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.155 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` > `1.0185` → IC=+0.267 (n=864)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0185 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2706` → IC=+0.290 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2706 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.5333` → IC=+0.256 (n=815)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5333 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` > `2.1516` → IC=+0.263 (n=839)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1516 (IC base=+0.005)

- **PATRÓN** `ballena_activa_n` < `197.0` → IC=+0.276 (n=820)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 197.0 (IC base=+0.005)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0116` → IC=+0.318 (n=1631)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0116 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.295 (n=3607)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.284)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.323 (n=1944)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.582` → IC=+0.305 (n=2438)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.582 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` < `0.1308` → IC=+0.292 (n=3345)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1308 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` > `3.2547` → IC=+0.300 (n=1166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.2547 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.292 (n=4343)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `2020.5034` → IC=+0.297 (n=1198)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2020.5034 (IC base=+0.284)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.302 (n=2209)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.337 (n=2229)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.308)

- **PATRÓN** `drift_60min` |x|≤ `0.1877` → IC=+0.328 (n=1472)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1877 (IC base=+0.308)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.325 (n=1281)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.308)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.312 (n=1518)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.308)

- **PATRÓN** `ibs_20min` < `0.0289` → IC=+0.309 (n=1471)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0289 (IC base=+0.308)

- **PATRÓN** `ibs_20min` > `0.1542` → IC=+0.319 (n=2228)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1542 (IC base=+0.308)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.056` → IC=+0.318 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.056 (IC base=+0.308)

- **PATRÓN** `volumen_pendiente_norm` < `0.1993` → IC=+0.309 (n=3318)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1993 (IC base=+0.308)

- **PATRÓN** `volumen_pendiente_norm` > `0.3446` → IC=+0.317 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3446 (IC base=+0.308)

- **PATRÓN** `volumen_spike_ratio` > `2.7409` → IC=+0.326 (n=1468)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7409 (IC base=+0.308)

- **PATRÓN** `libro_liquidez` > `2006.1448` → IC=+0.319 (n=1114)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2006.1448 (IC base=+0.308)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.312 (n=2246)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.308)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **PATRÓN** `dist_vwap_pct` > `0.1581` → IC=+0.236 (n=1182)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1581 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.6312` → IC=+0.236 (n=2624)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6312 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `1.1683` → IC=+0.236 (n=2387)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1683 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` > `0.5964` → IC=+0.235 (n=2387)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5964 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` < `0.1634` → IC=+0.236 (n=2507)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1634 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.1031` → IC=+0.243 (n=781)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1031 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `2.4161` → IC=+0.241 (n=2319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4161 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` > `1.4963` → IC=+0.236 (n=2071)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4963 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `113.0` → IC=+0.252 (n=2370)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 113.0 (IC base=+0.025)

- **PATRÓN** `ibs_20min` < `0.0913` → IC=+0.152 (n=1651)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.0913 (IC base=+0.012)

- **PATRÓN** `dist_vwap_pct` < `0.384` → IC=+0.261 (n=1932)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.384 (IC base=+0.012)

- **PATRÓN** `volumen_regimen` < `1.1822` → IC=+0.263 (n=1742)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1822 (IC base=+0.012)

- **PATRÓN** `volumen_regimen` > `0.6147` → IC=+0.260 (n=1742)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6147 (IC base=+0.012)

- **PATRÓN** `volumen_pendiente_norm` < `0.1015` → IC=+0.266 (n=1638)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1015 (IC base=+0.012)

- **PATRÓN** `volumen_pendiente_norm` > `0.1619` → IC=+0.283 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1619 (IC base=+0.012)

- **PATRÓN** `volumen_spike_ratio` < `1.7856` → IC=+0.283 (n=1120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7856 (IC base=+0.012)

- **PATRÓN** `volumen_spike_ratio` > `2.426` → IC=+0.274 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.426 (IC base=+0.012)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.281 (n=1705)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.012)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.75` → IC=-0.247 (n=2698)

  - _Acción_: SKIP cuando `ibs_20min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.314 (n=2701)

- **FILTRO** `ibs_20min` > `0.6071` → IC=-0.237 (n=1269)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6071
  - _Potencial_: sin este filtro IC_bueno=+0.166 (n=3810)

- **FILTRO** `sigma_ewma_delta_pct` > `8.241` → IC=-0.266 (n=580)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.241
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=4499)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.314 (n=2701)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.75 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` > `1.1068` → IC=+0.350 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1068 (IC base=+0.034)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.438` → IC=+0.158 (n=2207)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 2.438 (IC base=+0.034)

- **PATRÓN** `volumen_regimen` < `0.8446` → IC=+0.350 (n=1317)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8446 (IC base=+0.034)

- **PATRÓN** `volumen_regimen` > `0.6974` → IC=+0.335 (n=1765)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6974 (IC base=+0.034)

- **PATRÓN** `volumen_pendiente_norm` < `0.0993` → IC=+0.337 (n=1862)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0993 (IC base=+0.034)

- **PATRÓN** `volumen_pendiente_norm` > `0.2747` → IC=+0.368 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2747 (IC base=+0.034)

- **PATRÓN** `volumen_spike_ratio` < `1.4321` → IC=+0.363 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4321 (IC base=+0.034)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.354 (n=1722)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.034)

- **PATRÓN** `ibs_20min` < `0.6071` → IC=+0.166 (n=3810)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.6071 (IC base=+0.065)

- **PATRÓN** `dist_vwap_pct` < `0.3259` → IC=+0.275 (n=2047)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3259 (IC base=+0.065)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.728` → IC=+0.133 (n=3981)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 4.728 (IC base=+0.065)

- **PATRÓN** `volumen_regimen` < `0.6899` → IC=+0.286 (n=872)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6899 (IC base=+0.065)

- **PATRÓN** `volumen_pendiente_norm` > `0.0717` → IC=+0.300 (n=792)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0717 (IC base=+0.065)

- **PATRÓN** `volumen_spike_ratio` < `1.7989` → IC=+0.284 (n=1283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7989 (IC base=+0.065)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.292 (n=1957)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 45.0 (IC base=+0.065)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.354 (n=2518)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.314)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.317 (n=2843)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.314)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.316 (n=2961)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.314)

- **PATRÓN** `ibs_20min` > `0.651` → IC=+0.339 (n=2817)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.651 (IC base=+0.314)

- **PATRÓN** `dist_vwap_pct` > `0.22` → IC=+0.338 (n=1507)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.22 (IC base=+0.314)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.81` → IC=+0.338 (n=1104)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.81 (IC base=+0.314)

- **PATRÓN** `volumen_regimen` > `0.6288` → IC=+0.325 (n=2817)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6288 (IC base=+0.314)

- **PATRÓN** `volumen_pendiente_norm` > `0.2844` → IC=+0.347 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2844 (IC base=+0.314)

- **PATRÓN** `volumen_spike_ratio` > `1.5323` → IC=+0.326 (n=2431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5323 (IC base=+0.314)

- **PATRÓN** `libro_liquidez` > `3006.4708` → IC=+0.323 (n=939)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3006.4708 (IC base=+0.314)

- **PATRÓN** `sigma_h` > `0.0141` → IC=+0.349 (n=2026)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0141 (IC base=+0.313)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.316 (n=3040)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.313)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.314 (n=3047)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.313)

- **PATRÓN** `ibs_20min` < `0.3889` → IC=+0.328 (n=3039)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3889 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` > `1.296` → IC=+0.322 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.296 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` < `0.2575` → IC=+0.316 (n=2997)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2575 (IC base=+0.313)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.143` → IC=+0.326 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.143 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` < `0.7156` → IC=+0.315 (n=1338)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7156 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` > `1.2103` → IC=+0.340 (n=1013)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2103 (IC base=+0.313)

- **PATRÓN** `volumen_pendiente_norm` > `0.2867` → IC=+0.365 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2867 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` < `1.4133` → IC=+0.323 (n=952)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4133 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` > `2.1493` → IC=+0.317 (n=1294)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1493 (IC base=+0.313)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.221 (n=6394)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0127 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.1263` → IC=+0.193 (n=8443)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1263 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=19945)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.5357` → IC=+0.229 (n=19179)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5357 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.1698` → IC=+0.207 (n=7224)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1698 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.963` → IC=+0.255 (n=5014)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.963 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `1.1741` → IC=+0.152 (n=12790)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1741 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `0.6216` → IC=+0.152 (n=12789)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6216 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.2933` → IC=+0.207 (n=2760)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2933 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.5992` → IC=+0.185 (n=6226)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.5992 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.191 (n=18140)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 85.0 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.194 (n=8423)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0061 (IC base=+0.186)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.187 (n=12753)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0082 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.0849` → IC=+0.222 (n=6376)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0849 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.207 (n=9166)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` < `0.5254` → IC=+0.239 (n=19127)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5254 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` < `0.1957` → IC=+0.180 (n=13978)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.1957 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.423` → IC=+0.190 (n=3019)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 9.423 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.49` → IC=+0.192 (n=17078)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 2.49 (IC base=+0.186)

- **PATRÓN** `volumen_regimen` < `0.7013` → IC=+0.172 (n=5963)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.7013 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.2952` → IC=+0.219 (n=2873)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2952 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `2.633` → IC=+0.197 (n=6096)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.633 (IC base=+0.186)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.200 (n=18092)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 89.0 (IC base=+0.186)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.264 (n=1051)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.229)

- **PATRÓN** `drift_60min` |x|≤ `0.1069` → IC=+0.261 (n=1384)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1069 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.236 (n=3286)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.229)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.229 (n=2141)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` > `0.9421` → IC=+0.293 (n=2098)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9421 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.458` → IC=+0.328 (n=1032)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.458 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` > `0.2317` → IC=+0.283 (n=610)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2317 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` < `1.8312` → IC=+0.227 (n=2007)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8312 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` > `1.4363` → IC=+0.228 (n=3010)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4363 (IC base=+0.229)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=3423)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.229)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.256 (n=2649)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.254)

- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.262 (n=1765)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0078 (IC base=+0.254)

- **PATRÓN** `drift_60min` |x|≤ `0.1003` → IC=+0.306 (n=1165)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1003 (IC base=+0.254)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.257 (n=2727)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.254)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.260 (n=2413)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.254)

- **PATRÓN** `ibs_20min` < `0.0022` → IC=+0.311 (n=883)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0022 (IC base=+0.254)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.93` → IC=+0.258 (n=2617)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.93 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` < `0.1005` → IC=+0.257 (n=2334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1005 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` > `0.301` → IC=+0.266 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.301 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` < `1.5538` → IC=+0.264 (n=1120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5538 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` > `2.6917` → IC=+0.258 (n=848)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6917 (IC base=+0.254)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.262 (n=1832)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.254)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.189 (n=982)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0033 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.0673` → IC=+0.174 (n=977)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0673 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=3062)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.2514` → IC=+0.203 (n=2931)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2514 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.1952` → IC=+0.211 (n=1426)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1952 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.561` → IC=+0.205 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.561 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.8528` → IC=+0.132 (n=1954)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.8528 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` > `1.0475` → IC=+0.131 (n=1329)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 1.0475 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.174 (n=449)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.5077` → IC=+0.130 (n=1270)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.5077 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `2.455` → IC=+0.142 (n=962)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.455 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `389.0` → IC=+0.132 (n=2858)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 389.0 (IC base=+0.127)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.181 (n=2790)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.006 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.2544` → IC=+0.175 (n=2788)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2544 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.180 (n=1509)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.6117` → IC=+0.212 (n=3168)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6117 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.2198` → IC=+0.177 (n=3441)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.2198 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.893` → IC=+0.179 (n=586)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 10.893 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.001` → IC=+0.157 (n=2780)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 4.001 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `1.2068` → IC=+0.163 (n=3168)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2068 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` < `0.0718` → IC=+0.155 (n=2647)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.0718 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.4796` → IC=+0.157 (n=3040)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4796 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `204.0` → IC=+0.193 (n=1323)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 204.0 (IC base=+0.153)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.230 (n=1473)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.2562` → IC=+0.234 (n=2163)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2562 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.219 (n=3392)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.287 (n=1717)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.006` → IC=+0.304 (n=768)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.006 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.3498` → IC=+0.236 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3498 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.7128` → IC=+0.223 (n=1438)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7128 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.213 (n=3944)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2015.541` → IC=+0.222 (n=1081)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2015.541 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0123` → IC=+0.245 (n=2929)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0123 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.2526` → IC=+0.268 (n=1951)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2526 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.276 (n=1108)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0419` → IC=+0.295 (n=1289)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0419 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.814` → IC=+0.288 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.814 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.3536` → IC=+0.286 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3536 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.7663` → IC=+0.242 (n=1248)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7663 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.1766` → IC=+0.254 (n=1891)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1766 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1883.8084` → IC=+0.249 (n=1326)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1883.8084 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.240 (n=2814)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.240)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.194 (n=1056)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0039 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.0816` → IC=+0.173 (n=1056)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.0816 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=3282)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.245` → IC=+0.188 (n=3166)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.245 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.1488` → IC=+0.188 (n=1788)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1488 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.201` → IC=+0.204 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.201 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8369` → IC=+0.138 (n=2111)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.8369 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` > `1.1756` → IC=+0.127 (n=1056)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 1.1756 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2872` → IC=+0.176 (n=474)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2872 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.5167` → IC=+0.127 (n=1364)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.5167 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.5013` → IC=+0.136 (n=1033)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.5013 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `6932.744` → IC=+0.195 (n=1436)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 6932.744 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `123.0` → IC=+0.127 (n=3110)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 123.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.173 (n=2265)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0057 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.4295` → IC=+0.149 (n=3388)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.4295 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.165 (n=1623)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.6681` → IC=+0.190 (n=3389)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.6681 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.1708` → IC=+0.157 (n=3467)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1708 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.508` → IC=+0.140 (n=1160)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 6.508 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.064` → IC=+0.133 (n=3016)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 4.064 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.8536` → IC=+0.151 (n=2259)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8536 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.2925` → IC=+0.169 (n=511)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.2925 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.189` → IC=+0.135 (n=2840)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.189 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.5144` → IC=+0.136 (n=2882)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.5144 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `6679.7564` → IC=+0.192 (n=1536)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 6679.7564 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.155 (n=1092)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 48.0 (IC base=+0.133)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.013` → IC=+0.173 (n=1179)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.013 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.136 (n=3628)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.5937` → IC=+0.225 (n=3150)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5937 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `0.7959` → IC=+0.214 (n=900)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7959 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.984` → IC=+0.284 (n=744)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.984 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `1.1665` → IC=+0.131 (n=3526)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.1665 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` > `0.6273` → IC=+0.123 (n=3526)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.6273 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` < `0.163` → IC=+0.124 (n=3602)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.163 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `1.7906` → IC=+0.127 (n=2282)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.7906 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2714.6923` → IC=+0.198 (n=1599)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2714.6923 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.129 (n=1195)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 16.0 (IC base=+0.121)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.151 (n=3256)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0111 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.1186` → IC=+0.168 (n=1234)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.1186 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=3772)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` < `0.6429` → IC=+0.222 (n=3701)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6429 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` < `0.2271` → IC=+0.147 (n=3677)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.2271 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.229` → IC=+0.146 (n=3274)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 2.229 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `1.1798` → IC=+0.130 (n=3700)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1798 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.8605` → IC=+0.127 (n=2467)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.8605 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` < `0.1635` → IC=+0.127 (n=3660)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1635 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2767` → IC=+0.147 (n=516)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.2767 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.4388` → IC=+0.141 (n=1172)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.4388 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.4451` → IC=+0.135 (n=1172)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.4451 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `2613.7824` → IC=+0.189 (n=1678)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2613.7824 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.131 (n=3511)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 43.0 (IC base=+0.124)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.246 (n=3168)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.1682` → IC=+0.243 (n=1394)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1682 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=3295)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=2865)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.6646` → IC=+0.256 (n=3168)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6646 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.1868` → IC=+0.235 (n=1947)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1868 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` < `0.8385` → IC=+0.228 (n=3263)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8385 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.459` → IC=+0.271 (n=775)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.459 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `0.6187` → IC=+0.236 (n=3168)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6187 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2347` → IC=+0.265 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2347 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `2.1643` → IC=+0.228 (n=2721)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1643 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.8271` → IC=+0.229 (n=2061)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8271 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2623.8724` → IC=+0.233 (n=2112)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2623.8724 (IC base=+0.226)

- **PATRÓN** `sigma_h` > `0.0164` → IC=+0.248 (n=2200)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0164 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.6165` → IC=+0.247 (n=3298)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6165 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.248 (n=1620)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.242 (n=1491)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.0385` → IC=+0.298 (n=1453)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0385 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` > `0.3274` → IC=+0.245 (n=786)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3274 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.04` → IC=+0.271 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.04 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` < `0.8673` → IC=+0.241 (n=2199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8673 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` > `1.0478` → IC=+0.243 (n=1495)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0478 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2849` → IC=+0.294 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2849 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.851` → IC=+0.236 (n=2085)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.851 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `1.5546` → IC=+0.239 (n=2793)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5546 (IC base=+0.238)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.203 (n=1682)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.1437` → IC=+0.172 (n=2219)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1437 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=5266)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.6599` → IC=+0.222 (n=3359)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6599 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.9083` → IC=+0.180 (n=777)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.9083 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.501` → IC=+0.210 (n=813)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.501 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `0.857` → IC=+0.165 (n=3057)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.857 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` > `1.1888` → IC=+0.158 (n=1528)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 1.1888 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.1557` → IC=+0.171 (n=1301)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.1557 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.5265` → IC=+0.160 (n=2164)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.5265 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.159 (n=4240)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `7172.5751` → IC=+0.195 (n=2285)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 7172.5751 (IC base=+0.154)

- **PATRÓN** `ibs_20min` < `0.3876` → IC=+0.179 (n=3664)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.3876 (IC base=+0.102)

- **PATRÓN** `ballena_activa_n` < `136.0` → IC=+0.121 (n=5342)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 136.0 (IC base=+0.102)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.207 (n=1205)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0063 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.1055` → IC=+0.234 (n=531)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1055 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.229 (n=1088)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` > `0.6262` → IC=+0.260 (n=803)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6262 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` > `0.3251` → IC=+0.232 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3251 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.923` → IC=+0.226 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.923 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` < `0.6261` → IC=+0.230 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6261 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.09` → IC=+0.214 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.09 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` < `2.1519` → IC=+0.211 (n=1040)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1519 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `13762.5784` → IC=+0.206 (n=803)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13762.5784 (IC base=+0.198)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.156 (n=504)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0032 (IC base=+0.069)

- **PATRÓN** `ibs_20min` < `0.2189` → IC=+0.190 (n=662)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.2189 (IC base=+0.069)

- **PATRÓN** `ballena_activa_n` < `171.0` → IC=+0.164 (n=652)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 171.0 (IC base=+0.069)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.239 (n=519)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.1328` → IC=+0.159 (n=682)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1328 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=1611)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.7661` → IC=+0.259 (n=703)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7661 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.1568` → IC=+0.169 (n=740)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1568 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.945` → IC=+0.189 (n=220)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 9.945 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.8322` → IC=+0.158 (n=1033)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8322 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.2177` → IC=+0.185 (n=271)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2177 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.4672` → IC=+0.169 (n=509)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.4672 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `7898.5704` → IC=+0.179 (n=703)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 7898.5704 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.150 (n=515)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 30.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.122 (n=1544)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0081 (IC base=+0.110)

- **PATRÓN** `ibs_20min` < `0.0876` → IC=+0.216 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0876 (IC base=+0.110)

- **PATRÓN** `volumen_regimen` < `0.6744` → IC=+0.145 (n=679)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.6744 (IC base=+0.110)

- **PATRÓN** `volumen_pendiente_norm` > `0.2229` → IC=+0.130 (n=263)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` > 0.2229 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `5585.8391` → IC=+0.150 (n=1028)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 5585.8391 (IC base=+0.110)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.150 (n=664)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 40.0 (IC base=+0.110)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.154 (n=461)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0071 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.136 (n=1383)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 6.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.5294` → IC=+0.182 (n=1236)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.5294 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `1.045` → IC=+0.149 (n=246)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 1.045 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.871` → IC=+0.227 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.871 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `1.0461` → IC=+0.126 (n=1216)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.0461 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.2225` → IC=+0.139 (n=236)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.2225 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `1.4182` → IC=+0.147 (n=448)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4182 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `3060.1971` → IC=+0.152 (n=461)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3060.1971 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.5517` → IC=+0.171 (n=1337)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.5517 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `2773.9701` → IC=+0.164 (n=689)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2773.9701 (IC base=+0.092)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.121 (n=1307)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 27.0 (IC base=+0.092)

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
- **PATRÓN** `sigma_h` > `0.0128` → IC=+0.227 (n=8446)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0128 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=26439)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.9669` → IC=+0.302 (n=8439)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9669 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.946` → IC=+0.216 (n=2941)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.946 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.907` → IC=+0.261 (n=6192)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.907 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.2131` → IC=+0.160 (n=17073)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2131 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2408` → IC=+0.214 (n=4518)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2408 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6252` → IC=+0.193 (n=8247)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6252 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.200 (n=23947)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.209 (n=7841)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.3984` → IC=+0.201 (n=20703)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3984 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=8795)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.4863` → IC=+0.253 (n=20699)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4863 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` < `0.1904` → IC=+0.182 (n=15034)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.1904 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.504` → IC=+0.205 (n=21922)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.504 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `0.6286` → IC=+0.179 (n=5258)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.6286 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.2937` → IC=+0.256 (n=3243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2937 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `2.6242` → IC=+0.212 (n=7544)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6242 (IC base=+0.199)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.214 (n=22411)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.199)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.276 (n=1350)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.3776` → IC=+0.236 (n=4036)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3776 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.240 (n=4239)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.235 (n=2722)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` > `0.8614` → IC=+0.294 (n=2691)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8614 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.029` → IC=+0.301 (n=2646)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.029 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.2328` → IC=+0.288 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2328 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.288` → IC=+0.240 (n=1771)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.288 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.247 (n=4361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `2044.42` → IC=+0.241 (n=1345)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2044.42 (IC base=+0.235)

- **PATRÓN** `sigma_h` < `0.0107` → IC=+0.268 (n=3689)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0107 (IC base=+0.266)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.268 (n=2458)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.266)

- **PATRÓN** `drift_60min` |x|≤ `0.1274` → IC=+0.293 (n=1623)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1274 (IC base=+0.266)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.267 (n=3831)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.266)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.270 (n=3322)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.266)

- **PATRÓN** `ibs_20min` < `0.4667` → IC=+0.287 (n=3244)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4667 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` < `0.0989` → IC=+0.269 (n=3358)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0989 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` > `0.293` → IC=+0.285 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.293 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` < `1.5681` → IC=+0.266 (n=1563)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5681 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` > `2.6495` → IC=+0.275 (n=1184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6495 (IC base=+0.266)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.271 (n=2532)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.266)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.272 (n=1308)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.266)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.174 (n=1391)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0033 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.0822` → IC=+0.146 (n=1388)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.0822 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=4341)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.3001` → IC=+0.203 (n=3718)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3001 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.3446` → IC=+0.201 (n=1313)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3446 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.264` → IC=+0.171 (n=864)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 9.264 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.6356` → IC=+0.155 (n=1389)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6356 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `1.067` → IC=+0.144 (n=1887)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.067 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2719` → IC=+0.193 (n=584)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2719 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.166` → IC=+0.144 (n=3601)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.166 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.5192` → IC=+0.145 (n=3656)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.5192 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `290.0` → IC=+0.153 (n=2705)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 290.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.172 (n=3247)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.006 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.0835` → IC=+0.173 (n=1232)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0835 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=1357)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` < `0.6803` → IC=+0.192 (n=3685)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.6803 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.1547` → IC=+0.162 (n=3631)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1547 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.206` → IC=+0.151 (n=3763)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 6.206 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `1.0418` → IC=+0.156 (n=3243)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.0418 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.2211` → IC=+0.196 (n=673)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2211 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.4321` → IC=+0.151 (n=3574)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4321 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `1.7707` → IC=+0.152 (n=2383)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.7707 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=4786)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `212.0` → IC=+0.180 (n=1169)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 212.0 (IC base=+0.146)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0135` → IC=+0.239 (n=1403)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0135 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.236 (n=4416)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=1561)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.97` → IC=+0.315 (n=936)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.97 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.3485` → IC=+0.234 (n=551)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3485 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.7573` → IC=+0.241 (n=1870)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7573 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.229 (n=5116)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `1905.4784` → IC=+0.236 (n=1909)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1905.4784 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0113` → IC=+0.247 (n=3585)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0113 (IC base=+0.245)

- **PATRÓN** `drift_60min` |x|≤ `0.1853` → IC=+0.259 (n=1792)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1853 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.263 (n=1545)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.250 (n=1860)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.0676` → IC=+0.299 (n=1359)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0676 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.949` → IC=+0.304 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.949 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.3473` → IC=+0.301 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3473 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `2.1714` → IC=+0.257 (n=2627)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1714 (IC base=+0.245)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.249 (n=1966)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `2003.547` → IC=+0.253 (n=1357)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2003.547 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.248 (n=3472)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.245)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.190 (n=1461)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0039 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.3544` → IC=+0.147 (n=3854)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3544 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=4551)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.8775` → IC=+0.267 (n=1461)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8775 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.149` → IC=+0.167 (n=2166)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.149 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.187` → IC=+0.171 (n=872)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 9.187 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.8577` → IC=+0.153 (n=2921)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8577 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.2783` → IC=+0.201 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2783 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `1.5173` → IC=+0.155 (n=1885)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.5173 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `2.1549` → IC=+0.144 (n=1941)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.1549 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `5851.4217` → IC=+0.231 (n=1986)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5851.4217 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.142 (n=2850)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 85.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.174 (n=3257)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0071 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.46` → IC=+0.159 (n=3700)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.46 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=1361)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` < `0.569` → IC=+0.214 (n=3256)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.569 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` < `0.6342` → IC=+0.157 (n=4286)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.6342 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.038` → IC=+0.155 (n=741)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 9.038 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.018` → IC=+0.154 (n=3220)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 3.018 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `0.8525` → IC=+0.163 (n=2467)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8525 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.2929` → IC=+0.204 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2929 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `2.1974` → IC=+0.155 (n=3156)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.1974 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `1.5242` → IC=+0.158 (n=3203)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.5242 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `6741.2976` → IC=+0.216 (n=1233)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6741.2976 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.171 (n=1236)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 57.0 (IC base=+0.152)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.155 (n=1488)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0132 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.149 (n=3150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` > `0.6966` → IC=+0.257 (n=2971)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6966 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `1.0588` → IC=+0.201 (n=744)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0588 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.214` → IC=+0.269 (n=1134)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.214 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.2098` → IC=+0.127 (n=4458)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.2098 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.1012` → IC=+0.122 (n=4247)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1012 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.136 (n=556)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `2.4945` → IC=+0.124 (n=4351)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.4945 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2477.4482` → IC=+0.223 (n=2021)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2477.4482 (IC base=+0.120)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.159 (n=3657)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0112 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.1428` → IC=+0.152 (n=1383)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1428 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.149 (n=4268)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.5385` → IC=+0.247 (n=3650)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5385 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.2242` → IC=+0.153 (n=3824)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.2242 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.032` → IC=+0.161 (n=4027)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` < 3.032 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.6382` → IC=+0.153 (n=1383)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6382 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2312` → IC=+0.201 (n=724)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2312 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.4381` → IC=+0.164 (n=1320)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.4381 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.479` → IC=+0.144 (n=1320)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.479 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `2654.6046` → IC=+0.221 (n=1383)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2654.6046 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.151 (n=3977)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 48.0 (IC base=+0.138)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.257 (n=4074)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.243 (n=4261)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.242 (n=2733)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` > `0.9873` → IC=+0.307 (n=1361)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9873 (IC base=+0.237)

- **PATRÓN** `dist_vwap_pct` > `0.2044` → IC=+0.252 (n=2072)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2044 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.048` → IC=+0.296 (n=722)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.048 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` < `1.2138` → IC=+0.238 (n=4075)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2138 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` > `0.6422` → IC=+0.243 (n=4074)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6422 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.0789` → IC=+0.255 (n=1620)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0789 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.5104` → IC=+0.258 (n=1330)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5104 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `2644.235` → IC=+0.242 (n=2716)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2644.235 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0249` → IC=+0.269 (n=1413)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0249 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.249 (n=3982)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` < `0.1385` → IC=+0.307 (n=1864)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1385 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` > `1.1893` → IC=+0.249 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1893 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` < `0.231` → IC=+0.249 (n=4078)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.231 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.979` → IC=+0.278 (n=792)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.979 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` < `0.7152` → IC=+0.246 (n=1864)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7152 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` > `1.2196` → IC=+0.265 (n=1412)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2196 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` > `0.2867` → IC=+0.314 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2867 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `1.4345` → IC=+0.248 (n=4020)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4345 (IC base=+0.244)

### GBM_LATE_5M
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.240 (n=2433)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.5383` → IC=+0.232 (n=7299)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5383 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=7331)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.9286` → IC=+0.258 (n=2435)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9286 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` < `0.9552` → IC=+0.225 (n=5966)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9552 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.441` → IC=+0.231 (n=2431)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.441 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` < `0.7091` → IC=+0.230 (n=2274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7091 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `0.8828` → IC=+0.224 (n=3444)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8828 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` < `0.1037` → IC=+0.224 (n=6833)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1037 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.1642` → IC=+0.231 (n=2049)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1642 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` < `1.449` → IC=+0.234 (n=2394)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.449 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.228 (n=5223)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `5088.626` → IC=+0.234 (n=3309)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5088.626 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.230 (n=1740)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.212)

- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.214 (n=3475)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0073 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.4161` → IC=+0.224 (n=4582)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4161 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.226 (n=1741)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.226 (n=2352)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.7288` → IC=+0.218 (n=5207)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7288 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.7086` → IC=+0.220 (n=884)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7086 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` < `0.2553` → IC=+0.205 (n=4607)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2553 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.728` → IC=+0.226 (n=4725)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.728 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `1.2534` → IC=+0.212 (n=4735)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2534 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` > `0.7296` → IC=+0.205 (n=4230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7296 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` < `0.0982` → IC=+0.215 (n=4812)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0982 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.5316` → IC=+0.216 (n=2257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5316 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `1.8145` → IC=+0.219 (n=3419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8145 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.237 (n=3439)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 51.0 (IC base=+0.212)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.279 (n=836)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.271)

- **PATRÓN** `drift_60min` |x|≤ `0.0855` → IC=+0.302 (n=316)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0855 (IC base=+0.271)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.283 (n=483)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.271)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.270 (n=952)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.271)

- **PATRÓN** `ibs_20min` < `0.1414` → IC=+0.296 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1414 (IC base=+0.271)

- **PATRÓN** `dist_vwap_pct` < `0.5307` → IC=+0.279 (n=1049)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5307 (IC base=+0.271)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.129` → IC=+0.298 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.129 (IC base=+0.271)

- **PATRÓN** `volumen_regimen` < `1.2303` → IC=+0.276 (n=948)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2303 (IC base=+0.271)

- **PATRÓN** `volumen_regimen` > `0.8784` → IC=+0.290 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8784 (IC base=+0.271)

- **PATRÓN** `volumen_pendiente_norm` > `0.2875` → IC=+0.341 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2875 (IC base=+0.271)

- **PATRÓN** `volumen_spike_ratio` < `2.4928` → IC=+0.279 (n=943)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4928 (IC base=+0.271)

- **PATRÓN** `libro_liquidez` > `12913.0263` → IC=+0.282 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12913.0263 (IC base=+0.271)

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
- **PATRÓN** `sigma_h` < `0.0086` → IC=+0.221 (n=1987)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0086 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.4724` → IC=+0.220 (n=1986)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4724 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.235 (n=700)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` < `0.4713` → IC=+0.224 (n=1324)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4713 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `0.1432` → IC=+0.214 (n=1986)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1432 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` < `0.4198` → IC=+0.224 (n=1993)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4198 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.92` → IC=+0.224 (n=1806)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.92 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` < `0.8711` → IC=+0.216 (n=1324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8711 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` > `1.2332` → IC=+0.214 (n=662)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2332 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` < `0.0999` → IC=+0.216 (n=1839)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0999 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `1.4052` → IC=+0.227 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4052 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `1.4954` → IC=+0.215 (n=1732)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4954 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.213 (n=2004)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.213)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.243 (n=539)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.5101` → IC=+0.222 (n=1612)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5101 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.216 (n=607)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.223 (n=727)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `0.0842` → IC=+0.214 (n=1611)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0842 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `0.7081` → IC=+0.222 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7081 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.266` → IC=+0.211 (n=1463)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.266 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` < `1.2588` → IC=+0.213 (n=1613)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2588 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` > `0.7215` → IC=+0.211 (n=1441)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7215 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.0726` → IC=+0.228 (n=671)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0726 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `1.5082` → IC=+0.211 (n=694)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5082 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `1.7767` → IC=+0.213 (n=1052)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7767 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.209 (n=2120)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `7916.4834` → IC=+0.216 (n=1074)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7916.4834 (IC base=+0.207)

- **PATRÓN** `ballena_activa_n` < `95.0` → IC=+0.212 (n=1602)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 95.0 (IC base=+0.207)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.235 (n=425)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0078 (IC base=+0.214)

- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.219 (n=578)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.240 (n=1201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.214 (n=1174)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `0.9855` → IC=+0.297 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9855 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` > `1.1022` → IC=+0.246 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1022 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.98` → IC=+0.263 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.98 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` < `0.643` → IC=+0.245 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.643 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` > `1.2457` → IC=+0.214 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2457 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` < `0.1056` → IC=+0.216 (n=1169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1056 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.2735` → IC=+0.233 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2735 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` < `2.1623` → IC=+0.223 (n=1093)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1623 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.223 (n=1494)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.214)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.219 (n=1265)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.214)

- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.258 (n=638)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.249)

- **PATRÓN** `drift_60min` |x|≤ `0.6921` → IC=+0.264 (n=956)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6921 (IC base=+0.249)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.270 (n=664)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.249)

- **PATRÓN** `ibs_20min` < `0.7347` → IC=+0.272 (n=956)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7347 (IC base=+0.249)

- **PATRÓN** `dist_vwap_pct` > `0.5982` → IC=+0.250 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5982 (IC base=+0.249)

- **PATRÓN** `dist_vwap_pct` < `0.3347` → IC=+0.259 (n=848)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3347 (IC base=+0.249)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.99` → IC=+0.269 (n=902)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.99 (IC base=+0.249)

- **PATRÓN** `volumen_regimen` < `0.7522` → IC=+0.264 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7522 (IC base=+0.249)

- **PATRÓN** `volumen_pendiente_norm` < `0.1037` → IC=+0.260 (n=857)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1037 (IC base=+0.249)

- **PATRÓN** `volumen_spike_ratio` > `2.1886` → IC=+0.274 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1886 (IC base=+0.249)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.279 (n=841)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.249)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.148 (n=891)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0042 (IC base=+0.065)

- **PATRÓN** `ibs_20min` > `0.7505` → IC=+0.192 (n=1711)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.7505 (IC base=+0.065)

- **PATRÓN** `dist_vwap_pct` > `0.1578` → IC=+0.151 (n=1220)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.1578 (IC base=+0.065)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.425` → IC=+0.145 (n=559)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 10.425 (IC base=+0.065)

- **PATRÓN** `ibs_20min` < `0.5913` → IC=+0.167 (n=1954)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.5913 (IC base=+0.083)

- **PATRÓN** `volumen_pendiente_norm` > `0.1501` → IC=+0.178 (n=544)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1501 (IC base=+0.083)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.5427` → IC=-0.122 (n=334)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5427
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=680)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.174 (n=265)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0029 (IC base=+0.068)

- **PATRÓN** `ibs_20min` > `0.5427` → IC=+0.161 (n=680)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.5427 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.1288` → IC=+0.167 (n=358)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1288 (IC base=+0.068)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.128 (n=318)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0037 (IC base=+0.053)

- **PATRÓN** `ibs_20min` < `0.0659` → IC=+0.248 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0659 (IC base=+0.053)

- **PATRÓN** `volumen_pendiente_norm` > `0.0703` → IC=+0.144 (n=301)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.0703 (IC base=+0.053)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.5208` → IC=-0.125 (n=254)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5208
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=495)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.156 (n=361)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0043 (IC base=+0.066)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.129 (n=316)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.066)

- **PATRÓN** `ibs_20min` > `0.5205` → IC=+0.161 (n=705)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.5205 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` > `0.135` → IC=+0.159 (n=379)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.135 (IC base=+0.066)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.791` → IC=+0.178 (n=172)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 11.791 (IC base=+0.066)

- **PATRÓN** `ibs_20min` < `0.1005` → IC=+0.280 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1005 (IC base=+0.040)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.7209` → IC=+0.144 (n=593)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.7209 (IC base=+0.033)

- **PATRÓN** `dist_vwap_pct` > `0.7566` → IC=+0.153 (n=214)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.7566 (IC base=+0.033)

- **PATRÓN** `sigma_h` < `0.0101` → IC=+0.171 (n=390)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0101 (IC base=+0.099)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.192 (n=557)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.5 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` < `0.2164` → IC=+0.150 (n=555)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.2164 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.09` → IC=+0.232 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.09 (IC base=+0.099)

- **PATRÓN** `volumen_regimen` > `1.1136` → IC=+0.190 (n=185)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 1.1136 (IC base=+0.099)

- **PATRÓN** `volumen_pendiente_norm` > `0.1605` → IC=+0.180 (n=145)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.1605 (IC base=+0.099)

- **PATRÓN** `volumen_spike_ratio` < `2.193` → IC=+0.130 (n=460)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 2.193 (IC base=+0.099)

- **PATRÓN** `volumen_spike_ratio` > `1.4591` → IC=+0.137 (n=522)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.4591 (IC base=+0.099)

### GBM_LATE_60M#XRP#60min
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.346 (n=37)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.307)

- **PATRÓN** `drift_60min` |x|≤ `0.2821` → IC=+0.309 (n=19)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2821 (IC base=+0.307)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.321 (n=37)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.307)

- **PATRÓN** `ibs_20min` > `0.6977` → IC=+0.372 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6977 (IC base=+0.307)

- **PATRÓN** `dist_vwap_pct` > `0.8732` → IC=+0.409 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8732 (IC base=+0.307)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.717` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.717 (IC base=+0.307)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.328` → IC=+0.306 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.328 (IC base=+0.307)

- **PATRÓN** `volumen_regimen` < `0.9488` → IC=+0.321 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9488 (IC base=+0.307)

- **PATRÓN** `volumen_regimen` > `0.6848` → IC=+0.321 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6848 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` < `0.0555` → IC=+0.361 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0555 (IC base=+0.307)

- **PATRÓN** `volumen_spike_ratio` > `2.1829` → IC=+0.362 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1829 (IC base=+0.307)

- **PATRÓN** `libro_spread` < `0.07` → IC=+0.309 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.07 (IC base=+0.307)

- **PATRÓN** `libro_liquidez` > `34.2` → IC=+0.300 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 34.2 (IC base=+0.307)

- **PATRÓN** `sigma_h` < `0.0126` → IC=+0.357 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0126 (IC base=+0.306)

- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.324 (n=49)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.306)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.372 (n=45)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.306)

- **PATRÓN** `ibs_20min` < `0.0274` → IC=+0.342 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0274 (IC base=+0.306)

- **PATRÓN** `ibs_20min` > `0.3556` → IC=+0.340 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3556 (IC base=+0.306)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.841` → IC=+0.444 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.841 (IC base=+0.306)

- **PATRÓN** `volumen_regimen` > `0.5773` → IC=+0.363 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5773 (IC base=+0.306)

- **PATRÓN** `volumen_pendiente_norm` > `0.0899` → IC=+0.413 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0899 (IC base=+0.306)

- **PATRÓN** `volumen_spike_ratio` < `1.6405` → IC=+0.353 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6405 (IC base=+0.306)

- **PATRÓN** `libro_liquidez` > `34.6896` → IC=+0.326 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 34.6896 (IC base=+0.306)

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

- **FILTRO** `sigma_h` < `0.0074` → IC=-0.281 (n=277)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0074
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=93)

- **FILTRO** `dist_vwap_pct` > `0.4617` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4617
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=340)

- **FILTRO** `sigma_ewma_delta_pct` > `9.308` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.308
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=340)

- **FILTRO** `volumen_pendiente_norm` > `0.046` → IC=-0.375 (n=30)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.046
  - _Potencial_: sin este filtro IC_bueno=-0.245 (n=245)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.312 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.232 (n=95)

- **FILTRO** `ibs_20min` < `0.0068` → IC=-0.288 (n=31)

  - _Acción_: SKIP cuando `ibs_20min` < 0.0068
  - _Potencial_: sin este filtro IC_bueno=-0.240 (n=94)

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
- **FILTRO** `sigma_h` < `0.0111` → IC=-0.288 (n=97)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0111
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=51)

- **FILTRO** `drift_60min` |x|> `0.2367` → IC=-0.368 (n=36)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2367
  - _Potencial_: sin este filtro IC_bueno=-0.208 (n=111)

- **FILTRO** `sigma_ewma_delta_pct` > `4.378` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.378
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=52)

- **FILTRO** `volumen_regimen` < `0.9188` → IC=-0.458 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9188
  - _Potencial_: sin este filtro IC_bueno=-0.104 (n=46)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=45)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.257 (n=381)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.209 (n=325)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `0.6842` → IC=+0.205 (n=832)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6842 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.8551` → IC=+0.328 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8551 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.408` → IC=+0.194 (n=194)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 10.408 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.35` → IC=+0.167 (n=845)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` < 8.35 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `0.6244` → IC=+0.192 (n=277)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.6244 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` < `0.2079` → IC=+0.186 (n=809)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.2079 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.415` → IC=+0.212 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.415 (IC base=+0.167)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.167 (n=79)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0066 (IC base=+0.063)

- **PATRÓN** `ibs_20min` > `0.7988` → IC=+0.153 (n=211)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.7988 (IC base=+0.063)

- **PATRÓN** `dist_vwap_pct` > `0.6628` → IC=+0.229 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6628 (IC base=+0.063)

- **PATRÓN** `ibs_20min` < `0.2542` → IC=+0.131 (n=437)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.2542 (IC base=+0.072)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.181 (n=89)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0072 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.1124` → IC=+0.139 (n=117)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.1124 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.177 (n=97)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 18.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.143 (n=96)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 6.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.7994` → IC=+0.188 (n=238)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.7994 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.8083` → IC=+0.211 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8083 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1088` → IC=+0.156 (n=216)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1088 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.217` → IC=+0.156 (n=274)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 9.217 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.6229` → IC=+0.192 (n=89)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.6229 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `1.1834` → IC=+0.170 (n=89)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 1.1834 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` < `0.1803` → IC=+0.156 (n=283)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.1803 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.7165` → IC=+0.189 (n=159)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.7165 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=223)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `1844.9641` → IC=+0.175 (n=238)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 1844.9641 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.332` → IC=+0.123 (n=104)

  - _Acción_: Kelly boost +0.61€ cuando `sigma_ewma_delta_pct` > 9.332 (IC base=-0.004)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `volumen_regimen` < `0.9506` → IC=-0.147 (n=114)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9506
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=114)

- **FILTRO** `volumen_spike_ratio` > `2.0313` → IC=-0.136 (n=64)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.0313
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=126)

- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.326 (n=107)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0119 (IC base=+0.267)

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
  - _Potencial_: sin este filtro IC_bueno=+0.327 (n=189)

- **PATRÓN** `drift_ventana_pct` |x|> `0.5446` → IC=+0.346 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.5446 (IC base=+0.334)

- **PATRÓN** `elapsed_s` > `208.3` → IC=+0.381 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 208.3 (IC base=+0.334)

- **PATRÓN** `drift_15min` |x|≤ `1.3457` → IC=+0.368 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.3457 (IC base=+0.334)

- **PATRÓN** `drift_60min` |x|≤ `1.0314` → IC=+0.360 (n=148)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 1.0314 (IC base=+0.334)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.388 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.334)

- **PATRÓN** `ballena_activa_n` < `1044.0` → IC=+0.423 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1044.0 (IC base=+0.334)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3492` → IC=+0.294 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3492 (IC base=+0.288)

- **PATRÓN** `elapsed_s` > `231.5` → IC=+0.389 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 231.5 (IC base=+0.288)

- **PATRÓN** `drift_15min` |x|≤ `2.354` → IC=+0.319 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.354 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.9433` → IC=+0.312 (n=136)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9433 (IC base=+0.288)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.327 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.288)

- **PATRÓN** `ballena_activa_n` < `1305.0` → IC=+0.377 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1305.0 (IC base=+0.288)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.327 (n=189)

- **PATRÓN** `drift_ventana_pct` |x|> `0.5446` → IC=+0.346 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.5446 (IC base=+0.334)

- **PATRÓN** `elapsed_s` > `208.3` → IC=+0.381 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 208.3 (IC base=+0.334)

- **PATRÓN** `drift_15min` |x|≤ `1.3457` → IC=+0.368 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.3457 (IC base=+0.334)

- **PATRÓN** `drift_60min` |x|≤ `1.0314` → IC=+0.360 (n=148)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 1.0314 (IC base=+0.334)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.388 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.334)

- **PATRÓN** `ballena_activa_n` < `1044.0` → IC=+0.423 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1044.0 (IC base=+0.334)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3492` → IC=+0.294 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3492 (IC base=+0.288)

- **PATRÓN** `elapsed_s` > `231.5` → IC=+0.389 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 231.5 (IC base=+0.288)

- **PATRÓN** `drift_15min` |x|≤ `2.354` → IC=+0.319 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.354 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.9433` → IC=+0.312 (n=136)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9433 (IC base=+0.288)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.327 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.288)

- **PATRÓN** `ballena_activa_n` < `1305.0` → IC=+0.377 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1305.0 (IC base=+0.288)

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
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=1429)

### LIQUIDACIONES_15M#BNB#15min
- **PATRÓN** `liq_n` > `2.0` → IC=+0.179 (n=79)

  - _Acción_: Kelly boost +0.90€ cuando `liq_n` > 2.0 (IC base=+0.084)

- **PATRÓN** `liq_usd_total` > `145.86` → IC=+0.128 (n=143)

  - _Acción_: Kelly boost +0.64€ cuando `liq_usd_total` > 145.86 (IC base=+0.084)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.195 (n=57)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 6.0 (IC base=+0.084)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.141 (n=76)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` > 0.5 (IC base=+0.084)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.141 (n=101)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.03 (IC base=+0.084)

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
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=279)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=4201)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=238)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=195)

- **FILTRO** `ballena_activa_n` > `68.0` → IC=-0.179 (n=76)

  - _Acción_: SKIP cuando `ballena_activa_n` > 68.0
  - _Potencial_: sin este filtro IC_bueno=+0.162 (n=149)

- **PATRÓN** `ballena_activa_n` < `68.0` → IC=+0.162 (n=149)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 68.0 (IC base=+0.010)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=22)

- **FILTRO** `libro_liquidez` < `13988.6712` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 13988.6712
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.137 (n=290)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.495 (IC base=+0.024)

### LIQUIDACIONES_5M#DOGE#5min
- **PATRÓN** `liq_n` > `3.0` → IC=+0.333 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 3.0 (IC base=+0.188)

- **PATRÓN** `liq_usd_total` > `996.91` → IC=+0.292 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 996.91 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.234 (n=77)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.188)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.196 (n=110)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.03 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `3279.111` → IC=+0.206 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3279.111 (IC base=+0.188)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.195 (n=93)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 12.0 (IC base=+0.188)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=1643)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=1597)

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
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=749)

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
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=1129)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=1129)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=1516)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=1516)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=351)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=351)

- **FILTRO** `py_entrada` < `0.43` → IC=-0.138 (n=114)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=252)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.136 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=406)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=455)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=331)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=432)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=432)

- **FILTRO** `libro_liquidez` < `693.7144` → IC=-0.130 (n=152)

  - _Acción_: SKIP cuando `libro_liquidez` < 693.7144
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=310)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=427)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.126 (n=3468)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=9039)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.152 (n=44)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=91)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.136 (n=116)
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
- **FILTRO** `py_entrada` < `0.4` → IC=-0.157 (n=415)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=1011)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.151 (n=330)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=896)

- **PATRÓN** `py_entrada` < `0.51` → IC=+0.146 (n=428)

  - _Acción_: Kelly boost +0.73€ cuando `py_entrada` < 0.51 (IC base=-0.007)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.136 (n=196)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=447)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.123 (n=327)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=661)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.121 (n=714)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=758)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.138 (n=354)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=755)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.125 (n=334)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=915)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.121 (n=570)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=602)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.129 (n=620)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=712)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.178 (n=9148)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=28516)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.171 (n=9508)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=29468)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.197 (n=1703)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=5322)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.145 (n=2333)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=4582)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.139 (n=1800)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 1.0 (IC base=+0.039)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.136 (n=3257)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.5 (IC base=+0.015)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.184 (n=1190)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=3963)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.176 (n=1339)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=4115)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.197 (n=1729)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.090 (n=5363)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.134 (n=2158)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 1.0 (IC base=+0.032)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `ibs_20min` < `0.7648` → IC=-0.150 (n=1259)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7648
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=3784)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.177 (n=1368)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=4187)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.162 (n=1739)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=5306)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=2452)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2376)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=973)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=3305)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=4257)

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

- **FILTRO** `libro_liquidez` < `2030.5765` → IC=-0.138 (n=409)

  - _Acción_: SKIP cuando `libro_liquidez` < 2030.5765
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=831)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.137 (n=25547)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=57817)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.302 (n=20324)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=63040)

- **FILTRO** `ibs_7min` < `0.7273` → IC=-0.225 (n=27419)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7273
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=55945)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.155 (n=27996)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=55368)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.247 (n=25836)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=78463)

- **FILTRO** `ibs_7min` > `0.2783` → IC=-0.183 (n=26066)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2783
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=78233)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.164 (n=3585)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=11443)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.327 (n=3552)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=11476)

- **FILTRO** `ibs_7min` < `0.7083` → IC=-0.256 (n=4955)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7083
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=10073)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.279 (n=4379)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=13680)

- **FILTRO** `ibs_7min` > `0.7677` → IC=-0.211 (n=4514)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7677
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=13545)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.267 (n=3374)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=10373)

- **FILTRO** `ibs_7min` < `0.711` → IC=-0.215 (n=3435)

  - _Acción_: SKIP cuando `ibs_7min` < 0.711
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=10312)

- **FILTRO** `ballena_activa_n` > `157.0` → IC=-0.205 (n=3429)

  - _Acción_: SKIP cuando `ballena_activa_n` > 157.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=10318)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.267 (n=3210)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=10875)

- **FILTRO** `ibs_7min` > `0.2642` → IC=-0.191 (n=3520)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2642
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=10565)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.178 (n=3515)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=10570)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.169 (n=3445)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=10967)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.329 (n=3443)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=10969)

- **FILTRO** `ibs_7min` < `0.2901` → IC=-0.256 (n=4755)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2901
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=9657)

- **FILTRO** `ballena_activa_n` > `4.0` → IC=-0.174 (n=3460)

  - _Acción_: SKIP cuando `ballena_activa_n` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=10952)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.262 (n=4568)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=14532)

- **FILTRO** `ibs_7min` > `0.7222` → IC=-0.186 (n=4765)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7222
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=14335)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.277 (n=3054)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=10379)

- **FILTRO** `ibs_7min` < `0.711` → IC=-0.203 (n=3356)

  - _Acción_: SKIP cuando `ibs_7min` < 0.711
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=10077)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.200 (n=3248)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=10185)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.259 (n=3250)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=10699)

- **FILTRO** `ibs_7min` > `0.2719` → IC=-0.179 (n=3487)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2719
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=10462)

- **FILTRO** `ballena_activa_n` > `23.0` → IC=-0.168 (n=3482)

  - _Acción_: SKIP cuando `ballena_activa_n` > 23.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=10467)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.303 (n=3234)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=10034)

- **FILTRO** `ibs_7min` < `0.2941` → IC=-0.235 (n=4363)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2941
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=8905)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.218 (n=3292)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=9976)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.202 (n=4781)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=15404)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.315 (n=3300)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=10176)

- **FILTRO** `ibs_7min` < `0.72` → IC=-0.232 (n=4428)

  - _Acción_: SKIP cuando `ibs_7min` < 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=9048)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.196 (n=3344)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=10132)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.231 (n=4614)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=14307)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=121)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.163 (n=304)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=1034)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=1323)

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
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=926)

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
- **PATRÓN** `delta_ratio` |x|> `0.4305` → IC=+0.144 (n=760)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio` |x|> 0.4305 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.131 (n=613)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 4.0 (IC base=+0.124)

- **PATRÓN** `total_vol_5m` < `451.687` → IC=+0.167 (n=557)

  - _Acción_: Kelly boost +0.84€ cuando `total_vol_5m` < 451.687 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `4199.3632` → IC=+0.132 (n=557)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 4199.3632 (IC base=+0.124)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.187 (n=193)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 14.0 (IC base=+0.143)

- **PATRÓN** `total_vol_5m` < `381.605` → IC=+0.166 (n=339)

  - _Acción_: Kelly boost +0.83€ cuando `total_vol_5m` < 381.605 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.159 (n=268)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 9.0 (IC base=+0.143)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3988` → IC=+0.131 (n=348)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio` |x|> 0.3988 (IC base=+0.116)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.155 (n=146)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 4.0 (IC base=+0.116)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.120 (n=427)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.04 (IC base=+0.116)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4161` → IC=+0.168 (n=206)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.84€ cuando `delta_ratio` |x|> 0.4161 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.154 (n=284)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 5.0 (IC base=+0.128)

- **PATRÓN** `total_vol_5m` < `877.8133` → IC=+0.157 (n=310)

  - _Acción_: Kelly boost +0.79€ cuando `total_vol_5m` < 877.8133 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.186 (n=103)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 58.0 (IC base=+0.128)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4317` → IC=+0.215 (n=128)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4317 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.153 (n=194)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 11.0 (IC base=+0.132)

- **PATRÓN** `total_vol_5m` < `4782.684` → IC=+0.181 (n=189)

  - _Acción_: Kelly boost +0.90€ cuando `total_vol_5m` < 4782.684 (IC base=+0.132)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `13.0` → IC=+0.130 (n=306)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 13.0 (IC base=+0.100)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.137 (n=213)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.100)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `6.3582` → IC=-0.218 (n=83)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 6.3582
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=163)

- **FILTRO** `pct_vs_K` |x|> `3.4121` → IC=-0.145 (n=336)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.4121
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=654)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.157 (n=327)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0047 (IC base=-0.026)

### PRICE_TARGET_GBM#ETH#atexpiry
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

### PRICE_TARGET_GBM#SOL#reach
- **FILTRO** `sigma_h` < `0.0164` → IC=-0.192 (n=24)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0164
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `T_h` < `113.7599` → IC=-0.251 (n=565)

  - _Acción_: SKIP cuando `T_h` < 113.7599
  - _Potencial_: sin este filtro IC_bueno=-0.228 (n=292)

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

- **FILTRO** `sigma_h` < `0.0076` → IC=-0.172 (n=196)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0076
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=101)

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

- **FILTRO** `sigma_h` < `0.0058` → IC=-0.161 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0058
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=182)

- **FILTRO** `T_h` > `57.2148` → IC=-0.134 (n=162)

  - _Acción_: SKIP cuando `T_h` > 57.2148
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=80)

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
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=479)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=517)

- **PATRÓN** `streak_estiramiento` < `0.3762` → IC=+0.127 (n=159)

  - _Acción_: Kelly boost +0.64€ cuando `streak_estiramiento` < 0.3762 (IC base=+0.018)

- **PATRÓN** `streak_estiramiento` < `0.835` → IC=+0.125 (n=358)

  - _Acción_: Kelly boost +0.62€ cuando `streak_estiramiento` < 0.835 (IC base=+0.059)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.124 (n=269)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 29.0 (IC base=+0.059)

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
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=220)

- **PATRÓN** `streak_estiramiento` < `0.2119` → IC=+0.151 (n=61)

  - _Acción_: Kelly boost +0.75€ cuando `streak_estiramiento` < 0.2119 (IC base=+0.034)

- **PATRÓN** `streak_estiramiento` < `0.5992` → IC=+0.159 (n=180)

  - _Acción_: Kelly boost +0.80€ cuando `streak_estiramiento` < 0.5992 (IC base=+0.085)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.153 (n=171)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 30.0 (IC base=+0.085)

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
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1351)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1244)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=1332)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=5477)

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
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=3294)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.185 (n=2140)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0058 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.2323` → IC=+0.158 (n=6421)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2323 (IC base=+0.133)

- **PATRÓN** `drift_15min` |x|≤ `1.1206` → IC=+0.135 (n=6420)

  - _Acción_: Kelly boost +0.67€ cuando `drift_15min` |x|≤ 1.1206 (IC base=+0.133)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0645` → IC=+0.133 (n=6421)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio_macro` |x|> 0.0645 (IC base=+0.133)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1332` → IC=+0.142 (n=2666)

  - _Acción_: Kelly boost +0.71€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1332 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.145 (n=5932)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 6.0 (IC base=+0.133)

- **PATRÓN** `ibs_15` > `0.5556` → IC=+0.209 (n=5745)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5556 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.079` → IC=+0.233 (n=1198)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.079 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=3392)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `4323.0441` → IC=+0.171 (n=2140)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 4323.0441 (IC base=+0.133)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=2469)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.253 (n=290)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.0772` → IC=+0.246 (n=384)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0772 (IC base=+0.205)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2676` → IC=+0.226 (n=290)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2676 (IC base=+0.205)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2264` → IC=+0.217 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2264 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.230 (n=803)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.205)

- **PATRÓN** `ibs_15` > `0.7046` → IC=+0.275 (n=869)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7046 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `0.3926` → IC=+0.224 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3926 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` < `0.5461` → IC=+0.209 (n=979)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5461 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.088` → IC=+0.300 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.088 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.209 (n=1127)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `11847.0948` → IC=+0.225 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11847.0948 (IC base=+0.205)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.147 (n=985)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0067 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.109` → IC=+0.147 (n=746)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.109 (IC base=+0.133)

- **PATRÓN** `delta_ratio_macro` |x|> `0.084` → IC=+0.136 (n=999)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio_macro` |x|> 0.084 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.145 (n=789)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 11.0 (IC base=+0.133)

- **PATRÓN** `ibs_15` > `0.4837` → IC=+0.218 (n=1119)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.4837 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `0.1236` → IC=+0.144 (n=701)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.1236 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.6543` → IC=+0.136 (n=1271)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.6543 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.04` → IC=+0.288 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.04 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `6107.0908` → IC=+0.172 (n=507)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 6107.0908 (IC base=+0.133)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.8387` → IC=+0.147 (n=659)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.74€ cuando `ibs_15` > 0.8387 (IC base=+0.046)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` < `0.0139` → IC=+0.145 (n=717)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0139 (IC base=+0.139)

- **PATRÓN** `sigma_h` > `0.012` → IC=+0.144 (n=1628)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.012 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.2386` → IC=+0.175 (n=1628)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2386 (IC base=+0.139)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0581` → IC=+0.142 (n=1628)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.71€ cuando `delta_ratio_macro` |x|> 0.0581 (IC base=+0.139)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0926` → IC=+0.188 (n=508)

  - _Acción_: Kelly boost +0.94€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0926 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.146 (n=1486)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 6.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.140 (n=1505)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 15.0 (IC base=+0.139)

- **PATRÓN** `ibs_15` > `0.7` → IC=+0.235 (n=1086)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.2134` → IC=+0.152 (n=737)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.2134 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.9103` → IC=+0.142 (n=1881)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.9103 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.103` → IC=+0.186 (n=374)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 17.103 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `2944.8548` → IC=+0.182 (n=738)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2944.8548 (IC base=+0.139)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `drift_60min` |x|≤ `0.1103` → IC=+0.364 (n=534)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1103 (IC base=+0.363)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1464` → IC=+0.377 (n=533)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1464 (IC base=+0.363)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.107` → IC=+0.379 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.107 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.371 (n=845)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.363)

- **PATRÓN** `ibs_15` > `0.7904` → IC=+0.395 (n=801)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7904 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` > `0.4165` → IC=+0.380 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4165 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` < `0.5497` → IC=+0.363 (n=902)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5497 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.787` → IC=+0.396 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.787 (IC base=+0.363)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.366 (n=976)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.363)

- **PATRÓN** `libro_liquidez` > `9610.6074` → IC=+0.380 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9610.6074 (IC base=+0.363)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.365 (n=168)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.363)

- **PATRÓN** `drift_60min` |x|≤ `0.1519` → IC=+0.364 (n=336)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1519 (IC base=+0.363)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2194` → IC=+0.374 (n=173)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2194 (IC base=+0.363)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1476` → IC=+0.396 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1476 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.379 (n=353)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.363)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.362 (n=389)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.363)

- **PATRÓN** `ibs_15` > `0.8112` → IC=+0.383 (n=381)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8112 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` > `0.2502` → IC=+0.386 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2502 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.995` → IC=+0.381 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.995 (IC base=+0.363)

- **PATRÓN** `libro_liquidez` > `15195.4571` → IC=+0.386 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15195.4571 (IC base=+0.363)

- **PATRÓN** `ballena_activa_n` < `412.0` → IC=+0.384 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 412.0 (IC base=+0.363)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.363 (n=420)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.363)

- **PATRÓN** `drift_60min` |x|≤ `0.1062` → IC=+0.365 (n=280)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1062 (IC base=+0.363)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1264` → IC=+0.376 (n=280)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1264 (IC base=+0.363)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.370 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.371 (n=448)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.363)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.374 (n=197)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.363)

- **PATRÓN** `ibs_15` > `0.764` → IC=+0.398 (n=420)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.764 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` > `0.4542` → IC=+0.368 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4542 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` < `0.6628` → IC=+0.365 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6628 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.861` → IC=+0.399 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.861 (IC base=+0.363)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.365 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.363)

- **PATRÓN** `libro_liquidez` > `4306.4715` → IC=+0.376 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4306.4715 (IC base=+0.363)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=2650)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=3360)

- **FILTRO** `libro_liquidez` < `4371.3768` → IC=-0.172 (n=3966)

  - _Acción_: SKIP cuando `libro_liquidez` < 4371.3768
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=2044)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1411` → IC=+0.215 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1411 (IC base=-0.089)

- **PATRÓN** `ibs_15` > `0.6296` → IC=+0.278 (n=1321)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6296 (IC base=-0.089)

- **PATRÓN** `dist_vwap_pct` > `0.1154` → IC=+0.205 (n=779)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1154 (IC base=-0.089)

- **PATRÓN** `dist_vwap_pct` < `0.5908` → IC=+0.199 (n=1403)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.5908 (IC base=-0.089)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2289` → IC=+0.270 (n=1957)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2289 (IC base=+0.002)

- **PATRÓN** `ibs_15` < `0.3738` → IC=+0.283 (n=5872)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3738 (IC base=+0.002)

- **PATRÓN** `dist_vwap_pct` > `0.7074` → IC=+0.267 (n=834)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7074 (IC base=+0.002)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0739` → IC=-0.241 (n=1962)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0739
  - _Potencial_: sin este filtro IC_bueno=-0.122 (n=1965)

- **FILTRO** `sigma_h` < `0.004` → IC=-0.210 (n=981)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.004
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=2946)

- **FILTRO** `sigma_ewma_delta_pct` > `22.22` → IC=-0.243 (n=555)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.22
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=3372)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.145 (n=361)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0032 (IC base=+0.064)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2678` → IC=+0.274 (n=157)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2678 (IC base=+0.064)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.145` → IC=+0.279 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.145 (IC base=+0.064)

- **PATRÓN** `ibs_15` > `0.7593` → IC=+0.318 (n=471)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7593 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` > `0.1047` → IC=+0.282 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1047 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` < `0.5257` → IC=+0.284 (n=527)

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
  - _Potencial_: sin este filtro IC_bueno=+0.153 (n=871)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.161 (n=667)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0066 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.0718` → IC=+0.176 (n=294)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.0718 (IC base=+0.147)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3015` → IC=+0.189 (n=526)

  - _Acción_: Kelly boost +0.95€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3015 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.170 (n=477)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 11.0 (IC base=+0.147)

- **PATRÓN** `ibs_15` > `0.5659` → IC=+0.242 (n=666)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5659 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.1198` → IC=+0.156 (n=417)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1198 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.1598` → IC=+0.147 (n=511)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1598 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.851` → IC=+0.268 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.851 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=871)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `5193.6092` → IC=+0.164 (n=444)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 5193.6092 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.258 (n=1004)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.4785` → IC=+0.242 (n=2281)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4785 (IC base=+0.237)

- **PATRÓN** `drift_15min` |x|≤ `0.8201` → IC=+0.250 (n=2008)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.8201 (IC base=+0.237)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2015` → IC=+0.257 (n=1034)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2015 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.246 (n=841)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.241 (n=1012)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.237)

- **PATRÓN** `ibs_15` < `0.3875` → IC=+0.270 (n=2281)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3875 (IC base=+0.237)

- **PATRÓN** `dist_vwap_pct` > `0.2373` → IC=+0.254 (n=773)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2373 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.542` → IC=+0.245 (n=988)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.542 (IC base=+0.237)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.2012` → IC=-0.295 (n=359)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.2012
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=1084)

- **FILTRO** `drift_60min` |x|> `0.1729` → IC=-0.285 (n=490)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1729
  - _Potencial_: sin este filtro IC_bueno=-0.164 (n=953)

- **FILTRO** `drift_15min` |x|> `1.0097` → IC=-0.307 (n=360)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.0097
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=1083)

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

- **PATRÓN** `ibs_15` < `0.3793` → IC=+0.298 (n=982)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3793 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` < `0.4676` → IC=+0.251 (n=1056)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4676 (IC base=-0.026)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1214` → IC=-0.271 (n=845)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1214
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=849)

- **FILTRO** `sigma_h` > `0.0145` → IC=-0.252 (n=1134)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0145
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=560)

- **FILTRO** `drift_15min` |x|> `1.3087` → IC=-0.283 (n=423)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.3087
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=1271)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=1673)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.222)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.222)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0705` → IC=+0.284 (n=1228)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0705 (IC base=-0.009)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1182` → IC=+0.290 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1182 (IC base=-0.009)

- **PATRÓN** `ibs_15` < `0.1429` → IC=+0.307 (n=925)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1429 (IC base=-0.009)

- **PATRÓN** `dist_vwap_pct` > `0.7922` → IC=+0.324 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7922 (IC base=-0.009)

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
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.302 (n=492)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.293 (n=491)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0066 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.0531` → IC=+0.312 (n=492)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0531 (IC base=+0.284)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0682` → IC=+0.284 (n=1473)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0682 (IC base=+0.284)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2191` → IC=+0.289 (n=904)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2191 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.295 (n=1531)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.284)

- **PATRÓN** `ibs_15` > `0.8368` → IC=+0.311 (n=1474)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8368 (IC base=+0.284)

- **PATRÓN** `dist_vwap_pct` > `0.2746` → IC=+0.314 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2746 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.707` → IC=+0.385 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.707 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `13081.1746` → IC=+0.301 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13081.1746 (IC base=+0.284)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.308 (n=258)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.278)

- **PATRÓN** `drift_60min` |x|≤ `0.0763` → IC=+0.301 (n=340)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0763 (IC base=+0.278)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3894` → IC=+0.285 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3894 (IC base=+0.278)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.294 (n=813)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.278)

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
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.297 (n=309)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.0504` → IC=+0.323 (n=235)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0504 (IC base=+0.289)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0644` → IC=+0.292 (n=701)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0644 (IC base=+0.289)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1009` → IC=+0.310 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1009 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.298 (n=673)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.8447` → IC=+0.315 (n=701)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8447 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.2913` → IC=+0.312 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2913 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.001` → IC=+0.380 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.001 (IC base=+0.289)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5556 sube el IC de +0.133 a +0.209 en UPDOWN_GBM#15min (n=5745). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7046 sube el IC de +0.205 a +0.275 en UPDOWN_GBM#BTC#15min (n=869). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.4837 sube el IC de +0.133 a +0.218 en UPDOWN_GBM#ETH#15min (n=1119). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.7 sube el IC de +0.139 a +0.235 en UPDOWN_GBM#XRP#15min (n=1086). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6296 sube el IC de -0.089 a +0.278 en UPDOWN_GBM_15M_TARDIO (n=1321). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3738 sube el IC de +0.002 a +0.283 en UPDOWN_GBM_15M_TARDIO (n=5872). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7593 sube el IC de +0.064 a +0.318 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=471). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6255 sube el IC de -0.181 a +0.290 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=79). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5659 sube el IC de +0.147 a +0.242 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=666). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3875 sube el IC de +0.237 a +0.270 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=2281). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.9231 sube el IC de -0.205 a +0.380 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3793 sube el IC de -0.026 a +0.298 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=982). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.222 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.1429 sube el IC de -0.009 a +0.307 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=925). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8357 sube el IC de +0.088 a +0.306 en UPDOWN_GBM_ETH_15M_HORA7 (n=29). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8357 sube el IC de +0.088 a +0.306 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=29). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8368 sube el IC de +0.284 a +0.311 en UPDOWN_GBM_IBS_ALTO (n=1474). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.827 sube el IC de +0.278 a +0.301 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=773). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8447 sube el IC de +0.289 a +0.315 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=701). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7904 sube el IC de +0.363 a +0.395 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=801). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8112 sube el IC de +0.363 a +0.383 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=381). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.764 sube el IC de +0.363 a +0.398 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=420). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2311 | +0.083 | +243.71€ | 1 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2311 | +0.083 | +243.71€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1899 | +0.084 | +204.22€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1899 | +0.084 | +204.22€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 285 | +0.068 | +10.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 285 | +0.068 | +10.79€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 96 | +0.122 | +29.03€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 96 | +0.122 | +29.03€ | 0 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 1426 | -0.028 | +65.90€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 1426 | -0.028 | +65.90€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 1103 | -0.040 | +54.09€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 1103 | -0.040 | +54.09€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 224 | +0.035 | +20.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 224 | +0.035 | +20.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 92 | -0.043 | -11.49€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 92 | -0.043 | -11.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 51128 | -0.088 | -6592.09€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 3322 | +0.093 | -319.46€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 47806 | -0.100 | -6272.63€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 5088 | -0.116 | -816.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 5088 | -0.116 | -816.49€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 3322 | +0.093 | -319.46€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 3322 | +0.093 | -319.46€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 5091 | -0.108 | -951.84€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 5091 | -0.108 | -951.84€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 14147 | -0.045 | -1355.17€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 14147 | -0.045 | -1355.17€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 14079 | -0.122 | -1619.20€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 14079 | -0.122 | -1619.20€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 9401 | -0.138 | -1529.93€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 9401 | -0.138 | -1529.93€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 55815 | -0.012 | +2723.49€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 14384 | +0.003 | +1476.06€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 41431 | -0.017 | +1247.43€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 55815 | -0.012 | +2723.49€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 14384 | +0.003 | +1476.06€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 41431 | -0.017 | +1247.43€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 208697 | +0.113 | -8412.86€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 23134 | +0.179 | -762.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 973 | +0.019 | -76.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 172752 | +0.106 | -7148.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 11838 | +0.095 | -424.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 28633 | +0.102 | -2016.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 84 | -0.186 | +11.85€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 28525 | +0.103 | -2025.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#60min | 9 | +0.061 | +9.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 39138 | +0.123 | -608.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5692 | +0.177 | -230.10€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 28596 | +0.120 | -181.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4808 | +0.082 | -174.32€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 28680 | +0.099 | -1986.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 97 | -0.116 | +14.79€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 28562 | +0.100 | -1989.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#60min | 6 | -0.037 | +0.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 44656 | +0.123 | -930.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 11132 | +0.177 | -320.36€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 29055 | +0.106 | -526.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 4457 | +0.103 | -74.86€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 38933 | +0.111 | -1669.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 6031 | +0.199 | -253.15€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 876 | +0.043 | -22.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 29471 | +0.096 | -1205.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2555 | +0.106 | -188.22€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO#XRP | 28657 | +0.107 | -1203.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 98 | -0.130 | +14.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 28543 | +0.108 | -1219.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 33955 | +0.189 | -2522.92€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 33955 | +0.189 | -2522.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 7692 | +0.162 | -896.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 7692 | +0.162 | -896.60€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 5080 | +0.193 | -220.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 5080 | +0.193 | -220.24€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 7513 | +0.172 | -690.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 7513 | +0.172 | -690.48€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 6226 | +0.252 | -218.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 6226 | +0.252 | -218.03€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 7365 | +0.184 | -511.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 7365 | +0.184 | -511.34€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1319 | +0.424 | -52.29€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1319 | +0.424 | -52.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 560 | +0.438 | -6.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 560 | +0.438 | -6.84€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 528 | +0.421 | -23.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 528 | +0.421 | -23.69€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 217 | +0.400 | -17.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 217 | +0.400 | -17.90€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 120019 | +0.200 | -8688.13€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 120019 | +0.200 | -8688.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 20804 | +0.176 | -2436.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 20804 | +0.176 | -2436.05€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 19350 | +0.223 | -647.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 19350 | +0.223 | -647.38€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 20580 | +0.181 | -2137.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 20580 | +0.181 | -2137.45€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 19514 | +0.217 | -767.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 19514 | +0.217 | -767.44€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 19804 | +0.206 | -1160.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 19804 | +0.206 | -1160.63€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 19967 | +0.198 | -1539.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 19967 | +0.198 | -1539.18€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 46661 | +0.116 | +371.67€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 46661 | +0.116 | +371.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 23236 | +0.117 | +246.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 23236 | +0.117 | +246.13€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 23425 | +0.116 | +125.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 23425 | +0.116 | +125.54€ | 0 | 3 |
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
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 2037 | +0.065 | -102.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1312 | +0.075 | -37.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1603 | +0.071 | -56.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1312 | +0.075 | -37.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 95246 | +0.101 | -1992.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 7725 | +0.098 | +189.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 87521 | +0.101 | -2181.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 51998 | +0.105 | -430.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 7725 | +0.098 | +189.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 44273 | +0.107 | -619.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 20454 | +0.110 | -51.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 20454 | +0.110 | -51.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 22794 | +0.083 | -1509.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 22794 | +0.083 | -1509.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 914 | +0.186 | -109.27€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 914 | +0.186 | -109.27€ | 2 | 4 |
| ✅ GBM_LATE_15M | 64875 | +0.102 | +36537.18€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 64875 | +0.102 | +36537.18€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 10763 | +0.225 | +9260.15€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 10763 | +0.225 | +9260.15€ | 0 | 20 |
| ✅ GBM_LATE_15M#BTC | 10133 | +0.177 | +8167.30€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 10133 | +0.177 | +8167.30€ | 0 | 24 |
| ✅ GBM_LATE_15M#DOGE | 11604 | +0.207 | +9170.29€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 11604 | +0.207 | +9170.29€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 8584 | +0.062 | +2912.63€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 8584 | +0.062 | +2912.63€ | 1 | 17 |
| ✅ GBM_LATE_15M#SOL | 8983 | -0.026 | +2300.25€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 8983 | -0.026 | +2300.25€ | 4 | 17 |
| ✅ GBM_LATE_15M#XRP | 14808 | -0.019 | +4726.56€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 14808 | -0.019 | +4726.56€ | 3 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 68840 | +0.088 | +40231.27€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 68840 | +0.088 | +40231.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 13353 | -0.002 | +6972.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 13353 | -0.002 | +6972.23€ | 3 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 14806 | +0.007 | +4104.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 14806 | +0.007 | +4104.83€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 9246 | +0.296 | +10610.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 9246 | +0.296 | +10610.33€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 13150 | +0.018 | +4212.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 13150 | +0.018 | +4212.98€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 10478 | +0.049 | +4823.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 10478 | +0.049 | +4823.15€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 7807 | +0.314 | +9507.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 7807 | +0.314 | +9507.76€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 51066 | +0.179 | +42507.46€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 51066 | +0.179 | +42507.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 7722 | +0.240 | +7196.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 7722 | +0.240 | +7196.93€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 8130 | +0.141 | +6114.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 8130 | +0.141 | +6114.93€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 8224 | +0.224 | +7145.45€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 8224 | +0.224 | +7145.45€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 8737 | +0.130 | +6831.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 8737 | +0.130 | +6831.39€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 9634 | +0.123 | +7444.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 9634 | +0.123 | +7444.27€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 8619 | +0.232 | +7774.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 8619 | +0.232 | +7774.50€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 14044 | +0.127 | +7230.37€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 14044 | +0.127 | +7230.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 677 | +0.163 | +447.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 677 | +0.163 | +447.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3609 | +0.126 | +1970.45€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3609 | +0.126 | +1970.45€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 509 | +0.156 | +286.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 509 | +0.156 | +286.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 4121 | +0.128 | +2105.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 4121 | +0.128 | +2105.26€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 3867 | +0.104 | +1623.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 3867 | +0.104 | +1623.93€ | 0 | 12 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1261 | +0.168 | +796.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1261 | +0.168 | +796.67€ | 0 | 30 |
| ✅ GBM_LATE_15M_TARDIO | 65114 | +0.190 | +54298.96€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#15min | 65114 | +0.190 | +54298.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 10294 | +0.250 | +9932.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 10294 | +0.250 | +9932.34€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 10461 | +0.142 | +7581.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 10461 | +0.142 | +7581.08€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 11039 | +0.234 | +9960.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 11039 | +0.234 | +9960.17€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 10771 | +0.145 | +8134.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 10771 | +0.145 | +8134.41€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 11471 | +0.129 | +8399.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 11471 | +0.129 | +8399.01€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 11078 | +0.241 | +10291.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 11078 | +0.241 | +10291.95€ | 0 | 21 |
| ✅ GBM_LATE_5M | 16673 | +0.219 | +14070.12€ | 0 | 28 |
| ✅ GBM_LATE_5M#5min | 16673 | +0.219 | +14070.12€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1947 | +0.253 | +1897.59€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1947 | +0.253 | +1897.59€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3320 | +0.210 | +2854.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3320 | +0.210 | +2854.76€ | 0 | 27 |
| ✅ GBM_LATE_5M#DOGE | 1524 | +0.214 | +1243.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1524 | +0.214 | +1243.40€ | 0 | 18 |
| ✅ GBM_LATE_5M#ETH | 4795 | +0.210 | +3768.96€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 4795 | +0.210 | +3768.96€ | 0 | 28 |
| ✅ GBM_LATE_5M#SOL | 2973 | +0.229 | +2643.33€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2973 | +0.229 | +2643.33€ | 0 | 25 |
| ✅ GBM_LATE_5M#XRP | 2114 | +0.209 | +1662.07€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 2114 | +0.209 | +1662.07€ | 0 | 0 |
| ✅ GBM_LATE_60M | 6250 | +0.072 | +1990.51€ | 0 | 6 |
| ✅ GBM_LATE_60M#60min | 6250 | +0.072 | +1990.51€ | 0 | 0 |
| ✅ GBM_LATE_60M#BNB | 123 | +0.260 | +122.55€ | 0 | 0 |
| ✅ GBM_LATE_60M#BNB#60min | 123 | +0.260 | +122.55€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 2013 | +0.061 | +587.98€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 2013 | +0.061 | +587.98€ | 1 | 6 |
| ✅ GBM_LATE_60M#DOGE | 120 | +0.320 | +144.27€ | 0 | 0 |
| ✅ GBM_LATE_60M#DOGE#60min | 120 | +0.320 | +144.27€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH | 1870 | +0.055 | +593.23€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1870 | +0.055 | +593.23€ | 1 | 6 |
| ✅ GBM_LATE_60M#SOL | 2004 | +0.059 | +407.02€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 2004 | +0.059 | +407.02€ | 0 | 10 |
| ✅ GBM_LATE_60M#XRP | 120 | +0.311 | +135.45€ | 0 | 0 |
| ✅ GBM_LATE_60M#XRP#60min | 120 | +0.311 | +135.45€ | 0 | 23 |
| 🚫 GBM_LATE_60M_FADE | 781 | -0.246 | -33.28€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 781 | -0.246 | -33.28€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#BNB | 6 | +0.037 | +3.77€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#BNB#60min | 6 | +0.037 | +3.77€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 275 | -0.255 | -19.44€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 275 | -0.255 | -19.44€ | 4 | 0 |
| ✅ GBM_LATE_60M_FADE#DOGE | 6 | -0.037 | +0.48€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#DOGE#60min | 6 | -0.037 | +0.48€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 274 | -0.243 | -7.28€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 274 | -0.243 | -7.28€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 216 | -0.248 | -9.83€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 216 | -0.248 | -9.83€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 2389 | +0.088 | +596.14€ | 0 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 2389 | +0.088 | +596.14€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 896 | +0.069 | +205.67€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 896 | +0.069 | +205.67€ | 0 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#DOGE | 6 | +0.000 | +0.38€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#DOGE#60min | 6 | +0.000 | +0.38€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 816 | +0.058 | +151.29€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 816 | +0.058 | +151.29€ | 0 | 15 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 655 | +0.150 | +235.73€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 655 | +0.150 | +235.73€ | 2 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#XRP | 16 | +0.089 | +3.06€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#XRP#60min | 16 | +0.089 | +3.06€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN | 403 | +0.312 | +491.46€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 403 | +0.312 | +491.46€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 403 | +0.312 | +491.46€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 403 | +0.312 | +491.46€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 4857 | +0.095 | +1059.07€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4857 | +0.095 | +1059.07€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4857 | +0.095 | +1059.07€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4857 | +0.095 | +1059.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M | 1754 | +0.019 | +98.52€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 1754 | +0.019 | +98.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 213 | +0.081 | +37.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 213 | +0.081 | +37.93€ | 0 | 5 |
| ✅ LIQUIDACIONES_15M#BTC | 340 | -0.006 | +9.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 340 | -0.006 | +9.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 122 | +0.048 | +23.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 122 | +0.048 | +23.07€ | 2 | 2 |
| ✅ LIQUIDACIONES_15M#ETH | 397 | +0.026 | +22.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 397 | +0.026 | +22.30€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 353 | -0.018 | +1.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 353 | -0.018 | +1.29€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 329 | +0.023 | +4.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 329 | +0.023 | +4.20€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4545 | +0.018 | +192.13€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#5min | 4545 | +0.018 | +192.13€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 241 | +0.002 | -6.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 241 | +0.002 | -6.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 862 | +0.016 | +50.17€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 862 | +0.016 | +50.17€ | 2 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 336 | +0.065 | +83.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 336 | +0.065 | +83.95€ | 0 | 6 |
| ✅ LIQUIDACIONES_5M#ETH | 1695 | +0.021 | +33.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1695 | +0.021 | +33.28€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 790 | +0.015 | +6.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 790 | +0.015 | +6.09€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 621 | -0.006 | +24.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 621 | -0.006 | +24.80€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2740 | -0.034 | -6.74€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2740 | -0.034 | -6.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 836 | -0.036 | -15.48€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 836 | -0.036 | -15.48€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 985 | -0.016 | +17.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 985 | -0.016 | +17.42€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 904 | -0.053 | -9.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 904 | -0.053 | -9.33€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#XRP | 10 | +0.042 | +1.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#XRP#60min | 10 | +0.042 | +1.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 20548 | -0.031 | -165.41€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 9943 | -0.033 | -126.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 10605 | -0.029 | -38.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 733 | -0.051 | -37.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 369 | -0.039 | -7.99€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 364 | -0.063 | -29.53€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 5529 | -0.026 | -28.44€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 2627 | -0.024 | +1.04€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 2902 | -0.028 | -29.49€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1878 | -0.032 | -3.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 961 | -0.043 | -29.34€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 917 | -0.021 | +25.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 4697 | -0.032 | -56.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 2265 | -0.030 | -17.80€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 2432 | -0.034 | -38.91€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 3923 | -0.023 | +52.03€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1910 | -0.029 | -3.34€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 2013 | -0.017 | +55.37€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 3788 | -0.041 | -90.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1811 | -0.048 | -69.38€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1977 | -0.035 | -21.57€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 76640 | -0.000 | +4170.25€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 76640 | -0.000 | +4170.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 13940 | +0.027 | +1940.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 13940 | +0.027 | +1940.47€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 10607 | -0.038 | -135.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 10607 | -0.038 | -135.20€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 14092 | +0.026 | +1571.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 14092 | +0.026 | +1571.78€ | 1 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 10598 | -0.053 | -273.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 10598 | -0.053 | -273.21€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 13070 | -0.004 | +366.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 13070 | -0.004 | +366.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 14333 | +0.019 | +699.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 14333 | +0.019 | +699.76€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7427 | -0.052 | -105.55€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7427 | -0.052 | -105.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1270 | -0.002 | -14.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1270 | -0.002 | -14.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 2119 | -0.057 | -16.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 2119 | -0.057 | -16.44€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 102 | -0.019 | -0.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 102 | -0.019 | -0.22€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 819 | -0.116 | -32.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 819 | -0.116 | -32.98€ | 6 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2247 | -0.067 | -12.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2247 | -0.067 | -12.69€ | 2 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 187663 | -0.077 | +2223.82€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 187663 | -0.077 | +2223.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 33087 | -0.076 | +1931.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 33087 | -0.076 | +1931.07€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 27832 | -0.102 | -1376.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 27832 | -0.102 | -1376.45€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 33512 | -0.067 | +1608.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 33512 | -0.067 | +1608.21€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 27382 | -0.100 | -956.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 27382 | -0.100 | -956.60€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 33453 | -0.059 | +198.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 33453 | -0.059 | +198.38€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 32397 | -0.069 | +819.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 32397 | -0.069 | +819.21€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9349 | -0.036 | -189.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9349 | -0.036 | -189.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1012 | -0.017 | -19.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1012 | -0.017 | -19.26€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2191 | -0.046 | -27.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2191 | -0.046 | -27.95€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2677 | -0.024 | -32.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2677 | -0.024 | -32.43€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1298 | -0.064 | -32.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1298 | -0.064 | -32.37€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1162 | -0.040 | -45.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1162 | -0.040 | -45.84€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 2362 | +0.121 | +951.11€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 2226 | +0.124 | +938.52€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 513 | +0.143 | +268.50€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 513 | +0.143 | +268.50€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#DOGE | 464 | +0.116 | +161.10€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 464 | +0.116 | +161.10€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#ETH | 412 | +0.128 | +189.99€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 412 | +0.128 | +189.99€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 376 | +0.132 | +180.20€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 376 | +0.132 | +180.20€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 461 | +0.100 | +138.72€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 461 | +0.100 | +138.72€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 2502 | -0.022 | -45.53€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2502 | -0.022 | -45.53€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 445 | +0.008 | +22.68€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 445 | +0.008 | +22.68€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 458 | -0.048 | -30.02€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 458 | -0.048 | -30.02€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 608 | -0.044 | -42.06€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 608 | -0.044 | -42.06€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 521 | -0.005 | -1.96€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 521 | -0.005 | -1.96€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 470 | -0.015 | +5.84€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 470 | -0.015 | +5.84€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1303 | -0.041 | +136.66€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 601 | -0.066 | +27.55€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 472 | -0.061 | +51.30€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 129 | -0.080 | -23.75€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 458 | -0.011 | +72.15€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 337 | +0.010 | +80.90€ | 0 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 121 | -0.069 | -8.75€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 244 | -0.037 | +36.97€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 208 | -0.029 | +35.13€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 36 | -0.079 | +1.84€ | 1 | 0 |
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
| ✅ STREAK_FADE_15M | 1034 | +0.040 | +83.69€ | 2 | 3 |
| ✅ STREAK_FADE_15M#15min | 1034 | +0.040 | +83.69€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 359 | +0.015 | +2.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 359 | +0.015 | +2.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 80 | +0.024 | +1.80€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 80 | +0.024 | +1.80€ | 1 | 1 |
| ✅ STREAK_FADE_15M#SOL | 85 | +0.029 | +7.61€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 85 | +0.029 | +7.61€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 510 | +0.060 | +71.95€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 510 | +0.060 | +71.95€ | 1 | 3 |
| ✅ STREAK_FADE_5M | 3648 | -0.023 | -142.48€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3648 | -0.023 | -142.48€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 626 | -0.030 | -28.54€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 626 | -0.030 | -28.54€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 177 | -0.048 | -15.80€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 177 | -0.048 | -15.80€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1718 | -0.017 | -57.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1718 | -0.017 | -57.94€ | 1 | 0 |
| ✅ STREAK_FADE_60M | 140 | -0.014 | -7.05€ | 0 | 1 |
| ✅ STREAK_FADE_60M#60min | 140 | -0.014 | -7.05€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 48 | -0.040 | -2.81€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 48 | -0.040 | -2.81€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 84 | +0.000 | -5.54€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 84 | +0.000 | -5.54€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 11677 | +0.013 | +61.66€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11677 | +0.013 | +61.66€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 3007 | +0.017 | +21.32€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 3007 | +0.017 | +21.32€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 3111 | +0.013 | +24.45€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 3111 | +0.013 | +24.45€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2941 | +0.008 | -2.95€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2941 | +0.008 | -2.95€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2618 | +0.014 | +18.84€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2618 | +0.014 | +18.84€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 13659 | +0.019 | +7.17€ | 4 | 0 |
| ✅ STRUCT_NO_15M#15min | 13659 | +0.019 | +7.17€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 5496 | +0.021 | +4.85€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 5496 | +0.021 | +4.85€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 4835 | +0.019 | +3.97€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 4835 | +0.019 | +3.97€ | 4 | 0 |
| ✅ STRUCT_NO_15M#SOL | 3328 | +0.015 | -1.66€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 3328 | +0.015 | -1.66€ | 1 | 0 |
| ✅ UPDOWN_GBM | 123697 | +0.060 | +11840.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 30798 | +0.078 | +6064.23€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 3516 | -0.001 | +40.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 81645 | +0.062 | +5609.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 7320 | -0.001 | +131.71€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 10822 | +0.104 | +1998.53€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 2036 | +0.166 | +959.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 8696 | +0.090 | +1040.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 27884 | +0.057 | +2477.32€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 4099 | +0.081 | +922.17€ | 0 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 1031 | -0.001 | +21.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 19301 | +0.066 | +1446.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 3303 | -0.004 | +82.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 150 | -0.066 | +4.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 13887 | +0.075 | +1540.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 2033 | +0.156 | +874.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 11768 | +0.061 | +666.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 28916 | +0.050 | +2074.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 7133 | +0.071 | +1116.49€ | 0 | 9 |
| ✅ UPDOWN_GBM#ETH#240min | 997 | +0.004 | +15.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 17928 | +0.052 | +898.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2718 | -0.000 | +41.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 140 | -0.099 | +2.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 25679 | +0.041 | +1464.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 8349 | +0.033 | +478.84€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 915 | -0.010 | +8.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 14990 | +0.053 | +979.33€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1299 | +0.004 | +8.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 126 | -0.141 | -10.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 16507 | +0.073 | +2287.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 7148 | +0.089 | +1712.26€ | 0 | 12 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 8962 | +0.063 | +577.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 416 | -0.101 | -3.15€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 1067 | +0.363 | +397.62€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 1067 | +0.363 | +397.62€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 508 | +0.363 | +177.36€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 508 | +0.363 | +177.36€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 559 | +0.363 | +220.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 559 | +0.363 | +220.27€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 29238 | -0.017 | +7302.53€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 29238 | -0.017 | +7302.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 2281 | -0.045 | +615.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 2281 | -0.045 | +615.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 5370 | -0.115 | +301.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 5370 | -0.115 | +301.30€ | 3 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1258 | +0.218 | +1036.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1258 | +0.218 | +1036.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 3929 | +0.217 | +2477.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 3929 | +0.217 | +2477.35€ | 1 | 19 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 8246 | -0.057 | +1233.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 8246 | -0.057 | +1233.24€ | 3 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 8154 | -0.053 | +1638.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 8154 | -0.053 | +1638.85€ | 4 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 368 | +0.057 | +31.71€ | 0 | 9 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 368 | +0.057 | +31.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 368 | +0.057 | +31.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 368 | +0.057 | +31.71€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1964 | +0.284 | +1675.12€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1964 | +0.284 | +1675.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 1030 | +0.278 | +830.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 1030 | +0.278 | +830.29€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 934 | +0.289 | +844.83€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 934 | +0.289 | +844.83€ | 0 | 8 |
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