# Hipótesis automáticas — 2026-10-12 15:02 UTC
_Generado por shadow_postmortem.py sobre 866824 resoluciones (PNL=+109532.30€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **PATRÓN** `py_entrada` > `0.505` → IC=+0.214 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.127)

- **PATRÓN** `n_total_lado` > `68.0` → IC=+0.194 (n=246)

  - _Acción_: Kelly boost +0.97€ cuando `n_total_lado` > 68.0 (IC base=+0.127)

- **PATRÓN** `banda_hit_calibrado` > `0.6191` → IC=+0.255 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6191 (IC base=+0.127)

- **PATRÓN** `banda_z` > `9.322` → IC=+0.193 (n=242)

  - _Acción_: Kelly boost +0.96€ cuando `banda_z` > 9.322 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=246)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=775)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.127)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.505` → IC=+0.216 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.132)

- **PATRÓN** `n_total_lado` > `73.0` → IC=+0.213 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 73.0 (IC base=+0.132)

- **PATRÓN** `banda_hit_calibrado` > `0.6158` → IC=+0.244 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6158 (IC base=+0.132)

- **PATRÓN** `banda_z` > `9.759` → IC=+0.221 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.759 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=623)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=677)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.132)

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
- **FILTRO** `restante_s_al_confirmar` < `144.01` → IC=-0.205 (n=9194)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 144.01
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=27589)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `130.91` → IC=-0.265 (n=1106)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.91
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3319)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `122.47` → IC=-0.300 (n=1030)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 122.47
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=3091)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `166.33` → IC=-0.220 (n=2390)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 166.33
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=7173)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `131.73` → IC=-0.295 (n=1782)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 131.73
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=5348)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.208 (n=19398)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=4084)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `9416.0594` → IC=+0.180 (n=1827)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 9416.0594 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.132 (n=16201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.134 (n=19738)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.228 (n=15070)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.157 (n=6759)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7382.8769` → IC=+0.162 (n=2601)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 7382.8769 (IC base=+0.126)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=1954)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.197 (n=1912)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 17.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.348 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.198 (n=2401)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `16158.8276` → IC=+0.208 (n=622)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16158.8276 (IC base=+0.196)

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
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.170 (n=431)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.61 (IC base=+0.087)

- **PATRÓN** `libro_liquidez` > `6926.0677` → IC=+0.167 (n=118)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 6926.0677 (IC base=+0.087)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.137 (n=1023)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.44 (IC base=+0.086)

- **PATRÓN** `libro_liquidez` > `5815.7893` → IC=+0.127 (n=239)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 5815.7893 (IC base=+0.086)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=3784)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.365 (n=1234)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.226 (n=1678)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.217)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.361 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.223 (n=1953)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.217)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.148 (n=940)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.146 (n=806)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 15.0 (IC base=+0.142)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.260 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=732)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `1510.5581` → IC=+0.150 (n=803)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1510.5581 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `4420.281` → IC=+0.165 (n=150)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 4420.281 (IC base=+0.071)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.240 (n=891)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.408 (n=1078)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.148 (n=1258)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 7.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.157 (n=665)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.146)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.289 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=833)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.146)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.154 (n=400)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.229 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.124)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.795` → IC=-0.329 (n=68)

  - _Acción_: SKIP cuando `py_entrada` > 0.795
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=137)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=16226)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.200 (n=13788)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.230 (n=6796)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.198)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.179 (n=3573)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 6.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.177 (n=3577)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 17.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.179 (n=3645)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.73 (IC base=+0.175)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.225 (n=1750)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.228 (n=1746)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.313 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.224)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=3718)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.183 (n=3555)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.180 (n=3809)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.73 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.187 (n=2037)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.72 (IC base=+0.180)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.254 (n=3242)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.244)

- **PATRÓN** `py_entrada` > `0.78` → IC=+0.349 (n=1054)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.192 (n=3641)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.192 (n=2332)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.199 (n=1275)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.73 (IC base=+0.188)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=20775)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.245 (n=21264)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.201)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.187 (n=8328)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 8.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.187 (n=6684)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 12.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.200 (n=9294)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.185)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=4331)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.227 (n=4260)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.285 (n=3069)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.182 (n=8788)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 7.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.193 (n=8873)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.178)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.234 (n=4367)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.278 (n=3021)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.205 (n=8031)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.202 (n=7976)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.260 (n=3164)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.202)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.205 (n=3454)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.196 (n=3504)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 6.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.246 (n=3653)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.195)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=7534)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` < `4.2` → IC=+0.124 (n=6902)

  - _Acción_: Kelly boost +0.62€ cuando `restante_min` < 4.2 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.140 (n=7350)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.127 (n=9167)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.43` → IC=+0.139 (n=6897)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 2.43 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=3730)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.121)

- **PATRÓN** `restante_min` < `4.17` → IC=+0.127 (n=3424)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.17 (IC base=+0.121)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.143 (n=3701)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.95 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.135 (n=4543)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.121)

- **PATRÓN** `lag_apertura_s` < `2.9` → IC=+0.146 (n=3424)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 2.9 (IC base=+0.121)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.191 (n=3804)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.135 (n=4026)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.138 (n=3479)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.25 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.305 (n=1499)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.295)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.296 (n=1480)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.295)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.382 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.295)

- **PATRÓN** `libro_liquidez` > `4263.4949` → IC=+0.303 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4263.4949 (IC base=+0.295)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.296 (n=673)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.286)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.356 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `5350.3552` → IC=+0.315 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5350.3552 (IC base=+0.286)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.326 (n=481)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.294)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.298 (n=712)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.294)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.389 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.294)

- **PATRÓN** `libro_liquidez` > `1705.54` → IC=+0.307 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1705.54 (IC base=+0.294)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.447 (n=696)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.443)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.443 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.443)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.445 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.443)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.444 (n=779)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.443)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.446 (n=329)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.441)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.441 (n=319)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.441 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.447 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.441)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.464 (n=109)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.446)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.453 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.446)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.446)

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
- **PATRÓN** `drift_60min` |x|≤ `0.364` → IC=+0.137 (n=10219)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.364 (IC base=+0.116)

- **PATRÓN** `ibs_20min` > `0.9844` → IC=+0.244 (n=3871)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9844 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` < `0.2116` → IC=+0.254 (n=2691)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2116 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.977` → IC=+0.186 (n=4382)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 5.977 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` < `1.2099` → IC=+0.252 (n=3278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2099 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` > `0.6175` → IC=+0.256 (n=3278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6175 (IC base=+0.116)

- **PATRÓN** `volumen_pendiente_norm` > `0.302` → IC=+0.233 (n=1167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.302 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` > `2.3415` → IC=+0.222 (n=3711)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3415 (IC base=+0.116)

- **PATRÓN** `ibs_20min` < `0.5684` → IC=+0.143 (n=14241)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.5684 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.563` → IC=+0.199 (n=962)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.563 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `1.1974` → IC=+0.183 (n=5366)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 1.1974 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.0559` → IC=+0.181 (n=2432)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 1.0559 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2954` → IC=+0.228 (n=1353)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2954 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` > `1.569` → IC=+0.205 (n=8196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.569 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `111.0` → IC=+0.219 (n=9004)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 111.0 (IC base=+0.074)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.215 (n=857)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.187)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.209 (n=856)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.2778` → IC=+0.191 (n=2257)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.2778 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.201 (n=1237)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.190 (n=1719)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 11.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` > `0.9735` → IC=+0.271 (n=1162)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9735 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.154` → IC=+0.288 (n=777)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.154 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.243 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `2.2695` → IC=+0.201 (n=1104)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2695 (IC base=+0.187)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.200 (n=2678)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.187)

- **PATRÓN** `sigma_h` < `0.0079` → IC=+0.235 (n=2107)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0079 (IC base=+0.234)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.243 (n=1881)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.0875` → IC=+0.265 (n=703)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0875 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.253 (n=760)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.3992` → IC=+0.256 (n=1852)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3992 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.922` → IC=+0.234 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.922 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` < `0.0941` → IC=+0.238 (n=1862)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0941 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.287` → IC=+0.248 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.287 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.6473` → IC=+0.252 (n=658)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6473 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=2318)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.236 (n=911)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.175` → IC=+0.249 (n=1376)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.175 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.234 (n=2061)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.222 (n=2108)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` > `0.9697` → IC=+0.267 (n=688)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9697 (IC base=+0.221)

- **PATRÓN** `dist_vwap_pct` > `0.1888` → IC=+0.225 (n=1050)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1888 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.469` → IC=+0.261 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.469 (IC base=+0.221)

- **PATRÓN** `volumen_regimen` < `1.2487` → IC=+0.223 (n=2061)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2487 (IC base=+0.221)

- **PATRÓN** `volumen_regimen` > `0.6213` → IC=+0.226 (n=2063)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6213 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.2787` → IC=+0.249 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2787 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` < `1.5144` → IC=+0.223 (n=893)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5144 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.4423` → IC=+0.245 (n=676)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4423 (IC base=+0.221)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.188 (n=690)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0026 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0741` → IC=+0.173 (n=693)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0741 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.163 (n=782)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.7276` → IC=+0.181 (n=2070)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.7276 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.222` → IC=+0.151 (n=333)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 11.222 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.282` → IC=+0.146 (n=1894)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 4.282 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.199` → IC=+0.149 (n=2069)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.199 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.0974` → IC=+0.164 (n=763)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.0974 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.4604` → IC=+0.149 (n=1953)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.4604 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.4221` → IC=+0.145 (n=1953)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4221 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `225.0` → IC=+0.181 (n=829)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 225.0 (IC base=+0.138)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.211 (n=1194)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.196 (n=2771)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.194 (n=2359)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.268 (n=1015)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.343` → IC=+0.261 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.343 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` < `0.0977` → IC=+0.193 (n=2317)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0977 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.3484` → IC=+0.207 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3484 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `2.1566` → IC=+0.202 (n=1695)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1566 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=3106)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.190)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.226 (n=2048)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.1757` → IC=+0.229 (n=1024)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1757 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.247 (n=867)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.218 (n=1084)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.0698` → IC=+0.236 (n=1024)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0698 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.551` → IC=+0.256 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.551 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.3458` → IC=+0.256 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3458 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` < `1.7259` → IC=+0.216 (n=966)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7259 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.7242` → IC=+0.231 (n=995)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7242 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `2081.1956` → IC=+0.228 (n=776)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2081.1956 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.221 (n=2136)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.217)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.140 (n=137)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=3141)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.146 (n=636)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.004 (IC base=+0.050)

- **PATRÓN** `ibs_20min` > `0.9581` → IC=+0.222 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9581 (IC base=+0.050)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.06` → IC=+0.182 (n=1021)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 5.06 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` < `0.8546` → IC=+0.332 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8546 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` > `1.236` → IC=+0.351 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.236 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` < `0.1787` → IC=+0.325 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1787 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` > `0.2965` → IC=+0.342 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2965 (IC base=+0.050)

- **PATRÓN** `volumen_spike_ratio` < `1.4165` → IC=+0.364 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4165 (IC base=+0.050)

- **PATRÓN** `volumen_spike_ratio` > `2.2083` → IC=+0.325 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2083 (IC base=+0.050)

- **PATRÓN** `ballena_activa_n` < `149.0` → IC=+0.334 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 149.0 (IC base=+0.050)

- **PATRÓN** `ibs_20min` < `0.0987` → IC=+0.172 (n=820)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.0987 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` > `0.4532` → IC=+0.185 (n=268)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.4532 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` < `0.8511` → IC=+0.149 (n=918)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8511 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` > `0.2875` → IC=+0.206 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2875 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` > `1.5154` → IC=+0.159 (n=1176)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.5154 (IC base=+0.032)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.167 (n=85)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=486)

- **FILTRO** `ibs_20min` > `0.2222` → IC=-0.129 (n=3157)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2222
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=1559)

- **FILTRO** `sigma_ewma_delta_pct` > `8.666` → IC=-0.225 (n=485)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.666
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=4231)

- **PATRÓN** `ibs_20min` > `0.8` → IC=+0.182 (n=196)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.8 (IC base=+0.037)

- **PATRÓN** `dist_vwap_pct` > `1.6532` → IC=+0.294 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.6532 (IC base=+0.037)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.362` → IC=+0.157 (n=65)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 9.362 (IC base=+0.037)

- **PATRÓN** `volumen_regimen` > `0.992` → IC=+0.281 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.992 (IC base=+0.037)

- **PATRÓN** `volumen_pendiente_norm` < `0.1539` → IC=+0.266 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1539 (IC base=+0.037)

- **PATRÓN** `volumen_spike_ratio` < `2.1915` → IC=+0.281 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1915 (IC base=+0.037)

- **PATRÓN** `ibs_20min` < `0.2222` → IC=+0.147 (n=1559)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.2222 (IC base=-0.038)

- **PATRÓN** `dist_vwap_pct` > `0.2569` → IC=+0.279 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2569 (IC base=-0.038)

- **PATRÓN** `volumen_regimen` < `0.7096` → IC=+0.281 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7096 (IC base=-0.038)

- **PATRÓN** `volumen_pendiente_norm` > `0.08` → IC=+0.301 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.08 (IC base=-0.038)

