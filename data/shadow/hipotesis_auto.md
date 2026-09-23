# Hipótesis automáticas — 2026-09-23 23:10 UTC
_Generado por shadow_postmortem.py sobre 580193 resoluciones (PNL=+64784.28€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=469)

- **PATRÓN** `py_entrada` > `0.51` → IC=+0.258 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.51 (IC base=+0.140)

- **PATRÓN** `n_total_lado` > `75.0` → IC=+0.209 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 75.0 (IC base=+0.140)

- **PATRÓN** `banda_hit_calibrado` > `0.803` → IC=+0.256 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.803 (IC base=+0.140)

- **PATRÓN** `banda_z` > `4.143` → IC=+0.168 (n=543)

  - _Acción_: Kelly boost +0.84€ cuando `banda_z` > 4.143 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.151 (n=502)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=581)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `3000.0061` → IC=+0.154 (n=362)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 3000.0061 (IC base=+0.140)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.122 (n=469)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.495 (IC base=+0.047)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.137 (n=169)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 96.0 (IC base=+0.047)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.134 (n=162)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.260 (n=415)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=341)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.260 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.149)

- **PATRÓN** `n_total_lado` > `70.0` → IC=+0.210 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 70.0 (IC base=+0.149)

- **PATRÓN** `banda_hit_calibrado` > `0.7972` → IC=+0.263 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.7972 (IC base=+0.149)

- **PATRÓN** `banda_z` > `4.341` → IC=+0.174 (n=433)

  - _Acción_: Kelly boost +0.87€ cuando `banda_z` > 4.341 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.170 (n=310)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 11.0 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.156 (n=492)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `4456.7277` → IC=+0.153 (n=197)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 4456.7277 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.154 (n=128)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 96.0 (IC base=+0.049)

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
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=88)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.190 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=87)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=98)

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
- **FILTRO** `restante_s_al_confirmar` < `146.02` → IC=-0.234 (n=6946)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 146.02
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=20841)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `139.02` → IC=-0.241 (n=910)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 139.02
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=2730)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` < `496.69` → IC=-0.150 (n=358)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 496.69
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=1077)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `128.01` → IC=-0.304 (n=860)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.01
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=2581)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `164.55` → IC=-0.228 (n=1654)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 164.55
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=4965)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `125.16` → IC=-0.358 (n=1376)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 125.16
  - _Potencial_: sin este filtro IC_bueno=-0.124 (n=4131)

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
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.203 (n=13626)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.101)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=3423)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `5620.2261` → IC=+0.176 (n=2182)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 5620.2261 (IC base=+0.101)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.139 (n=11222)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.137 (n=13472)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 7.0 (IC base=+0.127)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.231 (n=10677)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.174 (n=5567)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `7754.0551` → IC=+0.173 (n=2097)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 7754.0551 (IC base=+0.127)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.209 (n=1611)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.205 (n=1652)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.353 (n=765)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=2080)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `15906.4754` → IC=+0.240 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15906.4754 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.204 (n=1494)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.205 (n=1646)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` < `0.375` → IC=+0.263 (n=1503)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.375 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.201 (n=2110)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `14100.206` → IC=+0.211 (n=741)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14100.206 (IC base=+0.200)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.615` → IC=+0.174 (n=320)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` > 0.615 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `4624.034` → IC=+0.146 (n=235)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 4624.034 (IC base=+0.104)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.147 (n=344)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 7.0 (IC base=+0.107)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.145 (n=809)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.44 (IC base=+0.107)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.125 (n=556)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `5859.5725` → IC=+0.162 (n=220)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 5859.5725 (IC base=+0.107)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.155 (n=2763)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 5.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.145 (n=2347)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 15.0 (IC base=+0.145)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.335 (n=938)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.247 (n=654)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.233)

- **PATRÓN** `py_entrada` < `0.255` → IC=+0.357 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.255 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.238 (n=1457)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.233)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.156 (n=452)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 11.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.144 (n=223)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 5.0 (IC base=+0.138)

- **PATRÓN** `py_entrada` > `0.665` → IC=+0.234 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.665 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=527)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `1301.6177` → IC=+0.150 (n=643)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1301.6177 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.071)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.238 (n=602)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.433 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.165 (n=1068)
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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.145 (n=305)
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

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=11238)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=10714)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.225 (n=3746)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.339 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `8491.3442` → IC=+0.342 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8491.3442 (IC base=+0.198)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.175 (n=2585)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 17.0 (IC base=+0.169)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.183 (n=1899)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` < 0.71 (IC base=+0.169)

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

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.259 (n=388)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.249)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.250 (n=790)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.249)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.353 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.249)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.185 (n=2544)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 6.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.187 (n=2554)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=2211)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.181)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.248 (n=2384)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.238)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.320 (n=842)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=2602)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.196 (n=2498)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 17.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.198 (n=1918)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.71 (IC base=+0.194)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.436 (n=516)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.431)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.433 (n=459)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.431)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.471 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.431)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.431)

- **PATRÓN** `libro_liquidez` > `2073.3909` → IC=+0.439 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2073.3909 (IC base=+0.431)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.439 (n=196)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.436 (n=201)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.435)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.454 (n=172)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.471 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.438)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.439 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.438)

- **PATRÓN** `libro_liquidez` > `3366.033` → IC=+0.446 (n=128)

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

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.200 (n=33440)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.235 (n=14994)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.197)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.176 (n=5779)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 8.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.180 (n=4610)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 12.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.189 (n=6213)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.175)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.225 (n=5988)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.225 (n=5950)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.274 (n=2129)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.176 (n=5741)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 8.0 (IC base=+0.172)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.188 (n=6085)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.172)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.231 (n=3015)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.220 (n=2255)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.264 (n=2076)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.220)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.209 (n=5537)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.255 (n=2228)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.196 (n=5593)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 8.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.195 (n=5539)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.253 (n=2135)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.194)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.195 (n=5096)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.118)

- **PATRÓN** `restante_min` < `4.15` → IC=+0.128 (n=4694)

  - _Acción_: Kelly boost +0.64€ cuando `restante_min` < 4.15 (IC base=+0.118)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.140 (n=5048)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.95 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.129 (n=6929)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 8.0 (IC base=+0.118)

- **PATRÓN** `lag_apertura_s` < `2.89` → IC=+0.141 (n=4673)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 2.89 (IC base=+0.118)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.199 (n=2567)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.38 (IC base=+0.123)

- **PATRÓN** `restante_min` < `4.1` → IC=+0.134 (n=2325)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` < 4.1 (IC base=+0.123)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.141 (n=2502)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.94 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.138 (n=3422)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 8.0 (IC base=+0.123)

- **PATRÓN** `lag_apertura_s` < `3.42` → IC=+0.144 (n=2323)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 3.42 (IC base=+0.123)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.191 (n=2529)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.113)

- **PATRÓN** `restante_min` < `4.19` → IC=+0.126 (n=2361)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.19 (IC base=+0.113)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.135 (n=2553)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.113)

- **PATRÓN** `lag_apertura_s` < `2.3` → IC=+0.139 (n=2358)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.3 (IC base=+0.113)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.324 (n=770)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.293)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.388 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `4081.2097` → IC=+0.315 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4081.2097 (IC base=+0.293)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.305 (n=337)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.280)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.346 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `4246.1312` → IC=+0.302 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4246.1312 (IC base=+0.280)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.335 (n=368)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.296)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.302 (n=543)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.296)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.387 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.296)

- **PATRÓN** `libro_liquidez` > `1462.5909` → IC=+0.312 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1462.5909 (IC base=+0.296)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.448 (n=499)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.440)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.445 (n=419)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.444 (n=495)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.440)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.442 (n=563)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.440)

- **PATRÓN** `libro_liquidez` > `2546.95` → IC=+0.440 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2546.95 (IC base=+0.440)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.448 (n=228)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.440)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.448 (n=228)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.446 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.440)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.450 (n=159)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.454 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.91` → IC=+0.440 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.91 (IC base=+0.442)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.443 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.442)

- **PATRÓN** `libro_liquidez` > `2007.6359` → IC=+0.461 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2007.6359 (IC base=+0.442)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.307 (n=205)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.257)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.385 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.269 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1367.7996` → IC=+0.286 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1367.7996 (IC base=+0.257)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=54)

- **FILTRO** `py_entrada` > `0.785` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.785
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=54)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.307 (n=205)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.257)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.385 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.269 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1367.7996` → IC=+0.286 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1367.7996 (IC base=+0.257)

### GBM_LATE_15M
- **PATRÓN** `drift_60min` |x|≤ `0.4815` → IC=+0.121 (n=7847)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.60€ cuando `drift_60min` |x|≤ 0.4815 (IC base=+0.106)

- **PATRÓN** `ibs_20min` > `0.9823` → IC=+0.245 (n=2615)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9823 (IC base=+0.106)

- **PATRÓN** `dist_vwap_pct` > `0.8494` → IC=+0.253 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8494 (IC base=+0.106)

- **PATRÓN** `dist_vwap_pct` < `0.6376` → IC=+0.250 (n=2197)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6376 (IC base=+0.106)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.958` → IC=+0.177 (n=3015)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 5.958 (IC base=+0.106)

- **PATRÓN** `volumen_regimen` < `1.2107` → IC=+0.249 (n=2107)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2107 (IC base=+0.106)

- **PATRÓN** `volumen_regimen` > `1.0476` → IC=+0.260 (n=956)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0476 (IC base=+0.106)

- **PATRÓN** `volumen_pendiente_norm` > `0.3054` → IC=+0.219 (n=781)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3054 (IC base=+0.106)

- **PATRÓN** `volumen_spike_ratio` > `1.9076` → IC=+0.206 (n=3570)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9076 (IC base=+0.106)

- **PATRÓN** `ibs_20min` < `0.5702` → IC=+0.132 (n=9472)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.5702 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` > `0.6162` → IC=+0.192 (n=697)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.6162 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` < `0.1525` → IC=+0.172 (n=2981)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.1525 (IC base=+0.064)

- **PATRÓN** `volumen_regimen` < `0.6986` → IC=+0.180 (n=1454)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.6986 (IC base=+0.064)

- **PATRÓN** `volumen_regimen` > `1.0522` → IC=+0.174 (n=1496)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 1.0522 (IC base=+0.064)

- **PATRÓN** `volumen_pendiente_norm` > `0.1679` → IC=+0.221 (n=1577)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1679 (IC base=+0.064)

- **PATRÓN** `volumen_spike_ratio` > `1.5716` → IC=+0.200 (n=4943)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5716 (IC base=+0.064)

- **PATRÓN** `ballena_activa_n` < `136.0` → IC=+0.210 (n=5318)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 136.0 (IC base=+0.064)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.183 (n=592)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.005 (IC base=+0.161)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.174 (n=594)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0082 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.348` → IC=+0.166 (n=1775)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.348 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.166 (n=864)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.172 (n=1185)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 11.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.270 (n=688)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.119` → IC=+0.271 (n=763)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.119 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.211 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `1.4363` → IC=+0.163 (n=1659)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.4363 (IC base=+0.161)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.249 (n=1190)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.09` → IC=+0.285 (n=444)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.09 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.246 (n=916)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.058` → IC=+0.291 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.058 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.412` → IC=+0.236 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.412 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.422` → IC=+0.247 (n=1382)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.422 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` < `0.0922` → IC=+0.230 (n=1137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0922 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2765` → IC=+0.261 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2765 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.6417` → IC=+0.241 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6417 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `1799.54` → IC=+0.236 (n=887)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1799.54 (IC base=+0.234)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.232 (n=903)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.084` → IC=+0.252 (n=450)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.084 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.233 (n=1349)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `0.9902` → IC=+0.268 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9902 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` > `0.2046` → IC=+0.221 (n=721)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2046 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` < `0.589` → IC=+0.222 (n=1410)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.589 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.863` → IC=+0.260 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.863 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` < `1.2524` → IC=+0.222 (n=1349)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2524 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` > `0.8736` → IC=+0.226 (n=899)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8736 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.237 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` < `1.4012` → IC=+0.222 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4012 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `2.3728` → IC=+0.225 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3728 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `16596.3663` → IC=+0.224 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16596.3663 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.177 (n=469)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0026 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0755` → IC=+0.160 (n=469)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.0755 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.168 (n=471)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 18.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.6918` → IC=+0.170 (n=1407)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.6918 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1332` → IC=+0.156 (n=1253)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1332 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.172` → IC=+0.159 (n=227)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 11.172 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.236` → IC=+0.140 (n=1280)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 4.236 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.204` → IC=+0.149 (n=1407)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.204 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.0963` → IC=+0.173 (n=506)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.0963 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.4156` → IC=+0.151 (n=1297)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4156 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.4221` → IC=+0.144 (n=1296)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.4221 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `411.0` → IC=+0.146 (n=1214)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 411.0 (IC base=+0.138)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.214 (n=579)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.189 (n=1736)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 6.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.192 (n=1549)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.264 (n=688)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.193` → IC=+0.251 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.193 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` < `0.2115` → IC=+0.188 (n=1731)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` < 0.2115 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.3614` → IC=+0.201 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3614 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `2.8473` → IC=+0.206 (n=747)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8473 (IC base=+0.187)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.194 (n=1238)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.02 (IC base=+0.187)

- **PATRÓN** `sigma_h` < `0.0115` → IC=+0.223 (n=1489)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0115 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.5908` → IC=+0.216 (n=1489)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5908 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.251 (n=568)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.219 (n=691)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` < `0.0625` → IC=+0.244 (n=655)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0625 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.609` → IC=+0.246 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.609 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.3585` → IC=+0.268 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3585 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` < `1.7801` → IC=+0.213 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7801 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `2.2159` → IC=+0.219 (n=906)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2159 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.222 (n=1009)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `1878.7384` → IC=+0.231 (n=675)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1878.7384 (IC base=+0.214)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.213 (n=1143)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.214)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.160 (n=98)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=2171)

- **PATRÓN** `ibs_20min` > `0.9422` → IC=+0.212 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9422 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` > `0.3692` → IC=+0.325 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3692 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` < `0.7982` → IC=+0.331 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7982 (IC base=+0.021)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.712` → IC=+0.154 (n=695)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 4.712 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` < `0.6681` → IC=+0.330 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6681 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` > `1.1977` → IC=+0.343 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1977 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` < `0.1818` → IC=+0.316 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1818 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.3037` → IC=+0.341 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3037 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` < `1.4012` → IC=+0.337 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4012 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` > `2.2012` → IC=+0.330 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2012 (IC base=+0.021)

- **PATRÓN** `ballena_activa_n` < `163.0` → IC=+0.330 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 163.0 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` > `0.68` → IC=+0.191 (n=137)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.68 (IC base=+0.015)

- **PATRÓN** `volumen_regimen` < `0.8497` → IC=+0.162 (n=540)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8497 (IC base=+0.015)

- **PATRÓN** `volumen_pendiente_norm` > `0.2269` → IC=+0.218 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2269 (IC base=+0.015)

