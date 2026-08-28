# Hipótesis automáticas — 2026-08-28 23:56 UTC
_Generado por shadow_postmortem.py sobre 194512 resoluciones (PNL=+14572.69€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.705` → IC=-0.167 (n=88)

  - _Acción_: SKIP cuando `py_entrada` < 0.705
  - _Potencial_: sin este filtro IC_bueno=+0.274 (n=264)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.284 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.164)

- **PATRÓN** `n_ballena_banda` > `16.0` → IC=+0.176 (n=270)

  - _Acción_: Kelly boost +0.88€ cuando `n_ballena_banda` > 16.0 (IC base=+0.164)

- **PATRÓN** `n_total_lado` > `58.0` → IC=+0.243 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 58.0 (IC base=+0.164)

- **PATRÓN** `banda_hit_calibrado` > `0.8178` → IC=+0.292 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8178 (IC base=+0.164)

- **PATRÓN** `banda_z` > `11.481` → IC=+0.289 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.481 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.188 (n=238)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 7.0 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.188 (n=277)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.01 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `3103.76` → IC=+0.238 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3103.76 (IC base=+0.164)

- **PATRÓN** `ballena_activa_n` < `237.0` → IC=+0.294 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 237.0 (IC base=+0.164)

- **PATRÓN** `py_entrada` < `0.835` → IC=+0.123 (n=221)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.835 (IC base=+0.000)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.123 (n=51)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=109)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.283 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.204)

- **PATRÓN** `n_ballena_banda` > `19.0` → IC=+0.217 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `n_ballena_banda` > 19.0 (IC base=+0.204)

- **PATRÓN** `n_total_lado` > `51.0` → IC=+0.244 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 51.0 (IC base=+0.204)

- **PATRÓN** `banda_hit_calibrado` > `0.8194` → IC=+0.305 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8194 (IC base=+0.204)

- **PATRÓN** `banda_z` > `11.806` → IC=+0.290 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.806 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.233 (n=155)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.216 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `3103.76` → IC=+0.237 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3103.76 (IC base=+0.204)

- **PATRÓN** `ballena_activa_n` < `259.0` → IC=+0.321 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 259.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.126 (n=113)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.495 (IC base=-0.018)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.335` → IC=-0.267 (n=28)

  - _Acción_: SKIP cuando `py_entrada` < 0.335
  - _Potencial_: sin este filtro IC_bueno=+0.195 (n=93)

- **FILTRO** `banda_hit_calibrado` < `0.6329` → IC=-0.232 (n=39)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6329
  - _Potencial_: sin este filtro IC_bueno=+0.238 (n=82)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=97)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.353 (n=32)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.134 (n=69)

- **FILTRO** `n_ballena_banda` < `30.0` → IC=-0.128 (n=49)

  - _Acción_: SKIP cuando `n_ballena_banda` < 30.0
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=52)

- **FILTRO** `hora_utc` < `11.0` → IC=-0.125 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=71)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=86)

- **PATRÓN** `py_entrada` > `0.335` → IC=+0.195 (n=93)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.335 (IC base=+0.085)

- **PATRÓN** `banda_hit_calibrado` > `0.6329` → IC=+0.238 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6329 (IC base=+0.085)

- **PATRÓN** `banda_z` > `8.441` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `banda_z` > 8.441 (IC base=+0.085)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.146 (n=97)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.02 (IC base=+0.085)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.495 (IC base=-0.024)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `147.84` → IC=-0.286 (n=2719)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 147.84
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=8158)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `133.5` → IC=-0.274 (n=343)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 133.5
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=1032)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `n_ballenas` < `8.0` → IC=-0.122 (n=239)

  - _Acción_: SKIP cuando `n_ballenas` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=527)

- **FILTRO** `restante_s_al_confirmar` > `626.37` → IC=-0.171 (n=259)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` > 626.37
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=507)

- **FILTRO** `restante_s_al_confirmar` < `409.18` → IC=-0.215 (n=191)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 409.18
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=575)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `115.59` → IC=-0.389 (n=349)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 115.59
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=1052)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `161.11` → IC=-0.156 (n=730)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 161.11
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=2193)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `141.52` → IC=-0.309 (n=632)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 141.52
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=1896)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `156.16` → IC=-0.351 (n=621)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 156.16
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=1263)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.7` → IC=+0.190 (n=5884)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.7 (IC base=+0.096)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.170 (n=1688)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.01 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `2376.0723` → IC=+0.172 (n=1624)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2376.0723 (IC base=+0.096)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.149 (n=3578)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 18.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.160 (n=4660)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 7.0 (IC base=+0.143)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.258 (n=3711)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.190 (n=3133)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.02 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `1910.9996` → IC=+0.183 (n=2627)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 1910.9996 (IC base=+0.143)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.221 (n=703)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` > `0.785` → IC=+0.388 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.785 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.207 (n=861)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.197 (n=629)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 7.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.196 (n=693)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 17.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` < `0.365` → IC=+0.259 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.365 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.189 (n=889)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.01 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `12906.7905` → IC=+0.232 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12906.7905 (IC base=+0.189)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.129 (n=567)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.116)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.131 (n=483)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 15.0 (IC base=+0.116)

- **PATRÓN** `py_entrada` > `0.555` → IC=+0.132 (n=560)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` > 0.555 (IC base=+0.116)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=262)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `4886.5239` → IC=+0.157 (n=208)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 4886.5239 (IC base=+0.116)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.191 (n=189)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 7.0 (IC base=+0.132)

- **PATRÓN** `py_entrada` < `0.415` → IC=+0.174 (n=311)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.415 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `4171.1992` → IC=+0.149 (n=294)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 4171.1992 (IC base=+0.132)

### FAVORITO_CONFIRMADO#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.135 (n=1320)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.128 (n=1107)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 15.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` > `0.69` → IC=+0.316 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.277 (n=460)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.276)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.279 (n=510)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.276)

- **PATRÓN** `py_entrada` < `0.195` → IC=+0.408 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.195 (IC base=+0.276)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.277 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.276)

- **PATRÓN** `libro_liquidez` > `4383.8031` → IC=+0.289 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4383.8031 (IC base=+0.276)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.136 (n=341)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.153 (n=289)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 15.0 (IC base=+0.136)

- **PATRÓN** `py_entrada` > `0.655` → IC=+0.256 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.655 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.146 (n=399)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.02 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `1928.4949` → IC=+0.157 (n=327)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 1928.4949 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `4420.281` → IC=+0.157 (n=141)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 4420.281 (IC base=+0.080)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.196 (n=992)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 6.0 (IC base=+0.186)

- **PATRÓN** `py_entrada` > `0.84` → IC=+0.444 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.84 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.244 (n=244)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.223 (n=316)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` < `0.205` → IC=+0.356 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.205 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.226 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `1955.3934` → IC=+0.241 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1955.3934 (IC base=+0.221)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.222 (n=95)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.347 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.185)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.230 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.185)

- **PATRÓN** `py_entrada` < `0.415` → IC=+0.152 (n=435)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` < 0.415 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.147 (n=276)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.02 (IC base=+0.105)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `9.0` → IC=-0.286 (n=82)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=86)

- **FILTRO** `py_entrada` > `0.84` → IC=-0.360 (n=41)

  - _Acción_: SKIP cuando `py_entrada` > 0.84
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=127)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.195 (n=4895)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.191 (n=4125)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.201 (n=2315)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.188)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.169 (n=1196)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 6.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.177 (n=1060)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 15.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` < `0.72` → IC=+0.177 (n=1059)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.72 (IC base=+0.167)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `12.0` → IC=-0.375 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.225 (n=67)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=67)

- **FILTRO** `libro_liquidez` < `11307.5209` → IC=-0.350 (n=58)

  - _Acción_: SKIP cuando `libro_liquidez` < 11307.5209
  - _Potencial_: sin este filtro IC_bueno=-0.106 (n=31)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.420 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.324)

- **PATRÓN** `py_entrada` > `0.845` → IC=+0.372 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.845 (IC base=+0.324)

- **PATRÓN** `libro_liquidez` > `2916.5858` → IC=+0.343 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2916.5858 (IC base=+0.324)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.173 (n=1185)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 6.0 (IC base=+0.166)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.171 (n=1040)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 15.0 (IC base=+0.166)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.173 (n=450)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` < 0.7 (IC base=+0.166)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.174 (n=821)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` > 0.72 (IC base=+0.166)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.243 (n=1117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.232)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.322 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.232)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.194 (n=1199)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.183 (n=1017)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 15.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.188 (n=1188)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.73 (IC base=+0.183)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.459 (n=216)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.447)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.446 (n=218)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.447)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.453 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.447)

- **PATRÓN** `libro_liquidez` > `3363.9486` → IC=+0.463 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3363.9486 (IC base=+0.447)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.449 (n=95)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.444)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.441 (n=83)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.444)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.446 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.444)

- **PATRÓN** `libro_liquidez` > `13751.4585` → IC=+0.455 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13751.4585 (IC base=+0.444)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.456 (n=88)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.434)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.436 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.434)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.432 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.434)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.432 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.434)

- **PATRÓN** `libro_liquidez` > `3806.2335` → IC=+0.477 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3806.2335 (IC base=+0.434)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.443 (n=51)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.448)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.451 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.448)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.451 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.448)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.442 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.448)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.206 (n=4617)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.219 (n=9915)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.191)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.137 (n=2505)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 6.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.132 (n=1763)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 12.0 (IC base=+0.131)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.159 (n=1686)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` > 0.72 (IC base=+0.131)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.240 (n=2168)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.234)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.281 (n=1218)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.234)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.201 (n=791)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.205 (n=1121)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.168)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.233 (n=1988)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.226)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.289 (n=760)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.226)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.228 (n=755)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.212)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.249 (n=1017)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.212)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.194 (n=782)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 18.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.193 (n=1621)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 12.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.223 (n=1134)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.185)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.203 (n=1804)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.133)

- **PATRÓN** `restante_min` < `3.98` → IC=+0.133 (n=1678)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` < 3.98 (IC base=+0.133)

- **PATRÓN** `restante_min` > `4.93` → IC=+0.159 (n=1791)

  - _Acción_: Kelly boost +0.79€ cuando `restante_min` > 4.93 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.151 (n=2423)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 8.0 (IC base=+0.133)

- **PATRÓN** `lag_apertura_s` < `4.22` → IC=+0.160 (n=1670)

  - _Acción_: Kelly boost +0.80€ cuando `lag_apertura_s` < 4.22 (IC base=+0.133)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.208 (n=913)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.139)

- **PATRÓN** `restante_min` < `3.94` → IC=+0.140 (n=833)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` < 3.94 (IC base=+0.139)

- **PATRÓN** `restante_min` > `4.88` → IC=+0.155 (n=1152)

  - _Acción_: Kelly boost +0.78€ cuando `restante_min` > 4.88 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.165 (n=1200)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 8.0 (IC base=+0.139)

- **PATRÓN** `lag_apertura_s` < `7.04` → IC=+0.158 (n=1098)

  - _Acción_: Kelly boost +0.79€ cuando `lag_apertura_s` < 7.04 (IC base=+0.139)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.198 (n=891)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.38 (IC base=+0.127)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.168 (n=938)

  - _Acción_: Kelly boost +0.84€ cuando `restante_min` > 4.94 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.130 (n=2526)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 6.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.137 (n=1223)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 8.0 (IC base=+0.127)

- **PATRÓN** `lag_apertura_s` < `3.37` → IC=+0.174 (n=841)

  - _Acción_: Kelly boost +0.87€ cuando `lag_apertura_s` < 3.37 (IC base=+0.127)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.315 (n=545)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.296)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.300 (n=632)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.296)

- **PATRÓN** `py_entrada` > `0.825` → IC=+0.376 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.825 (IC base=+0.296)

- **PATRÓN** `libro_liquidez` > `3875.4788` → IC=+0.299 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3875.4788 (IC base=+0.296)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.305 (n=234)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.281)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.280 (n=239)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.281)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.353 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.281)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.285 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `5679.4122` → IC=+0.322 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5679.4122 (IC base=+0.281)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.328 (n=202)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.298)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.308 (n=290)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.298)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.374 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.298)

- **PATRÓN** `libro_liquidez` > `1843.456` → IC=+0.312 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1843.456 (IC base=+0.298)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `12.0` → IC=+0.337 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.339)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.346 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.339)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.371 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.339)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.355 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.339)

- **PATRÓN** `libro_liquidez` > `761.0655` → IC=+0.364 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 761.0655 (IC base=+0.339)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.428 (n=275)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.414)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.420 (n=262)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.414)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.421 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.414)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.424 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.414)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.416 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.414)

- **PATRÓN** `libro_liquidez` > `2076.1143` → IC=+0.428 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2076.1143 (IC base=+0.414)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.424 (n=117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.410)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.424 (n=116)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.410)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.415 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.410)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.418 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.410)

- **PATRÓN** `libro_liquidez` > `5536.1709` → IC=+0.451 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5536.1709 (IC base=+0.410)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.430 (n=112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.420)

- **PATRÓN** `hora_utc` < `19.0` → IC=+0.418 (n=132)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 19.0 (IC base=+0.420)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.438 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.420)

- **PATRÓN** `py_entrada` > `0.91` → IC=+0.422 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.91 (IC base=+0.420)

- **PATRÓN** `libro_liquidez` > `2081.2854` → IC=+0.451 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2081.2854 (IC base=+0.420)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.307 (n=319)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.284)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.443 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.300 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.284)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.307 (n=319)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.284)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.443 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.300 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.284)

### GBM_LATE_15M
- **PATRÓN** `ibs_20min` > `0.9504` → IC=+0.210 (n=842)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9504 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` > `0.211` → IC=+0.229 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.211 (IC base=+0.064)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.268` → IC=+0.157 (n=1008)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 5.268 (IC base=+0.064)

- **PATRÓN** `volumen_regimen` < `0.627` → IC=+0.214 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.627 (IC base=+0.064)

- **PATRÓN** `volumen_regimen` > `1.067` → IC=+0.233 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.067 (IC base=+0.064)

- **PATRÓN** `volumen_pendiente_norm` > `0.3083` → IC=+0.153 (n=197)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.3083 (IC base=+0.064)

- **PATRÓN** `volumen_spike_ratio` < `2.423` → IC=+0.150 (n=1223)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.423 (IC base=+0.064)

- **PATRÓN** `ibs_20min` < `0.1163` → IC=+0.151 (n=1290)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.1163 (IC base=+0.031)

- **PATRÓN** `dist_vwap_pct` < `0.3233` → IC=+0.145 (n=896)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.3233 (IC base=+0.031)

- **PATRÓN** `volumen_regimen` < `0.6829` → IC=+0.159 (n=370)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.6829 (IC base=+0.031)

- **PATRÓN** `volumen_regimen` > `1.0483` → IC=+0.140 (n=381)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 1.0483 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.3085` → IC=+0.274 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3085 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` > `2.9153` → IC=+0.240 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9153 (IC base=+0.031)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.237 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.031)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.195 (n=188)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0075 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.169 (n=267)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 8.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.286 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.973` → IC=+0.319 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.973 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2159` → IC=+0.160 (n=92)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.2159 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.160 (n=374)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.04 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `60.0` → IC=+0.137 (n=210)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 60.0 (IC base=+0.129)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.263 (n=222)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.255)

- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.288 (n=111)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0074 (IC base=+0.255)

- **PATRÓN** `drift_60min` |x|≤ `0.0753` → IC=+0.323 (n=111)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0753 (IC base=+0.255)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.254 (n=299)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.255)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.267 (n=230)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.255)

- **PATRÓN** `ibs_20min` < `0.4216` → IC=+0.292 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4216 (IC base=+0.255)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.934` → IC=+0.282 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.934 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` < `0.0668` → IC=+0.246 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0668 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` > `0.3058` → IC=+0.311 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3058 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` < `1.88` → IC=+0.265 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.88 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` > `2.8103` → IC=+0.305 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8103 (IC base=+0.255)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.301 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `1952.5048` → IC=+0.296 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1952.5048 (IC base=+0.255)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.263 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.255)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.217 (n=288)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.201)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.210 (n=143)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.0936` → IC=+0.231 (n=143)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0936 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=436)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` > `0.4091` → IC=+0.223 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4091 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `0.3145` → IC=+0.233 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3145 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.354` → IC=+0.223 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.354 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` < `0.6916` → IC=+0.212 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6916 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` > `1.0826` → IC=+0.235 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0826 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` < `0.0952` → IC=+0.203 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0952 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.2681` → IC=+0.207 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2681 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` < `1.4526` → IC=+0.256 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4526 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `11693.3416` → IC=+0.213 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11693.3416 (IC base=+0.201)

- **PATRÓN** `sigma_h` < `0.0023` → IC=+0.157 (n=164)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0023 (IC base=+0.144)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.144 (n=223)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0049 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.0775` → IC=+0.157 (n=164)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.0775 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.153 (n=465)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 7.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.154 (n=518)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 18.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.4406` → IC=+0.181 (n=431)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.4406 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` < `0.1451` → IC=+0.171 (n=426)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1451 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.912` → IC=+0.228 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.912 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `0.6207` → IC=+0.187 (n=164)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.6207 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `1.0176` → IC=+0.144 (n=223)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.0176 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.0711` → IC=+0.207 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0711 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.7604` → IC=+0.169 (n=258)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.7604 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.4122` → IC=+0.170 (n=386)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.4122 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.145 (n=634)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `13934.8453` → IC=+0.193 (n=223)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 13934.8453 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `221.0` → IC=+0.173 (n=99)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 221.0 (IC base=+0.144)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.203 (n=230)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0078 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.218 (n=179)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.273 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.02` → IC=+0.275 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.02 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` < `0.2295` → IC=+0.136 (n=438)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` < 0.2295 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.4138` → IC=+0.135 (n=61)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.4138 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `2.546` → IC=+0.140 (n=284)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.546 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.6927` → IC=+0.140 (n=426)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.6927 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.172 (n=465)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.04 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.171 (n=171)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 40.0 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0097` → IC=+0.263 (n=390)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0097 (IC base=+0.249)

