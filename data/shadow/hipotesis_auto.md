# Hipótesis automáticas — 2026-09-23 21:03 UTC
_Generado por shadow_postmortem.py sobre 578767 resoluciones (PNL=+64546.90€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=467)

- **PATRÓN** `py_entrada` > `0.51` → IC=+0.258 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.51 (IC base=+0.140)

- **PATRÓN** `n_total_lado` > `75.0` → IC=+0.209 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 75.0 (IC base=+0.140)

- **PATRÓN** `banda_hit_calibrado` > `0.8032` → IC=+0.255 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8032 (IC base=+0.140)

- **PATRÓN** `banda_z` > `4.166` → IC=+0.167 (n=542)

  - _Acción_: Kelly boost +0.84€ cuando `banda_z` > 4.166 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.150 (n=501)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=580)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `3000.0061` → IC=+0.153 (n=361)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3000.0061 (IC base=+0.140)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.120 (n=467)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` < 0.495 (IC base=+0.046)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.133 (n=167)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 96.0 (IC base=+0.046)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=340)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.239 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.149)

- **PATRÓN** `n_total_lado` > `70.0` → IC=+0.210 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 70.0 (IC base=+0.149)

- **PATRÓN** `banda_hit_calibrado` > `0.7976` → IC=+0.266 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.7976 (IC base=+0.149)

- **PATRÓN** `banda_z` > `10.773` → IC=+0.221 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 10.773 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.169 (n=309)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 11.0 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=491)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `4456.7277` → IC=+0.151 (n=196)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4456.7277 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.151 (n=127)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 96.0 (IC base=+0.048)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.214 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=+0.218 (n=101)

- **FILTRO** `banda_hit_calibrado` < `0.6297` → IC=-0.152 (n=44)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6297
  - _Potencial_: sin este filtro IC_bueno=+0.239 (n=90)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.170 (n=107)

- **FILTRO** `py_entrada` > `0.845` → IC=-0.393 (n=26)

  - _Acción_: SKIP cuando `py_entrada` > 0.845
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=87)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.190 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=86)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=97)

- **PATRÓN** `py_entrada` > `0.55` → IC=+0.250 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.55 (IC base=+0.110)

- **PATRÓN** `banda_hit_calibrado` > `0.6297` → IC=+0.239 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6297 (IC base=+0.110)

- **PATRÓN** `banda_z` > `8.424` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `banda_z` > 8.424 (IC base=+0.110)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.170 (n=107)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.02 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `1195.1095` → IC=+0.167 (n=67)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 1195.1095 (IC base=+0.110)

### BALLENAS_CONFIRMADAS_15M#XRP#15min
- **PATRÓN** `n_ballena_banda` > `26.0` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `n_ballena_banda` > 26.0 (IC base=+0.154)

- **PATRÓN** `banda_z` > `2.517` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 2.517 (IC base=+0.154)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.705` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `ballenas_wallet_edge_medio` > 0.705 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.224 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.01 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `2518.5859` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2518.5859 (IC base=+0.154)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `146.07` → IC=-0.234 (n=6930)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 146.07
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=20793)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `139.07` → IC=-0.240 (n=906)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 139.07
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=2718)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` < `496.69` → IC=-0.150 (n=358)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 496.69
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=1075)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `129.22` → IC=-0.300 (n=858)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 129.22
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=2574)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `164.54` → IC=-0.228 (n=1650)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 164.54
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=4952)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `125.17` → IC=-0.357 (n=1375)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 125.17
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=4128)

### CANDIDATA9_BOT_CONSENSO
- **FILTRO** `py_entrada` < `0.48` → IC=-0.223 (n=380)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=380)

- **FILTRO** `py_entrada` > `0.54` → IC=-0.178 (n=234)

  - _Acción_: SKIP cuando `py_entrada` > 0.54
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=475)

- **FILTRO** `py_entrada` < `0.48` → IC=-0.145 (n=150)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=559)

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
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.203 (n=13613)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.101)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=3416)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `5618.809` → IC=+0.175 (n=2178)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 5618.809 (IC base=+0.101)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.139 (n=11135)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.137 (n=13472)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 7.0 (IC base=+0.127)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.232 (n=10661)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.174 (n=5562)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `7747.6147` → IC=+0.173 (n=2095)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 7747.6147 (IC base=+0.127)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.208 (n=1606)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.205 (n=1652)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.352 (n=763)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=2075)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `15898.9899` → IC=+0.237 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15898.9899 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.204 (n=1490)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.205 (n=1646)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` < `0.375` → IC=+0.263 (n=1500)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.375 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.201 (n=2106)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `14078.6167` → IC=+0.212 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14078.6167 (IC base=+0.200)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.615` → IC=+0.173 (n=319)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` > 0.615 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `4624.034` → IC=+0.146 (n=235)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 4624.034 (IC base=+0.104)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.147 (n=344)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 7.0 (IC base=+0.107)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.145 (n=807)

  - _Acción_: Kelly boost +0.73€ cuando `py_entrada` < 0.44 (IC base=+0.107)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.125 (n=556)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `5859.5725` → IC=+0.162 (n=220)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 5859.5725 (IC base=+0.107)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.154 (n=2756)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 5.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.145 (n=2347)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 15.0 (IC base=+0.145)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.335 (n=937)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.247 (n=654)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.233)

- **PATRÓN** `py_entrada` < `0.255` → IC=+0.357 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.255 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.238 (n=1457)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.233)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.155 (n=450)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 11.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.140 (n=645)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 17.0 (IC base=+0.137)

- **PATRÓN** `py_entrada` > `0.665` → IC=+0.234 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.665 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=525)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `1300.2394` → IC=+0.147 (n=642)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 1300.2394 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.071)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.231 (n=701)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.433 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.166 (n=1066)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 7.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.163 (n=573)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 7.0 (IC base=+0.162)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.316 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.162)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.171 (n=719)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.01 (IC base=+0.162)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.173 (n=301)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 7.0 (IC base=+0.165)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.165 (n=210)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 13.0 (IC base=+0.165)

- **PATRÓN** `py_entrada` > `0.743` → IC=+0.353 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.743 (IC base=+0.165)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.170 (n=186)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.02 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `1271.2794` → IC=+0.156 (n=222)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 1271.2794 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.144 (n=304)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 17.0 (IC base=+0.113)

- **PATRÓN** `py_entrada` < `0.355` → IC=+0.194 (n=374)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.355 (IC base=+0.113)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `9.0` → IC=-0.298 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=107)

- **FILTRO** `py_entrada` > `0.8` → IC=-0.333 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=130)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=11211)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=10714)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.225 (n=3736)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.339 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `8491.3442` → IC=+0.342 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8491.3442 (IC base=+0.198)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.175 (n=2585)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 17.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.183 (n=1896)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.71 (IC base=+0.168)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **FILTRO** `py_entrada` < `0.775` → IC=-0.284 (n=49)

  - _Acción_: SKIP cuando `py_entrada` < 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=63)

- **FILTRO** `libro_liquidez` < `9614.35` → IC=-0.328 (n=56)

  - _Acción_: SKIP cuando `libro_liquidez` < 9614.35
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=56)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.255 (n=382)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.248)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.250 (n=790)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.248)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.353 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.248)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.184 (n=2539)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 6.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.187 (n=2554)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=2208)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.181)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.248 (n=2378)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.238)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.319 (n=838)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.238)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.321 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.238)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=2597)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.196 (n=2498)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 17.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.197 (n=1915)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.71 (IC base=+0.193)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.436 (n=514)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.431)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.433 (n=459)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.431)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.471 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.431)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.430 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.431)

- **PATRÓN** `libro_liquidez` > `2073.3909` → IC=+0.439 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2073.3909 (IC base=+0.431)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.439 (n=195)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.436 (n=201)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.435)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.454 (n=171)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.471 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.438)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.438 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.438)

- **PATRÓN** `libro_liquidez` > `3366.033` → IC=+0.446 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3366.033 (IC base=+0.438)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.406 (n=104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.404)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.406 (n=104)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.404)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.419 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.404)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.406 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.404)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.775` → IC=-0.300 (n=23)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=16)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=23)

- **FILTRO** `libro_liquidez` < `7880.4556` → IC=-0.339 (n=29)

  - _Acción_: SKIP cuando `libro_liquidez` < 7880.4556
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.200 (n=33333)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.235 (n=14972)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.197)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.176 (n=5763)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 8.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.180 (n=4610)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 12.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.189 (n=6203)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.175)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.225 (n=5972)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.225 (n=5950)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.274 (n=2126)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.176 (n=5721)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 8.0 (IC base=+0.172)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.188 (n=6074)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.172)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.230 (n=2997)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.220 (n=2255)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.264 (n=2074)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.220)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.209 (n=5518)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.255 (n=2223)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.195 (n=5575)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 8.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.195 (n=5539)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.252 (n=2132)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.193)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=5086)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.118)

- **PATRÓN** `restante_min` < `4.15` → IC=+0.128 (n=4687)

  - _Acción_: Kelly boost +0.64€ cuando `restante_min` < 4.15 (IC base=+0.118)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.140 (n=5030)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.95 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.129 (n=6929)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 8.0 (IC base=+0.118)

- **PATRÓN** `lag_apertura_s` < `2.92` → IC=+0.141 (n=4661)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 2.92 (IC base=+0.118)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.200 (n=2562)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.123)

- **PATRÓN** `restante_min` < `4.1` → IC=+0.134 (n=2321)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` < 4.1 (IC base=+0.123)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.141 (n=2491)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.94 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.140 (n=2658)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 6.0 (IC base=+0.123)

- **PATRÓN** `lag_apertura_s` < `3.43` → IC=+0.145 (n=2315)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 3.43 (IC base=+0.123)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.191 (n=2524)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` < `4.19` → IC=+0.127 (n=2358)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.19 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.135 (n=2545)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `2.3` → IC=+0.138 (n=2351)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.3 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.323 (n=766)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.388 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `4080.5501` → IC=+0.312 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4080.5501 (IC base=+0.292)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.304 (n=335)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.279)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.345 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `4237.6328` → IC=+0.302 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4237.6328 (IC base=+0.279)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.334 (n=366)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.295)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.295 (n=519)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.295)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.387 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.295)

- **PATRÓN** `libro_liquidez` > `1466.3152` → IC=+0.311 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1466.3152 (IC base=+0.295)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.349 (n=84)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.341)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.363 (n=71)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.341)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.380 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.341)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.375 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.341)

- **PATRÓN** `libro_liquidez` > `720.8183` → IC=+0.377 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 720.8183 (IC base=+0.341)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.448 (n=496)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.440)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.445 (n=419)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.443 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.440)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.441 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.440)

- **PATRÓN** `libro_liquidez` > `2547.1781` → IC=+0.440 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2547.1781 (IC base=+0.440)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.448 (n=227)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.447 (n=205)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.445 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.445 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.450 (n=157)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.454 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.91` → IC=+0.440 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.91 (IC base=+0.442)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.443 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.442)

- **PATRÓN** `libro_liquidez` > `2024.9352` → IC=+0.460 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2024.9352 (IC base=+0.442)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` < `12.0` → IC=+0.370 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.384)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `hora_utc` > `15.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=54)

- **FILTRO** `py_entrada` > `0.785` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.785
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=54)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.305 (n=203)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.257)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.383 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.268 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1367.7996` → IC=+0.285 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1367.7996 (IC base=+0.257)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=54)

- **FILTRO** `py_entrada` > `0.785` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.785
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=54)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.305 (n=203)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.257)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.383 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.268 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1367.7996` → IC=+0.285 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1367.7996 (IC base=+0.257)

### GBM_LATE_15M
- **PATRÓN** `drift_60min` |x|≤ `0.481` → IC=+0.121 (n=7826)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.60€ cuando `drift_60min` |x|≤ 0.481 (IC base=+0.105)

- **PATRÓN** `ibs_20min` > `0.981` → IC=+0.244 (n=2610)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.981 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.8443` → IC=+0.250 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8443 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` < `0.6359` → IC=+0.250 (n=2185)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6359 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.953` → IC=+0.176 (n=3010)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 5.953 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` < `1.2117` → IC=+0.247 (n=2101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2117 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` > `1.0481` → IC=+0.259 (n=954)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0481 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` > `0.3055` → IC=+0.218 (n=779)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3055 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` > `1.9074` → IC=+0.206 (n=3559)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9074 (IC base=+0.105)

- **PATRÓN** `ibs_20min` < `0.57` → IC=+0.132 (n=9457)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.57 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` > `0.6126` → IC=+0.192 (n=699)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.6126 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` < `0.1523` → IC=+0.172 (n=2971)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.1523 (IC base=+0.064)

- **PATRÓN** `volumen_regimen` < `0.6986` → IC=+0.180 (n=1450)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.6986 (IC base=+0.064)

- **PATRÓN** `volumen_regimen` > `1.0529` → IC=+0.173 (n=1492)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 1.0529 (IC base=+0.064)

- **PATRÓN** `volumen_pendiente_norm` > `0.168` → IC=+0.222 (n=1575)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.168 (IC base=+0.064)

- **PATRÓN** `volumen_spike_ratio` > `1.5727` → IC=+0.200 (n=4929)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5727 (IC base=+0.064)

- **PATRÓN** `ballena_activa_n` < `136.0` → IC=+0.210 (n=5301)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 136.0 (IC base=+0.064)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.182 (n=595)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.005 (IC base=+0.161)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.174 (n=594)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0082 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.3482` → IC=+0.166 (n=1770)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.3482 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.166 (n=857)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.172 (n=1185)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 11.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.269 (n=685)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.116` → IC=+0.271 (n=761)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.116 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.211 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `1.4388` → IC=+0.163 (n=1653)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.4388 (IC base=+0.161)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.249 (n=1188)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.0896` → IC=+0.284 (n=443)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0896 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.246 (n=911)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.3691` → IC=+0.262 (n=1168)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3691 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.421` → IC=+0.234 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.421 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.427` → IC=+0.247 (n=1379)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.427 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` < `0.092` → IC=+0.230 (n=1133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.092 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2765` → IC=+0.261 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2765 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.6417` → IC=+0.241 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6417 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `1799.36` → IC=+0.235 (n=885)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1799.36 (IC base=+0.234)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.235 (n=594)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.0838` → IC=+0.252 (n=449)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0838 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.231 (n=1413)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` > `0.9894` → IC=+0.267 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9894 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` > `0.2018` → IC=+0.221 (n=722)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2018 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` < `0.5869` → IC=+0.221 (n=1404)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5869 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.863` → IC=+0.259 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.863 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` < `1.2525` → IC=+0.220 (n=1345)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2525 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` > `0.8746` → IC=+0.226 (n=897)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8746 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.2802` → IC=+0.234 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2802 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` < `1.4014` → IC=+0.222 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4014 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.3766` → IC=+0.223 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3766 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `16582.4066` → IC=+0.223 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16582.4066 (IC base=+0.217)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.150 (n=1407)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0056 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0753` → IC=+0.160 (n=468)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.0753 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.169 (n=554)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.6918` → IC=+0.170 (n=1404)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.6918 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1332` → IC=+0.155 (n=1249)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1332 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.183` → IC=+0.162 (n=226)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 11.183 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.252` → IC=+0.140 (n=1278)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 4.252 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.2044` → IC=+0.149 (n=1404)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.2044 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.0963` → IC=+0.173 (n=506)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.0963 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.4156` → IC=+0.151 (n=1294)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4156 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.4235` → IC=+0.143 (n=1293)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.4235 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `411.0` → IC=+0.146 (n=1210)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 411.0 (IC base=+0.138)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.215 (n=578)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.189 (n=1730)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 6.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.192 (n=1549)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.263 (n=685)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.199` → IC=+0.250 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.199 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` < `0.2115` → IC=+0.188 (n=1726)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` < 0.2115 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.3614` → IC=+0.200 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3614 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `2.8516` → IC=+0.207 (n=745)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8516 (IC base=+0.186)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.194 (n=1232)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.02 (IC base=+0.186)

- **PATRÓN** `sigma_h` < `0.0115` → IC=+0.223 (n=1484)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0115 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.5884` → IC=+0.217 (n=1484)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5884 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.252 (n=562)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.219 (n=691)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` < `0.0625` → IC=+0.244 (n=654)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0625 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.626` → IC=+0.248 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.626 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.3581` → IC=+0.272 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3581 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` < `1.7818` → IC=+0.211 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7818 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `2.2159` → IC=+0.220 (n=903)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2159 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.222 (n=1003)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `1876.5391` → IC=+0.232 (n=673)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1876.5391 (IC base=+0.214)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.213 (n=1138)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.214)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.163 (n=96)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=2169)

- **PATRÓN** `ibs_20min` > `0.9414` → IC=+0.212 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9414 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` > `0.3692` → IC=+0.325 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3692 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` < `0.7982` → IC=+0.330 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7982 (IC base=+0.021)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.712` → IC=+0.154 (n=694)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 4.712 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` < `0.8546` → IC=+0.322 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8546 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` > `1.2004` → IC=+0.341 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2004 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` < `0.1818` → IC=+0.316 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1818 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.3037` → IC=+0.341 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3037 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` < `1.4012` → IC=+0.337 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4012 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` > `2.1967` → IC=+0.323 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1967 (IC base=+0.021)

- **PATRÓN** `ballena_activa_n` < `164.0` → IC=+0.330 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 164.0 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` > `0.6787` → IC=+0.191 (n=137)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.6787 (IC base=+0.015)

- **PATRÓN** `volumen_regimen` < `0.8504` → IC=+0.164 (n=539)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8504 (IC base=+0.015)

- **PATRÓN** `volumen_pendiente_norm` > `0.2269` → IC=+0.218 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2269 (IC base=+0.015)

- **PATRÓN** `volumen_spike_ratio` > `1.5219` → IC=+0.176 (n=674)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.5219 (IC base=+0.015)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.172 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=316)

- **FILTRO** `ibs_20min` < `0.2703` → IC=-0.205 (n=93)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2703
  - _Potencial_: sin este filtro IC_bueno=+0.130 (n=282)

- **FILTRO** `ibs_20min` > `0.2568` → IC=-0.125 (n=2137)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2568
  - _Potencial_: sin este filtro IC_bueno=+0.126 (n=1053)

- **FILTRO** `sigma_ewma_delta_pct` > `8.651` → IC=-0.204 (n=343)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.651
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2847)

