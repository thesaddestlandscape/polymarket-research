# Hipótesis automáticas — 2026-10-12 18:21 UTC
_Generado por shadow_postmortem.py sobre 868972 resoluciones (PNL=+109782.26€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **PATRÓN** `py_entrada` > `0.505` → IC=+0.213 (n=737)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.126)

- **PATRÓN** `n_total_lado` > `68.0` → IC=+0.195 (n=247)

  - _Acción_: Kelly boost +0.97€ cuando `n_total_lado` > 68.0 (IC base=+0.126)

- **PATRÓN** `banda_hit_calibrado` > `0.6199` → IC=+0.255 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6199 (IC base=+0.126)

- **PATRÓN** `banda_z` > `9.381` → IC=+0.189 (n=242)

  - _Acción_: Kelly boost +0.94€ cuando `banda_z` > 9.381 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=247)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=777)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.126)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.505` → IC=+0.215 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.132)

- **PATRÓN** `n_total_lado` > `73.0` → IC=+0.214 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 73.0 (IC base=+0.132)

- **PATRÓN** `banda_hit_calibrado` > `0.6159` → IC=+0.245 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6159 (IC base=+0.132)

- **PATRÓN** `banda_z` > `9.789` → IC=+0.221 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.789 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=625)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=679)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.132)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.184 (n=115)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.353 (n=32)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.126 (n=97)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=113)

- **PATRÓN** `py_entrada` > `0.705` → IC=+0.255 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.705 (IC base=+0.125)

- **PATRÓN** `banda_hit_calibrado` > `0.8019` → IC=+0.255 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8019 (IC base=+0.125)

- **PATRÓN** `banda_z` > `7.17` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `banda_z` > 7.17 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.136 (n=97)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 14.0 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.184 (n=115)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.02 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.126 (n=97)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.495 (IC base=+0.004)

- **PATRÓN** `ballena_activa_n` < `77.0` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 77.0 (IC base=+0.004)

### BALLENAS_CONFIRMADAS_15M#XRP#15min
- **PATRÓN** `n_ballena_banda` > `26.0` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `n_ballena_banda` > 26.0 (IC base=+0.154)

- **PATRÓN** `n_total_lado` > `38.0` → IC=+0.224 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 38.0 (IC base=+0.154)

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
- **FILTRO** `restante_s_al_confirmar` < `144.05` → IC=-0.205 (n=9210)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 144.05
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=27631)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `130.91` → IC=-0.265 (n=1106)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.91
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3319)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `122.47` → IC=-0.300 (n=1030)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 122.47
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=3091)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `166.66` → IC=-0.220 (n=2395)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 166.66
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=7187)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `131.73` → IC=-0.294 (n=1786)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 131.73
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=5360)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.208 (n=19422)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=4090)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `9425.3283` → IC=+0.180 (n=1830)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 9425.3283 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.132 (n=16251)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.134 (n=19738)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.227 (n=15112)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.157 (n=6766)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7374.4882` → IC=+0.162 (n=2604)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 7374.4882 (IC base=+0.126)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=1959)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.197 (n=1917)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 17.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.775` → IC=+0.364 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.775 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.197 (n=2405)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `16167.0481` → IC=+0.210 (n=623)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16167.0481 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.195 (n=1730)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 7.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.194 (n=1931)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 17.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.191 (n=2472)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.01 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `16068.6951` → IC=+0.201 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16068.6951 (IC base=+0.189)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.168 (n=432)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` > 0.61 (IC base=+0.087)

- **PATRÓN** `libro_liquidez` > `6900.0098` → IC=+0.169 (n=119)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 6900.0098 (IC base=+0.087)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.137 (n=1024)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.44 (IC base=+0.086)

- **PATRÓN** `libro_liquidez` > `5830.4537` → IC=+0.128 (n=240)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 5830.4537 (IC base=+0.086)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=3795)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.364 (n=1238)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.226 (n=1681)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.361 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.223 (n=1956)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.218)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.147 (n=943)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.146 (n=808)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 15.0 (IC base=+0.141)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.260 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=734)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `1510.6056` → IC=+0.148 (n=805)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 1510.6056 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `4420.281` → IC=+0.165 (n=150)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 4420.281 (IC base=+0.072)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.241 (n=893)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.408 (n=1079)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.148 (n=1259)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 7.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.157 (n=665)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.147)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.289 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=833)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.147)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.177 (n=335)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 7.0 (IC base=+0.164)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.362 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.153 (n=194)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.02 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `3371.7925` → IC=+0.146 (n=80)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 3371.7925 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.155 (n=401)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.230 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.125)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.795` → IC=-0.329 (n=68)

  - _Acción_: SKIP cuando `py_entrada` > 0.795
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=137)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=16274)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.200 (n=13806)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.230 (n=6808)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.198)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.179 (n=3583)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 6.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.177 (n=3586)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 17.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.179 (n=3653)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.73 (IC base=+0.175)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.224 (n=1761)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.227 (n=1756)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.310 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.223)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=3727)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.183 (n=3564)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.186 (n=2039)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.72 (IC base=+0.180)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.254 (n=3250)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.244)

- **PATRÓN** `py_entrada` > `0.78` → IC=+0.349 (n=1057)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.78 (IC base=+0.244)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.244)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=3651)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.192 (n=2332)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.187)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.199 (n=1275)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.73 (IC base=+0.187)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.430 (n=642)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.427)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.427 (n=630)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.427)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=738)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.427)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.429 (n=746)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.427)

- **PATRÓN** `libro_liquidez` > `4010.7815` → IC=+0.438 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4010.7815 (IC base=+0.427)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.433 (n=283)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.447 (n=186)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.448 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.435)

- **PATRÓN** `libro_liquidez` > `18155.0675` → IC=+0.438 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 18155.0675 (IC base=+0.435)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.443 (n=191)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.431)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.431)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.431)

- **PATRÓN** `libro_liquidez` > `3430.6036` → IC=+0.440 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3430.6036 (IC base=+0.431)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.403 (n=132)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.402)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.402 (n=131)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.402)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.412 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.402)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=24)

- **FILTRO** `libro_liquidez` < `7880.4556` → IC=-0.344 (n=30)

  - _Acción_: SKIP cuando `libro_liquidez` < 7880.4556
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=20841)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.245 (n=21306)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.201)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.187 (n=8355)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 8.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.187 (n=6684)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 12.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.200 (n=9317)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.185)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.226 (n=4362)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.227 (n=4260)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.284 (n=3074)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.186 (n=3570)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.193 (n=8898)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.178)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.233 (n=4396)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.222 (n=3329)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.278 (n=3029)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.205 (n=8059)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.202 (n=7986)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.260 (n=3168)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.202)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.205 (n=3464)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.196 (n=3504)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 6.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.246 (n=3662)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.195)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=7553)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` < `4.2` → IC=+0.124 (n=6909)

  - _Acción_: Kelly boost +0.62€ cuando `restante_min` < 4.2 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.140 (n=7378)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.127 (n=9167)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.43` → IC=+0.139 (n=6925)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 2.43 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=3738)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.121)

- **PATRÓN** `restante_min` < `4.18` → IC=+0.126 (n=3449)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.18 (IC base=+0.121)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.143 (n=3714)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.95 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.135 (n=4543)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.121)

- **PATRÓN** `lag_apertura_s` < `2.88` → IC=+0.146 (n=3434)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 2.88 (IC base=+0.121)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.190 (n=3815)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.135 (n=4041)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.138 (n=3494)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.25 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.303 (n=1504)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.293)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.295 (n=1485)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.293)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.380 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `4271.1421` → IC=+0.300 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4271.1421 (IC base=+0.293)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.293 (n=676)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.284)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.286 (n=581)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.284)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.352 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `5371.2351` → IC=+0.306 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5371.2351 (IC base=+0.284)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.325 (n=483)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.293)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.297 (n=714)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.293)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.389 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `1707.6334` → IC=+0.306 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1707.6334 (IC base=+0.293)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.357 (n=82)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.351)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.377 (n=79)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.351)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.391 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.351)

- **PATRÓN** `libro_spread` < `0.07` → IC=+0.356 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.07 (IC base=+0.351)

- **PATRÓN** `libro_liquidez` > `761.0655` → IC=+0.378 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 761.0655 (IC base=+0.351)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.446 (n=697)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.441)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.441 (n=576)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.442 (n=685)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.445 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.441)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.443 (n=780)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.441)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.443 (n=330)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.438)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.441 (n=287)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.438 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.447 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.438)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.464 (n=109)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.446)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.453 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.446)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.447 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.446)

- **PATRÓN** `libro_liquidez` > `2089.6231` → IC=+0.461 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2089.6231 (IC base=+0.446)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` > `13.0` → IC=+0.385 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.396)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.409 (n=31)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.396)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.431 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.396)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.296 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=55)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.241 (n=56)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.229 (n=46)

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
- **FILTRO** `hora_utc` > `10.0` → IC=-0.296 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=55)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.241 (n=56)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.229 (n=46)

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
- **PATRÓN** `drift_60min` |x|≤ `0.364` → IC=+0.137 (n=10248)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.364 (IC base=+0.115)

- **PATRÓN** `ibs_20min` > `0.9841` → IC=+0.243 (n=3881)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9841 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` < `0.212` → IC=+0.254 (n=2709)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.212 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.977` → IC=+0.185 (n=4396)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 5.977 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `1.2084` → IC=+0.251 (n=3289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2084 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` > `0.6904` → IC=+0.258 (n=2938)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6904 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` > `0.3025` → IC=+0.232 (n=1172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3025 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` > `2.3431` → IC=+0.222 (n=3722)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3431 (IC base=+0.115)

- **PATRÓN** `ibs_20min` < `0.5683` → IC=+0.143 (n=14280)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.5683 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.566` → IC=+0.198 (n=956)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.566 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `1.1961` → IC=+0.183 (n=5382)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 1.1961 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.0551` → IC=+0.182 (n=2440)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.0551 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2954` → IC=+0.228 (n=1358)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2954 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` > `1.5692` → IC=+0.205 (n=8221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5692 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `111.0` → IC=+0.220 (n=9035)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 111.0 (IC base=+0.074)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.215 (n=857)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.187)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.211 (n=857)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.2773` → IC=+0.190 (n=2261)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.2773 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.201 (n=1244)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.190 (n=1719)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 11.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.274 (n=1061)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.154` → IC=+0.289 (n=779)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.154 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.238 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `2.2721` → IC=+0.202 (n=1107)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2721 (IC base=+0.187)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.200 (n=2681)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.187)

- **PATRÓN** `libro_liquidez` > `2101.62` → IC=+0.211 (n=857)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2101.62 (IC base=+0.187)

- **PATRÓN** `sigma_h` < `0.0079` → IC=+0.236 (n=2112)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0079 (IC base=+0.233)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.243 (n=1887)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.0875` → IC=+0.263 (n=707)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0875 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.253 (n=763)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.5067` → IC=+0.255 (n=2110)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5067 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.921` → IC=+0.234 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.921 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` < `0.0941` → IC=+0.237 (n=1867)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0941 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.287` → IC=+0.246 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.287 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.6474` → IC=+0.251 (n=660)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6474 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=2322)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.233)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.230 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.233)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.236 (n=912)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.1751` → IC=+0.248 (n=1380)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1751 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.234 (n=2070)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.222 (n=2117)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` > `0.9696` → IC=+0.266 (n=689)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9696 (IC base=+0.221)

- **PATRÓN** `dist_vwap_pct` > `0.1294` → IC=+0.225 (n=1155)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1294 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.483` → IC=+0.259 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.483 (IC base=+0.221)

- **PATRÓN** `volumen_regimen` < `1.2483` → IC=+0.223 (n=2068)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2483 (IC base=+0.221)

- **PATRÓN** `volumen_regimen` > `0.6213` → IC=+0.226 (n=2067)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6213 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.2786` → IC=+0.247 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2786 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` < `1.5145` → IC=+0.222 (n=896)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5145 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.4399` → IC=+0.246 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4399 (IC base=+0.221)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.187 (n=700)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0026 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.074` → IC=+0.173 (n=692)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.074 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.164 (n=786)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.5867` → IC=+0.187 (n=1826)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.5867 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.222` → IC=+0.153 (n=335)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 11.222 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.28` → IC=+0.146 (n=1900)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 4.28 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `1.1967` → IC=+0.149 (n=2075)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.1967 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.0967` → IC=+0.164 (n=765)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.0967 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.4589` → IC=+0.149 (n=1959)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4589 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.4221` → IC=+0.145 (n=1959)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4221 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `225.0` → IC=+0.182 (n=832)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 225.0 (IC base=+0.139)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.209 (n=1199)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.195 (n=2782)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.194 (n=2363)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.268 (n=1016)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.333` → IC=+0.261 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.333 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` < `0.0977` → IC=+0.193 (n=2323)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0977 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.3484` → IC=+0.205 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3484 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `2.1566` → IC=+0.202 (n=1700)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1566 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.197 (n=3116)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `2009.4584` → IC=+0.201 (n=1197)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2009.4584 (IC base=+0.190)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.226 (n=2052)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.1757` → IC=+0.230 (n=1026)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1757 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.247 (n=868)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.218 (n=1084)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.0704` → IC=+0.236 (n=1026)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0704 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.541` → IC=+0.257 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.541 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.3459` → IC=+0.256 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3459 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` < `1.7259` → IC=+0.216 (n=968)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7259 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.726` → IC=+0.233 (n=997)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.726 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `2081.1184` → IC=+0.228 (n=778)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2081.1184 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.222 (n=2143)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.217)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.140 (n=137)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=3149)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.146 (n=637)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.004 (IC base=+0.050)

- **PATRÓN** `ibs_20min` > `0.9581` → IC=+0.222 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9581 (IC base=+0.050)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.068` → IC=+0.182 (n=1024)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 5.068 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` < `0.8538` → IC=+0.330 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8538 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` > `1.2292` → IC=+0.351 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2292 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` < `0.1787` → IC=+0.324 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1787 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` > `0.2965` → IC=+0.342 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2965 (IC base=+0.050)

- **PATRÓN** `volumen_spike_ratio` < `1.4165` → IC=+0.359 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4165 (IC base=+0.050)

- **PATRÓN** `volumen_spike_ratio` > `2.2083` → IC=+0.326 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2083 (IC base=+0.050)

- **PATRÓN** `ballena_activa_n` < `149.0` → IC=+0.332 (n=505)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 149.0 (IC base=+0.050)

- **PATRÓN** `ibs_20min` < `0.0986` → IC=+0.172 (n=822)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.0986 (IC base=+0.033)

- **PATRÓN** `dist_vwap_pct` > `0.4581` → IC=+0.183 (n=266)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.4581 (IC base=+0.033)

- **PATRÓN** `volumen_regimen` < `0.8504` → IC=+0.149 (n=920)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8504 (IC base=+0.033)

- **PATRÓN** `volumen_pendiente_norm` > `0.2873` → IC=+0.206 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2873 (IC base=+0.033)

- **PATRÓN** `volumen_spike_ratio` > `1.5144` → IC=+0.159 (n=1179)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.5144 (IC base=+0.033)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.178 (n=88)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=488)

- **FILTRO** `ibs_20min` < `0.3103` → IC=-0.185 (n=144)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3103
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=432)

- **FILTRO** `ibs_20min` > `0.2222` → IC=-0.129 (n=3163)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2222
  - _Potencial_: sin este filtro IC_bueno=+0.148 (n=1567)

- **FILTRO** `sigma_ewma_delta_pct` > `8.665` → IC=-0.227 (n=488)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.665
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=4242)

- **PATRÓN** `ibs_20min` > `0.8` → IC=+0.183 (n=197)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.8 (IC base=+0.035)

- **PATRÓN** `dist_vwap_pct` > `0.9817` → IC=+0.283 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9817 (IC base=+0.035)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.412` → IC=+0.162 (n=66)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 9.412 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` > `1.0006` → IC=+0.297 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0006 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` < `0.1539` → IC=+0.266 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1539 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` < `2.1915` → IC=+0.281 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1915 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` > `1.5489` → IC=+0.261 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5489 (IC base=+0.035)

- **PATRÓN** `ibs_20min` < `0.2222` → IC=+0.148 (n=1567)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.2222 (IC base=-0.037)

- **PATRÓN** `dist_vwap_pct` > `0.2587` → IC=+0.279 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2587 (IC base=-0.037)

- **PATRÓN** `volumen_regimen` < `0.7071` → IC=+0.283 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7071 (IC base=-0.037)

- **PATRÓN** `volumen_pendiente_norm` > `0.0797` → IC=+0.303 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0797 (IC base=-0.037)

- **PATRÓN** `volumen_spike_ratio` < `2.4034` → IC=+0.301 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4034 (IC base=-0.037)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6329` → IC=-0.179 (n=828)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6329
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=2490)

- **FILTRO** `ibs_20min` < `0.7174` → IC=-0.154 (n=2189)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7174
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=1129)

- **FILTRO** `ibs_20min` > `0.76` → IC=-0.203 (n=1232)

  - _Acción_: SKIP cuando `ibs_20min` > 0.76
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=3699)

- **PATRÓN** `dist_vwap_pct` > `0.708` → IC=+0.320 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.708 (IC base=-0.074)

- **PATRÓN** `volumen_regimen` < `1.0034` → IC=+0.298 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0034 (IC base=-0.074)

- **PATRÓN** `volumen_regimen` > `0.6377` → IC=+0.307 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6377 (IC base=-0.074)

- **PATRÓN** `volumen_pendiente_norm` < `0.1062` → IC=+0.302 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1062 (IC base=-0.074)

- **PATRÓN** `volumen_spike_ratio` < `1.5988` → IC=+0.303 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5988 (IC base=-0.074)

- **PATRÓN** `volumen_spike_ratio` > `1.8742` → IC=+0.304 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8742 (IC base=-0.074)

- **PATRÓN** `dist_vwap_pct` > `0.7982` → IC=+0.277 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7982 (IC base=-0.009)