- **PATRÓN** `drift_60min` |x|≤ `0.4646` → IC=+0.260 (n=390)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4646 (IC base=+0.249)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.252 (n=272)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.249)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.262 (n=402)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.249)

- **PATRÓN** `ibs_20min` < `0.5294` → IC=+0.287 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5294 (IC base=+0.249)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.047` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.047 (IC base=+0.249)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.873` → IC=+0.252 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.873 (IC base=+0.249)

- **PATRÓN** `volumen_pendiente_norm` > `0.3948` → IC=+0.427 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3948 (IC base=+0.249)

- **PATRÓN** `volumen_spike_ratio` > `2.5785` → IC=+0.250 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5785 (IC base=+0.249)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.281 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.249)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.225 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 52.0 (IC base=+0.249)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.141 (n=126)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=379)

- **FILTRO** `ibs_20min` < `0.2846` → IC=-0.131 (n=166)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2846
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=339)

- **FILTRO** `ibs_20min` > `0.8686` → IC=-0.173 (n=221)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8686
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=668)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.172 (n=65)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=824)

- **PATRÓN** `dist_vwap_pct` > `0.124` → IC=+0.300 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.124 (IC base=-0.042)

- **PATRÓN** `volumen_regimen` < `0.6297` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6297 (IC base=-0.042)

- **PATRÓN** `volumen_regimen` > `0.7026` → IC=+0.267 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7026 (IC base=-0.042)

- **PATRÓN** `volumen_pendiente_norm` < `0.114` → IC=+0.235 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.114 (IC base=-0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.2199` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2199 (IC base=-0.042)

- **PATRÓN** `volumen_spike_ratio` < `1.4292` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4292 (IC base=-0.042)

- **PATRÓN** `volumen_spike_ratio` > `1.8068` → IC=+0.242 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8068 (IC base=-0.042)

- **PATRÓN** `ballena_activa_n` < `111.0` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 111.0 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` > `0.2864` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.2864 (IC base=-0.050)

- **PATRÓN** `volumen_pendiente_norm` > `0.0733` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0733 (IC base=-0.050)

- **PATRÓN** `volumen_spike_ratio` > `2.3816` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.3816 (IC base=-0.050)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.147 (n=83)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 142.0 (IC base=-0.050)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.136 (n=31)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=100)

- **FILTRO** `ibs_20min` > `0.5` → IC=-0.135 (n=674)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=720)

- **FILTRO** `sigma_ewma_delta_pct` > `5.042` → IC=-0.157 (n=295)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.042
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=1099)

- **FILTRO** `volumen_pendiente_norm` < `0.0964` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.0964
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

- **FILTRO** `volumen_spike_ratio` > `1.6234` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.6234
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.157 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0056 (IC base=+0.034)

- **PATRÓN** `ibs_20min` > `0.6842` → IC=+0.223 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6842 (IC base=+0.034)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.5438` → IC=-0.159 (n=250)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.5438
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=488)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.198 (n=170)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=568)

- **FILTRO** `ibs_20min` > `0.7881` → IC=-0.173 (n=313)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7881
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=942)

- **FILTRO** `sigma_ewma_delta_pct` > `6.719` → IC=-0.150 (n=204)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.719
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=1051)

- **PATRÓN** `dist_vwap_pct` < `0.2396` → IC=+0.175 (n=38)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.2396 (IC base=-0.107)

- **PATRÓN** `volumen_regimen` > `0.6932` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 0.6932 (IC base=-0.107)

- **PATRÓN** `dist_vwap_pct` < `0.2072` → IC=+0.227 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2072 (IC base=-0.044)

- **PATRÓN** `volumen_regimen` < `0.6966` → IC=+0.230 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6966 (IC base=-0.044)

- **PATRÓN** `volumen_regimen` > `1.1383` → IC=+0.254 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1383 (IC base=-0.044)

- **PATRÓN** `volumen_pendiente_norm` > `0.0858` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0858 (IC base=-0.044)

- **PATRÓN** `volumen_spike_ratio` > `1.6969` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.6969 (IC base=-0.044)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.137 (n=1438)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.0078 (IC base=+0.053)

- **PATRÓN** `ibs_20min` > `0.9448` → IC=+0.246 (n=1057)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9448 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` > `1.3014` → IC=+0.291 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.3014 (IC base=+0.053)

- **PATRÓN** `volumen_regimen` > `1.1718` → IC=+0.212 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1718 (IC base=+0.053)

- **PATRÓN** `volumen_pendiente_norm` < `0.115` → IC=+0.179 (n=1430)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` < 0.115 (IC base=+0.053)

- **PATRÓN** `volumen_pendiente_norm` > `0.249` → IC=+0.200 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.249 (IC base=+0.053)

- **PATRÓN** `volumen_spike_ratio` < `1.4786` → IC=+0.205 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4786 (IC base=+0.053)

- **PATRÓN** `volumen_spike_ratio` > `2.8297` → IC=+0.178 (n=488)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 2.8297 (IC base=+0.053)

- **PATRÓN** `ballena_activa_n` < `97.0` → IC=+0.275 (n=913)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 97.0 (IC base=+0.053)

- **PATRÓN** `ibs_20min` < `0.0909` → IC=+0.195 (n=1292)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.0909 (IC base=+0.040)

- **PATRÓN** `dist_vwap_pct` > `0.8155` → IC=+0.219 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8155 (IC base=+0.040)

- **PATRÓN** `dist_vwap_pct` < `0.223` → IC=+0.214 (n=808)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.223 (IC base=+0.040)

- **PATRÓN** `volumen_regimen` < `0.8592` → IC=+0.213 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8592 (IC base=+0.040)

- **PATRÓN** `volumen_regimen` > `1.2272` → IC=+0.235 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2272 (IC base=+0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.2567` → IC=+0.358 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2567 (IC base=+0.040)

- **PATRÓN** `volumen_spike_ratio` > `2.3783` → IC=+0.283 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3783 (IC base=+0.040)

- **PATRÓN** `ballena_activa_n` < `60.0` → IC=+0.262 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 60.0 (IC base=+0.040)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2441` → IC=-0.165 (n=222)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2441
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=453)

- **FILTRO** `sigma_ewma_delta_pct` > `2.143` → IC=-0.172 (n=248)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.143
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=564)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.373` → IC=+0.177 (n=128)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 5.373 (IC base=-0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.211` → IC=+0.342 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.211 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` > `2.7084` → IC=+0.242 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7084 (IC base=-0.004)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.400 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 45.0 (IC base=-0.004)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.8836` → IC=-0.153 (n=292)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8836
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=880)

- **PATRÓN** `volumen_regimen` < `0.5584` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5584 (IC base=-0.043)

- **PATRÓN** `volumen_spike_ratio` < `1.6985` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6985 (IC base=-0.043)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.283 (n=228)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0078 (IC base=+0.192)

- **PATRÓN** `drift_60min` |x|≤ `0.0756` → IC=+0.216 (n=167)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0756 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.198 (n=167)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 18.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.257 (n=175)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.192)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.289 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.165` → IC=+0.300 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.165 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` < `0.1438` → IC=+0.203 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1438 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` < `2.52` → IC=+0.201 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.52 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` > `4.1701` → IC=+0.197 (n=140)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 4.1701 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.218 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `1934.9386` → IC=+0.204 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1934.9386 (IC base=+0.192)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.233 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.192)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.328 (n=259)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.322)

- **PATRÓN** `drift_60min` |x|≤ `0.5361` → IC=+0.324 (n=294)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5361 (IC base=+0.322)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.348 (n=202)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.322)

- **PATRÓN** `ibs_20min` < `0.3388` → IC=+0.342 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3388 (IC base=+0.322)

- **PATRÓN** `ibs_20min` > `0.1308` → IC=+0.323 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1308 (IC base=+0.322)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.598` → IC=+0.333 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.598 (IC base=+0.322)

- **PATRÓN** `volumen_pendiente_norm` > `0.3592` → IC=+0.414 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3592 (IC base=+0.322)

- **PATRÓN** `volumen_spike_ratio` < `1.7067` → IC=+0.314 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7067 (IC base=+0.322)

- **PATRÓN** `volumen_spike_ratio` > `1.9441` → IC=+0.324 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9441 (IC base=+0.322)

- **PATRÓN** `libro_liquidez` > `1869.9762` → IC=+0.370 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1869.9762 (IC base=+0.322)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.321 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 30.0 (IC base=+0.322)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `sigma_h` > `0.0066` → IC=-0.148 (n=123)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0066
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=381)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.173 (n=166)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=338)

- **FILTRO** `dist_vwap_pct` < `0.2815` → IC=-0.237 (n=36)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.2815
  - _Potencial_: sin este filtro IC_bueno=+0.176 (n=35)

- **FILTRO** `volumen_regimen` > `1.0041` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.0041
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=54)

- **FILTRO** `ibs_20min` > `0.8665` → IC=-0.137 (n=257)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8665
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=772)

- **FILTRO** `dist_vwap_pct` < `0.0964` → IC=-0.136 (n=53)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0964
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

- **FILTRO** `volumen_regimen` > `0.8819` → IC=-0.231 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8819
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=49)

- **FILTRO** `volumen_regimen` < `0.6828` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.6828
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=49)

- **FILTRO** `volumen_pendiente_norm` < `0.1167` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.1167
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=5)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.171 (n=68)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=961)

- **PATRÓN** `dist_vwap_pct` > `0.7343` → IC=+0.233 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7343 (IC base=-0.083)

- **PATRÓN** `volumen_spike_ratio` < `1.4` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4 (IC base=-0.083)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7455` → IC=-0.135 (n=466)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7455
  - _Potencial_: sin este filtro IC_bueno=+0.216 (n=241)

- **FILTRO** `ibs_20min` > `0.7551` → IC=-0.200 (n=231)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7551
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=694)

- **FILTRO** `dist_vwap_pct` > `0.1326` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1326
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=54)

- **FILTRO** `volumen_regimen` > `1.3339` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.3339
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=53)

- **FILTRO** `volumen_pendiente_norm` < `0.1028` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.1028
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=14)

- **FILTRO** `volumen_spike_ratio` < `2.1818` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 2.1818
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=12)

- **FILTRO** `ballena_activa_n` > `35.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `ballena_activa_n` > 35.0
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

- **PATRÓN** `ibs_20min` > `0.859` → IC=+0.271 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.859 (IC base=-0.015)

- **PATRÓN** `dist_vwap_pct` > `0.6608` → IC=+0.302 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6608 (IC base=-0.015)

- **PATRÓN** `volumen_regimen` < `0.8552` → IC=+0.186 (n=135)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.8552 (IC base=-0.015)

- **PATRÓN** `volumen_regimen` > `1.1437` → IC=+0.239 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1437 (IC base=-0.015)

- **PATRÓN** `volumen_pendiente_norm` < `0.1202` → IC=+0.179 (n=188)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` < 0.1202 (IC base=-0.015)

- **PATRÓN** `volumen_pendiente_norm` > `0.2306` → IC=+0.256 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2306 (IC base=-0.015)

- **PATRÓN** `volumen_spike_ratio` < `1.5512` → IC=+0.209 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5512 (IC base=-0.015)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.238 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 51.0 (IC base=-0.015)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0248` → IC=+0.328 (n=202)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0248 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.238 (n=235)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.231 (n=284)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.8915` → IC=+0.307 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8915 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `1.4364` → IC=+0.342 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.4364 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.201` → IC=+0.277 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.201 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `0.8361` → IC=+0.261 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8361 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` < `0.0807` → IC=+0.230 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0807 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2828` → IC=+0.263 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2828 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `1.4247` → IC=+0.255 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4247 (IC base=+0.226)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.236 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2448.7802` → IC=+0.236 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2448.7802 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.279 (n=211)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.272)

- **PATRÓN** `sigma_h` > `0.0237` → IC=+0.282 (n=209)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0237 (IC base=+0.272)

- **PATRÓN** `drift_60min` |x|≤ `0.2933` → IC=+0.277 (n=419)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2933 (IC base=+0.272)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.281 (n=591)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.272)

- **PATRÓN** `ibs_20min` < `0.2788` → IC=+0.329 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2788 (IC base=+0.272)

- **PATRÓN** `dist_vwap_pct` < `0.2733` → IC=+0.282 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2733 (IC base=+0.272)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.938` → IC=+0.322 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.938 (IC base=+0.272)

- **PATRÓN** `volumen_regimen` < `0.8838` → IC=+0.272 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8838 (IC base=+0.272)

- **PATRÓN** `volumen_regimen` > `1.2602` → IC=+0.306 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2602 (IC base=+0.272)

- **PATRÓN** `volumen_pendiente_norm` > `0.2896` → IC=+0.386 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2896 (IC base=+0.272)

- **PATRÓN** `volumen_spike_ratio` > `2.1671` → IC=+0.288 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1671 (IC base=+0.272)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.191 (n=905)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0103 (IC base=+0.158)

- **PATRÓN** `drift_60min` |x|≤ `0.3396` → IC=+0.161 (n=2388)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.3396 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.166 (n=2750)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 6.0 (IC base=+0.158)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.282 (n=1335)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `1.1973` → IC=+0.258 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1973 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.426` → IC=+0.244 (n=1128)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.426 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` > `0.623` → IC=+0.170 (n=1879)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 0.623 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` > `0.2391` → IC=+0.191 (n=509)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2391 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` < `2.2894` → IC=+0.160 (n=2164)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.2894 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` > `1.8535` → IC=+0.153 (n=1639)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.8535 (IC base=+0.158)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.166 (n=2168)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `3206.2208` → IC=+0.183 (n=1230)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 3206.2208 (IC base=+0.158)

- **PATRÓN** `ballena_activa_n` < `110.0` → IC=+0.181 (n=1428)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 110.0 (IC base=+0.158)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.203 (n=1665)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.0816` → IC=+0.210 (n=830)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0816 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.206 (n=1170)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.185 (n=924)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 5.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` < `0.4118` → IC=+0.239 (n=2488)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4118 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.895` → IC=+0.217 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.895 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` < `1.1705` → IC=+0.170 (n=1963)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.1705 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` > `0.6864` → IC=+0.169 (n=1753)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 0.6864 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.2921` → IC=+0.259 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2921 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` < `1.5795` → IC=+0.177 (n=824)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.5795 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `2.6609` → IC=+0.211 (n=624)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6609 (IC base=+0.185)

- **PATRÓN** `ballena_activa_n` < `121.0` → IC=+0.190 (n=1277)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 121.0 (IC base=+0.185)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.158 (n=197)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0059 (IC base=+0.154)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.206 (n=202)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.271` → IC=+0.163 (n=443)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.271 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.211 (n=164)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.119` → IC=+0.327 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.119 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.2093` → IC=+0.201 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2093 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `1.4427` → IC=+0.138 (n=363)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.4427 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.181 (n=305)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.04 (IC base=+0.154)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.252 (n=212)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.252)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.270 (n=241)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.252)

- **PATRÓN** `drift_60min` |x|≤ `0.2618` → IC=+0.290 (n=212)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2618 (IC base=+0.252)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.272 (n=217)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.252)

- **PATRÓN** `ibs_20min` < `0.3945` → IC=+0.282 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3945 (IC base=+0.252)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.358` → IC=+0.271 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.358 (IC base=+0.252)

- **PATRÓN** `volumen_pendiente_norm` < `0.0847` → IC=+0.231 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0847 (IC base=+0.252)

- **PATRÓN** `volumen_pendiente_norm` > `0.3163` → IC=+0.274 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3163 (IC base=+0.252)

- **PATRÓN** `volumen_spike_ratio` < `1.9498` → IC=+0.275 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9498 (IC base=+0.252)

- **PATRÓN** `volumen_spike_ratio` > `2.8455` → IC=+0.287 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8455 (IC base=+0.252)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.309 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.252)

- **PATRÓN** `libro_liquidez` > `1939.2468` → IC=+0.319 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1939.2468 (IC base=+0.252)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.242 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.252)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.197 (n=345)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0062 (IC base=+0.173)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.184 (n=131)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0072 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.4287` → IC=+0.179 (n=391)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.4287 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.199 (n=397)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.6388` → IC=+0.224 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6388 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.2181` → IC=+0.234 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2181 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.549` → IC=+0.246 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.549 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `0.6383` → IC=+0.184 (n=131)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6383 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `1.0844` → IC=+0.200 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0844 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.2234` → IC=+0.244 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2234 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` < `1.3655` → IC=+0.240 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3655 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `12753.9278` → IC=+0.184 (n=261)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 12753.9278 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.173 (n=493)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0059 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.2334` → IC=+0.174 (n=433)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2334 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.174 (n=455)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 7.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` < `0.4271` → IC=+0.197 (n=493)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.4271 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` < `0.1641` → IC=+0.177 (n=491)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.1641 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.387` → IC=+0.236 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.387 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `0.6967` → IC=+0.212 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6967 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.1669` → IC=+0.232 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1669 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `2.5679` → IC=+0.164 (n=385)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 2.5679 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `1.4105` → IC=+0.150 (n=384)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.4105 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `14852.9029` → IC=+0.199 (n=164)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 14852.9029 (IC base=+0.152)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.244 (n=131)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0084 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.1532` → IC=+0.178 (n=262)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.1532 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.191 (n=137)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.229 (n=149)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.304 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.958` → IC=+0.294 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.958 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` < `0.2295` → IC=+0.160 (n=333)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` < 0.2295 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `1.9605` → IC=+0.203 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9605 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.190 (n=350)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.04 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `1946.061` → IC=+0.177 (n=131)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 1946.061 (IC base=+0.164)

- **PATRÓN** `sigma_h` < `0.0102` → IC=+0.281 (n=285)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0102 (IC base=+0.256)

- **PATRÓN** `drift_60min` |x|≤ `0.2281` → IC=+0.297 (n=190)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2281 (IC base=+0.256)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.278 (n=192)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.256)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.255 (n=288)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.256)

- **PATRÓN** `ibs_20min` < `0.3902` → IC=+0.298 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3902 (IC base=+0.256)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.143` → IC=+0.348 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.143 (IC base=+0.256)