- **PATRÓN** `volumen_spike_ratio` < `2.4034` → IC=+0.299 (n=566)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4034 (IC base=-0.038)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6316` → IC=-0.178 (n=827)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6316
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=2483)

- **FILTRO** `ibs_20min` < `0.7174` → IC=-0.153 (n=2184)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7174
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=1126)

- **FILTRO** `ibs_20min` > `0.76` → IC=-0.204 (n=1229)

  - _Acción_: SKIP cuando `ibs_20min` > 0.76
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=3689)

- **PATRÓN** `dist_vwap_pct` > `0.699` → IC=+0.320 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.699 (IC base=-0.073)

- **PATRÓN** `volumen_regimen` < `1.0013` → IC=+0.300 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0013 (IC base=-0.073)

- **PATRÓN** `volumen_regimen` > `0.6377` → IC=+0.308 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6377 (IC base=-0.073)

- **PATRÓN** `volumen_pendiente_norm` < `0.1052` → IC=+0.303 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1052 (IC base=-0.073)

- **PATRÓN** `volumen_spike_ratio` < `2.5237` → IC=+0.301 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5237 (IC base=-0.073)

- **PATRÓN** `volumen_spike_ratio` > `1.8734` → IC=+0.303 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8734 (IC base=-0.073)

- **PATRÓN** `dist_vwap_pct` > `0.7921` → IC=+0.279 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7921 (IC base=-0.009)

- **PATRÓN** `volumen_regimen` > `1.0812` → IC=+0.277 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0812 (IC base=-0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.1041` → IC=+0.282 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1041 (IC base=-0.009)

- **PATRÓN** `volumen_spike_ratio` < `2.1859` → IC=+0.257 (n=1034)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1859 (IC base=-0.009)

- **PATRÓN** `volumen_spike_ratio` > `1.5493` → IC=+0.261 (n=1050)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5493 (IC base=-0.009)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.203 (n=5116)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.097)

- **PATRÓN** `ibs_20min` > `0.4591` → IC=+0.185 (n=13687)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.4591 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.91` → IC=+0.282 (n=1159)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.91 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.655` → IC=+0.155 (n=6877)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 3.655 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` < `1.1749` → IC=+0.251 (n=5618)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1749 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` > `0.6892` → IC=+0.259 (n=5020)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6892 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` > `0.2401` → IC=+0.267 (n=1682)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2401 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` < `1.4633` → IC=+0.248 (n=3008)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4633 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` > `2.6418` → IC=+0.263 (n=3008)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6418 (IC base=+0.097)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.283 (n=8590)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 93.0 (IC base=+0.097)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.160 (n=4922)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0089 (IC base=+0.075)

- **PATRÓN** `ibs_20min` < `0.5396` → IC=+0.159 (n=12978)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.5396 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` < `0.8769` → IC=+0.254 (n=3040)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8769 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.1975` → IC=+0.261 (n=1519)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1975 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2947` → IC=+0.307 (n=942)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2947 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` < `1.5881` → IC=+0.282 (n=2824)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5881 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` > `2.2861` → IC=+0.276 (n=2908)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2861 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `78.0` → IC=+0.286 (n=6316)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 78.0 (IC base=+0.075)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.3718` → IC=-0.158 (n=1399)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3718
  - _Potencial_: sin este filtro IC_bueno=+0.131 (n=2842)

- **FILTRO** `ibs_20min` > `0.7566` → IC=-0.193 (n=872)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7566
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=2620)

- **FILTRO** `sigma_ewma_delta_pct` > `4.568` → IC=-0.189 (n=767)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.568
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=2725)

- **PATRÓN** `ibs_20min` > `0.9122` → IC=+0.286 (n=1061)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9122 (IC base=+0.035)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.205` → IC=+0.205 (n=747)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.205 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` > `0.2301` → IC=+0.293 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2301 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` < `1.4472` → IC=+0.220 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4472 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` > `2.2347` → IC=+0.256 (n=628)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2347 (IC base=+0.035)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.252 (n=952)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.035)

- **PATRÓN** `ibs_20min` < `0.1593` → IC=+0.151 (n=874)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.1593 (IC base=-0.028)

- **PATRÓN** `volumen_pendiente_norm` < `0.0758` → IC=+0.423 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0758 (IC base=-0.028)

- **PATRÓN** `volumen_spike_ratio` < `2.5496` → IC=+0.412 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5496 (IC base=-0.028)

- **PATRÓN** `volumen_spike_ratio` > `1.5457` → IC=+0.405 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5457 (IC base=-0.028)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.417 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=-0.028)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8557` → IC=+0.142 (n=1043)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.8557 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` > `0.1106` → IC=+0.195 (n=785)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1106 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` < `1.1971` → IC=+0.173 (n=1480)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 1.1971 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` > `0.6792` → IC=+0.183 (n=1322)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 0.6792 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` < `0.0751` → IC=+0.174 (n=1365)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` < 0.0751 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.2741` → IC=+0.219 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2741 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` < `1.4247` → IC=+0.199 (n=486)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.4247 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` > `2.4708` → IC=+0.191 (n=486)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.4708 (IC base=+0.024)

- **PATRÓN** `ballena_activa_n` < `222.0` → IC=+0.225 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 222.0 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` < `0.1481` → IC=+0.230 (n=931)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1481 (IC base=+0.002)

- **PATRÓN** `volumen_regimen` > `0.6195` → IC=+0.235 (n=912)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6195 (IC base=+0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.2728` → IC=+0.298 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2728 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` < `1.5537` → IC=+0.230 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5537 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` > `2.1933` → IC=+0.251 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1933 (IC base=+0.002)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.281 (n=2042)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.258)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.262 (n=2288)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.258)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.259 (n=1524)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.258)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=1186)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.27` → IC=+0.289 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.27 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` < `0.1318` → IC=+0.269 (n=2082)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1318 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` > `2.165` → IC=+0.266 (n=1462)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.165 (IC base=+0.258)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.268 (n=2679)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.258)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.305 (n=1930)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.179` → IC=+0.307 (n=851)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.179 (IC base=+0.290)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.323 (n=737)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.290)

- **PATRÓN** `ibs_20min` < `0.3644` → IC=+0.294 (n=1931)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3644 (IC base=+0.290)

- **PATRÓN** `ibs_20min` > `0.1056` → IC=+0.292 (n=1287)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1056 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.697` → IC=+0.306 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.697 (IC base=+0.290)

- **PATRÓN** `volumen_pendiente_norm` < `0.1953` → IC=+0.288 (n=1873)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1953 (IC base=+0.290)

- **PATRÓN** `volumen_pendiente_norm` > `0.339` → IC=+0.305 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.339 (IC base=+0.290)

- **PATRÓN** `volumen_spike_ratio` < `1.5716` → IC=+0.304 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5716 (IC base=+0.290)

- **PATRÓN** `volumen_spike_ratio` > `2.638` → IC=+0.296 (n=831)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.638 (IC base=+0.290)

- **PATRÓN** `libro_liquidez` > `2075.86` → IC=+0.311 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2075.86 (IC base=+0.290)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.292 (n=1602)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.290)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7547` → IC=-0.184 (n=905)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7547
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=2718)

- **PATRÓN** `ibs_20min` > `0.893` → IC=+0.167 (n=845)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.893 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` < `0.2018` → IC=+0.227 (n=965)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2018 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` < `1.0163` → IC=+0.237 (n=1008)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0163 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` > `0.6697` → IC=+0.219 (n=1024)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6697 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.1029` → IC=+0.240 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1029 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` < `1.4012` → IC=+0.260 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4012 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` > `2.4598` → IC=+0.228 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4598 (IC base=+0.028)

- **PATRÓN** `ballena_activa_n` < `109.0` → IC=+0.256 (n=991)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 109.0 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` < `1.0403` → IC=+0.235 (n=678)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0403 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` < `0.103` → IC=+0.240 (n=710)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.103 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2957` → IC=+0.277 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2957 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.8338` → IC=+0.267 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8338 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.4999` → IC=+0.245 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4999 (IC base=-0.001)

- **PATRÓN** `ballena_activa_n` < `129.0` → IC=+0.256 (n=730)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 129.0 (IC base=-0.001)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7632` → IC=-0.199 (n=1621)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7632
  - _Potencial_: sin este filtro IC_bueno=+0.293 (n=1625)

- **FILTRO** `ibs_20min` > `0.6604` → IC=-0.236 (n=806)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6604
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=2421)

- **FILTRO** `sigma_ewma_delta_pct` > `8.589` → IC=-0.228 (n=366)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.589
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=2861)

- **PATRÓN** `ibs_20min` > `0.7632` → IC=+0.293 (n=1625)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7632 (IC base=+0.047)

- **PATRÓN** `dist_vwap_pct` > `0.2093` → IC=+0.328 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2093 (IC base=+0.047)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.636` → IC=+0.167 (n=503)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 9.636 (IC base=+0.047)

- **PATRÓN** `volumen_regimen` < `0.8519` → IC=+0.319 (n=820)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8519 (IC base=+0.047)

- **PATRÓN** `volumen_regimen` > `0.6339` → IC=+0.312 (n=1230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6339 (IC base=+0.047)

- **PATRÓN** `volumen_pendiente_norm` < `0.1601` → IC=+0.308 (n=1272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1601 (IC base=+0.047)

- **PATRÓN** `volumen_pendiente_norm` > `0.2752` → IC=+0.345 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2752 (IC base=+0.047)

- **PATRÓN** `volumen_spike_ratio` < `1.4433` → IC=+0.330 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4433 (IC base=+0.047)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.335 (n=803)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.047)

- **PATRÓN** `ibs_20min` < `0.5556` → IC=+0.137 (n=2132)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.5556 (IC base=+0.027)

- **PATRÓN** `volumen_regimen` < `0.7056` → IC=+0.257 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7056 (IC base=+0.027)

- **PATRÓN** `volumen_pendiente_norm` < `0.0978` → IC=+0.237 (n=952)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0978 (IC base=+0.027)

- **PATRÓN** `volumen_pendiente_norm` > `0.0717` → IC=+0.244 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0717 (IC base=+0.027)

- **PATRÓN** `volumen_spike_ratio` < `2.4236` → IC=+0.252 (n=961)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4236 (IC base=+0.027)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.268 (n=979)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=+0.027)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.338 (n=1576)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.293)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.309 (n=836)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.293)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.325 (n=1765)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.293)

- **PATRÓN** `dist_vwap_pct` > `0.2123` → IC=+0.321 (n=1004)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2123 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.778` → IC=+0.316 (n=865)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.778 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.915` → IC=+0.293 (n=1998)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.915 (IC base=+0.293)

- **PATRÓN** `volumen_regimen` > `0.6244` → IC=+0.304 (n=1764)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6244 (IC base=+0.293)

- **PATRÓN** `volumen_pendiente_norm` > `0.2819` → IC=+0.342 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2819 (IC base=+0.293)

- **PATRÓN** `volumen_spike_ratio` > `1.4314` → IC=+0.306 (n=1688)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4314 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `2994.949` → IC=+0.317 (n=588)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2994.949 (IC base=+0.293)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.328 (n=1492)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.293)

- **PATRÓN** `sigma_h` > `0.015` → IC=+0.327 (n=1249)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.015 (IC base=+0.294)

- **PATRÓN** `drift_60min` |x|≤ `0.1858` → IC=+0.295 (n=824)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1858 (IC base=+0.294)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.300 (n=1262)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.294)

- **PATRÓN** `ibs_20min` < `0.3679` → IC=+0.320 (n=1871)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3679 (IC base=+0.294)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.518` → IC=+0.304 (n=683)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.518 (IC base=+0.294)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.038` → IC=+0.295 (n=2233)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.038 (IC base=+0.294)

- **PATRÓN** `volumen_regimen` > `1.2304` → IC=+0.324 (n=624)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2304 (IC base=+0.294)

- **PATRÓN** `volumen_pendiente_norm` > `0.2327` → IC=+0.342 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2327 (IC base=+0.294)

- **PATRÓN** `volumen_spike_ratio` < `1.4188` → IC=+0.301 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4188 (IC base=+0.294)

- **PATRÓN** `volumen_spike_ratio` > `2.1432` → IC=+0.297 (n=771)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1432 (IC base=+0.294)

- **PATRÓN** `libro_liquidez` > `2664.2915` → IC=+0.303 (n=1247)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2664.2915 (IC base=+0.294)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.186 (n=3768)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0047 (IC base=+0.177)

- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.217 (n=3766)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.344` → IC=+0.187 (n=9934)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.344 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=11773)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` > `0.5629` → IC=+0.230 (n=11289)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5629 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` > `0.1637` → IC=+0.203 (n=4707)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1637 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.362` → IC=+0.254 (n=2251)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.362 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` < `1.1991` → IC=+0.168 (n=7487)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1991 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` > `0.6273` → IC=+0.162 (n=7489)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6273 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.2943` → IC=+0.199 (n=1659)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2943 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `2.6084` → IC=+0.186 (n=3639)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.6084 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `2024.5448` → IC=+0.183 (n=10085)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2024.5448 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.193 (n=10205)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 100.0 (IC base=+0.177)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.188 (n=7231)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0067 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.0792` → IC=+0.225 (n=3608)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0792 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=4029)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` < `0.4942` → IC=+0.235 (n=10825)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4942 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.18` → IC=+0.195 (n=1793)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 10.18 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` < `1.1822` → IC=+0.166 (n=7738)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1822 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.2918` → IC=+0.224 (n=1592)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2918 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `2.6249` → IC=+0.183 (n=3366)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.6249 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `1838.6032` → IC=+0.178 (n=10824)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 1838.6032 (IC base=+0.178)

- **PATRÓN** `ballena_activa_n` < `68.0` → IC=+0.193 (n=8636)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 68.0 (IC base=+0.178)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.234 (n=633)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.204)

- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.222 (n=635)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0085 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.3313` → IC=+0.225 (n=1898)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3313 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.211 (n=2004)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.208 (n=1277)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `0.9202` → IC=+0.286 (n=1265)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9202 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.19` → IC=+0.334 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.19 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.2806` → IC=+0.265 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2806 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `1.5421` → IC=+0.206 (n=1596)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5421 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.215 (n=1998)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.245 (n=1287)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.242)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.252 (n=1307)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.0691` → IC=+0.300 (n=489)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0691 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.244 (n=1316)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.250 (n=722)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.242)

- **PATRÓN** `ibs_20min` < `0.2672` → IC=+0.265 (n=1287)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2672 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.107` → IC=+0.246 (n=1472)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.107 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` < `0.0993` → IC=+0.242 (n=1260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0993 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` > `0.2945` → IC=+0.275 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2945 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` < `1.4252` → IC=+0.257 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4252 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` > `2.6495` → IC=+0.248 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6495 (IC base=+0.242)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.246 (n=1614)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.242)