- **PATRÓN** `ibs_20min` > `0.7913` → IC=+0.223 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7913 (IC base=+0.046)

- **PATRÓN** `dist_vwap_pct` > `1.6532` → IC=+0.357 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.6532 (IC base=+0.046)

- **PATRÓN** `dist_vwap_pct` < `0.5947` → IC=+0.271 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5947 (IC base=+0.046)

- **PATRÓN** `volumen_regimen` < `0.6541` → IC=+0.265 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6541 (IC base=+0.046)

- **PATRÓN** `volumen_regimen` > `0.7836` → IC=+0.303 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7836 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` < `0.0729` → IC=+0.312 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0729 (IC base=+0.046)

- **PATRÓN** `volumen_spike_ratio` < `2.2264` → IC=+0.290 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2264 (IC base=+0.046)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.293 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 49.0 (IC base=+0.046)

- **PATRÓN** `ibs_20min` < `0.2568` → IC=+0.126 (n=1053)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` < 0.2568 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` > `0.6893` → IC=+0.254 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6893 (IC base=-0.042)

- **PATRÓN** `volumen_regimen` < `1.0932` → IC=+0.223 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0932 (IC base=-0.042)

- **PATRÓN** `volumen_regimen` > `0.9031` → IC=+0.212 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9031 (IC base=-0.042)

- **PATRÓN** `volumen_pendiente_norm` < `0.1041` → IC=+0.228 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1041 (IC base=-0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.1588` → IC=+0.256 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1588 (IC base=-0.042)

- **PATRÓN** `volumen_spike_ratio` < `2.4396` → IC=+0.260 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4396 (IC base=-0.042)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6585` → IC=-0.178 (n=548)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6585
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=1648)

- **FILTRO** `ibs_20min` < `0.7098` → IC=-0.157 (n=1449)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7098
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=747)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.198 (n=405)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=1791)

- **FILTRO** `ibs_20min` > `0.77` → IC=-0.201 (n=808)

  - _Acción_: SKIP cuando `ibs_20min` > 0.77
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=2437)

- **PATRÓN** `dist_vwap_pct` > `0.7895` → IC=+0.322 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7895 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` < `0.2685` → IC=+0.321 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2685 (IC base=-0.067)

- **PATRÓN** `volumen_regimen` < `0.9872` → IC=+0.295 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9872 (IC base=-0.067)

- **PATRÓN** `volumen_regimen` > `0.6166` → IC=+0.310 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6166 (IC base=-0.067)

- **PATRÓN** `volumen_pendiente_norm` < `0.0995` → IC=+0.297 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0995 (IC base=-0.067)

- **PATRÓN** `volumen_pendiente_norm` > `0.0744` → IC=+0.311 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0744 (IC base=-0.067)

- **PATRÓN** `volumen_spike_ratio` < `1.3923` → IC=+0.311 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3923 (IC base=-0.067)

- **PATRÓN** `volumen_spike_ratio` > `1.7955` → IC=+0.300 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7955 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` > `0.8778` → IC=+0.265 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8778 (IC base=-0.025)

- **PATRÓN** `volumen_regimen` < `0.7367` → IC=+0.248 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7367 (IC base=-0.025)

- **PATRÓN** `volumen_regimen` > `1.0829` → IC=+0.279 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0829 (IC base=-0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.1026` → IC=+0.273 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1026 (IC base=-0.025)

- **PATRÓN** `volumen_spike_ratio` < `2.1684` → IC=+0.250 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1684 (IC base=-0.025)

- **PATRÓN** `volumen_spike_ratio` > `1.4406` → IC=+0.246 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4406 (IC base=-0.025)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.244 (n=639)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=-0.025)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.198 (n=3270)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0097 (IC base=+0.097)

- **PATRÓN** `ibs_20min` > `0.4733` → IC=+0.188 (n=8750)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4733 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.7682` → IC=+0.289 (n=1040)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7682 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.585` → IC=+0.156 (n=4632)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 3.585 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` > `0.688` → IC=+0.248 (n=3100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.688 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` > `0.2972` → IC=+0.265 (n=823)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2972 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` < `1.4711` → IC=+0.241 (n=1877)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4711 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` > `2.6816` → IC=+0.237 (n=1876)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6816 (IC base=+0.097)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.268 (n=5148)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 98.0 (IC base=+0.097)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.151 (n=3275)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0091 (IC base=+0.072)

- **PATRÓN** `ibs_20min` < `0.5464` → IC=+0.152 (n=8626)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.5464 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` < `0.2484` → IC=+0.237 (n=2716)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2484 (IC base=+0.072)

- **PATRÓN** `volumen_regimen` < `0.7094` → IC=+0.237 (n=1266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7094 (IC base=+0.072)

- **PATRÓN** `volumen_regimen` > `1.2044` → IC=+0.244 (n=959)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2044 (IC base=+0.072)

- **PATRÓN** `volumen_pendiente_norm` > `0.2454` → IC=+0.301 (n=721)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2454 (IC base=+0.072)

- **PATRÓN** `volumen_spike_ratio` < `1.6086` → IC=+0.254 (n=1663)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6086 (IC base=+0.072)

- **PATRÓN** `volumen_spike_ratio` > `2.3262` → IC=+0.255 (n=1714)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3262 (IC base=+0.072)

- **PATRÓN** `ballena_activa_n` < `83.0` → IC=+0.261 (n=3654)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 83.0 (IC base=+0.072)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `sigma_ewma_delta_pct` > `4.503` → IC=-0.165 (n=512)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.503
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=1728)

- **PATRÓN** `ibs_20min` > `0.8889` → IC=+0.262 (n=678)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8889 (IC base=+0.044)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.772` → IC=+0.204 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.772 (IC base=+0.044)

- **PATRÓN** `volumen_pendiente_norm` > `0.2229` → IC=+0.275 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2229 (IC base=+0.044)

- **PATRÓN** `volumen_spike_ratio` < `1.4401` → IC=+0.178 (n=281)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.4401 (IC base=+0.044)

- **PATRÓN** `volumen_spike_ratio` > `2.1594` → IC=+0.190 (n=382)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.1594 (IC base=+0.044)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.179 (n=375)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 15.0 (IC base=+0.044)

- **PATRÓN** `volumen_pendiente_norm` < `0.1673` → IC=+0.442 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1673 (IC base=-0.018)

- **PATRÓN** `volumen_spike_ratio` < `2.7434` → IC=+0.432 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.7434 (IC base=-0.018)

- **PATRÓN** `volumen_spike_ratio` > `2.3568` → IC=+0.429 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3568 (IC base=-0.018)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=-0.018)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.86` → IC=+0.155 (n=654)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.86 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` > `0.1282` → IC=+0.173 (n=502)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1282 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` > `0.8564` → IC=+0.172 (n=598)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 0.8564 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.2752` → IC=+0.219 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2752 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `1.4239` → IC=+0.202 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4239 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `247.0` → IC=+0.195 (n=382)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 247.0 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` < `0.1622` → IC=+0.217 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1622 (IC base=+0.003)

- **PATRÓN** `volumen_regimen` > `0.6101` → IC=+0.212 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6101 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2721` → IC=+0.300 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2721 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` < `1.4496` → IC=+0.225 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4496 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.1598` → IC=+0.230 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1598 (IC base=+0.003)

- **PATRÓN** `ballena_activa_n` < `477.0` → IC=+0.213 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 477.0 (IC base=+0.003)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.292 (n=518)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.246)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.247 (n=1554)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.246)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.250 (n=1377)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.246)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.300 (n=823)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.246)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.736` → IC=+0.280 (n=494)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.736 (IC base=+0.246)

- **PATRÓN** `volumen_pendiente_norm` < `0.1373` → IC=+0.258 (n=1376)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1373 (IC base=+0.246)

- **PATRÓN** `volumen_spike_ratio` > `3.4416` → IC=+0.261 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.4416 (IC base=+0.246)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.255 (n=1089)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.246)

- **PATRÓN** `libro_liquidez` > `1948.2131` → IC=+0.255 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1948.2131 (IC base=+0.246)

- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.315 (n=561)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.282)

- **PATRÓN** `drift_60min` |x|≤ `0.6004` → IC=+0.283 (n=1235)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6004 (IC base=+0.282)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.329 (n=418)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.282)

- **PATRÓN** `ibs_20min` < `0.2233` → IC=+0.289 (n=1087)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2233 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.883` → IC=+0.300 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.883 (IC base=+0.282)

- **PATRÓN** `volumen_pendiente_norm` > `0.3414` → IC=+0.309 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3414 (IC base=+0.282)

- **PATRÓN** `volumen_spike_ratio` < `1.6017` → IC=+0.285 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6017 (IC base=+0.282)

- **PATRÓN** `volumen_spike_ratio` > `2.7705` → IC=+0.286 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7705 (IC base=+0.282)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.289 (n=829)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `1931.7443` → IC=+0.304 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1931.7443 (IC base=+0.282)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.287 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.282)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.2829` → IC=-0.190 (n=475)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2829
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=1430)

- **FILTRO** `ibs_20min` > `0.7739` → IC=-0.179 (n=581)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7739
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=1744)

- **PATRÓN** `ibs_20min` > `0.9101` → IC=+0.178 (n=477)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.9101 (IC base=+0.009)

- **PATRÓN** `dist_vwap_pct` > `0.4586` → IC=+0.224 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4586 (IC base=+0.009)

- **PATRÓN** `volumen_regimen` < `0.9969` → IC=+0.233 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9969 (IC base=+0.009)

- **PATRÓN** `volumen_regimen` > `0.5819` → IC=+0.209 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5819 (IC base=+0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.0773` → IC=+0.247 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0773 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` < `2.0971` → IC=+0.243 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0971 (IC base=+0.009)

- **PATRÓN** `ballena_activa_n` < `101.0` → IC=+0.253 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 101.0 (IC base=+0.009)

- **PATRÓN** `dist_vwap_pct` > `0.1559` → IC=+0.205 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1559 (IC base=-0.007)

- **PATRÓN** `dist_vwap_pct` < `0.6787` → IC=+0.194 (n=465)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.6787 (IC base=-0.007)

- **PATRÓN** `volumen_regimen` < `1.1643` → IC=+0.206 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1643 (IC base=-0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.2812` → IC=+0.278 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2812 (IC base=-0.007)

- **PATRÓN** `volumen_spike_ratio` < `1.8288` → IC=+0.255 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8288 (IC base=-0.007)

- **PATRÓN** `volumen_spike_ratio` > `2.178` → IC=+0.236 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.178 (IC base=-0.007)

- **PATRÓN** `ballena_activa_n` < `139.0` → IC=+0.244 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 139.0 (IC base=-0.007)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7188` → IC=-0.200 (n=1036)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7188
  - _Potencial_: sin este filtro IC_bueno=+0.281 (n=1038)

- **FILTRO** `ibs_20min` > `0.6875` → IC=-0.231 (n=540)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6875
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=1641)

- **FILTRO** `sigma_ewma_delta_pct` > `4.678` → IC=-0.176 (n=476)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.678
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=1705)

- **PATRÓN** `ibs_20min` > `0.7188` → IC=+0.281 (n=1038)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7188 (IC base=+0.041)

- **PATRÓN** `dist_vwap_pct` > `0.8494` → IC=+0.338 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8494 (IC base=+0.041)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.568` → IC=+0.158 (n=331)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 9.568 (IC base=+0.041)

- **PATRÓN** `volumen_regimen` < `0.8667` → IC=+0.303 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8667 (IC base=+0.041)

- **PATRÓN** `volumen_regimen` > `0.6434` → IC=+0.291 (n=762)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6434 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` < `0.1024` → IC=+0.295 (n=709)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1024 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.2247` → IC=+0.294 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2247 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` < `1.4421` → IC=+0.327 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4421 (IC base=+0.041)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.312 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.041)

- **PATRÓN** `ibs_20min` < `0.1` → IC=+0.213 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1 (IC base=+0.014)

- **PATRÓN** `dist_vwap_pct` < `0.2135` → IC=+0.215 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2135 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` < `0.7017` → IC=+0.246 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7017 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` < `0.0994` → IC=+0.205 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0994 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` > `0.0706` → IC=+0.199 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0706 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` < `2.4945` → IC=+0.215 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4945 (IC base=+0.014)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.233 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 51.0 (IC base=+0.014)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0168` → IC=+0.320 (n=849)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0168 (IC base=+0.279)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.301 (n=595)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.279)

- **PATRÓN** `ibs_20min` > `0.74` → IC=+0.325 (n=1138)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.74 (IC base=+0.279)

- **PATRÓN** `dist_vwap_pct` > `0.2044` → IC=+0.319 (n=759)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2044 (IC base=+0.279)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.523` → IC=+0.304 (n=671)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.523 (IC base=+0.279)

- **PATRÓN** `volumen_regimen` > `0.8627` → IC=+0.305 (n=849)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8627 (IC base=+0.279)

- **PATRÓN** `volumen_pendiente_norm` > `0.2826` → IC=+0.320 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2826 (IC base=+0.279)

- **PATRÓN** `volumen_spike_ratio` > `2.1562` → IC=+0.294 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1562 (IC base=+0.279)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.285 (n=1359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `2623.8724` → IC=+0.297 (n=849)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2623.8724 (IC base=+0.279)

- **PATRÓN** `sigma_h` > `0.0152` → IC=+0.295 (n=923)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0152 (IC base=+0.271)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.279 (n=482)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.271)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.273 (n=685)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.271)

- **PATRÓN** `ibs_20min` < `0.3953` → IC=+0.304 (n=1386)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3953 (IC base=+0.271)

- **PATRÓN** `dist_vwap_pct` > `0.2984` → IC=+0.278 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2984 (IC base=+0.271)

- **PATRÓN** `dist_vwap_pct` < `0.9682` → IC=+0.272 (n=1561)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9682 (IC base=+0.271)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.006` → IC=+0.295 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.006 (IC base=+0.271)

- **PATRÓN** `volumen_regimen` < `0.6388` → IC=+0.274 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6388 (IC base=+0.271)

- **PATRÓN** `volumen_regimen` > `1.2432` → IC=+0.306 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2432 (IC base=+0.271)

- **PATRÓN** `volumen_pendiente_norm` > `0.2392` → IC=+0.338 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2392 (IC base=+0.271)

- **PATRÓN** `volumen_spike_ratio` < `1.4335` → IC=+0.270 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4335 (IC base=+0.271)

- **PATRÓN** `volumen_spike_ratio` > `2.1624` → IC=+0.274 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1624 (IC base=+0.271)

- **PATRÓN** `libro_liquidez` > `2614.9946` → IC=+0.276 (n=923)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2614.9946 (IC base=+0.271)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.171 (n=2549)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0049 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.202 (n=2549)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.0898` → IC=+0.186 (n=2549)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.0898 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.178 (n=7973)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `0.5781` → IC=+0.217 (n=7644)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5781 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.1763` → IC=+0.197 (n=3355)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1763 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.311` → IC=+0.258 (n=1570)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.311 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `1.2151` → IC=+0.160 (n=5057)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2151 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` > `0.628` → IC=+0.160 (n=5057)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.628 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.2453` → IC=+0.193 (n=1543)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2453 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.5622` → IC=+0.171 (n=3223)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5622 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `2.6272` → IC=+0.175 (n=2442)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.6272 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `2399.8931` → IC=+0.168 (n=5096)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2399.8931 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `116.0` → IC=+0.180 (n=6551)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 116.0 (IC base=+0.167)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.182 (n=4893)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0066 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.0806` → IC=+0.208 (n=2444)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0806 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.203 (n=2824)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` < `0.4773` → IC=+0.226 (n=7324)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4773 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` < `0.2319` → IC=+0.159 (n=5318)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.2319 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.321` → IC=+0.195 (n=1250)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 10.321 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `1.174` → IC=+0.152 (n=5317)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.174 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.2916` → IC=+0.223 (n=1051)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2916 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.5644` → IC=+0.167 (n=2924)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.5644 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `2.6258` → IC=+0.171 (n=2215)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.6258 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `117.0` → IC=+0.173 (n=6284)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 117.0 (IC base=+0.167)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.222 (n=437)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.182)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.186 (n=594)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0076 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.3418` → IC=+0.206 (n=1306)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3418 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.195 (n=871)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 11.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.301 (n=642)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.107` → IC=+0.311 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.107 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.236 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `1.4363` → IC=+0.180 (n=1206)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.4363 (IC base=+0.182)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.251 (n=849)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.1866` → IC=+0.293 (n=632)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1866 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.242 (n=976)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.247 (n=465)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.3437` → IC=+0.263 (n=948)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3437 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.25` → IC=+0.251 (n=1021)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.25 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.096` → IC=+0.233 (n=785)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.096 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.287` → IC=+0.257 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.287 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.4205` → IC=+0.261 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4205 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1801.6295` → IC=+0.246 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1801.6295 (IC base=+0.237)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.234 (n=382)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.0742` → IC=+0.202 (n=380)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0742 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=1199)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `0.4084` → IC=+0.225 (n=1138)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4084 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` > `0.2116` → IC=+0.215 (n=682)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2116 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.523` → IC=+0.238 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.523 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` < `1.2653` → IC=+0.164 (n=1138)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2653 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` > `0.8793` → IC=+0.165 (n=759)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.8793 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.2827` → IC=+0.201 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2827 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` < `1.503` → IC=+0.189 (n=486)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.503 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `2.4602` → IC=+0.160 (n=368)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.4602 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `15869.2533` → IC=+0.162 (n=516)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 15869.2533 (IC base=+0.161)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.157 (n=1250)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0057 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.2922` → IC=+0.159 (n=1247)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2922 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.176 (n=418)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 18.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.5646` → IC=+0.184 (n=1247)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.5646 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.1346` → IC=+0.161 (n=1232)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.1346 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.777` → IC=+0.202 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.777 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.2113` → IC=+0.156 (n=1247)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.2113 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.1573` → IC=+0.153 (n=379)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.1573 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.4156` → IC=+0.145 (n=1135)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.4156 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `215.0` → IC=+0.171 (n=351)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 215.0 (IC base=+0.136)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.220 (n=427)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.2255` → IC=+0.214 (n=856)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2255 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.217 (n=444)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.291 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.868` → IC=+0.276 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.868 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.133` → IC=+0.200 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.133 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` < `1.6427` → IC=+0.199 (n=406)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.6427 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` > `2.8714` → IC=+0.207 (n=551)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8714 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.207 (n=905)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `1952.4384` → IC=+0.197 (n=427)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 1952.4384 (IC base=+0.197)