- **PATRÓN** `volumen_spike_ratio` > `1.5219` → IC=+0.175 (n=675)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.5219 (IC base=+0.015)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.172 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=316)

- **FILTRO** `ibs_20min` < `0.2703` → IC=-0.205 (n=93)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2703
  - _Potencial_: sin este filtro IC_bueno=+0.130 (n=282)

- **FILTRO** `ibs_20min` > `0.2571` → IC=-0.125 (n=2138)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2571
  - _Potencial_: sin este filtro IC_bueno=+0.124 (n=1058)

- **FILTRO** `sigma_ewma_delta_pct` > `8.651` → IC=-0.205 (n=344)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.651
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2852)

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

- **PATRÓN** `ibs_20min` < `0.2571` → IC=+0.124 (n=1058)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.2571 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` > `0.6927` → IC=+0.254 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6927 (IC base=-0.042)

- **PATRÓN** `volumen_regimen` < `1.0952` → IC=+0.224 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0952 (IC base=-0.042)

- **PATRÓN** `volumen_regimen` > `0.9031` → IC=+0.214 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9031 (IC base=-0.042)

- **PATRÓN** `volumen_pendiente_norm` < `0.1041` → IC=+0.228 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1041 (IC base=-0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.1582` → IC=+0.247 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1582 (IC base=-0.042)

- **PATRÓN** `volumen_spike_ratio` < `2.4353` → IC=+0.264 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4353 (IC base=-0.042)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6615` → IC=-0.179 (n=550)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6615
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=1653)

- **FILTRO** `ibs_20min` < `0.7098` → IC=-0.156 (n=1453)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7098
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=750)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.199 (n=406)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=1797)

- **FILTRO** `ibs_20min` > `0.77` → IC=-0.201 (n=811)

  - _Acción_: SKIP cuando `ibs_20min` > 0.77
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=2441)

- **PATRÓN** `dist_vwap_pct` > `0.7916` → IC=+0.320 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7916 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` < `0.2685` → IC=+0.323 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2685 (IC base=-0.066)

- **PATRÓN** `volumen_regimen` < `0.9865` → IC=+0.296 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9865 (IC base=-0.066)

- **PATRÓN** `volumen_regimen` > `0.616` → IC=+0.311 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.616 (IC base=-0.066)

- **PATRÓN** `volumen_pendiente_norm` < `0.0995` → IC=+0.299 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0995 (IC base=-0.066)

- **PATRÓN** `volumen_pendiente_norm` > `0.0744` → IC=+0.311 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0744 (IC base=-0.066)

- **PATRÓN** `volumen_spike_ratio` < `1.3923` → IC=+0.313 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3923 (IC base=-0.066)

- **PATRÓN** `volumen_spike_ratio` > `1.7955` → IC=+0.301 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7955 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` > `0.8796` → IC=+0.265 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8796 (IC base=-0.025)

- **PATRÓN** `volumen_regimen` < `0.7367` → IC=+0.249 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7367 (IC base=-0.025)

- **PATRÓN** `volumen_regimen` > `1.2494` → IC=+0.282 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2494 (IC base=-0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.1026` → IC=+0.273 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1026 (IC base=-0.025)

- **PATRÓN** `volumen_spike_ratio` < `2.1684` → IC=+0.251 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1684 (IC base=-0.025)

- **PATRÓN** `volumen_spike_ratio` > `1.4374` → IC=+0.247 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4374 (IC base=-0.025)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.244 (n=642)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=-0.025)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.198 (n=3280)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0097 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.4738` → IC=+0.188 (n=8775)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4738 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `0.7756` → IC=+0.289 (n=1037)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7756 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.586` → IC=+0.156 (n=4643)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 3.586 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` > `0.6881` → IC=+0.249 (n=3108)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6881 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` > `0.297` → IC=+0.266 (n=826)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.297 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` < `1.4706` → IC=+0.242 (n=1882)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4706 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` > `2.6803` → IC=+0.238 (n=1882)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6803 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.269 (n=5166)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 98.0 (IC base=+0.098)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.152 (n=3281)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0091 (IC base=+0.072)

- **PATRÓN** `ibs_20min` < `0.5476` → IC=+0.152 (n=8648)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.5476 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` < `0.2491` → IC=+0.238 (n=2727)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2491 (IC base=+0.072)

- **PATRÓN** `volumen_regimen` < `0.7092` → IC=+0.237 (n=1269)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7092 (IC base=+0.072)

- **PATRÓN** `volumen_regimen` > `1.2044` → IC=+0.245 (n=962)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2044 (IC base=+0.072)

- **PATRÓN** `volumen_pendiente_norm` > `0.2455` → IC=+0.300 (n=722)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2455 (IC base=+0.072)

- **PATRÓN** `volumen_spike_ratio` < `1.6084` → IC=+0.254 (n=1667)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6084 (IC base=+0.072)

- **PATRÓN** `volumen_spike_ratio` > `2.3262` → IC=+0.255 (n=1718)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3262 (IC base=+0.072)

- **PATRÓN** `ballena_activa_n` < `83.0` → IC=+0.262 (n=3664)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 83.0 (IC base=+0.072)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `sigma_ewma_delta_pct` > `4.508` → IC=-0.163 (n=515)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.508
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=1733)

- **PATRÓN** `ibs_20min` > `0.8893` → IC=+0.268 (n=678)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8893 (IC base=+0.045)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.772` → IC=+0.206 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.772 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` > `0.2229` → IC=+0.275 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2229 (IC base=+0.045)

- **PATRÓN** `volumen_spike_ratio` < `1.44` → IC=+0.180 (n=282)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.44 (IC base=+0.045)

- **PATRÓN** `volumen_spike_ratio` > `2.1594` → IC=+0.192 (n=384)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.1594 (IC base=+0.045)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.181 (n=377)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 15.0 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` < `0.1673` → IC=+0.442 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1673 (IC base=-0.018)

- **PATRÓN** `volumen_spike_ratio` < `2.7434` → IC=+0.432 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.7434 (IC base=-0.018)

- **PATRÓN** `volumen_spike_ratio` > `2.3568` → IC=+0.429 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3568 (IC base=-0.018)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=-0.018)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.862` → IC=+0.158 (n=656)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.862 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` > `0.1282` → IC=+0.173 (n=502)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1282 (IC base=+0.027)

- **PATRÓN** `volumen_regimen` > `0.6717` → IC=+0.166 (n=803)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.6717 (IC base=+0.027)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.219 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.027)

- **PATRÓN** `volumen_spike_ratio` < `1.4208` → IC=+0.205 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4208 (IC base=+0.027)

- **PATRÓN** `ballena_activa_n` < `247.0` → IC=+0.196 (n=383)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 247.0 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` < `0.1623` → IC=+0.215 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1623 (IC base=+0.003)

- **PATRÓN** `volumen_regimen` > `0.6101` → IC=+0.210 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6101 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2721` → IC=+0.300 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2721 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` < `1.4443` → IC=+0.226 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4443 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.1582` → IC=+0.231 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1582 (IC base=+0.003)

- **PATRÓN** `ballena_activa_n` < `476.0` → IC=+0.211 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 476.0 (IC base=+0.003)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.292 (n=518)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.246)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.248 (n=1559)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.246)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.250 (n=1377)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.246)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.301 (n=826)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.246)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.725` → IC=+0.280 (n=494)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.725 (IC base=+0.246)

- **PATRÓN** `volumen_pendiente_norm` < `0.1373` → IC=+0.258 (n=1379)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1373 (IC base=+0.246)

- **PATRÓN** `volumen_spike_ratio` > `3.4412` → IC=+0.262 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.4412 (IC base=+0.246)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.256 (n=1094)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.246)

- **PATRÓN** `libro_liquidez` > `1951.5744` → IC=+0.255 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1951.5744 (IC base=+0.246)

- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.316 (n=562)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.282)

- **PATRÓN** `drift_60min` |x|≤ `0.6005` → IC=+0.283 (n=1240)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6005 (IC base=+0.282)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.328 (n=423)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.282)

- **PATRÓN** `ibs_20min` < `0.2248` → IC=+0.287 (n=1090)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2248 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.819` → IC=+0.300 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.819 (IC base=+0.282)

- **PATRÓN** `volumen_pendiente_norm` > `0.3423` → IC=+0.304 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3423 (IC base=+0.282)

- **PATRÓN** `volumen_spike_ratio` < `1.5993` → IC=+0.286 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5993 (IC base=+0.282)

- **PATRÓN** `volumen_spike_ratio` > `2.7699` → IC=+0.285 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7699 (IC base=+0.282)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.289 (n=834)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `1933.4584` → IC=+0.302 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1933.4584 (IC base=+0.282)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.287 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.282)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.2829` → IC=-0.189 (n=477)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2829
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=1436)

- **FILTRO** `ibs_20min` > `0.7744` → IC=-0.181 (n=582)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7744
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=1748)

- **PATRÓN** `ibs_20min` > `0.9105` → IC=+0.178 (n=479)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.9105 (IC base=+0.010)

- **PATRÓN** `dist_vwap_pct` > `0.4588` → IC=+0.223 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4588 (IC base=+0.010)

- **PATRÓN** `volumen_regimen` < `0.9898` → IC=+0.234 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9898 (IC base=+0.010)

- **PATRÓN** `volumen_regimen` > `0.5808` → IC=+0.210 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5808 (IC base=+0.010)

- **PATRÓN** `volumen_pendiente_norm` > `0.0791` → IC=+0.250 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0791 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` < `2.0972` → IC=+0.244 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0972 (IC base=+0.010)

- **PATRÓN** `ballena_activa_n` < `101.0` → IC=+0.253 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 101.0 (IC base=+0.010)

- **PATRÓN** `dist_vwap_pct` > `0.1569` → IC=+0.205 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1569 (IC base=-0.007)

- **PATRÓN** `dist_vwap_pct` < `0.6852` → IC=+0.195 (n=470)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.6852 (IC base=-0.007)

- **PATRÓN** `volumen_regimen` < `1.1649` → IC=+0.206 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1649 (IC base=-0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.2812` → IC=+0.278 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2812 (IC base=-0.007)

- **PATRÓN** `volumen_spike_ratio` < `1.8288` → IC=+0.256 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8288 (IC base=-0.007)

- **PATRÓN** `volumen_spike_ratio` > `2.178` → IC=+0.238 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.178 (IC base=-0.007)

- **PATRÓN** `ballena_activa_n` < `139.0` → IC=+0.243 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 139.0 (IC base=-0.007)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7188` → IC=-0.200 (n=1039)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7188
  - _Potencial_: sin este filtro IC_bueno=+0.281 (n=1041)

- **FILTRO** `ibs_20min` > `0.6875` → IC=-0.230 (n=542)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6875
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=1644)

- **FILTRO** `sigma_ewma_delta_pct` > `4.678` → IC=-0.176 (n=477)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.678
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=1709)

- **PATRÓN** `ibs_20min` > `0.7188` → IC=+0.281 (n=1041)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7188 (IC base=+0.041)

- **PATRÓN** `dist_vwap_pct` > `0.8494` → IC=+0.338 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8494 (IC base=+0.041)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.573` → IC=+0.158 (n=331)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 9.573 (IC base=+0.041)

- **PATRÓN** `volumen_regimen` < `0.8667` → IC=+0.303 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8667 (IC base=+0.041)

- **PATRÓN** `volumen_regimen` > `0.6434` → IC=+0.291 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6434 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` < `0.1024` → IC=+0.295 (n=711)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1024 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.2247` → IC=+0.294 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2247 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` < `1.4421` → IC=+0.327 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4421 (IC base=+0.041)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.313 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.041)

- **PATRÓN** `ibs_20min` < `0.1` → IC=+0.213 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1 (IC base=+0.014)

- **PATRÓN** `dist_vwap_pct` < `0.2141` → IC=+0.216 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2141 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` < `0.7017` → IC=+0.246 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7017 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` < `0.1001` → IC=+0.207 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1001 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` > `0.0706` → IC=+0.201 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0706 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` < `2.4893` → IC=+0.216 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4893 (IC base=+0.014)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.233 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 51.0 (IC base=+0.014)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0167` → IC=+0.320 (n=853)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0167 (IC base=+0.280)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.288 (n=1338)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.280)

- **PATRÓN** `ibs_20min` > `0.74` → IC=+0.325 (n=1143)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.74 (IC base=+0.280)

- **PATRÓN** `dist_vwap_pct` > `0.2054` → IC=+0.319 (n=759)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2054 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.523` → IC=+0.305 (n=675)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.523 (IC base=+0.280)

- **PATRÓN** `volumen_regimen` > `0.8624` → IC=+0.304 (n=852)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8624 (IC base=+0.280)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.320 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.280)

- **PATRÓN** `volumen_spike_ratio` > `2.1562` → IC=+0.293 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1562 (IC base=+0.280)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.285 (n=1364)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `2622.2007` → IC=+0.296 (n=852)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2622.2007 (IC base=+0.280)

- **PATRÓN** `sigma_h` > `0.0152` → IC=+0.295 (n=924)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0152 (IC base=+0.271)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.280 (n=484)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.271)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.273 (n=685)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.271)

- **PATRÓN** `ibs_20min` < `0.3953` → IC=+0.304 (n=1388)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3953 (IC base=+0.271)

- **PATRÓN** `dist_vwap_pct` > `0.2984` → IC=+0.278 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2984 (IC base=+0.271)