- **PATRÓN** `libro_liquidez` > `1868.8836` → IC=+0.247 (n=975)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1868.8836 (IC base=+0.242)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.241 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.242)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.220 (n=565)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.16` → IC=+0.186 (n=1129)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.16 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.177 (n=1787)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` > `0.3656` → IC=+0.223 (n=1693)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3656 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.1362` → IC=+0.209 (n=1059)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1362 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.481` → IC=+0.231 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.481 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `0.6892` → IC=+0.167 (n=745)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.6892 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` > `1.0736` → IC=+0.157 (n=768)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 1.0736 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.2827` → IC=+0.188 (n=270)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2827 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `1.4146` → IC=+0.180 (n=552)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.4146 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `2.4993` → IC=+0.159 (n=552)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.4993 (IC base=+0.156)

- **PATRÓN** `ballena_activa_n` < `426.0` → IC=+0.160 (n=1616)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 426.0 (IC base=+0.156)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.167 (n=1780)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0056 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.2295` → IC=+0.176 (n=1565)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2295 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.187 (n=675)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.6038` → IC=+0.205 (n=1779)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6038 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.719` → IC=+0.206 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.719 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.2065` → IC=+0.167 (n=1779)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2065 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` < `0.0951` → IC=+0.148 (n=1491)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.0951 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.1598` → IC=+0.150 (n=547)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.1598 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.4989` → IC=+0.154 (n=1661)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4989 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.7795` → IC=+0.149 (n=1107)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.7795 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `234.0` → IC=+0.172 (n=697)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 234.0 (IC base=+0.147)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.231 (n=864)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.3997` → IC=+0.221 (n=1676)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3997 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.214 (n=1987)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.296 (n=995)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.5` → IC=+0.285 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.5 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.3512` → IC=+0.220 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3512 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` < `1.7699` → IC=+0.213 (n=809)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7699 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `2.6928` → IC=+0.219 (n=833)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6928 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.215 (n=2243)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.208)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.246 (n=1430)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.01 (IC base=+0.232)

- **PATRÓN** `drift_60min` |x|≤ `0.1419` → IC=+0.267 (n=715)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1419 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.280 (n=620)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` < `0.3529` → IC=+0.252 (n=1625)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3529 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.632` → IC=+0.268 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.632 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.3508` → IC=+0.271 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3508 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` < `1.72` → IC=+0.244 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.72 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `2.724` → IC=+0.236 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.724 (IC base=+0.232)

- **PATRÓN** `libro_liquidez` > `2078.82` → IC=+0.248 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2078.82 (IC base=+0.232)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.228 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.232)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.213 (n=800)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.0748` → IC=+0.202 (n=605)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0748 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=1892)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.3204` → IC=+0.209 (n=1815)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3204 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.1362` → IC=+0.190 (n=1140)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1362 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.969` → IC=+0.209 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.969 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.856` → IC=+0.161 (n=1210)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.856 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.1015` → IC=+0.176 (n=748)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1015 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `1.4265` → IC=+0.161 (n=593)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.4265 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `2.5068` → IC=+0.167 (n=593)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.5068 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `5050.7283` → IC=+0.201 (n=1210)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5050.7283 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `146.0` → IC=+0.158 (n=1760)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 146.0 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.157 (n=1909)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.007 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.381` → IC=+0.147 (n=1909)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.381 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=712)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.6818` → IC=+0.189 (n=1909)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.6818 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.871` → IC=+0.153 (n=670)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 6.871 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.856` → IC=+0.164 (n=1273)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.856 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2969` → IC=+0.195 (n=290)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2969 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.8092` → IC=+0.132 (n=1185)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.8092 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `1.4148` → IC=+0.132 (n=1777)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 1.4148 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `4518.0251` → IC=+0.172 (n=1273)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 4518.0251 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `122.0` → IC=+0.129 (n=1520)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 122.0 (IC base=+0.128)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.128 (n=691)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0058 (IC base=+0.126)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.169 (n=937)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0099 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.5595` → IC=+0.127 (n=2066)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.5595 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=2114)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.214 (n=2067)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.1929` → IC=+0.187 (n=1228)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1929 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.686` → IC=+0.265 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.686 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `1.1924` → IC=+0.139 (n=2066)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.1924 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` < `0.1626` → IC=+0.136 (n=2089)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` < 0.1626 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.5464` → IC=+0.137 (n=881)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.5464 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.127 (n=2145)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `2891.4485` → IC=+0.210 (n=937)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2891.4485 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.156 (n=650)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 21.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.138 (n=2098)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0103 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.104` → IC=+0.172 (n=699)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.104 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=2121)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.5909` → IC=+0.218 (n=2100)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5909 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `0.7402` → IC=+0.128 (n=353)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` > 0.7402 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.212` → IC=+0.125 (n=630)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 5.212 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.1789` → IC=+0.132 (n=2095)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.1789 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.1652` → IC=+0.122 (n=2007)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1652 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2749` → IC=+0.151 (n=270)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.2749 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.4537` → IC=+0.137 (n=646)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.4537 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `2.4306` → IC=+0.126 (n=645)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 2.4306 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2750.8782` → IC=+0.191 (n=950)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2750.8782 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.129 (n=1908)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 51.0 (IC base=+0.120)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.238 (n=1711)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.282` → IC=+0.224 (n=1277)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.282 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.219 (n=1989)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.215)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.219 (n=1295)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` > `0.6533` → IC=+0.253 (n=1914)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6533 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` > `0.1881` → IC=+0.218 (n=1268)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1881 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` < `0.268` → IC=+0.216 (n=1408)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.268 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.588` → IC=+0.248 (n=874)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.588 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` < `1.0264` → IC=+0.216 (n=1685)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0264 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` > `0.6192` → IC=+0.222 (n=1914)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6192 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.2335` → IC=+0.265 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2335 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `2.4841` → IC=+0.219 (n=1862)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4841 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `1.8139` → IC=+0.230 (n=1241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8139 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `2666.66` → IC=+0.226 (n=1276)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2666.66 (IC base=+0.215)

- **PATRÓN** `sigma_h` < `0.0121` → IC=+0.233 (n=862)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0121 (IC base=+0.225)

- **PATRÓN** `sigma_h` > `0.0224` → IC=+0.228 (n=887)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0224 (IC base=+0.225)

- **PATRÓN** `drift_60min` |x|≤ `0.0896` → IC=+0.256 (n=654)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0896 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.242 (n=945)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.225 (n=892)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` < `0.4231` → IC=+0.256 (n=1957)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4231 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` > `1.1415` → IC=+0.235 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1415 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.374` → IC=+0.251 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.374 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` > `0.6401` → IC=+0.233 (n=1956)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6401 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.284 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `1.4386` → IC=+0.226 (n=1808)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4386 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `2636.5754` → IC=+0.233 (n=1304)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2636.5754 (IC base=+0.225)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.208 (n=978)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.3302` → IC=+0.182 (n=2580)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.3302 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.203 (n=1454)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.4861` → IC=+0.205 (n=2620)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4861 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.3611` → IC=+0.179 (n=864)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.3611 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.69` → IC=+0.198 (n=1255)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 3.69 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `1.0587` → IC=+0.183 (n=2315)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 1.0587 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` > `0.6955` → IC=+0.174 (n=2350)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 0.6955 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.1018` → IC=+0.184 (n=1057)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1018 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.4361` → IC=+0.188 (n=950)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.4361 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.5215` → IC=+0.173 (n=950)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.5215 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.174 (n=3341)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.02 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `2771.686` → IC=+0.177 (n=2620)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2771.686 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `151.0` → IC=+0.184 (n=2714)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 151.0 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.144 (n=1014)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0036 (IC base=+0.107)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.121 (n=2857)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.107)

- **PATRÓN** `ibs_20min` < `0.0826` → IC=+0.196 (n=1009)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.0826 (IC base=+0.107)

- **PATRÓN** `volumen_spike_ratio` < `1.4323` → IC=+0.137 (n=981)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.4323 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `4449.2251` → IC=+0.133 (n=2017)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 4449.2251 (IC base=+0.107)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.134 (n=1270)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 29.0 (IC base=+0.107)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.207 (n=370)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.160)

- **PATRÓN** `drift_60min` |x|≤ `0.099` → IC=+0.214 (n=369)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.099 (IC base=+0.160)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.191 (n=766)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 8.0 (IC base=+0.160)

- **PATRÓN** `ibs_20min` > `0.6402` → IC=+0.215 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6402 (IC base=+0.160)

- **PATRÓN** `dist_vwap_pct` > `0.2999` → IC=+0.180 (n=264)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.2999 (IC base=+0.160)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.092` → IC=+0.185 (n=360)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 3.092 (IC base=+0.160)

- **PATRÓN** `volumen_regimen` < `0.8753` → IC=+0.189 (n=560)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.8753 (IC base=+0.160)

- **PATRÓN** `volumen_pendiente_norm` > `0.071` → IC=+0.171 (n=329)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.071 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` < `2.2256` → IC=+0.168 (n=723)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 2.2256 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` > `1.417` → IC=+0.162 (n=821)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.417 (IC base=+0.160)

- **PATRÓN** `libro_liquidez` > `14746.216` → IC=+0.170 (n=559)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 14746.216 (IC base=+0.160)

- **PATRÓN** `ballena_activa_n` < `153.0` → IC=+0.200 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 153.0 (IC base=+0.160)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.190 (n=324)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0027 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.2647` → IC=+0.149 (n=853)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.2647 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.147 (n=873)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 7.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.6202` → IC=+0.178 (n=853)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.6202 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.74` → IC=+0.138 (n=186)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 8.74 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.177` → IC=+0.143 (n=880)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 3.177 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.2044` → IC=+0.139 (n=970)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.2044 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `0.7005` → IC=+0.149 (n=866)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.7005 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.07` → IC=+0.177 (n=382)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.07 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.1209` → IC=+0.152 (n=843)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.1209 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=1257)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `359.0` → IC=+0.151 (n=938)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 359.0 (IC base=+0.138)

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

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.127 (n=395)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0037 (IC base=+0.090)

- **PATRÓN** `ibs_20min` < `0.0933` → IC=+0.168 (n=299)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.0933 (IC base=+0.090)

- **PATRÓN** `libro_liquidez` > `3974.0337` → IC=+0.128 (n=801)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 3974.0337 (IC base=+0.090)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.128 (n=382)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 43.0 (IC base=+0.090)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.151 (n=459)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0075 (IC base=+0.145)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.146 (n=312)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` > 0.0091 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.5317` → IC=+0.145 (n=688)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.5317 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.174 (n=617)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 8.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.264 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.932` → IC=+0.200 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.932 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.155` → IC=+0.204 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.155 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.0652` → IC=+0.164 (n=605)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.0652 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` > `0.7264` → IC=+0.156 (n=614)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.7264 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.2809` → IC=+0.173 (n=102)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2809 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.4594` → IC=+0.147 (n=222)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.4594 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `2.2007` → IC=+0.160 (n=301)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.2007 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.151 (n=714)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.02 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `3082.2108` → IC=+0.193 (n=229)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 3082.2108 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.4737` → IC=+0.157 (n=590)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.4737 (IC base=+0.070)

- **PATRÓN** `volumen_spike_ratio` < `1.4564` → IC=+0.143 (n=214)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4564 (IC base=+0.070)

- **PATRÓN** `libro_liquidez` > `2844.564` → IC=+0.157 (n=304)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2844.564 (IC base=+0.070)