- **PATRÓN** `volumen_pendiente_norm` > `0.3666` → IC=+0.417 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3666 (IC base=+0.256)

- **PATRÓN** `volumen_spike_ratio` > `2.3561` → IC=+0.275 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3561 (IC base=+0.256)

- **PATRÓN** `ballena_activa_n` < `60.0` → IC=+0.210 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 60.0 (IC base=+0.256)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0091` → IC=+0.210 (n=391)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0091 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.5026` → IC=+0.190 (n=391)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.5026 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.193 (n=405)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 6.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `0.4362` → IC=+0.230 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4362 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` > `0.9816` → IC=+0.232 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9816 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.408` → IC=+0.333 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.408 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` > `0.699` → IC=+0.195 (n=349)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` > 0.699 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.1008` → IC=+0.213 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1008 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` < `1.4303` → IC=+0.180 (n=126)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.4303 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `2.5007` → IC=+0.227 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5007 (IC base=+0.174)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.176 (n=448)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.01 (IC base=+0.174)

- **PATRÓN** `libro_liquidez` > `12277.2558` → IC=+0.220 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12277.2558 (IC base=+0.174)

- **PATRÓN** `ballena_activa_n` < `145.0` → IC=+0.177 (n=218)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 145.0 (IC base=+0.174)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.241 (n=160)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.3825` → IC=+0.158 (n=472)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.3825 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.163 (n=321)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 11.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.154 (n=177)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 5.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.3583` → IC=+0.207 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3583 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.526` → IC=+0.191 (n=108)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 12.526 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `1.1685` → IC=+0.154 (n=472)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.1685 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` > `0.599` → IC=+0.151 (n=471)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.599 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.1023` → IC=+0.167 (n=145)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.1023 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `1.9025` → IC=+0.173 (n=243)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.9025 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `2.5362` → IC=+0.153 (n=122)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.5362 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `10944.7908` → IC=+0.167 (n=157)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 10944.7908 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `121.0` → IC=+0.141 (n=126)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 121.0 (IC base=+0.141)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.184 (n=242)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0109 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.145 (n=486)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 8.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.5625` → IC=+0.182 (n=533)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.5625 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `0.9462` → IC=+0.268 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9462 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.202` → IC=+0.293 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.202 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` > `0.6804` → IC=+0.144 (n=476)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 0.6804 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` < `0.163` → IC=+0.134 (n=523)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` < 0.163 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `1.4402` → IC=+0.133 (n=167)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.4402 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` > `1.5512` → IC=+0.128 (n=447)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.5512 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `3239.7916` → IC=+0.222 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3239.7916 (IC base=+0.121)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.173 (n=151)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.005 (IC base=+0.138)

- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.204 (n=150)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.203 (n=220)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.4098` → IC=+0.238 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4098 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.9932` → IC=+0.144 (n=57)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.9932 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.22` → IC=+0.201 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.22 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.1404` → IC=+0.149 (n=448)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.1404 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `0.8386` → IC=+0.171 (n=299)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 0.8386 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2196` → IC=+0.214 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2196 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.2667` → IC=+0.232 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2667 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `2131.3425` → IC=+0.191 (n=299)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2131.3425 (IC base=+0.138)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0238` → IC=+0.199 (n=257)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0238 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.1645` → IC=+0.201 (n=249)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1645 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.202 (n=203)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.907` → IC=+0.268 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.907 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `1.6268` → IC=+0.268 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.6268 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.169` → IC=+0.236 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.169 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` > `0.6073` → IC=+0.183 (n=566)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 0.6073 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.2397` → IC=+0.253 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2397 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `2.1481` → IC=+0.187 (n=464)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 2.1481 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.172 (n=569)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.01 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `2449.769` → IC=+0.172 (n=566)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2449.769 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.280 (n=243)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.6757` → IC=+0.231 (n=555)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6757 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=273)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.254 (n=258)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` < `0.38` → IC=+0.260 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.38 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.225` → IC=+0.281 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.225 (IC base=+0.221)

- **PATRÓN** `volumen_regimen` > `0.6925` → IC=+0.241 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6925 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.359 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.6983` → IC=+0.255 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6983 (IC base=+0.221)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.006` → IC=+0.141 (n=352)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` > 0.006 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.192 (n=258)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 16.0 (IC base=+0.104)

- **PATRÓN** `ibs_20min` > `0.6176` → IC=+0.170 (n=473)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.6176 (IC base=+0.104)

- **PATRÓN** `dist_vwap_pct` > `0.8872` → IC=+0.259 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8872 (IC base=+0.104)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.235` → IC=+0.185 (n=144)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 8.235 (IC base=+0.104)

- **PATRÓN** `volumen_pendiente_norm` > `0.1826` → IC=+0.171 (n=144)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1826 (IC base=+0.104)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=394)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.01 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `2625.0768` → IC=+0.133 (n=352)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2625.0768 (IC base=+0.104)

- **PATRÓN** `ibs_20min` < `0.3158` → IC=+0.137 (n=337)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` < 0.3158 (IC base=+0.057)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.772` → IC=+0.143 (n=113)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 7.772 (IC base=+0.057)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.200 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.126 (n=89)

- **FILTRO** `ibs_20min` < `0.5377` → IC=-0.177 (n=29)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5377
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=88)

- **FILTRO** `libro_liquidez` < `8276.6888` → IC=-0.175 (n=38)

  - _Acción_: SKIP cuando `libro_liquidez` < 8276.6888
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=79)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.126 (n=89)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 9.0 (IC base=+0.046)

- **PATRÓN** `ibs_20min` > `0.5377` → IC=+0.122 (n=88)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` > 0.5377 (IC base=+0.046)

- **PATRÓN** `dist_vwap_pct` > `0.7932` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7932 (IC base=+0.046)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.167` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 4.167 (IC base=+0.046)

- **PATRÓN** `libro_liquidez` > `12103.1125` → IC=+0.156 (n=59)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 12103.1125 (IC base=+0.046)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.221 (n=59)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.102)

- **PATRÓN** `drift_60min` |x|≤ `0.3657` → IC=+0.135 (n=176)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.3657 (IC base=+0.102)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.172 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 4.0 (IC base=+0.102)

- **PATRÓN** `ibs_20min` < `0.6123` → IC=+0.175 (n=155)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.6123 (IC base=+0.102)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.767` → IC=+0.222 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.767 (IC base=+0.102)

- **PATRÓN** `volumen_regimen` < `1.1856` → IC=+0.129 (n=176)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1856 (IC base=+0.102)

- **PATRÓN** `volumen_pendiente_norm` > `0.1497` → IC=+0.308 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1497 (IC base=+0.102)

- **PATRÓN** `volumen_spike_ratio` < `1.7313` → IC=+0.146 (n=111)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.7313 (IC base=+0.102)

- **PATRÓN** `ballena_activa_n` < `162.0` → IC=+0.151 (n=64)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 162.0 (IC base=+0.102)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **FILTRO** `sigma_h` > `0.0064` → IC=-0.231 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0064
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=76)

- **FILTRO** `ibs_20min` > `0.6889` → IC=-0.269 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6889
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=76)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.291 (n=89)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.294)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.329 (n=68)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.294)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.326 (n=90)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.294)

- **PATRÓN** `ibs_20min` > `0.8289` → IC=+0.329 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8289 (IC base=+0.294)

- **PATRÓN** `dist_vwap_pct` > `0.1466` → IC=+0.351 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1466 (IC base=+0.294)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.561` → IC=+0.377 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.561 (IC base=+0.294)

- **PATRÓN** `volumen_regimen` < `0.7015` → IC=+0.372 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7015 (IC base=+0.294)

- **PATRÓN** `volumen_regimen` > `1.0786` → IC=+0.312 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0786 (IC base=+0.294)

- **PATRÓN** `volumen_pendiente_norm` > `0.1782` → IC=+0.402 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1782 (IC base=+0.294)

- **PATRÓN** `volumen_spike_ratio` < `2.2928` → IC=+0.305 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2928 (IC base=+0.294)

- **PATRÓN** `volumen_spike_ratio` > `1.5284` → IC=+0.318 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5284 (IC base=+0.294)

- **PATRÓN** `libro_liquidez` > `2687.8872` → IC=+0.296 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2687.8872 (IC base=+0.294)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.357 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.020)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.159 (n=42)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 13.0 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` < `0.7011` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.7011 (IC base=+0.020)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` < `0.5556` → IC=-0.173 (n=50)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5556
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=152)

- **FILTRO** `hora_utc` < `4.0` → IC=-0.200 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=91)

- **FILTRO** `ibs_20min` > `0.4783` → IC=-0.238 (n=40)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4783
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=79)

- **FILTRO** `dist_vwap_pct` > `0.1977` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1977
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=99)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.161 (n=57)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.029)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.199 (n=71)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 1.0 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` > `0.4993` → IC=+0.179 (n=26)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.4993 (IC base=+0.029)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.198 (n=41)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 15.0 (IC base=+0.093)

- **PATRÓN** `ibs_20min` > `0.6047` → IC=+0.125 (n=78)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` > 0.6047 (IC base=+0.093)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.745` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.745 (IC base=+0.093)

- **PATRÓN** `volumen_regimen` > `0.6461` → IC=+0.125 (n=78)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.6461 (IC base=+0.093)

- **PATRÓN** `volumen_pendiente_norm` > `0.2164` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2164 (IC base=+0.093)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.122 (n=96)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `2446.4744` → IC=+0.129 (n=87)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2446.4744 (IC base=+0.093)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.093)

- **PATRÓN** `ibs_20min` < `0.0488` → IC=+0.241 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0488 (IC base=+0.056)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.185 (n=2118)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0066 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.159 (n=3234)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 6.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.9412` → IC=+0.289 (n=1440)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9412 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `1.1283` → IC=+0.239 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1283 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.529` → IC=+0.228 (n=1847)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.529 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.699` → IC=+0.149 (n=985)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.699 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` > `1.0787` → IC=+0.153 (n=1015)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 1.0787 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.1653` → IC=+0.174 (n=819)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1653 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.3115` → IC=+0.152 (n=2512)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.3115 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.8681` → IC=+0.158 (n=1902)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.8681 (IC base=+0.150)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.156 (n=2534)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `2479.6478` → IC=+0.175 (n=2115)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2479.6478 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `141.0` → IC=+0.188 (n=1580)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 141.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.215 (n=1954)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.4838` → IC=+0.199 (n=2927)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.4838 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.189 (n=2073)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 11.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.206 (n=1029)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` < `0.5624` → IC=+0.245 (n=2927)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5624 (IC base=+0.189)

- **PATRÓN** `dist_vwap_pct` < `0.4433` → IC=+0.181 (n=2180)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.4433 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.42` → IC=+0.206 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.42 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.655` → IC=+0.193 (n=2747)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 2.655 (IC base=+0.189)

- **PATRÓN** `volumen_regimen` < `0.6179` → IC=+0.186 (n=721)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.6179 (IC base=+0.189)

- **PATRÓN** `volumen_regimen` > `1.2004` → IC=+0.174 (n=721)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 1.2004 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.2391` → IC=+0.268 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2391 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `2.304` → IC=+0.207 (n=1010)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.304 (IC base=+0.189)

- **PATRÓN** `ballena_activa_n` < `172.0` → IC=+0.168 (n=1799)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 172.0 (IC base=+0.189)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.227 (n=236)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.155 (n=529)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 6.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.173 (n=347)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 11.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.313 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.347` → IC=+0.306 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.347 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.2129` → IC=+0.226 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2129 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `1.586` → IC=+0.126 (n=193)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.586 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.9148` → IC=+0.148 (n=291)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.9148 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.200 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.287 (n=228)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.265)

- **PATRÓN** `drift_60min` |x|≤ `0.1064` → IC=+0.296 (n=150)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1064 (IC base=+0.265)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.267 (n=307)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.265)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.278 (n=237)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.265)