- **PATRÓN** `volumen_regimen` > `1.0826` → IC=+0.279 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0826 (IC base=-0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.1044` → IC=+0.285 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1044 (IC base=-0.009)

- **PATRÓN** `volumen_spike_ratio` < `2.1859` → IC=+0.258 (n=1037)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1859 (IC base=-0.009)

- **PATRÓN** `volumen_spike_ratio` > `1.4315` → IC=+0.262 (n=1179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4315 (IC base=-0.009)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.203 (n=5121)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.459` → IC=+0.185 (n=13724)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.459 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.9203` → IC=+0.283 (n=1152)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9203 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.657` → IC=+0.155 (n=6890)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 3.657 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` < `1.1748` → IC=+0.251 (n=5635)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1748 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` > `0.6887` → IC=+0.259 (n=5034)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6887 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.2402` → IC=+0.267 (n=1685)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2402 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` > `2.6441` → IC=+0.264 (n=3016)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6441 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.283 (n=8617)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 93.0 (IC base=+0.096)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.160 (n=4930)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0089 (IC base=+0.075)

- **PATRÓN** `ibs_20min` < `0.5391` → IC=+0.159 (n=13011)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.5391 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` < `0.8766` → IC=+0.255 (n=3049)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8766 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.1975` → IC=+0.261 (n=1525)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1975 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2945` → IC=+0.308 (n=947)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2945 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` < `1.5874` → IC=+0.283 (n=2833)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5874 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` > `2.2859` → IC=+0.276 (n=2918)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2859 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `79.0` → IC=+0.288 (n=6359)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 79.0 (IC base=+0.075)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.3718` → IC=-0.159 (n=1402)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3718
  - _Potencial_: sin este filtro IC_bueno=+0.131 (n=2849)

- **FILTRO** `ibs_20min` > `0.7548` → IC=-0.192 (n=875)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7548
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=2626)

- **FILTRO** `sigma_ewma_delta_pct` > `4.574` → IC=-0.190 (n=769)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.574
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=2732)

- **PATRÓN** `ibs_20min` > `0.9122` → IC=+0.287 (n=1063)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9122 (IC base=+0.035)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.2` → IC=+0.206 (n=750)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.2 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` > `0.2297` → IC=+0.290 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2297 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` < `1.4484` → IC=+0.219 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4484 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` > `2.2395` → IC=+0.256 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2395 (IC base=+0.035)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.252 (n=955)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.035)

- **PATRÓN** `ibs_20min` < `0.1593` → IC=+0.151 (n=876)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.1593 (IC base=-0.028)

- **PATRÓN** `volumen_pendiente_norm` < `0.2295` → IC=+0.416 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2295 (IC base=-0.028)

- **PATRÓN** `volumen_spike_ratio` < `2.5496` → IC=+0.413 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5496 (IC base=-0.028)

- **PATRÓN** `volumen_spike_ratio` > `1.5399` → IC=+0.406 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5399 (IC base=-0.028)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.418 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=-0.028)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8555` → IC=+0.143 (n=1048)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.8555 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` > `0.1111` → IC=+0.195 (n=784)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1111 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` < `1.197` → IC=+0.174 (n=1485)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 1.197 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` > `0.6787` → IC=+0.184 (n=1326)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 0.6787 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.2745` → IC=+0.219 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2745 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` < `1.425` → IC=+0.198 (n=488)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.425 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` > `2.4806` → IC=+0.191 (n=487)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.4806 (IC base=+0.024)

- **PATRÓN** `ballena_activa_n` < `222.0` → IC=+0.226 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 222.0 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` < `0.1491` → IC=+0.231 (n=935)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1491 (IC base=+0.002)

- **PATRÓN** `volumen_regimen` > `0.6194` → IC=+0.236 (n=915)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6194 (IC base=+0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.2721` → IC=+0.298 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2721 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` < `1.5571` → IC=+0.229 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5571 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` > `2.1933` → IC=+0.251 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1933 (IC base=+0.002)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.281 (n=2049)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.257)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.262 (n=2295)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.257)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.258 (n=2047)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.257)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=1188)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.257)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.27` → IC=+0.289 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.27 (IC base=+0.257)

- **PATRÓN** `volumen_pendiente_norm` < `0.1318` → IC=+0.269 (n=2087)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1318 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` > `2.1656` → IC=+0.266 (n=1466)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1656 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.268 (n=2686)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.257)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.305 (n=1936)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.179` → IC=+0.307 (n=853)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.179 (IC base=+0.290)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.323 (n=738)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.290)

- **PATRÓN** `ibs_20min` < `0.3647` → IC=+0.293 (n=1935)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3647 (IC base=+0.290)

- **PATRÓN** `ibs_20min` > `0.1071` → IC=+0.293 (n=1290)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1071 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.697` → IC=+0.306 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.697 (IC base=+0.290)

- **PATRÓN** `volumen_pendiente_norm` < `0.1951` → IC=+0.288 (n=1878)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1951 (IC base=+0.290)

- **PATRÓN** `volumen_pendiente_norm` > `0.339` → IC=+0.305 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.339 (IC base=+0.290)

- **PATRÓN** `volumen_spike_ratio` < `1.5718` → IC=+0.305 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5718 (IC base=+0.290)

- **PATRÓN** `volumen_spike_ratio` > `2.638` → IC=+0.296 (n=833)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.638 (IC base=+0.290)

- **PATRÓN** `libro_liquidez` > `2075.815` → IC=+0.311 (n=645)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2075.815 (IC base=+0.290)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.292 (n=1606)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.290)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7539` → IC=-0.182 (n=908)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7539
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=2727)

- **PATRÓN** `ibs_20min` > `0.8924` → IC=+0.168 (n=848)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.8924 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` < `0.2037` → IC=+0.228 (n=974)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2037 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` < `1.0157` → IC=+0.236 (n=1013)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0157 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` > `0.6696` → IC=+0.220 (n=1028)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6696 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.103` → IC=+0.240 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.103 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` < `1.4` → IC=+0.256 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4 (IC base=+0.028)

- **PATRÓN** `ballena_activa_n` < `109.0` → IC=+0.256 (n=997)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 109.0 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` < `1.0404` → IC=+0.237 (n=682)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0404 (IC base=-0.000)

- **PATRÓN** `volumen_pendiente_norm` < `0.103` → IC=+0.240 (n=714)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.103 (IC base=-0.000)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.277 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=-0.000)

- **PATRÓN** `volumen_spike_ratio` < `1.8288` → IC=+0.268 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8288 (IC base=-0.000)

- **PATRÓN** `volumen_spike_ratio` > `2.478` → IC=+0.247 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.478 (IC base=-0.000)

- **PATRÓN** `ballena_activa_n` < `129.0` → IC=+0.257 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 129.0 (IC base=-0.000)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7636` → IC=-0.198 (n=1626)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7636
  - _Potencial_: sin este filtro IC_bueno=+0.292 (n=1627)

- **FILTRO** `ibs_20min` > `0.6596` → IC=-0.237 (n=808)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6596
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=2428)

- **FILTRO** `sigma_ewma_delta_pct` > `8.585` → IC=-0.230 (n=368)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.585
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=2868)

- **PATRÓN** `ibs_20min` > `0.7636` → IC=+0.292 (n=1627)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7636 (IC base=+0.047)

- **PATRÓN** `dist_vwap_pct` > `1.018` → IC=+0.340 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.018 (IC base=+0.047)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.636` → IC=+0.169 (n=505)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 9.636 (IC base=+0.047)

- **PATRÓN** `volumen_regimen` < `0.8519` → IC=+0.318 (n=823)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8519 (IC base=+0.047)

- **PATRÓN** `volumen_regimen` > `0.6337` → IC=+0.313 (n=1233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6337 (IC base=+0.047)

- **PATRÓN** `volumen_pendiente_norm` < `0.0986` → IC=+0.308 (n=1163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0986 (IC base=+0.047)

- **PATRÓN** `volumen_pendiente_norm` > `0.2757` → IC=+0.345 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2757 (IC base=+0.047)

- **PATRÓN** `volumen_spike_ratio` < `1.4433` → IC=+0.331 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4433 (IC base=+0.047)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.334 (n=806)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.047)

- **PATRÓN** `ibs_20min` < `0.5556` → IC=+0.137 (n=2139)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` < 0.5556 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` < `0.7052` → IC=+0.258 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7052 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` < `0.0981` → IC=+0.237 (n=956)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0981 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.0717` → IC=+0.246 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0717 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` < `2.4253` → IC=+0.251 (n=967)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4253 (IC base=+0.028)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.269 (n=983)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=+0.028)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.339 (n=1579)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0105 (IC base=+0.293)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.309 (n=836)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.293)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.325 (n=1768)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.293)

- **PATRÓN** `dist_vwap_pct` > `0.2128` → IC=+0.321 (n=1003)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2128 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.778` → IC=+0.316 (n=866)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.778 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.904` → IC=+0.293 (n=2003)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.904 (IC base=+0.293)

- **PATRÓN** `volumen_regimen` > `0.6244` → IC=+0.304 (n=1767)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6244 (IC base=+0.293)

- **PATRÓN** `volumen_pendiente_norm` > `0.2824` → IC=+0.342 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2824 (IC base=+0.293)

- **PATRÓN** `volumen_spike_ratio` > `1.4315` → IC=+0.306 (n=1692)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4315 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `2994.9154` → IC=+0.317 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2994.9154 (IC base=+0.293)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.328 (n=1496)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.293)

- **PATRÓN** `sigma_h` > `0.015` → IC=+0.327 (n=1251)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.015 (IC base=+0.294)

- **PATRÓN** `drift_60min` |x|≤ `0.1858` → IC=+0.296 (n=825)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1858 (IC base=+0.294)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.300 (n=1266)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.294)

- **PATRÓN** `ibs_20min` < `0.3676` → IC=+0.320 (n=1874)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3676 (IC base=+0.294)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.518` → IC=+0.305 (n=686)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.518 (IC base=+0.294)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.038` → IC=+0.295 (n=2236)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.038 (IC base=+0.294)

- **PATRÓN** `volumen_regimen` > `1.2314` → IC=+0.325 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2314 (IC base=+0.294)

- **PATRÓN** `volumen_pendiente_norm` > `0.2327` → IC=+0.343 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2327 (IC base=+0.294)

- **PATRÓN** `volumen_spike_ratio` < `1.4187` → IC=+0.302 (n=568)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4187 (IC base=+0.294)

- **PATRÓN** `volumen_spike_ratio` > `2.1432` → IC=+0.297 (n=772)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1432 (IC base=+0.294)

- **PATRÓN** `libro_liquidez` > `2664.0987` → IC=+0.303 (n=1249)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2664.0987 (IC base=+0.294)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.186 (n=3773)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0047 (IC base=+0.176)

- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.216 (n=3770)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.176)

- **PATRÓN** `drift_60min` |x|≤ `0.3436` → IC=+0.186 (n=9953)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.3436 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=11802)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` > `0.5625` → IC=+0.229 (n=11312)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5625 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.1641` → IC=+0.203 (n=4703)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1641 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.371` → IC=+0.254 (n=2254)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.371 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` < `1.1989` → IC=+0.167 (n=7506)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1989 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` > `0.6261` → IC=+0.162 (n=7504)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6261 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.2943` → IC=+0.198 (n=1664)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2943 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `2.6089` → IC=+0.186 (n=3647)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.6089 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `2023.856` → IC=+0.182 (n=10104)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2023.856 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.192 (n=10228)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 100.0 (IC base=+0.176)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.188 (n=7239)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0067 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.0794` → IC=+0.225 (n=3620)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0794 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=4044)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` < `0.4943` → IC=+0.235 (n=10854)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4943 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.177` → IC=+0.195 (n=1798)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 10.177 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `1.1821` → IC=+0.167 (n=7758)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1821 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.2918` → IC=+0.224 (n=1597)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2918 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `2.6249` → IC=+0.184 (n=3376)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.6249 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `1837.1` → IC=+0.179 (n=10854)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 1837.1 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `68.0` → IC=+0.194 (n=8668)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 68.0 (IC base=+0.179)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.236 (n=638)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.204)

- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.221 (n=637)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0085 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.3312` → IC=+0.224 (n=1900)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3312 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.210 (n=2007)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.208 (n=1277)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `0.92` → IC=+0.286 (n=1267)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.92 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.202` → IC=+0.334 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.202 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.261 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `1.5423` → IC=+0.206 (n=1598)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5423 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.215 (n=2000)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.245 (n=1291)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.242)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.253 (n=1311)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.0986` → IC=+0.293 (n=647)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0986 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.244 (n=1323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.250 (n=722)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.242)

- **PATRÓN** `ibs_20min` < `0.2672` → IC=+0.265 (n=1291)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2672 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.117` → IC=+0.245 (n=1478)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.117 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` < `0.0995` → IC=+0.242 (n=1264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0995 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` > `0.2955` → IC=+0.273 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2955 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` < `1.4266` → IC=+0.258 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4266 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` > `2.6552` → IC=+0.247 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6552 (IC base=+0.242)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.246 (n=1618)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.242)

- **PATRÓN** `libro_liquidez` > `1609.46` → IC=+0.258 (n=1467)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1609.46 (IC base=+0.242)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.243 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.242)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.220 (n=566)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.16` → IC=+0.185 (n=1132)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.16 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.176 (n=1792)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `0.3643` → IC=+0.222 (n=1697)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3643 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.1365` → IC=+0.209 (n=1059)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1365 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.501` → IC=+0.228 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.501 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `0.6891` → IC=+0.165 (n=747)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.6891 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` > `1.0702` → IC=+0.157 (n=770)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 1.0702 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.2827` → IC=+0.185 (n=271)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2827 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `1.4144` → IC=+0.177 (n=553)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.4144 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `2.4993` → IC=+0.158 (n=553)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.4993 (IC base=+0.155)

- **PATRÓN** `ballena_activa_n` < `425.0` → IC=+0.160 (n=1619)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 425.0 (IC base=+0.155)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.168 (n=1783)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0056 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.2299` → IC=+0.177 (n=1569)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2299 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.188 (n=678)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.6038` → IC=+0.206 (n=1783)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6038 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.719` → IC=+0.206 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.719 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `1.204` → IC=+0.167 (n=1783)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.204 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` < `0.0948` → IC=+0.148 (n=1494)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.0948 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.151 (n=548)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.4989` → IC=+0.154 (n=1665)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4989 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.781` → IC=+0.150 (n=1110)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.781 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `234.0` → IC=+0.173 (n=699)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 234.0 (IC base=+0.148)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.231 (n=865)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.3996` → IC=+0.220 (n=1679)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3996 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.213 (n=1991)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.297 (n=996)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.5` → IC=+0.285 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.5 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.3511` → IC=+0.221 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3511 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` < `1.7703` → IC=+0.213 (n=810)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7703 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `2.6928` → IC=+0.219 (n=835)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6928 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.215 (n=2247)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `1998.1898` → IC=+0.224 (n=865)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1998.1898 (IC base=+0.208)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.246 (n=1435)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.01 (IC base=+0.232)

- **PATRÓN** `drift_60min` |x|≤ `0.1419` → IC=+0.268 (n=717)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1419 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.280 (n=621)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` < `0.3548` → IC=+0.251 (n=1633)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3548 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.623` → IC=+0.268 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.623 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.3508` → IC=+0.272 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3508 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` < `1.7209` → IC=+0.245 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7209 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `2.7242` → IC=+0.239 (n=702)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7242 (IC base=+0.232)

- **PATRÓN** `libro_liquidez` > `2077.858` → IC=+0.249 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2077.858 (IC base=+0.232)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.230 (n=671)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.232)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.213 (n=802)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.0748` → IC=+0.200 (n=607)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0748 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=1898)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.3204` → IC=+0.208 (n=1819)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3204 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.1366` → IC=+0.190 (n=1140)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1366 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.979` → IC=+0.208 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.979 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.856` → IC=+0.161 (n=1215)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.856 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.1015` → IC=+0.177 (n=750)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1015 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `1.4265` → IC=+0.158 (n=595)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.4265 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `2.5051` → IC=+0.167 (n=595)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.5051 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `5016.7718` → IC=+0.200 (n=1213)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5016.7718 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `146.0` → IC=+0.158 (n=1766)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 146.0 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.157 (n=1915)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.007 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.3824` → IC=+0.147 (n=1915)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3824 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=715)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.6818` → IC=+0.189 (n=1915)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.6818 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.879` → IC=+0.153 (n=673)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 6.879 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.8568` → IC=+0.165 (n=1277)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8568 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2966` → IC=+0.193 (n=291)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2966 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `1.808` → IC=+0.134 (n=1189)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.808 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `1.4146` → IC=+0.132 (n=1782)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 1.4146 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `4520.6002` → IC=+0.172 (n=1276)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 4520.6002 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `122.0` → IC=+0.131 (n=1526)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 122.0 (IC base=+0.129)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.128 (n=691)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0058 (IC base=+0.126)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.167 (n=939)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0099 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.5595` → IC=+0.126 (n=2070)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.63€ cuando `drift_60min` |x|≤ 0.5595 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.142 (n=2119)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.213 (n=2070)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.1935` → IC=+0.187 (n=1227)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1935 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.71` → IC=+0.266 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.71 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `1.1924` → IC=+0.138 (n=2070)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.1924 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` > `0.7153` → IC=+0.126 (n=1849)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.7153 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` < `0.1624` → IC=+0.134 (n=2093)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` < 0.1624 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.4402` → IC=+0.138 (n=669)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.4402 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.126 (n=2148)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `2888.477` → IC=+0.211 (n=939)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2888.477 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.154 (n=654)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 21.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.138 (n=2102)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0103 (IC base=+0.121)