- **PATRÓN** `ballena_activa_n` < `32.0` → IC=+0.124 (n=541)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 32.0 (IC base=+0.070)

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
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.180 (n=4903)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0046 (IC base=+0.179)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.219 (n=4897)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=15357)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `0.5593` → IC=+0.237 (n=13121)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5593 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.1597` → IC=+0.188 (n=5367)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1597 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.345` → IC=+0.251 (n=3614)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.345 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `0.8785` → IC=+0.174 (n=6559)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.8785 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.2909` → IC=+0.204 (n=1968)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2909 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `2.6109` → IC=+0.195 (n=4749)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6109 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `2496.9664` → IC=+0.184 (n=9791)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2496.9664 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `76.0` → IC=+0.204 (n=11738)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 76.0 (IC base=+0.179)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.194 (n=5839)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0053 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.1442` → IC=+0.196 (n=5833)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.1442 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=4916)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` < `0.5769` → IC=+0.242 (n=13261)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5769 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.98` → IC=+0.208 (n=1857)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.98 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.673` → IC=+0.190 (n=12790)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 3.673 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` < `1.0605` → IC=+0.161 (n=7880)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.0605 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.2898` → IC=+0.250 (n=1788)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2898 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `2.617` → IC=+0.199 (n=4154)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.617 (IC base=+0.188)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.213 (n=8151)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.188)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.243 (n=810)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.214)

- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.244 (n=807)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0084 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.229 (n=1162)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.217 (n=1628)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.323 (n=931)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.666` → IC=+0.348 (n=563)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.666 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.2762` → IC=+0.279 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2762 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `2.2602` → IC=+0.228 (n=1048)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2602 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.231 (n=2507)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.214)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.228 (n=960)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.214)

- **PATRÓN** `sigma_h` < `0.008` → IC=+0.262 (n=2031)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.259)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.264 (n=2039)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.259)

- **PATRÓN** `drift_60min` |x|≤ `0.2024` → IC=+0.271 (n=1354)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2024 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.265 (n=1844)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.259)

- **PATRÓN** `ibs_20min` < `0.4947` → IC=+0.284 (n=2032)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4947 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.491` → IC=+0.263 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.491 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` < `0.1572` → IC=+0.257 (n=2000)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1572 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` > `0.2845` → IC=+0.278 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2845 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` > `2.2759` → IC=+0.273 (n=867)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2759 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.260 (n=2243)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1878.5011` → IC=+0.259 (n=1354)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1878.5011 (IC base=+0.259)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.201 (n=786)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.1751` → IC=+0.167 (n=1573)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.1751 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=2469)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.2708` → IC=+0.208 (n=2358)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2708 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1242` → IC=+0.192 (n=1282)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1242 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.723` → IC=+0.165 (n=511)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 9.723 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.181` → IC=+0.155 (n=2149)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.181 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.6288` → IC=+0.175 (n=787)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6288 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` < `0.0718` → IC=+0.153 (n=2098)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.0718 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.2713` → IC=+0.180 (n=339)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2713 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.1754` → IC=+0.160 (n=2023)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1754 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.5329` → IC=+0.153 (n=2054)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.5329 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `269.0` → IC=+0.181 (n=988)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 269.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.195 (n=654)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0026 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.077` → IC=+0.183 (n=654)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.077 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.180 (n=738)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.6963` → IC=+0.199 (n=1958)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.6963 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.365` → IC=+0.159 (n=438)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 9.365 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `1.1856` → IC=+0.160 (n=1958)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.1856 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.1543` → IC=+0.193 (n=525)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.1543 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.4411` → IC=+0.154 (n=1855)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4411 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.7862` → IC=+0.163 (n=1237)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.7862 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `253.0` → IC=+0.150 (n=592)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 253.0 (IC base=+0.148)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.246 (n=813)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.229 (n=2558)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=2185)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.301 (n=919)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.391` → IC=+0.311 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.391 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` < `0.0977` → IC=+0.223 (n=2141)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0977 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.6973` → IC=+0.235 (n=1069)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6973 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.230 (n=2869)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.221)

- **PATRÓN** `sigma_h` < `0.0085` → IC=+0.243 (n=1516)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0085 (IC base=+0.240)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.242 (n=2030)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.1782` → IC=+0.260 (n=1001)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1782 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.264 (n=851)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0204` → IC=+0.303 (n=758)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0204 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.079` → IC=+0.289 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.079 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.3426` → IC=+0.300 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3426 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.724` → IC=+0.238 (n=945)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.724 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.1351` → IC=+0.249 (n=1431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1351 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `2078.0166` → IC=+0.263 (n=758)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2078.0166 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.264 (n=770)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.240)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.201 (n=1108)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.325` → IC=+0.156 (n=2213)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.325 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.160 (n=2622)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.2654` → IC=+0.193 (n=2514)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.2654 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.5323` → IC=+0.169 (n=644)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.5323 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.19` → IC=+0.165 (n=1024)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 4.19 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `0.8733` → IC=+0.163 (n=1676)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8733 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.2832` → IC=+0.181 (n=334)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2832 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.5223` → IC=+0.171 (n=1078)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5223 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `2.1779` → IC=+0.158 (n=1111)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.1779 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `7159.933` → IC=+0.240 (n=1140)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7159.933 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `79.0` → IC=+0.171 (n=1073)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 79.0 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.194 (n=691)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0032 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.337` → IC=+0.140 (n=1811)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.337 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.155 (n=747)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` < `0.7427` → IC=+0.189 (n=2058)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.7427 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.325` → IC=+0.167 (n=421)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.325 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `0.8745` → IC=+0.143 (n=1372)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.8745 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.2964` → IC=+0.224 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2964 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `1.4316` → IC=+0.141 (n=1974)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.4316 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `5308.505` → IC=+0.205 (n=933)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5308.505 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `161.0` → IC=+0.131 (n=1988)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 161.0 (IC base=+0.131)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.149 (n=1152)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0099 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.178 (n=931)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.4483` → IC=+0.197 (n=2543)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.4483 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `1.0114` → IC=+0.206 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0114 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.919` → IC=+0.262 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.919 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `0.8886` → IC=+0.146 (n=1694)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.8886 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` < `0.1626` → IC=+0.125 (n=2632)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1626 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.2808` → IC=+0.136 (n=330)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.2808 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `2.4767` → IC=+0.122 (n=2477)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.4767 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `1.4662` → IC=+0.128 (n=2477)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.4662 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.128 (n=2588)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.02 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `2912.6118` → IC=+0.253 (n=847)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2912.6118 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.137 (n=803)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 26.0 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.143 (n=2412)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0108 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.1301` → IC=+0.163 (n=804)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.1301 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.157 (n=1121)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 15.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.214 (n=2413)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6364 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.379` → IC=+0.135 (n=2320)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 3.379 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `0.713` → IC=+0.147 (n=1061)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.713 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.223` → IC=+0.168 (n=401)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.223 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.4366` → IC=+0.157 (n=747)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.4366 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2780.1246` → IC=+0.207 (n=804)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2780.1246 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.139 (n=1979)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 49.0 (IC base=+0.120)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0133` → IC=+0.241 (n=2166)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0133 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.227 (n=2534)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.228 (n=1754)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `0.605` → IC=+0.269 (n=2166)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.605 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` > `0.1967` → IC=+0.237 (n=1342)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1967 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.743` → IC=+0.264 (n=821)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.743 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` < `1.2323` → IC=+0.227 (n=2425)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2323 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` > `0.6389` → IC=+0.224 (n=2424)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6389 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.2376` → IC=+0.251 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2376 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.5204` → IC=+0.250 (n=785)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5204 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.226 (n=2110)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `2673.605` → IC=+0.237 (n=1616)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2673.605 (IC base=+0.222)

- **PATRÓN** `sigma_h` > `0.0227` → IC=+0.241 (n=1147)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0227 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.231 (n=2374)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` < `0.51` → IC=+0.262 (n=2531)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.51 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.19` → IC=+0.256 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.19 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` > `1.2332` → IC=+0.254 (n=843)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2332 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.2821` → IC=+0.295 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2821 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `1.4358` → IC=+0.227 (n=2335)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4358 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `2658.8407` → IC=+0.223 (n=1686)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2658.8407 (IC base=+0.223)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.217 (n=2271)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.223)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.182 (n=4382)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.235 (n=1491)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.4959` → IC=+0.207 (n=4453)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4959 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.210 (n=1606)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.198 (n=3065)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 11.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` > `0.9412` → IC=+0.246 (n=1484)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9412 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` > `0.168` → IC=+0.201 (n=1659)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.168 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` < `0.2376` → IC=+0.200 (n=2790)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2376 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.188` → IC=+0.215 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.188 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` < `0.7092` → IC=+0.210 (n=1410)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7092 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` > `0.892` → IC=+0.203 (n=2136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.892 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.1671` → IC=+0.220 (n=1250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1671 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` < `1.4557` → IC=+0.205 (n=1464)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4557 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` > `1.8475` → IC=+0.201 (n=2924)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8475 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=3367)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `2973.5125` → IC=+0.208 (n=3978)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2973.5125 (IC base=+0.197)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.230 (n=1100)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.4868` → IC=+0.197 (n=3298)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.4868 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.199 (n=1106)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.200 (n=1486)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` < `0.1782` → IC=+0.197 (n=1452)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.1782 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.6469` → IC=+0.186 (n=556)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.6469 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.858` → IC=+0.188 (n=2936)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 3.858 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.2566` → IC=+0.187 (n=3105)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 1.2566 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` < `0.0976` → IC=+0.186 (n=3007)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.0976 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` < `1.5352` → IC=+0.186 (n=1431)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.5352 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `1.8194` → IC=+0.188 (n=2168)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 1.8194 (IC base=+0.181)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.182 (n=4382)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.195 (n=2160)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 69.0 (IC base=+0.181)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.249 (n=505)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.1096` → IC=+0.269 (n=253)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1096 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.231 (n=421)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` < `0.2756` → IC=+0.265 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2756 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.761` → IC=+0.229 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.761 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` < `0.317` → IC=+0.238 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.317 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.071` → IC=+0.242 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.071 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.566` → IC=+0.228 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.566 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` < `1.231` → IC=+0.234 (n=574)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.231 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `0.8602` → IC=+0.242 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8602 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2958` → IC=+0.324 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2958 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `1.5506` → IC=+0.240 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5506 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `12462.0901` → IC=+0.247 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12462.0901 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.237 (n=493)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.158)

- **PATRÓN** `drift_60min` |x|≤ `0.3662` → IC=+0.172 (n=1118)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.3662 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.198 (n=409)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.158)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.188 (n=418)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 5.0 (IC base=+0.158)

- **PATRÓN** `ibs_20min` < `0.1485` → IC=+0.186 (n=492)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.1485 (IC base=+0.158)

- **PATRÓN** `ibs_20min` > `0.6071` → IC=+0.162 (n=507)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.6071 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `0.6714` → IC=+0.198 (n=104)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.6714 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` < `0.211` → IC=+0.159 (n=1132)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.211 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.421` → IC=+0.177 (n=1101)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 6.421 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` < `0.8872` → IC=+0.195 (n=746)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.8872 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` > `0.0692` → IC=+0.181 (n=516)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.0692 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` < `2.5306` → IC=+0.164 (n=1114)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 2.5306 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` > `1.8123` → IC=+0.176 (n=743)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.8123 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `11474.1256` → IC=+0.172 (n=1118)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 11474.1256 (IC base=+0.158)

- **PATRÓN** `ballena_activa_n` < `701.0` → IC=+0.171 (n=1073)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 701.0 (IC base=+0.158)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.201 (n=232)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.172)

- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.185 (n=316)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0098 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.2884` → IC=+0.172 (n=464)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.2884 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.232 (n=248)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.235 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.51` → IC=+0.217 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.51 (IC base=+0.172)

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

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.281 (n=39)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.2121` → IC=+0.263 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2121 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.442` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.442 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` < `0.2021` → IC=+0.250 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2021 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `2.4518` → IC=+0.250 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4518 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `3.306` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.306 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `2407.5596` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2407.5596 (IC base=+0.227)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.008` → IC=+0.215 (n=1302)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.4578` → IC=+0.208 (n=1301)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4578 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=469)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.201 (n=1146)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` < `0.5174` → IC=+0.216 (n=868)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5174 (IC base=+0.201)

- **PATRÓN** `ibs_20min` > `0.8779` → IC=+0.209 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8779 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.134` → IC=+0.208 (n=1170)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.134 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` < `0.8825` → IC=+0.205 (n=869)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8825 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` > `1.2423` → IC=+0.209 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2423 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` < `0.1054` → IC=+0.204 (n=1195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1054 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.1645` → IC=+0.205 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1645 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` < `1.4176` → IC=+0.224 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4176 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=1323)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.245 (n=351)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.4878` → IC=+0.203 (n=1051)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4878 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.190 (n=404)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 16.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.192 (n=705)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 10.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` < `0.7511` → IC=+0.184 (n=1051)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.7511 (IC base=+0.177)

- **PATRÓN** `ibs_20min` > `0.0863` → IC=+0.179 (n=1051)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.0863 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` > `0.6351` → IC=+0.195 (n=195)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.6351 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.718` → IC=+0.183 (n=1073)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 6.718 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` < `1.2445` → IC=+0.191 (n=1051)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 1.2445 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` > `0.7194` → IC=+0.177 (n=939)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.7194 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.0735` → IC=+0.194 (n=443)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.0735 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` < `2.1843` → IC=+0.189 (n=905)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 2.1843 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `1.7807` → IC=+0.179 (n=686)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 1.7807 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `7269.491` → IC=+0.190 (n=1051)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 7269.491 (IC base=+0.177)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.224 (n=418)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.2892` → IC=+0.172 (n=419)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.2892 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.202 (n=598)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.252 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` > `0.2517` → IC=+0.201 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2517 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.252` → IC=+0.217 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.252 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `0.7061` → IC=+0.209 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7061 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` < `0.1075` → IC=+0.177 (n=564)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` < 0.1075 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.1633` → IC=+0.193 (n=190)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.1633 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `2.5465` → IC=+0.207 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5465 (IC base=+0.171)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.177 (n=722)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.02 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `3205.049` → IC=+0.198 (n=560)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 3205.049 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.185 (n=608)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 54.0 (IC base=+0.171)

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

- **PATRÓN** `ibs_20min` > `0.4161` → IC=+0.147 (n=1357)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.4161 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` > `0.1386` → IC=+0.138 (n=724)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.1386 (IC base=+0.072)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.443` → IC=+0.183 (n=304)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 11.443 (IC base=+0.072)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.161 (n=184)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.072)

- **PATRÓN** `ibs_20min` < `0.1923` → IC=+0.252 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1923 (IC base=+0.058)

- **PATRÓN** `dist_vwap_pct` < `0.0868` → IC=+0.126 (n=632)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` < 0.0868 (IC base=+0.058)

- **PATRÓN** `volumen_pendiente_norm` > `0.1474` → IC=+0.192 (n=170)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.1474 (IC base=+0.058)

- **PATRÓN** `volumen_spike_ratio` < `1.3932` → IC=+0.124 (n=195)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.3932 (IC base=+0.058)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.137 (n=491)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0056 (IC base=+0.091)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.137 (n=166)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 18.0 (IC base=+0.091)

- **PATRÓN** `ibs_20min` > `0.3752` → IC=+0.169 (n=460)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.3752 (IC base=+0.091)

- **PATRÓN** `dist_vwap_pct` > `0.119` → IC=+0.158 (n=241)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.119 (IC base=+0.091)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.461` → IC=+0.121 (n=262)

  - _Acción_: Kelly boost +0.61€ cuando `sigma_ewma_delta_pct` > 3.461 (IC base=+0.091)