- **PATRÓN** `ibs_20min` < `0.562` → IC=+0.305 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.562 (IC base=+0.265)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.116` → IC=+0.285 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.116 (IC base=+0.265)

- **PATRÓN** `volumen_pendiente_norm` > `0.3023` → IC=+0.325 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3023 (IC base=+0.265)

- **PATRÓN** `volumen_spike_ratio` > `2.7667` → IC=+0.317 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7667 (IC base=+0.265)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.296 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.265)

- **PATRÓN** `libro_liquidez` > `1960.7048` → IC=+0.310 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1960.7048 (IC base=+0.265)

- **PATRÓN** `ballena_activa_n` < `74.0` → IC=+0.244 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 74.0 (IC base=+0.265)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.163 (n=170)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0029 (IC base=+0.154)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.180 (n=170)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0071 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.4191` → IC=+0.155 (n=508)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4191 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.182 (n=460)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 8.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.3308` → IC=+0.210 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3308 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.2678` → IC=+0.228 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2678 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.567` → IC=+0.204 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.567 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `1.2673` → IC=+0.161 (n=508)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2673 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` > `1.0896` → IC=+0.174 (n=231)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 1.0896 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` < `0.0733` → IC=+0.172 (n=410)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` < 0.0733 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.2054` → IC=+0.190 (n=98)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2054 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `2.4168` → IC=+0.186 (n=460)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 2.4168 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `1.3655` → IC=+0.175 (n=459)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.3655 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `12240.9476` → IC=+0.172 (n=339)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 12240.9476 (IC base=+0.154)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.175 (n=487)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0061 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.279` → IC=+0.177 (n=428)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.279 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.174 (n=458)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 7.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.181 (n=503)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 18.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` < `0.3935` → IC=+0.219 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3935 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` < `0.1554` → IC=+0.182 (n=435)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.1554 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.805` → IC=+0.216 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.805 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `0.6183` → IC=+0.238 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6183 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.146` → IC=+0.281 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.146 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `2.5087` → IC=+0.189 (n=390)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 2.5087 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.167 (n=629)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `13247.5111` → IC=+0.180 (n=220)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 13247.5111 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `307.0` → IC=+0.187 (n=97)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 307.0 (IC base=+0.167)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.260 (n=190)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0079 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.249 (n=193)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `0.7037` → IC=+0.259 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7037 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.217` → IC=+0.348 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.217 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` < `0.222` → IC=+0.188 (n=354)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` < 0.222 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` < `1.9553` → IC=+0.195 (n=152)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.9553 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.212 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `1831.6886` → IC=+0.198 (n=279)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 1831.6886 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.245 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 49.0 (IC base=+0.183)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.307 (n=143)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.2118` → IC=+0.241 (n=284)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2118 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.281 (n=162)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.5541` → IC=+0.303 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5541 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.108` → IC=+0.262 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.108 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.3579` → IC=+0.333 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3579 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.7651` → IC=+0.238 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7651 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `2.364` → IC=+0.211 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.364 (IC base=+0.238)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.271 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.238)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.186 (n=192)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 58.0 (IC base=+0.238)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0089` → IC=+0.154 (n=510)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0089 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.1495` → IC=+0.143 (n=225)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.1495 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.167 (n=467)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 8.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.3436` → IC=+0.193 (n=510)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.3436 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.8501` → IC=+0.217 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8501 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.492` → IC=+0.187 (n=244)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 4.492 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.9051` → IC=+0.164 (n=340)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.9051 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `1.2091` → IC=+0.157 (n=170)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 1.2091 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.2692` → IC=+0.256 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2692 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `2.1158` → IC=+0.224 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1158 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `5099.5365` → IC=+0.219 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5099.5365 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `162.0` → IC=+0.179 (n=257)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 162.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.193 (n=148)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0033 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.5036` → IC=+0.160 (n=439)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.5036 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.148 (n=160)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 17.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.176 (n=202)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 7.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` < `0.6499` → IC=+0.182 (n=439)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.6499 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.2359` → IC=+0.152 (n=182)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.2359 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.901` → IC=+0.210 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.901 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.5823` → IC=+0.164 (n=147)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.5823 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` > `1.1518` → IC=+0.171 (n=147)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 1.1518 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.2393` → IC=+0.300 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2393 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.4896` → IC=+0.198 (n=127)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.4896 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `11684.767` → IC=+0.211 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11684.767 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `135.0` → IC=+0.205 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 135.0 (IC base=+0.146)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.138 (n=255)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` > 0.0114 (IC base=+0.093)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.124 (n=503)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 8.0 (IC base=+0.093)

- **PATRÓN** `ibs_20min` > `0.4868` → IC=+0.178 (n=563)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.4868 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` > `0.9198` → IC=+0.229 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9198 (IC base=+0.093)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.432` → IC=+0.223 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.432 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `2971.9929` → IC=+0.268 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2971.9929 (IC base=+0.093)

- **PATRÓN** `ballena_activa_n` < `66.0` → IC=+0.158 (n=337)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 66.0 (IC base=+0.093)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.184 (n=175)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0056 (IC base=+0.116)

- **PATRÓN** `drift_60min` |x|≤ `0.1241` → IC=+0.150 (n=175)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.1241 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.165 (n=252)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` < `0.5918` → IC=+0.202 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5918 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` < `0.5096` → IC=+0.136 (n=501)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.5096 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.086` → IC=+0.139 (n=513)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 3.086 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` < `0.7055` → IC=+0.152 (n=231)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.7055 (IC base=+0.116)

- **PATRÓN** `volumen_pendiente_norm` > `0.0713` → IC=+0.171 (n=153)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.0713 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` < `2.0903` → IC=+0.140 (n=331)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.0903 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` > `1.4382` → IC=+0.145 (n=376)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4382 (IC base=+0.116)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.124 (n=548)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `2692.6188` → IC=+0.163 (n=238)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2692.6188 (IC base=+0.116)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0272` → IC=+0.221 (n=220)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0272 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.189 (n=663)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 6.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `0.9609` → IC=+0.297 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9609 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` > `1.0343` → IC=+0.282 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0343 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.118` → IC=+0.248 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.118 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` > `1.0357` → IC=+0.212 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0357 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.1708` → IC=+0.240 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1708 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `1.8195` → IC=+0.191 (n=406)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 1.8195 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.186 (n=785)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.02 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `2451.004` → IC=+0.181 (n=659)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 2451.004 (IC base=+0.178)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.218 (n=395)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.178)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.294 (n=241)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.493` → IC=+0.226 (n=629)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.493 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.222 (n=671)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.217)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.220 (n=759)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.4964` → IC=+0.281 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4964 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` < `0.1739` → IC=+0.231 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1739 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.61` → IC=+0.296 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.61 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` > `1.2406` → IC=+0.237 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2406 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.2827` → IC=+0.320 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2827 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.2111` → IC=+0.229 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2111 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.184 (n=435)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 37.0 (IC base=+0.217)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.145 (n=1258)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.157 (n=298)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 18.0 (IC base=+0.105)

- **PATRÓN** `ibs_20min` > `0.8113` → IC=+0.162 (n=389)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.8113 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `1.4973` → IC=+0.149 (n=132)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 1.4973 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` > `1.0826` → IC=+0.126 (n=287)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 1.0826 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` > `0.2444` → IC=+0.167 (n=157)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2444 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` < `1.4475` → IC=+0.142 (n=283)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4475 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` > `2.6043` → IC=+0.134 (n=282)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.6043 (IC base=+0.105)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.192 (n=319)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0037 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.3821` → IC=+0.166 (n=841)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.3821 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.156 (n=373)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.194 (n=331)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 4.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.1951` → IC=+0.160 (n=421)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1951 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.093` → IC=+0.142 (n=955)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.093 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.1992` → IC=+0.152 (n=354)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.1992 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.061` → IC=+0.153 (n=956)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 6.061 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `1.2126` → IC=+0.151 (n=931)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.2126 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` < `0.0927` → IC=+0.151 (n=857)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` < 0.0927 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `2.5268` → IC=+0.158 (n=947)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.5268 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.423` → IC=+0.148 (n=947)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.423 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.145 (n=1258)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `10602.7113` → IC=+0.149 (n=637)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 10602.7113 (IC base=+0.141)

### GBM_LATE_5M#BTC#5min
- **FILTRO** `sigma_ewma_delta_pct` > `2.779` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.779
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=130)

- **FILTRO** `volumen_pendiente_norm` > `0.1016` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1016
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=133)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.125 (n=102)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 14.0 (IC base=+0.062)

- **PATRÓN** `volumen_spike_ratio` < `1.5292` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.5292 (IC base=+0.062)

- **PATRÓN** `libro_liquidez` > `12574.1361` → IC=+0.147 (n=114)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 12574.1361 (IC base=+0.062)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.193 (n=229)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0036 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.3904` → IC=+0.149 (n=520)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.3904 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.181 (n=202)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.186 (n=189)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.1706` → IC=+0.171 (n=229)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.1706 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.6841` → IC=+0.183 (n=58)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.6841 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.22` → IC=+0.160 (n=521)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` < 6.22 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.1847` → IC=+0.155 (n=520)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.1847 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.0692` → IC=+0.168 (n=245)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.0692 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.5395` → IC=+0.154 (n=518)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.5395 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.8093` → IC=+0.151 (n=345)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.8093 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `11991.7118` → IC=+0.149 (n=465)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 11991.7118 (IC base=+0.140)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.184 (n=115)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0098 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.3484` → IC=+0.133 (n=115)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.66€ cuando `drift_60min` |x|≤ 0.3484 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.179 (n=157)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 7.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `0.9259` → IC=+0.250 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9259 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.03` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.03 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2139` → IC=+0.194 (n=47)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2139 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `2.2908` → IC=+0.147 (n=114)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 2.2908 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `1904.217` → IC=+0.149 (n=172)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1904.217 (IC base=+0.128)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.161 (n=302)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0093 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.5372` → IC=+0.145 (n=302)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.5372 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.192 (n=115)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 18.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.902` → IC=+0.128 (n=302)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.902 (IC base=+0.129)

- **PATRÓN** `ibs_20min` > `0.803` → IC=+0.169 (n=137)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.803 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` > `0.9427` → IC=+0.176 (n=72)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.9427 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` < `0.226` → IC=+0.136 (n=256)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.226 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.027` → IC=+0.173 (n=47)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 11.027 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.266` → IC=+0.138 (n=266)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 4.266 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.728` → IC=+0.159 (n=133)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.728 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` < `0.1178` → IC=+0.131 (n=272)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` < 0.1178 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.0778` → IC=+0.135 (n=135)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.0778 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `1.424` → IC=+0.170 (n=98)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.424 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `1.8447` → IC=+0.136 (n=196)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.8447 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `8982.0928` → IC=+0.151 (n=270)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 8982.0928 (IC base=+0.129)

- **PATRÓN** `sigma_h` < `0.0088` → IC=+0.145 (n=274)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0088 (IC base=+0.134)

- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.136 (n=182)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.0062 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.4222` → IC=+0.191 (n=241)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.4222 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.163 (n=185)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 11.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.6178` → IC=+0.142 (n=241)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.6178 (IC base=+0.134)

- **PATRÓN** `ibs_20min` > `0.1102` → IC=+0.154 (n=273)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` > 0.1102 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `0.1548` → IC=+0.157 (n=103)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1548 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.438` → IC=+0.180 (n=48)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 11.438 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `1.1943` → IC=+0.156 (n=274)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.1943 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` < `0.139` → IC=+0.158 (n=279)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` < 0.139 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `2.1843` → IC=+0.178 (n=237)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 2.1843 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.4499` → IC=+0.161 (n=269)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.4499 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `10385.425` → IC=+0.145 (n=91)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 10385.425 (IC base=+0.134)

### GBM_LATE_5M#SOL#5min
- **FILTRO** `hora_utc` > `6.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=64)

- **FILTRO** `libro_liquidez` < `2949.8034` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `libro_liquidez` < 2949.8034
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=63)

- **FILTRO** `sigma_h` < `0.011` → IC=-0.196 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.011
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=21)

- **FILTRO** `sigma_ewma_delta_pct` < `3.941` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 3.941
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=25)

### GBM_LATE_60M
- **FILTRO** `ibs_20min` < `0.6789` → IC=-0.206 (n=49)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6789
  - _Potencial_: sin este filtro IC_bueno=+0.233 (n=148)

- **FILTRO** `sigma_h` > `0.0111` → IC=-0.282 (n=53)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0111
  - _Potencial_: sin este filtro IC_bueno=-0.130 (n=163)

- **FILTRO** `ibs_20min` > `0.1674` → IC=-0.190 (n=85)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1674
  - _Potencial_: sin este filtro IC_bueno=+0.145 (n=29)

- **FILTRO** `dist_vwap_pct` > `0.111` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.111
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=57)

- **FILTRO** `volumen_regimen` > `1.0316` → IC=-0.200 (n=38)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.0316
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=76)

- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.185 (n=160)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0055 (IC base=+0.076)

- **PATRÓN** `ibs_20min` > `0.6789` → IC=+0.233 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6789 (IC base=+0.076)

- **PATRÓN** `dist_vwap_pct` > `0.129` → IC=+0.184 (n=74)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.129 (IC base=+0.076)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.047` → IC=+0.232 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.047 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` < `0.5932` → IC=+0.135 (n=50)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.5932 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` > `1.1731` → IC=+0.173 (n=50)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 1.1731 (IC base=+0.076)

- **PATRÓN** `volumen_pendiente_norm` < `0.0847` → IC=+0.256 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0847 (IC base=+0.076)

- **PATRÓN** `volumen_pendiente_norm` > `0.2652` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2652 (IC base=+0.076)

- **PATRÓN** `volumen_spike_ratio` < `2.0129` → IC=+0.261 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0129 (IC base=+0.076)

- **PATRÓN** `volumen_spike_ratio` > `1.4935` → IC=+0.308 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4935 (IC base=+0.076)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.167 (n=133)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.02 (IC base=+0.076)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.792` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `ibs_20min` < 0.792
  - _Potencial_: sin este filtro IC_bueno=+0.226 (n=49)

- **FILTRO** `sigma_h` > `0.005` → IC=-0.192 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=47)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.339 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.074)

- **PATRÓN** `ibs_20min` > `0.792` → IC=+0.226 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.792 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.1647` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1647 (IC base=+0.074)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.232` → IC=+0.129 (n=33)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 6.232 (IC base=+0.074)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0068` → IC=-0.333 (n=22)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=45)

- **FILTRO** `ibs_20min` > `0.3405` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `ibs_20min` > 0.3405
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=13)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.174 (n=84)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0059 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.148 (n=89)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 7.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.126 (n=97)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 17.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.360 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` < `0.1247` → IC=+0.222 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1247 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.06` → IC=+0.324 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.06 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `0.8266` → IC=+0.211 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8266 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` > `1.0933` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0933 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2498.7472` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2498.7472 (IC base=+0.125)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0165` → IC=-0.309 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0165
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=59)

- **FILTRO** `ibs_20min` > `0.4286` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4286
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

- **FILTRO** `volumen_regimen` > `0.903` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.903
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=19)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.188 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.000)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `15.0` → IC=-0.462 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.233 (n=73)

- **FILTRO** `dist_vwap_pct` > `0.0755` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.0755
  - _Potencial_: sin este filtro IC_bueno=-0.283 (n=81)

- **FILTRO** `volumen_regimen` < `1.0933` → IC=-0.351 (n=72)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.0933
  - _Potencial_: sin este filtro IC_bueno=-0.130 (n=25)

- **FILTRO** `ibs_20min` > `0.6429` → IC=-0.340 (n=48)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6429
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=50)

- **FILTRO** `dist_vwap_pct` < `0.1009` → IC=-0.354 (n=53)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1009
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=45)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `volumen_regimen` < `1.2353` → IC=-0.300 (n=23)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.2353
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=13)

- **FILTRO** `sigma_h` < `0.0019` → IC=-0.318 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0019
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=21)

- **FILTRO** `ibs_20min` > `0.6267` → IC=-0.364 (n=20)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6267
  - _Potencial_: sin este filtro IC_bueno=-0.152 (n=21)

- **FILTRO** `dist_vwap_pct` < `0.0931` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0931
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=14)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.6354` → IC=-0.462 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6354
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=18)

- **FILTRO** `ibs_20min` > `0.8144` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8144
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=17)

- **FILTRO** `dist_vwap_pct` > `0.0802` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.0802
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=15)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `sigma_h` < `0.0064` → IC=-0.262 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0064
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

- **FILTRO** `ibs_20min` < `0.5833` → IC=-0.309 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5833
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

- **FILTRO** `sigma_h` < `0.0065` → IC=-0.382 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0065
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **FILTRO** `dist_vwap_pct` < `0.3782` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.3782
  - _Potencial_: sin este filtro IC_bueno=-0.300 (n=8)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.441 (n=15)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `dist_vwap_pct` > `0.2258` → IC=-0.145 (n=29)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2258
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=132)

- **PATRÓN** `ibs_20min` > `0.5882` → IC=+0.136 (n=141)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 0.5882 (IC base=+0.040)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.172 (n=59)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 15.0 (IC base=+0.040)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.659` → IC=+0.167 (n=31)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.659 (IC base=+0.040)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `sigma_h` < `0.0017` → IC=-0.206 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0017
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=47)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=47)

- **FILTRO** `ibs_20min` < `0.4975` → IC=-0.409 (n=20)

  - _Acción_: SKIP cuando `ibs_20min` < 0.4975
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=42)

- **PATRÓN** `ibs_20min` > `0.7305` → IC=+0.167 (n=31)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.7305 (IC base=-0.078)

- **PATRÓN** `sigma_h` > `0.0036` → IC=+0.200 (n=28)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0036 (IC base=+0.107)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.250 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.107)

- **PATRÓN** `ibs_20min` < `0.3387` → IC=+0.188 (n=62)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.3387 (IC base=+0.107)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.519` → IC=+0.174 (n=41)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 3.519 (IC base=+0.107)

- **PATRÓN** `volumen_regimen` < `1.1843` → IC=+0.141 (n=62)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.1843 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `4049.975` → IC=+0.132 (n=55)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 4049.975 (IC base=+0.107)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.321 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0022 (IC base=+0.100)

- **PATRÓN** `drift_60min` |x|≤ `0.1478` → IC=+0.147 (n=32)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.1478 (IC base=+0.100)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.100)

- **PATRÓN** `ibs_20min` > `0.8029` → IC=+0.243 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8029 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.517` → IC=+0.167 (n=31)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 6.517 (IC base=+0.100)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.100)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.143 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=14)

- **FILTRO** `ibs_20min` > `0.0435` → IC=-0.145 (n=29)

  - _Acción_: SKIP cuando `ibs_20min` > 0.0435
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=11)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.227 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.095)

- **PATRÓN** `drift_60min` |x|≤ `0.1849` → IC=+0.159 (n=39)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1849 (IC base=+0.095)

- **PATRÓN** `ibs_20min` < `0.7333` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7333 (IC base=+0.095)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.256 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.095)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.160 (n=45)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.03 (IC base=+0.095)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `libro_liquidez` > `2490.1288` → IC=+0.156 (n=123)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2490.1288 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.127 (n=132)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.132 (n=142)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 18.0 (IC base=+0.118)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.128 (n=49)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.495 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2538.9528` → IC=+0.158 (n=118)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2538.9528 (IC base=+0.118)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2490.1288` → IC=+0.156 (n=123)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2490.1288 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.127 (n=132)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.132 (n=142)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 18.0 (IC base=+0.118)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.128 (n=49)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.495 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2538.9528` → IC=+0.158 (n=118)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2538.9528 (IC base=+0.118)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `9.0` → IC=-0.185 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=44)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=99)

- **FILTRO** `libro_liquidez` < `2110.4161` → IC=-0.367 (n=28)

  - _Acción_: SKIP cuando `libro_liquidez` < 2110.4161
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=87)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=104)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=15)

- **FILTRO** `libro_liquidez` < `11321.3584` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 11321.3584
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=16)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=12)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=8)

- **FILTRO** `libro_liquidez` < `13267.3` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_liquidez` < 13267.3
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=616)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=89)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9444` → IC=-0.289 (n=36)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9444
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=74)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=89)

- **FILTRO** `ballena_activa_n` > `558.0` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `ballena_activa_n` > 558.0
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=58)

### LIQUIDACIONES_5M#BNB#5min
- **PATRÓN** `py_entrada` < `0.5` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.5 (IC base=+0.065)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_usd_total` < `26874.22` → IC=-0.156 (n=30)

  - _Acción_: SKIP cuando `liq_usd_total` < 26874.22
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=61)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=17)

- **FILTRO** `libro_liquidez` < `15381.0964` → IC=-0.231 (n=24)

  - _Acción_: SKIP cuando `libro_liquidez` < 15381.0964
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `ballena_activa_n` > `630.0` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `ballena_activa_n` > 630.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=8)

- **PATRÓN** `liq_usd_total` > `99462.85` → IC=+0.136 (n=31)

  - _Acción_: Kelly boost +0.68€ cuando `liq_usd_total` > 99462.85 (IC base=+0.005)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `0.8749` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.8749
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=48)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.155 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=37)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=45)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=184)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9593` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9593
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=15)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

- **PATRÓN** `liq_n` > `3.0` → IC=+0.122 (n=72)

  - _Acción_: Kelly boost +0.61€ cuando `liq_n` > 3.0 (IC base=+0.064)

- **PATRÓN** `liq_usd_total` > `15114.67` → IC=+0.192 (n=50)

  - _Acción_: Kelly boost +0.96€ cuando `liq_usd_total` > 15114.67 (IC base=+0.064)

### LIQUIDACIONES_5M#SOL#5min
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
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=27)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=27)

### LIQUIDACIONES_60M
- **FILTRO** `py_entrada` > `0.56` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=104)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.128 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=56)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=29)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=79)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=29)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=27)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2179.6408` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `libro_liquidez` < 2179.6408
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=126)

### MOMENTUM_IBS_15M#DOGE#15min
- **FILTRO** `ibs_20min` > `0.9412` → IC=-0.170 (n=101)

  - _Acción_: SKIP cuando `ibs_20min` > 0.9412
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=307)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=497)

### MOMENTUM_IBS_15M#SOL#15min
- **FILTRO** `drift_20min_pct` |x|> `0.1779` → IC=-0.125 (n=110)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1779
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=214)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.46` → IC=-0.173 (n=950)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=2871)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.206 (n=971)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=2938)

- **FILTRO** `ibs_20min` > `0.27` → IC=-0.171 (n=977)

  - _Acción_: SKIP cuando `ibs_20min` > 0.27
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=2932)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.225 (n=136)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=416)

- **FILTRO** `ibs_20min` < `0.7361` → IC=-0.164 (n=138)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7361
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=414)

- **FILTRO** `ibs_20min` > `0.75` → IC=-0.157 (n=167)

  - _Acción_: SKIP cuando `ibs_20min` > 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=509)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.198 (n=157)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=482)

- **FILTRO** `ballena_activa_n` > `42.0` → IC=-0.124 (n=216)

  - _Acción_: SKIP cuando `ballena_activa_n` > 42.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=423)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.136 (n=174)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=412)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.178 (n=256)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=330)

- **FILTRO** `ibs_20min` < `0.7271` → IC=-0.189 (n=146)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7271
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=440)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.227 (n=159)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=498)