- **PATRÓN** `drift_60min` |x|≤ `0.1048` → IC=+0.172 (n=703)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1048 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=2129)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` < `0.5893` → IC=+0.219 (n=2101)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5893 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `0.7428` → IC=+0.125 (n=350)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` > 0.7428 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.211` → IC=+0.125 (n=632)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 5.211 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.533` → IC=+0.123 (n=1852)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` < 2.533 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `1.1789` → IC=+0.133 (n=2101)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.1789 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` < `0.1652` → IC=+0.123 (n=2013)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1652 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.2744` → IC=+0.148 (n=271)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2744 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `1.4537` → IC=+0.139 (n=648)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.4537 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` > `2.4294` → IC=+0.126 (n=647)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 2.4294 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2747.7553` → IC=+0.191 (n=952)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2747.7553 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.130 (n=1914)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 51.0 (IC base=+0.121)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.237 (n=1716)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.1751` → IC=+0.226 (n=845)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1751 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.219 (n=1995)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.218 (n=1731)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.253 (n=1928)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` > `0.1888` → IC=+0.218 (n=1267)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1888 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` < `0.2685` → IC=+0.216 (n=1416)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2685 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.588` → IC=+0.247 (n=878)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.588 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` < `1.0264` → IC=+0.216 (n=1689)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0264 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` > `0.6188` → IC=+0.222 (n=1919)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6188 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.2335` → IC=+0.265 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2335 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` < `2.4913` → IC=+0.219 (n=1867)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4913 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `1.8145` → IC=+0.229 (n=1244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8145 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `2478.3046` → IC=+0.223 (n=1714)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2478.3046 (IC base=+0.214)

- **PATRÓN** `sigma_h` < `0.0121` → IC=+0.233 (n=863)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0121 (IC base=+0.225)

- **PATRÓN** `sigma_h` > `0.0224` → IC=+0.229 (n=890)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0224 (IC base=+0.225)

- **PATRÓN** `drift_60min` |x|≤ `0.0896` → IC=+0.256 (n=654)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0896 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.244 (n=951)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` < `0.4231` → IC=+0.256 (n=1962)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4231 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` > `1.1476` → IC=+0.233 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1476 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.374` → IC=+0.252 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.374 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` > `0.6397` → IC=+0.234 (n=1962)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6397 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.285 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `1.4377` → IC=+0.227 (n=1814)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4377 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `2428.9954` → IC=+0.233 (n=1753)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2428.9954 (IC base=+0.225)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.208 (n=979)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.3303` → IC=+0.182 (n=2584)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.3303 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.203 (n=1459)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` > `0.4878` → IC=+0.205 (n=2623)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4878 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` > `0.5777` → IC=+0.181 (n=574)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.5777 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.691` → IC=+0.198 (n=1257)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 3.691 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` < `1.0582` → IC=+0.183 (n=2317)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 1.0582 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` > `0.6953` → IC=+0.175 (n=2352)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 0.6953 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.1018` → IC=+0.183 (n=1058)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1018 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` < `1.4364` → IC=+0.189 (n=952)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.4364 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` > `2.522` → IC=+0.173 (n=951)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.522 (IC base=+0.170)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.174 (n=3344)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.02 (IC base=+0.170)

- **PATRÓN** `libro_liquidez` > `2771.502` → IC=+0.177 (n=2623)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2771.502 (IC base=+0.170)

- **PATRÓN** `ballena_activa_n` < `151.0` → IC=+0.184 (n=2717)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 151.0 (IC base=+0.170)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.144 (n=1014)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0036 (IC base=+0.106)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.123 (n=2026)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 11.0 (IC base=+0.106)

- **PATRÓN** `ibs_20min` < `0.0833` → IC=+0.194 (n=1014)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.0833 (IC base=+0.106)

- **PATRÓN** `volumen_spike_ratio` < `1.433` → IC=+0.137 (n=982)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.433 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `4454.2977` → IC=+0.132 (n=2020)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 4454.2977 (IC base=+0.106)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.133 (n=1272)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 29.0 (IC base=+0.106)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.207 (n=370)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.160)

- **PATRÓN** `drift_60min` |x|≤ `0.099` → IC=+0.215 (n=370)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.099 (IC base=+0.160)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.192 (n=768)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 8.0 (IC base=+0.160)

- **PATRÓN** `ibs_20min` > `0.6412` → IC=+0.215 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6412 (IC base=+0.160)

- **PATRÓN** `dist_vwap_pct` > `0.3004` → IC=+0.180 (n=264)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.3004 (IC base=+0.160)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.109` → IC=+0.184 (n=359)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 3.109 (IC base=+0.160)

- **PATRÓN** `volumen_regimen` < `0.8745` → IC=+0.189 (n=561)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.8745 (IC base=+0.160)

- **PATRÓN** `volumen_pendiente_norm` > `0.071` → IC=+0.171 (n=329)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.071 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` < `2.223` → IC=+0.169 (n=724)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 2.223 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` > `1.4195` → IC=+0.163 (n=822)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.4195 (IC base=+0.160)

- **PATRÓN** `libro_liquidez` > `14766.5292` → IC=+0.171 (n=560)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 14766.5292 (IC base=+0.160)

- **PATRÓN** `ballena_activa_n` < `153.0` → IC=+0.200 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 153.0 (IC base=+0.160)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.190 (n=324)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0027 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.2654` → IC=+0.150 (n=855)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.2654 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.145 (n=875)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 7.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.6231` → IC=+0.177 (n=855)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.6231 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.74` → IC=+0.138 (n=186)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 8.74 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.162` → IC=+0.141 (n=882)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 3.162 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.2004` → IC=+0.138 (n=971)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.2004 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `0.7005` → IC=+0.148 (n=867)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.7005 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.07` → IC=+0.177 (n=382)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.07 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.121` → IC=+0.152 (n=845)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.121 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.137 (n=1259)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `359.0` → IC=+0.150 (n=939)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 359.0 (IC base=+0.137)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.247 (n=611)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.2006` → IC=+0.224 (n=610)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2006 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.222 (n=961)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `0.6787` → IC=+0.264 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6787 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `0.3552` → IC=+0.210 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3552 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` < `0.2052` → IC=+0.210 (n=827)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2052 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.951` → IC=+0.224 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.951 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` < `0.8363` → IC=+0.211 (n=610)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8363 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `1.1816` → IC=+0.223 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1816 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.1588` → IC=+0.237 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1588 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `1.4109` → IC=+0.246 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4109 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `2.4387` → IC=+0.223 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4387 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.124 (n=397)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0038 (IC base=+0.089)

- **PATRÓN** `ibs_20min` < `0.0951` → IC=+0.166 (n=300)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.0951 (IC base=+0.089)

- **PATRÓN** `libro_liquidez` > `3974.3907` → IC=+0.126 (n=802)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 3974.3907 (IC base=+0.089)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.128 (n=382)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 43.0 (IC base=+0.089)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.151 (n=459)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0075 (IC base=+0.145)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.148 (n=313)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0091 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.174 (n=618)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 8.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.265 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.932` → IC=+0.200 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.932 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.155` → IC=+0.205 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.155 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.0652` → IC=+0.165 (n=606)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.0652 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` > `0.7239` → IC=+0.156 (n=615)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.7239 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.2809` → IC=+0.173 (n=102)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2809 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `2.482` → IC=+0.146 (n=664)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.482 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `2.2007` → IC=+0.160 (n=301)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.2007 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.151 (n=715)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.02 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `3081.1151` → IC=+0.194 (n=230)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 3081.1151 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.4737` → IC=+0.156 (n=591)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.4737 (IC base=+0.069)

- **PATRÓN** `volumen_spike_ratio` < `1.5709` → IC=+0.135 (n=283)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.5709 (IC base=+0.069)

- **PATRÓN** `libro_liquidez` > `2842.4907` → IC=+0.158 (n=305)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2842.4907 (IC base=+0.069)

- **PATRÓN** `ballena_activa_n` < `32.0` → IC=+0.123 (n=542)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 32.0 (IC base=+0.069)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0238` → IC=+0.170 (n=192)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0238 (IC base=+0.154)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.186 (n=192)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.007 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.3919` → IC=+0.167 (n=169)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.3919 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.181 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 16.0 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.204 (n=86)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.5556` → IC=+0.184 (n=172)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.5556 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.2393` → IC=+0.167 (n=106)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.2393 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` < `1.115` → IC=+0.162 (n=214)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 1.115 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.385` → IC=+0.181 (n=164)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 3.385 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` > `0.6182` → IC=+0.175 (n=192)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.6182 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` < `0.2537` → IC=+0.184 (n=188)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.2537 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.4483` → IC=+0.241 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4483 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `2.6132` → IC=+0.172 (n=56)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.6132 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.183 (n=197)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.02 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `2503.8283` → IC=+0.169 (n=128)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2503.8283 (IC base=+0.154)

- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.158 (n=191)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0117 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.163 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` < `0.61` → IC=+0.134 (n=214)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.61 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` > `1.1597` → IC=+0.292 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1597 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.009` → IC=+0.146 (n=80)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 3.009 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` > `1.2382` → IC=+0.144 (n=71)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.2382 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` > `0.2295` → IC=+0.174 (n=41)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2295 (IC base=+0.115)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.138 (n=172)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 17.0 (IC base=+0.115)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.181 (n=4937)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0046 (IC base=+0.179)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.219 (n=4912)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=15413)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `0.5588` → IC=+0.237 (n=13161)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5588 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.16` → IC=+0.188 (n=5365)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.16 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.354` → IC=+0.251 (n=3620)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.354 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `1.2285` → IC=+0.166 (n=9863)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2285 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.2911` → IC=+0.202 (n=1973)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2911 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `2.6131` → IC=+0.195 (n=4764)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6131 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `2014.2662` → IC=+0.185 (n=13158)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2014.2662 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `76.0` → IC=+0.204 (n=11779)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 76.0 (IC base=+0.179)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.191 (n=11704)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0092 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.1443` → IC=+0.196 (n=5849)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.1443 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=4932)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` < `0.5769` → IC=+0.242 (n=13299)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5769 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.971` → IC=+0.209 (n=1863)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.971 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.675` → IC=+0.190 (n=12827)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 3.675 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` < `0.7049` → IC=+0.165 (n=3951)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.7049 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.2896` → IC=+0.249 (n=1797)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2896 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `2.6167` → IC=+0.199 (n=4166)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.6167 (IC base=+0.188)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.213 (n=8177)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.188)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.243 (n=810)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.214)

- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.243 (n=809)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0084 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.220 (n=2426)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.217 (n=1628)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.323 (n=932)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.666` → IC=+0.348 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.666 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.277` → IC=+0.274 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.277 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `2.2635` → IC=+0.228 (n=1051)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2635 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.230 (n=2511)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `2101.57` → IC=+0.235 (n=808)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2101.57 (IC base=+0.214)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.228 (n=964)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.214)

- **PATRÓN** `sigma_h` < `0.008` → IC=+0.262 (n=2037)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.258)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.261 (n=1826)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.258)

- **PATRÓN** `drift_60min` |x|≤ `0.2021` → IC=+0.270 (n=1358)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2021 (IC base=+0.258)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.273 (n=737)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.258)

- **PATRÓN** `ibs_20min` < `0.4947` → IC=+0.284 (n=2038)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4947 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.472` → IC=+0.263 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.472 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` < `0.1574` → IC=+0.257 (n=2007)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1574 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` > `0.2846` → IC=+0.275 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2846 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` > `2.6427` → IC=+0.274 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6427 (IC base=+0.258)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.260 (n=2247)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `1876.7746` → IC=+0.258 (n=1358)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1876.7746 (IC base=+0.258)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.200 (n=791)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.1752` → IC=+0.166 (n=1577)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1752 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=2478)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.269` → IC=+0.208 (n=2364)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.269 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1244` → IC=+0.191 (n=1280)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1244 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.708` → IC=+0.166 (n=396)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.708 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.182` → IC=+0.155 (n=2156)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 4.182 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.6282` → IC=+0.174 (n=789)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6282 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` < `0.072` → IC=+0.153 (n=2105)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.072 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.2716` → IC=+0.178 (n=340)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2716 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.1761` → IC=+0.160 (n=2029)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1761 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.5329` → IC=+0.153 (n=2061)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.5329 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `268.0` → IC=+0.180 (n=986)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 268.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.196 (n=655)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0026 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.0769` → IC=+0.185 (n=655)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.0769 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.180 (n=742)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.6944` → IC=+0.199 (n=1964)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6944 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.359` → IC=+0.161 (n=440)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 9.359 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `1.1847` → IC=+0.160 (n=1965)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.1847 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.1543` → IC=+0.193 (n=526)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1543 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.4394` → IC=+0.154 (n=1861)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4394 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.7859` → IC=+0.162 (n=1241)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.7859 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `252.0` → IC=+0.152 (n=590)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 252.0 (IC base=+0.148)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.244 (n=815)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.228 (n=2568)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.227 (n=2189)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.301 (n=920)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.376` → IC=+0.311 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.376 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` < `0.0977` → IC=+0.223 (n=2147)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0977 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.6973` → IC=+0.235 (n=1074)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6973 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.230 (n=2878)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `1871.4804` → IC=+0.234 (n=1630)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1871.4804 (IC base=+0.221)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.248 (n=2004)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.240)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.242 (n=2035)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.178` → IC=+0.261 (n=1002)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.178 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.265 (n=852)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.021` → IC=+0.303 (n=760)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.021 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.806` → IC=+0.291 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.806 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.3426` → IC=+0.301 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3426 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.724` → IC=+0.239 (n=947)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.724 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.1354` → IC=+0.249 (n=1434)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1354 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `2077.858` → IC=+0.264 (n=759)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2077.858 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.265 (n=691)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=+0.240)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.186 (n=1682)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0049 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.325` → IC=+0.156 (n=2219)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.325 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.160 (n=2633)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.2627` → IC=+0.193 (n=2522)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.2627 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.1381` → IC=+0.162 (n=1370)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.1381 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.201` → IC=+0.164 (n=1028)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 4.201 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `0.873` → IC=+0.164 (n=1682)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.873 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.2832` → IC=+0.181 (n=334)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2832 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.5223` → IC=+0.170 (n=1083)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5223 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `2.1748` → IC=+0.159 (n=1115)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.1748 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `7151.316` → IC=+0.239 (n=1144)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7151.316 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `79.0` → IC=+0.170 (n=1080)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 79.0 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.194 (n=691)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0032 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.3387` → IC=+0.142 (n=1817)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.3387 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.156 (n=750)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` < `0.7426` → IC=+0.190 (n=2064)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.7426 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.325` → IC=+0.168 (n=422)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 9.325 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `0.8745` → IC=+0.143 (n=1376)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.8745 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.2959` → IC=+0.224 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2959 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` < `2.2358` → IC=+0.135 (n=1743)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.2358 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `1.4314` → IC=+0.141 (n=1980)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.4314 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `5331.93` → IC=+0.204 (n=936)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5331.93 (IC base=+0.131)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.148 (n=1158)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0099 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.179 (n=933)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.4483` → IC=+0.197 (n=2550)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.4483 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `1.0166` → IC=+0.206 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0166 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.938` → IC=+0.262 (n=645)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.938 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `0.8886` → IC=+0.145 (n=1700)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.8886 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` < `0.0987` → IC=+0.123 (n=2394)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.0987 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.137 (n=331)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `1.4667` → IC=+0.127 (n=2484)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 1.4667 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.128 (n=2594)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.02 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `2909.4755` → IC=+0.252 (n=849)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2909.4755 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.135 (n=809)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 26.0 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.143 (n=2420)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0108 (IC base=+0.121)

- **PATRÓN** `drift_60min` |x|≤ `0.1303` → IC=+0.163 (n=807)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.1303 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.158 (n=1129)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 15.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.214 (n=2421)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6364 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.379` → IC=+0.136 (n=2328)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 3.379 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `0.7128` → IC=+0.147 (n=1064)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.7128 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.223` → IC=+0.169 (n=403)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.223 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `1.4382` → IC=+0.158 (n=750)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.4382 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2772.1243` → IC=+0.208 (n=806)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2772.1243 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.139 (n=1986)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 49.0 (IC base=+0.121)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0134` → IC=+0.241 (n=2171)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0134 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.226 (n=2542)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.228 (n=1754)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `0.6047` → IC=+0.268 (n=2171)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6047 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` > `0.197` → IC=+0.236 (n=1341)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.197 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.726` → IC=+0.265 (n=822)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.726 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` < `1.2317` → IC=+0.227 (n=2431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2317 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` > `0.6388` → IC=+0.224 (n=2430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6388 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.2376` → IC=+0.252 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2376 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.5204` → IC=+0.250 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5204 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.226 (n=2111)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `2672.137` → IC=+0.237 (n=1620)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2672.137 (IC base=+0.222)

- **PATRÓN** `sigma_h` > `0.0227` → IC=+0.242 (n=1149)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0227 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.232 (n=2381)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` < `0.51` → IC=+0.263 (n=2537)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.51 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.924` → IC=+0.258 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.924 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `1.2332` → IC=+0.254 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2332 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2822` → IC=+0.296 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2822 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `1.4357` → IC=+0.228 (n=2340)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4357 (IC base=+0.224)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.218 (n=2275)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.224)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.183 (n=4407)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.237 (n=1493)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.4967` → IC=+0.207 (n=4480)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4967 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=1617)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.198 (n=3065)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 11.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` > `0.9408` → IC=+0.244 (n=1494)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9408 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` > `0.1686` → IC=+0.200 (n=1655)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1686 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` < `0.2409` → IC=+0.201 (n=2831)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2409 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.198` → IC=+0.217 (n=734)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.198 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.631` → IC=+0.198 (n=3991)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 3.631 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` < `0.7075` → IC=+0.210 (n=1422)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7075 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` > `0.8906` → IC=+0.203 (n=2154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8906 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.1673` → IC=+0.220 (n=1254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1673 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` < `1.4551` → IC=+0.206 (n=1471)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4551 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` > `2.2745` → IC=+0.202 (n=2000)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2745 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=3399)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `2970.457` → IC=+0.208 (n=4001)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2970.457 (IC base=+0.198)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.229 (n=1111)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.4871` → IC=+0.197 (n=3317)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.4871 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.200 (n=1111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.200 (n=1486)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` < `0.1778` → IC=+0.198 (n=1460)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.1778 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.6563` → IC=+0.186 (n=552)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.6563 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.141` → IC=+0.188 (n=3326)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 6.141 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.2546` → IC=+0.187 (n=3124)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 1.2546 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` < `0.0976` → IC=+0.186 (n=3024)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.0976 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` < `1.5334` → IC=+0.187 (n=1440)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.5334 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `1.8164` → IC=+0.187 (n=2181)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 1.8164 (IC base=+0.181)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.183 (n=4407)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.195 (n=2172)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 69.0 (IC base=+0.181)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.252 (n=511)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.229)

- **PATRÓN** `drift_60min` |x|≤ `0.0834` → IC=+0.276 (n=194)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0834 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.230 (n=524)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.229)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.232 (n=263)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` < `0.2754` → IC=+0.267 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2754 (IC base=+0.229)

- **PATRÓN** `dist_vwap_pct` < `0.1788` → IC=+0.237 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1788 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.078` → IC=+0.244 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.078 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.566` → IC=+0.231 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.566 (IC base=+0.229)

- **PATRÓN** `volumen_regimen` < `1.2246` → IC=+0.239 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2246 (IC base=+0.229)

- **PATRÓN** `volumen_regimen` > `0.8546` → IC=+0.245 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8546 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` > `0.2924` → IC=+0.327 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2924 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` < `1.8412` → IC=+0.240 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8412 (IC base=+0.229)

- **PATRÓN** `libro_liquidez` > `12456.1721` → IC=+0.251 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12456.1721 (IC base=+0.229)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.239 (n=497)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.3661` → IC=+0.173 (n=1125)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.3661 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.199 (n=410)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.159)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.188 (n=418)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 5.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` < `0.1485` → IC=+0.188 (n=495)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.1485 (IC base=+0.159)

- **PATRÓN** `ibs_20min` > `0.6044` → IC=+0.162 (n=510)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.6044 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` > `0.6734` → IC=+0.202 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6734 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` < `0.2114` → IC=+0.160 (n=1141)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.2114 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.391` → IC=+0.177 (n=1107)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 6.391 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` < `0.8855` → IC=+0.197 (n=750)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.8855 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` > `0.0691` → IC=+0.182 (n=520)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.0691 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` < `2.5306` → IC=+0.164 (n=1120)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 2.5306 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` > `1.8136` → IC=+0.176 (n=747)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.8136 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `11419.5725` → IC=+0.171 (n=1124)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 11419.5725 (IC base=+0.159)