- **PATRÓN** `ibs_20min` < `0.0468` → IC=+0.284 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0468 (IC base=+0.078)

- **PATRÓN** `dist_vwap_pct` < `0.1052` → IC=+0.131 (n=304)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.1052 (IC base=+0.078)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.623` → IC=+0.131 (n=258)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` < 4.623 (IC base=+0.078)

- **PATRÓN** `volumen_pendiente_norm` > `0.0755` → IC=+0.159 (n=121)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.0755 (IC base=+0.078)

- **PATRÓN** `volumen_spike_ratio` < `2.5595` → IC=+0.121 (n=275)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_spike_ratio` < 2.5595 (IC base=+0.078)

### GBM_LATE_60M#ETH#60min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.155 (n=320)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0046 (IC base=+0.095)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.132 (n=443)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 7.0 (IC base=+0.095)

- **PATRÓN** `ibs_20min` > `0.6728` → IC=+0.208 (n=395)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6728 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` > `0.1226` → IC=+0.181 (n=236)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.1226 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.742` → IC=+0.262 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.742 (IC base=+0.095)

- **PATRÓN** `volumen_regimen` < `0.8187` → IC=+0.123 (n=295)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 0.8187 (IC base=+0.095)

- **PATRÓN** `volumen_pendiente_norm` > `0.2835` → IC=+0.189 (n=59)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2835 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `1727.3747` → IC=+0.149 (n=146)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 1727.3747 (IC base=+0.095)

- **PATRÓN** `ibs_20min` < `0.0244` → IC=+0.291 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0244 (IC base=+0.010)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.103` → IC=+0.177 (n=29)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 11.103 (IC base=+0.010)

- **PATRÓN** `volumen_pendiente_norm` > `0.136` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.136 (IC base=+0.010)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `ibs_20min` > `0.1333` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1333
  - _Potencial_: sin este filtro IC_bueno=+0.255 (n=153)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.159 (n=315)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.75 (IC base=+0.030)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.968` → IC=+0.139 (n=128)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 7.968 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.2436` → IC=+0.152 (n=87)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.2436 (IC base=+0.030)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.161 (n=184)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0092 (IC base=+0.077)

- **PATRÓN** `ibs_20min` < `0.1333` → IC=+0.255 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1333 (IC base=+0.077)

- **PATRÓN** `dist_vwap_pct` > `0.1353` → IC=+0.167 (n=37)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1353 (IC base=+0.077)

- **PATRÓN** `dist_vwap_pct` < `0.3459` → IC=+0.171 (n=168)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.3459 (IC base=+0.077)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.757` → IC=+0.344 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.757 (IC base=+0.077)

- **PATRÓN** `volumen_regimen` < `0.6683` → IC=+0.138 (n=67)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.6683 (IC base=+0.077)

- **PATRÓN** `volumen_regimen` > `1.074` → IC=+0.217 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.074 (IC base=+0.077)

- **PATRÓN** `volumen_pendiente_norm` > `0.1518` → IC=+0.287 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1518 (IC base=+0.077)

- **PATRÓN** `volumen_spike_ratio` > `2.4899` → IC=+0.217 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4899 (IC base=+0.077)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.205 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.077)

- **PATRÓN** `libro_liquidez` > `794.3457` → IC=+0.177 (n=91)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 794.3457 (IC base=+0.077)

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
  - _Potencial_: sin este filtro IC_bueno=-0.246 (n=175)

- **FILTRO** `dist_vwap_pct` > `0.3328` → IC=-0.386 (n=33)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3328
  - _Potencial_: sin este filtro IC_bueno=-0.261 (n=199)

- **FILTRO** `volumen_regimen` > `0.8688` → IC=-0.312 (n=78)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8688
  - _Potencial_: sin este filtro IC_bueno=-0.263 (n=154)

- **FILTRO** `volumen_pendiente_norm` > `0.0549` → IC=-0.389 (n=25)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0549
  - _Potencial_: sin este filtro IC_bueno=-0.256 (n=121)

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
  - _Potencial_: sin este filtro IC_bueno=-0.218 (n=76)

- **FILTRO** `volumen_spike_ratio` > `1.5538` → IC=-0.329 (n=33)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.5538
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=35)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.8227` → IC=-0.378 (n=47)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8227
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=48)

- **FILTRO** `hora_utc` < `5.0` → IC=-0.350 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.257 (n=68)

- **FILTRO** `dist_vwap_pct` > `0.1182` → IC=-0.333 (n=28)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1182
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=58)

- **FILTRO** `volumen_spike_ratio` > `2.2319` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.2319
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=36)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.276 (n=56)

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
- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.167 (n=208)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0057 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.120 (n=480)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 5.0 (IC base=+0.104)

- **PATRÓN** `ibs_20min` > `0.6686` → IC=+0.148 (n=456)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.6686 (IC base=+0.104)

- **PATRÓN** `dist_vwap_pct` > `0.4854` → IC=+0.207 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4854 (IC base=+0.104)

- **PATRÓN** `volumen_regimen` < `0.6589` → IC=+0.156 (n=152)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6589 (IC base=+0.104)

- **PATRÓN** `volumen_pendiente_norm` < `0.2335` → IC=+0.135 (n=393)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` < 0.2335 (IC base=+0.104)

- **PATRÓN** `volumen_spike_ratio` < `2.5471` → IC=+0.135 (n=354)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.5471 (IC base=+0.104)

- **PATRÓN** `ibs_20min` < `0.1622` → IC=+0.168 (n=465)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.1622 (IC base=+0.071)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.127` → IC=+0.187 (n=161)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 9.127 (IC base=+0.071)

- **PATRÓN** `libro_liquidez` > `3082.2157` → IC=+0.155 (n=352)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 3082.2157 (IC base=+0.071)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6544` → IC=-0.250 (n=46)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6544
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=140)

- **PATRÓN** `sigma_h` > `0.004` → IC=+0.212 (n=109)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.004 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.165 (n=162)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 12.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.174 (n=90)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 6.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` < `0.1321` → IC=+0.201 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1321 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.2224` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.2224 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.0916` → IC=+0.159 (n=244)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.0916 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.253` → IC=+0.175 (n=75)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 10.253 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.645` → IC=+0.167 (n=190)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 4.645 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` > `0.6754` → IC=+0.167 (n=214)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.6754 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` < `0.078` → IC=+0.177 (n=184)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` < 0.078 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.2817` → IC=+0.167 (n=37)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2817 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.2515` → IC=+0.170 (n=183)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 2.2515 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.449` → IC=+0.160 (n=207)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.449 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `5157.3278` → IC=+0.158 (n=159)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 5157.3278 (IC base=+0.150)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `ibs_20min` > `0.2345` → IC=-0.130 (n=90)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2345
  - _Potencial_: sin este filtro IC_bueno=+0.129 (n=176)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.139 (n=142)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0045 (IC base=+0.088)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.161 (n=57)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 18.0 (IC base=+0.088)

- **PATRÓN** `ibs_20min` > `0.7141` → IC=+0.132 (n=161)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` > 0.7141 (IC base=+0.088)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.022` → IC=+0.139 (n=120)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 3.022 (IC base=+0.088)

- **PATRÓN** `volumen_pendiente_norm` < `0.1363` → IC=+0.127 (n=148)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1363 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` < `1.7926` → IC=+0.170 (n=89)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.7926 (IC base=+0.088)

- **PATRÓN** `libro_liquidez` > `1868.6989` → IC=+0.124 (n=107)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 1868.6989 (IC base=+0.088)

- **PATRÓN** `ibs_20min` < `0.2345` → IC=+0.129 (n=176)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.2345 (IC base=+0.041)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.957` → IC=+0.255 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.957 (IC base=+0.041)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.1679` → IC=-0.221 (n=59)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1679
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=61)

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

- **PATRÓN** `sigma_ewma_delta_pct` > `8.418` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.418 (IC base=-0.074)

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
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.121 (n=1138)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.102)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.121 (n=1138)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.102)

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
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=3091)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.135 (n=206)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.495 (IC base=+0.045)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=1129)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=1083)

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
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=794)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=794)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.133 (n=246)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=628)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=661)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=661)

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
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=166)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=190)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=244)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=204)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=317)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=317)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=230)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.43` → IC=-0.120 (n=1672)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=1792)

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
- **FILTRO** `py_entrada` < `0.5` → IC=-0.133 (n=227)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=118)

- **FILTRO** `profundidad_ratio` < `236.9` → IC=-0.126 (n=113)

  - _Acción_: SKIP cuando `profundidad_ratio` < 236.9
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=232)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.182 (n=108)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.46 (IC base=+0.027)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.200 (n=38)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=183)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.154 (n=102)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=123)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.242 (n=64)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=241)

- **FILTRO** `profundidad_ratio` < `53.7` → IC=-0.167 (n=100)

  - _Acción_: SKIP cuando `profundidad_ratio` < 53.7
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=205)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.245 (n=53)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=248)

- **PATRÓN** `py_entrada` < `0.46` → IC=+0.154 (n=79)

  - _Acción_: Kelly boost +0.77€ cuando `py_entrada` < 0.46 (IC base=-0.028)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.142 (n=188)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=200)

- **FILTRO** `restante_min` < `3.35` → IC=-0.192 (n=128)

  - _Acción_: SKIP cuando `restante_min` < 3.35
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=260)

- **FILTRO** `lag_apertura_s` > `97.1` → IC=-0.199 (n=131)

  - _Acción_: SKIP cuando `lag_apertura_s` > 97.1
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=257)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.146 (n=63)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=243)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **PATRÓN** `py_entrada` > `0.48` → IC=+0.123 (n=120)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.48 (IC base=-0.023)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.137 (n=235)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=122)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.183 (n=99)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=346)

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
- **FILTRO** `py_entrada` < `0.475` → IC=-0.158 (n=5330)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=15996)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.166 (n=5502)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=16518)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.184 (n=952)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=2867)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.156 (n=910)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=3028)

- **PATRÓN** `libro_liquidez` > `1969.89` → IC=+0.153 (n=955)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 1969.89 (IC base=+0.037)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.122 (n=1821)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.5 (IC base=+0.015)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.174 (n=756)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=2405)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.174 (n=939)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=2931)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.185 (n=994)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=3013)

- **PATRÓN** `ibs_20min` > `0.9653` → IC=+0.121 (n=1316)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` > 0.9653 (IC base=+0.036)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=2245)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=2661)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=3401)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.172 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=412)

- **FILTRO** `libro_liquidez` < `16920.0467` → IC=-0.163 (n=176)

  - _Acción_: SKIP cuando `libro_liquidez` < 16920.0467
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=359)

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
  - _Potencial_: sin este filtro IC_bueno=-0.106 (n=323)

- **FILTRO** `libro_liquidez` < `3139.5911` → IC=-0.184 (n=134)

  - _Acción_: SKIP cuando `libro_liquidez` < 3139.5911
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=275)

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
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=32969)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.285 (n=11475)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=36255)

- **FILTRO** `ibs_7min` < `0.25` → IC=-0.232 (n=11919)

  - _Acción_: SKIP cuando `ibs_7min` < 0.25
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=35811)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.154 (n=15747)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=31983)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.237 (n=14660)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=45848)

- **FILTRO** `ibs_7min` > `0.2857` → IC=-0.179 (n=15037)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=45471)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.146 (n=2381)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=5833)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.310 (n=1970)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=6244)

- **FILTRO** `ibs_7min` < `0.7089` → IC=-0.248 (n=2708)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7089
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=5506)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.173 (n=1930)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=6284)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.269 (n=2576)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=7918)

- **FILTRO** `ibs_7min` > `0.7754` → IC=-0.208 (n=2623)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7754
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=7871)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.128 (n=1948)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=6160)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.263 (n=1841)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=6267)

- **FILTRO** `ibs_7min` < `0.7352` → IC=-0.197 (n=2027)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7352
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=6081)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.187 (n=2015)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=6093)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.264 (n=1990)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=6266)

- **FILTRO** `ibs_7min` > `0.2665` → IC=-0.195 (n=2062)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2665
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=6194)

- **FILTRO** `ballena_activa_n` > `148.0` → IC=-0.185 (n=2048)

  - _Acción_: SKIP cuando `ballena_activa_n` > 148.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=6208)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.163 (n=1918)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=5894)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.319 (n=1871)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=5941)

- **FILTRO** `ibs_7min` < `0.7021` → IC=-0.245 (n=2577)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7021
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=5235)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.222 (n=1657)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=6155)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.247 (n=2534)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=8638)

- **FILTRO** `ibs_7min` > `0.7341` → IC=-0.174 (n=2792)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7341
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=8380)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.126 (n=2545)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=5272)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.252 (n=1954)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=5863)

- **FILTRO** `ibs_7min` < `0.7344` → IC=-0.187 (n=1954)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7344
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=5863)

- **FILTRO** `ballena_activa_n` > `28.0` → IC=-0.190 (n=1939)

  - _Acción_: SKIP cuando `ballena_activa_n` > 28.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=5878)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.263 (n=2018)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=6068)

- **FILTRO** `ibs_7min` > `0.2753` → IC=-0.179 (n=2021)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2753
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=6065)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.180 (n=1987)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=6099)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.272 (n=1955)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=5999)

- **FILTRO** `ibs_7min` < `0.2333` → IC=-0.234 (n=1985)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2333
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=5969)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.185 (n=2735)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=8821)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.283 (n=1923)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=5902)

- **FILTRO** `ibs_7min` < `0.2245` → IC=-0.223 (n=1956)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2245
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=5869)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.200 (n=1834)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=5991)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.209 (n=2664)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=8280)

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

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=371)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.138 (n=158)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=315)

- **FILTRO** `libro_liquidez` < `3312.3658` → IC=-0.151 (n=167)

  - _Acción_: SKIP cuando `libro_liquidez` < 3312.3658
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=502)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=336)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.398` → IC=+0.142 (n=1025)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.71€ cuando `delta_ratio` |x|> 0.398 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.136 (n=476)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 14.0 (IC base=+0.127)