- **FILTRO** `ibs_20min` > `0.7304` → IC=-0.223 (n=164)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7304
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=493)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.133 (n=178)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=505)

- **FILTRO** `py_entrada` > `0.52` → IC=-0.182 (n=168)

  - _Acción_: SKIP cuando `py_entrada` > 0.52
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=515)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.157 (n=170)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=513)

### MOMENTUM_IBS_15M_BALLENA#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.130 (n=190)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=465)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.207 (n=148)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=476)

- **FILTRO** `ibs_20min` > `0.2759` → IC=-0.156 (n=155)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2759
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=469)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.215 (n=156)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=482)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=623)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.237 (n=207)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=423)

- **FILTRO** `ibs_20min` > `0.2734` → IC=-0.204 (n=157)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2734
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=473)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `hora_utc` > `19.0` → IC=-0.206 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=128)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=375)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=381)

### MOMENTUM_IBS_15M_FADE#BNB#15min
- **FILTRO** `libro_liquidez` < `2063.3848` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 2063.3848
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=55)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `19.0` → IC=-0.132 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=12)

- **FILTRO** `ibs_20min` < `1.0` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=19)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `hora_utc` < `19.0` → IC=-0.300 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=13)

- **FILTRO** `drift_20min_pct` |x|> `0.0299` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.0299
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **FILTRO** `ibs_20min` < `0.0752` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `ibs_20min` < 0.0752
  - _Potencial_: sin este filtro IC_bueno=-0.222 (n=16)

- **FILTRO** `libro_liquidez` < `15251.0076` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `libro_liquidez` < 15251.0076
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=11)

- **FILTRO** `drift_20min_pct` |x|> `0.1906` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1906
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=58)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `11.0` → IC=-0.300 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=56)

- **FILTRO** `ibs_20min` > `0.8837` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8837
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=38)

### MOMENTUM_IBS_5M#BNB#5min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=38)

- **FILTRO** `drift_7min_pct` |x|> `0.0725` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.0725
  - _Potencial_: sin este filtro IC_bueno=+0.133 (n=28)

- **PATRÓN** `drift_7min_pct` |x|≤ `0.0331` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_7min_pct` |x|≤ 0.0331 (IC base=-0.026)

### MOMENTUM_IBS_5M#BTC#5min
- **FILTRO** `hora_utc` > `18.0` → IC=-0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 18.0
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=88)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.143 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 17.0 (IC base=+0.033)

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
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=630)

### MOMENTUM_IBS_5M_BALLENA
- **FILTRO** `hora_utc` < `7.0` → IC=-0.136 (n=2371)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=7301)

- **FILTRO** `py_entrada` < `0.36` → IC=-0.282 (n=2371)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=7301)

- **FILTRO** `ibs_7min` < `0.7294` → IC=-0.236 (n=2418)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7294
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=7254)

- **FILTRO** `ballena_activa_n` > `19.0` → IC=-0.173 (n=3254)

  - _Acción_: SKIP cuando `ballena_activa_n` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=6418)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.222 (n=2945)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=8860)

- **FILTRO** `ibs_7min` > `0.7168` → IC=-0.174 (n=2951)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7168
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=8854)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.317 (n=321)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=996)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.191 (n=922)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=395)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.247 (n=314)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=1003)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.227 (n=488)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=1546)

- **FILTRO** `drift_7min_pct` |x|> `0.1325` → IC=-0.138 (n=691)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1325
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=1343)

- **FILTRO** `ibs_7min` > `0.8511` → IC=-0.182 (n=508)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8511
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=1526)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.142 (n=392)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=1473)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.252 (n=446)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=1419)

- **FILTRO** `ibs_7min` < `0.792` → IC=-0.186 (n=466)

  - _Acción_: SKIP cuando `ibs_7min` < 0.792
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=1399)

- **FILTRO** `ballena_activa_n` > `162.0` → IC=-0.188 (n=466)

  - _Acción_: SKIP cuando `ballena_activa_n` > 162.0
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=1399)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.217 (n=458)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=1408)

- **FILTRO** `ballena_activa_n` > `98.0` → IC=-0.166 (n=632)

  - _Acción_: SKIP cuando `ballena_activa_n` > 98.0
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=1234)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.202 (n=333)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=1072)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.313 (n=452)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=953)

- **FILTRO** `ibs_7min` < `0.2174` → IC=-0.287 (n=351)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2174
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=1054)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.273 (n=346)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=1059)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.251 (n=447)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=1627)

- **FILTRO** `ibs_7min` > `0.812` → IC=-0.189 (n=518)

  - _Acción_: SKIP cuando `ibs_7min` > 0.812
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=1556)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.151 (n=480)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=1146)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.216 (n=783)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=843)

- **FILTRO** `ibs_7min` < `0.7565` → IC=-0.191 (n=406)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7565
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=1220)

- **FILTRO** `ballena_activa_n` > `42.0` → IC=-0.202 (n=401)

  - _Acción_: SKIP cuando `ballena_activa_n` > 42.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=1225)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.264 (n=392)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=1232)

- **FILTRO** `ibs_7min` > `0.1822` → IC=-0.164 (n=552)

  - _Acción_: SKIP cuando `ibs_7min` > 0.1822
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=1072)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.172 (n=549)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=1075)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.231 (n=455)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1411)

- **FILTRO** `ibs_7min` < `0.7692` → IC=-0.203 (n=456)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7692
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=1410)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.183 (n=465)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=1401)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.187 (n=528)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=1658)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.37` → IC=-0.299 (n=386)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=1207)

- **FILTRO** `ibs_7min` < `0.75` → IC=-0.234 (n=392)

  - _Acción_: SKIP cuando `ibs_7min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=1201)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.234 (n=389)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=1204)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.273 (n=408)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=1613)

- **FILTRO** `ibs_7min` > `0.8` → IC=-0.173 (n=503)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=1518)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.127 (n=658)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=1363)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=149)

- **FILTRO** `drift_7min_pct` |x|> `0.106` → IC=-0.139 (n=59)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.106
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=116)

- **FILTRO** `ibs_7min` > `0.0606` → IC=-0.133 (n=58)

  - _Acción_: SKIP cuando `ibs_7min` > 0.0606
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=117)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=412)

### MOMENTUM_IBS_5M_FADE#DOGE#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=596)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=568)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=248)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=435)

### ORDER_FLOW_5M
- **FILTRO** `total_vol_5m` > `215.224` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `total_vol_5m` > 215.224
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `delta_ratio` |x|> `0.3987` → IC=+0.135 (n=351)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio` |x|> 0.3987 (IC base=+0.115)

- **PATRÓN** `total_vol_5m` < `459.6089` → IC=+0.170 (n=110)

  - _Acción_: Kelly boost +0.85€ cuando `total_vol_5m` < 459.6089 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `3219.7168` → IC=+0.141 (n=126)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 3219.7168 (IC base=+0.115)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `12.0` → IC=+0.255 (n=51)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.125)

- **PATRÓN** `total_vol_5m` < `637.367` → IC=+0.133 (n=77)

  - _Acción_: Kelly boost +0.66€ cuando `total_vol_5m` < 637.367 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.139 (n=70)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 53.0 (IC base=+0.125)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `libro_liquidez` > `2022.4544` → IC=+0.136 (n=53)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2022.4544 (IC base=+0.097)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4171` → IC=+0.167 (n=22)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio` |x|> 0.4171 (IC base=+0.094)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.157 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 8.0 (IC base=+0.094)

- **PATRÓN** `total_vol_5m` < `549.0615` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `total_vol_5m` < 549.0615 (IC base=+0.094)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4012` → IC=+0.202 (n=45)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4012 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.222 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `3228.9504` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3228.9504 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.140 (n=23)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 73.0 (IC base=+0.129)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.3956` → IC=+0.127 (n=57)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.64€ cuando `delta_ratio` |x|> 0.3956 (IC base=+0.064)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.152 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 4.0 (IC base=+0.064)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=31)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.064)

- **PATRÓN** `libro_liquidez` > `3395.535` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3395.535 (IC base=+0.064)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` < `0.0084` → IC=-0.180 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0084
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=71)

- **FILTRO** `T_h` > `63.9853` → IC=-0.345 (n=101)

  - _Acción_: SKIP cuando `T_h` > 63.9853
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=35)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `87.9957` → IC=-0.460 (n=23)

  - _Acción_: SKIP cuando `T_h` > 87.9957
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=25)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.283 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=-0.146)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `T_h` > `144.5498` → IC=-0.339 (n=29)

  - _Acción_: SKIP cuando `T_h` > 144.5498
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=90)

- **FILTRO** `T_h` < `135.9851` → IC=-0.436 (n=45)

  - _Acción_: SKIP cuando `T_h` < 135.9851
  - _Potencial_: sin este filtro IC_bueno=-0.266 (n=45)

- **PATRÓN** `pct_vs_K` |x|≤ `1.3968` → IC=+0.250 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 1.3968 (IC base=-0.054)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **PATRÓN** `T_h` < `111.9808` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `T_h` < 111.9808 (IC base=+0.092)

- **PATRÓN** `pct_vs_K` |x|≤ `1.4454` → IC=+0.308 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 1.4454 (IC base=+0.092)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `T_h` > `87.9957` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `T_h` > 87.9957
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=20)

- **FILTRO** `sigma_h` < `0.0045` → IC=-0.357 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0045
  - _Potencial_: sin este filtro IC_bueno=-0.292 (n=22)

### STREAK_FADE_15M
- **FILTRO** `ballena_activa_n` > `67.0` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `ballena_activa_n` > 67.0
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=35)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=89)

- **PATRÓN** `streak_estiramiento` < `0.4813` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.4813 (IC base=+0.044)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.203 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.044)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `ballena_activa_n` > `18.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `ballena_activa_n` > 18.0
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=56)

- **FILTRO** `streak_estiramiento` > `0.4374` → IC=-0.156 (n=30)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4374
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=15)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=55)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.132 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=11)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.250 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=89)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=98)

- **FILTRO** `streak_estiramiento` > `0.6136` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.6136
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=55)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=99)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=171)

- **PATRÓN** `streak_estiramiento` < `0.3225` → IC=+0.156 (n=30)

  - _Acción_: Kelly boost +0.78€ cuando `streak_estiramiento` < 0.3225 (IC base=+0.010)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=343)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=179)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=243)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.162 (n=69)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 5.0 (IC base=+0.065)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=1245)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=705)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=713)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.154 (n=131)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.003 (IC base=+0.117)

- **PATRÓN** `drift_60min` |x|≤ `0.188` → IC=+0.126 (n=391)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.63€ cuando `drift_60min` |x|≤ 0.188 (IC base=+0.117)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0684` → IC=+0.125 (n=390)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.62€ cuando `delta_ratio_macro` |x|> 0.0684 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.121 (n=415)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 4.0 (IC base=+0.117)

- **PATRÓN** `ibs_15` > `0.5294` → IC=+0.205 (n=391)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5294 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `0.398` → IC=+0.173 (n=102)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.398 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.763` → IC=+0.245 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.763 (IC base=+0.117)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.124 (n=410)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.01 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `7519.476` → IC=+0.167 (n=130)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 7519.476 (IC base=+0.117)

### UPDOWN_GBM#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1001` → IC=-0.128 (n=181)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1001
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=368)

- **FILTRO** `ibs_15` < `0.259` → IC=-0.176 (n=137)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.259
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=412)

- **FILTRO** `sigma_ewma_delta_pct` > `6.578` → IC=-0.209 (n=53)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.578
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=496)

### UPDOWN_GBM#60min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0347` → IC=-0.192 (n=24)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0347
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=49)

- **FILTRO** `ibs_15` < `0.2105` → IC=-0.214 (n=19)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.2105
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=40)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=19)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `sigma_h` < `0.0041` → IC=-0.260 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0041
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=69)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.239 (n=21)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=71)

- **FILTRO** `ibs_15` > `0.7088` → IC=-0.167 (n=22)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.7088
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=70)

- **FILTRO** `ibs_15` < `0.2983` → IC=-0.180 (n=23)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.2983
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=69)

- **FILTRO** `libro_liquidez` < `13630.9549` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `libro_liquidez` < 13630.9549
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=69)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.160 (n=101)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0038 (IC base=+0.156)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.200 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.1944` → IC=+0.184 (n=115)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1944 (IC base=+0.156)

- **PATRÓN** `drift_15min` |x|≤ `0.4671` → IC=+0.183 (n=77)

  - _Acción_: Kelly boost +0.92€ cuando `drift_15min` |x|≤ 0.4671 (IC base=+0.156)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2457` → IC=+0.200 (n=38)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2457 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.181 (n=117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 4.0 (IC base=+0.156)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.167 (n=118)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 17.0 (IC base=+0.156)

- **PATRÓN** `ibs_15` > `0.8791` → IC=+0.256 (n=76)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8791 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.3217` → IC=+0.211 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3217 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` < `0.546` → IC=+0.164 (n=126)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.546 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.029` → IC=+0.200 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.029 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `11757.2155` → IC=+0.185 (n=52)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 11757.2155 (IC base=+0.156)

### UPDOWN_GBM#BTC#5min
- **FILTRO** `sigma_h` > `0.0048` → IC=-0.184 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0048
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=52)

- **FILTRO** `sigma_h` < `0.0035` → IC=-0.208 (n=22)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0035
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=47)

- **FILTRO** `ibs_15` < `0.1271` → IC=-0.289 (n=17)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1271
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=52)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `hora_utc` > `19.0` → IC=-0.132 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=83)

- **FILTRO** `ibs_15` < `0.8481` → IC=-0.154 (n=50)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8481
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=50)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `ibs_15` < `0.617` → IC=-0.237 (n=36)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.617
  - _Potencial_: sin este filtro IC_bueno=+0.231 (n=76)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.121 (n=85)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.0049 (IC base=+0.079)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2671` → IC=+0.200 (n=28)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2671 (IC base=+0.079)

- **PATRÓN** `ibs_15` > `0.617` → IC=+0.231 (n=76)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.617 (IC base=+0.079)

- **PATRÓN** `dist_vwap_pct` < `0.092` → IC=+0.133 (n=47)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.092 (IC base=+0.079)

- **PATRÓN** `sigma_ewma_delta_pct` > `15.544` → IC=+0.188 (n=30)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 15.544 (IC base=+0.079)

### UPDOWN_GBM#ETH#5min
- **FILTRO** `hora_utc` > `8.0` → IC=-0.200 (n=28)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=64)

- **FILTRO** `dist_vwap_pct` > `0.1641` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1641
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=77)

- **FILTRO** `drift_15min` |x|> `0.513` → IC=-0.149 (n=129)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.513
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=388)

- **FILTRO** `sigma_ewma_delta_pct` > `9.964` → IC=-0.125 (n=86)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.964
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=431)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `ibs_15` < `0.6` → IC=-0.177 (n=29)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.265 (n=32)

- **PATRÓN** `ibs_15` > `0.6` → IC=+0.265 (n=32)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6 (IC base=+0.056)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.477` → IC=+0.318 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.477 (IC base=+0.056)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0264` → IC=-0.224 (n=27)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0264
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=53)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1009` → IC=-0.179 (n=26)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1009
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=54)

- **FILTRO** `ibs_15` < `0.2222` → IC=-0.409 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.2222
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=60)

### UPDOWN_GBM#SOL#60min
- **FILTRO** `sigma_h` > `0.0127` → IC=-0.214 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0127
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=38)

- **FILTRO** `sigma_ewma_delta_pct` < `3.393` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 3.393
  - _Potencial_: sin este filtro IC_bueno=+0.375 (n=6)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.265 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=-0.009)

- **PATRÓN** `ibs_15` > `0.5` → IC=+0.129 (n=33)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.64€ cuando `ibs_15` > 0.5 (IC base=-0.009)

- **PATRÓN** `dist_vwap_pct` < `0.3805` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` < 0.3805 (IC base=-0.009)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `delta_ratio_macro` |x|> `0.0597` → IC=+0.135 (n=102)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio_macro` |x|> 0.0597 (IC base=+0.099)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.140 (n=48)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 15.0 (IC base=+0.099)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.167 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 6.0 (IC base=+0.099)

- **PATRÓN** `ibs_15` > `0.4444` → IC=+0.167 (n=103)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.83€ cuando `ibs_15` > 0.4444 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `0.3587` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3587 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.569` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.569 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `2503.3208` → IC=+0.156 (n=91)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2503.3208 (IC base=+0.099)

- **PATRÓN** `ibs_15` < `0.125` → IC=+0.204 (n=113)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.125 (IC base=+0.046)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.393 (n=54)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.312)

- **PATRÓN** `drift_60min` |x|≤ `0.1159` → IC=+0.338 (n=109)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1159 (IC base=+0.312)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1506` → IC=+0.327 (n=108)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1506 (IC base=+0.312)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.343 (n=151)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.312)

- **PATRÓN** `ibs_15` > `0.814` → IC=+0.357 (n=145)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.814 (IC base=+0.312)

- **PATRÓN** `dist_vwap_pct` > `0.157` → IC=+0.342 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.157 (IC base=+0.312)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.888` → IC=+0.328 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.888 (IC base=+0.312)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.729` → IC=+0.309 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.729 (IC base=+0.312)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.312 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.312)

- **PATRÓN** `libro_liquidez` > `7152.8647` → IC=+0.342 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7152.8647 (IC base=+0.312)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1986` → IC=+0.307 (n=81)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1986 (IC base=+0.290)

- **PATRÓN** `sigma_h` < `0.0024` → IC=+0.291 (n=41)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0024 (IC base=+0.290)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.379 (n=31)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.16` → IC=+0.319 (n=81)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.16 (IC base=+0.290)

- **PATRÓN** `drift_15min` |x|≤ `0.4155` → IC=+0.314 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4155 (IC base=+0.290)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1236` → IC=+0.400 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1236 (IC base=+0.290)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.322 (n=99)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.290)