- **PATRÓN** `dist_vwap_pct` < `0.9685` → IC=+0.272 (n=1563)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9685 (IC base=+0.271)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.006` → IC=+0.295 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.006 (IC base=+0.271)

- **PATRÓN** `volumen_regimen` < `0.6391` → IC=+0.272 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6391 (IC base=+0.271)

- **PATRÓN** `volumen_regimen` > `1.2434` → IC=+0.306 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2434 (IC base=+0.271)

- **PATRÓN** `volumen_pendiente_norm` > `0.2392` → IC=+0.338 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2392 (IC base=+0.271)

- **PATRÓN** `volumen_spike_ratio` < `1.434` → IC=+0.268 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.434 (IC base=+0.271)

- **PATRÓN** `volumen_spike_ratio` > `2.1624` → IC=+0.275 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1624 (IC base=+0.271)

- **PATRÓN** `libro_liquidez` > `2613.8325` → IC=+0.277 (n=924)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2613.8325 (IC base=+0.271)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.173 (n=2561)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0049 (IC base=+0.168)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.201 (n=2557)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.0899` → IC=+0.186 (n=2557)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.0899 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.179 (n=8002)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` > `0.5789` → IC=+0.217 (n=7665)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5789 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` > `0.1772` → IC=+0.197 (n=3352)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1772 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.316` → IC=+0.258 (n=1575)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.316 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `1.2135` → IC=+0.160 (n=5071)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2135 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` > `0.6282` → IC=+0.161 (n=5071)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6282 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.2453` → IC=+0.194 (n=1546)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2453 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `1.5622` → IC=+0.172 (n=3234)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5622 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `2.6248` → IC=+0.175 (n=2449)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.6248 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `2400.6554` → IC=+0.169 (n=5110)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2400.6554 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `116.0` → IC=+0.180 (n=6574)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 116.0 (IC base=+0.168)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.182 (n=4902)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0066 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.0806` → IC=+0.208 (n=2448)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0806 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.203 (n=2842)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` < `0.4783` → IC=+0.226 (n=7337)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4783 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` < `0.232` → IC=+0.158 (n=5330)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.232 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.32` → IC=+0.195 (n=1251)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.32 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `1.1737` → IC=+0.152 (n=5325)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1737 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.2917` → IC=+0.222 (n=1051)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2917 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.5639` → IC=+0.168 (n=2930)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.5639 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `2.259` → IC=+0.170 (n=3018)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.259 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `117.0` → IC=+0.173 (n=6301)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 117.0 (IC base=+0.167)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.223 (n=438)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.182)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.186 (n=594)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0076 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.3418` → IC=+0.206 (n=1310)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3418 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.198 (n=644)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 8.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `0.8961` → IC=+0.277 (n=873)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8961 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.122` → IC=+0.311 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.122 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2299` → IC=+0.234 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2299 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `1.4361` → IC=+0.179 (n=1210)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.4361 (IC base=+0.182)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.251 (n=850)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.1878` → IC=+0.292 (n=634)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1878 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.242 (n=979)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.247 (n=465)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.3443` → IC=+0.263 (n=950)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3443 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.234` → IC=+0.251 (n=1024)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.234 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.096` → IC=+0.233 (n=788)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.096 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.287` → IC=+0.257 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.287 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.4205` → IC=+0.261 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4205 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1801.66` → IC=+0.245 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1801.66 (IC base=+0.237)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.236 (n=384)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.162)

- **PATRÓN** `drift_60min` |x|≤ `0.0742` → IC=+0.202 (n=381)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0742 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=1204)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` > `0.4081` → IC=+0.226 (n=1142)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4081 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` > `0.212` → IC=+0.214 (n=680)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.212 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.523` → IC=+0.239 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.523 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` < `1.2629` → IC=+0.165 (n=1142)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2629 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` > `1.0753` → IC=+0.167 (n=518)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 1.0753 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` > `0.2827` → IC=+0.202 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2827 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` < `1.4112` → IC=+0.194 (n=370)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.4112 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `15891.3699` → IC=+0.165 (n=518)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 15891.3699 (IC base=+0.162)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.158 (n=1251)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0057 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.2922` → IC=+0.159 (n=1248)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.2922 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.177 (n=419)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 18.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.5649` → IC=+0.185 (n=1248)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.5649 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.1346` → IC=+0.161 (n=1233)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.1346 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.777` → IC=+0.202 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.777 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.2113` → IC=+0.156 (n=1248)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.2113 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.1573` → IC=+0.153 (n=379)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.1573 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.4156` → IC=+0.145 (n=1136)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.4156 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `215.0` → IC=+0.172 (n=352)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 215.0 (IC base=+0.136)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.219 (n=429)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.2255` → IC=+0.215 (n=857)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2255 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.218 (n=449)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.291 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.863` → IC=+0.276 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.863 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.1328` → IC=+0.198 (n=502)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1328 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` < `1.6421` → IC=+0.199 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6421 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` > `2.8549` → IC=+0.208 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8549 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.207 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `1953.22` → IC=+0.201 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1953.22 (IC base=+0.197)

- **PATRÓN** `sigma_h` < `0.0113` → IC=+0.232 (n=1065)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0113 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.0967` → IC=+0.256 (n=355)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0967 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.277 (n=375)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` < `0.2407` → IC=+0.256 (n=937)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2407 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.735` → IC=+0.271 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.735 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.3585` → IC=+0.268 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3585 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` < `1.7818` → IC=+0.220 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7818 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `3.4252` → IC=+0.230 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.4252 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `1881.693` → IC=+0.226 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1881.693 (IC base=+0.220)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.220 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.220)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.209 (n=411)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.4327` → IC=+0.159 (n=1225)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4327 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=1288)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` > `0.379` → IC=+0.197 (n=1224)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.379 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.1633` → IC=+0.180 (n=817)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.1633 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.936` → IC=+0.227 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.936 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `1.0413` → IC=+0.144 (n=1078)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.0413 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` > `0.6274` → IC=+0.148 (n=1224)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.6274 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.2919` → IC=+0.200 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2919 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `1.4216` → IC=+0.152 (n=400)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.4216 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `2.529` → IC=+0.169 (n=400)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.529 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `6793.8152` → IC=+0.185 (n=816)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 6793.8152 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `165.0` → IC=+0.145 (n=1162)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 165.0 (IC base=+0.143)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.155 (n=1295)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0073 (IC base=+0.123)

- **PATRÓN** `drift_60min` |x|≤ `0.3831` → IC=+0.143 (n=1295)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3831 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=506)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` < `0.4578` → IC=+0.186 (n=1140)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.4578 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` < `0.5831` → IC=+0.132 (n=1502)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.5831 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.904` → IC=+0.170 (n=453)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 6.904 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `0.8485` → IC=+0.148 (n=864)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8485 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.2908` → IC=+0.197 (n=186)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2908 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.7906` → IC=+0.134 (n=784)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.7906 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.489` → IC=+0.135 (n=392)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.489 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `10015.5876` → IC=+0.159 (n=587)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 10015.5876 (IC base=+0.123)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.155 (n=627)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0101 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=1418)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.5169` → IC=+0.203 (n=1383)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5169 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `0.8449` → IC=+0.216 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8449 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.729` → IC=+0.254 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.729 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `1.2208` → IC=+0.130 (n=1383)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.2208 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` > `0.7252` → IC=+0.123 (n=1235)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.7252 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` < `0.1649` → IC=+0.131 (n=1391)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` < 0.1649 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `2.4817` → IC=+0.128 (n=1335)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 2.4817 (IC base=+0.118)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.127 (n=1450)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2896.4901` → IC=+0.196 (n=627)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2896.4901 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.136 (n=1059)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 50.0 (IC base=+0.118)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.149 (n=622)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0061 (IC base=+0.113)

- **PATRÓN** `drift_60min` |x|≤ `0.1032` → IC=+0.152 (n=470)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1032 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.163 (n=641)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 15.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.5652` → IC=+0.209 (n=1408)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5652 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` > `1.0029` → IC=+0.142 (n=185)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 1.0029 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.1993` → IC=+0.137 (n=1296)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.1993 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.978` → IC=+0.143 (n=228)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 8.978 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `1.1736` → IC=+0.121 (n=1408)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.1736 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.277` → IC=+0.171 (n=171)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.277 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` > `2.4249` → IC=+0.130 (n=420)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.4249 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `3086.3351` → IC=+0.159 (n=470)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 3086.3351 (IC base=+0.113)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0188` → IC=+0.215 (n=882)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0188 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=485)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.209 (n=599)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` > `0.7386` → IC=+0.262 (n=1182)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7386 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `0.5059` → IC=+0.221 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5059 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.566` → IC=+0.244 (n=623)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.566 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` < `1.2089` → IC=+0.205 (n=1324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2089 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` > `0.8591` → IC=+0.222 (n=882)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8591 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.2333` → IC=+0.269 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2333 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` < `2.1558` → IC=+0.216 (n=1124)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1558 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `1.4095` → IC=+0.208 (n=1278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4095 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.206 (n=1405)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `2613.0376` → IC=+0.206 (n=882)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2613.0376 (IC base=+0.203)

- **PATRÓN** `sigma_h` < `0.0086` → IC=+0.233 (n=458)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0086 (IC base=+0.203)

- **PATRÓN** `sigma_h` > `0.0224` → IC=+0.206 (n=623)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0224 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.0896` → IC=+0.222 (n=458)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0896 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.221 (n=678)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.212 (n=624)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` < `0.44` → IC=+0.245 (n=1380)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.44 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `1.2288` → IC=+0.221 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2288 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.402` → IC=+0.242 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.402 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` > `0.6282` → IC=+0.215 (n=1374)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6282 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.2833` → IC=+0.288 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2833 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` < `2.2184` → IC=+0.193 (n=1084)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.2184 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `1.4406` → IC=+0.198 (n=1232)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4406 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `2586.8192` → IC=+0.205 (n=916)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2586.8192 (IC base=+0.203)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.166 (n=603)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0038 (IC base=+0.148)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.180 (n=604)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0089 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.0997` → IC=+0.154 (n=602)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.0997 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.187 (n=919)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 15.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.55` → IC=+0.189 (n=1613)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.55 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.8848` → IC=+0.195 (n=283)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.8848 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.726` → IC=+0.176 (n=829)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 3.726 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.8743` → IC=+0.165 (n=1054)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8743 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` > `1.2084` → IC=+0.156 (n=527)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 1.2084 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.1654` → IC=+0.177 (n=500)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1654 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `1.4378` → IC=+0.168 (n=580)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.4378 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `2.5472` → IC=+0.159 (n=579)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.5472 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.152 (n=2045)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.02 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `12330.8778` → IC=+0.156 (n=602)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 12330.8778 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `163.0` → IC=+0.168 (n=1583)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 163.0 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.133 (n=1268)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0057 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.120 (n=1927)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 5.0 (IC base=+0.105)

- **PATRÓN** `ibs_20min` < `0.5224` → IC=+0.142 (n=1672)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.5224 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` < `2.227` → IC=+0.122 (n=1608)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.227 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `3863.6748` → IC=+0.123 (n=1267)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 3863.6748 (IC base=+0.105)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.1102` → IC=+0.139 (n=200)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.1102 (IC base=+0.107)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.149 (n=408)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 9.0 (IC base=+0.107)

- **PATRÓN** `ibs_20min` > `0.2517` → IC=+0.146 (n=453)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.2517 (IC base=+0.107)

- **PATRÓN** `dist_vwap_pct` > `0.3098` → IC=+0.163 (n=158)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.3098 (IC base=+0.107)

- **PATRÓN** `volumen_regimen` < `0.6182` → IC=+0.156 (n=152)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6182 (IC base=+0.107)

- **PATRÓN** `volumen_pendiente_norm` > `0.0881` → IC=+0.127 (n=159)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` > 0.0881 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `12711.7416` → IC=+0.136 (n=405)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 12711.7416 (IC base=+0.107)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.207 (n=203)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.3378` → IC=+0.149 (n=607)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3378 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.142 (n=626)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` < `0.6041` → IC=+0.175 (n=534)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.6041 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.3088` → IC=+0.150 (n=643)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.3088 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.351` → IC=+0.155 (n=236)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 4.351 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` > `1.0609` → IC=+0.164 (n=275)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 1.0609 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.205 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` < `2.0997` → IC=+0.151 (n=525)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.0997 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `1.4135` → IC=+0.141 (n=597)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.4135 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `387.0` → IC=+0.142 (n=574)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 387.0 (IC base=+0.131)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.262 (n=246)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.0977` → IC=+0.213 (n=186)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0977 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.234 (n=257)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `0.7028` → IC=+0.243 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7028 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` > `0.9497` → IC=+0.223 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9497 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.93` → IC=+0.224 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.93 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` < `0.8363` → IC=+0.200 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8363 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` > `1.156` → IC=+0.213 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.156 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.2607` → IC=+0.298 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2607 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` < `1.3913` → IC=+0.240 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3913 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.4036` → IC=+0.230 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4036 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.201 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `12357.9012` → IC=+0.207 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12357.9012 (IC base=+0.193)

- **PATRÓN** `ibs_20min` < `0.0837` → IC=+0.146 (n=176)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.0837 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2258` → IC=+0.127 (n=81)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` > 0.2258 (IC base=+0.087)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` > `0.5227` → IC=-0.161 (n=125)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5227
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=379)

- **FILTRO** `dist_vwap_pct` > `0.3429` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3429
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=470)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.194 (n=181)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0089 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.167 (n=370)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 8.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` > `0.7368` → IC=+0.206 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7368 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` > `0.6368` → IC=+0.216 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6368 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.127` → IC=+0.208 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.127 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `1.0699` → IC=+0.148 (n=347)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.0699 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` > `0.2893` → IC=+0.214 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2893 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` > `2.2252` → IC=+0.169 (n=170)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.2252 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.134 (n=430)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.02 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `3062.644` → IC=+0.202 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3062.644 (IC base=+0.132)

- **PATRÓN** `ibs_20min` < `0.5227` → IC=+0.140 (n=379)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.5227 (IC base=+0.065)

- **PATRÓN** `volumen_spike_ratio` < `1.8646` → IC=+0.139 (n=236)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.8646 (IC base=+0.065)

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
- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.208 (n=3264)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.179 (n=10240)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.216 (n=9798)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4706 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.9803` → IC=+0.206 (n=1376)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9803 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.61` → IC=+0.227 (n=4742)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.61 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `0.8812` → IC=+0.165 (n=4362)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8812 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.2399` → IC=+0.201 (n=1833)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2399 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.6025` → IC=+0.188 (n=3135)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6025 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `2342.629` → IC=+0.172 (n=6527)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2342.629 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `87.0` → IC=+0.195 (n=7412)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 87.0 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.190 (n=5931)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.007 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.1472` → IC=+0.189 (n=3914)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.1472 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.204 (n=3392)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` < `0.5667` → IC=+0.237 (n=8897)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5667 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` < `0.2486` → IC=+0.161 (n=5519)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.2486 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.0` → IC=+0.203 (n=1250)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.0 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.719` → IC=+0.181 (n=8616)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 3.719 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.7043` → IC=+0.160 (n=2695)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.7043 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.241 (n=1165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6332` → IC=+0.192 (n=2715)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6332 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.191 (n=5208)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 48.0 (IC base=+0.180)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.211 (n=556)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.190)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.224 (n=555)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.199 (n=805)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 15.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.200 (n=1120)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.322 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.038` → IC=+0.314 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.038 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.2272` → IC=+0.247 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2272 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` < `1.552` → IC=+0.182 (n=691)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.552 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `2.2444` → IC=+0.200 (n=712)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2444 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.192 (n=994)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.02 (IC base=+0.190)

- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.258 (n=1297)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0078 (IC base=+0.257)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.262 (n=1161)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.257)

- **PATRÓN** `drift_60min` |x|≤ `0.1279` → IC=+0.285 (n=571)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1279 (IC base=+0.257)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.268 (n=1175)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.257)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.258 (n=1180)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.257)