- **PATRÓN** `total_vol_5m` < `3639.536` → IC=+0.147 (n=684)

  - _Acción_: Kelly boost +0.74€ cuando `total_vol_5m` < 3639.536 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `3728.089` → IC=+0.132 (n=465)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 3728.089 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.160 (n=330)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 13.0 (IC base=+0.127)

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
- **PATRÓN** `delta_ratio` |x|> `0.401` → IC=+0.134 (n=173)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio` |x|> 0.401 (IC base=+0.095)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.121 (n=172)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` < 13.0 (IC base=+0.095)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.183 (n=121)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `3656.7944` → IC=+0.167 (n=88)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3656.7944 (IC base=+0.095)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `8.4547` → IC=-0.256 (n=43)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.4547
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=130)

- **FILTRO** `sigma_h` > `0.0052` → IC=-0.264 (n=294)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0052
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=295)

- **FILTRO** `T_h` > `130.2581` → IC=-0.211 (n=147)

  - _Acción_: SKIP cuando `T_h` > 130.2581
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=442)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.167 (n=148)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0034 (IC base=-0.084)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0056` → IC=-0.264 (n=87)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0056
  - _Potencial_: sin este filtro IC_bueno=+0.178 (n=88)

- **FILTRO** `T_h` > `88.1896` → IC=-0.300 (n=43)

  - _Acción_: SKIP cuando `T_h` > 88.1896
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=132)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.304 (n=44)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=-0.042)

- **PATRÓN** `pct_vs_K` |x|≤ `1.7112` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `pct_vs_K` |x|≤ 1.7112 (IC base=-0.042)

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
- **FILTRO** `sigma_h` < `0.0097` → IC=-0.222 (n=404)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=135)

- **FILTRO** `sigma_h` > `0.0089` → IC=-0.317 (n=113)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0089
  - _Potencial_: sin este filtro IC_bueno=-0.228 (n=343)

- **FILTRO** `pct_vs_K` |x|> `3.4411` → IC=-0.439 (n=113)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.4411
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=343)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0042` → IC=-0.202 (n=45)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0042
  - _Potencial_: sin este filtro IC_bueno=-0.121 (n=138)

- **FILTRO** `T_h` > `79.3043` → IC=-0.177 (n=122)

  - _Acción_: SKIP cuando `T_h` > 79.3043
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=61)

- **FILTRO** `pct_vs_K` |x|> `2.067` → IC=-0.393 (n=82)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.067
  - _Potencial_: sin este filtro IC_bueno=-0.163 (n=84)

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
- **FILTRO** `sigma_h` < `0.0049` → IC=-0.288 (n=50)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0049
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=102)

- **FILTRO** `T_h` < `87.9882` → IC=-0.269 (n=50)

  - _Acción_: SKIP cuando `T_h` < 87.9882
  - _Potencial_: sin este filtro IC_bueno=-0.240 (n=102)

- **FILTRO** `pct_vs_K` |x|> `2.6475` → IC=-0.401 (n=69)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.6475
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=71)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `T_h` < `145.7969` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` < 145.7969
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0083` → IC=-0.245 (n=45)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0083
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=94)

- **FILTRO** `T_h` > `111.9844` → IC=-0.176 (n=69)

  - _Acción_: SKIP cuando `T_h` > 111.9844
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=70)

- **FILTRO** `pct_vs_K` |x|> `3.9474` → IC=-0.409 (n=31)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.9474
  - _Potencial_: sin este filtro IC_bueno=-0.238 (n=63)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1236` → IC=+0.475 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1236 (IC base=+0.341)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.386 (n=86)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.341)

- **PATRÓN** `T_h` < `0.9781` → IC=+0.359 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.9781 (IC base=+0.341)

- **PATRÓN** `T_h` > `1.1834` → IC=+0.403 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.1834 (IC base=+0.341)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.476 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.341)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.361 (n=77)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.341)

- **PATRÓN** `edge` > `0.096` → IC=+0.446 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.096 (IC base=+0.418)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.429 (n=68)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.418)

- **PATRÓN** `sigma_h` > `0.0096` → IC=+0.441 (n=133)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0096 (IC base=+0.418)

- **PATRÓN** `T_h` < `0.5967` → IC=+0.427 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.5967 (IC base=+0.418)

- **PATRÓN** `T_h` > `1.4829` → IC=+0.442 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4829 (IC base=+0.418)

- **PATRÓN** `dist_50` > `0.3874` → IC=+0.465 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3874 (IC base=+0.418)

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
- **PATRÓN** `edge` > `0.1975` → IC=+0.482 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1975 (IC base=+0.432)

- **PATRÓN** `sigma_h` < `0.016` → IC=+0.464 (n=53)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.016 (IC base=+0.432)

- **PATRÓN** `T_h` > `0.639` → IC=+0.459 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.639 (IC base=+0.432)

- **PATRÓN** `dist_50` > `0.354` → IC=+0.464 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.354 (IC base=+0.432)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.435 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.432)

- **PATRÓN** `edge` > `0.2005` → IC=+0.477 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2005 (IC base=+0.463)

- **PATRÓN** `sigma_h` < `0.0157` → IC=+0.477 (n=130)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0157 (IC base=+0.463)

- **PATRÓN** `T_h` > `1.2025` → IC=+0.477 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.2025 (IC base=+0.463)

- **PATRÓN** `dist_50` > `0.4455` → IC=+0.485 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4455 (IC base=+0.463)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.472 (n=139)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.463)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=276)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=352)

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
- **PATRÓN** `streak_estiramiento` < `0.3514` → IC=+0.133 (n=47)

  - _Acción_: Kelly boost +0.66€ cuando `streak_estiramiento` < 0.3514 (IC base=+0.010)

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
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=41)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=26)

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
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=897)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1326)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=1032)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=1045)

### STRUCT_NO_15M
- **FILTRO** `libro_liquidez` < `7203.0371` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 7203.0371
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=3697)

### STRUCT_NO_15M#ETH#15min
- **FILTRO** `libro_liquidez` < `7203.0371` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 7203.0371
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=1975)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.205 (n=1015)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.192)

- **PATRÓN** `sigma_h` > `0.011` → IC=+0.230 (n=1015)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.192)

- **PATRÓN** `drift_60min` |x|≤ `0.1656` → IC=+0.200 (n=2680)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1656 (IC base=+0.192)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2288` → IC=+0.193 (n=1015)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.97€ cuando `delta_ratio_macro` |x|> 0.2288 (IC base=+0.192)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3522` → IC=+0.204 (n=2710)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3522 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.197 (n=2830)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 6.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.196 (n=2791)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.192)

- **PATRÓN** `ibs_15` > `0.587` → IC=+0.268 (n=3046)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.587 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` > `0.1212` → IC=+0.186 (n=1442)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1212 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` < `0.2991` → IC=+0.179 (n=2291)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.2991 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.579` → IC=+0.271 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.579 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `5427.2622` → IC=+0.202 (n=1015)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5427.2622 (IC base=+0.192)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1191)

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
- **FILTRO** `sigma_ewma_delta_pct` > `28.475` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 28.475
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=679)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.185 (n=201)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0033 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.0667` → IC=+0.159 (n=265)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.0667 (IC base=+0.147)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1506` → IC=+0.161 (n=402)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio_macro` |x|> 0.1506 (IC base=+0.147)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1304` → IC=+0.168 (n=233)

  - _Acción_: Kelly boost +0.84€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1304 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.155 (n=282)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 15.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.153 (n=632)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 17.0 (IC base=+0.147)

- **PATRÓN** `ibs_15` > `0.5728` → IC=+0.244 (n=603)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5728 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.1534` → IC=+0.149 (n=337)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.1534 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.2646` → IC=+0.151 (n=560)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.2646 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.049` → IC=+0.286 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.049 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `3532.4883` → IC=+0.152 (n=539)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3532.4883 (IC base=+0.147)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `19.257` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.257
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=244)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.151 (n=190)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0055 (IC base=+0.115)

- **PATRÓN** `sigma_h` > `0.0096` → IC=+0.165 (n=189)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0096 (IC base=+0.115)

- **PATRÓN** `drift_60min` |x|≤ `0.1376` → IC=+0.156 (n=379)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1376 (IC base=+0.115)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3405` → IC=+0.133 (n=518)

  - _Acción_: Kelly boost +0.66€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3405 (IC base=+0.115)

- **PATRÓN** `ibs_15` > `0.5082` → IC=+0.194 (n=507)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.97€ cuando `ibs_15` > 0.5082 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` < `0.1905` → IC=+0.134 (n=504)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1905 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.265` → IC=+0.190 (n=114)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 17.265 (IC base=+0.115)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=316)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.115)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `15.781` → IC=+0.167 (n=40)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 15.781 (IC base=+0.012)

- **PATRÓN** `libro_liquidez` > `3382.3786` → IC=+0.120 (n=77)

  - _Acción_: Kelly boost +0.60€ cuando `libro_liquidez` > 3382.3786 (IC base=+0.012)

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
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.366 (n=385)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.364)

- **PATRÓN** `sigma_h` > `0.0027` → IC=+0.372 (n=576)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0027 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1522` → IC=+0.386 (n=384)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1522 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2309` → IC=+0.388 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2309 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.378 (n=581)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.7883` → IC=+0.398 (n=576)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7883 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.4129` → IC=+0.384 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4129 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.88` → IC=+0.385 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.88 (IC base=+0.364)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.369 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `3851.736` → IC=+0.372 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3851.736 (IC base=+0.364)

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
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.363 (n=180)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.364)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.375 (n=270)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0033 (IC base=+0.364)

- **PATRÓN** `drift_60min` |x|≤ `0.1074` → IC=+0.368 (n=180)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1074 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0904` → IC=+0.377 (n=241)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0904 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2995` → IC=+0.393 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2995 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.407 (n=127)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.364)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.364 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.7557` → IC=+0.408 (n=270)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7557 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.4366` → IC=+0.366 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4366 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` < `0.2765` → IC=+0.370 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2765 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.356` → IC=+0.391 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.356 (IC base=+0.364)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.370 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `3893.6222` → IC=+0.388 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3893.6222 (IC base=+0.364)

- **PATRÓN** `ballena_activa_n` < `140.0` → IC=+0.372 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 140.0 (IC base=+0.364)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0121` → IC=-0.222 (n=986)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0121
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=2960)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.207 (n=1531)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=2415)

- **FILTRO** `libro_liquidez` < `4125.872` → IC=-0.146 (n=2604)

  - _Acción_: SKIP cuando `libro_liquidez` < 4125.872
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

- **PATRÓN** `delta_ratio_macro` |x|> `0.2253` → IC=+0.267 (n=1067)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2253 (IC base=-0.012)

- **PATRÓN** `ibs_15` < `0.3525` → IC=+0.282 (n=3201)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3525 (IC base=-0.012)

- **PATRÓN** `dist_vwap_pct` > `0.6383` → IC=+0.282 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6383 (IC base=-0.012)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0066` → IC=-0.203 (n=547)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0066
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=1645)

- **FILTRO** `sigma_h` < `0.0033` → IC=-0.229 (n=548)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=1644)

- **FILTRO** `sigma_ewma_delta_pct` > `23.887` → IC=-0.268 (n=317)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.887
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=1875)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.203 (n=62)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=2130)

- **FILTRO** `libro_liquidez` < `16286.5135` → IC=-0.203 (n=1446)

  - _Acción_: SKIP cuando `libro_liquidez` < 16286.5135
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=746)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.171 (n=223)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0026 (IC base=+0.094)

- **PATRÓN** `delta_ratio_macro` |x|> `0.217` → IC=+0.298 (n=132)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.217 (IC base=+0.094)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1042` → IC=+0.281 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1042 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.137 (n=326)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 15.0 (IC base=+0.094)

- **PATRÓN** `ibs_15` > `0.7566` → IC=+0.336 (n=291)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7566 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `0.1047` → IC=+0.301 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1047 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` < `0.3651` → IC=+0.293 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3651 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `24.877` → IC=+0.141 (n=154)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 24.877 (IC base=+0.094)

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

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.258 (n=485)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.3481` → IC=+0.244 (n=969)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3481 (IC base=+0.241)

- **PATRÓN** `drift_15min` |x|≤ `0.7516` → IC=+0.253 (n=969)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7516 (IC base=+0.241)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2143` → IC=+0.263 (n=499)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2143 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.243 (n=984)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.241)

- **PATRÓN** `ibs_15` < `0.3683` → IC=+0.272 (n=1101)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3683 (IC base=+0.241)

- **PATRÓN** `dist_vwap_pct` > `0.764` → IC=+0.288 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.764 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.404` → IC=+0.258 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.404 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.584` → IC=+0.246 (n=1151)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.584 (IC base=+0.241)

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

- **PATRÓN** `delta_ratio_macro` |x|> `0.0649` → IC=+0.243 (n=496)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0649 (IC base=-0.038)

- **PATRÓN** `ibs_15` < `0.3462` → IC=+0.287 (n=496)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3462 (IC base=-0.038)

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
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.298 (n=843)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.292)

- **PATRÓN** `sigma_h` > `0.0028` → IC=+0.291 (n=957)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0028 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.0533` → IC=+0.323 (n=320)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0533 (IC base=+0.292)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2484` → IC=+0.297 (n=319)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2484 (IC base=+0.292)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2247` → IC=+0.311 (n=563)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2247 (IC base=+0.292)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.309 (n=1001)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.292)