- **PATRÓN** `ibs_15` > `0.838` → IC=+0.333 (n=82)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.838 (IC base=+0.290)

- **PATRÓN** `dist_vwap_pct` > `0.2738` → IC=+0.375 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2738 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.145` → IC=+0.289 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.145 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.39` → IC=+0.293 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.39 (IC base=+0.290)

- **PATRÓN** `libro_liquidez` > `9160.5319` → IC=+0.341 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9160.5319 (IC base=+0.290)

- **PATRÓN** `ballena_activa_n` < `581.0` → IC=+0.400 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 581.0 (IC base=+0.290)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.353 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.333)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.357 (n=47)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.333)

- **PATRÓN** `drift_60min` |x|≤ `0.0823` → IC=+0.382 (n=32)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0823 (IC base=+0.333)

- **PATRÓN** `delta_ratio_macro` |x|> `0.13` → IC=+0.378 (n=47)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.13 (IC base=+0.333)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2773` → IC=+0.354 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2773 (IC base=+0.333)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.338 (n=66)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.333)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.331 (n=69)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.333)

- **PATRÓN** `ibs_15` > `0.8055` → IC=+0.408 (n=63)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8055 (IC base=+0.333)

- **PATRÓN** `dist_vwap_pct` < `0.157` → IC=+0.342 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.157 (IC base=+0.333)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.86` → IC=+0.372 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.86 (IC base=+0.333)

- **PATRÓN** `libro_liquidez` > `3271.2182` → IC=+0.337 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3271.2182 (IC base=+0.333)

- **PATRÓN** `ballena_activa_n` < `184.0` → IC=+0.353 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 184.0 (IC base=+0.333)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0099` → IC=-0.179 (n=266)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0099
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=799)

- **FILTRO** `ibs_15` < `0.4601` → IC=-0.250 (n=102)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.4601
  - _Potencial_: sin este filtro IC_bueno=+0.158 (n=308)

- **FILTRO** `sigma_ewma_delta_pct` > `17.701` → IC=-0.175 (n=364)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.701
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=2762)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.357` → IC=+0.146 (n=145)

  - _Acción_: Kelly boost +0.73€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.357 (IC base=-0.064)

- **PATRÓN** `ibs_15` > `0.4601` → IC=+0.158 (n=308)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.79€ cuando `ibs_15` > 0.4601 (IC base=-0.064)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0648` → IC=+0.250 (n=210)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0648 (IC base=-0.076)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2993` → IC=+0.273 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2993 (IC base=-0.076)

- **PATRÓN** `ibs_15` < `0.3696` → IC=+0.312 (n=211)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3696 (IC base=-0.076)

- **PATRÓN** `dist_vwap_pct` < `0.2567` → IC=+0.249 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2567 (IC base=-0.076)

- **PATRÓN** `ballena_activa_n` < `66.0` → IC=+0.254 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 66.0 (IC base=-0.076)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0075` → IC=-0.247 (n=168)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0075
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=506)

- **FILTRO** `sigma_h` < `0.0036` → IC=-0.219 (n=222)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0036
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=452)

- **FILTRO** `hora_utc` > `17.0` → IC=-0.259 (n=143)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=531)

- **FILTRO** `sigma_ewma_delta_pct` > `19.944` → IC=-0.266 (n=126)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.944
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=548)

- **FILTRO** `libro_liquidez` < `15259.6134` → IC=-0.222 (n=444)

  - _Acción_: SKIP cuando `libro_liquidez` < 15259.6134
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=230)

- **PATRÓN** `ibs_15` > `0.7496` → IC=+0.292 (n=22)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7496 (IC base=+0.017)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.4646` → IC=-0.351 (n=45)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.4646
  - _Potencial_: sin este filtro IC_bueno=+0.186 (n=138)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=166)

- **PATRÓN** `drift_60min` |x|≤ `0.0629` → IC=+0.188 (n=46)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.0629 (IC base=+0.051)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3719` → IC=+0.224 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3719 (IC base=+0.051)

- **PATRÓN** `ibs_15` > `0.4646` → IC=+0.186 (n=138)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.93€ cuando `ibs_15` > 0.4646 (IC base=+0.051)

- **PATRÓN** `libro_liquidez` > `10043.6494` → IC=+0.208 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10043.6494 (IC base=+0.051)

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1043` → IC=+0.253 (n=79)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1043 (IC base=+0.236)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.250 (n=118)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.236)

- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.241 (n=79)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.236)

- **PATRÓN** `drift_15min` |x|≤ `0.4267` → IC=+0.262 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4267 (IC base=+0.236)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0822` → IC=+0.250 (n=118)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0822 (IC base=+0.236)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3069` → IC=+0.244 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3069 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.250 (n=54)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.318 (n=42)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.236)

- **PATRÓN** `ibs_15` < `0.3696` → IC=+0.325 (n=118)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3696 (IC base=+0.236)

- **PATRÓN** `dist_vwap_pct` < `0.2166` → IC=+0.242 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2166 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.717` → IC=+0.263 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.717 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `13769.0298` → IC=+0.262 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13769.0298 (IC base=+0.236)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1583` → IC=-0.174 (n=87)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1583
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=169)

- **FILTRO** `drift_15min` |x|> `0.7912` → IC=-0.238 (n=63)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.7912
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=193)

- **PATRÓN** `ibs_15` > `0.8125` → IC=+0.206 (n=15)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8125 (IC base=-0.108)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2219` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2219 (IC base=-0.057)

- **PATRÓN** `ibs_15` < `0.2796` → IC=+0.218 (n=37)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2796 (IC base=-0.057)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `drift_15min` |x|> `1.159` → IC=-0.257 (n=68)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.159
  - _Potencial_: sin este filtro IC_bueno=-0.127 (n=207)

- **FILTRO** `sigma_ewma_delta_pct` > `14.966` → IC=-0.218 (n=37)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 14.966
  - _Potencial_: sin este filtro IC_bueno=-0.150 (n=238)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.278 (n=25)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=250)

- **FILTRO** `libro_liquidez` < `2501.2592` → IC=-0.243 (n=68)

  - _Acción_: SKIP cuando `libro_liquidez` < 2501.2592
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=207)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0981` → IC=+0.444 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0981 (IC base=-0.067)

- **PATRÓN** `ibs_15` > `0.1321` → IC=+0.362 (n=27)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.1321 (IC base=-0.067)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.282 (n=259)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.280)

- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.298 (n=117)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0055 (IC base=+0.280)

- **PATRÓN** `drift_60min` |x|≤ `0.0537` → IC=+0.332 (n=87)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0537 (IC base=+0.280)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1879` → IC=+0.317 (n=118)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1879 (IC base=+0.280)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1236` → IC=+0.352 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1236 (IC base=+0.280)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.310 (n=272)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.280)

- **PATRÓN** `ibs_15` > `0.9678` → IC=+0.349 (n=117)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9678 (IC base=+0.280)

- **PATRÓN** `dist_vwap_pct` > `0.5198` → IC=+0.365 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5198 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.694` → IC=+0.289 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.694 (IC base=+0.280)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.281 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `11800.2375` → IC=+0.324 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11800.2375 (IC base=+0.280)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0024` → IC=+0.265 (n=49)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0024 (IC base=+0.265)

- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.304 (n=49)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0057 (IC base=+0.265)

- **PATRÓN** `drift_60min` |x|≤ `0.162` → IC=+0.294 (n=129)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.162 (IC base=+0.265)

- **PATRÓN** `drift_15min` |x|≤ `0.7294` → IC=+0.264 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7294 (IC base=+0.265)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2616` → IC=+0.304 (n=49)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2616 (IC base=+0.265)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1236` → IC=+0.328 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1236 (IC base=+0.265)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.331 (n=69)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.265)

- **PATRÓN** `ibs_15` > `0.9691` → IC=+0.309 (n=66)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9691 (IC base=+0.265)

- **PATRÓN** `dist_vwap_pct` > `0.3665` → IC=+0.362 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3665 (IC base=+0.265)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.453` → IC=+0.271 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.453 (IC base=+0.265)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.717` → IC=+0.279 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.717 (IC base=+0.265)

- **PATRÓN** `libro_liquidez` > `13285.6042` → IC=+0.294 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13285.6042 (IC base=+0.265)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.309 (n=113)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0074 (IC base=+0.296)

- **PATRÓN** `drift_60min` |x|≤ `0.0637` → IC=+0.346 (n=50)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0637 (IC base=+0.296)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0673` → IC=+0.325 (n=101)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0673 (IC base=+0.296)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3059` → IC=+0.351 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3059 (IC base=+0.296)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.325 (n=118)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.296)

- **PATRÓN** `ibs_15` > `0.963` → IC=+0.368 (n=51)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.963 (IC base=+0.296)

- **PATRÓN** `dist_vwap_pct` > `0.6569` → IC=+0.380 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6569 (IC base=+0.296)

- **PATRÓN** `sigma_ewma_delta_pct` < `14.575` → IC=+0.302 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 14.575 (IC base=+0.296)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.296)

- **PATRÓN** `libro_liquidez` > `9906.9054` → IC=+0.387 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9906.9054 (IC base=+0.296)

- **PATRÓN** `ballena_activa_n` < `106.0` → IC=+0.362 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 106.0 (IC base=+0.296)

### UPDOWN_OU_5M
- **FILTRO** `sigma_h` > `0.0061` → IC=-0.258 (n=31)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0061
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=97)

- **FILTRO** `drift_60min` |x|> `0.3197` → IC=-0.167 (n=31)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.3197
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=97)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1212` → IC=-0.170 (n=98)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1212
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=298)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.154 (n=53)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=27)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0902` → IC=-0.184 (n=17)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0902
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=52)

- **FILTRO** `drift_15min` |x|> `0.2326` → IC=-0.222 (n=16)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.2326
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=18)

### UPDOWN_OU_5M#DOGE#5min
- **FILTRO** `drift_15min` |x|> `0.3434` → IC=-0.184 (n=17)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3434
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `sigma_h` < `0.0054` → IC=-0.167 (n=16)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0054
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### WEEKLY_PRICE
- **PATRÓN** `T_h` < `79.3918` → IC=+0.222 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 79.3918 (IC base=+0.100)

- **PATRÓN** `ratio` < `0.972` → IC=+0.460 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.972 (IC base=+0.100)

- **PATRÓN** `T_h` > `146.0966` → IC=+0.431 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0966 (IC base=+0.342)

- **PATRÓN** `ratio` < `1.0189` → IC=+0.214 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 1.0189 (IC base=+0.342)

- **PATRÓN** `ratio` > `1.0147` → IC=+0.198 (n=51)

  - _Acción_: Kelly boost +0.99€ cuando `ratio` > 1.0147 (IC base=+0.342)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` < `57.6124` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `T_h` < 57.6124 (IC base=+0.094)

- **PATRÓN** `T_h` < `111.9558` → IC=+0.335 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 111.9558 (IC base=+0.266)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` < `113.3454` → IC=+0.242 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 113.3454 (IC base=+0.138)

- **PATRÓN** `T_h` < `87.9969` → IC=+0.322 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 87.9969 (IC base=+0.306)