- **PATRÓN** `ibs_20min` < `0.35` → IC=+0.289 (n=1141)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.35 (IC base=+0.257)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.466` → IC=+0.262 (n=1355)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.466 (IC base=+0.257)

- **PATRÓN** `volumen_pendiente_norm` > `0.2802` → IC=+0.284 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2802 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` > `1.8682` → IC=+0.272 (n=791)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8682 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1799.36` → IC=+0.262 (n=864)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1799.36 (IC base=+0.257)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.195 (n=523)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0028 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.0842` → IC=+0.163 (n=523)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.0842 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=1640)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.3123` → IC=+0.204 (n=1567)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3123 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.3455` → IC=+0.196 (n=636)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.3455 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.755` → IC=+0.175 (n=358)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 9.755 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.233` → IC=+0.154 (n=1409)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.233 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.63` → IC=+0.180 (n=523)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.63 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.2681` → IC=+0.208 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2681 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.1137` → IC=+0.163 (n=1331)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 2.1137 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.7583` → IC=+0.156 (n=1008)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.7583 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `15677.0952` → IC=+0.156 (n=711)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 15677.0952 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `477.0` → IC=+0.160 (n=1443)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 477.0 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.165 (n=1357)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0057 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.3224` → IC=+0.162 (n=1357)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.3224 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.178 (n=457)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 18.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` < `0.269` → IC=+0.234 (n=905)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.269 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.1371` → IC=+0.166 (n=1224)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1371 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.313` → IC=+0.161 (n=228)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 11.313 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `1.1862` → IC=+0.162 (n=1357)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1862 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.1514` → IC=+0.198 (n=366)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1514 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.3998` → IC=+0.160 (n=1259)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.3998 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `2.0862` → IC=+0.162 (n=572)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.0862 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `424.0` → IC=+0.157 (n=1022)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 424.0 (IC base=+0.150)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.243 (n=528)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.224 (n=1664)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.223 (n=1607)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `0.6697` → IC=+0.256 (n=1416)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6697 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.809` → IC=+0.294 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.809 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` < `0.2125` → IC=+0.221 (n=1562)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2125 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `2.8416` → IC=+0.243 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8416 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.229 (n=1129)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `1957.842` → IC=+0.221 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1957.842 (IC base=+0.218)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.231 (n=1311)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 53.0 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0115` → IC=+0.240 (n=1477)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0115 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.1659` → IC=+0.239 (n=650)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1659 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.263 (n=563)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.238 (n=693)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.36` → IC=+0.270 (n=1299)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.36 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.751` → IC=+0.280 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.751 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.3447` → IC=+0.300 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3447 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.7536` → IC=+0.234 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7536 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.1905` → IC=+0.236 (n=901)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1905 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.244 (n=1001)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `1878.7384` → IC=+0.250 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1878.7384 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.231 (n=1270)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=+0.234)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.185 (n=557)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0035 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.4373` → IC=+0.143 (n=1669)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.4373 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.149 (n=1749)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` > `0.8762` → IC=+0.260 (n=757)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8762 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.5853` → IC=+0.167 (n=469)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.5853 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.157` → IC=+0.159 (n=693)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 4.157 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `0.8748` → IC=+0.154 (n=1113)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8748 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.2367` → IC=+0.217 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2367 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `1.5214` → IC=+0.147 (n=710)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.5214 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `1.7646` → IC=+0.147 (n=1076)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.7646 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `8101.5764` → IC=+0.229 (n=757)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8101.5764 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `80.0` → IC=+0.149 (n=523)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 80.0 (IC base=+0.135)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.155 (n=1364)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0076 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.4464` → IC=+0.154 (n=1364)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4464 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=512)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.142 (n=621)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.7021` → IC=+0.181 (n=1364)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.7021 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.6022` → IC=+0.142 (n=1508)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.6022 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.137` → IC=+0.178 (n=200)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 11.137 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.8616` → IC=+0.146 (n=910)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.8616 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `1.1938` → IC=+0.141 (n=455)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.1938 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2871` → IC=+0.244 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2871 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.444` → IC=+0.150 (n=1292)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.444 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `10917.9028` → IC=+0.207 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10917.9028 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `179.0` → IC=+0.144 (n=1287)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 179.0 (IC base=+0.136)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.136 (n=1101)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.0081 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.132 (n=1700)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.190 (n=1655)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.4706 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` > `1.081` → IC=+0.204 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.081 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.442` → IC=+0.233 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.442 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `0.8911` → IC=+0.133 (n=1102)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.8911 (IC base=+0.111)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.125 (n=1666)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `2909.4755` → IC=+0.251 (n=551)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2909.4755 (IC base=+0.111)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.130 (n=1266)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 54.0 (IC base=+0.111)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.173 (n=542)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0058 (IC base=+0.111)

- **PATRÓN** `drift_60min` |x|≤ `0.1314` → IC=+0.160 (n=542)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1314 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.123 (n=1680)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 5.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.202 (n=1626)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6364 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` < `0.219` → IC=+0.128 (n=1324)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.219 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.449` → IC=+0.123 (n=1572)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` < 3.449 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `0.717` → IC=+0.151 (n=715)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.717 (IC base=+0.111)

- **PATRÓN** `volumen_pendiente_norm` > `0.2252` → IC=+0.169 (n=252)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2252 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` < `1.4497` → IC=+0.137 (n=488)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.4497 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` > `2.517` → IC=+0.129 (n=488)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 2.517 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `2844.2019` → IC=+0.165 (n=541)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2844.2019 (IC base=+0.111)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0193` → IC=+0.221 (n=1105)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0193 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.215 (n=1733)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.213 (n=1476)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.5146` → IC=+0.251 (n=1656)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5146 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.2021` → IC=+0.235 (n=978)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2021 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.275` → IC=+0.271 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.275 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` < `1.0709` → IC=+0.212 (n=1458)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0709 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` > `0.6363` → IC=+0.218 (n=1656)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6363 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.2344` → IC=+0.250 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2344 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.5103` → IC=+0.236 (n=533)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5103 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.220 (n=1737)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2618.6162` → IC=+0.224 (n=1104)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2618.6162 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0088` → IC=+0.225 (n=594)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0088 (IC base=+0.199)

- **PATRÓN** `sigma_h` > `0.0256` → IC=+0.218 (n=594)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0256 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.207 (n=1262)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.5188` → IC=+0.255 (n=1780)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5188 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `1.2401` → IC=+0.200 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2401 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` < `0.9192` → IC=+0.203 (n=1981)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9192 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.808` → IC=+0.262 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.808 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` > `1.2332` → IC=+0.233 (n=594)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2332 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.2826` → IC=+0.262 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2826 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `2.2045` → IC=+0.195 (n=1405)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.2045 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `1.4328` → IC=+0.196 (n=1596)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4328 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=1067)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.138 (n=2951)

- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.159 (n=2482)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0093 (IC base=+0.150)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.151 (n=2519)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0056 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.5227` → IC=+0.160 (n=2819)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.5227 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.158 (n=947)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 18.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.166 (n=1260)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 6.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.9428` → IC=+0.212 (n=940)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9428 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1905` → IC=+0.155 (n=1028)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1905 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.5007` → IC=+0.143 (n=1696)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.5007 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.12` → IC=+0.181 (n=459)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 10.12 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` > `0.9009` → IC=+0.162 (n=1205)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.9009 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.1723` → IC=+0.183 (n=772)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1723 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `1.4564` → IC=+0.157 (n=929)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.4564 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.8856` → IC=+0.162 (n=1856)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.8856 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `3709.9614` → IC=+0.153 (n=1879)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3709.9614 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.194 (n=742)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0038 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.4871` → IC=+0.154 (n=2226)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4871 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.169 (n=814)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.164 (n=754)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 4.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.0862` → IC=+0.169 (n=742)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.0862 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.9213` → IC=+0.148 (n=339)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.9213 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.4334` → IC=+0.129 (n=2200)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.4334 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.224` → IC=+0.145 (n=2216)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 6.224 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.2455` → IC=+0.141 (n=2123)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.2455 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.0724` → IC=+0.144 (n=1031)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.0724 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.5361` → IC=+0.146 (n=967)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.5361 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.8147` → IC=+0.141 (n=1464)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.8147 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=2951)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `6949.6369` → IC=+0.149 (n=1988)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 6949.6369 (IC base=+0.136)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.170 (n=331)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0056 (IC base=+0.151)

- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.177 (n=125)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0065 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.0895` → IC=+0.188 (n=126)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.0895 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.160 (n=377)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.5452` → IC=+0.188 (n=251)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.5452 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.2158` → IC=+0.154 (n=177)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.2158 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `0.3916` → IC=+0.158 (n=366)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.3916 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.401` → IC=+0.163 (n=399)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 2.401 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` > `0.8487` → IC=+0.186 (n=250)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 0.8487 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.3101` → IC=+0.286 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3101 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `1.4485` → IC=+0.188 (n=126)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.4485 (IC base=+0.151)

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
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0044 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.1253` → IC=+0.158 (n=290)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1253 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.161 (n=611)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 11.0 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.168 (n=302)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 4.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` < `0.5623` → IC=+0.159 (n=579)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.5623 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.8892` → IC=+0.170 (n=289)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.8892 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `1.006` → IC=+0.162 (n=196)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 1.006 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` < `0.4271` → IC=+0.168 (n=804)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.4271 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.684` → IC=+0.162 (n=871)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 6.684 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `0.6357` → IC=+0.154 (n=290)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6357 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` > `0.7179` → IC=+0.158 (n=775)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.7179 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` < `0.1108` → IC=+0.157 (n=800)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` < 0.1108 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.1721` → IC=+0.160 (n=254)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.1721 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.4349` → IC=+0.164 (n=284)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.4349 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.160 (n=848)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.154)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.153 (n=733)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0084 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.3907` → IC=+0.169 (n=644)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.3907 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.163 (n=262)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.148 (n=512)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 11.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.7466` → IC=+0.140 (n=732)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.7466 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.103` → IC=+0.150 (n=732)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` > 0.103 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.6442` → IC=+0.169 (n=164)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.6442 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.3875` → IC=+0.138 (n=741)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.3875 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.738` → IC=+0.153 (n=119)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 10.738 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.281` → IC=+0.140 (n=665)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 4.281 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.6452` → IC=+0.168 (n=245)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.6452 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `0.7259` → IC=+0.140 (n=654)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.7259 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.0733` → IC=+0.166 (n=309)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0733 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.1996` → IC=+0.151 (n=631)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.1996 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.7829` → IC=+0.148 (n=478)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.7829 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `7593.5796` → IC=+0.162 (n=732)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 7593.5796 (IC base=+0.138)

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

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.197 (n=394)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.004 (IC base=+0.098)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.130 (n=832)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 8.0 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.6774` → IC=+0.206 (n=713)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6774 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `0.1549` → IC=+0.160 (n=436)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1549 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.429` → IC=+0.223 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.429 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` > `0.9793` → IC=+0.137 (n=362)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.9793 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` > `0.2818` → IC=+0.195 (n=103)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2818 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` < `2.0809` → IC=+0.140 (n=604)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.0809 (IC base=+0.098)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.125 (n=643)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `2424.4386` → IC=+0.149 (n=351)

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
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.167 (n=304)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.006 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.130 (n=303)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 7.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` > `0.52` → IC=+0.187 (n=273)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.52 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` > `0.1366` → IC=+0.183 (n=143)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1366 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.573` → IC=+0.136 (n=163)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 3.573 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `1.0632` → IC=+0.128 (n=240)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.0632 (IC base=+0.111)

- **PATRÓN** `volumen_pendiente_norm` < `0.067` → IC=+0.141 (n=207)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` < 0.067 (IC base=+0.111)

- **PATRÓN** `volumen_pendiente_norm` > `0.2771` → IC=+0.149 (n=35)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2771 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` < `2.0118` → IC=+0.178 (n=206)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 2.0118 (IC base=+0.111)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.127 (n=282)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `4085.8043` → IC=+0.142 (n=118)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 4085.8043 (IC base=+0.111)

- **PATRÓN** `ibs_20min` < `0.279` → IC=+0.223 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.279 (IC base=+0.051)

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

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.159 (n=203)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0051 (IC base=+0.106)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.142 (n=272)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 8.0 (IC base=+0.106)

- **PATRÓN** `ibs_20min` > `0.6816` → IC=+0.232 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6816 (IC base=+0.106)

- **PATRÓN** `dist_vwap_pct` > `0.3477` → IC=+0.170 (n=110)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.3477 (IC base=+0.106)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.815` → IC=+0.300 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.815 (IC base=+0.106)

- **PATRÓN** `volumen_regimen` > `0.9516` → IC=+0.143 (n=124)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.9516 (IC base=+0.106)

- **PATRÓN** `volumen_pendiente_norm` > `0.283` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.283 (IC base=+0.106)

- **PATRÓN** `volumen_spike_ratio` < `1.7281` → IC=+0.173 (n=148)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.7281 (IC base=+0.106)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.130 (n=182)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `1760.3207` → IC=+0.196 (n=90)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 1760.3207 (IC base=+0.106)

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

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.132 (n=202)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 13.0 (IC base=+0.075)

- **PATRÓN** `ibs_20min` > `0.6744` → IC=+0.175 (n=226)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.6744 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` > `0.2066` → IC=+0.155 (n=143)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.2066 (IC base=+0.075)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.379` → IC=+0.186 (n=100)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 5.379 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.0639` → IC=+0.167 (n=85)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 1.0639 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2443` → IC=+0.180 (n=48)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2443 (IC base=+0.075)

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

- **FILTRO** `hora_utc` < `4.0` → IC=-0.305 (n=39)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.288 (n=130)

- **FILTRO** `dist_vwap_pct` > `0.4139` → IC=-0.413 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4139
  - _Potencial_: sin este filtro IC_bueno=-0.273 (n=148)

- **FILTRO** `sigma_ewma_delta_pct` > `8.488` → IC=-0.306 (n=29)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.488
  - _Potencial_: sin este filtro IC_bueno=-0.289 (n=140)

- **FILTRO** `volumen_pendiente_norm` > `0.0812` → IC=-0.389 (n=16)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0812
  - _Potencial_: sin este filtro IC_bueno=-0.286 (n=68)

- **FILTRO** `volumen_spike_ratio` > `1.948` → IC=-0.409 (n=20)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.948
  - _Potencial_: sin este filtro IC_bueno=-0.273 (n=64)

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

- **FILTRO** `sigma_h` < `0.0017` → IC=-0.289 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0017
  - _Potencial_: sin este filtro IC_bueno=-0.245 (n=53)

- **FILTRO** `dist_vwap_pct` < `0.0689` → IC=-0.314 (n=41)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0689
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=29)

- **FILTRO** `volumen_regimen` > `0.9309` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.9309
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=53)

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
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=324)

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

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.121 (n=233)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.2 (IC base=+0.041)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.0` → IC=+0.136 (n=108)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 6.0 (IC base=+0.041)