- **PATRÓN** `ibs_15` > `0.838` → IC=+0.324 (n=958)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.838 (IC base=+0.292)

- **PATRÓN** `dist_vwap_pct` > `0.263` → IC=+0.318 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.263 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` > `24.005` → IC=+0.366 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 24.005 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `12762.7474` → IC=+0.307 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12762.7474 (IC base=+0.292)

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
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.307 (n=293)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.297)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.298 (n=439)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0033 (IC base=+0.297)

- **PATRÓN** `drift_60min` |x|≤ `0.0506` → IC=+0.326 (n=147)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0506 (IC base=+0.297)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1534` → IC=+0.303 (n=293)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1534 (IC base=+0.297)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3023` → IC=+0.320 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3023 (IC base=+0.297)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.317 (n=425)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.297)

- **PATRÓN** `ibs_15` > `0.876` → IC=+0.343 (n=392)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.876 (IC base=+0.297)

- **PATRÓN** `dist_vwap_pct` > `0.5931` → IC=+0.325 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5931 (IC base=+0.297)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.754` → IC=+0.348 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.754 (IC base=+0.297)

### UPDOWN_OU_5M
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1089` → IC=-0.149 (n=209)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1089
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=71)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.172 (n=117)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=353)

- **FILTRO** `ballena_activa_n` > `50.0` → IC=-0.204 (n=52)

  - _Acción_: SKIP cuando `ballena_activa_n` > 50.0
  - _Potencial_: sin este filtro IC_bueno=-0.129 (n=157)

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
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=141)

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
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=17)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0905` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0905
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `81.6471` → IC=+0.198 (n=429)

  - _Acción_: Kelly boost +0.99€ cuando `T_h` > 81.6471 (IC base=+0.192)

- **PATRÓN** `ratio` < `0.9744` → IC=+0.415 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9744 (IC base=+0.192)

- **PATRÓN** `T_h` > `145.7201` → IC=+0.384 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7201 (IC base=+0.335)

- **PATRÓN** `ratio` > `1.0236` → IC=+0.366 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0236 (IC base=+0.335)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `103.3918` → IC=+0.176 (n=177)

  - _Acción_: Kelly boost +0.88€ cuando `T_h` > 103.3918 (IC base=+0.165)

- **PATRÓN** `ratio` < `0.9702` → IC=+0.370 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9702 (IC base=+0.165)

- **PATRÓN** `T_h` > `106.964` → IC=+0.299 (n=665)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 106.964 (IC base=+0.289)

- **PATRÓN** `ratio` > `1.0466` → IC=+0.392 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0466 (IC base=+0.289)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `81.6124` → IC=+0.237 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 81.6124 (IC base=+0.229)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.401 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.229)

- **PATRÓN** `T_h` > `111.9668` → IC=+0.347 (n=703)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9668 (IC base=+0.323)