- **PATRÓN** `ballena_activa_n` < `701.0` → IC=+0.171 (n=1079)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 701.0 (IC base=+0.159)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.201 (n=232)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.172)

- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.185 (n=316)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0098 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.5794` → IC=+0.180 (n=696)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.5794 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.232 (n=248)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.235 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.51` → IC=+0.217 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.51 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` < `0.3521` → IC=+0.172 (n=834)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` < 0.3521 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.2084` → IC=+0.226 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2084 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `3.3854` → IC=+0.184 (n=232)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 3.3854 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `2525.266` → IC=+0.217 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2525.266 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.229 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.227)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.275 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `2.0` → IC=+0.267 (n=58)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 2.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.2121` → IC=+0.263 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2121 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.442` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.442 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` < `0.2021` → IC=+0.250 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2021 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `2.4518` → IC=+0.250 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4518 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `1.861` → IC=+0.250 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.861 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `2407.5596` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2407.5596 (IC base=+0.227)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.229 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 27.0 (IC base=+0.227)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0079` → IC=+0.214 (n=1314)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0079 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.4605` → IC=+0.207 (n=1314)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4605 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=476)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` < `0.5155` → IC=+0.217 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5155 (IC base=+0.201)

- **PATRÓN** `ibs_20min` > `0.8784` → IC=+0.204 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8784 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.152` → IC=+0.208 (n=1185)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.152 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` < `0.8824` → IC=+0.204 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8824 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` > `1.2398` → IC=+0.211 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2398 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` < `0.1056` → IC=+0.205 (n=1209)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1056 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.1645` → IC=+0.204 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1645 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` < `1.4166` → IC=+0.224 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4166 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=1338)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.246 (n=356)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.4923` → IC=+0.204 (n=1060)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4923 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.196 (n=413)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 16.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.188 (n=757)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 11.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` < `0.7503` → IC=+0.185 (n=1060)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.7503 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `0.0847` → IC=+0.180 (n=1059)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.0847 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.6442` → IC=+0.189 (n=191)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.6442 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.654` → IC=+0.184 (n=1082)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 6.654 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `1.2449` → IC=+0.193 (n=1060)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 1.2449 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.0735` → IC=+0.198 (n=448)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.0735 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` < `2.1797` → IC=+0.191 (n=913)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 2.1797 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `7238.8989` → IC=+0.192 (n=1059)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 7238.8989 (IC base=+0.179)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.222 (n=419)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.2892` → IC=+0.172 (n=419)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.2892 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.201 (n=600)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.252 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` > `0.2522` → IC=+0.203 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2522 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.252` → IC=+0.217 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.252 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `0.7061` → IC=+0.206 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7061 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` < `0.1075` → IC=+0.176 (n=566)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` < 0.1075 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.1633` → IC=+0.193 (n=190)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.1633 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `2.5405` → IC=+0.209 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5405 (IC base=+0.171)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.176 (n=724)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.02 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `3205.049` → IC=+0.196 (n=561)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 3205.049 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.185 (n=610)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 54.0 (IC base=+0.171)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.192 (n=300)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0084 (IC base=+0.192)

- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.215 (n=205)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0103 (IC base=+0.192)

- **PATRÓN** `drift_60min` |x|≤ `0.357` → IC=+0.229 (n=300)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.357 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.223 (n=305)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.192)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.241 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` > `0.762` → IC=+0.211 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.762 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.947` → IC=+0.199 (n=81)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 8.947 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.837` → IC=+0.194 (n=396)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 2.837 (IC base=+0.192)

- **PATRÓN** `volumen_regimen` < `0.7658` → IC=+0.210 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7658 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` < `0.1073` → IC=+0.228 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1073 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` < `1.6214` → IC=+0.197 (n=193)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.6214 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` > `2.2075` → IC=+0.215 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2075 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `3135.8736` → IC=+0.219 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3135.8736 (IC base=+0.192)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.229 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 49.0 (IC base=+0.192)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.157 (n=640)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0038 (IC base=+0.072)

- **PATRÓN** `ibs_20min` > `0.4165` → IC=+0.147 (n=1361)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.4165 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` > `0.7189` → IC=+0.164 (n=251)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.7189 (IC base=+0.072)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.442` → IC=+0.184 (n=305)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 11.442 (IC base=+0.072)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.158 (n=185)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.072)

- **PATRÓN** `ibs_20min` < `0.1875` → IC=+0.255 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1875 (IC base=+0.061)

- **PATRÓN** `dist_vwap_pct` < `0.0873` → IC=+0.131 (n=643)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.0873 (IC base=+0.061)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.686` → IC=+0.142 (n=107)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 10.686 (IC base=+0.061)

- **PATRÓN** `volumen_pendiente_norm` > `0.147` → IC=+0.195 (n=175)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.147 (IC base=+0.061)

- **PATRÓN** `volumen_spike_ratio` < `1.4824` → IC=+0.130 (n=260)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.4824 (IC base=+0.061)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.138 (n=492)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0056 (IC base=+0.092)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.137 (n=166)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 18.0 (IC base=+0.092)

- **PATRÓN** `ibs_20min` > `0.3752` → IC=+0.170 (n=461)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.3752 (IC base=+0.092)

- **PATRÓN** `dist_vwap_pct` > `0.119` → IC=+0.158 (n=241)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.119 (IC base=+0.092)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.461` → IC=+0.121 (n=262)

  - _Acción_: Kelly boost +0.61€ cuando `sigma_ewma_delta_pct` > 3.461 (IC base=+0.092)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.130 (n=217)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0034 (IC base=+0.081)

- **PATRÓN** `ibs_20min` < `0.0468` → IC=+0.285 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0468 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` < `0.1067` → IC=+0.134 (n=307)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1067 (IC base=+0.081)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.647` → IC=+0.132 (n=259)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 4.647 (IC base=+0.081)

- **PATRÓN** `volumen_regimen` < `1.1823` → IC=+0.120 (n=301)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_regimen` < 1.1823 (IC base=+0.081)

- **PATRÓN** `volumen_pendiente_norm` > `0.0753` → IC=+0.156 (n=123)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.0753 (IC base=+0.081)

- **PATRÓN** `volumen_spike_ratio` < `2.5247` → IC=+0.124 (n=277)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.5247 (IC base=+0.081)

### GBM_LATE_60M#ETH#60min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.155 (n=320)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0046 (IC base=+0.095)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.131 (n=445)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 7.0 (IC base=+0.095)

- **PATRÓN** `ibs_20min` > `0.6632` → IC=+0.206 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6632 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` > `0.1226` → IC=+0.181 (n=236)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.1226 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.658` → IC=+0.262 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.658 (IC base=+0.095)

- **PATRÓN** `volumen_regimen` < `0.8187` → IC=+0.124 (n=296)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 0.8187 (IC base=+0.095)

- **PATRÓN** `volumen_pendiente_norm` > `0.2835` → IC=+0.177 (n=60)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2835 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `1732.7498` → IC=+0.151 (n=147)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1732.7498 (IC base=+0.095)

- **PATRÓN** `ibs_20min` < `0.0162` → IC=+0.309 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0162 (IC base=+0.015)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.103` → IC=+0.188 (n=30)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 11.103 (IC base=+0.015)

- **PATRÓN** `volumen_pendiente_norm` > `0.1353` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.1353 (IC base=+0.015)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `ibs_20min` > `0.1304` → IC=-0.217 (n=51)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1304
  - _Potencial_: sin este filtro IC_bueno=+0.252 (n=155)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.159 (n=315)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.75 (IC base=+0.030)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.874` → IC=+0.141 (n=129)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 7.874 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.2436` → IC=+0.152 (n=87)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.2436 (IC base=+0.030)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.160 (n=186)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0092 (IC base=+0.078)

- **PATRÓN** `ibs_20min` < `0.1304` → IC=+0.252 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1304 (IC base=+0.078)

- **PATRÓN** `dist_vwap_pct` > `0.1531` → IC=+0.167 (n=37)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1531 (IC base=+0.078)

- **PATRÓN** `dist_vwap_pct` < `0.3549` → IC=+0.171 (n=171)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.3549 (IC base=+0.078)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.757` → IC=+0.348 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.757 (IC base=+0.078)

- **PATRÓN** `volumen_regimen` > `1.074` → IC=+0.222 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.074 (IC base=+0.078)

- **PATRÓN** `volumen_pendiente_norm` > `0.1518` → IC=+0.276 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1518 (IC base=+0.078)

- **PATRÓN** `volumen_spike_ratio` < `2.1906` → IC=+0.181 (n=117)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 2.1906 (IC base=+0.078)

- **PATRÓN** `volumen_spike_ratio` > `2.5298` → IC=+0.223 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5298 (IC base=+0.078)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.204 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.078)

- **PATRÓN** `libro_liquidez` > `798.7992` → IC=+0.174 (n=93)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 798.7992 (IC base=+0.078)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `8.0` → IC=-0.328 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=219)

- **FILTRO** `dist_vwap_pct` > `0.2348` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2348
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=264)

- **FILTRO** `volumen_regimen` < `0.7615` → IC=-0.333 (n=70)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7615
  - _Potencial_: sin este filtro IC_bueno=-0.162 (n=211)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.381 (n=57)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.243 (n=177)

- **FILTRO** `hora_utc` < `5.0` → IC=-0.300 (n=53)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=181)

- **FILTRO** `dist_vwap_pct` > `0.338` → IC=-0.382 (n=32)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.338
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=202)

- **FILTRO** `sigma_ewma_delta_pct` > `10.676` → IC=-0.308 (n=24)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 10.676
  - _Potencial_: sin este filtro IC_bueno=-0.274 (n=210)

- **FILTRO** `volumen_pendiente_norm` > `0.0538` → IC=-0.389 (n=25)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0538
  - _Potencial_: sin este filtro IC_bueno=-0.252 (n=123)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.266 (n=45)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=48)

- **FILTRO** `ibs_20min` < `0.1017` → IC=-0.250 (n=30)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1017
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=63)

- **FILTRO** `volumen_regimen` < `0.8417` → IC=-0.300 (n=23)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8417
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=70)

- **FILTRO** `volumen_spike_ratio` > `3.5274` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 3.5274
  - _Potencial_: sin este filtro IC_bueno=-0.154 (n=53)

- **FILTRO** `sigma_h` < `0.002` → IC=-0.315 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.002
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=77)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.292 (n=51)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=51)

- **FILTRO** `volumen_regimen` > `0.8213` → IC=-0.315 (n=25)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8213
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=77)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.8227` → IC=-0.378 (n=47)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8227
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=48)

- **FILTRO** `hora_utc` < `5.0` → IC=-0.350 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.261 (n=69)

- **FILTRO** `dist_vwap_pct` > `0.1182` → IC=-0.333 (n=28)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1182
  - _Potencial_: sin este filtro IC_bueno=-0.254 (n=59)

- **FILTRO** `volumen_spike_ratio` > `2.2319` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.2319
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=37)

- **FILTRO** `volumen_spike_ratio` < `1.4507` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.4507
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=37)

- **PATRÓN** `ibs_20min` > `0.9508` → IC=+0.157 (n=33)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.9508 (IC base=-0.160)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=77)

- **FILTRO** `volumen_spike_ratio` < `1.5847` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.5847
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=51)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.225 (n=67)

- **FILTRO** `dist_vwap_pct` < `0.219` → IC=-0.346 (n=24)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.219
  - _Potencial_: sin este filtro IC_bueno=-0.283 (n=21)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.458 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=23)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.160 (n=207)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0057 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.142 (n=227)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 15.0 (IC base=+0.103)

- **PATRÓN** `ibs_20min` > `0.6732` → IC=+0.148 (n=456)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.6732 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` > `0.4856` → IC=+0.207 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4856 (IC base=+0.103)

- **PATRÓN** `volumen_regimen` < `0.6589` → IC=+0.152 (n=153)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6589 (IC base=+0.103)

- **PATRÓN** `volumen_pendiente_norm` < `0.2335` → IC=+0.134 (n=394)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` < 0.2335 (IC base=+0.103)

- **PATRÓN** `volumen_spike_ratio` < `2.5521` → IC=+0.136 (n=355)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.5521 (IC base=+0.103)

- **PATRÓN** `ibs_20min` < `0.1622` → IC=+0.167 (n=467)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.1622 (IC base=+0.071)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.127` → IC=+0.189 (n=162)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 9.127 (IC base=+0.071)

- **PATRÓN** `libro_liquidez` > `2938.1704` → IC=+0.157 (n=354)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2938.1704 (IC base=+0.071)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6544` → IC=-0.250 (n=46)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6544
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=140)

- **PATRÓN** `sigma_h` > `0.004` → IC=+0.212 (n=109)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.004 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.167 (n=163)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 12.0 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.174 (n=90)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 6.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.1361` → IC=+0.203 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1361 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.2224` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.2224 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `0.0916` → IC=+0.160 (n=245)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.0916 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.253` → IC=+0.175 (n=75)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 10.253 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.645` → IC=+0.168 (n=191)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` < 4.645 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` > `0.6861` → IC=+0.167 (n=214)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.6861 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` < `0.078` → IC=+0.179 (n=185)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` < 0.078 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.2806` → IC=+0.175 (n=38)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2806 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.2476` → IC=+0.170 (n=183)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 2.2476 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.449` → IC=+0.162 (n=208)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.449 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `5151.5741` → IC=+0.161 (n=160)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 5151.5741 (IC base=+0.151)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `ibs_20min` > `0.2345` → IC=-0.130 (n=90)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2345
  - _Potencial_: sin este filtro IC_bueno=+0.131 (n=177)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.139 (n=142)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0045 (IC base=+0.085)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.161 (n=57)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 18.0 (IC base=+0.085)

- **PATRÓN** `ibs_20min` > `0.7141` → IC=+0.128 (n=162)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` > 0.7141 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.022` → IC=+0.139 (n=120)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 3.022 (IC base=+0.085)

- **PATRÓN** `volumen_pendiente_norm` < `0.1371` → IC=+0.127 (n=148)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1371 (IC base=+0.085)

- **PATRÓN** `volumen_spike_ratio` < `1.7943` → IC=+0.174 (n=90)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.7943 (IC base=+0.085)

- **PATRÓN** `ibs_20min` < `0.2345` → IC=+0.131 (n=177)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.2345 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.059` → IC=+0.259 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.059 (IC base=+0.043)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.4444` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4444
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=91)

- **FILTRO** `dist_vwap_pct` > `0.2724` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2724
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=97)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.302 (n=104)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.270 (n=146)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.242)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.253 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.242)

- **PATRÓN** `dist_vwap_pct` > `0.6434` → IC=+0.375 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6434 (IC base=+0.242)

- **PATRÓN** `dist_vwap_pct` < `0.2189` → IC=+0.242 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2189 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.333` → IC=+0.297 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.333 (IC base=+0.242)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.294 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` < `0.2516` → IC=+0.296 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2516 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.325 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` < `1.4907` → IC=+0.372 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4907 (IC base=+0.242)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.246 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.242)

- **PATRÓN** `libro_liquidez` > `665.8128` → IC=+0.245 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 665.8128 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.321` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.321 (IC base=-0.077)

### LATE_WINDOW_5MIN
- **PATRÓN** `drift_ventana_pct` |x|> `0.332` → IC=+0.296 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.332 (IC base=+0.289)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.370 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.289)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.450 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.9778` → IC=+0.352 (n=52)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9778 (IC base=+0.289)

- **PATRÓN** `ballena_activa_n` < `1245.0` → IC=+0.300 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1245.0 (IC base=+0.289)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3418` → IC=+0.250 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3418 (IC base=+0.216)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.226 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.216)

- **PATRÓN** `elapsed_s` < `214.1` → IC=+0.240 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 214.1 (IC base=+0.216)

- **PATRÓN** `drift_15min` |x|≤ `1.2534` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.2534 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.269 (n=37)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.216)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.310 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.216)

- **PATRÓN** `ballena_activa_n` < `1854.0` → IC=+0.272 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1854.0 (IC base=+0.216)

### LATE_WINDOW_5MIN#BTC#5min
- **PATRÓN** `drift_ventana_pct` |x|> `0.332` → IC=+0.296 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.332 (IC base=+0.289)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.370 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.289)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.450 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.9778` → IC=+0.352 (n=52)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9778 (IC base=+0.289)

- **PATRÓN** `ballena_activa_n` < `1245.0` → IC=+0.300 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1245.0 (IC base=+0.289)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3418` → IC=+0.250 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3418 (IC base=+0.216)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.226 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.216)

- **PATRÓN** `elapsed_s` < `214.1` → IC=+0.240 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 214.1 (IC base=+0.216)

- **PATRÓN** `drift_15min` |x|≤ `1.2534` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.2534 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.269 (n=37)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.216)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.310 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.216)

- **PATRÓN** `ballena_activa_n` < `1854.0` → IC=+0.272 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1854.0 (IC base=+0.216)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.121 (n=1142)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.5 (IC base=+0.102)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.121 (n=1142)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.5 (IC base=+0.102)

### LIQUIDACIONES_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=168)

- **FILTRO** `libro_liquidez` < `2696.1504` → IC=-0.229 (n=46)

  - _Acción_: SKIP cuando `libro_liquidez` < 2696.1504
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=138)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=246)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=232)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=60)