- **PATRÓN** `T_h` > `145.7688` → IC=+0.324 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7688 (IC base=+0.306)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `135.9824` → IC=+0.436 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 135.9824 (IC base=+0.413)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-SIGMA-SOL-60MIN**: `UPDOWN_GBM#SOL#60min` gana cuando sigma_h < 0.0058 (IC=+0.265 n=15). Implementar como filtro pre-predicción en shadow_predict.py.
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5294 sube el IC de +0.117 a +0.205 en UPDOWN_GBM#15min (n=391). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.8791 sube el IC de +0.156 a +0.256 en UPDOWN_GBM#BTC#15min (n=76). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.617 sube el IC de +0.079 a +0.231 en UPDOWN_GBM#ETH#15min (n=76). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.056 a +0.265 en UPDOWN_GBM#SOL#15min (n=32). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.4444 sube el IC de +0.099 a +0.167 en UPDOWN_GBM#XRP#15min (n=103). Ya aplicado como kelly_boost=+0.83€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.125 sube el IC de +0.046 a +0.204 en UPDOWN_GBM#XRP#15min (n=113). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.4601 sube el IC de -0.064 a +0.158 en UPDOWN_GBM_15M_TARDIO (n=308). Ya aplicado como kelly_boost=+0.79€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3696 sube el IC de -0.076 a +0.312 en UPDOWN_GBM_15M_TARDIO (n=211). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7496 sube el IC de +0.017 a +0.292 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=22). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.4646 sube el IC de +0.051 a +0.186 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=138). Ya aplicado como kelly_boost=+0.93€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3696 sube el IC de +0.236 a +0.325 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=118). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8125 sube el IC de -0.108 a +0.206 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=15). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.2796 sube el IC de -0.057 a +0.218 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=37). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS > 0.1321 sube el IC de -0.067 a +0.362 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=27). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.9678 sube el IC de +0.280 a +0.349 en UPDOWN_GBM_IBS_ALTO (n=117). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.9691 sube el IC de +0.265 a +0.309 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=66). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.963 sube el IC de +0.296 a +0.368 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=51). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.814 sube el IC de +0.312 a +0.357 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=145). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.838 sube el IC de +0.290 a +0.333 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=82). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.8055 sube el IC de +0.333 a +0.408 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=63). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#SOL#sniper` — IC=+0.472 n=34. Faltan ~6 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#SOL` — IC=+0.472 n=34. Faltan ~6 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min` — IC=+0.357 n=33. Faltan ~7 resoluciones para umbral n≥40. ETA: ~5h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL` — IC=+0.357 n=33. Faltan ~7 resoluciones para umbral n≥40. ETA: ~5h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min` — IC=+0.167 n=31. Faltan ~9 resoluciones para umbral n≥40. ETA: ~6h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 642 | +0.090 | +45.13€ | 1 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 642 | +0.090 | +45.13€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 391 | +0.113 | +35.01€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 391 | +0.113 | +35.01€ | 1 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 222 | +0.036 | -0.81€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 222 | +0.036 | -0.81€ | 7 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 29 | +0.177 | +10.93€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 29 | +0.177 | +10.93€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 10877 | -0.095 | -1797.84€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 766 | -0.055 | -132.55€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 10111 | -0.098 | -1665.29€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 1375 | -0.038 | -274.69€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 1375 | -0.038 | -274.69€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 766 | -0.055 | -132.55€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 766 | -0.055 | -132.55€ | 3 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 1401 | -0.144 | -425.08€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 1401 | -0.144 | -425.08€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 2923 | -0.064 | -288.97€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 2923 | -0.064 | -288.97€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 2528 | -0.096 | -221.94€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 2528 | -0.096 | -221.94€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 1884 | -0.163 | -454.61€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 1884 | -0.163 | -454.61€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 753 | -0.062 | +346.83€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 217 | -0.002 | +88.47€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 536 | -0.086 | +258.36€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 753 | -0.062 | +346.83€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 217 | -0.002 | +88.47€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 536 | -0.086 | +258.36€ | 0 | 0 |
| 🚫 CANDIDATA9_BOT_CONSENSO | 12 | -0.129 | -6.46€ | 0 | 0 |
| 🚫 CANDIDATA9_BOT_CONSENSO#5min | 12 | -0.129 | -6.46€ | 0 | 0 |
| 🚫 CANDIDATA9_BOT_CONSENSO#BTC | 12 | -0.129 | -6.46€ | 0 | 0 |
| 🚫 CANDIDATA9_BOT_CONSENSO#BTC#5min | 12 | -0.129 | -6.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 35504 | +0.115 | -2205.42€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 6407 | +0.186 | -232.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 113 | -0.083 | -46.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 25679 | +0.098 | -1874.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 3305 | +0.119 | -52.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 4307 | +0.069 | -684.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 21 | -0.065 | +2.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#240min | 5 | -0.089 | -6.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 4281 | +0.070 | -679.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 7270 | +0.133 | -160.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 1815 | +0.197 | -97.08€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 4272 | +0.110 | -92.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 1141 | +0.127 | +51.37€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 4317 | +0.084 | -509.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 22 | +0.083 | +3.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 4294 | +0.084 | -511.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 7801 | +0.127 | -122.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 2326 | +0.168 | -16.43€ | 0 | 8 |
| 🚫 FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 4276 | +0.113 | -70.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 1187 | +0.101 | -26.72€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 7503 | +0.133 | -462.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 2206 | +0.200 | -124.31€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 51 | +0.028 | -6.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 4269 | +0.100 | -254.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 977 | +0.132 | -77.26€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#XRP | 4306 | +0.109 | -266.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 17 | -0.022 | -0.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 4287 | +0.110 | -265.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 6312 | +0.175 | -485.15€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 6312 | +0.175 | -485.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 1593 | +0.167 | -169.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 1593 | +0.167 | -169.75€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 123 | -0.116 | +1.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 123 | -0.116 | +1.57€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 1570 | +0.166 | -171.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 1570 | +0.166 | -171.25€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 1418 | +0.232 | -38.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 1418 | +0.232 | -38.94€ | 0 | 2 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 1529 | +0.183 | -120.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 1529 | +0.183 | -120.53€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 321 | +0.447 | +4.44€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 321 | +0.447 | +4.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 123 | +0.444 | +1.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 123 | +0.444 | +1.89€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 120 | +0.434 | -0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 120 | +0.434 | -0.24€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 75 | +0.448 | +2.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 75 | +0.448 | +2.65€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 18267 | +0.191 | -1602.09€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 18267 | +0.191 | -1602.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 3316 | +0.131 | -590.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 3316 | +0.131 | -590.54€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 2857 | +0.234 | -63.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 2857 | +0.234 | -63.87€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 3129 | +0.168 | -380.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 3129 | +0.168 | -380.22€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 2906 | +0.226 | -99.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 2906 | +0.226 | -99.86€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 2982 | +0.212 | -163.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 2982 | +0.212 | -163.70€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 3077 | +0.185 | -303.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 3077 | +0.185 | -303.91€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 6677 | +0.133 | +244.61€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 6677 | +0.133 | +244.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 3323 | +0.139 | +155.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 3323 | +0.139 | +155.65€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 3354 | +0.127 | +88.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 3354 | +0.127 | +88.95€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 813 | +0.296 | -0.90€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 813 | +0.296 | -0.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 349 | +0.281 | -8.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 349 | +0.281 | -8.04€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 379 | +0.298 | +5.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 379 | +0.298 | +5.92€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 85 | +0.339 | +1.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 85 | +0.339 | +1.21€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 347 | +0.414 | -15.01€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 347 | +0.414 | -15.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 154 | +0.410 | -7.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 154 | +0.410 | -7.73€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 160 | +0.420 | -6.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 160 | +0.420 | -6.31€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 33 | +0.357 | -0.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 33 | +0.357 | -0.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 277 | +0.084 | -7.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 82 | +0.095 | -1.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 195 | +0.079 | -6.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 11 | +0.064 | +0.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 11 | +0.064 | +0.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 226 | +0.092 | -2.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 31 | +0.167 | +3.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 195 | +0.079 | -6.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 40 | +0.024 | -6.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 40 | +0.024 | -6.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 8001 | +0.095 | -272.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 779 | +0.071 | -18.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 7222 | +0.098 | -254.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 5247 | +0.097 | -106.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 779 | +0.071 | -18.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 4468 | +0.101 | -87.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 403 | +0.127 | +13.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 403 | +0.127 | +13.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 2351 | +0.087 | -180.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 2351 | +0.087 | -180.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 461 | +0.284 | -30.91€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 461 | +0.284 | -30.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 461 | +0.284 | -30.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 461 | +0.284 | -30.91€ | 0 | 3 |
| ✅ GBM_LATE_15M | 8519 | +0.044 | +2759.68€ | 0 | 14 |
| ✅ GBM_LATE_15M#15min | 8519 | +0.044 | +2759.68€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 1190 | +0.176 | +763.77€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 1190 | +0.176 | +763.77€ | 0 | 21 |
| ✅ GBM_LATE_15M#BTC | 1223 | +0.171 | +711.25€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 1223 | +0.171 | +711.25€ | 0 | 29 |
| ✅ GBM_LATE_15M#DOGE | 1194 | +0.191 | +831.60€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 1194 | +0.191 | +831.60€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 1394 | -0.047 | +36.44€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 1394 | -0.047 | +36.44€ | 4 | 12 |
| ✅ GBM_LATE_15M#SOL | 1525 | -0.048 | +151.41€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 1525 | -0.048 | +151.41€ | 5 | 2 |
| ✅ GBM_LATE_15M#XRP | 1993 | -0.067 | +265.21€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 1993 | -0.067 | +265.21€ | 4 | 7 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 9391 | +0.046 | +3702.59€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 9391 | +0.046 | +3702.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 1487 | -0.017 | +673.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 1487 | -0.017 | +673.54€ | 2 | 4 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 2040 | -0.040 | +163.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 2040 | -0.040 | +163.37€ | 1 | 2 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 1058 | +0.241 | +968.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 1058 | +0.241 | +968.85€ | 0 | 23 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 1533 | -0.053 | -20.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 1533 | -0.053 | -20.38€ | 10 | 2 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 1632 | -0.027 | +340.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 1632 | -0.027 | +340.23€ | 7 | 8 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 1641 | +0.250 | +1576.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 1641 | +0.250 | +1576.98€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 6933 | +0.171 | +4828.06€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 6933 | +0.171 | +4828.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 911 | +0.189 | +655.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 911 | +0.189 | +655.12€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 1177 | +0.162 | +783.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 1177 | +0.162 | +783.94€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 901 | +0.203 | +701.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 901 | +0.203 | +701.79€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 1148 | +0.157 | +733.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 1148 | +0.157 | +733.33€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 1307 | +0.129 | +819.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 1307 | +0.129 | +819.57€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 1489 | +0.195 | +1134.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 1489 | +0.195 | +1134.31€ | 0 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 1374 | +0.081 | +301.67€ | 0 | 10 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 1374 | +0.081 | +301.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 56 | +0.086 | +14.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 56 | +0.086 | +14.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 351 | +0.084 | +94.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 351 | +0.084 | +94.84€ | 3 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 199 | +0.127 | +78.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 199 | +0.127 | +78.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 234 | +0.178 | +77.45€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 234 | +0.178 | +77.45€ | 2 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 321 | -0.020 | +4.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 321 | -0.020 | +4.04€ | 4 | 3 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 213 | +0.077 | +32.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 213 | +0.077 | +32.53€ | 0 | 9 |
| ✅ GBM_LATE_15M_TARDIO | 8132 | +0.169 | +5477.17€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#15min | 8132 | +0.169 | +5477.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 1142 | +0.198 | +852.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 1142 | +0.198 | +852.17€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 1324 | +0.161 | +857.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 1324 | +0.161 | +857.00€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 1123 | +0.211 | +898.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 1123 | +0.211 | +898.86€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 1264 | +0.143 | +732.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 1264 | +0.143 | +732.15€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 1449 | +0.104 | +748.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 1449 | +0.104 | +748.55€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 1830 | +0.199 | +1388.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 1830 | +0.199 | +1388.44€ | 0 | 22 |
| ✅ GBM_LATE_5M | 2416 | +0.124 | +1061.77€ | 1 | 21 |
| ✅ GBM_LATE_5M#5min | 2416 | +0.124 | +1061.77€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 95 | +0.222 | +72.24€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 95 | +0.222 | +72.24€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 844 | +0.127 | +423.83€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 844 | +0.127 | +423.83€ | 2 | 15 |
| ✅ GBM_LATE_5M#DOGE | 239 | +0.143 | +115.21€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 239 | +0.143 | +115.21€ | 0 | 8 |
| ✅ GBM_LATE_5M#ETH | 766 | +0.132 | +327.47€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 766 | +0.132 | +327.47€ | 0 | 28 |
| ✅ GBM_LATE_5M#SOL | 126 | -0.023 | -1.19€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 126 | -0.023 | -1.19€ | 4 | 0 |
| ✅ GBM_LATE_5M#XRP | 346 | +0.112 | +124.21€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 346 | +0.112 | +124.21€ | 0 | 0 |
| ✅ GBM_LATE_60M | 535 | -0.023 | +100.00€ | 5 | 11 |
| ✅ GBM_LATE_60M#60min | 535 | -0.023 | +100.00€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 184 | +0.011 | +6.74€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 184 | +0.011 | +6.74€ | 2 | 4 |
| ✅ GBM_LATE_60M#ETH | 193 | +0.013 | +65.66€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 193 | +0.013 | +65.66€ | 2 | 9 |
| ✅ GBM_LATE_60M#SOL | 158 | -0.106 | +27.59€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 158 | -0.106 | +27.59€ | 3 | 1 |
| 🚫 GBM_LATE_60M_FADE | 195 | -0.302 | -33.28€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 195 | -0.302 | -33.28€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 77 | -0.260 | -7.87€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 77 | -0.260 | -7.87€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 65 | -0.351 | -19.05€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 65 | -0.351 | -19.05€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 53 | -0.282 | -6.35€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 53 | -0.282 | -6.35€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 348 | +0.040 | +3.16€ | 1 | 3 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 348 | +0.040 | +3.16€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 144 | +0.027 | +7.31€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 144 | +0.027 | +7.31€ | 3 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 87 | +0.073 | +0.32€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 87 | +0.073 | +0.32€ | 0 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 117 | +0.029 | -4.47€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 117 | +0.029 | -4.47€ | 2 | 5 |
| ✅ LATE_WINDOW_5MIN | 25 | +0.278 | +10.54€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 25 | +0.278 | +10.54€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 25 | +0.278 | +10.54€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 25 | +0.278 | +10.54€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 339 | +0.107 | +93.25€ | 0 | 5 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 339 | +0.107 | +93.25€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 339 | +0.107 | +93.25€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 339 | +0.107 | +93.25€ | 0 | 5 |
| ✅ LIQUIDACIONES_15M | 240 | -0.099 | -29.49€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 240 | -0.099 | -29.49€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 59 | -0.090 | -7.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 59 | -0.090 | -7.07€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 23 | -0.180 | -4.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 23 | -0.180 | -4.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 49 | -0.088 | -6.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 49 | -0.088 | -6.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 57 | +0.009 | -0.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 57 | +0.009 | -0.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 47 | -0.173 | -9.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 47 | -0.173 | -9.46€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 811 | -0.017 | -16.85€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 811 | -0.017 | -16.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 50 | +0.019 | -1.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 50 | +0.019 | -1.14€ | 0 | 1 |
| ✅ LIQUIDACIONES_5M#BTC | 123 | -0.044 | -5.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 123 | -0.044 | -5.35€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 68 | -0.100 | -7.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 68 | -0.100 | -7.86€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 230 | +0.022 | +9.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 230 | +0.022 | +9.31€ | 3 | 2 |
| ✅ LIQUIDACIONES_5M#SOL | 284 | +0.000 | -4.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 284 | +0.000 | -4.18€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 56 | -0.121 | -7.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 56 | -0.121 | -7.62€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M | 471 | -0.012 | -4.42€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 471 | -0.012 | -4.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 149 | -0.036 | -10.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 149 | -0.036 | -10.33€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 144 | +0.000 | +1.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 144 | +0.000 | +1.50€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 178 | +0.000 | +4.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 178 | +0.000 | +4.41€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 4902 | -0.003 | -80.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 4902 | -0.003 | -80.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 521 | -0.007 | +0.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 521 | -0.007 | +0.91€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 599 | +0.004 | -9.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 599 | +0.004 | -9.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 906 | -0.001 | -22.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 906 | -0.001 | -22.52€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 1061 | +0.008 | +12.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 1061 | +0.008 | +12.89€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 903 | -0.008 | -31.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 903 | -0.008 | -31.65€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 912 | -0.014 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 912 | -0.014 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 7730 | -0.035 | +200.55€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 7730 | -0.035 | +200.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 1228 | -0.031 | +130.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 1228 | -0.031 | +130.81€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 1346 | -0.030 | -10.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 1346 | -0.030 | -10.68€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 1243 | -0.047 | +78.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 1243 | -0.047 | +78.85€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 1366 | -0.035 | -36.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 1366 | -0.035 | -36.01€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 1279 | -0.037 | +42.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 1279 | -0.037 | +42.65€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 1268 | -0.028 | -5.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 1268 | -0.028 | -5.06€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 556 | -0.061 | -42.52€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 556 | -0.061 | -42.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 104 | -0.038 | -5.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 104 | -0.038 | -5.15€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 67 | -0.065 | -5.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 67 | -0.065 | -5.01€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 36 | -0.105 | -4.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 36 | -0.105 | -4.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 108 | -0.118 | -14.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 108 | -0.118 | -14.05€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 140 | -0.028 | -6.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 140 | -0.028 | -6.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 101 | -0.044 | -7.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 101 | -0.044 | -7.92€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M | 3170 | +0.004 | -5.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3170 | +0.004 | -5.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 126 | -0.039 | -1.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 126 | -0.039 | -1.34€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 185 | +0.008 | -2.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 185 | +0.008 | -2.27€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 136 | +0.000 | -1.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 136 | +0.000 | -1.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1160 | +0.008 | +7.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1160 | +0.008 | +7.79€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1385 | +0.006 | -2.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1385 | +0.006 | -2.03€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 178 | -0.006 | -5.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 178 | -0.006 | -5.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 21477 | -0.076 | +338.59€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 21477 | -0.076 | +338.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 3351 | -0.088 | +402.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 3351 | -0.088 | +402.78€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 3731 | -0.067 | -30.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 3731 | -0.067 | -30.55€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 3479 | -0.084 | +32.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 3479 | -0.084 | +32.62€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 3250 | -0.097 | -166.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 3250 | -0.097 | -166.76€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 4052 | -0.051 | +1.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 4052 | -0.051 | +1.47€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 3614 | -0.076 | +99.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 3614 | -0.076 | +99.03€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6012 | -0.010 | -119.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6012 | -0.010 | -119.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 992 | -0.018 | -21.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 992 | -0.018 | -21.41€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1204 | +0.000 | -15.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1204 | +0.000 | -15.38€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1001 | -0.019 | -30.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1001 | -0.019 | -30.28€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1310 | -0.002 | -14.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1310 | -0.002 | -14.24€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 780 | -0.010 | -14.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 780 | -0.010 | -14.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 725 | -0.020 | -23.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 725 | -0.020 | -23.89€ | 2 | 0 |
| ✅ ORDER_FLOW_5M | 506 | +0.092 | +120.21€ | 1 | 3 |
| ✅ ORDER_FLOW_5M#5min | 370 | +0.105 | +107.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 102 | +0.125 | +44.52€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 102 | +0.125 | +44.52€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#DOGE | 70 | +0.097 | +15.82€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 70 | +0.097 | +15.82€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 62 | +0.094 | +15.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 62 | +0.094 | +15.62€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#SOL | 60 | +0.129 | +22.34€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 60 | +0.129 | +22.34€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 76 | +0.064 | +9.32€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 76 | +0.064 | +9.32€ | 0 | 4 |
| ✅ PRICE_TARGET_GBM | 268 | -0.159 | -23.41€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC | 120 | -0.238 | -35.09€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 105 | -0.266 | -34.36€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 15 | -0.022 | -0.74€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 101 | -0.131 | -3.37€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 82 | -0.143 | -6.34€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 19 | -0.068 | +2.97€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 47 | -0.010 | +15.05€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 40 | +0.000 | +14.48€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 7 | -0.019 | +0.57€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 227 | -0.177 | -26.22€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 41 | -0.058 | +2.80€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE | 209 | -0.187 | +19.09€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 85 | -0.098 | +17.95€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 83 | -0.088 | +18.97€ | 0 | 2 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 84 | -0.279 | -16.66€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 80 | -0.281 | -18.05€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 40 | -0.167 | +17.79€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 38 | -0.150 | +19.63€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#atexpiry | 201 | -0.180 | +20.56€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#reach | 8 | -0.120 | -1.47€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 71 | +0.322 | +16.16€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC | 17 | -0.022 | -2.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 17 | -0.022 | -2.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 20 | +0.318 | +2.90€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 20 | +0.318 | +2.90€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 34 | +0.472 | +16.21€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 34 | +0.472 | +16.21€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 71 | +0.322 | +16.16€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 168 | +0.018 | -2.76€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 168 | +0.018 | -2.76€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 70 | +0.000 | -5.05€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 70 | +0.000 | -5.05€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 10 | +0.000 | -0.13€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 10 | +0.000 | -0.13€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 16 | +0.089 | +1.68€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 16 | +0.089 | +1.68€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 72 | +0.013 | +0.74€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 72 | +0.013 | +0.74€ | 1 | 0 |
| ✅ STREAK_FADE_5M | 1207 | -0.021 | -54.79€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 1207 | -0.021 | -54.79€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 403 | -0.018 | -13.68€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 403 | -0.018 | -13.68€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 440 | -0.007 | -12.12€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 440 | -0.007 | -12.12€ | 3 | 0 |
| ✅ STREAK_FADE_5M#SOL | 132 | -0.037 | -12.47€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 132 | -0.037 | -12.47€ | 2 | 0 |
| ✅ STREAK_FADE_5M#XRP | 232 | -0.043 | -16.53€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 232 | -0.043 | -16.53€ | 4 | 0 |
| ✅ STREAK_FADE_60M | 34 | +0.000 | -0.62€ | 0 | 0 |
| ✅ STREAK_FADE_60M#60min | 34 | +0.000 | -0.62€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 20 | -0.091 | -2.33€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 20 | -0.091 | -2.33€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 14 | +0.087 | +1.71€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 14 | +0.087 | +1.71€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 2529 | +0.030 | +53.22€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 2529 | +0.030 | +53.22€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 842 | +0.034 | +18.11€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 842 | +0.034 | +18.11€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 477 | +0.026 | +9.18€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 477 | +0.026 | +9.18€ | 1 | 1 |
| ✅ STREAK_MOM_5M#SOL | 746 | +0.025 | +7.75€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 746 | +0.025 | +7.75€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 464 | +0.032 | +18.18€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 464 | +0.032 | +18.18€ | 2 | 1 |
| ✅ STRUCT_NO_15M | 3283 | +0.011 | -23.08€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 3283 | +0.011 | -23.08€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 1264 | +0.013 | -7.56€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 1264 | +0.013 | -7.56€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 1282 | +0.016 | -1.62€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 1282 | +0.016 | -1.62€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 737 | -0.003 | -13.91€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 737 | -0.003 | -13.91€ | 2 | 0 |
| ✅ UPDOWN_GBM | 6725 | +0.004 | +144.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 2427 | +0.043 | +232.31€ | 0 | 9 |
| ✅ UPDOWN_GBM#240min | 273 | +0.016 | +1.32€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 3574 | -0.019 | -82.34€ | 3 | 0 |
| ✅ UPDOWN_GBM#60min | 404 | -0.007 | -6.15€ | 3 | 0 |
| ✅ UPDOWN_GBM#BNB | 196 | +0.091 | +38.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 179 | +0.119 | +42.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 8 | -0.040 | -1.01€ | 0 | 0 |
| 🚫 UPDOWN_GBM#BNB#5min | 9 | -0.102 | -2.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 1519 | +0.014 | +64.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 244 | +0.073 | +39.80€ | 5 | 12 |
| ✅ UPDOWN_GBM#BTC#240min | 80 | +0.061 | +5.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 1047 | +0.005 | +23.48€ | 3 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 130 | -0.030 | -6.14€ | 2 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 824 | -0.004 | +0.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 122 | +0.105 | +29.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 9 | +0.021 | +0.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 693 | -0.024 | -29.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 1605 | -0.003 | -7.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 722 | +0.021 | +17.55€ | 1 | 5 |
| ✅ UPDOWN_GBM#ETH#240min | 80 | +0.061 | +4.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 609 | -0.038 | -30.17€ | 4 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 179 | +0.014 | +1.23€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 1642 | -0.008 | -19.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 575 | +0.003 | -1.82€ | 1 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 64 | +0.000 | -2.32€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 896 | -0.011 | -14.33€ | 3 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 95 | -0.015 | -1.24€ | 2 | 3 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 937 | +0.009 | +70.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 585 | +0.059 | +105.16€ | 0 | 8 |
| ✅ UPDOWN_GBM#XRP#240min | 32 | -0.147 | -5.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 320 | -0.065 | -29.19€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 216 | +0.312 | +40.77€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 216 | +0.312 | +40.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 122 | +0.290 | +13.09€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 122 | +0.290 | +13.09€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 94 | +0.333 | +27.68€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 94 | +0.333 | +27.68€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 4191 | -0.073 | +868.37€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 4191 | -0.073 | +868.37€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 303 | -0.051 | +341.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 303 | -0.051 | +341.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 854 | -0.165 | -98.78€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 854 | -0.165 | -98.78€ | 5 | 1 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 77 | +0.070 | +14.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 77 | +0.070 | +14.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 340 | +0.137 | +157.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 340 | +0.137 | +157.70€ | 2 | 16 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 1346 | -0.067 | +245.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 1346 | -0.067 | +245.01€ | 2 | 3 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 1271 | -0.088 | +208.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 1271 | -0.088 | +208.64€ | 4 | 2 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 33 | -0.014 | -2.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 33 | -0.014 | -2.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 33 | -0.014 | -2.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 33 | -0.014 | -2.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 344 | +0.280 | +261.26€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 344 | +0.280 | +261.26€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 194 | +0.265 | +137.99€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 194 | +0.265 | +137.99€ | 0 | 12 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 150 | +0.296 | +123.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 150 | +0.296 | +123.27€ | 0 | 11 |
| ✅ UPDOWN_OU_5M | 524 | -0.087 | -54.90€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#5min | 524 | -0.087 | -54.90€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 284 | -0.063 | -28.78€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 284 | -0.063 | -28.78€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 103 | -0.014 | -1.06€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 103 | -0.014 | -1.06€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 30 | -0.188 | -6.21€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 30 | -0.188 | -6.21€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 39 | -0.159 | -5.76€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 39 | -0.159 | -5.76€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 37 | -0.192 | -6.28€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 37 | -0.192 | -6.28€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 31 | -0.197 | -6.80€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 31 | -0.197 | -6.80€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 1134 | +0.290 | +476.00€ | 0 | 5 |
| ✅ WEEKLY_PRICE#BTC | 342 | +0.209 | +2.62€ | 0 | 2 |
| ✅ WEEKLY_PRICE#ETH | 359 | +0.265 | +92.97€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 433 | +0.371 | +380.41€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.084) — sin ventaja clara. oversold(IBS<0.3): IC=+0.017 n=2410 | neutral: IC=+0.001 n=2578 | overbought(IBS>0.7): IC=+0.085 n=2631
  - _Datos_: n=7946 IC=+0.035 PNL=+711.22€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: (cache 881s) 31 celda(s) GATE OK de 2177 trackeadas

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.003 < 0.08 — monitorear
  - _Datos_: n=575 IC=+0.003 PNL=-1.82€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=359/15 IC=+0.265 PNL=+92.97€ | BTC: n=342/15 IC=+0.209 PNL=+2.62€ | SOL: n=433/15 IC=+0.371 PNL=+380.41€