- **PATRÓN** `libro_liquidez` > `3787.1326` → IC=+0.153 (n=119)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3787.1326 (IC base=+0.041)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.576` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `ibs_20min` < 0.576
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=82)

- **FILTRO** `volumen_regimen` < `0.7924` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7924
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=82)

- **PATRÓN** `drift_60min` |x|≤ `0.2285` → IC=+0.144 (n=102)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.2285 (IC base=+0.109)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.196 (n=44)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 16.0 (IC base=+0.109)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.154 (n=53)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.109)

- **PATRÓN** `ibs_20min` < `0.113` → IC=+0.182 (n=105)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.113 (IC base=+0.109)

- **PATRÓN** `volumen_pendiente_norm` < `0.1813` → IC=+0.156 (n=88)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.1813 (IC base=+0.109)

- **PATRÓN** `volumen_spike_ratio` < `2.8706` → IC=+0.144 (n=88)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.8706 (IC base=+0.109)

- **PATRÓN** `volumen_spike_ratio` > `1.4478` → IC=+0.133 (n=88)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.4478 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `3574.4675` → IC=+0.164 (n=120)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 3574.4675 (IC base=+0.109)

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
- **PATRÓN** `libro_liquidez` > `2908.9915` → IC=+0.162 (n=229)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2908.9915 (IC base=+0.104)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2908.9915` → IC=+0.162 (n=229)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2908.9915 (IC base=+0.104)

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
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=1716)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9583` → IC=-0.295 (n=37)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9583
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=76)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

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
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=760)

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
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=341)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=341)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.148 (n=86)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=270)

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
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=124)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.191 (n=108)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=261)

- **PATRÓN** `py_entrada` < `0.48` → IC=+0.170 (n=110)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` < 0.48 (IC base=+0.027)

- **PATRÓN** `profundidad_ratio` > `103.8` → IC=+0.173 (n=102)

  - _Acción_: Kelly boost +0.87€ cuando `profundidad_ratio` > 103.8 (IC base=+0.027)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **PATRÓN** `py_entrada` < `0.56` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.56 (IC base=+0.089)

- **PATRÓN** `restante_min` > `11.01` → IC=+0.141 (n=37)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 11.01 (IC base=+0.089)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.141 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 11.0 (IC base=+0.089)

- **PATRÓN** `lag_apertura_s` < `232.79` → IC=+0.132 (n=36)

  - _Acción_: Kelly boost +0.66€ cuando `lag_apertura_s` < 232.79 (IC base=+0.089)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.58` → IC=+0.232 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.58 (IC base=+0.134)

- **PATRÓN** `restante_min` < `3.1` → IC=+0.140 (n=23)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` < 3.1 (IC base=+0.134)

- **PATRÓN** `restante_min` > `3.99` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `restante_min` > 3.99 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.273 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.224 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.134)

- **PATRÓN** `lag_apertura_s` < `60.77` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `lag_apertura_s` < 60.77 (IC base=+0.134)

- **PATRÓN** `profundidad_ratio` > `79.6` → IC=+0.235 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `profundidad_ratio` > 79.6 (IC base=+0.134)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=24)

- **FILTRO** `profundidad_ratio` < `45.3` → IC=-0.328 (n=27)

  - _Acción_: SKIP cuando `profundidad_ratio` < 45.3
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

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
- **FILTRO** `py_entrada` > `0.41` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `py_entrada` > 0.41
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=18)

- **FILTRO** `restante_min` < `3.82` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `restante_min` < 3.82
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=17)

- **FILTRO** `lag_apertura_s` > `71.83` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `lag_apertura_s` > 71.83
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.147 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 17.0 (IC base=+0.038)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `restante_min` < `13.48` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `restante_min` < 13.48
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

- **FILTRO** `lag_apertura_s` > `91.17` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `lag_apertura_s` > 91.17
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **FILTRO** `py_entrada` > `0.54` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.54
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=18)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.51` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.51
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=15)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.232 (n=39)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=23)

- **FILTRO** `restante_min` < `2.58` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `restante_min` < 2.58
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=47)

- **FILTRO** `lag_apertura_s` > `145.1` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `lag_apertura_s` > 145.1
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=47)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=1073)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=5550)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=7438)

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
- **FILTRO** `py_entrada` < `0.47` → IC=-0.173 (n=3253)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=10513)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.169 (n=3559)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=10691)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.212 (n=592)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.101 (n=1793)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.155 (n=630)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=1923)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.199 (n=590)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=1839)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.202 (n=623)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=1926)

- **FILTRO** `ibs_20min` > `0.2812` → IC=-0.162 (n=637)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2812
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=1912)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.170 (n=588)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=1780)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.182 (n=623)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=1926)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `libro_spread` > `0.01` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=2735)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=2911)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=2917)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `ibs_20min` > `0.1705` → IC=-0.148 (n=123)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1705
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=372)

- **FILTRO** `libro_liquidez` < `15744.4242` → IC=-0.132 (n=123)

  - _Acción_: SKIP cuando `libro_liquidez` < 15744.4242
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=372)

- **FILTRO** `libro_liquidez` < `16939.3779` → IC=-0.143 (n=222)

  - _Acción_: SKIP cuando `libro_liquidez` < 16939.3779
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=668)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.214 (n=68)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=241)

- **FILTRO** `ibs_20min` < `0.11` → IC=-0.234 (n=77)

  - _Acción_: SKIP cuando `ibs_20min` < 0.11
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=232)

- **FILTRO** `py_entrada` > `0.625` → IC=-0.279 (n=66)

  - _Acción_: SKIP cuando `py_entrada` > 0.625
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=236)

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
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=21936)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.273 (n=7721)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=23903)

- **FILTRO** `ibs_7min` < `0.2857` → IC=-0.235 (n=7892)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=23732)

- **FILTRO** `ballena_activa_n` > `16.0` → IC=-0.158 (n=10462)

  - _Acción_: SKIP cuando `ballena_activa_n` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=21162)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.229 (n=9724)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=29820)

- **FILTRO** `ibs_7min` > `0.2936` → IC=-0.179 (n=9883)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2936
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=29661)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.306 (n=1245)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=3977)

- **FILTRO** `ibs_7min` < `0.7103` → IC=-0.250 (n=1723)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7103
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=3499)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.186 (n=1204)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=4018)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.259 (n=1680)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=5116)

- **FILTRO** `drift_7min_pct` |x|> `0.1118` → IC=-0.123 (n=2309)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1118
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=4487)

- **FILTRO** `ibs_7min` > `0.7903` → IC=-0.205 (n=1698)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7903
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=5098)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.137 (n=1265)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=4199)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.249 (n=1313)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=4151)

- **FILTRO** `ibs_7min` < `0.7483` → IC=-0.192 (n=1366)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7483
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=4098)

- **FILTRO** `ballena_activa_n` > `161.0` → IC=-0.171 (n=1358)

  - _Acción_: SKIP cuando `ballena_activa_n` > 161.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=4106)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.255 (n=1375)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=4155)

- **FILTRO** `ibs_7min` > `0.2605` → IC=-0.176 (n=1382)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2605
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=4148)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.184 (n=1377)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=4153)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.167 (n=1211)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=3737)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.307 (n=1211)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=3737)

- **FILTRO** `ibs_7min` < `0.1944` → IC=-0.257 (n=1237)

  - _Acción_: SKIP cuando `ibs_7min` < 0.1944
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=3711)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.219 (n=1158)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=3790)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.237 (n=1666)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=5600)

- **FILTRO** `ibs_7min` > `0.75` → IC=-0.176 (n=1812)

  - _Acción_: SKIP cuando `ibs_7min` > 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=5454)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.37` → IC=-0.232 (n=1540)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=3677)

- **FILTRO** `ibs_7min` < `0.7412` → IC=-0.181 (n=1304)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7412
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=3913)

- **FILTRO** `ballena_activa_n` > `32.0` → IC=-0.169 (n=1289)

  - _Acción_: SKIP cuando `ballena_activa_n` > 32.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=3928)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.266 (n=1175)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=4129)

- **FILTRO** `ibs_7min` > `0.275` → IC=-0.176 (n=1325)

  - _Acción_: SKIP cuando `ibs_7min` > 0.275
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=3979)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.186 (n=1322)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=3982)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.36` → IC=-0.260 (n=1339)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=4185)

- **FILTRO** `ibs_7min` < `0.7` → IC=-0.240 (n=1374)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=4150)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.178 (n=1800)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=5721)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.38` → IC=-0.253 (n=1693)

  - _Acción_: SKIP cuando `py_entrada` < 0.38
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=3556)

- **FILTRO** `ibs_7min` < `0.7` → IC=-0.227 (n=1299)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=3950)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.214 (n=1278)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=3971)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.203 (n=1711)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=5416)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=1061)

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
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=1048)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=323)

- **FILTRO** `ballena_activa_n` > `2.0` → IC=-0.138 (n=139)

  - _Acción_: SKIP cuando `ballena_activa_n` > 2.0
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=286)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=552)

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

- **FILTRO** `T_h` < `39.9942` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `T_h` < 39.9942
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=50)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `T_h` > `109.663` → IC=-0.149 (n=186)

  - _Acción_: SKIP cuando `T_h` > 109.663
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=187)

- **FILTRO** `pct_vs_K` |x|> `4.167` → IC=-0.258 (n=93)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.167
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=280)

- **FILTRO** `sigma_h` < `0.0044` → IC=-0.317 (n=80)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0044
  - _Potencial_: sin este filtro IC_bueno=-0.297 (n=240)

- **FILTRO** `T_h` > `63.8116` → IC=-0.326 (n=239)

  - _Acción_: SKIP cuando `T_h` > 63.8116
  - _Potencial_: sin este filtro IC_bueno=-0.235 (n=81)

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
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=752)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=758)

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
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=583)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1108)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=733)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=706)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=2859)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1450)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=1458)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.221 (n=701)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0085 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.0749` → IC=+0.201 (n=680)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0749 (IC base=+0.186)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2134` → IC=+0.193 (n=515)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.96€ cuando `delta_ratio_macro` |x|> 0.2134 (IC base=+0.186)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1267` → IC=+0.227 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1267 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.195 (n=1450)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 6.0 (IC base=+0.186)

- **PATRÓN** `ibs_15` > `0.6071` → IC=+0.264 (n=1545)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6071 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` > `0.1185` → IC=+0.187 (n=812)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1185 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` < `0.6134` → IC=+0.176 (n=1491)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.6134 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.866` → IC=+0.274 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.866 (IC base=+0.186)

- **PATRÓN** `libro_liquidez` > `2979.0729` → IC=+0.193 (n=1030)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2979.0729 (IC base=+0.186)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=577)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.212 (n=356)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.0587` → IC=+0.293 (n=119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0587 (IC base=+0.202)

- **PATRÓN** `drift_15min` |x|≤ `0.3838` → IC=+0.211 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3838 (IC base=+0.202)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2526` → IC=+0.244 (n=119)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2526 (IC base=+0.202)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1446` → IC=+0.262 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1446 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.222 (n=376)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.202)

- **PATRÓN** `ibs_15` > `0.7061` → IC=+0.268 (n=356)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7061 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.4073` → IC=+0.248 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4073 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.537` → IC=+0.268 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.537 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `16040.8773` → IC=+0.244 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16040.8773 (IC base=+0.202)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `24.537` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 24.537
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=357)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.146 (n=159)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0041 (IC base=+0.136)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.158 (n=241)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0051 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.069` → IC=+0.148 (n=160)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.069 (IC base=+0.136)

- **PATRÓN** `delta_ratio_macro` |x|> `0.232` → IC=+0.175 (n=121)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.87€ cuando `delta_ratio_macro` |x|> 0.232 (IC base=+0.136)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2558` → IC=+0.155 (n=256)

  - _Acción_: Kelly boost +0.78€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2558 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.148 (n=362)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.140 (n=378)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 17.0 (IC base=+0.136)

- **PATRÓN** `ibs_15` > `0.662` → IC=+0.245 (n=323)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.662 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.5943` → IC=+0.146 (n=77)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.5943 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.1661` → IC=+0.150 (n=284)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1661 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.307` → IC=+0.196 (n=156)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 8.307 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `9553.1781` → IC=+0.163 (n=164)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 9553.1781 (IC base=+0.136)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.155 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=90)

- **FILTRO** `ibs_15` > `0.2172` → IC=-0.242 (n=29)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.2172
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=88)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.297 (n=62)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.1511` → IC=+0.209 (n=163)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1511 (IC base=+0.173)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0675` → IC=+0.207 (n=165)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0675 (IC base=+0.173)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2704` → IC=+0.226 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2704 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.215 (n=128)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.173)

- **PATRÓN** `ibs_15` > `0.6111` → IC=+0.259 (n=185)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6111 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.122` → IC=+0.200 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.122 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.532` → IC=+0.400 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.532 (IC base=+0.173)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.174 (n=142)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `3071.8702` → IC=+0.279 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3071.8702 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.228 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.173)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.5797` → IC=-0.134 (n=121)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.5797
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=864)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `15.662` → IC=+0.204 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 15.662 (IC base=+0.013)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0177` → IC=+0.238 (n=273)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0177 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.0864` → IC=+0.212 (n=182)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0864 (IC base=+0.188)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0389` → IC=+0.192 (n=410)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.96€ cuando `delta_ratio_macro` |x|> 0.0389 (IC base=+0.188)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0898` → IC=+0.248 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0898 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.226 (n=202)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.188)

- **PATRÓN** `ibs_15` > `0.5488` → IC=+0.284 (n=410)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5488 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` > `0.1329` → IC=+0.209 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1329 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` < `0.8104` → IC=+0.188 (n=472)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.8104 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.92` → IC=+0.223 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.92 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.785` → IC=+0.190 (n=408)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 10.785 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `2910.1242` → IC=+0.277 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2910.1242 (IC base=+0.188)

- **PATRÓN** `ibs_15` < `0.1171` → IC=+0.157 (n=459)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.79€ cuando `ibs_15` < 0.1171 (IC base=+0.046)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.338 (n=269)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.336)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.376 (n=183)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.336)

- **PATRÓN** `drift_60min` |x|≤ `0.1105` → IC=+0.343 (n=271)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1105 (IC base=+0.336)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1426` → IC=+0.359 (n=268)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1426 (IC base=+0.336)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1284` → IC=+0.373 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1284 (IC base=+0.336)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.385 (n=190)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.336)

- **PATRÓN** `ibs_15` > `0.7862` → IC=+0.381 (n=402)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7862 (IC base=+0.336)

- **PATRÓN** `dist_vwap_pct` > `0.4406` → IC=+0.384 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4406 (IC base=+0.336)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.188` → IC=+0.340 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.188 (IC base=+0.336)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.899` → IC=+0.337 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.899 (IC base=+0.336)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.343 (n=495)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.336)

- **PATRÓN** `libro_liquidez` > `3532.4883` → IC=+0.351 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3532.4883 (IC base=+0.336)

- **PATRÓN** `ballena_activa_n` < `469.0` → IC=+0.358 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 469.0 (IC base=+0.336)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.351 (n=199)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.341)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.370 (n=75)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.341)

- **PATRÓN** `drift_60min` |x|≤ `0.0571` → IC=+0.359 (n=76)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0571 (IC base=+0.341)