- **PATRÓN** `sigma_h` < `0.0113` → IC=+0.233 (n=1062)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0113 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.0967` → IC=+0.256 (n=354)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0967 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.280 (n=371)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` < `0.2405` → IC=+0.258 (n=934)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2405 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.746` → IC=+0.273 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.746 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.3581` → IC=+0.272 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3581 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` < `1.7913` → IC=+0.217 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7913 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `3.4252` → IC=+0.233 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.4252 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `1880.6384` → IC=+0.225 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1880.6384 (IC base=+0.221)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.220 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.221)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.172 (n=1075)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0067 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.4327` → IC=+0.158 (n=1222)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4327 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=1284)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` > `0.3782` → IC=+0.195 (n=1221)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.3782 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.1621` → IC=+0.180 (n=817)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.1621 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.936` → IC=+0.227 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.936 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `1.0418` → IC=+0.142 (n=1075)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.0418 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` > `0.6283` → IC=+0.148 (n=1221)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.6283 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.2448` → IC=+0.196 (n=258)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2448 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `1.4216` → IC=+0.151 (n=399)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4216 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `2.5292` → IC=+0.171 (n=399)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.5292 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `6680.8292` → IC=+0.184 (n=814)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 6680.8292 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `165.0` → IC=+0.144 (n=1158)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 165.0 (IC base=+0.142)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.155 (n=1295)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0073 (IC base=+0.123)

- **PATRÓN** `drift_60min` |x|≤ `0.3834` → IC=+0.144 (n=1293)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3834 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.177 (n=503)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` < `0.635` → IC=+0.170 (n=1293)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.635 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` < `0.5821` → IC=+0.133 (n=1499)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.5821 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.904` → IC=+0.170 (n=453)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 6.904 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `0.849` → IC=+0.148 (n=862)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.849 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.2908` → IC=+0.197 (n=186)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2908 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.7906` → IC=+0.133 (n=783)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.7906 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.489` → IC=+0.136 (n=391)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.489 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `10015.5876` → IC=+0.160 (n=586)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 10015.5876 (IC base=+0.123)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.155 (n=627)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0101 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=1414)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.5167` → IC=+0.203 (n=1380)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5167 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `0.8401` → IC=+0.215 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8401 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.729` → IC=+0.253 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.729 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `1.2233` → IC=+0.130 (n=1382)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.2233 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` > `0.639` → IC=+0.122 (n=1380)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` > 0.639 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` < `0.1649` → IC=+0.131 (n=1388)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1649 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.0711` → IC=+0.121 (n=579)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` > 0.0711 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.4413` → IC=+0.143 (n=444)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4413 (IC base=+0.118)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.126 (n=1446)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2896.4901` → IC=+0.196 (n=626)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2896.4901 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.135 (n=1056)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 50.0 (IC base=+0.118)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.149 (n=620)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0061 (IC base=+0.113)

- **PATRÓN** `drift_60min` |x|≤ `0.1031` → IC=+0.154 (n=469)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1031 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.163 (n=638)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 15.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.5652` → IC=+0.209 (n=1406)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5652 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` > `0.9994` → IC=+0.144 (n=186)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.9994 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.1983` → IC=+0.137 (n=1293)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.1983 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.006` → IC=+0.143 (n=228)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 9.006 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `1.174` → IC=+0.121 (n=1406)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.174 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.2773` → IC=+0.171 (n=171)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2773 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` > `2.4253` → IC=+0.130 (n=419)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.4253 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `3086.3351` → IC=+0.158 (n=469)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 3086.3351 (IC base=+0.113)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0189` → IC=+0.214 (n=879)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0189 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=1371)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.209 (n=599)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` > `0.7381` → IC=+0.262 (n=1178)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7381 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.5032` → IC=+0.222 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5032 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.547` → IC=+0.244 (n=622)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.547 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` < `1.209` → IC=+0.205 (n=1319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.209 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` > `0.8592` → IC=+0.222 (n=880)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8592 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` > `0.234` → IC=+0.268 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.234 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` < `2.1558` → IC=+0.215 (n=1121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1558 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` > `1.4098` → IC=+0.207 (n=1273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4098 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.205 (n=1400)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `2613.2973` → IC=+0.206 (n=879)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2613.2973 (IC base=+0.202)

- **PATRÓN** `sigma_h` < `0.0086` → IC=+0.233 (n=458)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0086 (IC base=+0.204)

- **PATRÓN** `sigma_h` > `0.0224` → IC=+0.205 (n=622)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0224 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.0896` → IC=+0.223 (n=457)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0896 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.222 (n=674)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.212 (n=624)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` < `0.4385` → IC=+0.245 (n=1371)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4385 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `1.2049` → IC=+0.225 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2049 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.388` → IC=+0.242 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.388 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` > `0.628` → IC=+0.216 (n=1371)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.628 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.2833` → IC=+0.288 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2833 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` < `2.2184` → IC=+0.193 (n=1082)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 2.2184 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `1.4406` → IC=+0.198 (n=1230)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4406 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `2586.8546` → IC=+0.206 (n=914)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2586.8546 (IC base=+0.204)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.164 (n=602)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0039 (IC base=+0.147)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.181 (n=600)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0089 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.0997` → IC=+0.153 (n=600)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.0997 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.185 (n=912)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.5505` → IC=+0.188 (n=1608)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.5505 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.8737` → IC=+0.191 (n=286)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.8737 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.728` → IC=+0.176 (n=828)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 3.728 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `0.8743` → IC=+0.164 (n=1050)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8743 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` > `1.2097` → IC=+0.155 (n=525)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 1.2097 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.165` → IC=+0.175 (n=499)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.165 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `1.4378` → IC=+0.167 (n=578)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.4378 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `2.5472` → IC=+0.159 (n=578)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.5472 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.150 (n=1621)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `12348.3168` → IC=+0.156 (n=600)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 12348.3168 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `164.0` → IC=+0.166 (n=1580)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 164.0 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.133 (n=1263)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0057 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.121 (n=1808)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 6.0 (IC base=+0.104)

- **PATRÓN** `ibs_20min` < `0.3161` → IC=+0.160 (n=1263)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.3161 (IC base=+0.104)

- **PATRÓN** `volumen_spike_ratio` < `2.227` → IC=+0.122 (n=1603)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.227 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `3859.8614` → IC=+0.123 (n=1262)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 3859.8614 (IC base=+0.104)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.1101` → IC=+0.137 (n=199)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.1101 (IC base=+0.107)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.148 (n=407)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 9.0 (IC base=+0.107)

- **PATRÓN** `ibs_20min` > `0.2513` → IC=+0.146 (n=453)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.2513 (IC base=+0.107)

- **PATRÓN** `dist_vwap_pct` > `0.3087` → IC=+0.163 (n=158)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.3087 (IC base=+0.107)

- **PATRÓN** `volumen_regimen` < `0.6136` → IC=+0.154 (n=151)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6136 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `12708.3374` → IC=+0.136 (n=405)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 12708.3374 (IC base=+0.107)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.204 (n=204)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.3387` → IC=+0.148 (n=604)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3387 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.141 (n=622)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.6039` → IC=+0.177 (n=531)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.6039 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` < `0.307` → IC=+0.149 (n=639)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.307 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.384` → IC=+0.152 (n=234)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 4.384 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` > `0.7174` → IC=+0.147 (n=539)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.7174 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.205 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `2.1013` → IC=+0.151 (n=523)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.1013 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `1.4187` → IC=+0.141 (n=594)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.4187 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `389.0` → IC=+0.139 (n=572)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 389.0 (IC base=+0.130)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.260 (n=244)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.192)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.195 (n=185)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.007 (IC base=+0.192)

- **PATRÓN** `drift_60min` |x|≤ `0.0979` → IC=+0.206 (n=185)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0979 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.229 (n=253)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.192)

- **PATRÓN** `ibs_20min` > `0.7033` → IC=+0.241 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7033 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` > `0.9351` → IC=+0.226 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9351 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.948` → IC=+0.221 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.948 (IC base=+0.192)

- **PATRÓN** `volumen_regimen` < `0.8389` → IC=+0.198 (n=369)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 0.8389 (IC base=+0.192)

- **PATRÓN** `volumen_regimen` > `1.1573` → IC=+0.211 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1573 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` > `0.2601` → IC=+0.295 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2601 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` < `1.3913` → IC=+0.239 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3913 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` > `2.4036` → IC=+0.228 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4036 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.199 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `12367.2302` → IC=+0.206 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12367.2302 (IC base=+0.192)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.120 (n=459)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.0061 (IC base=+0.087)

- **PATRÓN** `ibs_20min` < `0.0837` → IC=+0.150 (n=175)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.0837 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2242` → IC=+0.131 (n=82)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` > 0.2242 (IC base=+0.087)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` > `0.5227` → IC=-0.161 (n=125)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5227
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=378)

- **FILTRO** `dist_vwap_pct` > `0.3427` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3427
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=469)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.189 (n=178)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0089 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.165 (n=368)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 8.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` > `0.7333` → IC=+0.203 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7333 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` > `0.6339` → IC=+0.219 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6339 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.134` → IC=+0.208 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.134 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `1.0712` → IC=+0.147 (n=346)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.0712 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` > `0.7359` → IC=+0.154 (n=351)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.7359 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.289` → IC=+0.202 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.289 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` < `1.4844` → IC=+0.138 (n=125)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.4844 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `2.2214` → IC=+0.169 (n=170)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.2214 (IC base=+0.131)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.133 (n=429)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.02 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `3064.7088` → IC=+0.199 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3064.7088 (IC base=+0.131)

- **PATRÓN** `ibs_20min` < `0.5227` → IC=+0.140 (n=378)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.5227 (IC base=+0.064)

- **PATRÓN** `volumen_spike_ratio` < `1.8672` → IC=+0.139 (n=236)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.8672 (IC base=+0.064)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0232` → IC=+0.161 (n=178)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0232 (IC base=+0.147)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.182 (n=177)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0068 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.2324` → IC=+0.178 (n=119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.2324 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.167 (n=64)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 16.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.216 (n=79)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.4` → IC=+0.189 (n=178)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.2468` → IC=+0.153 (n=93)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.2468 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `1.0795` → IC=+0.160 (n=201)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 1.0795 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.705` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 7.705 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.317` → IC=+0.175 (n=152)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` < 3.317 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` > `0.6778` → IC=+0.171 (n=159)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 0.6778 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` < `0.2547` → IC=+0.174 (n=173)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` < 0.2547 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `1.4421` → IC=+0.222 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4421 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.176 (n=180)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.02 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `2727.8122` → IC=+0.163 (n=81)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2727.8122 (IC base=+0.147)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.155 (n=201)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0091 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.178` → IC=+0.170 (n=89)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.178 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `1.1744` → IC=+0.295 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1744 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.576` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.576 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `0.8853` → IC=+0.128 (n=135)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 0.8853 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.6515` → IC=+0.136 (n=201)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.6515 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1187` → IC=+0.130 (n=179)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1187 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.6848` → IC=+0.135 (n=83)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.6848 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `2.8185` → IC=+0.131 (n=63)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.8185 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.146 (n=162)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 17.0 (IC base=+0.122)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.208 (n=3258)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.179 (n=10206)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.216 (n=9776)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4706 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.9719` → IC=+0.207 (n=1385)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9719 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.61` → IC=+0.227 (n=4733)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.61 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `0.8815` → IC=+0.164 (n=4351)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8815 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.24` → IC=+0.200 (n=1826)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.24 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.6046` → IC=+0.188 (n=3126)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6046 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `2342.6107` → IC=+0.172 (n=6510)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2342.6107 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `87.0` → IC=+0.195 (n=7389)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 87.0 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.190 (n=5930)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.007 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.1472` → IC=+0.189 (n=3908)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.1472 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.204 (n=3368)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` < `0.566` → IC=+0.237 (n=8878)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.566 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` < `0.2477` → IC=+0.161 (n=5500)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.2477 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.008` → IC=+0.203 (n=1248)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.008 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.721` → IC=+0.180 (n=8595)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 3.721 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.704` → IC=+0.160 (n=2690)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.704 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2879` → IC=+0.241 (n=1166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2879 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6329` → IC=+0.192 (n=2709)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6329 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.191 (n=5191)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 48.0 (IC base=+0.180)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.210 (n=556)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.190)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.224 (n=555)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.198 (n=799)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 15.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.200 (n=1120)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.321 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.017` → IC=+0.314 (n=739)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.017 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.2734` → IC=+0.249 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2734 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` < `1.552` → IC=+0.182 (n=689)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.552 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `2.5813` → IC=+0.202 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5813 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.191 (n=988)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.02 (IC base=+0.190)

- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.257 (n=1295)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0078 (IC base=+0.257)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.262 (n=1155)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.257)

- **PATRÓN** `drift_60min` |x|≤ `0.1277` → IC=+0.285 (n=569)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1277 (IC base=+0.257)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.268 (n=1170)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.257)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.258 (n=1180)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.257)

- **PATRÓN** `ibs_20min` < `0.3485` → IC=+0.289 (n=1138)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3485 (IC base=+0.257)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.569` → IC=+0.262 (n=1296)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.569 (IC base=+0.257)

- **PATRÓN** `volumen_pendiente_norm` > `0.2802` → IC=+0.284 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2802 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` > `1.8654` → IC=+0.271 (n=789)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8654 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1798.2686` → IC=+0.263 (n=862)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1798.2686 (IC base=+0.257)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.195 (n=525)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0028 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.0841` → IC=+0.162 (n=521)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.0841 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=1634)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.3134` → IC=+0.203 (n=1563)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3134 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.3442` → IC=+0.197 (n=638)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.3442 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.74` → IC=+0.175 (n=358)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 9.74 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.233` → IC=+0.153 (n=1404)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 4.233 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.6288` → IC=+0.179 (n=521)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.6288 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.2681` → IC=+0.207 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2681 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.1148` → IC=+0.162 (n=1327)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.1148 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.7596` → IC=+0.155 (n=1005)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.7596 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `15661.8767` → IC=+0.153 (n=709)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 15661.8767 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `477.0` → IC=+0.159 (n=1438)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 477.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.164 (n=1355)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0057 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.3225` → IC=+0.160 (n=1355)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.3225 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.175 (n=454)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 18.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` < `0.2689` → IC=+0.234 (n=904)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2689 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.1366` → IC=+0.165 (n=1221)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1366 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.325` → IC=+0.159 (n=227)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 11.325 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `1.1888` → IC=+0.162 (n=1355)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1888 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.1514` → IC=+0.198 (n=366)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1514 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.3998` → IC=+0.159 (n=1257)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.3998 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `2.0862` → IC=+0.161 (n=571)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.0862 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `425.0` → IC=+0.157 (n=1021)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 425.0 (IC base=+0.149)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.245 (n=527)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.224 (n=1658)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.223 (n=1607)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `0.6697` → IC=+0.256 (n=1412)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6697 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.81` → IC=+0.293 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.81 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` < `0.2125` → IC=+0.221 (n=1557)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2125 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `2.844` → IC=+0.243 (n=682)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.844 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.228 (n=1123)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `1956.62` → IC=+0.220 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1956.62 (IC base=+0.218)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.231 (n=1306)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 53.0 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0115` → IC=+0.240 (n=1473)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0115 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.1657` → IC=+0.240 (n=648)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1657 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.263 (n=558)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.233)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.238 (n=693)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.3594` → IC=+0.270 (n=1296)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3594 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.756` → IC=+0.280 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.756 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.3447` → IC=+0.300 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3447 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` < `1.7544` → IC=+0.233 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7544 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.1919` → IC=+0.237 (n=898)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1919 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.243 (n=996)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `1877.7172` → IC=+0.249 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1877.7172 (IC base=+0.233)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.231 (n=1265)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=+0.233)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.179 (n=558)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0035 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.4373` → IC=+0.143 (n=1664)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.4373 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.149 (n=1743)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` > `0.8762` → IC=+0.260 (n=755)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8762 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.5779` → IC=+0.168 (n=471)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.5779 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.157` → IC=+0.159 (n=692)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 4.157 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `0.8766` → IC=+0.154 (n=1110)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8766 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.2358` → IC=+0.215 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2358 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `1.5214` → IC=+0.148 (n=708)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.5214 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `1.7646` → IC=+0.146 (n=1073)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.7646 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `8121.0948` → IC=+0.228 (n=755)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8121.0948 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `80.0` → IC=+0.151 (n=522)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 80.0 (IC base=+0.135)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.155 (n=1362)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0076 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.4464` → IC=+0.154 (n=1362)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4464 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=509)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.142 (n=621)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.7011` → IC=+0.181 (n=1362)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.7011 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.6016` → IC=+0.142 (n=1504)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.6016 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.14` → IC=+0.177 (n=199)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 11.14 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.8616` → IC=+0.146 (n=908)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.8616 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `1.1938` → IC=+0.140 (n=454)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 1.1938 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2865` → IC=+0.244 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2865 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.4439` → IC=+0.150 (n=1290)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.4439 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `10917.9028` → IC=+0.208 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10917.9028 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `179.0` → IC=+0.144 (n=1284)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 179.0 (IC base=+0.136)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.137 (n=1099)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.0081 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.132 (n=1696)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.190 (n=1652)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.4706 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` > `1.0784` → IC=+0.202 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0784 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.451` → IC=+0.232 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.451 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `0.8906` → IC=+0.133 (n=1100)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.8906 (IC base=+0.111)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.124 (n=1662)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `2909.4755` → IC=+0.250 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2909.4755 (IC base=+0.111)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.130 (n=1264)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 54.0 (IC base=+0.111)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.173 (n=543)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0058 (IC base=+0.111)

- **PATRÓN** `drift_60min` |x|≤ `0.1305` → IC=+0.159 (n=541)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1305 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.123 (n=1676)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 5.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.202 (n=1623)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6364 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` < `0.219` → IC=+0.127 (n=1320)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.219 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.451` → IC=+0.123 (n=1568)

  - _Acción_: Kelly boost +0.61€ cuando `sigma_ewma_delta_pct` < 3.451 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `0.7164` → IC=+0.150 (n=713)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.7164 (IC base=+0.111)