- **PATRÓN** `ratio` > `1.0093` → IC=+0.348 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0093 (IC base=+0.323)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1062` → IC=+0.450 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1062 (IC base=+0.400)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.587 sube el IC de +0.192 a +0.268 en UPDOWN_GBM#15min (n=3046). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7199 sube el IC de +0.217 a +0.280 en UPDOWN_GBM#BTC#15min (n=540). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5728 sube el IC de +0.147 a +0.244 en UPDOWN_GBM#ETH#15min (n=603). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.5082 sube el IC de +0.115 a +0.194 en UPDOWN_GBM#SOL#15min (n=507). Ya aplicado como kelly_boost=+0.97€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5745 sube el IC de +0.222 a +0.303 en UPDOWN_GBM#XRP#15min (n=699). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1111 sube el IC de +0.065 a +0.162 en UPDOWN_GBM#XRP#15min (n=722). Ya aplicado como kelly_boost=+0.81€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6352 sube el IC de -0.066 a +0.284 en UPDOWN_GBM_15M_TARDIO (n=948). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3525 sube el IC de -0.012 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=3201). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7566 sube el IC de +0.094 a +0.336 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=291). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.618 sube el IC de -0.193 a +0.311 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=51). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6314 sube el IC de +0.153 a +0.255 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=475). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3683 sube el IC de +0.241 a +0.272 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1101). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.181 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3462 sube el IC de -0.038 a +0.287 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=496). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.202 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.027 a +0.295 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=778). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.838 sube el IC de +0.292 a +0.324 en UPDOWN_GBM_IBS_ALTO (n=958). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8601 sube el IC de +0.286 a +0.319 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=463). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.876 sube el IC de +0.297 a +0.343 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=392). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7883 sube el IC de +0.364 a +0.398 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=576). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8077 sube el IC de +0.361 a +0.387 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=307). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7557 sube el IC de +0.364 a +0.408 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=270). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1722 | +0.088 | +194.64€ | 0 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1722 | +0.088 | +194.64€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1348 | +0.091 | +166.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1348 | +0.091 | +166.79€ | 0 | 6 |
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
| ✅ BALLENAS_TARDIAS | 36783 | -0.083 | -4709.95€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1939 | +0.004 | -244.97€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 34844 | -0.088 | -4464.98€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4425 | -0.116 | -762.75€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4425 | -0.116 | -762.75€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1939 | +0.004 | -244.97€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1939 | +0.004 | -244.97€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4121 | -0.113 | -845.32€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4121 | -0.113 | -845.32€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 9605 | -0.000 | -874.56€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 9605 | -0.000 | -874.56€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 9563 | -0.109 | -716.28€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 9563 | -0.109 | -716.28€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 7130 | -0.147 | -1266.06€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 7130 | -0.147 | -1266.06€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 29997 | -0.018 | +3581.04€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 7758 | +0.003 | +1740.84€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 22239 | -0.025 | +1840.19€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 29997 | -0.018 | +3581.04€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 7758 | +0.003 | +1740.84€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 22239 | -0.025 | +1840.19€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 129277 | +0.114 | -5425.67€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 17357 | +0.182 | -534.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 559 | -0.033 | -65.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 103475 | +0.105 | -4553.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 7886 | +0.103 | -271.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 17172 | +0.106 | -1098.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 58 | -0.150 | +11.01€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 17099 | +0.107 | -1098.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 25339 | +0.129 | -393.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5032 | +0.193 | -150.43€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 17156 | +0.118 | -134.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3109 | +0.087 | -85.85€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 17223 | +0.097 | -1274.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 68 | -0.114 | -5.90€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 17140 | +0.098 | -1257.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 27470 | +0.124 | -476.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 7220 | +0.176 | -123.43€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 17366 | +0.106 | -297.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2872 | +0.101 | -46.21€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 24883 | +0.114 | -1329.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4919 | +0.191 | -272.40€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 462 | +0.002 | -11.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 17597 | +0.093 | -905.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1905 | +0.134 | -139.66€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 17190 | +0.104 | -853.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 60 | -0.065 | +6.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 17117 | +0.105 | -860.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 20735 | +0.194 | -1323.10€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 20735 | +0.194 | -1323.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 4766 | +0.175 | -437.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 4766 | +0.175 | -437.74€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 2428 | +0.200 | -55.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 2428 | +0.200 | -55.21€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 4707 | +0.179 | -392.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 4707 | +0.179 | -392.47€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 4113 | +0.244 | -143.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 4113 | +0.244 | -143.25€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 4642 | +0.187 | -308.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 4642 | +0.187 | -308.19€ | 0 | 3 |
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
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 72113 | +0.201 | -5266.02€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 72113 | +0.201 | -5266.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 12396 | +0.185 | -1282.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 12396 | +0.185 | -1282.56€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 11613 | +0.225 | -397.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 11613 | +0.225 | -397.01€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 12377 | +0.178 | -1352.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 12377 | +0.178 | -1352.43€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 11695 | +0.221 | -430.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 11695 | +0.221 | -430.71€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 11962 | +0.201 | -808.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 11962 | +0.201 | -808.31€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 12070 | +0.195 | -995.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 12070 | +0.195 | -995.00€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 27554 | +0.117 | +218.61€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 27554 | +0.117 | +218.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 13690 | +0.121 | +187.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 13690 | +0.121 | +187.55€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 13864 | +0.114 | +31.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 13864 | +0.114 | +31.06€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1882 | +0.295 | +6.86€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1882 | +0.295 | +6.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 853 | +0.286 | -4.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 853 | +0.286 | -4.97€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 910 | +0.294 | +6.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 910 | +0.294 | +6.52€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 119 | +0.351 | +5.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 119 | +0.351 | +5.31€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 868 | +0.443 | +6.43€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 868 | +0.443 | +6.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 419 | +0.441 | +0.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 419 | +0.441 | +0.71€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 403 | +0.446 | +5.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 403 | +0.446 | +5.16€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1464 | +0.073 | -55.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 548 | +0.064 | -35.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 916 | +0.078 | -19.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 69 | +0.106 | +2.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 69 | +0.106 | +2.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1134 | +0.079 | -23.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 218 | +0.082 | -3.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 916 | +0.078 | -19.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 261 | +0.036 | -34.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 261 | +0.036 | -34.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 53598 | +0.100 | -1354.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 4340 | +0.094 | +71.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 49258 | +0.101 | -1426.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 29605 | +0.105 | -303.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 4340 | +0.094 | +71.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 25265 | +0.107 | -375.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 10824 | +0.109 | -44.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 10824 | +0.109 | -44.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 13169 | +0.081 | -1005.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 13169 | +0.081 | -1005.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 883 | +0.197 | -111.73€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 883 | +0.197 | -111.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 883 | +0.197 | -111.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 883 | +0.197 | -111.73€ | 2 | 4 |
| ✅ GBM_LATE_15M | 37055 | +0.091 | +18849.60€ | 0 | 15 |
| ✅ GBM_LATE_15M#15min | 37055 | +0.091 | +18849.60€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 6222 | +0.208 | +4919.25€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 6222 | +0.208 | +4919.25€ | 0 | 20 |
| ✅ GBM_LATE_15M#BTC | 5505 | +0.180 | +4087.73€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 5505 | +0.180 | +4087.73€ | 0 | 23 |
| ✅ GBM_LATE_15M#DOGE | 6610 | +0.203 | +5076.03€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 6610 | +0.203 | +5076.03€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 5203 | +0.039 | +1378.15€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 5203 | +0.039 | +1378.15€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 5287 | -0.030 | +1169.62€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 5287 | -0.030 | +1169.62€ | 3 | 11 |
| ✅ GBM_LATE_15M#XRP | 8228 | -0.035 | +2218.81€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 8228 | -0.035 | +2218.81€ | 3 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 40089 | +0.086 | +21551.38€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 40089 | +0.086 | +21551.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 7733 | +0.007 | +4035.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 7733 | +0.007 | +4035.65€ | 3 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 8422 | +0.013 | +1869.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 8422 | +0.013 | +1869.65€ | 0 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 5614 | +0.272 | +5896.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 5614 | +0.272 | +5896.08€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 7002 | +0.013 | +1634.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 7002 | +0.013 | +1634.49€ | 1 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 6473 | +0.037 | +2607.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 6473 | +0.037 | +2607.85€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 4845 | +0.294 | +5507.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 4845 | +0.294 | +5507.66€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 29482 | +0.177 | +23388.87€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 29482 | +0.177 | +23388.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 4479 | +0.221 | +3817.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 4479 | +0.221 | +3817.96€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 4628 | +0.151 | +3401.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 4628 | +0.151 | +3401.28€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 4705 | +0.219 | +3966.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 4705 | +0.219 | +3966.35€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 4964 | +0.139 | +3751.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 4964 | +0.139 | +3751.35€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 5546 | +0.123 | +4048.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 5546 | +0.123 | +4048.86€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 5160 | +0.220 | +4403.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 5160 | +0.220 | +4403.07€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 7942 | +0.138 | +3856.61€ | 0 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 7942 | +0.138 | +3856.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 358 | +0.144 | +211.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 358 | +0.144 | +211.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2410 | +0.148 | +1368.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2410 | +0.148 | +1368.32€ | 0 | 24 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 413 | +0.146 | +201.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 413 | +0.146 | +201.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2413 | +0.148 | +1176.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2413 | +0.148 | +1176.67€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1809 | +0.108 | +657.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1809 | +0.108 | +657.88€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 539 | +0.134 | +240.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 539 | +0.134 | +240.28€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO | 37257 | +0.183 | +29246.33€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 37257 | +0.183 | +29246.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 5927 | +0.234 | +5355.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 5927 | +0.234 | +5355.71€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 5753 | +0.149 | +3846.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 5753 | +0.149 | +3846.03€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 6278 | +0.230 | +5546.69€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 6278 | +0.230 | +5546.69€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 6094 | +0.139 | +4329.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 6094 | +0.139 | +4329.40€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 6602 | +0.122 | +4514.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 6602 | +0.122 | +4514.35€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 6603 | +0.223 | +5654.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 6603 | +0.223 | +5654.16€ | 0 | 21 |
| ✅ GBM_LATE_5M | 10333 | +0.190 | +7557.81€ | 1 | 28 |
| ✅ GBM_LATE_5M#5min | 10333 | +0.190 | +7557.81€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 919 | +0.232 | +813.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 919 | +0.232 | +813.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2254 | +0.181 | +1722.49€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2254 | +0.181 | +1722.49€ | 0 | 28 |
| ✅ GBM_LATE_5M#DOGE | 1002 | +0.176 | +657.98€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1002 | +0.176 | +657.98€ | 0 | 18 |
| ✅ GBM_LATE_5M#ETH | 3135 | +0.191 | +2188.53€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3135 | +0.191 | +2188.53€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 1434 | +0.180 | +1031.02€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1434 | +0.180 | +1031.02€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1589 | +0.195 | +1143.79€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1589 | +0.195 | +1143.79€ | 0 | 0 |
| ✅ GBM_LATE_60M | 2892 | +0.067 | +988.73€ | 0 | 9 |
| ✅ GBM_LATE_60M#60min | 2892 | +0.067 | +988.73€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1083 | +0.086 | +386.26€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1083 | +0.086 | +386.26€ | 0 | 10 |
| ✅ GBM_LATE_60M#ETH | 918 | +0.069 | +358.43€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 918 | +0.069 | +358.43€ | 0 | 11 |
| ✅ GBM_LATE_60M#SOL | 891 | +0.043 | +244.03€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 891 | +0.043 | +244.03€ | 1 | 14 |
| 🚫 GBM_LATE_60M_FADE | 513 | -0.242 | -19.32€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 513 | -0.242 | -19.32€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 194 | -0.235 | -11.07€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 194 | -0.235 | -11.07€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 181 | -0.221 | -1.28€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 181 | -0.221 | -1.28€ | 5 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 138 | -0.271 | -6.96€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 138 | -0.271 | -6.96€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1311 | +0.086 | +338.09€ | 0 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1311 | +0.086 | +338.09€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 504 | +0.083 | +103.83€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 504 | +0.083 | +103.83€ | 1 | 14 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 480 | +0.062 | +81.05€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 480 | +0.062 | +81.05€ | 1 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 327 | +0.126 | +153.22€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 327 | +0.126 | +153.22€ | 1 | 13 |
| ✅ LATE_WINDOW_5MIN | 141 | +0.255 | +122.89€ | 0 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 141 | +0.255 | +122.89€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 141 | +0.255 | +122.89€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 141 | +0.255 | +122.89€ | 0 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 3111 | +0.100 | +774.90€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 3111 | +0.100 | +774.90€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 3111 | +0.100 | +774.90€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 3111 | +0.100 | +774.90€ | 0 | 1 |
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
| ✅ LIQUIDACIONES_5M | 3297 | +0.020 | +87.31€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3297 | +0.020 | +87.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 161 | +0.015 | -3.70€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 161 | +0.015 | -3.70€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 591 | +0.031 | +44.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 591 | +0.031 | +44.04€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 203 | -0.017 | -5.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 203 | -0.017 | -5.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1179 | +0.033 | +36.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1179 | +0.033 | +36.00€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 744 | +0.011 | +0.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 744 | +0.011 | +0.71€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 419 | +0.006 | +15.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 419 | +0.006 | +15.34€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1550 | -0.042 | -27.54€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1550 | -0.042 | -27.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 438 | -0.036 | -12.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 438 | -0.036 | -12.50€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 520 | -0.017 | +4.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 520 | -0.017 | +4.37€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 592 | -0.067 | -19.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 592 | -0.067 | -19.41€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 6328 | -0.023 | +37.21€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 3015 | -0.031 | -33.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 3313 | -0.016 | +70.44€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 182 | -0.011 | +6.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 89 | +0.038 | +12.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 93 | -0.058 | -6.17€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 1574 | -0.013 | +31.68€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 754 | -0.017 | +4.10€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 820 | -0.009 | +27.58€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 706 | -0.025 | +5.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 359 | -0.040 | -8.65€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 347 | -0.010 | +14.11€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 1307 | -0.036 | -39.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 606 | -0.054 | -46.58€ | 3 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 701 | -0.021 | +6.78€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 1243 | -0.019 | +21.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 599 | -0.024 | +8.70€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 644 | -0.014 | +13.06€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 1316 | -0.027 | +11.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 608 | -0.034 | -3.62€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 708 | -0.021 | +15.06€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 43346 | -0.002 | +2091.95€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 43346 | -0.002 | +2091.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 7757 | +0.026 | +1015.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 7757 | +0.026 | +1015.47€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 6355 | -0.034 | -117.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 6355 | -0.034 | -117.10€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 7877 | +0.022 | +773.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 7877 | +0.022 | +773.23€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 6186 | -0.049 | -163.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 6186 | -0.049 | -163.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 7315 | -0.005 | +240.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 7315 | -0.005 | +240.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 7856 | +0.014 | +343.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 7856 | +0.014 | +343.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6364 | -0.060 | -157.10€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6364 | -0.060 | -157.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1222 | +0.000 | -14.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1222 | +0.000 | -14.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1615 | -0.078 | -39.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1615 | -0.078 | -39.03€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 53 | -0.064 | -2.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 53 | -0.064 | -2.93€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 743 | -0.121 | -32.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 743 | -0.121 | -32.92€ | 4 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 108238 | -0.074 | +1740.84€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 108238 | -0.074 | +1740.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 18708 | -0.075 | +993.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 18708 | -0.075 | +993.41€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 16364 | -0.099 | -898.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 16364 | -0.099 | -898.31€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 18984 | -0.066 | +1085.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 18984 | -0.066 | +1085.09€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 15903 | -0.095 | -480.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 15903 | -0.095 | -480.57€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 19510 | -0.053 | +386.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 19510 | -0.053 | +386.32€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 18769 | -0.065 | +654.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 18769 | -0.065 | +654.89€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8568 | -0.033 | -176.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8568 | -0.033 | -176.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1960 | -0.045 | -21.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1960 | -0.045 | -21.69€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2563 | -0.027 | -44.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2563 | -0.027 | -44.16€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1143 | -0.049 | -23.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1143 | -0.049 | -23.05€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 898 | -0.032 | -35.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 898 | -0.032 | -35.07€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1502 | +0.121 | +596.22€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#5min | 1366 | +0.127 | +583.63€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 322 | +0.148 | +175.84€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 322 | +0.148 | +175.84€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 270 | +0.110 | +83.77€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 270 | +0.110 | +83.77€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#ETH | 274 | +0.127 | +122.07€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 274 | +0.127 | +122.07€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 243 | +0.149 | +130.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 243 | +0.149 | +130.57€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 257 | +0.095 | +71.38€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 257 | +0.095 | +71.38€ | 0 | 4 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1168 | -0.020 | -23.85€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1168 | -0.020 | -23.85€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 227 | -0.015 | +0.27€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 227 | -0.015 | +0.27€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 195 | -0.008 | +3.91€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 195 | -0.008 | +3.91€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 300 | -0.040 | -20.44€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 300 | -0.040 | -20.44€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 245 | -0.002 | -1.65€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 245 | -0.002 | -1.65€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 201 | -0.027 | -5.93€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 201 | -0.027 | -5.93€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 829 | -0.070 | -36.17€ | 3 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 382 | -0.120 | -76.52€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 293 | -0.154 | -66.73€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 89 | -0.005 | -9.80€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 295 | -0.032 | +27.22€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 209 | -0.026 | +27.73€ | 2 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 86 | -0.045 | -0.50€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 152 | -0.019 | +13.13€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 122 | -0.024 | +8.23€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 30 | +0.000 | +4.90€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 624 | -0.086 | -30.77€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 205 | -0.022 | -5.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 995 | -0.206 | -51.65€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 405 | -0.205 | -36.64€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 349 | -0.209 | -36.92€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 56 | -0.172 | +0.28€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 338 | -0.215 | -28.27€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 292 | -0.225 | -33.96€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 46 | -0.146 | +5.69€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 252 | -0.193 | +13.26€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 233 | -0.189 | +10.12€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 19 | -0.204 | +3.14€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 874 | -0.210 | -60.77€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 121 | -0.175 | +9.11€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 414 | +0.397 | +398.12€ | 0 | 13 |
| ✅ RESOLUTION_SNIPER#BTC | 53 | +0.118 | +46.13€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 53 | +0.118 | +46.13€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 104 | +0.377 | +93.44€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 104 | +0.377 | +93.44€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 257 | +0.458 | +258.55€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 257 | +0.458 | +258.55€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 414 | +0.397 | +398.12€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 666 | +0.030 | +31.51€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 666 | +0.030 | +31.51€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 296 | +0.024 | +3.43€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 296 | +0.024 | +3.43€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 53 | -0.027 | -5.65€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 53 | -0.027 | -5.65€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 69 | -0.007 | -0.06€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 69 | -0.007 | -0.06€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 248 | +0.060 | +33.78€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 248 | +0.060 | +33.78€ | 0 | 5 |
| ✅ STREAK_FADE_5M | 3364 | -0.021 | -129.05€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3364 | -0.021 | -129.05€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1051 | -0.022 | -37.52€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1051 | -0.022 | -37.52€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 586 | -0.025 | -25.10€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 586 | -0.025 | -25.10€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 160 | -0.043 | -14.37€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 160 | -0.043 | -14.37€ | 3 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1567 | -0.016 | -52.06€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1567 | -0.016 | -52.06€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 94 | -0.052 | -9.37€ | 4 | 0 |
| ✅ STREAK_FADE_60M#60min | 94 | -0.052 | -9.37€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 39 | -0.085 | -3.98€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 39 | -0.085 | -3.98€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 55 | -0.026 | -5.39€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 55 | -0.026 | -5.39€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 10245 | +0.018 | +104.39€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 10245 | +0.018 | +104.39€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2648 | +0.021 | +27.27€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2648 | +0.021 | +27.27€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2596 | +0.022 | +42.47€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2596 | +0.022 | +42.47€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2882 | +0.009 | -2.09€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2882 | +0.009 | -2.09€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2119 | +0.023 | +36.74€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2119 | +0.023 | +36.74€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 9328 | +0.013 | -43.86€ | 1 | 0 |
| ✅ STRUCT_NO_15M#15min | 9328 | +0.013 | -43.86€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3716 | +0.019 | -2.48€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3716 | +0.019 | -2.48€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3603 | +0.011 | -28.25€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3603 | +0.011 | -28.25€ | 1 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2009 | +0.009 | -13.13€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2009 | +0.009 | -13.13€ | 1 | 0 |
| ✅ UPDOWN_GBM | 67808 | +0.052 | +5886.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 16890 | +0.085 | +3834.11€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 2233 | +0.006 | +13.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 44602 | +0.046 | +1977.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 3855 | +0.008 | +63.35€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6818 | +0.089 | +1072.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1543 | +0.158 | +694.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 77 | -0.006 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5198 | +0.070 | +378.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 13595 | +0.054 | +1133.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2094 | +0.091 | +508.53€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 572 | +0.012 | +7.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 9126 | +0.058 | +568.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1720 | +0.006 | +46.27€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 83 | -0.076 | +2.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 8043 | +0.066 | +843.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1529 | +0.149 | +607.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 78 | +0.013 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 6436 | +0.047 | +237.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 14953 | +0.042 | +917.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 3885 | +0.062 | +548.19€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 566 | +0.009 | +9.78€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 9112 | +0.041 | +345.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1314 | +0.011 | +10.82€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 76 | -0.103 | +2.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 14890 | +0.029 | +636.53€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 4043 | +0.035 | +344.92€ | 0 | 8 |
| ✅ UPDOWN_GBM#SOL#240min | 552 | -0.004 | -1.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 9407 | +0.031 | +291.50€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 821 | +0.007 | +6.27€ | 0 | 2 |
| ✅ UPDOWN_GBM#SOL#daily | 67 | -0.138 | -5.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 9507 | +0.062 | +1285.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 3796 | +0.103 | +1130.42€ | 0 | 10 |
| ✅ UPDOWN_GBM#XRP#240min | 388 | +0.010 | -0.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 5323 | +0.036 | +154.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 226 | -0.105 | +0.17€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 768 | +0.364 | +276.14€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 768 | +0.364 | +276.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 409 | +0.361 | +139.61€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 409 | +0.361 | +139.61€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 359 | +0.364 | +136.52€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 359 | +0.364 | +136.52€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 18105 | -0.024 | +4383.36€ | 3 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 18105 | -0.024 | +4383.36€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1674 | -0.056 | +500.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1674 | -0.056 | +500.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 3082 | -0.110 | +135.60€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 3082 | -0.110 | +135.60€ | 5 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 926 | +0.220 | +767.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 926 | +0.220 | +767.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2100 | +0.215 | +1344.63€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2100 | +0.215 | +1344.63€ | 1 | 22 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 5139 | -0.063 | +698.42€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 5139 | -0.063 | +698.42€ | 3 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5184 | -0.064 | +936.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5184 | -0.064 | +936.25€ | 4 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 201 | +0.037 | +7.46€ | 0 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 201 | +0.037 | +7.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 201 | +0.037 | +7.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 201 | +0.037 | +7.46€ | 0 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1276 | +0.292 | +1072.13€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1276 | +0.292 | +1072.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 691 | +0.286 | +542.54€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 691 | +0.286 | +542.54€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 585 | +0.297 | +529.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 585 | +0.297 | +529.59€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 791 | -0.112 | -82.03€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#5min | 791 | -0.112 | -82.03€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 237 | -0.086 | -18.43€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 237 | -0.086 | -18.43€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 84 | -0.151 | -7.62€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 84 | -0.151 | -7.62€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 87 | -0.185 | -6.62€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 87 | -0.185 | -6.62€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 3240 | +0.303 | +1556.41€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1176 | +0.255 | +157.29€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1242 | +0.297 | +548.00€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 822 | +0.379 | +851.11€ | 0 | 1 |