- **FILTRO** `libro_liquidez` < `11321.3584` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_liquidez` < 11321.3584
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=60)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=25)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.143 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=10)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.136 (n=31)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=107)

### LIQUIDACIONES_15M#XRP#15min
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
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=3096)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=100)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=57)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=89)

- **FILTRO** `ballena_activa_n` > `118.0` → IC=-0.217 (n=58)

  - _Acción_: SKIP cuando `ballena_activa_n` > 118.0
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=29)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.188 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=125)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=20)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=20)

- **FILTRO** `libro_liquidez` < `15247.5472` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `libro_liquidez` < 15247.5472
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=12)

- **FILTRO** `ballena_activa_n` > `558.0` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `ballena_activa_n` > 558.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.136 (n=207)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.495 (IC base=+0.046)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=1130)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=1084)

- **FILTRO** `liq_usd_total` < `12056.79` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `liq_usd_total` < 12056.79
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **FILTRO** `hora_utc` > `6.0` → IC=-0.292 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=12)

- **FILTRO** `ballena_activa_n` > `118.0` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `ballena_activa_n` > 118.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.505` → IC=-0.140 (n=23)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=695)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=703)

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
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=389)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=370)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.140 (n=148)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.495 (IC base=+0.013)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=795)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=795)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.133 (n=246)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=629)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=667)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=667)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=218)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=218)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.136 (n=53)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=180)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.122 (n=88)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=145)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=168)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=192)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=244)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=207)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=318)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=318)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=231)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.43` → IC=-0.120 (n=1684)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=1813)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.122 (n=43)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=24)

- **FILTRO** `restante_min` < `3.89` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `restante_min` < 3.89
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

- **FILTRO** `hora_utc` < `17.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

- **FILTRO** `lag_apertura_s` > `66.61` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `lag_apertura_s` > 66.61
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.135 (n=228)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=122)

- **FILTRO** `profundidad_ratio` < `253.7` → IC=-0.133 (n=115)

  - _Acción_: SKIP cuando `profundidad_ratio` < 253.7
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=235)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.173 (n=111)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` < 0.46 (IC base=+0.026)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.207 (n=39)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=184)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.154 (n=102)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=123)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.140 (n=231)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=78)

- **FILTRO** `profundidad_ratio` < `53.7` → IC=-0.170 (n=101)

  - _Acción_: SKIP cuando `profundidad_ratio` < 53.7
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=208)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.245 (n=53)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=249)

- **PATRÓN** `py_entrada` < `0.46` → IC=+0.154 (n=79)

  - _Acción_: Kelly boost +0.77€ cuando `py_entrada` < 0.46 (IC base=-0.026)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.139 (n=189)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=202)

- **FILTRO** `restante_min` < `3.36` → IC=-0.195 (n=129)

  - _Acción_: SKIP cuando `restante_min` < 3.36
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=262)

- **FILTRO** `lag_apertura_s` > `96.44` → IC=-0.202 (n=132)

  - _Acción_: SKIP cuando `lag_apertura_s` > 96.44
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=259)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.157 (n=65)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=246)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **PATRÓN** `py_entrada` > `0.48` → IC=+0.129 (n=122)

  - _Acción_: Kelly boost +0.65€ cuando `py_entrada` > 0.48 (IC base=-0.020)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.139 (n=236)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=123)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.183 (n=99)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=348)

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

- **FILTRO** `libro_liquidez` < `15906.9303` → IC=-0.152 (n=268)

  - _Acción_: SKIP cuando `libro_liquidez` < 15906.9303
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=805)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=2289)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=1413)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.47` → IC=-0.164 (n=5045)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=16324)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.166 (n=5516)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=16569)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.185 (n=953)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=2875)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.156 (n=911)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=3038)

- **PATRÓN** `libro_liquidez` > `1969.8015` → IC=+0.154 (n=957)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 1969.8015 (IC base=+0.037)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.122 (n=1827)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.5 (IC base=+0.014)

- **PATRÓN** `libro_liquidez` > `1586.3048` → IC=+0.149 (n=1343)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1586.3048 (IC base=+0.014)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.174 (n=760)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=2411)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.173 (n=941)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=2937)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.185 (n=995)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=3021)

- **PATRÓN** `ibs_20min` > `0.9645` → IC=+0.121 (n=1319)

  - _Acción_: Kelly boost +0.60€ cuando `ibs_20min` > 0.9645 (IC base=+0.036)

- **PATRÓN** `libro_liquidez` > `1870.3173` → IC=+0.131 (n=1319)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 1870.3173 (IC base=+0.036)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=2246)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=2666)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=3406)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.172 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=413)

- **FILTRO** `ibs_20min` > `0.1725` → IC=-0.137 (n=133)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1725
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=403)

### MOMENTUM_IBS_15M_FADE#DOGE#15min
- **FILTRO** `libro_liquidez` < `2574.706` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 2574.706
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `ibs_20min` < `0.1975` → IC=-0.223 (n=110)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1975
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=224)

- **FILTRO** `py_entrada` > `0.615` → IC=-0.216 (n=86)

  - _Acción_: SKIP cuando `py_entrada` > 0.615
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=325)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=818)

- **FILTRO** `libro_liquidez` < `2042.3274` → IC=-0.163 (n=342)

  - _Acción_: SKIP cuando `libro_liquidez` < 2042.3274
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=696)

### MOMENTUM_IBS_5M#BNB#5min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=41)

- **FILTRO** `drift_7min_pct` |x|> `0.0331` → IC=-0.158 (n=36)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.0331
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=19)

- **PATRÓN** `drift_7min_pct` |x|≤ `0.0331` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_7min_pct` |x|≤ 0.0331 (IC base=-0.026)

### MOMENTUM_IBS_5M#BTC#5min
- **FILTRO** `hora_utc` > `18.0` → IC=-0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 18.0
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=90)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.152 (n=44)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 17.0 (IC base=+0.037)

### MOMENTUM_IBS_5M#DOGE#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=39)

### MOMENTUM_IBS_5M#ETH#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=414)

### MOMENTUM_IBS_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=631)

### MOMENTUM_IBS_5M_BALLENA
- **FILTRO** `hora_utc` < `8.0` → IC=-0.131 (n=14761)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=33104)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.285 (n=11507)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=36358)

- **FILTRO** `ibs_7min` < `0.25` → IC=-0.232 (n=11961)

  - _Acción_: SKIP cuando `ibs_7min` < 0.25
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=35904)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.154 (n=15780)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=32085)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.236 (n=14688)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=45964)

- **FILTRO** `ibs_7min` > `0.2857` → IC=-0.179 (n=15066)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=45586)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.146 (n=2381)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=5858)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.311 (n=1974)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=6265)

- **FILTRO** `ibs_7min` < `0.709` → IC=-0.247 (n=2718)

  - _Acción_: SKIP cuando `ibs_7min` < 0.709
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=5521)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.173 (n=1931)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=6308)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.269 (n=2580)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=7943)

- **FILTRO** `ibs_7min` > `0.775` → IC=-0.208 (n=2627)

  - _Acción_: SKIP cuando `ibs_7min` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=7896)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.128 (n=1948)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=6183)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.263 (n=1851)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=6280)

- **FILTRO** `ibs_7min` < `0.7349` → IC=-0.197 (n=2032)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7349
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=6099)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.188 (n=2022)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=6109)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.264 (n=1996)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=6277)

- **FILTRO** `ibs_7min` > `0.2664` → IC=-0.195 (n=2068)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2664
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=6205)

- **FILTRO** `ballena_activa_n` > `148.0` → IC=-0.184 (n=2055)

  - _Acción_: SKIP cuando `ballena_activa_n` > 148.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=6218)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.163 (n=1918)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=5918)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.318 (n=1876)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=5960)

- **FILTRO** `ibs_7min` < `0.7021` → IC=-0.245 (n=2585)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7021
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=5251)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.223 (n=1660)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=6176)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.246 (n=2541)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=8658)

- **FILTRO** `ibs_7min` > `0.7342` → IC=-0.174 (n=2798)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7342
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=8401)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.126 (n=2545)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=5294)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.261 (n=1803)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=6036)

- **FILTRO** `ibs_7min` < `0.734` → IC=-0.186 (n=1958)

  - _Acción_: SKIP cuando `ibs_7min` < 0.734
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=5881)

- **FILTRO** `ballena_activa_n` > `28.0` → IC=-0.190 (n=1942)

  - _Acción_: SKIP cuando `ballena_activa_n` > 28.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=5897)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.263 (n=2020)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=6084)

- **FILTRO** `ibs_7min` > `0.2751` → IC=-0.178 (n=2025)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2751
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=6079)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.179 (n=1990)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=6114)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.272 (n=1959)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=6013)

- **FILTRO** `ibs_7min` < `0.2333` → IC=-0.234 (n=1992)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2333
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=5980)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.185 (n=2740)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=8843)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.282 (n=1928)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=5920)

- **FILTRO** `ibs_7min` < `0.2286` → IC=-0.224 (n=1962)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2286
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=5886)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.200 (n=1834)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=6014)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.209 (n=2667)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=8303)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.158 (n=299)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=979)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=1263)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.160 (n=51)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=631)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=815)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=371)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.138 (n=158)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=315)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.129 (n=68)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=601)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=336)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.398` → IC=+0.141 (n=1027)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.71€ cuando `delta_ratio` |x|> 0.398 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.135 (n=478)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 14.0 (IC base=+0.127)

- **PATRÓN** `total_vol_5m` < `3646.355` → IC=+0.148 (n=685)

  - _Acción_: Kelly boost +0.74€ cuando `total_vol_5m` < 3646.355 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `3725.3423` → IC=+0.130 (n=466)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 3725.3423 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.149 (n=354)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 14.0 (IC base=+0.127)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4372` → IC=+0.163 (n=81)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.81€ cuando `delta_ratio` |x|> 0.4372 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.220 (n=116)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `2614.7862` → IC=+0.235 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2614.7862 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.189 (n=104)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 9.0 (IC base=+0.148)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3988` → IC=+0.129 (n=203)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.65€ cuando `delta_ratio` |x|> 0.3988 (IC base=+0.110)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.121 (n=180)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` < 14.0 (IC base=+0.110)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.121 (n=238)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.04 (IC base=+0.110)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.144 (n=99)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 10.0 (IC base=+0.110)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4156` → IC=+0.176 (n=137)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio` |x|> 0.4156 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.149 (n=212)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 4.0 (IC base=+0.127)

- **PATRÓN** `total_vol_5m` < `388.5476` → IC=+0.220 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 388.5476 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `7205.1728` → IC=+0.134 (n=184)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 7205.1728 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `72.0` → IC=+0.196 (n=90)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 72.0 (IC base=+0.127)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4332` → IC=+0.241 (n=83)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4332 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.214 (n=61)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.149)

- **PATRÓN** `total_vol_5m` < `8043.774` → IC=+0.170 (n=183)

  - _Acción_: Kelly boost +0.85€ cuando `total_vol_5m` < 8043.774 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `3092.8641` → IC=+0.160 (n=183)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 3092.8641 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.189 (n=59)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 28.0 (IC base=+0.149)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `13.0` → IC=+0.121 (n=172)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` < 13.0 (IC base=+0.094)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.183 (n=121)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.094)

- **PATRÓN** `libro_liquidez` > `3635.4092` → IC=+0.170 (n=89)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 3635.4092 (IC base=+0.094)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `8.4547` → IC=-0.256 (n=43)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.4547
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=130)

- **FILTRO** `sigma_h` > `0.0051` → IC=-0.265 (n=296)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0051
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=299)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.169 (n=149)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0034 (IC base=-0.085)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0072` → IC=-0.348 (n=44)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0072
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=134)

- **FILTRO** `T_h` > `87.9981` → IC=-0.283 (n=44)

  - _Acción_: SKIP cuando `T_h` > 87.9981
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=134)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.308 (n=45)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=-0.044)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0055` → IC=-0.152 (n=44)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0055
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=16)

- **FILTRO** `pct_vs_K` |x|> `7.7861` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.7861
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=40)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `T_h` < `87.9936` → IC=-0.148 (n=52)

  - _Acción_: SKIP cuando `T_h` < 87.9936
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=52)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.224 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=-0.066)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0097` → IC=-0.224 (n=411)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=138)

- **FILTRO** `sigma_h` > `0.0089` → IC=-0.312 (n=115)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0089
  - _Potencial_: sin este filtro IC_bueno=-0.228 (n=347)

- **FILTRO** `pct_vs_K` |x|> `3.4232` → IC=-0.440 (n=115)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.4232
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=347)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0042` → IC=-0.202 (n=45)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0042
  - _Potencial_: sin este filtro IC_bueno=-0.127 (n=140)

- **FILTRO** `T_h` > `79.6334` → IC=-0.180 (n=123)

  - _Acción_: SKIP cuando `T_h` > 79.6334
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=62)

- **FILTRO** `pct_vs_K` |x|> `2.0268` → IC=-0.395 (n=84)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.0268
  - _Potencial_: sin este filtro IC_bueno=-0.155 (n=85)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `sigma_h` > `0.0042` → IC=-0.184 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0042
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=11)

- **FILTRO** `T_h` < `139.5329` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `T_h` < 139.5329
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `sigma_h` < `0.0085` → IC=-0.239 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

- **FILTRO** `T_h` > `144.5457` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` > 144.5457
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.0049` → IC=-0.274 (n=51)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0049
  - _Potencial_: sin este filtro IC_bueno=-0.236 (n=104)

- **FILTRO** `T_h` < `87.9882` → IC=-0.269 (n=50)

  - _Acción_: SKIP cuando `T_h` < 87.9882
  - _Potencial_: sin este filtro IC_bueno=-0.238 (n=105)

- **FILTRO** `pct_vs_K` |x|> `2.6864` → IC=-0.403 (n=70)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.6864
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=72)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `T_h` < `145.7969` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` < 145.7969
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0083` → IC=-0.276 (n=47)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0083
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=97)

- **FILTRO** `T_h` > `113.0501` → IC=-0.199 (n=71)

  - _Acción_: SKIP cuando `T_h` > 113.0501
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=73)

- **FILTRO** `sigma_h` > `0.015` → IC=-0.340 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.015
  - _Potencial_: sin este filtro IC_bueno=-0.270 (n=72)

- **FILTRO** `pct_vs_K` |x|> `3.8526` → IC=-0.412 (n=32)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.8526
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=63)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1236` → IC=+0.475 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1236 (IC base=+0.343)

- **PATRÓN** `sigma_h` < `0.0135` → IC=+0.365 (n=87)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0135 (IC base=+0.343)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.388 (n=87)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.343)

- **PATRÓN** `T_h` < `0.9178` → IC=+0.359 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.9178 (IC base=+0.343)

- **PATRÓN** `T_h` > `1.1834` → IC=+0.403 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.1834 (IC base=+0.343)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.476 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.343)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.362 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.343)

- **PATRÓN** `edge` > `0.096` → IC=+0.446 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.096 (IC base=+0.418)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.429 (n=68)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.418)

- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.441 (n=134)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.418)

- **PATRÓN** `T_h` < `0.5967` → IC=+0.430 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.5967 (IC base=+0.418)

- **PATRÓN** `T_h` > `1.4829` → IC=+0.442 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4829 (IC base=+0.418)

- **PATRÓN** `dist_50` > `0.3811` → IC=+0.466 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3811 (IC base=+0.418)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.478 (n=133)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.418)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1026` → IC=+0.457 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1026 (IC base=+0.430)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.417 (n=22)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.430)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.460 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.430)

- **PATRÓN** `T_h` < `0.9672` → IC=+0.456 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.9672 (IC base=+0.430)

- **PATRÓN** `T_h` > `0.4508` → IC=+0.423 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4508 (IC base=+0.430)

- **PATRÓN** `dist_50` > `0.4084` → IC=+0.478 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4084 (IC base=+0.430)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.423 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.430)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.441 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.430)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.1975` → IC=+0.482 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1975 (IC base=+0.433)

- **PATRÓN** `sigma_h` < `0.016` → IC=+0.464 (n=54)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.016 (IC base=+0.433)

- **PATRÓN** `T_h` > `0.4742` → IC=+0.446 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4742 (IC base=+0.433)

- **PATRÓN** `dist_50` > `0.3288` → IC=+0.464 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3288 (IC base=+0.433)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.435 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.433)

- **PATRÓN** `edge` > `0.2005` → IC=+0.477 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2005 (IC base=+0.463)

- **PATRÓN** `sigma_h` < `0.0156` → IC=+0.477 (n=131)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0156 (IC base=+0.463)

- **PATRÓN** `T_h` > `1.1968` → IC=+0.477 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.1968 (IC base=+0.463)

- **PATRÓN** `dist_50` > `0.4421` → IC=+0.485 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4421 (IC base=+0.463)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.472 (n=139)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.463)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=277)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=352)

- **PATRÓN** `streak_estiramiento` < `0.4315` → IC=+0.121 (n=93)

  - _Acción_: Kelly boost +0.61€ cuando `streak_estiramiento` < 0.4315 (IC base=+0.017)

- **PATRÓN** `streak_estiramiento` < `0.5637` → IC=+0.183 (n=156)

  - _Acción_: Kelly boost +0.92€ cuando `streak_estiramiento` < 0.5637 (IC base=+0.041)

- **PATRÓN** `libro_liquidez` > `2526.423` → IC=+0.123 (n=128)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 2526.423 (IC base=+0.041)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=27)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=12)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=27)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.01 (IC base=+0.000)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `streak_estiramiento` > `0.4782` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4782
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=70)

- **PATRÓN** `volumen_racha` < `945898.4` → IC=+0.135 (n=50)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_racha` < 945898.4 (IC base=+0.015)

- **PATRÓN** `streak_estiramiento` < `0.3514` → IC=+0.133 (n=47)

  - _Acción_: Kelly boost +0.66€ cuando `streak_estiramiento` < 0.3514 (IC base=+0.015)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.132 (n=104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 7.0 (IC base=+0.092)

- **PATRÓN** `streak_estiramiento` < `0.3243` → IC=+0.182 (n=64)

  - _Acción_: Kelly boost +0.91€ cuando `streak_estiramiento` < 0.3243 (IC base=+0.092)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.151 (n=107)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 45.0 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `2659.6588` → IC=+0.136 (n=75)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2659.6588 (IC base=+0.092)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.179 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=94)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=100)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=42)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=27)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=820)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=826)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=687)

### STREAK_FADE_60M
- **FILTRO** `hora_utc` < `9.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=16)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=17)

- **FILTRO** `volumen_racha` > `9229.0178` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `volumen_racha` > 9229.0178
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=17)

- **FILTRO** `libro_liquidez` < `2349.4469` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 2349.4469
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=16)

### STREAK_FADE_60M#ETH#60min
- **FILTRO** `hora_utc` > `5.0` → IC=-0.147 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