- **PATRÓN** `volumen_pendiente_norm` > `0.2248` → IC=+0.172 (n=251)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2248 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` < `1.4497` → IC=+0.136 (n=487)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.4497 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` > `2.5192` → IC=+0.128 (n=487)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 2.5192 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `2844.2019` → IC=+0.164 (n=540)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2844.2019 (IC base=+0.111)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0193` → IC=+0.221 (n=1101)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0193 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.214 (n=1727)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.213 (n=1476)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.5146` → IC=+0.251 (n=1652)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5146 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` > `0.2017` → IC=+0.234 (n=980)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2017 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.219` → IC=+0.271 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.219 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` < `1.0716` → IC=+0.211 (n=1454)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0716 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` > `0.6363` → IC=+0.218 (n=1652)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6363 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.235` → IC=+0.250 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.235 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.5103` → IC=+0.237 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5103 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.220 (n=1732)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2620.2181` → IC=+0.224 (n=1101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2620.2181 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0088` → IC=+0.224 (n=593)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0088 (IC base=+0.199)

- **PATRÓN** `sigma_h` > `0.0256` → IC=+0.218 (n=594)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0256 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.207 (n=1258)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.5185` → IC=+0.254 (n=1777)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5185 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `1.2304` → IC=+0.201 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2304 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` < `0.9159` → IC=+0.203 (n=1977)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9159 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.807` → IC=+0.262 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.807 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` > `1.2332` → IC=+0.233 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2332 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.2826` → IC=+0.262 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2826 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `2.2043` → IC=+0.195 (n=1402)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.2043 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `1.4328` → IC=+0.196 (n=1593)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4328 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=1067)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.138 (n=2948)

- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.159 (n=2479)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0093 (IC base=+0.150)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.151 (n=2517)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0056 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.5228` → IC=+0.159 (n=2817)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.5228 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.156 (n=944)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 18.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.166 (n=1260)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 6.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.9429` → IC=+0.212 (n=939)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9429 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1902` → IC=+0.156 (n=1029)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1902 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.4998` → IC=+0.143 (n=1691)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.4998 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.129` → IC=+0.180 (n=458)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 10.129 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` > `0.9013` → IC=+0.163 (n=1204)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.9013 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.1723` → IC=+0.183 (n=771)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1723 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `1.4563` → IC=+0.158 (n=928)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.4563 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.8854` → IC=+0.162 (n=1855)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.8854 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `3708.1619` → IC=+0.153 (n=1878)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3708.1619 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.195 (n=742)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0038 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.4871` → IC=+0.155 (n=2223)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4871 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=811)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.164 (n=754)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 4.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.184` → IC=+0.166 (n=978)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.184 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.6922` → IC=+0.149 (n=428)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.6922 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.4318` → IC=+0.129 (n=2197)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.4318 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.22` → IC=+0.145 (n=2214)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 6.22 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.2456` → IC=+0.141 (n=2121)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.2456 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.0724` → IC=+0.144 (n=1030)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.0724 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.5361` → IC=+0.146 (n=966)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.5361 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.8143` → IC=+0.142 (n=1463)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.8143 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=2948)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `6937.818` → IC=+0.150 (n=1986)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 6937.818 (IC base=+0.136)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.169 (n=330)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0056 (IC base=+0.151)

- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.177 (n=125)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0065 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.0895` → IC=+0.188 (n=126)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.0895 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.159 (n=376)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.5413` → IC=+0.191 (n=250)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.5413 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `0.3825` → IC=+0.156 (n=364)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.3825 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.399` → IC=+0.163 (n=398)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 2.399 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` > `0.8487` → IC=+0.186 (n=250)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 0.8487 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.3101` → IC=+0.286 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3101 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `1.4419` → IC=+0.185 (n=125)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.4419 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `2.6734` → IC=+0.209 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6734 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `12451.0907` → IC=+0.191 (n=335)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 12451.0907 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.212 (n=408)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.1116` → IC=+0.172 (n=407)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1116 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.179 (n=350)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.172 (n=352)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 5.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.1382` → IC=+0.175 (n=407)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.1382 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.6084` → IC=+0.142 (n=420)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.6084 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.6984` → IC=+0.151 (n=84)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.6984 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.2186` → IC=+0.138 (n=947)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.2186 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.369` → IC=+0.159 (n=904)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 6.369 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.8812` → IC=+0.183 (n=617)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.8812 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.0693` → IC=+0.165 (n=434)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0693 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.422` → IC=+0.145 (n=308)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.422 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.8194` → IC=+0.147 (n=615)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.8194 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `11389.4654` → IC=+0.148 (n=925)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 11389.4654 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `707.0` → IC=+0.144 (n=880)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 707.0 (IC base=+0.136)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.186 (n=208)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.006 (IC base=+0.165)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.181 (n=283)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0099 (IC base=+0.165)

- **PATRÓN** `drift_60min` |x|≤ `0.5715` → IC=+0.174 (n=623)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.5715 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.222 (n=232)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.994` → IC=+0.233 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.994 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.706` → IC=+0.225 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.706 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` < `0.3499` → IC=+0.170 (n=749)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` < 0.3499 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.2084` → IC=+0.204 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2084 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `3.3904` → IC=+0.167 (n=622)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 3.3904 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` > `2.2621` → IC=+0.171 (n=414)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.2621 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `2425.929` → IC=+0.198 (n=283)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2425.929 (IC base=+0.165)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.312 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.254)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.262 (n=40)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.254)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.262 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.254)

- **PATRÓN** `ibs_20min` > `0.4722` → IC=+0.312 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4722 (IC base=+0.254)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.213` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.213 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` < `0.1317` → IC=+0.273 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1317 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` > `0.1037` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1037 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` < `2.5115` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5115 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` > `3.6446` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.6446 (IC base=+0.254)

- **PATRÓN** `libro_liquidez` > `2362.106` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2362.106 (IC base=+0.254)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.256 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 25.0 (IC base=+0.254)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.162 (n=867)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0044 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.1256` → IC=+0.156 (n=289)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1256 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.166 (n=342)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.168 (n=302)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 4.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.5618` → IC=+0.159 (n=578)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.5618 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.8892` → IC=+0.170 (n=289)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.8892 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.9899` → IC=+0.163 (n=197)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.9899 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.427` → IC=+0.167 (n=802)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.427 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.684` → IC=+0.161 (n=869)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 6.684 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `0.6357` → IC=+0.153 (n=289)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6357 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` > `0.7181` → IC=+0.157 (n=774)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.7181 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` < `0.1108` → IC=+0.157 (n=799)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.1108 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.1721` → IC=+0.159 (n=253)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.1721 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `1.4338` → IC=+0.163 (n=283)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.4338 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.159 (n=846)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.154 (n=730)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0084 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.3914` → IC=+0.171 (n=642)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.3914 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=259)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.148 (n=512)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 11.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.7466` → IC=+0.141 (n=730)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.7466 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.103` → IC=+0.151 (n=729)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.103 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.6351` → IC=+0.171 (n=165)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.6351 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.3872` → IC=+0.139 (n=738)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.3872 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.768` → IC=+0.158 (n=118)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 10.768 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.266` → IC=+0.140 (n=662)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 4.266 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.6452` → IC=+0.167 (n=244)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.6452 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `0.7274` → IC=+0.142 (n=652)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.7274 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.0735` → IC=+0.167 (n=307)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0735 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.1958` → IC=+0.151 (n=629)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.1958 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.7829` → IC=+0.151 (n=476)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.7829 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `7593.8032` → IC=+0.162 (n=729)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 7593.8032 (IC base=+0.139)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `ibs_20min` > `0.9615` → IC=+0.214 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9615 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.1976` → IC=+0.126 (n=145)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` > 0.1976 (IC base=+0.088)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.218` → IC=+0.181 (n=45)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 9.218 (IC base=+0.088)

- **PATRÓN** `volumen_pendiente_norm` > `0.1587` → IC=+0.206 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1587 (IC base=+0.088)

- **PATRÓN** `libro_liquidez` > `3427.7149` → IC=+0.144 (n=189)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 3427.7149 (IC base=+0.088)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.143 (n=208)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` > 0.0069 (IC base=+0.108)

- **PATRÓN** `drift_60min` |x|≤ `0.3981` → IC=+0.152 (n=139)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.3981 (IC base=+0.108)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.155 (n=140)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 10.0 (IC base=+0.108)

- **PATRÓN** `ibs_20min` < `0.1429` → IC=+0.208 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1429 (IC base=+0.108)

- **PATRÓN** `dist_vwap_pct` > `0.6223` → IC=+0.180 (n=98)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.6223 (IC base=+0.108)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.711` → IC=+0.136 (n=116)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 2.711 (IC base=+0.108)

- **PATRÓN** `volumen_pendiente_norm` < `0.089` → IC=+0.165 (n=159)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` < 0.089 (IC base=+0.108)

- **PATRÓN** `volumen_spike_ratio` < `1.867` → IC=+0.125 (n=134)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.867 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `3279.9138` → IC=+0.141 (n=207)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 3279.9138 (IC base=+0.108)

- **PATRÓN** `ballena_activa_n` < `61.0` → IC=+0.151 (n=196)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 61.0 (IC base=+0.108)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0068` → IC=-0.214 (n=117)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=355)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.187 (n=113)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=359)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.196 (n=390)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.004 (IC base=+0.098)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.130 (n=824)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 8.0 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.6781` → IC=+0.207 (n=707)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6781 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `0.1546` → IC=+0.160 (n=436)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1546 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.443` → IC=+0.222 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.443 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` > `0.9805` → IC=+0.137 (n=359)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.9805 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` > `0.2825` → IC=+0.199 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2825 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` < `2.0813` → IC=+0.140 (n=598)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.0813 (IC base=+0.098)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.124 (n=637)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `2424.4386` → IC=+0.149 (n=348)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 2424.4386 (IC base=+0.098)

- **PATRÓN** `ibs_20min` < `0.057` → IC=+0.268 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.057 (IC base=+0.002)

- **PATRÓN** `dist_vwap_pct` < `0.1871` → IC=+0.122 (n=305)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.1871 (IC base=+0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.0706` → IC=+0.207 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0706 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` < `2.5523` → IC=+0.135 (n=220)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.5523 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` > `1.4444` → IC=+0.136 (n=196)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4444 (IC base=+0.002)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.167 (n=301)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.006 (IC base=+0.110)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.126 (n=316)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.110)

- **PATRÓN** `ibs_20min` > `0.5273` → IC=+0.191 (n=270)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.5273 (IC base=+0.110)

- **PATRÓN** `dist_vwap_pct` > `0.1366` → IC=+0.183 (n=143)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1366 (IC base=+0.110)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.581` → IC=+0.134 (n=162)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 3.581 (IC base=+0.110)

- **PATRÓN** `volumen_regimen` < `1.0669` → IC=+0.125 (n=238)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 1.0669 (IC base=+0.110)

- **PATRÓN** `volumen_pendiente_norm` < `0.0678` → IC=+0.142 (n=205)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` < 0.0678 (IC base=+0.110)

- **PATRÓN** `volumen_pendiente_norm` > `0.2867` → IC=+0.149 (n=35)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2867 (IC base=+0.110)

- **PATRÓN** `volumen_spike_ratio` < `2.0129` → IC=+0.180 (n=204)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 2.0129 (IC base=+0.110)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.126 (n=279)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `4075.5853` → IC=+0.147 (n=117)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 4075.5853 (IC base=+0.110)

- **PATRÓN** `ibs_20min` < `0.279` → IC=+0.223 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.279 (IC base=+0.051)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.732` → IC=+0.160 (n=101)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` < 4.732 (IC base=+0.051)

- **PATRÓN** `volumen_regimen` < `0.6023` → IC=+0.174 (n=41)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6023 (IC base=+0.051)

- **PATRÓN** `volumen_pendiente_norm` > `0.0709` → IC=+0.229 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0709 (IC base=+0.051)

- **PATRÓN** `volumen_spike_ratio` < `2.3433` → IC=+0.170 (n=98)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 2.3433 (IC base=+0.051)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0062` → IC=-0.237 (n=36)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0062
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=111)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=112)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.160 (n=201)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0051 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.142 (n=269)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 8.0 (IC base=+0.105)

- **PATRÓN** `ibs_20min` > `0.6839` → IC=+0.230 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6839 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.3437` → IC=+0.170 (n=110)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.3437 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.016` → IC=+0.315 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.016 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` > `0.9558` → IC=+0.140 (n=123)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.9558 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` > `0.2835` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2835 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` < `1.7354` → IC=+0.164 (n=147)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.7354 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.126 (n=180)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `1767.0561` → IC=+0.192 (n=89)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 1767.0561 (IC base=+0.105)

- **PATRÓN** `ibs_20min` < `0.1419` → IC=+0.281 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1419 (IC base=-0.017)

- **PATRÓN** `dist_vwap_pct` < `0.1269` → IC=+0.130 (n=90)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.1269 (IC base=-0.017)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.838` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.838 (IC base=-0.017)

- **PATRÓN** `volumen_pendiente_norm` > `0.1363` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1363 (IC base=-0.017)

- **PATRÓN** `volumen_spike_ratio` > `2.3094` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.3094 (IC base=-0.017)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.138 (n=78)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.02 (IC base=-0.017)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `ibs_20min` > `0.0714` → IC=-0.245 (n=45)

  - _Acción_: SKIP cuando `ibs_20min` > 0.0714
  - _Potencial_: sin este filtro IC_bueno=+0.276 (n=47)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.127 (n=124)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0061 (IC base=+0.076)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.134 (n=200)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 13.0 (IC base=+0.076)

- **PATRÓN** `ibs_20min` > `0.6744` → IC=+0.178 (n=225)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.6744 (IC base=+0.076)

- **PATRÓN** `dist_vwap_pct` > `0.1982` → IC=+0.158 (n=144)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1982 (IC base=+0.076)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.379` → IC=+0.186 (n=100)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 5.379 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` > `1.0639` → IC=+0.163 (n=84)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 1.0639 (IC base=+0.076)

- **PATRÓN** `volumen_pendiente_norm` > `0.2443` → IC=+0.180 (n=48)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2443 (IC base=+0.076)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.123 (n=67)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0075 (IC base=-0.048)

- **PATRÓN** `ibs_20min` < `0.0714` → IC=+0.276 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0714 (IC base=-0.048)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.202` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.202 (IC base=-0.048)

- **PATRÓN** `volumen_pendiente_norm` > `0.1002` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1002 (IC base=-0.048)

- **PATRÓN** `volumen_spike_ratio` < `2.5975` → IC=+0.135 (n=50)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.5975 (IC base=-0.048)

- **PATRÓN** `volumen_spike_ratio` > `1.3803` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.3803 (IC base=-0.048)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `9.0` → IC=-0.396 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=148)

- **FILTRO** `dist_vwap_pct` > `0.2402` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2402
  - _Potencial_: sin este filtro IC_bueno=-0.213 (n=179)

- **FILTRO** `volumen_regimen` < `0.7468` → IC=-0.348 (n=64)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7468
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=130)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.379 (n=56)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.246 (n=112)

- **FILTRO** `dist_vwap_pct` > `0.4139` → IC=-0.413 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4139
  - _Potencial_: sin este filtro IC_bueno=-0.272 (n=147)

- **FILTRO** `sigma_ewma_delta_pct` > `8.488` → IC=-0.306 (n=29)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.488
  - _Potencial_: sin este filtro IC_bueno=-0.287 (n=139)

- **FILTRO** `volumen_pendiente_norm` > `0.0895` → IC=-0.389 (n=16)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0895
  - _Potencial_: sin este filtro IC_bueno=-0.283 (n=67)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=53)

- **FILTRO** `ibs_20min` < `0.0329` → IC=-0.250 (n=22)

  - _Acción_: SKIP cuando `ibs_20min` < 0.0329
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=46)

- **FILTRO** `volumen_regimen` < `0.8127` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8127
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=51)

- **FILTRO** `sigma_h` < `0.002` → IC=-0.292 (n=22)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.002
  - _Potencial_: sin este filtro IC_bueno=-0.235 (n=47)

- **FILTRO** `dist_vwap_pct` < `0.0689` → IC=-0.309 (n=40)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0689
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=29)

- **FILTRO** `sigma_ewma_delta_pct` > `5.128` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.128
  - _Potencial_: sin este filtro IC_bueno=-0.245 (n=49)

- **FILTRO** `volumen_regimen` > `0.9309` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.9309
  - _Potencial_: sin este filtro IC_bueno=-0.222 (n=52)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.8798` → IC=-0.409 (n=42)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8798
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=23)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.350 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.225 (n=38)

- **FILTRO** `ibs_20min` > `0.6404` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6404
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=29)

- **FILTRO** `dist_vwap_pct` < `0.2294` → IC=-0.276 (n=47)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.2294
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `drift_60min` |x|> `0.2109` → IC=-0.409 (n=20)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2109
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=40)

- **FILTRO** `volumen_spike_ratio` > `2.138` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.138
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=19)

- **FILTRO** `dist_vwap_pct` < `0.1871` → IC=-0.370 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1871
  - _Potencial_: sin este filtro IC_bueno=-0.292 (n=22)

- **FILTRO** `volumen_regimen` < `1.1043` → IC=-0.433 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.1043
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=15)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `dist_vwap_pct` > `0.6357` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.6357
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=323)

- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.143 (n=113)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0057 (IC base=+0.090)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.142 (n=118)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 15.0 (IC base=+0.090)

- **PATRÓN** `ibs_20min` > `0.6522` → IC=+0.160 (n=248)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.6522 (IC base=+0.090)

- **PATRÓN** `dist_vwap_pct` > `0.4967` → IC=+0.183 (n=58)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.4967 (IC base=+0.090)

- **PATRÓN** `volumen_spike_ratio` < `1.396` → IC=+0.135 (n=50)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.396 (IC base=+0.090)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.007` → IC=+0.136 (n=108)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 6.007 (IC base=+0.040)

- **PATRÓN** `libro_liquidez` > `3771.3449` → IC=+0.153 (n=119)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3771.3449 (IC base=+0.040)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.576` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `ibs_20min` < 0.576
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=82)

- **FILTRO** `volumen_regimen` < `0.7924` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7924
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=82)