- **PATRÓN** `drift_15min` |x|≤ `0.4288` → IC=+0.353 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4288 (IC base=+0.341)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0705` → IC=+0.350 (n=225)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0705 (IC base=+0.341)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1231` → IC=+0.383 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1231 (IC base=+0.341)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.368 (n=210)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.341)

- **PATRÓN** `ibs_15` > `0.8166` → IC=+0.377 (n=225)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8166 (IC base=+0.341)

- **PATRÓN** `dist_vwap_pct` > `0.4075` → IC=+0.408 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4075 (IC base=+0.341)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.152` → IC=+0.348 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.152 (IC base=+0.341)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.922` → IC=+0.345 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.922 (IC base=+0.341)

- **PATRÓN** `libro_liquidez` > `15700.521` → IC=+0.357 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15700.521 (IC base=+0.341)

- **PATRÓN** `ballena_activa_n` < `574.0` → IC=+0.388 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 574.0 (IC base=+0.341)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.381 (n=82)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.328)

- **PATRÓN** `drift_60min` |x|≤ `0.1062` → IC=+0.343 (n=119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1062 (IC base=+0.328)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0897` → IC=+0.351 (n=159)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0897 (IC base=+0.328)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.358 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.328)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.395 (n=84)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.328)

- **PATRÓN** `ibs_15` > `0.7401` → IC=+0.388 (n=177)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7401 (IC base=+0.328)

- **PATRÓN** `dist_vwap_pct` > `0.4658` → IC=+0.379 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4658 (IC base=+0.328)

- **PATRÓN** `dist_vwap_pct` < `0.1274` → IC=+0.335 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1274 (IC base=+0.328)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.639` → IC=+0.342 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.639 (IC base=+0.328)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.694` → IC=+0.332 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.694 (IC base=+0.328)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.342 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.328)

- **PATRÓN** `libro_liquidez` > `3534.509` → IC=+0.350 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3534.509 (IC base=+0.328)

- **PATRÓN** `ballena_activa_n` < `164.0` → IC=+0.341 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 164.0 (IC base=+0.328)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0131` → IC=-0.220 (n=645)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0131
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=1939)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.190 (n=871)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1713)

- **FILTRO** `libro_liquidez` < `3914.9244` → IC=-0.137 (n=1705)

  - _Acción_: SKIP cuando `libro_liquidez` < 3914.9244
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=879)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1366` → IC=+0.251 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1366 (IC base=-0.062)

- **PATRÓN** `ibs_15` > `0.6349` → IC=+0.271 (n=621)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6349 (IC base=-0.062)

- **PATRÓN** `dist_vwap_pct` < `0.2815` → IC=+0.181 (n=490)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.2815 (IC base=-0.062)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1193` → IC=+0.243 (n=1119)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1193 (IC base=-0.035)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1774` → IC=+0.235 (n=1082)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1774 (IC base=-0.035)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.276 (n=1680)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.035)

- **PATRÓN** `dist_vwap_pct` > `0.9674` → IC=+0.296 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9674 (IC base=-0.035)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0068` → IC=-0.216 (n=392)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=1180)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.232 (n=393)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=1179)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.208 (n=999)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=573)

- **FILTRO** `sigma_ewma_delta_pct` > `19.574` → IC=-0.246 (n=281)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.574
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=1291)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.162 (n=149)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0028 (IC base=+0.078)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2023` → IC=+0.285 (n=77)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2023 (IC base=+0.078)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1378` → IC=+0.319 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1378 (IC base=+0.078)

- **PATRÓN** `ibs_15` > `0.7466` → IC=+0.324 (n=168)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7466 (IC base=+0.078)

- **PATRÓN** `dist_vwap_pct` > `0.1071` → IC=+0.280 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1071 (IC base=+0.078)

- **PATRÓN** `dist_vwap_pct` < `0.581` → IC=+0.272 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.581 (IC base=+0.078)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.6647` → IC=-0.200 (n=98)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6647
  - _Potencial_: sin este filtro IC_bueno=+0.265 (n=296)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.162 (n=377)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.188 (n=197)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0051 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.0768` → IC=+0.214 (n=131)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0768 (IC base=+0.149)

- **PATRÓN** `drift_15min` |x|≤ `0.4223` → IC=+0.163 (n=99)

  - _Acción_: Kelly boost +0.82€ cuando `drift_15min` |x|≤ 0.4223 (IC base=+0.149)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1323` → IC=+0.153 (n=197)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.77€ cuando `delta_ratio_macro` |x|> 0.1323 (IC base=+0.149)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2883` → IC=+0.235 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2883 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.204 (n=140)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.149)

- **PATRÓN** `ibs_15` > `0.6647` → IC=+0.265 (n=296)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6647 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.4822` → IC=+0.171 (n=83)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.4822 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.1663` → IC=+0.177 (n=227)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1663 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.024` → IC=+0.161 (n=252)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 9.024 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.162 (n=377)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `11008.7835` → IC=+0.199 (n=134)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 11008.7835 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.263 (n=222)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.4431` → IC=+0.224 (n=664)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4431 (IC base=+0.224)

- **PATRÓN** `drift_15min` |x|≤ `0.7872` → IC=+0.230 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7872 (IC base=+0.224)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2011` → IC=+0.253 (n=301)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2011 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.229 (n=260)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.240 (n=294)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.224)

- **PATRÓN** `ibs_15` < `0.2696` → IC=+0.277 (n=584)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2696 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.7785` → IC=+0.300 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7785 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.806` → IC=+0.241 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.806 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.189` → IC=+0.229 (n=709)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.189 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `3552.4266` → IC=+0.223 (n=663)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3552.4266 (IC base=+0.224)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1671` → IC=-0.221 (n=206)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1671
  - _Potencial_: sin este filtro IC_bueno=-0.139 (n=402)

- **FILTRO** `drift_15min` |x|> `0.8922` → IC=-0.265 (n=151)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8922
  - _Potencial_: sin este filtro IC_bueno=-0.134 (n=457)

- **PATRÓN** `ibs_15` > `0.8889` → IC=+0.342 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8889 (IC base=-0.167)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0758` → IC=+0.224 (n=270)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0758 (IC base=-0.042)

- **PATRÓN** `ibs_15` < `0.3529` → IC=+0.263 (n=302)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3529 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` > `0.4961` → IC=+0.211 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4961 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` < `0.199` → IC=+0.220 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.199 (IC base=-0.042)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0198` → IC=-0.259 (n=380)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0198
  - _Potencial_: sin este filtro IC_bueno=-0.135 (n=381)

- **FILTRO** `drift_15min` |x|> `1.2406` → IC=-0.260 (n=190)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2406
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=571)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.265 (n=185)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=576)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1316` → IC=+0.277 (n=204)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1316 (IC base=-0.046)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.103` → IC=+0.348 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.103 (IC base=-0.046)

- **PATRÓN** `ibs_15` < `0.3457` → IC=+0.308 (n=451)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3457 (IC base=-0.046)

- **PATRÓN** `dist_vwap_pct` > `0.932` → IC=+0.352 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.932 (IC base=-0.046)

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
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.295 (n=432)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.290)

- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.290 (n=294)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0054 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.057` → IC=+0.321 (n=216)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.057 (IC base=+0.290)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2389` → IC=+0.303 (n=216)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2389 (IC base=+0.290)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1073` → IC=+0.345 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1073 (IC base=+0.290)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.320 (n=591)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.290)

- **PATRÓN** `ibs_15` > `0.838` → IC=+0.326 (n=648)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.838 (IC base=+0.290)

- **PATRÓN** `dist_vwap_pct` > `0.1594` → IC=+0.320 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1594 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.101` → IC=+0.329 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.101 (IC base=+0.290)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.294 (n=794)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.290)

- **PATRÓN** `libro_liquidez` > `13081.1746` → IC=+0.304 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13081.1746 (IC base=+0.290)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.311 (n=120)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.288 (n=163)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.0574` → IC=+0.344 (n=120)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0574 (IC base=+0.284)

- **PATRÓN** `delta_ratio_macro` |x|> `0.26` → IC=+0.303 (n=120)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.26 (IC base=+0.284)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3796` → IC=+0.305 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3796 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.303 (n=379)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.284)

- **PATRÓN** `ibs_15` > `0.83` → IC=+0.312 (n=360)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.83 (IC base=+0.284)

- **PATRÓN** `dist_vwap_pct` > `0.4456` → IC=+0.351 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4456 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.589` → IC=+0.355 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.589 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `16111.0352` → IC=+0.328 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16111.0352 (IC base=+0.284)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.307 (n=288)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.297)

- **PATRÓN** `drift_60min` |x|≤ `0.1127` → IC=+0.299 (n=192)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1127 (IC base=+0.297)

- **PATRÓN** `delta_ratio_macro` |x|> `0.226` → IC=+0.316 (n=96)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.226 (IC base=+0.297)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.288` → IC=+0.336 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.288 (IC base=+0.297)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.332 (n=260)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.297)

- **PATRÓN** `ibs_15` > `0.846` → IC=+0.338 (n=288)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.846 (IC base=+0.297)

- **PATRÓN** `dist_vwap_pct` > `0.2966` → IC=+0.309 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2966 (IC base=+0.297)

- **PATRÓN** `dist_vwap_pct` < `0.1715` → IC=+0.297 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1715 (IC base=+0.297)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.169` → IC=+0.315 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.169 (IC base=+0.297)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.310 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.297)

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