### STREAK_FADE_60M#SOL#60min
- **PATRÓN** `regimen_ma_toques` > `4.0` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `regimen_ma_toques` > 4.0 (IC base=+0.050)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=899)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1326)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=1035)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=1047)

### STRUCT_NO_15M
- **FILTRO** `libro_liquidez` < `7203.0371` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 7203.0371
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=3701)

### STRUCT_NO_15M#ETH#15min
- **FILTRO** `libro_liquidez` < `7203.0371` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 7203.0371
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=1978)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.204 (n=1019)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.191)

- **PATRÓN** `sigma_h` > `0.011` → IC=+0.228 (n=1019)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.191)

- **PATRÓN** `drift_60min` |x|≤ `0.1659` → IC=+0.199 (n=2689)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.1659 (IC base=+0.191)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2288` → IC=+0.192 (n=1018)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.96€ cuando `delta_ratio_macro` |x|> 0.2288 (IC base=+0.191)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.352` → IC=+0.202 (n=2720)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.352 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.196 (n=3056)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.196 (n=2796)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.191)

- **PATRÓN** `ibs_15` > `0.5859` → IC=+0.268 (n=3055)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5859 (IC base=+0.191)

- **PATRÓN** `dist_vwap_pct` > `0.1215` → IC=+0.185 (n=1439)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.1215 (IC base=+0.191)

- **PATRÓN** `dist_vwap_pct` < `0.3009` → IC=+0.178 (n=2310)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.3009 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.579` → IC=+0.269 (n=804)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.579 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `5363.1879` → IC=+0.201 (n=1019)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5363.1879 (IC base=+0.191)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=1201)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.238 (n=361)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.0591` → IC=+0.265 (n=181)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0591 (IC base=+0.217)

- **PATRÓN** `delta_ratio_macro` |x|> `0.255` → IC=+0.264 (n=180)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.255 (IC base=+0.217)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2321` → IC=+0.230 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2321 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.236 (n=544)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.217)

- **PATRÓN** `ibs_15` > `0.7199` → IC=+0.280 (n=540)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7199 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` > `0.1371` → IC=+0.241 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1371 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.196` → IC=+0.295 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.196 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.219 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `16220.2116` → IC=+0.247 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16220.2116 (IC base=+0.217)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `28.391` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 28.391
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=683)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.188 (n=203)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0033 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.066` → IC=+0.153 (n=266)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.066 (IC base=+0.146)

- **PATRÓN** `delta_ratio_macro` |x|> `0.149` → IC=+0.160 (n=404)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio_macro` |x|> 0.149 (IC base=+0.146)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1304` → IC=+0.165 (n=234)

  - _Acción_: Kelly boost +0.83€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1304 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.150 (n=430)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.154 (n=423)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 11.0 (IC base=+0.146)

- **PATRÓN** `ibs_15` > `0.5728` → IC=+0.243 (n=605)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5728 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.1133` → IC=+0.150 (n=384)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.1133 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.266` → IC=+0.148 (n=564)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.266 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.028` → IC=+0.288 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.028 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `3532.4883` → IC=+0.152 (n=541)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3532.4883 (IC base=+0.146)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `19.062` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.062
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=248)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.144 (n=192)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0055 (IC base=+0.111)

- **PATRÓN** `sigma_h` > `0.0096` → IC=+0.156 (n=193)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0096 (IC base=+0.111)

- **PATRÓN** `drift_60min` |x|≤ `0.1404` → IC=+0.155 (n=384)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1404 (IC base=+0.111)

- **PATRÓN** `ibs_15` > `0.9118` → IC=+0.289 (n=192)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9118 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` < `0.194` → IC=+0.125 (n=518)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` < 0.194 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.286` → IC=+0.175 (n=115)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 17.286 (IC base=+0.111)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=320)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.111)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `15.788` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 15.788 (IC base=+0.012)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0232` → IC=+0.283 (n=233)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0232 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.1653` → IC=+0.230 (n=616)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1653 (IC base=+0.222)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1101` → IC=+0.223 (n=467)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1101 (IC base=+0.222)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.327` → IC=+0.248 (n=602)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.327 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.237 (n=645)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.222)

- **PATRÓN** `ibs_15` > `0.5745` → IC=+0.303 (n=699)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5745 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` > `0.1857` → IC=+0.232 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1857 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.758` → IC=+0.272 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.758 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `2928.9931` → IC=+0.277 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2928.9931 (IC base=+0.222)

- **PATRÓN** `ibs_15` < `0.1111` → IC=+0.162 (n=722)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.81€ cuando `ibs_15` < 0.1111 (IC base=+0.065)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.366 (n=386)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.362)

- **PATRÓN** `sigma_h` > `0.0027` → IC=+0.369 (n=579)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0027 (IC base=+0.362)

- **PATRÓN** `drift_15min` |x|≤ `0.4002` → IC=+0.361 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4002 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.152` → IC=+0.386 (n=385)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.152 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1413` → IC=+0.386 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1413 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.375 (n=584)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.788` → IC=+0.395 (n=580)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.788 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.4137` → IC=+0.384 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4137 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.858` → IC=+0.386 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.858 (IC base=+0.362)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.366 (n=702)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `3851.736` → IC=+0.371 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3851.736 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.360 (n=270)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.361)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.376 (n=103)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.361)

- **PATRÓN** `drift_15min` |x|≤ `0.5078` → IC=+0.360 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.5078 (IC base=+0.361)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2158` → IC=+0.394 (n=139)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2158 (IC base=+0.361)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1356` → IC=+0.393 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1356 (IC base=+0.361)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.381 (n=309)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.361)

- **PATRÓN** `ibs_15` > `0.8077` → IC=+0.387 (n=307)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8077 (IC base=+0.361)

- **PATRÓN** `dist_vwap_pct` > `0.2515` → IC=+0.394 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2515 (IC base=+0.361)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.997` → IC=+0.382 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.997 (IC base=+0.361)

- **PATRÓN** `libro_liquidez` > `15252.9657` → IC=+0.387 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15252.9657 (IC base=+0.361)

- **PATRÓN** `ballena_activa_n` < `489.0` → IC=+0.409 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 489.0 (IC base=+0.361)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.361 (n=120)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.360)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.369 (n=272)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0033 (IC base=+0.360)

- **PATRÓN** `drift_60min` |x|≤ `0.1074` → IC=+0.359 (n=182)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1074 (IC base=+0.360)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0903` → IC=+0.373 (n=243)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0903 (IC base=+0.360)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2995` → IC=+0.384 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2995 (IC base=+0.360)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.394 (n=130)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.360)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.364 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.360)

- **PATRÓN** `ibs_15` > `0.7504` → IC=+0.405 (n=272)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7504 (IC base=+0.360)

- **PATRÓN** `dist_vwap_pct` > `0.1542` → IC=+0.362 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1542 (IC base=+0.360)

- **PATRÓN** `dist_vwap_pct` < `0.2797` → IC=+0.364 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2797 (IC base=+0.360)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.352` → IC=+0.393 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.352 (IC base=+0.360)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.365 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.360)

- **PATRÓN** `libro_liquidez` > `3882.8993` → IC=+0.381 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3882.8993 (IC base=+0.360)

- **PATRÓN** `ballena_activa_n` < `139.0` → IC=+0.364 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 139.0 (IC base=+0.360)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0121` → IC=-0.222 (n=986)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0121
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=2961)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.207 (n=1531)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=2416)

- **FILTRO** `libro_liquidez` < `4127.9822` → IC=-0.146 (n=2605)

  - _Acción_: SKIP cuando `libro_liquidez` < 4127.9822
  - _Potencial_: sin este filtro IC_bueno=+0.090 (n=1342)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1425` → IC=+0.188 (n=632)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.1425 (IC base=-0.066)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.138` → IC=+0.224 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.138 (IC base=-0.066)

- **PATRÓN** `ibs_15` > `0.6352` → IC=+0.284 (n=948)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6352 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` > `0.1073` → IC=+0.205 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1073 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` < `0.2614` → IC=+0.201 (n=796)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2614 (IC base=-0.066)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1326` → IC=+0.262 (n=2141)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1326 (IC base=-0.012)

- **PATRÓN** `ibs_15` < `0.3529` → IC=+0.282 (n=3209)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3529 (IC base=-0.012)

- **PATRÓN** `dist_vwap_pct` > `0.643` → IC=+0.281 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.643 (IC base=-0.012)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0066` → IC=-0.202 (n=549)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0066
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=1650)

- **FILTRO** `sigma_h` < `0.0033` → IC=-0.230 (n=549)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=1650)

- **FILTRO** `sigma_ewma_delta_pct` > `23.858` → IC=-0.269 (n=318)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.858
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=1881)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.203 (n=62)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=2137)

- **FILTRO** `libro_liquidez` < `16283.0924` → IC=-0.203 (n=1451)

  - _Acción_: SKIP cuando `libro_liquidez` < 16283.0924
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=748)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.171 (n=223)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0026 (IC base=+0.093)

- **PATRÓN** `delta_ratio_macro` |x|> `0.217` → IC=+0.298 (n=132)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.217 (IC base=+0.093)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1042` → IC=+0.281 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1042 (IC base=+0.093)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.135 (n=327)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 15.0 (IC base=+0.093)

- **PATRÓN** `ibs_15` > `0.7566` → IC=+0.336 (n=291)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7566 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` > `0.1047` → IC=+0.301 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1047 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` < `0.3651` → IC=+0.293 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3651 (IC base=+0.093)

- **PATRÓN** `sigma_ewma_delta_pct` > `24.877` → IC=+0.141 (n=154)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 24.877 (IC base=+0.093)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0659` → IC=+0.236 (n=51)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0659 (IC base=-0.193)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1779` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1779 (IC base=-0.193)

- **PATRÓN** `ibs_15` < `0.618` → IC=+0.311 (n=51)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.618 (IC base=-0.193)

- **PATRÓN** `dist_vwap_pct` < `0.0474` → IC=+0.304 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0474 (IC base=-0.193)

- **PATRÓN** `ballena_activa_n` < `295.0` → IC=+0.417 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 295.0 (IC base=-0.193)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.162 (n=616)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.162 (n=418)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0058 (IC base=+0.153)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.163 (n=475)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0033 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.1104` → IC=+0.183 (n=317)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1104 (IC base=+0.153)

- **PATRÓN** `drift_15min` |x|≤ `0.4034` → IC=+0.158 (n=159)

  - _Acción_: Kelly boost +0.79€ cuando `drift_15min` |x|≤ 0.4034 (IC base=+0.153)

- **PATRÓN** `delta_ratio_macro` |x|> `0.141` → IC=+0.158 (n=317)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.79€ cuando `delta_ratio_macro` |x|> 0.141 (IC base=+0.153)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2962` → IC=+0.200 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2962 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.177 (n=336)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 11.0 (IC base=+0.153)

- **PATRÓN** `ibs_15` > `0.6314` → IC=+0.255 (n=475)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6314 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.5931` → IC=+0.156 (n=88)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.5931 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.266` → IC=+0.158 (n=445)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.266 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.52` → IC=+0.260 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.52 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.162 (n=616)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `10755.3155` → IC=+0.171 (n=159)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 10755.3155 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.255 (n=488)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.3488` → IC=+0.245 (n=973)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3488 (IC base=+0.242)

- **PATRÓN** `drift_15min` |x|≤ `0.7516` → IC=+0.254 (n=973)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7516 (IC base=+0.242)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2139` → IC=+0.260 (n=502)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2139 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.244 (n=986)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.242)

- **PATRÓN** `ibs_15` < `0.3683` → IC=+0.273 (n=1106)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3683 (IC base=+0.242)

- **PATRÓN** `dist_vwap_pct` > `0.7711` → IC=+0.286 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7711 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.569` → IC=+0.253 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.569 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.598` → IC=+0.247 (n=1155)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.598 (IC base=+0.242)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1716` → IC=-0.254 (n=307)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1716
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=597)

- **FILTRO** `drift_15min` |x|> `0.8773` → IC=-0.275 (n=225)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8773
  - _Potencial_: sin este filtro IC_bueno=-0.149 (n=679)

- **FILTRO** `sigma_ewma_delta_pct` > `6.572` → IC=-0.195 (n=221)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.572
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=683)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.181 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.181)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.181)

- **PATRÓN** `dist_vwap_pct` < `0.1292` → IC=+0.167 (n=52)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1292 (IC base=-0.181)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.233 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=-0.181)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0646` → IC=+0.244 (n=498)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0646 (IC base=-0.037)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.289 (n=500)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.037)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0195` → IC=-0.249 (n=548)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0195
  - _Potencial_: sin este filtro IC_bueno=-0.154 (n=550)

- **FILTRO** `drift_15min` |x|> `1.2333` → IC=-0.261 (n=274)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2333
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=824)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=1079)

- **FILTRO** `libro_liquidez` < `2982.5179` → IC=-0.213 (n=823)

  - _Acción_: SKIP cuando `libro_liquidez` < 2982.5179
  - _Potencial_: sin este filtro IC_bueno=-0.168 (n=275)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.202)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.202)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1517` → IC=+0.276 (n=351)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1517 (IC base=-0.027)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1114` → IC=+0.302 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1114 (IC base=-0.027)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.295 (n=778)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.027)

- **PATRÓN** `dist_vwap_pct` > `0.7812` → IC=+0.344 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7812 (IC base=-0.027)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `dist_vwap_pct` > `0.1506` → IC=+0.138 (n=56)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.1506 (IC base=+0.036)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `dist_vwap_pct` > `0.1506` → IC=+0.138 (n=56)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.1506 (IC base=+0.036)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.297 (n=845)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.0532` → IC=+0.320 (n=320)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0532 (IC base=+0.291)

- **PATRÓN** `delta_ratio_macro` |x|> `0.248` → IC=+0.298 (n=320)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.248 (IC base=+0.291)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2245` → IC=+0.307 (n=563)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2245 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.307 (n=1003)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.291)

- **PATRÓN** `ibs_15` > `0.838` → IC=+0.323 (n=959)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.838 (IC base=+0.291)

- **PATRÓN** `dist_vwap_pct` > `0.1552` → IC=+0.313 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1552 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.991` → IC=+0.366 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.991 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `12753.6666` → IC=+0.308 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12753.6666 (IC base=+0.291)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.309 (n=229)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.0582` → IC=+0.311 (n=173)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0582 (IC base=+0.286)

- **PATRÓN** `drift_15min` |x|≤ `0.6308` → IC=+0.286 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.6308 (IC base=+0.286)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2616` → IC=+0.311 (n=173)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2616 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.308 (n=519)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.286)

- **PATRÓN** `ibs_15` > `0.8601` → IC=+0.319 (n=463)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8601 (IC base=+0.286)

- **PATRÓN** `dist_vwap_pct` > `0.2552` → IC=+0.327 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2552 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `24.371` → IC=+0.374 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 24.371 (IC base=+0.286)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.286 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `16334.7136` → IC=+0.323 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16334.7136 (IC base=+0.286)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.307 (n=294)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.295)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.295 (n=441)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0033 (IC base=+0.295)

- **PATRÓN** `drift_60min` |x|≤ `0.0504` → IC=+0.319 (n=147)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0504 (IC base=+0.295)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1522` → IC=+0.304 (n=294)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1522 (IC base=+0.295)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3023` → IC=+0.315 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3023 (IC base=+0.295)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.314 (n=427)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.295)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.295 (n=399)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.295)

- **PATRÓN** `ibs_15` > `0.8759` → IC=+0.341 (n=394)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8759 (IC base=+0.295)

- **PATRÓN** `dist_vwap_pct` > `0.6017` → IC=+0.321 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6017 (IC base=+0.295)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.754` → IC=+0.348 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.754 (IC base=+0.295)

### UPDOWN_OU_5M
- **FILTRO** `drift_60min` |x|> `0.1498` → IC=-0.136 (n=160)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1498
  - _Potencial_: sin este filtro IC_bueno=-0.104 (n=162)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1208` → IC=-0.146 (n=80)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1208
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=242)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.172 (n=117)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=354)

- **FILTRO** `ballena_activa_n` > `50.0` → IC=-0.204 (n=52)

  - _Acción_: SKIP cuando `ballena_activa_n` > 50.0
  - _Potencial_: sin este filtro IC_bueno=-0.131 (n=158)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1319` → IC=-0.173 (n=47)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1319
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=142)

- **FILTRO** `drift_60min` |x|> `0.2244` → IC=-0.222 (n=16)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2244
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=33)

- **FILTRO** `drift_15min` |x|> `0.3481` → IC=-0.278 (n=16)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3481
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=33)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1941` → IC=-0.231 (n=24)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1941
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=25)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.3151` → IC=-0.158 (n=36)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.3151
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=19)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.296` → IC=-0.370 (n=21)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.296
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