- **PATRÓN** `drift_60min` |x|≤ `0.2285` → IC=+0.141 (n=101)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.2285 (IC base=+0.106)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.154 (n=53)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.106)

- **PATRÓN** `ibs_20min` < `0.1218` → IC=+0.182 (n=105)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.1218 (IC base=+0.106)

- **PATRÓN** `volumen_pendiente_norm` < `0.1813` → IC=+0.152 (n=87)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.1813 (IC base=+0.106)

- **PATRÓN** `volumen_spike_ratio` < `2.9499` → IC=+0.144 (n=88)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.9499 (IC base=+0.106)

- **PATRÓN** `volumen_spike_ratio` > `1.4478` → IC=+0.129 (n=87)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.4478 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `3574.4675` → IC=+0.161 (n=119)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 3574.4675 (IC base=+0.106)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `libro_liquidez` < `1549.4073` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_liquidez` < 1549.4073
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=56)

- **FILTRO** `ibs_20min` > `0.3114` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `ibs_20min` > 0.3114
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=84)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.162 (n=63)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0042 (IC base=+0.065)

- **PATRÓN** `drift_60min` |x|≤ `0.2855` → IC=+0.131 (n=63)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.2855 (IC base=+0.065)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.250 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.065)

- **PATRÓN** `ibs_20min` > `0.7272` → IC=+0.146 (n=63)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.7272 (IC base=+0.065)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=56)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.065)

- **PATRÓN** `libro_liquidez` > `1549.4073` → IC=+0.155 (n=56)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 1549.4073 (IC base=+0.065)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.321` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.321 (IC base=+0.004)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.2` → IC=-0.167 (n=37)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=42)

- **FILTRO** `volumen_regimen` < `1.0341` → IC=-0.159 (n=39)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.0341
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=40)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.203 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.193)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.214 (n=47)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.220 (n=98)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.192 (n=102)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 17.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` < `0.9714` → IC=+0.222 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.9714 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` > `0.6943` → IC=+0.328 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6943 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.688` → IC=+0.234 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.688 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` < `0.7968` → IC=+0.278 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7968 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.166` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.166 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` < `1.3956` → IC=+0.400 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3956 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.195 (n=80)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.06 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.0772` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0772 (IC base=-0.043)

### LATE_WINDOW_5MIN
- **PATRÓN** `drift_ventana_pct` |x|> `0.4605` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4605 (IC base=+0.288)

- **PATRÓN** `elapsed_s` > `210.1` → IC=+0.389 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 210.1 (IC base=+0.288)

- **PATRÓN** `drift_15min` |x|≤ `1.1328` → IC=+0.447 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.1328 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.8446` → IC=+0.361 (n=34)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8446 (IC base=+0.288)

- **PATRÓN** `ballena_activa_n` < `1559.0` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1559.0 (IC base=+0.288)

- **PATRÓN** `elapsed_s` > `193.3` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 193.3 (IC base=+0.202)

- **PATRÓN** `drift_15min` |x|≤ `2.414` → IC=+0.250 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.414 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.6484` → IC=+0.300 (n=23)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6484 (IC base=+0.202)

- **PATRÓN** `ballena_activa_n` < `1770.0` → IC=+0.250 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1770.0 (IC base=+0.202)

### LATE_WINDOW_5MIN#BTC#5min
- **PATRÓN** `drift_ventana_pct` |x|> `0.4605` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4605 (IC base=+0.288)

- **PATRÓN** `elapsed_s` > `210.1` → IC=+0.389 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 210.1 (IC base=+0.288)

- **PATRÓN** `drift_15min` |x|≤ `1.1328` → IC=+0.447 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.1328 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.8446` → IC=+0.361 (n=34)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8446 (IC base=+0.288)

- **PATRÓN** `ballena_activa_n` < `1559.0` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1559.0 (IC base=+0.288)

- **PATRÓN** `elapsed_s` > `193.3` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 193.3 (IC base=+0.202)

- **PATRÓN** `drift_15min` |x|≤ `2.414` → IC=+0.250 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.414 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.6484` → IC=+0.300 (n=23)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6484 (IC base=+0.202)

- **PATRÓN** `ballena_activa_n` < `1770.0` → IC=+0.250 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1770.0 (IC base=+0.202)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `libro_liquidez` > `2909.492` → IC=+0.165 (n=228)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2909.492 (IC base=+0.103)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2909.492` → IC=+0.165 (n=228)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2909.492 (IC base=+0.103)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `10.0` → IC=-0.204 (n=69)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=78)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=131)

- **FILTRO** `libro_liquidez` < `2415.4574` → IC=-0.263 (n=36)

  - _Acción_: SKIP cuando `libro_liquidez` < 2415.4574
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=111)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=206)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=192)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=36)

- **FILTRO** `liq_n` < `4.0` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `liq_n` < 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=19)

- **FILTRO** `libro_liquidez` < `15479.8554` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `libro_liquidez` < 15479.8554
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=15)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

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
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=1715)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9583` → IC=-0.295 (n=37)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9583
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=76)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

- **FILTRO** `ballena_activa_n` > `558.0` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `ballena_activa_n` > 558.0
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=60)

### LIQUIDACIONES_5M#BNB#5min
- **PATRÓN** `hora_utc` < `14.0` → IC=+0.127 (n=65)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 14.0 (IC base=+0.045)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.147 (n=32)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 25.0 (IC base=+0.045)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_usd_total` < `29085.84` → IC=-0.167 (n=43)

  - _Acción_: SKIP cuando `liq_usd_total` < 29085.84
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=130)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=19)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.167 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=12)

- **FILTRO** `libro_liquidez` < `15405.8709` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 15405.8709
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `ballena_activa_n` > `569.0` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `ballena_activa_n` > 569.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

- **PATRÓN** `liq_n` > `18.0` → IC=+0.214 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 18.0 (IC base=+0.026)

- **PATRÓN** `liq_usd_total` > `80598.37` → IC=+0.163 (n=87)

  - _Acción_: Kelly boost +0.81€ cuando `liq_usd_total` > 80598.37 (IC base=+0.026)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.151 (n=84)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` < 0.495 (IC base=+0.026)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=759)

- **FILTRO** `liq_usd_total` < `9664.41` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `liq_usd_total` < 9664.41
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9593` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9593
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=16)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=427)

- **FILTRO** `liq_n` < `8.0` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `liq_n` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **FILTRO** `liq_usd_total` < `24810.11` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `liq_usd_total` < 24810.11
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

### LIQUIDACIONES_5M#XRP#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=146)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.123 (n=75)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=87)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=622)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=622)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.143 (n=208)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=494)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=339)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=339)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.148 (n=86)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=268)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=172)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=172)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=107)

- **FILTRO** `hora_utc` > `9.0` → IC=-0.122 (n=72)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=42)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=99)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=199)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=78)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=81)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=236)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=236)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=122)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.189 (n=104)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=255)

- **FILTRO** `restante_min` < `3.32` → IC=-0.159 (n=89)

  - _Acción_: SKIP cuando `restante_min` < 3.32
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=270)

- **PATRÓN** `py_entrada` < `0.47` → IC=+0.196 (n=100)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.47 (IC base=+0.034)

- **PATRÓN** `profundidad_ratio` > `49.3` → IC=+0.154 (n=134)

  - _Acción_: Kelly boost +0.77€ cuando `profundidad_ratio` > 49.3 (IC base=+0.034)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **PATRÓN** `py_entrada` < `0.56` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.56 (IC base=+0.082)

- **PATRÓN** `restante_min` > `11.01` → IC=+0.132 (n=36)

  - _Acción_: Kelly boost +0.66€ cuando `restante_min` > 11.01 (IC base=+0.082)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.132 (n=36)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 11.0 (IC base=+0.082)

- **PATRÓN** `lag_apertura_s` < `232.79` → IC=+0.122 (n=35)

  - _Acción_: Kelly boost +0.61€ cuando `lag_apertura_s` < 232.79 (IC base=+0.082)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.59` → IC=+0.208 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.59 (IC base=+0.138)

- **PATRÓN** `restante_min` < `3.82` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` < 3.82 (IC base=+0.138)

- **PATRÓN** `restante_min` > `3.99` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `restante_min` > 3.99 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.300 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.224 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.138)

- **PATRÓN** `lag_apertura_s` < `60.77` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `lag_apertura_s` < 60.77 (IC base=+0.138)

- **PATRÓN** `profundidad_ratio` > `100.0` → IC=+0.223 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `profundidad_ratio` > 100.0 (IC base=+0.138)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `profundidad_ratio` < `36.6` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `profundidad_ratio` < 36.6
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=24)

- **FILTRO** `profundidad_ratio` < `60.7` → IC=-0.312 (n=30)

  - _Acción_: SKIP cuando `profundidad_ratio` < 60.7
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=10)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.58` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

- **FILTRO** `restante_min` < `13.0` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `restante_min` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=16)

- **FILTRO** `lag_apertura_s` > `120.14` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `lag_apertura_s` > 120.14
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=16)

- **FILTRO** `profundidad_ratio` < `49.3` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `profundidad_ratio` < 49.3
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=11)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `restante_min` < `3.82` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `restante_min` < 3.82
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=17)

- **FILTRO** `lag_apertura_s` > `60.81` → IC=-0.231 (n=24)

  - _Acción_: SKIP cuando `lag_apertura_s` > 60.81
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.147 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 17.0 (IC base=+0.038)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **FILTRO** `py_entrada` > `0.54` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.54
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=16)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.51` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.51
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14)

- **FILTRO** `profundidad_ratio` < `33.3` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `profundidad_ratio` < 33.3
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=21)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.232 (n=39)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=22)

- **FILTRO** `restante_min` < `2.68` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `restante_min` < 2.68
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=46)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.214 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=42)

- **FILTRO** `lag_apertura_s` > `139.44` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `lag_apertura_s` > 139.44
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=46)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=1073)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=5550)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=7430)

### MOMENTUM_IBS_15M#BTC#15min
- **FILTRO** `py_entrada` > `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=1058)

- **FILTRO** `libro_liquidez` < `15906.9303` → IC=-0.152 (n=268)

  - _Acción_: SKIP cuando `libro_liquidez` < 15906.9303
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=805)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=1413)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.47` → IC=-0.172 (n=3243)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=10476)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.168 (n=3549)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=10673)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.213 (n=590)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.101 (n=1787)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.154 (n=629)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=1920)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.200 (n=588)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=1832)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.201 (n=621)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=1922)

- **FILTRO** `ibs_20min` > `0.2814` → IC=-0.161 (n=635)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2814
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=1908)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.169 (n=587)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=1772)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.181 (n=621)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=1922)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `libro_spread` > `0.01` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=2731)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=2902)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=2908)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `ibs_20min` > `0.1705` → IC=-0.145 (n=122)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1705
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=369)

- **FILTRO** `libro_liquidez` < `15696.2813` → IC=-0.129 (n=122)

  - _Acción_: SKIP cuando `libro_liquidez` < 15696.2813
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=369)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.214 (n=68)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=241)

- **FILTRO** `ibs_20min` < `0.11` → IC=-0.234 (n=77)

  - _Acción_: SKIP cuando `ibs_20min` < 0.11
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=232)

- **FILTRO** `py_entrada` > `0.625` → IC=-0.279 (n=66)

  - _Acción_: SKIP cuando `py_entrada` > 0.625
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=234)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.227 (n=192)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=584)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=223)

### MOMENTUM_IBS_5M#BNB#5min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=40)

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

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.179 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 15.0 (IC base=+0.032)

### MOMENTUM_IBS_5M#DOGE#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=38)

### MOMENTUM_IBS_5M#ETH#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=414)

### MOMENTUM_IBS_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=631)

### MOMENTUM_IBS_5M_BALLENA
- **FILTRO** `hora_utc` < `8.0` → IC=-0.129 (n=9688)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=21845)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.273 (n=7695)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=23838)

- **FILTRO** `ibs_7min` < `0.2857` → IC=-0.235 (n=7864)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=23669)

- **FILTRO** `ballena_activa_n` > `16.0` → IC=-0.158 (n=10434)

  - _Acción_: SKIP cuando `ballena_activa_n` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=21099)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.229 (n=9707)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=29749)

- **FILTRO** `ibs_7min` > `0.2934` → IC=-0.179 (n=9863)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2934
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=29593)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.305 (n=1241)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=3964)

- **FILTRO** `ibs_7min` < `0.7099` → IC=-0.249 (n=1717)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7099
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=3488)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.185 (n=1200)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=4005)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.260 (n=1678)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=5105)

- **FILTRO** `drift_7min_pct` |x|> `0.1119` → IC=-0.124 (n=2305)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1119
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=4478)

- **FILTRO** `ibs_7min` > `0.7913` → IC=-0.205 (n=1695)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7913
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=5088)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.137 (n=1265)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=4186)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.250 (n=1308)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=4143)

- **FILTRO** `ibs_7min` < `0.7483` → IC=-0.192 (n=1362)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7483
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=4089)

- **FILTRO** `ballena_activa_n` > `161.0` → IC=-0.171 (n=1356)

  - _Acción_: SKIP cuando `ballena_activa_n` > 161.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=4095)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.254 (n=1370)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=4148)

- **FILTRO** `ibs_7min` > `0.2605` → IC=-0.176 (n=1379)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2605
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=4139)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.184 (n=1375)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=4143)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.167 (n=1211)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=3720)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.307 (n=1210)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=3721)

- **FILTRO** `ibs_7min` < `0.1935` → IC=-0.258 (n=1227)

  - _Acción_: SKIP cuando `ibs_7min` < 0.1935
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=3704)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.220 (n=1157)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=3774)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.237 (n=1663)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=5583)

- **FILTRO** `ibs_7min` > `0.7474` → IC=-0.178 (n=1811)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7474
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=5435)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.37` → IC=-0.232 (n=1536)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=3666)

- **FILTRO** `ibs_7min` < `0.742` → IC=-0.181 (n=1299)

  - _Acción_: SKIP cuando `ibs_7min` < 0.742
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=3903)

- **FILTRO** `ballena_activa_n` > `32.0` → IC=-0.169 (n=1287)

  - _Acción_: SKIP cuando `ballena_activa_n` > 32.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=3915)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.266 (n=1174)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=4118)

- **FILTRO** `ibs_7min` > `0.2748` → IC=-0.174 (n=1322)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2748
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=3970)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.186 (n=1320)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=3972)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.36` → IC=-0.261 (n=1331)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=4179)

- **FILTRO** `ibs_7min` < `0.7` → IC=-0.241 (n=1369)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=4141)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.178 (n=1794)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=5711)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.38` → IC=-0.253 (n=1687)

  - _Acción_: SKIP cuando `py_entrada` < 0.38
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=3547)

- **FILTRO** `ibs_7min` < `0.7` → IC=-0.227 (n=1295)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=3939)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.214 (n=1272)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=3962)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.203 (n=1709)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=5403)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=1060)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=527)

### MOMENTUM_IBS_5M_FADE#DOGE#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=596)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=1022)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=323)

- **FILTRO** `ballena_activa_n` > `2.0` → IC=-0.138 (n=139)

  - _Acción_: SKIP cuando `ballena_activa_n` > 2.0
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=286)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=551)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=436)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4164` → IC=+0.142 (n=484)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.71€ cuando `delta_ratio` |x|> 0.4164 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.127 (n=333)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 14.0 (IC base=+0.111)

- **PATRÓN** `total_vol_5m` < `469.512` → IC=+0.145 (n=243)

  - _Acción_: Kelly boost +0.72€ cuando `total_vol_5m` < 469.512 (IC base=+0.111)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4382` → IC=+0.144 (n=57)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio` |x|> 0.4382 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=176)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.129)

- **PATRÓN** `total_vol_5m` < `445.688` → IC=+0.138 (n=150)

  - _Acción_: Kelly boost +0.69€ cuando `total_vol_5m` < 445.688 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.149 (n=55)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 12.0 (IC base=+0.129)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.121 (n=101)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 10.0 (IC base=+0.093)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.131 (n=63)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 13.0 (IC base=+0.093)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4131` → IC=+0.180 (n=98)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio` |x|> 0.4131 (IC base=+0.094)

- **PATRÓN** `total_vol_5m` < `394.71` → IC=+0.202 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 394.71 (IC base=+0.094)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.167 (n=49)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 69.0 (IC base=+0.094)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3985` → IC=+0.164 (n=129)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.82€ cuando `delta_ratio` |x|> 0.3985 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.192 (n=89)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.130)

- **PATRÓN** `total_vol_5m` < `6300.756` → IC=+0.161 (n=113)

  - _Acción_: Kelly boost +0.80€ cuando `total_vol_5m` < 6300.756 (IC base=+0.130)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.3998` → IC=+0.148 (n=126)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.74€ cuando `delta_ratio` |x|> 0.3998 (IC base=+0.105)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.139 (n=128)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 13.0 (IC base=+0.105)

- **PATRÓN** `total_vol_5m` < `262739.3` → IC=+0.149 (n=95)

  - _Acción_: Kelly boost +0.75€ cuando `total_vol_5m` < 262739.3 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.223 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `3566.692` → IC=+0.182 (n=64)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 3566.692 (IC base=+0.105)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` > `0.0071` → IC=-0.327 (n=125)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0071
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=245)

- **FILTRO** `T_h` > `51.6999` → IC=-0.243 (n=247)

  - _Acción_: SKIP cuando `T_h` > 51.6999
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=123)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `51.365` → IC=-0.347 (n=57)

  - _Acción_: SKIP cuando `T_h` > 51.365
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=58)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.175 (n=38)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0053 (IC base=-0.133)

- **PATRÓN** `T_h` < `39.9942` → IC=+0.125 (n=38)

  - _Acción_: Kelly boost +0.62€ cuando `T_h` < 39.9942 (IC base=-0.133)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0107` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0107
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=20)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0127` → IC=-0.208 (n=22)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0127
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=44)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `pct_vs_K` |x|> `2.7902` → IC=-0.237 (n=184)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.7902
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=189)