**🟡 H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.074 n=109085 | tras_1loss IC=+0.046 n=85128 | tras_2loss IC=+0.009 n=38624/40 | gap=+0.066 (umbral 0.05)

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 19 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC, UPDOWN_GBM#SOL
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
  - _Estado_: 6663 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.104 n=46/60 | contraria IC=+0.000 n=24 | gap=+0.104 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=84, boost estimado=+0.006. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 60 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=179/40 IC=+0.014 PNL=+1.23€ | BTC#60min: n=130/40 IC=-0.030 PNL=-6.14€ | SOL#60min: n=95/40 IC=-0.015 PNL=-1.24€

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=-0.011 n=730 | contrario_BTC IC=-0.017 n=553/40 | gap=-0.006 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.184 > 0.08 con n=74 PNL=+44.34€
  - _Datos_: n=74 IC=+0.184 PNL=+44.34€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.139 > 0.08 con n=95 PNL=+26.15€
  - _Datos_: n=95 IC=+0.139 PNL=+26.15€

**⏳ H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: 25
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: 13/25 ops en el filtro definido (IC actual=+0.238 PNL=+15.01€)
  - _Datos_: n=13 IC=+0.238 PNL=+15.01€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.333 > 0.1 con n=962 PNL=+478.54€
  - _Datos_: n=962 IC=+0.333 PNL=+478.54€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=62 IC=+0.031 PNL=+10.83€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=62 IC=+0.031 PNL=+10.83€

**⏳ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: 30
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: 15/30 ops en el filtro definido (IC actual=+0.110 PNL=+5.52€)
  - _Datos_: n=15 IC=+0.110 PNL=+5.52€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=6478 IC=+0.001 PNL=+94.95€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=6478 IC=+0.001 PNL=+94.95€

**⏳ H-CUSTOM-OF-02H-BTCSOL** — ORDER_FLOW H=02h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 02h está en el blacklist basado en TODOS los pares. Con BTC+SOL solo, el historial muestra 4/5 (80%) IC=+0.054. ¿Se confirma la señal positiva con más datos?
  - _Umbral_: 15
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 02h del blacklist ORDER_FLOW
  - _Estado_: 1/15 ops en el filtro definido (IC actual=+0.008 PNL=+1.22€)
  - _Datos_: n=1 IC=+0.008 PNL=+1.22€

**⏳ H-CUSTOM-OF-07H-BTCSOL** — ORDER_FLOW H=07h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 07h está en el blacklist. Con BTC+SOL solo, el historial muestra 7/12 (58%) IC=+0.043. El blacklist puede estar basado en pares negativos que ya están excluidos.
  - _Umbral_: 20
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 07h del blacklist ORDER_FLOW
  - _Estado_: 0/20 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: 07h sigue en ORDER_FLOW_BLACKLIST_HOURS -- mientras siga ahí, nunca genera fila para volver a evaluarse (26-Ago, triage candidatas estancadas)

**〰️ H-CUSTOM-GBM-60MIN-BUYYES** — GBM 60min BUY_YES — ¿edge superior al BUY_NO?
  - _Hipótesis_: Análisis actual muestra BUY_YES 60min: 22/36 (61%) IC=+0.105 vs BUY_NO 60min: 8/14 (57%) IC=+0.044. En 60min parece que BUY_YES es la dirección dominante, al contrario que en 15min.
  - _Umbral_: n≥30 y IC>+0.08
  - _Acción_: Si BUY_YES 60min confirma IC≥0.10 n≥40 → prioridad live por encima de BUY_NO
  - _Estado_: n=331 IC=+0.007 PNL=+0.03€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=331 IC=+0.007 PNL=+0.03€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=73 IC=-0.073 PNL=-6.17€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=73 IC=-0.073 PNL=-6.17€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=116 IC=-0.076 PNL=-9.41€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=116 IC=-0.076 PNL=-9.41€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.117 > 0.1 con n=520 PNL=+123.67€
  - _Datos_: n=520 IC=+0.117 PNL=+123.67€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=174 IC=+0.074 PNL=+39.40€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=174 IC=+0.074 PNL=+39.40€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=244 IC=+0.073 PNL=+39.80€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=244 IC=+0.073 PNL=+39.80€

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
  - _Estado_: n=1405 IC=+0.027 PNL=+85.41€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1405 IC=+0.027 PNL=+85.41€

**⏳ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: 26/30 ops en el filtro definido (IC actual=-0.214 PNL=-5.03€)
  - _Datos_: n=26 IC=-0.214 PNL=-5.03€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=79 IC=-0.018 PNL=+8.79€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=79 IC=-0.018 PNL=+8.79€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=93 IC=+0.037 PNL=+8.60€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=93 IC=+0.037 PNL=+8.60€

**⏳ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: 15
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: 6/15 ops en el filtro definido (IC actual=+0.037 PNL=+1.09€)
  - _Datos_: n=6 IC=+0.037 PNL=+1.09€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=2249 IC=-0.021 PNL=-55.72€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2249 IC=-0.021 PNL=-55.72€

**🟡 H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.214 > 0.08 con n=33 PNL=+9.78€
  - _Datos_: n=33 IC=+0.214 PNL=+9.78€

**⏳ H-LATE-WINDOW-5MIN** — Late-window BTC 5min — arbitraje timing vs Polymarket
  - _Hipótesis_: Inspirado en VyvanseWithMarijuana (36.5% ROI, $42k vol). A T+160-270s dentro de una ventana BTC 5min, si BTC ya se movió >0.3%, Polymarket no ha actualizado precio → edge estructural. Estrategia LATE_WINDOW_5MIN en shadow hasta n≥30. FIX 2026-07-02: la estrategia llevaba 0 predicciones desde su creacion porque HORIZONTE_MIN_HORAS=0.05 (3min) descartaba todo mercado a <3min de expirar — y su zona de entrada (160-270s de una ventana de 5min) deja 30-140s restantes, siempre bajo el suelo. Corregido en shadow_predict (zona late-window marcada _solo_late, 30s-3min, solo evaluada por esta estrategia). El reloj de acumulacion empieza de verdad hoy. Contexto extra: el estudio de ballenas de hoy confirma que comprar el lado ganador a mitad/final de ventana es el playbook comun de los 3 mayores ganadores verificados de estos mercados (Bonereaper +$19.9k/mes, wowitsamazing +$10k/mes, zhangfan151 +$8.7k/mes).
  - _Umbral_: 30
  - _Acción_: Si IC≥0.08 con n≥30 → proponer pasar a live con stake mínimo (0.50€). Si IC<0 con n≥30 → el lag de Polymarket en BTC es insuficiente.
  - _Estado_: 25/30 ops en el filtro definido (IC actual=+0.278 PNL=+10.54€)
  - _Datos_: n=25 IC=+0.278 PNL=+10.54€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=1781 IC=+0.022 PNL=+100.67€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1781 IC=+0.022 PNL=+100.67€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=464 IC=+0.039 PNL=+3.46€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=464 IC=+0.039 PNL=+3.46€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.092 > 0.08 con n=128 PNL=+24.67€
  - _Datos_: n=128 IC=+0.092 PNL=+24.67€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.136 > 0.08 con n=127 PNL=+3.86€
  - _Datos_: n=127 IC=+0.136 PNL=+3.86€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.123 > 0.08 con n=120 PNL=+38.35€
  - _Datos_: n=120 IC=+0.123 PNL=+38.35€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=18363 IC=+0.100 PNL=+5419.27€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=18363 IC=+0.100 PNL=+5419.27€

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
  - _Estado_: n=880 IC=+0.029 PNL=+51.37€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=880 IC=+0.029 PNL=+51.37€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.113 > 0.02 con n=272 PNL=+72.29€
  - _Datos_: n=272 IC=+0.113 PNL=+72.29€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=94 IC=-0.094 PNL=+19.83€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=94 IC=-0.094 PNL=+19.83€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.443 > 0.1 con n=612 PNL=+523.69€
  - _Datos_: n=612 IC=+0.443 PNL=+523.69€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=1605 IC=+0.020 PNL=+78.16€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=1605 IC=+0.020 PNL=+78.16€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.166 > 0.1 con n=792 PNL=+293.30€
  - _Datos_: n=792 IC=+0.166 PNL=+293.30€

**⏳ H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: 40
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: 31/40 ops en el filtro definido (IC actual=-0.227 PNL=-4.41€)
  - _Datos_: n=31 IC=-0.227 PNL=-4.41€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=450 IC=+0.046 PNL=+62.10€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=450 IC=+0.046 PNL=+62.10€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=30 IC=-0.188 PNL=+2.99€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=30 IC=-0.188 PNL=+2.99€

**〰️ H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: n=70 IC=+0.056 PNL=+1.65€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=70 IC=+0.056 PNL=+1.65€

**⏳ H-CUSTOM-ETH15-BUYNO-PRECIO-ALTO** — ETH#15min BUY_NO con precio_yes>0.55 pierde (NO longshot contra favorito)
  - _Hipótesis_: Detectado 2026-07-02: ult.60 shadow ETH15 BUY_NO — py_mkt~0.5 wr=0.67 PNL=+29.3 (n=49); py_mkt 0.6-0.8 wr 0.33-0 PNL=-5.75 (n=9). Filtro RETURN NONE (no SKIP) aplicado en shadow_predict.py (PY_MKT_MAX_BUY_NO_ETH15=0.55) el mismo dia -- bloquea la GENERACIÓN de la fila, no solo la decisión. Esta hipotesis trackea la zona filtrada: si las ops que HABRIAN caido aqui siguen apareciendo en otras estrategias o el IC forward de la zona se vuelve positivo, revisar el filtro. CAVEAT: n=9, muestra chica — el filtro se aplico por asimetria de riesgo (afecta a dinero live), no por significancia. ⚠️ 05-Ago (fix): la clave del filtro decía 'py_mkt', que NUNCA existió ni en features de UPDOWN_GBM (T_h/delta_ratio_macro/drift_15min/drift_60min/pct_spot_vs_ref/sigma_h) ni como columna top-level de results.csv -- corregida a 'precio_yes_mercado' (columna real). Aun así, con la clave correcta esta hipótesis NUNCA podrá acumular n mientras el filtro RETURN NONE siga activo -- es el mismo patrón 'frozen by design' que H-CUSTOM-LATE15-PHOTO-FINISH (más abajo): la propia protección impide generar los datos necesarios para volver a evaluarla. Para monitorearla de verdad haría falta un logger separado que capture la señal SIN aplicar el filtro (mismo patrón que gate_bucket_propio con data/markets histórico) -- no construido, pendiente decisión.
  - _Umbral_: 20
  - _Acción_: Si IC forward de la zona >0 con n>=20 → retirar filtro; si confirma negativo → considerar extender a BTC/SOL 15min
  - _Estado_: 0/20 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: PY_MKT_MAX_BUY_NO_ETH15=0.55 en shadow_predict.py hace RETURN NONE (bloquea generación, no solo decisión) -- nunca podrá acumular n mientras siga activo. Haría falta un logger separado sin el filtro para monitorear de verdad (no construido, 26-Ago)

**〰️ H-PRECIO-YES-BARATO** — BUY_YES con precio de mercado 0.30-0.40 — mercado infravalora YES
  - _Hipótesis_: Detectado 2026-07-03 en benchmark de calibración del mercado (7d, estrategias GBM): en el bucket precio_yes_mercado [0.3-0.4) la frecuencia real de YES fue 0.45 vs 0.35 implícito (+0.10, n=38). Posible sesgo favorito-longshot suave en binarios de 15min (complemento del LONGSHOT ya activo para BUY_NO con py<0.20). Si se confirma, BUY_YES comprado en esa banda lleva viento de cola estructural del propio mercado, independiente del modelo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → kelly_boost ×1.1 para BUY_YES con precio_yes_mercado en [0.30,0.40), simétrico al longshot BUY_NO existente
  - _Estado_: n=5087 IC=-0.146 PNL=+174.14€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=5087 IC=-0.146 PNL=+174.14€

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
  - _Estado_: n=653 IC=+0.144 PNL=+291.69€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=653 IC=+0.144 PNL=+291.69€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.117 > 0.08 con n=520 PNL=+123.67€
  - _Datos_: n=520 IC=+0.117 PNL=+123.67€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=670 IC=+0.000 PNL=+1.86€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=670 IC=+0.000 PNL=+1.86€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.087 > 0.08 con n=662 PNL=+350.88€
  - _Datos_: n=662 IC=+0.087 PNL=+350.88€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.156 > 0.08 con n=152 PNL=+46.12€
  - _Datos_: n=152 IC=+0.156 PNL=+46.12€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.241 < -0.1 con n=569 PNL=-80.28€
  - _Datos_: n=569 IC=-0.241 PNL=-80.28€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=1353 IC=+0.132 PNL=+689.76€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=1353 IC=+0.132 PNL=+689.76€

**⏳ H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: 40
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: 31/40 ops en el filtro definido (IC actual=+0.045 PNL=+1.77€)
  - _Datos_: n=31 IC=+0.045 PNL=+1.77€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=718 IC=-0.026 PNL=+45.32€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=718 IC=-0.026 PNL=+45.32€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.181 > 0.08 con n=622 PNL=+373.88€
  - _Datos_: n=622 IC=+0.181 PNL=+373.88€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=1048 IC=-0.060 PNL=+149.01€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1048 IC=-0.060 PNL=+149.01€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.117 > 0.08 con n=267 PNL=-33.76€
  - _Datos_: n=267 IC=+0.117 PNL=-33.76€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.236 > 0.08 con n=1541 PNL=-149.57€
  - _Datos_: n=1541 IC=+0.236 PNL=-149.57€

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 11/40 ops en el filtro definido (IC actual=-0.021 PNL=+0.98€)
  - _Datos_: n=11 IC=-0.021 PNL=+0.98€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.118 n=176) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=176 IC=+0.118 PNL=+50.29€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.355 > 0.08 con n=74 PNL=+50.85€
  - _Datos_: n=74 IC=+0.355 PNL=+50.85€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.429 n=237) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=237 IC=+0.429 PNL=+320.82€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=3316 IC=+0.131 PNL=-590.54€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=3316 IC=+0.131 PNL=-590.54€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.182 > 0.1 con n=42 PNL=+22.66€
  - _Datos_: n=42 IC=+0.182 PNL=+22.66€