- **FILTRO** `sigma_h` < `0.0063` → IC=-0.243 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=18)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0905` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0905
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `82.5234` → IC=+0.197 (n=437)

  - _Acción_: Kelly boost +0.99€ cuando `T_h` > 82.5234 (IC base=+0.192)

- **PATRÓN** `ratio` < `0.973` → IC=+0.417 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.192)

- **PATRÓN** `T_h` > `111.9959` → IC=+0.352 (n=1979)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9959 (IC base=+0.336)

- **PATRÓN** `ratio` > `1.0236` → IC=+0.367 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0236 (IC base=+0.336)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `103.3918` → IC=+0.176 (n=180)

  - _Acción_: Kelly boost +0.88€ cuando `T_h` > 103.3918 (IC base=+0.167)

- **PATRÓN** `ratio` < `0.9702` → IC=+0.375 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9702 (IC base=+0.167)

- **PATRÓN** `T_h` > `108.3228` → IC=+0.303 (n=675)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 108.3228 (IC base=+0.290)

- **PATRÓN** `ratio` > `1.0466` → IC=+0.393 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0466 (IC base=+0.290)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `82.5234` → IC=+0.238 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 82.5234 (IC base=+0.228)

- **PATRÓN** `ratio` < `0.985` → IC=+0.428 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.985 (IC base=+0.228)

- **PATRÓN** `T_h` > `111.9836` → IC=+0.350 (n=712)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9836 (IC base=+0.323)

- **PATRÓN** `ratio` > `1.0093` → IC=+0.345 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0093 (IC base=+0.323)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1062` → IC=+0.450 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1062 (IC base=+0.400)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5859 sube el IC de +0.191 a +0.268 en UPDOWN_GBM#15min (n=3055). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7199 sube el IC de +0.217 a +0.280 en UPDOWN_GBM#BTC#15min (n=540). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5728 sube el IC de +0.146 a +0.243 en UPDOWN_GBM#ETH#15min (n=605). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.9118 sube el IC de +0.111 a +0.289 en UPDOWN_GBM#SOL#15min (n=192). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5745 sube el IC de +0.222 a +0.303 en UPDOWN_GBM#XRP#15min (n=699). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1111 sube el IC de +0.065 a +0.162 en UPDOWN_GBM#XRP#15min (n=722). Ya aplicado como kelly_boost=+0.81€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6352 sube el IC de -0.066 a +0.284 en UPDOWN_GBM_15M_TARDIO (n=948). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3529 sube el IC de -0.012 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=3209). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7566 sube el IC de +0.093 a +0.336 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=291). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.618 sube el IC de -0.193 a +0.311 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=51). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6314 sube el IC de +0.153 a +0.255 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=475). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3683 sube el IC de +0.242 a +0.273 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1106). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.181 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.037 a +0.289 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=500). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.202 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.027 a +0.295 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=778). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.838 sube el IC de +0.291 a +0.323 en UPDOWN_GBM_IBS_ALTO (n=959). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8601 sube el IC de +0.286 a +0.319 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=463). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8759 sube el IC de +0.295 a +0.341 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=394). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.362 a +0.395 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=580). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8077 sube el IC de +0.361 a +0.387 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=307). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7504 sube el IC de +0.360 a +0.405 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=272). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1724 | +0.087 | +193.25€ | 0 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1724 | +0.087 | +193.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1350 | +0.091 | +165.40€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1350 | +0.091 | +165.40€ | 0 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 271 | +0.068 | +12.14€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 271 | +0.068 | +12.14€ | 3 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 72 | +0.108 | +16.05€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 72 | +0.108 | +16.05€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 417 | +0.004 | +70.27€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 417 | +0.004 | +70.27€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 301 | +0.002 | +46.93€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 301 | +0.002 | +46.93€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 91 | +0.016 | +17.69€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 91 | +0.016 | +17.69€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 23 | -0.060 | +1.23€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 23 | -0.060 | +1.23€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 36841 | -0.083 | -4714.70€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1947 | +0.005 | -246.48€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 34894 | -0.088 | -4468.23€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4425 | -0.116 | -762.75€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4425 | -0.116 | -762.75€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1947 | +0.005 | -246.48€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1947 | +0.005 | -246.48€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4121 | -0.113 | -845.32€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4121 | -0.113 | -845.32€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 9620 | -0.000 | -880.70€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 9620 | -0.000 | -880.70€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 9582 | -0.109 | -716.34€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 9582 | -0.109 | -716.34€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 7146 | -0.146 | -1263.10€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 7146 | -0.146 | -1263.10€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 30091 | -0.018 | +3577.66€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 7784 | +0.003 | +1738.55€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 22307 | -0.025 | +1839.12€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 30091 | -0.018 | +3577.66€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 7784 | +0.003 | +1738.55€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 22307 | -0.025 | +1839.12€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 129561 | +0.114 | -5432.45€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 17379 | +0.182 | -529.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 560 | -0.032 | -65.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 103719 | +0.104 | -4572.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 7903 | +0.103 | -265.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 17213 | +0.106 | -1094.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 58 | -0.150 | +11.01€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 17140 | +0.107 | -1093.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 25392 | +0.128 | -400.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5037 | +0.192 | -150.39€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 17196 | +0.118 | -146.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3117 | +0.086 | -81.54€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 17263 | +0.097 | -1274.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 68 | -0.114 | -5.90€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 17180 | +0.098 | -1257.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 27533 | +0.124 | -475.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 7234 | +0.176 | -120.28€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 17409 | +0.106 | -300.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2878 | +0.101 | -46.41€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 24930 | +0.114 | -1329.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4922 | +0.191 | -270.52€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 463 | +0.003 | -11.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 17637 | +0.093 | -909.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1908 | +0.134 | -137.56€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 17230 | +0.104 | -858.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 60 | -0.065 | +6.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 17157 | +0.105 | -864.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 20783 | +0.194 | -1329.77€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 20783 | +0.194 | -1329.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 4776 | +0.175 | -438.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 4776 | +0.175 | -438.53€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 2439 | +0.199 | -58.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 2439 | +0.199 | -58.09€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 4716 | +0.179 | -393.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 4716 | +0.179 | -393.27€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 4121 | +0.244 | -142.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 4121 | +0.244 | -142.13€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 4652 | +0.187 | -311.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 4652 | +0.187 | -311.50€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 932 | +0.427 | -31.67€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 932 | +0.427 | -31.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 369 | +0.435 | -5.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 369 | +0.435 | -5.95€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 360 | +0.431 | -8.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 360 | +0.431 | -8.65€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 191 | +0.402 | -14.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 191 | +0.402 | -14.63€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 72292 | +0.200 | -5290.46€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 72292 | +0.200 | -5290.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 12423 | +0.185 | -1288.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 12423 | +0.185 | -1288.93€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 11645 | +0.224 | -401.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 11645 | +0.224 | -401.96€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 12409 | +0.178 | -1359.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 12409 | +0.178 | -1359.65€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 11726 | +0.221 | -433.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 11726 | +0.221 | -433.75€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 11990 | +0.201 | -808.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 11990 | +0.201 | -808.91€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 12099 | +0.195 | -997.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 12099 | +0.195 | -997.26€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 27622 | +0.117 | +218.35€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 27622 | +0.117 | +218.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 13725 | +0.121 | +187.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 13725 | +0.121 | +187.59€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 13897 | +0.114 | +30.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 13897 | +0.114 | +30.76€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1887 | +0.293 | +2.01€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1887 | +0.293 | +2.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 856 | +0.284 | -8.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 856 | +0.284 | -8.54€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 912 | +0.293 | +5.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 912 | +0.293 | +5.24€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 119 | +0.351 | +5.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 119 | +0.351 | +5.31€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 869 | +0.441 | +4.39€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 869 | +0.441 | +4.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 420 | +0.438 | -1.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 420 | +0.438 | -1.33€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 403 | +0.446 | +5.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 403 | +0.446 | +5.16€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1468 | +0.071 | -59.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 550 | +0.062 | -37.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 918 | +0.077 | -22.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 69 | +0.106 | +2.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 69 | +0.106 | +2.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1137 | +0.078 | -26.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 219 | +0.079 | -4.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 918 | +0.077 | -22.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 262 | +0.034 | -35.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 262 | +0.034 | -35.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 53750 | +0.100 | -1358.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 4353 | +0.094 | +72.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 49397 | +0.101 | -1430.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 29690 | +0.105 | -307.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 4353 | +0.094 | +72.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 25337 | +0.107 | -379.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 10857 | +0.109 | -44.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 10857 | +0.109 | -44.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 13203 | +0.081 | -1006.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 13203 | +0.081 | -1006.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 883 | +0.197 | -111.73€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 883 | +0.197 | -111.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 883 | +0.197 | -111.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 883 | +0.197 | -111.73€ | 2 | 4 |
| ✅ GBM_LATE_15M | 37159 | +0.091 | +18901.39€ | 0 | 15 |
| ✅ GBM_LATE_15M#15min | 37159 | +0.091 | +18901.39€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 6238 | +0.208 | +4930.57€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 6238 | +0.208 | +4930.57€ | 0 | 22 |
| ✅ GBM_LATE_15M#BTC | 5522 | +0.180 | +4102.75€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 5522 | +0.180 | +4102.75€ | 0 | 23 |
| ✅ GBM_LATE_15M#DOGE | 6628 | +0.203 | +5087.32€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 6628 | +0.203 | +5087.32€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 5216 | +0.039 | +1383.17€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 5216 | +0.039 | +1383.17€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 5306 | -0.030 | +1173.20€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 5306 | -0.030 | +1173.20€ | 4 | 12 |
| ✅ GBM_LATE_15M#XRP | 8249 | -0.035 | +2224.38€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 8249 | -0.035 | +2224.38€ | 3 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 40194 | +0.086 | +21605.09€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 40194 | +0.086 | +21605.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 7752 | +0.007 | +4041.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 7752 | +0.007 | +4041.19€ | 3 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 8446 | +0.013 | +1876.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 8446 | +0.013 | +1876.05€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 5627 | +0.272 | +5909.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 5627 | +0.272 | +5909.56€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 7026 | +0.013 | +1642.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 7026 | +0.013 | +1642.71€ | 1 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 6489 | +0.037 | +2614.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 6489 | +0.037 | +2614.31€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 4854 | +0.294 | +5521.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 4854 | +0.294 | +5521.26€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 29551 | +0.177 | +23439.25€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 29551 | +0.177 | +23439.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 4489 | +0.220 | +3821.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 4489 | +0.220 | +3821.64€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 4638 | +0.151 | +3412.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 4638 | +0.151 | +3412.38€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 4715 | +0.219 | +3974.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 4715 | +0.219 | +3974.04€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 4977 | +0.140 | +3759.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 4977 | +0.140 | +3759.51€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 5559 | +0.123 | +4055.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 5559 | +0.123 | +4055.09€ | 0 | 28 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 5173 | +0.220 | +4416.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 5173 | +0.220 | +4416.59€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 7954 | +0.137 | +3845.83€ | 0 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 7954 | +0.137 | +3845.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 361 | +0.142 | +209.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 361 | +0.142 | +209.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2414 | +0.148 | +1365.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2414 | +0.148 | +1365.40€ | 0 | 24 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 413 | +0.146 | +201.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 413 | +0.146 | +201.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2415 | +0.147 | +1173.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2415 | +0.147 | +1173.50€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1812 | +0.107 | +655.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1812 | +0.107 | +655.27€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 539 | +0.134 | +240.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 539 | +0.134 | +240.28€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO | 37360 | +0.183 | +29321.13€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 37360 | +0.183 | +29321.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 5944 | +0.234 | +5364.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 5944 | +0.234 | +5364.99€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 5770 | +0.149 | +3861.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 5770 | +0.149 | +3861.05€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 6295 | +0.230 | +5560.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 6295 | +0.230 | +5560.01€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 6113 | +0.139 | +4341.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 6113 | +0.139 | +4341.41€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 6620 | +0.122 | +4522.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 6620 | +0.122 | +4522.15€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 6618 | +0.223 | +5671.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 6618 | +0.223 | +5671.52€ | 0 | 20 |
| ✅ GBM_LATE_5M | 10393 | +0.191 | +7623.46€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 10393 | +0.191 | +7623.46€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 919 | +0.232 | +813.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 919 | +0.232 | +813.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2272 | +0.183 | +1749.54€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2272 | +0.183 | +1749.54€ | 0 | 28 |
| ✅ GBM_LATE_5M#DOGE | 1002 | +0.176 | +657.98€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1002 | +0.176 | +657.98€ | 0 | 20 |
| ✅ GBM_LATE_5M#ETH | 3163 | +0.191 | +2219.13€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3163 | +0.191 | +2219.13€ | 0 | 24 |
| ✅ GBM_LATE_5M#SOL | 1436 | +0.180 | +1031.49€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1436 | +0.180 | +1031.49€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1601 | +0.194 | +1151.32€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1601 | +0.194 | +1151.32€ | 0 | 0 |
| ✅ GBM_LATE_60M | 2906 | +0.068 | +1001.74€ | 0 | 10 |
| ✅ GBM_LATE_60M#60min | 2906 | +0.068 | +1001.74€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1087 | +0.088 | +398.86€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1087 | +0.088 | +398.86€ | 0 | 12 |
| ✅ GBM_LATE_60M#ETH | 923 | +0.070 | +359.24€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 923 | +0.070 | +359.24€ | 0 | 11 |
| ✅ GBM_LATE_60M#SOL | 896 | +0.043 | +243.64€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 896 | +0.043 | +243.64€ | 1 | 14 |
| 🚫 GBM_LATE_60M_FADE | 515 | -0.241 | -16.64€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 515 | -0.241 | -16.64€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 195 | -0.231 | -7.88€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 195 | -0.231 | -7.88€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 182 | -0.223 | -1.79€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 182 | -0.223 | -1.79€ | 5 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 138 | -0.271 | -6.96€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 138 | -0.271 | -6.96€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1315 | +0.086 | +338.61€ | 0 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1315 | +0.086 | +338.61€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 505 | +0.084 | +105.46€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 505 | +0.084 | +105.46€ | 1 | 14 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 482 | +0.062 | +81.31€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 482 | +0.062 | +81.31€ | 1 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 328 | +0.124 | +151.85€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 328 | +0.124 | +151.85€ | 2 | 13 |
| ✅ LATE_WINDOW_5MIN | 141 | +0.255 | +122.89€ | 0 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 141 | +0.255 | +122.89€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 141 | +0.255 | +122.89€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 141 | +0.255 | +122.89€ | 0 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 3119 | +0.100 | +776.69€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 3119 | +0.100 | +776.69€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 3119 | +0.100 | +776.69€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 3119 | +0.100 | +776.69€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 451 | -0.065 | -30.21€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 451 | -0.065 | -30.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 129 | -0.019 | +0.68€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 129 | -0.019 | +0.68€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 73 | -0.087 | -8.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 73 | -0.087 | -8.28€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 168 | -0.029 | -5.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 168 | -0.029 | -5.75€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 2 | 0 |
| ✅ LIQUIDACIONES_5M | 3302 | +0.020 | +87.75€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3302 | +0.020 | +87.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 161 | +0.015 | -3.70€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 161 | +0.015 | -3.70€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 595 | +0.033 | +44.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 595 | +0.033 | +44.99€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 203 | -0.017 | -5.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 203 | -0.017 | -5.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1180 | +0.032 | +35.49€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1180 | +0.032 | +35.49€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 744 | +0.011 | +0.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 744 | +0.011 | +0.71€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 419 | +0.006 | +15.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 419 | +0.006 | +15.34€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1557 | -0.040 | -24.52€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1557 | -0.040 | -24.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 440 | -0.034 | -11.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 440 | -0.034 | -11.39€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 523 | -0.014 | +6.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 523 | -0.014 | +6.07€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 594 | -0.067 | -19.19€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 594 | -0.067 | -19.19€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 6368 | -0.023 | +33.67€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 3037 | -0.031 | -37.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 3331 | -0.016 | +70.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 183 | -0.008 | +7.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 90 | +0.043 | +13.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 93 | -0.058 | -6.17€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 1587 | -0.013 | +30.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 761 | -0.018 | +2.97€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 826 | -0.009 | +27.50€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 708 | -0.025 | +5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 361 | -0.040 | -8.77€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 347 | -0.010 | +14.11€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 1316 | -0.037 | -42.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 611 | -0.055 | -47.55€ | 3 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 705 | -0.022 | +5.26€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 1254 | -0.018 | +22.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 604 | -0.025 | +6.79€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 650 | -0.012 | +15.36€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 1320 | -0.027 | +10.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 610 | -0.034 | -3.95€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 710 | -0.021 | +14.67€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 14662 | -0.012 | -218.19€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14662 | -0.012 | -218.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 3379 | -0.021 | -71.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 3379 | -0.021 | -71.38€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 3075 | -0.015 | -29.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 3075 | -0.015 | -29.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 43454 | -0.002 | +2090.89€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 43454 | -0.002 | +2090.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 7777 | +0.025 | +1013.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 7777 | +0.025 | +1013.10€ | 2 | 3 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 6371 | -0.034 | -120.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 6371 | -0.034 | -120.49€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 7894 | +0.022 | +772.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 7894 | +0.022 | +772.23€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 6201 | -0.049 | -163.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 6201 | -0.049 | -163.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 7334 | -0.005 | +245.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 7334 | -0.005 | +245.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 7877 | +0.014 | +344.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 7877 | +0.014 | +344.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6370 | -0.060 | -157.87€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6370 | -0.060 | -157.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1222 | +0.000 | -14.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1222 | +0.000 | -14.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1619 | -0.079 | -39.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1619 | -0.079 | -39.99€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 53 | -0.064 | -2.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 53 | -0.064 | -2.93€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 745 | -0.121 | -32.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 745 | -0.121 | -32.73€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1875 | -0.080 | -42.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1875 | -0.080 | -42.40€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 856 | -0.015 | -25.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 856 | -0.015 | -25.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M | 3360 | +0.004 | -2.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3360 | +0.004 | -2.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 129 | -0.042 | -1.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 129 | -0.042 | -1.78€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 192 | +0.015 | +1.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 192 | +0.015 | +1.02€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 138 | +0.000 | -1.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 138 | +0.000 | -1.83€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1322 | +0.005 | +5.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1322 | +0.005 | +5.17€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1390 | +0.007 | +0.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1390 | +0.007 | +0.32€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 189 | -0.008 | -5.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 189 | -0.008 | -5.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 108517 | -0.074 | +1727.37€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 108517 | -0.074 | +1727.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 18762 | -0.074 | +990.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 18762 | -0.074 | +990.56€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 16404 | -0.099 | -897.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 16404 | -0.099 | -897.58€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 19035 | -0.066 | +1092.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 19035 | -0.066 | +1092.31€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 15943 | -0.095 | -479.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 15943 | -0.095 | -479.02€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 19555 | -0.054 | +377.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 19555 | -0.054 | +377.10€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 18818 | -0.066 | +644.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 18818 | -0.066 | +644.00€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8571 | -0.033 | -175.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8571 | -0.033 | -175.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1960 | -0.045 | -21.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1960 | -0.045 | -21.69€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2566 | -0.026 | -42.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2566 | -0.026 | -42.78€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1143 | -0.049 | -23.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1143 | -0.049 | -23.05€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 898 | -0.032 | -35.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 898 | -0.032 | -35.07€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1504 | +0.121 | +596.19€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#5min | 1368 | +0.127 | +583.60€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 322 | +0.148 | +175.84€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 322 | +0.148 | +175.84€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 270 | +0.110 | +83.77€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 270 | +0.110 | +83.77€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#ETH | 274 | +0.127 | +122.07€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 274 | +0.127 | +122.07€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 243 | +0.149 | +130.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 243 | +0.149 | +130.57€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 259 | +0.094 | +71.35€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 259 | +0.094 | +71.35€ | 0 | 3 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1173 | -0.020 | -25.51€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1173 | -0.020 | -25.51€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 227 | -0.015 | +0.27€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 227 | -0.015 | +0.27€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 197 | -0.007 | +3.72€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 197 | -0.007 | +3.72€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 301 | -0.038 | -19.76€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 301 | -0.038 | -19.76€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 246 | -0.004 | -2.72€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 246 | -0.004 | -2.72€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 202 | -0.029 | -7.00€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 202 | -0.029 | -7.00€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 835 | -0.071 | -38.83€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 385 | -0.120 | -77.25€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 296 | -0.154 | -67.46€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 89 | -0.005 | -9.80€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 298 | -0.033 | +25.29€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 212 | -0.028 | +25.80€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 86 | -0.045 | -0.50€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 152 | -0.019 | +13.13€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 122 | -0.024 | +8.23€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 30 | +0.000 | +4.90€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 630 | -0.087 | -33.43€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 205 | -0.022 | -5.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1011 | -0.207 | -54.90€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 410 | -0.206 | -37.86€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 354 | -0.211 | -38.14€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 56 | -0.172 | +0.28€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 343 | -0.216 | -29.45€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 297 | -0.226 | -35.14€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 46 | -0.146 | +5.69€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 258 | -0.192 | +12.40€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 239 | -0.189 | +9.26€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 19 | -0.204 | +3.14€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 890 | -0.211 | -64.02€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 121 | -0.175 | +9.11€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 417 | +0.397 | +402.51€ | 0 | 14 |
| ✅ RESOLUTION_SNIPER#BTC | 53 | +0.118 | +46.13€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 53 | +0.118 | +46.13€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 104 | +0.377 | +93.44€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 104 | +0.377 | +93.44€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 260 | +0.458 | +262.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 260 | +0.458 | +262.94€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 417 | +0.397 | +402.51€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 667 | +0.031 | +32.05€ | 2 | 3 |
| ✅ STREAK_FADE_15M#15min | 667 | +0.031 | +32.05€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 296 | +0.024 | +3.43€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 296 | +0.024 | +3.43€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 53 | -0.027 | -5.65€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 53 | -0.027 | -5.65€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 69 | -0.007 | -0.06€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 69 | -0.007 | -0.06€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 249 | +0.062 | +34.32€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 249 | +0.062 | +34.32€ | 1 | 6 |
| ✅ STREAK_FADE_5M | 3365 | -0.021 | -128.53€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3365 | -0.021 | -128.53€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1051 | -0.022 | -37.52€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1051 | -0.022 | -37.52€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 586 | -0.025 | -25.10€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 586 | -0.025 | -25.10€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 161 | -0.040 | -13.85€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 161 | -0.040 | -13.85€ | 3 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1567 | -0.016 | -52.06€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1567 | -0.016 | -52.06€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 94 | -0.052 | -9.37€ | 4 | 0 |
| ✅ STREAK_FADE_60M#60min | 94 | -0.052 | -9.37€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 39 | -0.085 | -3.98€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 39 | -0.085 | -3.98€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 55 | -0.026 | -5.39€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 55 | -0.026 | -5.39€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 10255 | +0.018 | +102.36€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 10255 | +0.018 | +102.36€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2648 | +0.021 | +27.27€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2648 | +0.021 | +27.27€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2601 | +0.022 | +41.96€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2601 | +0.022 | +41.96€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2882 | +0.009 | -2.09€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2882 | +0.009 | -2.09€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2124 | +0.023 | +35.22€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2124 | +0.023 | +35.22€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 9335 | +0.014 | -42.49€ | 1 | 0 |
| ✅ STRUCT_NO_15M#15min | 9335 | +0.014 | -42.49€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3720 | +0.019 | -1.57€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3720 | +0.019 | -1.57€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3603 | +0.011 | -28.25€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3603 | +0.011 | -28.25€ | 1 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2012 | +0.009 | -12.68€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2012 | +0.009 | -12.68€ | 1 | 0 |
| ✅ UPDOWN_GBM | 68000 | +0.052 | +5880.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 16934 | +0.085 | +3823.03€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 2239 | +0.006 | +12.93€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 44718 | +0.046 | +1980.33€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 3875 | +0.008 | +64.76€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6818 | +0.089 | +1072.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1543 | +0.158 | +694.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 77 | -0.006 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5198 | +0.070 | +378.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 13660 | +0.054 | +1138.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2101 | +0.091 | +509.32€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 574 | +0.012 | +7.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 9172 | +0.058 | +571.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1728 | +0.006 | +48.16€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 85 | -0.075 | +2.33€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 8043 | +0.066 | +843.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1529 | +0.149 | +607.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 78 | +0.013 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 6436 | +0.047 | +237.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 15023 | +0.042 | +919.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 3901 | +0.062 | +545.63€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 568 | +0.009 | +9.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 9154 | +0.041 | +350.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1322 | +0.011 | +11.22€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 78 | -0.100 | +2.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 14937 | +0.028 | +624.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 4064 | +0.035 | +335.61€ | 0 | 7 |
| ✅ UPDOWN_GBM#SOL#240min | 554 | -0.004 | -1.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 9425 | +0.031 | +288.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 825 | +0.007 | +5.38€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 69 | -0.134 | -4.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 9517 | +0.062 | +1284.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 3796 | +0.103 | +1130.42€ | 0 | 10 |
| ✅ UPDOWN_GBM#XRP#240min | 388 | +0.010 | -0.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 5333 | +0.035 | +153.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 232 | -0.103 | +0.99€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 771 | +0.362 | +273.22€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 771 | +0.362 | +273.22€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 409 | +0.361 | +139.61€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 409 | +0.361 | +139.61€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 362 | +0.360 | +133.60€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 362 | +0.360 | +133.60€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 18132 | -0.024 | +4393.94€ | 3 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 18132 | -0.024 | +4393.94€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1674 | -0.056 | +500.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1674 | -0.056 | +500.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 3090 | -0.111 | +130.99€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 3090 | -0.111 | +130.99€ | 5 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 926 | +0.220 | +767.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 926 | +0.220 | +767.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2107 | +0.215 | +1353.42€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2107 | +0.215 | +1353.42€ | 1 | 22 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 5151 | -0.063 | +704.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 5151 | -0.063 | +704.82€ | 3 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5184 | -0.064 | +936.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5184 | -0.064 | +936.25€ | 4 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 201 | +0.037 | +7.46€ | 0 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 201 | +0.037 | +7.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 201 | +0.037 | +7.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 201 | +0.037 | +7.46€ | 0 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1278 | +0.291 | +1068.05€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1278 | +0.291 | +1068.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 691 | +0.286 | +542.54€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 691 | +0.286 | +542.54€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 587 | +0.295 | +525.51€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 587 | +0.295 | +525.51€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 793 | -0.111 | -82.06€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 793 | -0.111 | -82.06€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 238 | -0.083 | -17.95€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 238 | -0.083 | -17.95€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 84 | -0.151 | -7.62€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 84 | -0.151 | -7.62€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 88 | -0.189 | -7.13€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 88 | -0.189 | -7.13€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 3287 | +0.303 | +1584.37€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1194 | +0.256 | +160.29€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1262 | +0.297 | +560.00€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 831 | +0.379 | +864.08€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.045) — sin ventaja clara. oversold(IBS<0.3): IC=+0.062 n=23713 | neutral: IC=+0.054 n=25035 | overbought(IBS>0.7): IC=+0.099 n=24116
  - _Datos_: n=75725 IC=+0.072 PNL=+11149.33€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 673 celda(s) pasan gate riguroso completo de 2589 evaluadas (n>=40) y 3580 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.035 < 0.08 — monitorear
  - _Datos_: n=4064 IC=+0.035 PNL=+335.61€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1262/15 IC=+0.297 PNL=+560.00€ | BTC: n=1194/15 IC=+0.256 PNL=+160.29€ | SOL: n=831/15 IC=+0.379 PNL=+864.08€

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
  - _Estado_: 67938 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.140 n=712/60 | contraria IC=+0.202 n=744 | gap=-0.062 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=415, boost estimado=+0.009. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 243 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1322/40 IC=+0.011 PNL=+11.22€ | BTC#60min: n=1728/40 IC=+0.006 PNL=+48.16€ | SOL#60min: n=825/40 IC=+0.007 PNL=+5.38€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.048 n=492649 | tras_1loss IC=+0.092 n=376025 | tras_2loss IC=+0.062 n=153287/40 | gap=-0.014 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.033 n=9080 | contrario_BTC IC=+0.048 n=7962/40 | gap=+0.015 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.216 > 0.08 con n=622 PNL=+498.63€
  - _Datos_: n=622 IC=+0.216 PNL=+498.63€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.187 > 0.08 con n=713 PNL=+455.32€
  - _Datos_: n=713 IC=+0.187 PNL=+455.32€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.189 > 0.08 con n=59 PNL=+35.04€
  - _Datos_: n=59 IC=+0.189 PNL=+35.04€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.332 > 0.1 con n=2681 PNL=+1495.23€
  - _Datos_: n=2681 IC=+0.332 PNL=+1495.23€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=568 IC=+0.075 PNL=+66.51€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=568 IC=+0.075 PNL=+66.51€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=74 IC=+0.171 PNL=+45.37€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=74 IC=+0.171 PNL=+45.37€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=64069 IC=+0.051 PNL=+5592.95€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=64069 IC=+0.051 PNL=+5592.95€