- **FILTRO** `pct_vs_K` |x|> `3.325` → IC=-0.436 (n=108)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.325
  - _Potencial_: sin este filtro IC_bueno=-0.234 (n=212)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.004` → IC=-0.206 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.004
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=99)

- **FILTRO** `pct_vs_K` |x|> `2.9087` → IC=-0.353 (n=32)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9087
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=99)

- **FILTRO** `T_h` < `96.6729` → IC=-0.375 (n=38)

  - _Acción_: SKIP cuando `T_h` < 96.6729
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=79)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `T_h` > `135.9558` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `T_h` > 135.9558
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=79)

- **FILTRO** `pct_vs_K` |x|> `2.4229` → IC=-0.352 (n=52)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.4229
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=53)

- **FILTRO** `sigma_h` > `0.0094` → IC=-0.315 (n=25)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0094
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=78)

- **FILTRO** `sigma_h` < `0.0045` → IC=-0.352 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0045
  - _Potencial_: sin este filtro IC_bueno=-0.225 (n=78)

- **FILTRO** `T_h` > `49.1198` → IC=-0.310 (n=77)

  - _Acción_: SKIP cuando `T_h` > 49.1198
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=26)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0082` → IC=-0.177 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0082
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=59)

- **FILTRO** `T_h` > `133.4167` → IC=-0.210 (n=29)

  - _Acción_: SKIP cuando `T_h` > 133.4167
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=59)

- **FILTRO** `pct_vs_K` |x|> `5.0091` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 5.0091
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=67)

- **FILTRO** `sigma_h` < `0.0156` → IC=-0.360 (n=48)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0156
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=16)

- **FILTRO** `T_h` > `63.3218` → IC=-0.378 (n=47)

  - _Acción_: SKIP cuando `T_h` > 63.3218
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=17)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1255` → IC=+0.464 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1255 (IC base=+0.381)

- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.447 (n=36)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.381)

- **PATRÓN** `T_h` > `0.4742` → IC=+0.430 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4742 (IC base=+0.381)

- **PATRÓN** `dist_50` > `0.4444` → IC=+0.474 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4444 (IC base=+0.381)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.433 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.381)

- **PATRÓN** `edge` > `0.096` → IC=+0.456 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.096 (IC base=+0.417)

- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.456 (n=89)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0095 (IC base=+0.417)

- **PATRÓN** `T_h` < `0.639` → IC=+0.458 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.639 (IC base=+0.417)

- **PATRÓN** `T_h` > `1.4774` → IC=+0.438 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4774 (IC base=+0.417)

- **PATRÓN** `dist_50` > `0.3938` → IC=+0.485 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3938 (IC base=+0.417)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.467 (n=88)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.417)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1078` → IC=+0.443 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1078 (IC base=+0.407)

- **PATRÓN** `sigma_h` < `0.0088` → IC=+0.389 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0088 (IC base=+0.407)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.450 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.407)

- **PATRÓN** `T_h` < `0.9672` → IC=+0.441 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.9672 (IC base=+0.407)

- **PATRÓN** `T_h` > `0.5243` → IC=+0.386 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.5243 (IC base=+0.407)

- **PATRÓN** `dist_50` > `0.4122` → IC=+0.471 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4122 (IC base=+0.407)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.407)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.423 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.407)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.225` → IC=+0.471 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.225 (IC base=+0.481)

- **PATRÓN** `sigma_h` < `0.0138` → IC=+0.471 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0138 (IC base=+0.481)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.471 (n=33)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.481)

- **PATRÓN** `T_h` > `0.8566` → IC=+0.471 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8566 (IC base=+0.481)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.463 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.481)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.463 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.481)

- **PATRÓN** `edge` > `0.096` → IC=+0.478 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.096 (IC base=+0.469)

- **PATRÓN** `sigma_h` < `0.0162` → IC=+0.478 (n=88)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0162 (IC base=+0.469)

- **PATRÓN** `T_h` > `1.2464` → IC=+0.467 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.2464 (IC base=+0.469)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.488 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.469)

- **PATRÓN** `hora_utc` < `2.0` → IC=+0.476 (n=39)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 2.0 (IC base=+0.469)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=168)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=286)

- **PATRÓN** `streak_estiramiento` < `0.4117` → IC=+0.167 (n=43)

  - _Acción_: Kelly boost +0.83€ cuando `streak_estiramiento` < 0.4117 (IC base=+0.041)

- **PATRÓN** `streak_estiramiento` < `0.5637` → IC=+0.164 (n=123)

  - _Acción_: Kelly boost +0.82€ cuando `streak_estiramiento` < 0.5637 (IC base=+0.037)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.206 (n=15)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.000)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `volumen_racha` > `990711.2` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `volumen_racha` > 990711.2
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=27)

- **PATRÓN** `volumen_racha` < `990711.2` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_racha` < 990711.2 (IC base=+0.000)

- **PATRÓN** `streak_estiramiento` < `0.4152` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `streak_estiramiento` < 0.4152 (IC base=+0.000)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 52.0 (IC base=+0.000)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.122 (n=88)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 49.0 (IC base=+0.051)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.219 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=78)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=88)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=36)

- **FILTRO** `streak_estiramiento` > `1.1202` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_estiramiento` > 1.1202
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=31)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=24)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=749)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=755)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=389)

### STREAK_FADE_60M
- **FILTRO** `hora_utc` > `3.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=14)

- **FILTRO** `libro_liquidez` < `2775.6672` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_liquidez` < 2775.6672
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### STREAK_FADE_60M#ETH#60min
- **FILTRO** `hora_utc` > `5.0` → IC=-0.147 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=582)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1108)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=728)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=704)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=2852)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1447)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=1455)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.219 (n=696)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0085 (IC base=+0.184)

- **PATRÓN** `drift_60min` |x|≤ `0.0748` → IC=+0.201 (n=676)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0748 (IC base=+0.184)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2127` → IC=+0.191 (n=512)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.95€ cuando `delta_ratio_macro` |x|> 0.2127 (IC base=+0.184)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1263` → IC=+0.229 (n=533)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1263 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.193 (n=1437)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 6.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.185 (n=1545)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 16.0 (IC base=+0.184)

- **PATRÓN** `ibs_15` > `0.6047` → IC=+0.262 (n=1536)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6047 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` > `0.3017` → IC=+0.190 (n=539)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.3017 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.899` → IC=+0.274 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.899 (IC base=+0.184)

- **PATRÓN** `libro_liquidez` > `2979.0729` → IC=+0.192 (n=1023)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2979.0729 (IC base=+0.184)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=573)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.211 (n=354)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.0587` → IC=+0.292 (n=118)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0587 (IC base=+0.200)

- **PATRÓN** `drift_15min` |x|≤ `0.3811` → IC=+0.208 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3811 (IC base=+0.200)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2526` → IC=+0.242 (n=118)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2526 (IC base=+0.200)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1443` → IC=+0.268 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1443 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.220 (n=373)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.200)

- **PATRÓN** `ibs_15` > `0.7036` → IC=+0.267 (n=354)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7036 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` > `0.4048` → IC=+0.252 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4048 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.537` → IC=+0.268 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.537 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `15960.6783` → IC=+0.233 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15960.6783 (IC base=+0.200)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `24.537` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 24.537
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=354)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.139 (n=120)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0036 (IC base=+0.135)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.160 (n=239)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0051 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.0688` → IC=+0.144 (n=158)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.0688 (IC base=+0.135)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2337` → IC=+0.172 (n=120)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.86€ cuando `delta_ratio_macro` |x|> 0.2337 (IC base=+0.135)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1159` → IC=+0.174 (n=127)

  - _Acción_: Kelly boost +0.87€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1159 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.148 (n=359)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.135)

- **PATRÓN** `ibs_15` > `0.662` → IC=+0.243 (n=321)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.662 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.5785` → IC=+0.138 (n=78)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.5785 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.1658` → IC=+0.152 (n=280)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1658 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.386` → IC=+0.196 (n=156)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 8.386 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `9553.1781` → IC=+0.161 (n=163)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 9553.1781 (IC base=+0.135)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.143 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=90)

- **FILTRO** `ibs_15` > `0.2175` → IC=-0.233 (n=28)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.2175
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=88)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.297 (n=62)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.1498` → IC=+0.207 (n=162)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1498 (IC base=+0.172)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0669` → IC=+0.207 (n=165)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0669 (IC base=+0.172)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2704` → IC=+0.224 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2704 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.213 (n=127)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.172)

- **PATRÓN** `ibs_15` > `0.6111` → IC=+0.258 (n=184)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6111 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.2696` → IC=+0.208 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2696 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.532` → IC=+0.400 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.532 (IC base=+0.172)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.174 (n=142)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `3056.7878` → IC=+0.279 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3056.7878 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.226 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.172)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.5723` → IC=-0.140 (n=123)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.5723
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=854)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `15.662` → IC=+0.204 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 15.662 (IC base=+0.013)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0178` → IC=+0.237 (n=272)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0178 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.0864` → IC=+0.210 (n=181)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0864 (IC base=+0.187)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0597` → IC=+0.192 (n=365)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.96€ cuando `delta_ratio_macro` |x|> 0.0597 (IC base=+0.187)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0893` → IC=+0.245 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0893 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.226 (n=202)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.187)

- **PATRÓN** `ibs_15` > `0.5488` → IC=+0.283 (n=408)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5488 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` > `0.1329` → IC=+0.209 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1329 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` < `0.7658` → IC=+0.186 (n=470)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.7658 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.928` → IC=+0.223 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.928 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.396` → IC=+0.188 (n=366)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 7.396 (IC base=+0.187)

- **PATRÓN** `libro_liquidez` > `2911.0954` → IC=+0.283 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2911.0954 (IC base=+0.187)

- **PATRÓN** `ibs_15` < `0.1176` → IC=+0.155 (n=462)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.78€ cuando `ibs_15` < 0.1176 (IC base=+0.046)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.336 (n=267)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.336)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.375 (n=182)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.336)

- **PATRÓN** `drift_60min` |x|≤ `0.1089` → IC=+0.344 (n=267)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1089 (IC base=+0.336)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1438` → IC=+0.362 (n=266)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1438 (IC base=+0.336)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1274` → IC=+0.372 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1274 (IC base=+0.336)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.384 (n=187)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.336)

- **PATRÓN** `ibs_15` > `0.7856` → IC=+0.381 (n=400)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7856 (IC base=+0.336)

- **PATRÓN** `dist_vwap_pct` > `0.4335` → IC=+0.386 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4335 (IC base=+0.336)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.188` → IC=+0.340 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.188 (IC base=+0.336)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.77` → IC=+0.336 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.77 (IC base=+0.336)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.342 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.336)

- **PATRÓN** `libro_liquidez` > `3532.3524` → IC=+0.351 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3532.3524 (IC base=+0.336)

- **PATRÓN** `ballena_activa_n` < `472.0` → IC=+0.358 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 472.0 (IC base=+0.336)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.349 (n=197)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.340)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.370 (n=75)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.340)

- **PATRÓN** `drift_60min` |x|≤ `0.0569` → IC=+0.370 (n=75)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0569 (IC base=+0.340)

- **PATRÓN** `drift_15min` |x|≤ `0.4288` → IC=+0.351 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4288 (IC base=+0.340)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1505` → IC=+0.361 (n=149)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1505 (IC base=+0.340)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1224` → IC=+0.382 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1224 (IC base=+0.340)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.367 (n=208)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.340)

- **PATRÓN** `ibs_15` > `0.8154` → IC=+0.376 (n=224)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8154 (IC base=+0.340)

- **PATRÓN** `dist_vwap_pct` > `0.4016` → IC=+0.410 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4016 (IC base=+0.340)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.997` → IC=+0.348 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.997 (IC base=+0.340)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.922` → IC=+0.344 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.922 (IC base=+0.340)

- **PATRÓN** `libro_liquidez` > `15670.1365` → IC=+0.344 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15670.1365 (IC base=+0.340)

- **PATRÓN** `ballena_activa_n` < `574.0` → IC=+0.387 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 574.0 (IC base=+0.340)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.367 (n=118)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.327)

- **PATRÓN** `drift_60min` |x|≤ `0.1058` → IC=+0.342 (n=118)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1058 (IC base=+0.327)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0897` → IC=+0.350 (n=158)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0897 (IC base=+0.327)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.357 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.327)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.394 (n=83)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.327)

- **PATRÓN** `ibs_15` > `0.7359` → IC=+0.388 (n=177)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7359 (IC base=+0.327)

- **PATRÓN** `dist_vwap_pct` > `0.4658` → IC=+0.379 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4658 (IC base=+0.327)

- **PATRÓN** `dist_vwap_pct` < `0.1256` → IC=+0.333 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1256 (IC base=+0.327)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.639` → IC=+0.342 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.639 (IC base=+0.327)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.587` → IC=+0.330 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.587 (IC base=+0.327)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.342 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.327)

- **PATRÓN** `libro_liquidez` > `3534.509` → IC=+0.350 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3534.509 (IC base=+0.327)

- **PATRÓN** `ballena_activa_n` < `164.0` → IC=+0.339 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 164.0 (IC base=+0.327)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0131` → IC=-0.219 (n=643)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0131
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=1932)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.190 (n=868)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=1707)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1365` → IC=+0.250 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1365 (IC base=-0.063)

- **PATRÓN** `ibs_15` > `0.6341` → IC=+0.268 (n=618)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6341 (IC base=-0.063)

- **PATRÓN** `dist_vwap_pct` > `0.5908` → IC=+0.175 (n=115)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.5908 (IC base=-0.063)

- **PATRÓN** `dist_vwap_pct` < `0.2788` → IC=+0.178 (n=485)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.2788 (IC base=-0.063)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0756` → IC=+0.238 (n=1492)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0756 (IC base=-0.035)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1772` → IC=+0.235 (n=1077)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1772 (IC base=-0.035)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.276 (n=1673)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.035)

- **PATRÓN** `dist_vwap_pct` > `0.6896` → IC=+0.287 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6896 (IC base=-0.035)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0068` → IC=-0.218 (n=391)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=1176)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.230 (n=391)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=1176)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.208 (n=994)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=573)

- **FILTRO** `sigma_ewma_delta_pct` > `19.563` → IC=-0.247 (n=279)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.563
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=1288)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.164 (n=147)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0028 (IC base=+0.077)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2023` → IC=+0.282 (n=76)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2023 (IC base=+0.077)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1378` → IC=+0.319 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1378 (IC base=+0.077)

- **PATRÓN** `ibs_15` > `0.7413` → IC=+0.317 (n=167)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7413 (IC base=+0.077)

- **PATRÓN** `dist_vwap_pct` > `0.102` → IC=+0.281 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.102 (IC base=+0.077)

- **PATRÓN** `dist_vwap_pct` < `0.5498` → IC=+0.274 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5498 (IC base=+0.077)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.6647` → IC=-0.200 (n=98)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6647
  - _Potencial_: sin este filtro IC_bueno=+0.264 (n=294)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=375)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.192 (n=196)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0051 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.0764` → IC=+0.212 (n=130)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0764 (IC base=+0.147)

- **PATRÓN** `drift_15min` |x|≤ `0.4246` → IC=+0.163 (n=99)

  - _Acción_: Kelly boost +0.82€ cuando `drift_15min` |x|≤ 0.4246 (IC base=+0.147)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1329` → IC=+0.157 (n=196)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.78€ cuando `delta_ratio_macro` |x|> 0.1329 (IC base=+0.147)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.288` → IC=+0.234 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.288 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.200 (n=138)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.147)

- **PATRÓN** `ibs_15` > `0.6647` → IC=+0.264 (n=294)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6647 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.4741` → IC=+0.155 (n=85)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.4741 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.1651` → IC=+0.174 (n=225)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.1651 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.024` → IC=+0.159 (n=250)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 9.024 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.161 (n=375)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `10970.2258` → IC=+0.191 (n=134)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 10970.2258 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.262 (n=221)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.4388` → IC=+0.224 (n=661)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4388 (IC base=+0.224)

- **PATRÓN** `drift_15min` |x|≤ `0.7872` → IC=+0.231 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7872 (IC base=+0.224)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2011` → IC=+0.252 (n=300)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2011 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.230 (n=257)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.240 (n=294)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.224)

- **PATRÓN** `ibs_15` < `0.2693` → IC=+0.276 (n=582)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2693 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.7744` → IC=+0.304 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7744 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.817` → IC=+0.241 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.817 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.189` → IC=+0.229 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.189 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `3551.8492` → IC=+0.224 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3551.8492 (IC base=+0.224)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1671` → IC=-0.221 (n=206)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1671
  - _Potencial_: sin este filtro IC_bueno=-0.139 (n=400)

- **FILTRO** `drift_15min` |x|> `0.8922` → IC=-0.265 (n=151)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8922
  - _Potencial_: sin este filtro IC_bueno=-0.135 (n=455)

- **PATRÓN** `ibs_15` > `0.8889` → IC=+0.342 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8889 (IC base=-0.168)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0758` → IC=+0.223 (n=269)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0758 (IC base=-0.043)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.262 (n=301)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.043)

- **PATRÓN** `dist_vwap_pct` > `0.4921` → IC=+0.211 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4921 (IC base=-0.043)

- **PATRÓN** `dist_vwap_pct` < `0.199` → IC=+0.218 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.199 (IC base=-0.043)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0199` → IC=-0.259 (n=379)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0199
  - _Potencial_: sin este filtro IC_bueno=-0.135 (n=381)

- **FILTRO** `drift_15min` |x|> `1.2406` → IC=-0.259 (n=189)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2406
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=571)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.265 (n=185)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=575)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1579` → IC=+0.276 (n=150)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1579 (IC base=-0.046)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.103` → IC=+0.348 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.103 (IC base=-0.046)

- **PATRÓN** `ibs_15` < `0.3457` → IC=+0.307 (n=449)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3457 (IC base=-0.046)

- **PATRÓN** `dist_vwap_pct` > `0.9013` → IC=+0.343 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9013 (IC base=-0.046)

### UPDOWN_GBM_ETH_15M_HORA7
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2775` → IC=-0.136 (n=20)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2775
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **FILTRO** `ibs_15` < `0.8489` → IC=-0.136 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8489
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **PATRÓN** `drift_60min` |x|≤ `0.0856` → IC=+0.200 (n=28)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0856 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` > `0.1687` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1687 (IC base=+0.054)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2775` → IC=-0.136 (n=20)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2775
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **FILTRO** `ibs_15` < `0.8489` → IC=-0.136 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8489
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **PATRÓN** `drift_60min` |x|≤ `0.0856` → IC=+0.200 (n=28)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0856 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` > `0.1687` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1687 (IC base=+0.054)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.294 (n=430)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.289)

- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.289 (n=292)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0054 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.057` → IC=+0.320 (n=215)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.057 (IC base=+0.289)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2394` → IC=+0.306 (n=214)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2394 (IC base=+0.289)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1069` → IC=+0.344 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1069 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.309 (n=675)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.8393` → IC=+0.325 (n=643)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8393 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.1581` → IC=+0.320 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1581 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.101` → IC=+0.329 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.101 (IC base=+0.289)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.293 (n=789)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `14480.7481` → IC=+0.302 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14480.7481 (IC base=+0.289)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.311 (n=120)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.282)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.287 (n=162)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.282)

- **PATRÓN** `drift_60min` |x|≤ `0.058` → IC=+0.344 (n=120)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.058 (IC base=+0.282)

- **PATRÓN** `delta_ratio_macro` |x|> `0.26` → IC=+0.302 (n=119)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.26 (IC base=+0.282)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3729` → IC=+0.303 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3729 (IC base=+0.282)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.302 (n=376)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.282)