- **PATRÓN** `T_h` < `111.9952` → IC=+0.287 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 111.9952 (IC base=+0.281)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6071 sube el IC de +0.186 a +0.264 en UPDOWN_GBM#15min (n=1545). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7061 sube el IC de +0.202 a +0.268 en UPDOWN_GBM#BTC#15min (n=356). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.662 sube el IC de +0.136 a +0.245 en UPDOWN_GBM#ETH#15min (n=323). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6111 sube el IC de +0.173 a +0.259 en UPDOWN_GBM#SOL#15min (n=185). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5488 sube el IC de +0.188 a +0.284 en UPDOWN_GBM#XRP#15min (n=410). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1171 sube el IC de +0.046 a +0.157 en UPDOWN_GBM#XRP#15min (n=459). Ya aplicado como kelly_boost=+0.79€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6349 sube el IC de -0.062 a +0.271 en UPDOWN_GBM_15M_TARDIO (n=621). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.035 a +0.276 en UPDOWN_GBM_15M_TARDIO (n=1680). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7466 sube el IC de +0.078 a +0.324 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=168). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6647 sube el IC de +0.149 a +0.265 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=296). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.2696 sube el IC de +0.224 a +0.277 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=584). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8889 sube el IC de -0.167 a +0.342 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3529 sube el IC de -0.042 a +0.263 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=302). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3457 sube el IC de -0.046 a +0.308 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=451). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.838 sube el IC de +0.290 a +0.326 en UPDOWN_GBM_IBS_ALTO (n=648). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.83 sube el IC de +0.284 a +0.312 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=360). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.846 sube el IC de +0.297 a +0.338 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=288). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7862 sube el IC de +0.336 a +0.381 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=402). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8166 sube el IC de +0.341 a +0.377 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=225). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7401 sube el IC de +0.328 a +0.388 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=177). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1304 | +0.099 | +194.76€ | 1 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1304 | +0.099 | +194.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 970 | +0.109 | +168.84€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 970 | +0.109 | +168.84€ | 2 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 248 | +0.052 | +7.26€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 248 | +0.052 | +7.26€ | 6 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 60 | +0.145 | +20.16€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 60 | +0.145 | +20.16€ | 0 | 6 |
| ✅ BALLENAS_TARDIAS | 24720 | -0.091 | -3145.89€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1435 | -0.048 | -222.31€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 23285 | -0.094 | -2923.59€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3640 | -0.089 | -577.06€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3640 | -0.089 | -577.06€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1435 | -0.048 | -222.31€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1435 | -0.048 | -222.31€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 374 | -0.136 | -161.05€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 374 | -0.136 | -161.05€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 7145 | -0.023 | -652.66€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 7145 | -0.023 | -652.66€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 6619 | -0.098 | -452.53€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 6619 | -0.098 | -452.53€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 5507 | -0.183 | -1080.29€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 5507 | -0.183 | -1080.29€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 17534 | -0.029 | +4081.13€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 4586 | +0.000 | +1830.62€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 12948 | -0.039 | +2250.51€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 17534 | -0.029 | +4081.13€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 4586 | +0.000 | +1830.62€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 12948 | -0.039 | +2250.51€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 90818 | +0.112 | -4646.43€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 13763 | +0.185 | -442.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 363 | -0.089 | -50.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 70758 | +0.100 | -3944.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 5934 | +0.108 | -208.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 11770 | +0.098 | -1011.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 44 | -0.174 | -3.33€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 11711 | +0.099 | -996.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 18369 | +0.132 | -377.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4324 | +0.202 | -145.32€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 11729 | +0.112 | -182.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2274 | +0.105 | -27.60€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 11809 | +0.089 | -1108.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 51 | -0.085 | -5.77€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 11743 | +0.090 | -1091.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 19333 | +0.123 | -403.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 5321 | +0.175 | -81.02€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 11853 | +0.105 | -262.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2147 | +0.098 | -51.68€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 17751 | +0.114 | -1040.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 3978 | +0.188 | -214.99€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 266 | -0.049 | +3.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 11994 | +0.091 | -699.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1513 | +0.127 | -129.61€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 11786 | +0.100 | -704.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 45 | -0.032 | +7.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 11728 | +0.101 | -711.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 14403 | +0.192 | -931.34€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 14403 | +0.192 | -931.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 3440 | +0.169 | -361.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 3440 | +0.169 | -361.27€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1160 | +0.198 | -4.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1160 | +0.198 | -4.14€ | 4 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 3383 | +0.181 | -286.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 3383 | +0.181 | -286.98€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3020 | +0.239 | -97.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3020 | +0.239 | -97.63€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 3321 | +0.194 | -195.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 3321 | +0.194 | -195.07€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 678 | +0.431 | -17.45€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 678 | +0.431 | -17.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 261 | +0.435 | -3.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 261 | +0.435 | -3.79€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 255 | +0.438 | -1.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 255 | +0.438 | -1.90€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 154 | +0.404 | -10.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 154 | +0.404 | -10.72€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 49577 | +0.197 | -3944.05€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 49577 | +0.197 | -3944.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 8587 | +0.175 | -1013.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 8587 | +0.175 | -1013.97€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 7914 | +0.222 | -300.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 7914 | +0.222 | -300.75€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 8558 | +0.172 | -1040.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 8558 | +0.172 | -1040.52€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 8012 | +0.218 | -319.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 8012 | +0.218 | -319.40€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 8188 | +0.203 | -548.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 8188 | +0.203 | -548.80€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 8318 | +0.194 | -720.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 8318 | +0.194 | -720.61€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 18679 | +0.118 | +164.54€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 18679 | +0.118 | +164.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 9274 | +0.123 | +152.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 9274 | +0.123 | +152.32€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 9405 | +0.113 | +12.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 9405 | +0.113 | +12.22€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1441 | +0.293 | -3.40€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1441 | +0.293 | -3.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 643 | +0.280 | -12.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 643 | +0.280 | -12.94€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 693 | +0.296 | +7.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 693 | +0.296 | +7.51€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 105 | +0.341 | +2.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 105 | +0.341 | +2.03€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 629 | +0.440 | +2.47€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 629 | +0.440 | +2.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 296 | +0.440 | +0.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 296 | +0.440 | +0.77€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 292 | +0.442 | +1.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 292 | +0.442 | +1.69€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 41 | +0.384 | +0.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 41 | +0.384 | +0.01€ | 0 | 1 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1084 | +0.076 | -39.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 375 | +0.062 | -28.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 709 | +0.084 | -10.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 61 | +0.119 | +3.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 61 | +0.119 | +3.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 855 | +0.083 | -14.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 146 | +0.081 | -3.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 709 | +0.084 | -10.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 168 | +0.024 | -28.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 168 | +0.024 | -28.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 34474 | +0.097 | -1102.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 2853 | +0.088 | +14.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 31621 | +0.097 | -1116.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 19390 | +0.101 | -334.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 2853 | +0.088 | +14.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 16537 | +0.103 | -349.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 6437 | +0.106 | -48.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 6437 | +0.106 | -48.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 8647 | +0.080 | -718.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 8647 | +0.080 | -718.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 792 | +0.214 | -97.65€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 792 | +0.214 | -97.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 792 | +0.214 | -97.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 792 | +0.214 | -97.65€ | 2 | 4 |
| ✅ GBM_LATE_15M | 24810 | +0.082 | +11690.95€ | 0 | 17 |
| ✅ GBM_LATE_15M#15min | 24810 | +0.082 | +11690.95€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 4140 | +0.192 | +2995.56€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 4140 | +0.192 | +2995.56€ | 0 | 19 |
| ✅ GBM_LATE_15M#BTC | 3673 | +0.177 | +2541.62€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 3673 | +0.177 | +2541.62€ | 0 | 25 |
| ✅ GBM_LATE_15M#DOGE | 4296 | +0.199 | +3222.77€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 4296 | +0.199 | +3222.77€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 3675 | +0.018 | +750.88€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 3675 | +0.018 | +750.88€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 3571 | -0.033 | +808.43€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 3571 | -0.033 | +808.43€ | 4 | 15 |
| ✅ GBM_LATE_15M#XRP | 5455 | -0.042 | +1371.69€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 5455 | -0.042 | +1371.69€ | 4 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 26195 | +0.085 | +13653.62€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 26195 | +0.085 | +13653.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 4959 | +0.016 | +2631.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 4959 | +0.016 | +2631.04€ | 1 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 5457 | +0.014 | +1125.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 5457 | +0.014 | +1125.47€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 3719 | +0.262 | +3743.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 3719 | +0.262 | +3743.29€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 4243 | +0.001 | +777.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 4243 | +0.001 | +777.37€ | 2 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 4266 | +0.027 | +1595.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 4266 | +0.027 | +1595.55€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 3551 | +0.275 | +3780.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 3551 | +0.275 | +3780.90€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 20002 | +0.168 | +14869.99€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 20002 | +0.168 | +14869.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 3012 | +0.205 | +2376.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 3012 | +0.205 | +2376.15€ | 0 | 18 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 3185 | +0.149 | +2324.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 3185 | +0.149 | +2324.46€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 3132 | +0.208 | +2488.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 3132 | +0.208 | +2488.54€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 3358 | +0.133 | +2325.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 3358 | +0.133 | +2325.22€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 3720 | +0.116 | +2523.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 3720 | +0.116 | +2523.59€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 3595 | +0.203 | +2832.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 3595 | +0.203 | +2832.02€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 4939 | +0.126 | +2036.42€ | 0 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 4939 | +0.126 | +2036.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 184 | +0.118 | +76.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 184 | +0.118 | +76.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1412 | +0.121 | +626.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1412 | +0.121 | +626.13€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 372 | +0.144 | +178.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 372 | +0.144 | +178.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1438 | +0.142 | +626.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1438 | +0.142 | +626.15€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1029 | +0.099 | +312.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1029 | +0.099 | +312.52€ | 2 | 12 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 504 | +0.134 | +216.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 504 | +0.134 | +216.54€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 24913 | +0.174 | +18435.76€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 24913 | +0.174 | +18435.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 3946 | +0.220 | +3311.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 3946 | +0.220 | +3311.88€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 3898 | +0.150 | +2573.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 3898 | +0.150 | +2573.53€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 4080 | +0.226 | +3516.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 4080 | +0.226 | +3516.87€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 4042 | +0.136 | +2721.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 4042 | +0.136 | +2721.60€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 4366 | +0.111 | +2709.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 4366 | +0.111 | +2709.34€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 4581 | +0.205 | +3602.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 4581 | +0.205 | +3602.55€ | 0 | 24 |
| ✅ GBM_LATE_5M | 6724 | +0.144 | +3755.94€ | 1 | 28 |
| ✅ GBM_LATE_5M#5min | 6724 | +0.144 | +3755.94€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 594 | +0.186 | +416.56€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 594 | +0.186 | +416.56€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1733 | +0.141 | +1103.21€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1733 | +0.141 | +1103.21€ | 0 | 28 |
| ✅ GBM_LATE_5M#DOGE | 889 | +0.171 | +564.50€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 889 | +0.171 | +564.50€ | 0 | 22 |
| ✅ GBM_LATE_5M#ETH | 2131 | +0.146 | +1172.19€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2131 | +0.146 | +1172.19€ | 0 | 31 |
| ✅ GBM_LATE_5M#SOL | 558 | +0.098 | +183.16€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 558 | +0.098 | +183.16€ | 0 | 15 |
| ✅ GBM_LATE_5M#XRP | 819 | +0.115 | +316.33€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 819 | +0.115 | +316.33€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1657 | +0.071 | +737.26€ | 2 | 15 |
| ✅ GBM_LATE_60M#60min | 1657 | +0.071 | +737.26€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 596 | +0.092 | +261.44€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 596 | +0.092 | +261.44€ | 0 | 15 |
| ✅ GBM_LATE_60M#ETH | 551 | +0.073 | +285.63€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 551 | +0.073 | +285.63€ | 2 | 16 |
| ✅ GBM_LATE_60M#SOL | 510 | +0.043 | +190.19€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 510 | +0.043 | +190.19€ | 1 | 12 |
| 🚫 GBM_LATE_60M_FADE | 363 | -0.259 | -27.59€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 363 | -0.259 | -27.59€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 138 | -0.229 | -12.35€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 138 | -0.229 | -12.35€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 121 | -0.256 | -8.96€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 121 | -0.256 | -8.96€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 104 | -0.292 | -6.28€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 104 | -0.292 | -6.28€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 679 | +0.065 | +134.51€ | 1 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 679 | +0.065 | +134.51€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 268 | +0.056 | +45.58€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 268 | +0.056 | +45.58€ | 2 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 194 | +0.031 | +2.52€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 194 | +0.031 | +2.52€ | 2 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 217 | +0.107 | +86.41€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 217 | +0.107 | +86.41€ | 2 | 12 |
| ✅ LATE_WINDOW_5MIN | 95 | +0.253 | +75.39€ | 0 | 9 |
| ✅ LATE_WINDOW_5MIN#5min | 95 | +0.253 | +75.39€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 95 | +0.253 | +75.39€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 95 | +0.253 | +75.39€ | 0 | 9 |
| ✅ LEADLAG_BTC_XRP_15M | 1870 | +0.096 | +495.06€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 1870 | +0.096 | +495.06€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 1870 | +0.096 | +495.06€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 1870 | +0.096 | +495.06€ | 0 | 1 |
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
| ✅ LIQUIDACIONES_5M | 1914 | +0.004 | +12.46€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1914 | +0.004 | +12.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 103 | +0.024 | +0.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 103 | +0.024 | +0.01€ | 0 | 2 |
| ✅ LIQUIDACIONES_5M#BTC | 207 | -0.007 | +11.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 207 | -0.007 | +11.30€ | 5 | 3 |
| ✅ LIQUIDACIONES_5M#DOGE | 155 | -0.041 | -8.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 155 | -0.041 | -8.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 807 | +0.027 | +22.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 807 | +0.027 | +22.87€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 467 | -0.001 | -5.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 467 | -0.001 | -5.46€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 175 | -0.042 | -8.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 175 | -0.042 | -8.26€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M | 1058 | -0.048 | -31.48€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1058 | -0.048 | -31.48€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 301 | -0.045 | -13.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 301 | -0.045 | -13.58€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 352 | -0.034 | -3.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 352 | -0.034 | -3.94€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 405 | -0.063 | -13.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 405 | -0.063 | -13.96€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 773 | -0.025 | +5.46€ | 1 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 347 | -0.021 | +4.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 426 | -0.028 | +1.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 23 | -0.020 | +1.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 13 | +0.065 | +3.90€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 10 | -0.083 | -2.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 194 | +0.071 | +45.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 85 | +0.063 | +16.70€ | 0 | 4 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 109 | +0.077 | +28.66€ | 0 | 7 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 126 | -0.078 | -14.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 57 | -0.059 | -4.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 69 | -0.091 | -9.86€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 126 | -0.070 | -11.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 55 | -0.097 | -8.65€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 71 | -0.048 | -2.41€ | 3 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 120 | -0.025 | -1.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 61 | -0.024 | +1.56€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 59 | -0.025 | -3.01€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 184 | -0.059 | -14.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 76 | -0.051 | -4.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 108 | -0.064 | -9.29€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M | 14302 | -0.012 | -207.32€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14302 | -0.012 | -207.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 3019 | -0.021 | -60.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 3019 | -0.021 | -60.51€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 3075 | -0.015 | -29.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 3075 | -0.015 | -29.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 28016 | -0.008 | +1208.88€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 28016 | -0.008 | +1208.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 4938 | +0.016 | +592.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 4938 | +0.016 | +592.27€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 4358 | -0.029 | -57.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 4358 | -0.029 | -57.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 4978 | +0.014 | +449.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 4978 | +0.014 | +449.18€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 4141 | -0.053 | -152.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 4141 | -0.053 | -152.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 4684 | -0.012 | +173.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 4684 | -0.012 | +173.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 4917 | +0.007 | +204.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 4917 | +0.007 | +204.88€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 5747 | -0.056 | -131.30€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 5747 | -0.056 | -131.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1203 | +0.000 | -15.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1203 | +0.000 | -15.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1385 | -0.080 | -37.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1385 | -0.080 | -37.17€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 43 | -0.122 | -5.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 43 | -0.122 | -5.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 611 | -0.115 | -19.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 611 | -0.115 | -19.32€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1658 | -0.075 | -28.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1658 | -0.075 | -28.13€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 71168 | -0.072 | +1734.14€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 71168 | -0.072 | +1734.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 12018 | -0.079 | +713.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 12018 | -0.079 | +713.02€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 10994 | -0.092 | -465.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 10994 | -0.092 | -465.52€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 12214 | -0.067 | +681.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 12214 | -0.067 | +681.36€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 10521 | -0.092 | -145.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 10521 | -0.092 | -145.73€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 13045 | -0.048 | +379.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 13045 | -0.048 | +379.25€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 12376 | -0.063 | +571.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 12376 | -0.063 | +571.77€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 7450 | -0.023 | -109.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 7450 | -0.023 | -109.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1649 | -0.025 | +0.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1649 | -0.025 | +0.29€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1003 | -0.020 | -31.30€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2032 | -0.017 | -17.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2032 | -0.017 | -17.37€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1032 | -0.041 | -17.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1032 | -0.041 | -17.42€ | 3 | 0 |
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
| ✅ ORDER_FLOW_5M_REACTIVO | 447 | -0.061 | -54.19€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 447 | -0.061 | -54.19€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 96 | -0.020 | +0.01€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 96 | -0.020 | +0.01€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 54 | -0.125 | -15.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 54 | -0.125 | -15.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 128 | -0.077 | -24.50€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 128 | -0.077 | -24.50€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 95 | -0.005 | +0.19€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 95 | -0.005 | +0.19€ | 0 | 0 |
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
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 84 | -0.035 | +11.21€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 22 | +0.042 | +6.69€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 441 | -0.132 | -57.70€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 114 | +0.009 | +17.52€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 693 | -0.208 | -32.85€ | 4 | 0 |
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
| ✅ STREAK_FADE_5M | 2726 | -0.023 | -113.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2726 | -0.023 | -113.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 566 | -0.023 | -23.32€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 566 | -0.023 | -23.32€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 155 | -0.048 | -14.93€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 155 | -0.048 | -14.93€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1201 | -0.022 | -48.21€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1201 | -0.022 | -48.21€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 73 | -0.060 | -7.39€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 73 | -0.060 | -7.39€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 35 | -0.013 | -2.95€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 35 | -0.013 | -2.95€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 7628 | +0.023 | +110.56€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 7628 | +0.023 | +110.56€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2131 | +0.021 | +20.86€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2131 | +0.021 | +20.86€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1701 | +0.034 | +50.24€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1701 | +0.034 | +50.24€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2315 | +0.011 | +1.09€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2315 | +0.011 | +1.09€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1481 | +0.030 | +38.39€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1481 | +0.030 | +38.39€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 7162 | +0.011 | -49.79€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 7162 | +0.011 | -49.79€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 2878 | +0.014 | -12.54€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 2878 | +0.014 | -12.54€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 2802 | +0.011 | -19.63€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 2802 | +0.011 | -19.63€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1482 | +0.003 | -17.62€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1482 | +0.003 | -17.62€ | 2 | 0 |
| ✅ UPDOWN_GBM | 35778 | +0.030 | +2089.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 9669 | +0.066 | +1710.97€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 1325 | +0.004 | +5.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 22467 | +0.019 | +352.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 2178 | +0.007 | +20.54€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 3603 | +0.065 | +376.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 619 | +0.144 | +234.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 29 | -0.016 | -0.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 2955 | +0.050 | +142.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 6619 | +0.035 | +442.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1227 | +0.083 | +268.84€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 360 | +0.019 | +7.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 4001 | +0.031 | +148.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 978 | +0.004 | +17.10€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 53 | -0.100 | +0.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 4169 | +0.040 | +250.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 572 | +0.141 | +206.32€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 27 | -0.017 | -2.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 3570 | +0.024 | +46.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 7619 | +0.017 | +274.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 2496 | +0.045 | +266.45€ | 0 | 12 |
| ✅ UPDOWN_GBM#ETH#240min | 348 | +0.006 | +6.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 3988 | +0.005 | +2.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 742 | +0.003 | -4.35€ | 2 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 45 | -0.138 | +3.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 8588 | +0.015 | +214.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 2375 | +0.026 | +165.18€ | 0 | 11 |
| ✅ UPDOWN_GBM#SOL#240min | 342 | -0.006 | -3.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 5374 | +0.012 | +46.84€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 458 | +0.020 | +7.79€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 39 | -0.159 | -2.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 5178 | +0.034 | +532.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 2380 | +0.079 | +569.84€ | 0 | 12 |
| ✅ UPDOWN_GBM#XRP#240min | 219 | -0.002 | -3.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 2579 | -0.003 | -34.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 137 | -0.133 | +2.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 536 | +0.336 | +156.53€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 536 | +0.336 | +156.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 300 | +0.341 | +84.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 300 | +0.341 | +84.74€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 236 | +0.328 | +71.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 236 | +0.328 | +71.79€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 11583 | -0.041 | +2369.80€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 11583 | -0.041 | +2369.80€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 717 | -0.042 | +334.37€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 717 | -0.042 | +334.37€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2160 | -0.123 | +15.00€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2160 | -0.123 | +15.00€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 354 | +0.180 | +236.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 354 | +0.180 | +236.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1278 | +0.201 | +731.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1278 | +0.201 | +731.88€ | 2 | 23 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 3530 | -0.064 | +532.23€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 3530 | -0.064 | +532.23€ | 2 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 3544 | -0.078 | +520.20€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 3544 | -0.078 | +520.20€ | 3 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 137 | +0.040 | +8.30€ | 2 | 2 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 137 | +0.040 | +8.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 137 | +0.040 | +8.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 137 | +0.040 | +8.30€ | 2 | 2 |
| ✅ UPDOWN_GBM_IBS_ALTO | 862 | +0.290 | +696.76€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 862 | +0.290 | +696.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 479 | +0.284 | +361.92€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 479 | +0.284 | +361.92€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 383 | +0.297 | +334.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 383 | +0.297 | +334.84€ | 0 | 10 |
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
| ✅ WEEKLY_PRICE#BTC | 803 | +0.248 | +108.30€ | 0 | 5 |
| ✅ WEEKLY_PRICE#ETH | 869 | +0.288 | +362.56€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 660 | +0.376 | +690.02€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.059) — sin ventaja clara. oversold(IBS<0.3): IC=+0.046 n=12627 | neutral: IC=+0.027 n=13488 | overbought(IBS>0.7): IC=+0.086 n=12759
  - _Datos_: n=40251 IC=+0.053 PNL=+4773.75€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 520 celda(s) pasan gate riguroso completo de 2211 evaluadas (n>=40) y 3203 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.026 < 0.08 — monitorear
  - _Datos_: n=2374 IC=+0.026 PNL=+164.70€

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