**⏳ H-CUSTOM-OF-02H-BTCSOL** — ORDER_FLOW H=02h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 02h está en el blacklist basado en TODOS los pares. Con BTC+SOL solo, el historial muestra 4/5 (80%) IC=+0.054. ¿Se confirma la señal positiva con más datos?
  - _Umbral_: 15
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 02h del blacklist ORDER_FLOW
  - _Estado_: 5/15 ops en el filtro definido (IC actual=+0.054 PNL=+5.10€)
  - _Datos_: n=5 IC=+0.054 PNL=+5.10€

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
  - _Estado_: n=2620 IC=+0.009 PNL=+7.82€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2620 IC=+0.009 PNL=+7.82€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1255 IC=+0.007 PNL=+56.94€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1255 IC=+0.007 PNL=+56.94€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=848 IC=+0.014 PNL=+32.68€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=848 IC=+0.014 PNL=+32.68€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.191 > 0.1 con n=4073 PNL=+2728.05€
  - _Datos_: n=4073 IC=+0.191 PNL=+2728.05€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=2883 IC=+0.069 PNL=+218.64€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2883 IC=+0.069 PNL=+218.64€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=2101 IC=+0.091 PNL=+509.32€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=2101 IC=+0.091 PNL=+509.32€

**⏳ H-CUSTOM-DRIFT15-ZONA-MUERTA** — GBM#15min drift_15min ∈ [-0.3,+0.3] — zona muerta de señal
  - _Hipótesis_: Análisis n=127 GBM#15min: cuando drift_15min está entre -0.3 y +0.3 (mercado sin dirección clara) el IC es negativo (-0.043). Cuando drift>0.3 IC=+0.100 (n=28). Cuando drift<-1 IC=+0.048 (reversión). La señal requiere mercado con dirección clara.
  - _Umbral_: 50
  - _Acción_: Filtrar señales GBM#15min cuando drift_15min ∈ [-0.3, +0.3] — validar con n≥50 antes de implementar
  - _Estado_: 0/50 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: confirmada 2026-07-01 (IC=-0.037 n=52) e implementada en shadow_predict.py (skip si drift_15min∈[-0.3,0.3)) -- verificado 26-Ago con 2177 filas post-TWAP reales, 0 caen en la zona filtrada. Frozen by design, no falta n

**🟡 H-CUSTOM-DRIFT15-MOMENTUM** — GBM#15min drift_15min > 0.3 — zona de momentum (señal fuerte)
  - _Hipótesis_: Cuando drift_15min > 0.3%/h el GBM captura bien la dirección: IC=+0.100 n=28 en todos GBM#15min; IC=+0.152 n=13 solo BTC. El mercado tiene dirección clara y el GBM la sigue. Hipótesis: este rango es donde la señal es real.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma IC>0.10 con n≥40 → boost ×1.2 en GBM#15min cuando drift_15min>0.3
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.102 > 0.08 con n=9668 PNL=+2853.08€
  - _Datos_: n=9668 IC=+0.102 PNL=+2853.08€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=242 IC=-0.254 PNL=-10.72€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=242 IC=-0.254 PNL=-10.72€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=363 IC=-0.023 PNL=-7.06€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=363 IC=-0.023 PNL=-7.06€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=873 IC=+0.041 PNL=+87.65€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=873 IC=+0.041 PNL=+87.65€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=99 IC=+0.035 PNL=+3.55€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=99 IC=+0.035 PNL=+3.55€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=7683 IC=+0.017 PNL=+162.13€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=7683 IC=+0.017 PNL=+162.13€

**🟡 H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.113 > 0.08 con n=334 PNL=+71.63€
  - _Datos_: n=334 IC=+0.113 PNL=+71.63€

**🔶 H-LATE-WINDOW-5MIN** — Late-window BTC 5min — arbitraje timing vs Polymarket
  - _Hipótesis_: Inspirado en VyvanseWithMarijuana (36.5% ROI, $42k vol). A T+160-270s dentro de una ventana BTC 5min, si BTC ya se movió >0.3%, Polymarket no ha actualizado precio → edge estructural. Estrategia LATE_WINDOW_5MIN en shadow hasta n≥30. FIX 2026-07-02: la estrategia llevaba 0 predicciones desde su creacion porque HORIZONTE_MIN_HORAS=0.05 (3min) descartaba todo mercado a <3min de expirar — y su zona de entrada (160-270s de una ventana de 5min) deja 30-140s restantes, siempre bajo el suelo. Corregido en shadow_predict (zona late-window marcada _solo_late, 30s-3min, solo evaluada por esta estrategia). El reloj de acumulacion empieza de verdad hoy. Contexto extra: el estudio de ballenas de hoy confirma que comprar el lado ganador a mitad/final de ventana es el playbook comun de los 3 mayores ganadores verificados de estos mercados (Bonereaper +$19.9k/mes, wowitsamazing +$10k/mes, zhangfan151 +$8.7k/mes).
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si IC≥0.08 con n≥30 → proponer pasar a live con stake mínimo (0.50€). Si IC<0 con n≥30 → el lag de Polymarket en BTC es insuficiente.
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.255 n=141) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=141 IC=+0.255 PNL=+122.89€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=11334 IC=+0.052 PNL=+995.11€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=11334 IC=+0.052 PNL=+995.11€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=3955 IC=+0.068 PNL=+579.19€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3955 IC=+0.068 PNL=+579.19€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.107 > 0.08 con n=487 PNL=+150.03€
  - _Datos_: n=487 IC=+0.107 PNL=+150.03€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.157 > 0.08 con n=979 PNL=+276.30€
  - _Datos_: n=979 IC=+0.157 PNL=+276.30€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.111 > 0.08 con n=757 PNL=+393.18€
  - _Datos_: n=757 IC=+0.111 PNL=+393.18€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=64364 IC=+0.118 PNL=+23936.47€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=64364 IC=+0.118 PNL=+23936.47€

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
  - _Estado_: n=10175 IC=+0.056 PNL=+1015.67€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=10175 IC=+0.056 PNL=+1015.67€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.128 > 0.02 con n=869 PNL=+370.41€
  - _Datos_: n=869 IC=+0.128 PNL=+370.41€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=202 IC=-0.083 PNL=+23.24€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=202 IC=-0.083 PNL=+23.24€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.448 > 0.1 con n=1503 PNL=+1464.36€
  - _Datos_: n=1503 IC=+0.448 PNL=+1464.36€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=26125 IC=+0.074 PNL=+3826.37€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=26125 IC=+0.074 PNL=+3826.37€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.214 > 0.1 con n=6090 PNL=+3713.50€
  - _Datos_: n=6090 IC=+0.214 PNL=+3713.50€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.133 < -0.1 con n=399 PNL=+52.78€
  - _Datos_: n=399 IC=-0.133 PNL=+52.78€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=2864 IC=+0.065 PNL=+347.74€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2864 IC=+0.065 PNL=+347.74€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=126 IC=-0.109 PNL=+3.80€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=126 IC=-0.109 PNL=+3.80€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.116 > 0.1 con n=683 PNL=+177.59€
  - _Datos_: n=683 IC=+0.116 PNL=+177.59€

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
  - _Estado_: n=27589 IC=-0.136 PNL=+2013.02€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=27589 IC=-0.136 PNL=+2013.02€

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
  - _Estado_: n=2766 IC=+0.139 PNL=+1675.66€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=2766 IC=+0.139 PNL=+1675.66€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.209 > 0.08 con n=3700 PNL=+2735.65€
  - _Datos_: n=3700 IC=+0.209 PNL=+2735.65€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=6993 IC=+0.046 PNL=+531.74€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6993 IC=+0.046 PNL=+531.74€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.090 > 0.08 con n=3034 PNL=+1607.17€
  - _Datos_: n=3034 IC=+0.090 PNL=+1607.17€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.217 > 0.08 con n=718 PNL=+410.61€
  - _Datos_: n=718 IC=+0.217 PNL=+410.61€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.224 < -0.1 con n=2830 PNL=-213.99€
  - _Datos_: n=2830 IC=-0.224 PNL=-213.99€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=7619 IC=+0.195 PNL=+5612.84€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=7619 IC=+0.195 PNL=+5612.84€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.116 > 0.08 con n=110 PNL=+46.21€
  - _Datos_: n=110 IC=+0.116 PNL=+46.21€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=2806 IC=+0.080 PNL=+936.58€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2806 IC=+0.080 PNL=+936.58€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.179 > 0.08 con n=2566 PNL=+1873.79€
  - _Datos_: n=2566 IC=+0.179 PNL=+1873.79€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=4334 IC=-0.029 PNL=+1167.31€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4334 IC=-0.029 PNL=+1167.31€

**〰️ H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: n=638 IC=+0.073 PNL=-59.94€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=638 IC=+0.073 PNL=-59.94€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.239 > 0.08 con n=4336 PNL=-364.94€
  - _Datos_: n=4336 IC=+0.239 PNL=-364.94€

**〰️ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: n>=40 y IC>0.08
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: n=59 IC=-0.008 PNL=+5.77€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=59 IC=-0.008 PNL=+5.77€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.098 n=1586) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1586 IC=+0.098 PNL=+340.28€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.323 > 0.08 con n=399 PNL=+124.93€
  - _Datos_: n=399 IC=+0.323 PNL=+124.93€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.412 n=534) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=534 IC=+0.412 PNL=+766.29€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=12423 IC=+0.185 PNL=-1288.93€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=12423 IC=+0.185 PNL=-1288.93€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.210 > 0.1 con n=205 PNL=+128.93€
  - _Datos_: n=205 IC=+0.210 PNL=+128.93€