- **PATRÓN** `ibs_15` > `0.8303` → IC=+0.313 (n=357)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8303 (IC base=+0.282)

- **PATRÓN** `dist_vwap_pct` > `0.444` → IC=+0.353 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.444 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.589` → IC=+0.355 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.589 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `16049.3542` → IC=+0.326 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16049.3542 (IC base=+0.282)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.306 (n=286)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.296)

- **PATRÓN** `drift_60min` |x|≤ `0.1127` → IC=+0.298 (n=191)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1127 (IC base=+0.296)

- **PATRÓN** `delta_ratio_macro` |x|> `0.226` → IC=+0.316 (n=96)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.226 (IC base=+0.296)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2866` → IC=+0.335 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2866 (IC base=+0.296)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.331 (n=258)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.296)

- **PATRÓN** `ibs_15` > `0.8486` → IC=+0.337 (n=286)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8486 (IC base=+0.296)

- **PATRÓN** `dist_vwap_pct` > `0.6245` → IC=+0.309 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6245 (IC base=+0.296)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.169` → IC=+0.315 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.169 (IC base=+0.296)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.308 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.296)

### UPDOWN_OU_5M
- **FILTRO** `drift_60min` |x|> `0.2656` → IC=-0.186 (n=68)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2656
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=207)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1131` → IC=-0.171 (n=68)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1131
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=207)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1209` → IC=-0.164 (n=108)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1209
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=328)

- **FILTRO** `drift_15min` |x|> `0.4327` → IC=-0.133 (n=148)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.4327
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=288)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1445` → IC=-0.148 (n=52)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1445
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=108)

- **FILTRO** `drift_15min` |x|> `0.2287` → IC=-0.262 (n=19)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.2287
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=21)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2236` → IC=-0.133 (n=28)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2236
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=15)

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.309 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2122` → IC=-0.395 (n=17)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2122
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.103` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.103
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **FILTRO** `drift_15min` |x|> `0.2131` → IC=-0.231 (n=24)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.2131
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `71.4766` → IC=+0.211 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 71.4766 (IC base=+0.198)

- **PATRÓN** `ratio` < `0.9779` → IC=+0.462 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9779 (IC base=+0.198)

- **PATRÓN** `T_h` > `145.7851` → IC=+0.394 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7851 (IC base=+0.332)

- **PATRÓN** `ratio` > `1.0088` → IC=+0.273 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0088 (IC base=+0.332)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `73.0783` → IC=+0.187 (n=129)

  - _Acción_: Kelly boost +0.94€ cuando `T_h` > 73.0783 (IC base=+0.172)

- **PATRÓN** `ratio` < `0.973` → IC=+0.442 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.172)

- **PATRÓN** `T_h` > `99.1458` → IC=+0.291 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 99.1458 (IC base=+0.281)

- **PATRÓN** `ratio` > `1.0455` → IC=+0.327 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0455 (IC base=+0.281)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `87.9957` → IC=+0.271 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.9957 (IC base=+0.242)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.413 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.242)

- **PATRÓN** `T_h` > `103.3918` → IC=+0.326 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 103.3918 (IC base=+0.308)

- **PATRÓN** `ratio` > `1.0131` → IC=+0.306 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0131 (IC base=+0.308)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1359` → IC=+0.457 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1359 (IC base=+0.403)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6047 sube el IC de +0.184 a +0.262 en UPDOWN_GBM#15min (n=1536). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7036 sube el IC de +0.200 a +0.267 en UPDOWN_GBM#BTC#15min (n=354). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.662 sube el IC de +0.135 a +0.243 en UPDOWN_GBM#ETH#15min (n=321). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6111 sube el IC de +0.172 a +0.258 en UPDOWN_GBM#SOL#15min (n=184). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5488 sube el IC de +0.187 a +0.283 en UPDOWN_GBM#XRP#15min (n=408). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1176 sube el IC de +0.046 a +0.155 en UPDOWN_GBM#XRP#15min (n=462). Ya aplicado como kelly_boost=+0.78€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6341 sube el IC de -0.063 a +0.268 en UPDOWN_GBM_15M_TARDIO (n=618). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.035 a +0.276 en UPDOWN_GBM_15M_TARDIO (n=1673). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7413 sube el IC de +0.077 a +0.317 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=167). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6647 sube el IC de +0.147 a +0.264 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=294). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.2693 sube el IC de +0.224 a +0.276 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=582). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8889 sube el IC de -0.168 a +0.342 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.043 a +0.262 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=301). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3457 sube el IC de -0.046 a +0.307 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=449). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8393 sube el IC de +0.289 a +0.325 en UPDOWN_GBM_IBS_ALTO (n=643). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8303 sube el IC de +0.282 a +0.313 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=357). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8486 sube el IC de +0.296 a +0.337 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=286). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7856 sube el IC de +0.336 a +0.381 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=400). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8154 sube el IC de +0.340 a +0.376 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=224). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7359 sube el IC de +0.327 a +0.388 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=177). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1301 | +0.098 | +190.93€ | 1 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1301 | +0.098 | +190.93€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 968 | +0.108 | +165.87€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 968 | +0.108 | +165.87€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 247 | +0.050 | +6.40€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 247 | +0.050 | +6.40€ | 6 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 60 | +0.145 | +20.16€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 60 | +0.145 | +20.16€ | 0 | 6 |
| ✅ BALLENAS_TARDIAS | 24665 | -0.091 | -3154.63€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1433 | -0.048 | -223.67€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 23232 | -0.094 | -2930.97€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3624 | -0.088 | -579.41€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3624 | -0.088 | -579.41€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1433 | -0.048 | -223.67€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1433 | -0.048 | -223.67€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 374 | -0.136 | -161.05€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 374 | -0.136 | -161.05€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 7129 | -0.023 | -652.88€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 7129 | -0.023 | -652.88€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 6602 | -0.098 | -458.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 6602 | -0.098 | -458.49€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 5503 | -0.183 | -1079.14€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 5503 | -0.183 | -1079.14€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 17468 | -0.029 | +4082.83€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 4568 | +0.000 | +1828.56€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 12900 | -0.039 | +2254.27€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 17468 | -0.029 | +4082.83€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 4568 | +0.000 | +1828.56€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 12900 | -0.039 | +2254.27€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 1469 | -0.102 | -185.83€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#15min | 168 | -0.053 | -21.36€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 1301 | -0.108 | -164.47€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB#5min | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 780 | -0.091 | -97.63€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#15min | 144 | -0.048 | -16.13€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 636 | -0.100 | -81.50€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH | 491 | -0.125 | -74.32€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#15min | 24 | -0.077 | -5.22€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#5min | 467 | -0.127 | -69.10€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL#5min | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP | 57 | -0.161 | -4.36€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP#5min | 57 | -0.161 | -4.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 90635 | +0.112 | -4653.20€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 13744 | +0.184 | -448.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 363 | -0.089 | -50.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 70603 | +0.100 | -3940.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 5925 | +0.108 | -213.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 11744 | +0.098 | -1014.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 44 | -0.174 | -3.33€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 11685 | +0.099 | -999.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 18331 | +0.132 | -383.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4315 | +0.202 | -150.56€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 11704 | +0.112 | -181.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2270 | +0.105 | -28.59€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 11784 | +0.089 | -1106.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 51 | -0.085 | -5.77€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 11718 | +0.090 | -1089.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 19295 | +0.123 | -406.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 5314 | +0.175 | -81.72€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 11826 | +0.105 | -262.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2143 | +0.098 | -54.03€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 17721 | +0.114 | -1038.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 3975 | +0.188 | -214.62€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 266 | -0.049 | +3.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 11968 | +0.091 | -696.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1512 | +0.127 | -130.91€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 11760 | +0.100 | -704.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 45 | -0.032 | +7.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 11702 | +0.101 | -711.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 14376 | +0.192 | -939.10€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 14376 | +0.192 | -939.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 3435 | +0.168 | -363.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 3435 | +0.168 | -363.05€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1154 | +0.196 | -6.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1154 | +0.196 | -6.39€ | 4 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 3378 | +0.180 | -288.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 3378 | +0.180 | -288.98€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3014 | +0.238 | -97.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3014 | +0.238 | -97.47€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 3316 | +0.193 | -196.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 3316 | +0.193 | -196.96€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 676 | +0.431 | -17.74€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 676 | +0.431 | -17.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 260 | +0.435 | -3.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 260 | +0.435 | -3.96€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 254 | +0.438 | -2.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 254 | +0.438 | -2.02€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 154 | +0.404 | -10.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 154 | +0.404 | -10.72€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 49470 | +0.197 | -3950.26€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 49470 | +0.197 | -3950.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 8571 | +0.175 | -1012.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 8571 | +0.175 | -1012.37€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 7898 | +0.222 | -300.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 7898 | +0.222 | -300.93€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 8538 | +0.172 | -1039.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 8538 | +0.172 | -1039.64€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 7994 | +0.218 | -323.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 7994 | +0.218 | -323.05€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 8169 | +0.202 | -549.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 8169 | +0.202 | -549.58€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 8300 | +0.193 | -724.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 8300 | +0.193 | -724.69€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 18636 | +0.118 | +172.89€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 18636 | +0.118 | +172.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 9252 | +0.123 | +156.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 9252 | +0.123 | +156.00€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 9384 | +0.114 | +16.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 9384 | +0.114 | +16.89€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1437 | +0.292 | -5.17€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1437 | +0.292 | -5.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 641 | +0.279 | -14.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 641 | +0.279 | -14.00€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 691 | +0.295 | +6.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 691 | +0.295 | +6.80€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 105 | +0.341 | +2.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 105 | +0.341 | +2.03€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 626 | +0.440 | +2.03€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 626 | +0.440 | +2.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 295 | +0.439 | +0.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 295 | +0.439 | +0.62€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 290 | +0.442 | +1.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 290 | +0.442 | +1.40€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 41 | +0.384 | +0.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 41 | +0.384 | +0.01€ | 0 | 1 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1082 | +0.076 | -41.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 375 | +0.062 | -28.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 707 | +0.083 | -12.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 61 | +0.119 | +3.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 61 | +0.119 | +3.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 853 | +0.083 | -15.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 146 | +0.081 | -3.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 707 | +0.083 | -12.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 168 | +0.024 | -28.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 168 | +0.024 | -28.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 34376 | +0.097 | -1090.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 2845 | +0.089 | +17.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 31531 | +0.097 | -1108.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 19339 | +0.101 | -329.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 2845 | +0.089 | +17.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 16494 | +0.103 | -347.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 6413 | +0.107 | -40.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 6413 | +0.107 | -40.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 8624 | +0.080 | -720.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 8624 | +0.080 | -720.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 790 | +0.213 | -98.74€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 790 | +0.213 | -98.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 790 | +0.213 | -98.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 790 | +0.213 | -98.74€ | 2 | 4 |
| ✅ GBM_LATE_15M | 24752 | +0.081 | +11656.27€ | 0 | 17 |
| ✅ GBM_LATE_15M#15min | 24752 | +0.081 | +11656.27€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 4128 | +0.192 | +2984.04€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 4128 | +0.192 | +2984.04€ | 0 | 19 |
| ✅ GBM_LATE_15M#BTC | 3664 | +0.176 | +2532.02€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 3664 | +0.176 | +2532.02€ | 0 | 25 |
| ✅ GBM_LATE_15M#DOGE | 4284 | +0.199 | +3211.29€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 4284 | +0.199 | +3211.29€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 3670 | +0.017 | +749.63€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 3670 | +0.017 | +749.63€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 3565 | -0.033 | +808.45€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 3565 | -0.033 | +808.45€ | 4 | 15 |
| ✅ GBM_LATE_15M#XRP | 5441 | -0.042 | +1370.84€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 5441 | -0.042 | +1370.84€ | 4 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 26126 | +0.085 | +13609.18€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 26126 | +0.085 | +13609.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 4945 | +0.016 | +2628.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 4945 | +0.016 | +2628.36€ | 1 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 5444 | +0.014 | +1117.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 5444 | +0.014 | +1117.61€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 3709 | +0.262 | +3727.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 3709 | +0.262 | +3727.73€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 4230 | +0.001 | +775.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 4230 | +0.001 | +775.54€ | 2 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 4255 | +0.027 | +1590.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 4255 | +0.027 | +1590.68€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 3543 | +0.275 | +3769.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 3543 | +0.275 | +3769.26€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 19955 | +0.167 | +14826.14€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 19955 | +0.167 | +14826.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 3004 | +0.205 | +2368.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 3004 | +0.205 | +2368.47€ | 0 | 18 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 3179 | +0.148 | +2310.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 3179 | +0.148 | +2310.72€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 3123 | +0.208 | +2482.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 3123 | +0.208 | +2482.94€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 3351 | +0.133 | +2320.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 3351 | +0.133 | +2320.27€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 3713 | +0.115 | +2519.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 3713 | +0.115 | +2519.27€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 3585 | +0.203 | +2824.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 3585 | +0.203 | +2824.46€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 4923 | +0.125 | +2022.88€ | 0 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 4923 | +0.125 | +2022.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 184 | +0.118 | +76.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 184 | +0.118 | +76.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1407 | +0.120 | +621.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1407 | +0.120 | +621.97€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 372 | +0.144 | +178.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 372 | +0.144 | +178.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1430 | +0.141 | +619.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1430 | +0.141 | +619.06€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1026 | +0.098 | +310.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1026 | +0.098 | +310.22€ | 2 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 504 | +0.134 | +216.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 504 | +0.134 | +216.54€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 24855 | +0.174 | +18368.99€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 24855 | +0.174 | +18368.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 3935 | +0.219 | +3298.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 3935 | +0.219 | +3298.32€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 3889 | +0.150 | +2557.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 3889 | +0.150 | +2557.68€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 4069 | +0.225 | +3503.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 4069 | +0.225 | +3503.35€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 4033 | +0.135 | +2715.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 4033 | +0.135 | +2715.12€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 4358 | +0.111 | +2703.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 4358 | +0.111 | +2703.54€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 4571 | +0.205 | +3590.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 4571 | +0.205 | +3590.99€ | 0 | 24 |
| ✅ GBM_LATE_5M | 6718 | +0.144 | +3753.82€ | 1 | 28 |
| ✅ GBM_LATE_5M#5min | 6718 | +0.144 | +3753.82€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 594 | +0.186 | +416.56€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 594 | +0.186 | +416.56€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1732 | +0.141 | +1102.93€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1732 | +0.141 | +1102.93€ | 0 | 27 |
| ✅ GBM_LATE_5M#DOGE | 889 | +0.171 | +564.50€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 889 | +0.171 | +564.50€ | 0 | 22 |
| ✅ GBM_LATE_5M#ETH | 2126 | +0.147 | +1170.34€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2126 | +0.147 | +1170.34€ | 0 | 31 |
| ✅ GBM_LATE_5M#SOL | 558 | +0.098 | +183.16€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 558 | +0.098 | +183.16€ | 0 | 15 |
| ✅ GBM_LATE_5M#XRP | 819 | +0.115 | +316.33€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 819 | +0.115 | +316.33€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1649 | +0.071 | +737.97€ | 2 | 15 |
| ✅ GBM_LATE_60M#60min | 1649 | +0.071 | +737.97€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 593 | +0.092 | +260.98€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 593 | +0.092 | +260.98€ | 0 | 16 |
| ✅ GBM_LATE_60M#ETH | 548 | +0.073 | +286.68€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 548 | +0.073 | +286.68€ | 2 | 16 |
| ✅ GBM_LATE_60M#SOL | 508 | +0.043 | +190.31€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 508 | +0.043 | +190.31€ | 1 | 13 |
| 🚫 GBM_LATE_60M_FADE | 362 | -0.258 | -27.08€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 362 | -0.258 | -27.08€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 137 | -0.227 | -11.84€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 137 | -0.227 | -11.84€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 121 | -0.256 | -8.96€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 121 | -0.256 | -8.96€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 104 | -0.292 | -6.28€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 104 | -0.292 | -6.28€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 678 | +0.065 | +133.77€ | 1 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 678 | +0.065 | +133.77€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 267 | +0.054 | +44.84€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 267 | +0.054 | +44.84€ | 2 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 194 | +0.031 | +2.52€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 194 | +0.031 | +2.52€ | 2 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 217 | +0.107 | +86.41€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 217 | +0.107 | +86.41€ | 2 | 12 |
| ✅ LATE_WINDOW_5MIN | 95 | +0.253 | +75.39€ | 0 | 9 |
| ✅ LATE_WINDOW_5MIN#5min | 95 | +0.253 | +75.39€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 95 | +0.253 | +75.39€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 95 | +0.253 | +75.39€ | 0 | 9 |
| ✅ LEADLAG_BTC_XRP_15M | 1866 | +0.095 | +491.31€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 1866 | +0.095 | +491.31€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 1866 | +0.095 | +491.31€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 1866 | +0.095 | +491.31€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 374 | -0.082 | -35.05€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 374 | -0.082 | -35.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 94 | -0.062 | -5.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 94 | -0.062 | -5.45€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 67 | -0.080 | -7.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 67 | -0.080 | -7.45€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 132 | -0.030 | -5.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 132 | -0.030 | -5.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 1913 | +0.004 | +11.94€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1913 | +0.004 | +11.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 103 | +0.024 | +0.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 103 | +0.024 | +0.01€ | 0 | 2 |
| ✅ LIQUIDACIONES_5M#BTC | 207 | -0.007 | +11.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 207 | -0.007 | +11.30€ | 5 | 3 |
| ✅ LIQUIDACIONES_5M#DOGE | 155 | -0.041 | -8.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 155 | -0.041 | -8.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 806 | +0.026 | +22.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 806 | +0.026 | +22.35€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 467 | -0.001 | -5.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 467 | -0.001 | -5.46€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 175 | -0.042 | -8.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 175 | -0.042 | -8.26€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M | 1056 | -0.047 | -30.46€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1056 | -0.047 | -30.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 301 | -0.045 | -13.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 301 | -0.045 | -13.58€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 352 | -0.034 | -3.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 352 | -0.034 | -3.94€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 403 | -0.060 | -12.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 403 | -0.060 | -12.94€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 752 | -0.025 | +6.22€ | 2 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 337 | -0.022 | +4.13€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 415 | -0.028 | +2.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 23 | -0.020 | +1.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 13 | +0.065 | +3.90€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 10 | -0.083 | -2.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 189 | +0.065 | +42.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 83 | +0.053 | +14.67€ | 0 | 4 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 106 | +0.074 | +27.56€ | 0 | 7 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 121 | -0.069 | -11.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 55 | -0.061 | -4.97€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 66 | -0.073 | -6.65€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 124 | -0.071 | -11.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 54 | -0.089 | -7.57€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 70 | -0.056 | -3.67€ | 2 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 115 | -0.013 | +1.88€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 58 | -0.017 | +2.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 57 | -0.009 | -0.87€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 180 | -0.066 | -16.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 74 | -0.053 | -4.65€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 106 | -0.074 | -11.46€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M | 14294 | -0.012 | -206.27€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14294 | -0.012 | -206.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 3011 | -0.021 | -59.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 3011 | -0.021 | -59.46€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 3075 | -0.015 | -29.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 3075 | -0.015 | -29.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 27941 | -0.008 | +1227.17€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 27941 | -0.008 | +1227.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 4926 | +0.016 | +594.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 4926 | +0.016 | +594.71€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 4348 | -0.028 | -52.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 4348 | -0.028 | -52.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 4963 | +0.014 | +449.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 4963 | +0.014 | +449.99€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 4129 | -0.052 | -147.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 4129 | -0.052 | -147.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 4673 | -0.012 | +175.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 4673 | -0.012 | +175.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 4902 | +0.007 | +207.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 4902 | +0.007 | +207.76€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 5734 | -0.056 | -128.96€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 5734 | -0.056 | -128.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1203 | +0.000 | -15.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1203 | +0.000 | -15.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1376 | -0.078 | -35.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1376 | -0.078 | -35.57€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 43 | -0.122 | -5.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 43 | -0.122 | -5.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 609 | -0.115 | -19.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 609 | -0.115 | -19.60€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1656 | -0.075 | -27.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1656 | -0.075 | -27.11€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 847 | -0.016 | -25.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 847 | -0.016 | -25.72€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3343 | +0.005 | -1.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3343 | +0.005 | -1.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 189 | +0.013 | -1.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 189 | +0.013 | -1.05€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 136 | +0.000 | -1.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 136 | +0.000 | -1.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1315 | +0.007 | +7.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1315 | +0.007 | +7.70€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1388 | +0.007 | +0.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1388 | +0.007 | +0.29€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 70989 | -0.072 | +1721.24€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 70989 | -0.072 | +1721.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 11988 | -0.079 | +705.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 11988 | -0.079 | +705.09€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 10969 | -0.092 | -467.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 10969 | -0.092 | -467.81€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 12177 | -0.067 | +672.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 12177 | -0.067 | +672.53€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 10494 | -0.092 | -144.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 10494 | -0.092 | -144.33€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 13015 | -0.048 | +374.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 13015 | -0.048 | +374.30€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 12346 | -0.062 | +581.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 12346 | -0.062 | +581.46€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 7421 | -0.023 | -110.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 7421 | -0.023 | -110.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1648 | -0.025 | +0.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1648 | -0.025 | +0.80€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1003 | -0.020 | -31.30€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2005 | -0.018 | -19.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2005 | -0.018 | -19.44€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1031 | -0.040 | -16.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1031 | -0.040 | -16.91€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 738 | -0.020 | -23.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 738 | -0.020 | -23.52€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1104 | +0.105 | +360.18€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#5min | 968 | +0.111 | +347.58€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 227 | +0.129 | +105.84€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 227 | +0.129 | +105.84€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 187 | +0.093 | +43.26€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 187 | +0.093 | +43.26€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 195 | +0.094 | +64.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 195 | +0.094 | +64.08€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#SOL | 171 | +0.130 | +76.59€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 171 | +0.130 | +76.59€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 188 | +0.105 | +57.82€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 188 | +0.105 | +57.82€ | 0 | 5 |
| ✅ ORDER_FLOW_5M_REACTIVO | 445 | -0.059 | -52.05€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 445 | -0.059 | -52.05€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 95 | -0.015 | +1.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 95 | -0.015 | +1.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 54 | -0.125 | -15.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 54 | -0.125 | -15.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 128 | -0.077 | -24.50€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 128 | -0.077 | -24.50€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 94 | +0.000 | +1.26€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 94 | +0.000 | +1.26€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 74 | -0.105 | -14.81€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 74 | -0.105 | -14.81€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 555 | -0.103 | -40.18€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 256 | -0.155 | -57.95€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 208 | -0.200 | -60.63€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 48 | +0.040 | +2.69€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 193 | -0.080 | -0.13€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 149 | -0.089 | -8.28€ | 1 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 44 | -0.043 | +8.15€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 106 | -0.018 | +17.90€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 84 | -0.035 | +11.21€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 22 | +0.042 | +6.69€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 441 | -0.132 | -57.70€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 114 | +0.009 | +17.52€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 693 | -0.208 | -32.85€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 285 | -0.200 | -27.22€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 248 | -0.196 | -26.82€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 37 | -0.218 | -0.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 240 | -0.223 | -22.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 208 | -0.233 | -27.06€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 32 | -0.147 | +4.66€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 168 | -0.194 | +16.76€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 152 | -0.195 | +12.09€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 16 | -0.133 | +4.67€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 608 | -0.210 | -41.78€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 85 | -0.190 | +8.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 284 | +0.409 | +213.96€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#BTC | 29 | +0.048 | -4.24€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 29 | +0.048 | -4.24€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 76 | +0.372 | +56.60€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 76 | +0.372 | +56.60€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 179 | +0.478 | +161.59€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 179 | +0.478 | +161.59€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 284 | +0.409 | +213.96€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 492 | +0.038 | +18.46€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 492 | +0.038 | +18.46€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 229 | +0.045 | +8.44€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 229 | +0.045 | +8.44€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 33 | +0.071 | +0.99€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 33 | +0.071 | +0.99€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 53 | -0.009 | -2.28€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 53 | -0.009 | -2.28€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 177 | +0.036 | +11.31€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 177 | +0.036 | +11.31€ | 1 | 4 |
| ✅ STREAK_FADE_5M | 2723 | -0.023 | -113.87€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2723 | -0.023 | -113.87€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 566 | -0.023 | -23.32€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 566 | -0.023 | -23.32€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 155 | -0.048 | -14.93€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 155 | -0.048 | -14.93€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1198 | -0.022 | -48.67€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1198 | -0.022 | -48.67€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 73 | -0.060 | -7.39€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 73 | -0.060 | -7.39€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 35 | -0.013 | -2.95€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 35 | -0.013 | -2.95€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 7613 | +0.022 | +109.24€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 7613 | +0.022 | +109.24€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2130 | +0.021 | +20.36€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2130 | +0.021 | +20.36€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1697 | +0.034 | +50.29€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1697 | +0.034 | +50.29€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2312 | +0.011 | +1.63€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2312 | +0.011 | +1.63€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1474 | +0.029 | +36.98€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1474 | +0.029 | +36.98€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 7146 | +0.011 | -49.55€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 7146 | +0.011 | -49.55€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 2871 | +0.014 | -11.94€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 2871 | +0.014 | -11.94€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 2796 | +0.011 | -19.54€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 2796 | +0.011 | -19.54€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1479 | +0.003 | -18.07€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1479 | +0.003 | -18.07€ | 2 | 0 |
| ✅ UPDOWN_GBM | 35638 | +0.030 | +2070.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 9627 | +0.065 | +1689.47€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 1325 | +0.004 | +5.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 22381 | +0.019 | +356.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 2166 | +0.006 | +19.48€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 3582 | +0.066 | +372.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 613 | +0.144 | +230.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 29 | -0.016 | -0.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 2940 | +0.050 | +143.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 6596 | +0.035 | +439.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1220 | +0.082 | +264.71€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 360 | +0.019 | +7.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 3991 | +0.031 | +149.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 972 | +0.004 | +16.92€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 53 | -0.100 | +0.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 4149 | +0.040 | +243.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 564 | +0.140 | +200.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 27 | -0.017 | -2.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 3558 | +0.024 | +45.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 7585 | +0.017 | +275.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 2488 | +0.045 | +265.53€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 348 | +0.006 | +6.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 3966 | +0.005 | +3.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 738 | +0.003 | -4.32€ | 2 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 45 | -0.138 | +3.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 8561 | +0.015 | +212.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 2369 | +0.026 | +162.79€ | 0 | 11 |
| ✅ UPDOWN_GBM#SOL#240min | 342 | -0.006 | -3.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 5355 | +0.012 | +48.57€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 456 | +0.018 | +6.88€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 39 | -0.159 | -2.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 5163 | +0.034 | +528.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 2373 | +0.078 | +565.69€ | 0 | 12 |
| ✅ UPDOWN_GBM#XRP#240min | 219 | -0.002 | -3.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 2571 | -0.003 | -34.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 137 | -0.133 | +2.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 533 | +0.336 | +154.34€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 533 | +0.336 | +154.34€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 298 | +0.340 | +83.23€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 298 | +0.340 | +83.23€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 235 | +0.327 | +71.10€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 235 | +0.327 | +71.10€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 11541 | -0.042 | +2369.45€ | 2 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 11541 | -0.042 | +2369.45€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 714 | -0.041 | +337.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 714 | -0.041 | +337.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2151 | -0.123 | +16.21€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2151 | -0.123 | +16.21€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 348 | +0.180 | +232.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 348 | +0.180 | +232.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1273 | +0.200 | +727.48€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1273 | +0.200 | +727.48€ | 2 | 23 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 3520 | -0.064 | +532.67€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 3520 | -0.064 | +532.67€ | 2 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 3535 | -0.078 | +523.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 3535 | -0.078 | +523.12€ | 3 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 137 | +0.040 | +8.30€ | 2 | 2 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 137 | +0.040 | +8.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 137 | +0.040 | +8.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 137 | +0.040 | +8.30€ | 2 | 2 |
| ✅ UPDOWN_GBM_IBS_ALTO | 857 | +0.289 | +689.87€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 857 | +0.289 | +689.87€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 476 | +0.282 | +357.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 476 | +0.282 | +357.64€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 381 | +0.296 | +332.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 381 | +0.296 | +332.24€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 711 | -0.109 | -81.34€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 711 | -0.109 | -81.34€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 200 | -0.069 | -12.79€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 200 | -0.069 | -12.79€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 69 | -0.162 | -8.81€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 69 | -0.162 | -8.81€ | 3 | 0 |
| 🚫 UPDOWN_OU_5M#SOL | 64 | -0.212 | -10.19€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#SOL#5min | 64 | -0.212 | -10.19€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 2332 | +0.299 | +1160.88€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 803 | +0.248 | +108.30€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 869 | +0.288 | +362.56€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 660 | +0.376 | +690.02€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.018 n=477 — no justifica filtro, seguir monitorizando
  - _Datos_: n=477 IC=+0.018 PNL=+22.99€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 519 celda(s) pasan gate riguroso completo de 2205 evaluadas (n>=40) y 3195 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.026 < 0.08 — monitorear
  - _Datos_: n=2369 IC=+0.026 PNL=+162.79€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=869/15 IC=+0.288 PNL=+362.56€ | BTC: n=803/15 IC=+0.248 PNL=+108.30€ | SOL: n=660/15 IC=+0.376 PNL=+690.02€

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 30 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH#60min, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC#60min
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
  - _Estado_: alineada_con_outcome_prev IC=+0.097 n=288/60 | contraria IC=+0.150 n=278 | gap=-0.053 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=278, boost estimado=+0.003. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=738/40 IC=+0.003 PNL=-4.32€ | BTC#60min: n=972/40 IC=+0.004 PNL=+16.92€ | SOL#60min: n=456/40 IC=+0.018 PNL=+6.88€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.050 n=325079 | tras_1loss IC=+0.077 n=253341 | tras_2loss IC=+0.046 n=107121/40 | gap=+0.004 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.174 > 0.08 con n=311 PNL=+193.62€
  - _Datos_: n=311 IC=+0.174 PNL=+193.62€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.220 > 0.08 con n=373 PNL=+273.31€
  - _Datos_: n=373 IC=+0.220 PNL=+273.31€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.238 > 0.08 con n=40 PNL=+29.59€
  - _Datos_: n=40 IC=+0.238 PNL=+29.59€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.327 > 0.1 con n=1919 PNL=+1069.33€
  - _Datos_: n=1919 IC=+0.327 PNL=+1069.33€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=274 IC=+0.080 PNL=+34.60€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=274 IC=+0.080 PNL=+34.60€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=50 IC=+0.192 PNL=+34.21€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=50 IC=+0.192 PNL=+34.21€