**⏳ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: 15
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: Falta 11 ops más en GBM@18h (IC actual=-0.067)
  - _Datos_: n=4 IC=-0.067 PNL=-3.02€

**⏳ H-HORA-GBM** — hora_utc causal automático en GBM (forward)
  - _Umbral_: n≥20 forward con hora_utc + alguna hora con n≥15 IC<-0.10 o >+0.10
  - _Acción_: El sistema lo aplica automáticamente vía FEATURE_RULES. Verificar en strategy_params.json.
  - _Estado_: 35661 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.099 n=290/60 | contraria IC=+0.150 n=281 | gap=-0.051 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=278, boost estimado=+0.003. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 171 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=740/40 IC=+0.003 PNL=-4.33€ | BTC#60min: n=975/40 IC=+0.004 PNL=+16.38€ | SOL#60min: n=457/40 IC=+0.018 PNL=+7.34€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.050 n=325569 | tras_1loss IC=+0.077 n=253694 | tras_2loss IC=+0.046 n=107272/40 | gap=+0.004 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.015 n=4120 | contrario_BTC IC=+0.022 n=3656/40 | gap=+0.006 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=34365 IC=+0.029 PNL=+1973.37€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=34365 IC=+0.029 PNL=+1973.37€

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
  - _Estado_: n=1543 IC=+0.015 PNL=+12.26€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1543 IC=+0.015 PNL=+12.26€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=629 IC=-0.013 PNL=+7.13€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=629 IC=-0.013 PNL=+7.13€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.185 > 0.1 con n=2053 PNL=+1275.17€
  - _Datos_: n=2053 IC=+0.185 PNL=+1275.17€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=975 IC=+0.045 PNL=+72.09€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=975 IC=+0.045 PNL=+72.09€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1224 IC=+0.082 PNL=+267.10€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1224 IC=+0.082 PNL=+267.10€

**⏳ H-CUSTOM-DRIFT15-ZONA-MUERTA** — GBM#15min drift_15min ∈ [-0.3,+0.3] — zona muerta de señal
  - _Hipótesis_: Análisis n=127 GBM#15min: cuando drift_15min está entre -0.3 y +0.3 (mercado sin dirección clara) el IC es negativo (-0.043). Cuando drift>0.3 IC=+0.100 (n=28). Cuando drift<-1 IC=+0.048 (reversión). La señal requiere mercado con dirección clara.
  - _Umbral_: 50
  - _Acción_: Filtrar señales GBM#15min cuando drift_15min ∈ [-0.3, +0.3] — validar con n≥50 antes de implementar
  - _Estado_: 0/50 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: confirmada 2026-07-01 (IC=-0.037 n=52) e implementada en shadow_predict.py (skip si drift_15min∈[-0.3,0.3)) -- verificado 26-Ago con 2177 filas post-TWAP reales, 0 caen en la zona filtrada. Frozen by design, no falta n

**〰️ H-CUSTOM-DRIFT15-MOMENTUM** — GBM#15min drift_15min > 0.3 — zona de momentum (señal fuerte)
  - _Hipótesis_: Cuando drift_15min > 0.3%/h el GBM captura bien la dirección: IC=+0.100 n=28 en todos GBM#15min; IC=+0.152 n=13 solo BTC. El mercado tiene dirección clara y el GBM la sigue. Hipótesis: este rango es donde la señal es real.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma IC>0.10 con n≥40 → boost ×1.2 en GBM#15min cuando drift_15min>0.3
  - _Estado_: n=5526 IC=+0.076 PNL=+1235.05€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=5526 IC=+0.076 PNL=+1235.05€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=143 IC=-0.259 PNL=-10.91€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=143 IC=-0.259 PNL=-10.91€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=249 IC=-0.022 PNL=+8.26€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=249 IC=-0.022 PNL=+8.26€

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

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=5643 IC=-0.004 PNL=-16.91€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=5643 IC=-0.004 PNL=-16.91€

**🟡 H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.176 > 0.08 con n=66 PNL=+18.24€
  - _Datos_: n=66 IC=+0.176 PNL=+18.24€

**🔶 H-LATE-WINDOW-5MIN** — Late-window BTC 5min — arbitraje timing vs Polymarket
  - _Hipótesis_: Inspirado en VyvanseWithMarijuana (36.5% ROI, $42k vol). A T+160-270s dentro de una ventana BTC 5min, si BTC ya se movió >0.3%, Polymarket no ha actualizado precio → edge estructural. Estrategia LATE_WINDOW_5MIN en shadow hasta n≥30. FIX 2026-07-02: la estrategia llevaba 0 predicciones desde su creacion porque HORIZONTE_MIN_HORAS=0.05 (3min) descartaba todo mercado a <3min de expirar — y su zona de entrada (160-270s de una ventana de 5min) deja 30-140s restantes, siempre bajo el suelo. Corregido en shadow_predict (zona late-window marcada _solo_late, 30s-3min, solo evaluada por esta estrategia). El reloj de acumulacion empieza de verdad hoy. Contexto extra: el estudio de ballenas de hoy confirma que comprar el lado ganador a mitad/final de ventana es el playbook comun de los 3 mayores ganadores verificados de estos mercados (Bonereaper +$19.9k/mes, wowitsamazing +$10k/mes, zhangfan151 +$8.7k/mes).
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si IC≥0.08 con n≥30 → proponer pasar a live con stake mínimo (0.50€). Si IC<0 con n≥30 → el lag de Polymarket en BTC es insuficiente.
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.253 n=95) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=95 IC=+0.253 PNL=+75.39€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=6908 IC=+0.033 PNL=+386.14€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=6908 IC=+0.033 PNL=+386.14€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=2149 IC=+0.053 PNL=+252.55€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2149 IC=+0.053 PNL=+252.55€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.105 > 0.08 con n=340 PNL=+97.29€
  - _Datos_: n=340 IC=+0.105 PNL=+97.29€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.135 > 0.08 con n=576 PNL=+130.43€
  - _Datos_: n=576 IC=+0.135 PNL=+130.43€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.122 > 0.08 con n=440 PNL=+209.86€
  - _Datos_: n=440 IC=+0.122 PNL=+209.86€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=28591 IC=+0.102 PNL=+8994.95€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=28591 IC=+0.102 PNL=+8994.95€

**〰️ H-CUSTOM-MERCURY-RETROGRADO** — Mercurio retrógrado: ¿rendimiento peor durante la ventana?
  - _Hipótesis_: Mismo origen que H-CUSTOM-MOON-LLENA (paper de Fornero, 43 Jornadas SADAF 2023). Qi, Wang & Zhang (2022, 48 mercados, 1973-2019): rendimientos 3.33%/año más bajos durante Mercurio retrógrado. Kou & Ma (2022) en China (99.8% cuentas retail): hasta -31% anualizado. Ambos estudios confirman que el mecanismo es la creencia/superstición de inversores retail (mayor efecto cuanto más retail y más supersticioso el mercado), no un efecto astral literal — Polymarket encaja en ese perfil. Ventanas 2026 (fuente pública, actualizar cada año): 26-feb a 20-mar, 29-jun a 23-jul, 24-oct a 13-nov.
  - _Umbral_: n≥100 PERO ADEMÁS necesita cubrir al menos 2-3 ventanas de retrogradación distintas (no solo la de jun-jul 2026) — esperar mínimo hasta después de la ventana de oct-nov 2026
  - _Acción_: Si IC en mercury_retrogrado=1 < IC en mercury_retrogrado=0 con margen ≥0.05 y ≥2 ventanas distintas cubiertas → considerar boost/filtro. No implementar tras una sola ventana (jun-jul 2026) por more que n sea alto — sería solo un evento, no un patrón.
  - _Estado_: n=1792 IC=+0.109 PNL=+195.82€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=1792 IC=+0.109 PNL=+195.82€

**〰️ H-CUSTOM-SMART-MONEY-CONSENSUS** — Consenso de wallets 'smart money' — ¿confirma nuestra dirección?
  - _Hipótesis_: Javi propuso estudiar bots/wallets que operan bien en nuestros mismos mercados. En vez de creer artículos (ya verificamos 2 veces esta semana que las narrativas no aguantan el cruce con datos reales), smart_money_tracker.py mide el track record REAL de wallets activas en BTC/ETH/SOL/XRP Up-or-Down 5/15/60min vía data-api.polymarket.com/positions, filtrado a posiciones 'Up or Down'. Clasifica como 'smart' las wallets con n>=10 posiciones, win_rate>=0.55 y pnl_total>0. smart_money_consensus es el sesgo direccional reciente (Up-Down)/(Up+Down) de esas wallets 'smart' por activo. Hipótesis: si nuestra decisión (BUY_YES/BUY_NO) coincide con el consenso smart money, mejor IC que cuando diverge. RESET METODOLOGICO 2026-07-02: la clasificacion 'smart' original via /positions estaba INVERTIDA para wallets de alta frecuencia (el endpoint solo retiene el residuo perdedor sin redimir; verificado: 'wowitsamazing' figuraba como -$478k y es +$10k/mes en el leaderboard oficial). Desde 2026-07-02T06:12Z el consenso se construye solo con wallets verificadas en el leaderboard oficial (pnl_mes>=$1000, 24 wallets). Los valores de smart_money_consensus capturados en features ANTES de esa fecha provienen de la clasificacion rota — descontar ese tramo al evaluar.
  - _Umbral_: n≥40 y IC>+0.08 — además necesita que existan wallets 'smart' acumuladas (0 al empezar, se van descubriendo cada ciclo)
  - _Acción_: Si IC en confluencia (decisión coincide con signo de smart_money_consensus) supera en >=0.05 al IC en divergencia, con n≥40 en cada lado → boost ×1.1-1.2 cuando coincide, considerar reducir stake cuando diverge fuerte.
  - _Estado_: n=5343 IC=+0.036 PNL=+371.85€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=5343 IC=+0.036 PNL=+371.85€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.447 > 0.1 con n=1115 PNL=+1112.78€
  - _Datos_: n=1115 IC=+0.447 PNL=+1112.78€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=12365 IC=+0.054 PNL=+1505.38€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=12365 IC=+0.054 PNL=+1505.38€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.200 > 0.1 con n=3308 PNL=+1784.00€
  - _Datos_: n=3308 IC=+0.200 PNL=+1784.00€

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
  - _Estado_: n=1832 IC=+0.045 PNL=+184.51€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1832 IC=+0.045 PNL=+184.51€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.127 > 0.1 con n=395 PNL=+111.14€
  - _Datos_: n=395 IC=+0.127 PNL=+111.14€

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
  - _Estado_: n=17353 IC=-0.137 PNL=+1187.43€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=17353 IC=-0.137 PNL=+1187.43€

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
  - _Estado_: n=1873 IC=+0.138 PNL=+1003.19€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=1873 IC=+0.138 PNL=+1003.19€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.187 > 0.08 con n=2014 PNL=+1262.54€
  - _Datos_: n=2014 IC=+0.187 PNL=+1262.54€

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

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.200 > 0.08 con n=472 PNL=+229.40€
  - _Datos_: n=472 IC=+0.200 PNL=+229.40€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.239 < -0.1 con n=1699 PNL=-188.12€
  - _Datos_: n=1699 IC=-0.239 PNL=-188.12€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=5144 IC=+0.162 PNL=+3334.08€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=5144 IC=+0.162 PNL=+3334.08€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.097 > 0.08 con n=75 PNL=+25.00€
  - _Datos_: n=75 IC=+0.097 PNL=+25.00€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=1935 IC=+0.059 PNL=+517.02€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1935 IC=+0.059 PNL=+517.02€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.180 > 0.08 con n=1751 PNL=+1211.11€
  - _Datos_: n=1751 IC=+0.180 PNL=+1211.11€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=2864 IC=-0.031 PNL=+745.31€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2864 IC=-0.031 PNL=+745.31€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.087 > 0.08 con n=543 PNL=-50.58€
  - _Datos_: n=543 IC=+0.087 PNL=-50.58€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.234 > 0.08 con n=3224 PNL=-301.66€
  - _Datos_: n=3224 IC=+0.234 PNL=-301.66€

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
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.088 n=956) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=956 IC=+0.088 PNL=+213.13€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.340 > 0.08 con n=248 PNL=+93.20€
  - _Datos_: n=248 IC=+0.340 PNL=+93.20€

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
  - _Estado_: n=8580 IC=+0.175 PNL=-1012.03€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=8580 IC=+0.175 PNL=-1012.03€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.194 > 0.1 con n=132 PNL=+75.67€
  - _Datos_: n=132 IC=+0.194 PNL=+75.67€