**⏳ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: 30
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-OF-02H-BTCSOL** — ORDER_FLOW H=02h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 02h está en el blacklist basado en TODOS los pares. Con BTC+SOL solo, el historial muestra 4/5 (80%) IC=+0.054. ¿Se confirma la señal positiva con más datos?
  - _Umbral_: 15
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 02h del blacklist ORDER_FLOW
  - _Estado_: 3/15 ops en el filtro definido (IC actual=+0.045 PNL=+5.14€)
  - _Datos_: n=3 IC=+0.045 PNL=+5.14€

**⏳ H-CUSTOM-OF-07H-BTCSOL** — ORDER_FLOW H=07h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 07h está en el blacklist. Con BTC+SOL solo, el historial muestra 7/12 (58%) IC=+0.043. El blacklist puede estar basado en pares negativos que ya están excluidos.
  - _Umbral_: 20
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 07h del blacklist ORDER_FLOW
  - _Estado_: 1/20 ops en el filtro definido (IC actual=+0.008 PNL=+1.96€)
  - _Datos_: n=1 IC=+0.008 PNL=+1.96€
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: 07h sigue en ORDER_FLOW_BLACKLIST_HOURS -- mientras siga ahí, nunca genera fila para volver a evaluarse (26-Ago, triage candidatas estancadas)

**〰️ H-CUSTOM-GBM-60MIN-BUYYES** — GBM 60min BUY_YES — ¿edge superior al BUY_NO?
  - _Hipótesis_: Análisis actual muestra BUY_YES 60min: 22/36 (61%) IC=+0.105 vs BUY_NO 60min: 8/14 (57%) IC=+0.044. En 60min parece que BUY_YES es la dirección dominante, al contrario que en 15min.
  - _Umbral_: n≥30 y IC>+0.08
  - _Acción_: Si BUY_YES 60min confirma IC≥0.10 n≥40 → prioridad live por encima de BUY_NO
  - _Estado_: n=1539 IC=+0.015 PNL=+12.32€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1539 IC=+0.015 PNL=+12.32€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=627 IC=-0.013 PNL=+7.16€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=627 IC=-0.013 PNL=+7.16€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=477 IC=+0.018 PNL=+22.99€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=477 IC=+0.018 PNL=+22.99€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.184 > 0.1 con n=2046 PNL=+1264.33€
  - _Datos_: n=2046 IC=+0.184 PNL=+1264.33€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1220 IC=+0.082 PNL=+264.71€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1220 IC=+0.082 PNL=+264.71€

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
  - _Estado_: n=513 IC=+0.003 PNL=+28.80€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=513 IC=+0.003 PNL=+28.80€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=49 IC=+0.049 PNL=+2.29€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=49 IC=+0.049 PNL=+2.29€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.253 n=95) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=95 IC=+0.253 PNL=+75.39€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.121 > 0.02 con n=632 PNL=+241.00€
  - _Datos_: n=632 IC=+0.121 PNL=+241.00€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=147 IC=-0.044 PNL=+35.89€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=147 IC=-0.044 PNL=+35.89€

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
  - _Estado_: n=12328 IC=+0.054 PNL=+1492.84€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=12328 IC=+0.054 PNL=+1492.84€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.158 < -0.1 con n=223 PNL=+19.25€
  - _Datos_: n=223 IC=-0.158 PNL=+19.25€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=1829 IC=+0.046 PNL=+186.02€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1829 IC=+0.046 PNL=+186.02€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=74 IC=-0.105 PNL=+5.08€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=74 IC=-0.105 PNL=+5.08€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.126 > 0.1 con n=391 PNL=+108.75€
  - _Datos_: n=391 IC=+0.126 PNL=+108.75€

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
  - _Estado_: n=17328 IC=-0.137 PNL=+1170.95€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=17328 IC=-0.137 PNL=+1170.95€

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
  - _Estado_: n=1871 IC=+0.138 PNL=+1000.21€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=1871 IC=+0.138 PNL=+1000.21€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=3730 IC=+0.021 PNL=+125.99€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3730 IC=+0.021 PNL=+125.99€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.087 > 0.08 con n=2001 PNL=+1052.79€
  - _Datos_: n=2001 IC=+0.087 PNL=+1052.79€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.239 < -0.1 con n=1698 PNL=-187.05€
  - _Datos_: n=1698 IC=-0.239 PNL=-187.05€

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

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 35/40 ops en el filtro definido (IC actual=-0.041 PNL=+2.93€)
  - _Datos_: n=35 IC=-0.041 PNL=+2.93€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.087 n=955) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=955 IC=+0.087 PNL=+212.27€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.411 n=438) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=438 IC=+0.411 PNL=+617.55€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=8569 IC=+0.175 PNL=-1011.57€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=8569 IC=+0.175 PNL=-1011.57€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.194 > 0.1 con n=132 PNL=+75.67€
  - _Datos_: n=132 IC=+0.194 PNL=+75.67€
