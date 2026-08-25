# Hipótesis automáticas — 2026-08-25 18:21 UTC
_Generado por shadow_postmortem.py sobre 153553 resoluciones (PNL=+10208.51€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.705` → IC=-0.167 (n=88)

  - _Acción_: SKIP cuando `py_entrada` < 0.705
  - _Potencial_: sin este filtro IC_bueno=+0.273 (n=218)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.377 (n=63)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=215)

- **PATRÓN** `py_entrada` > `0.725` → IC=+0.289 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.146)

- **PATRÓN** `n_ballena_banda` > `20.0` → IC=+0.164 (n=215)

  - _Acción_: Kelly boost +0.82€ cuando `n_ballena_banda` > 20.0 (IC base=+0.146)

- **PATRÓN** `n_total_lado` > `58.0` → IC=+0.237 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 58.0 (IC base=+0.146)

- **PATRÓN** `banda_hit_calibrado` > `0.8208` → IC=+0.278 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8208 (IC base=+0.146)

- **PATRÓN** `banda_z` > `10.286` → IC=+0.247 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 10.286 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.175 (n=155)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 11.0 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.168 (n=239)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `3507.1457` → IC=+0.234 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3507.1457 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `288.0` → IC=+0.313 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 288.0 (IC base=+0.146)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.136 (n=215)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.5 (IC base=+0.018)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.725` → IC=+0.294 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.186)

- **PATRÓN** `n_ballena_banda` > `21.0` → IC=+0.203 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `n_ballena_banda` > 21.0 (IC base=+0.186)

- **PATRÓN** `n_total_lado` > `58.0` → IC=+0.265 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 58.0 (IC base=+0.186)

- **PATRÓN** `banda_hit_calibrado` > `0.8205` → IC=+0.294 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8205 (IC base=+0.186)

- **PATRÓN** `banda_z` > `11.481` → IC=+0.280 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.481 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.221 (n=102)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.186)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.190 (n=169)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.01 (IC base=+0.186)

- **PATRÓN** `libro_liquidez` > `3120.8362` → IC=+0.235 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3120.8362 (IC base=+0.186)

- **PATRÓN** `ballena_activa_n` < `296.0` → IC=+0.324 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 296.0 (IC base=+0.186)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.126 (n=113)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.495 (IC base=+0.013)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.335` → IC=-0.267 (n=28)

  - _Acción_: SKIP cuando `py_entrada` < 0.335
  - _Potencial_: sin este filtro IC_bueno=+0.193 (n=86)

- **FILTRO** `banda_hit_calibrado` < `0.6284` → IC=-0.218 (n=37)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6284
  - _Potencial_: sin este filtro IC_bueno=+0.222 (n=77)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.141 (n=90)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.353 (n=32)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.134 (n=69)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=86)

- **PATRÓN** `py_entrada` > `0.725` → IC=+0.271 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.078)

- **PATRÓN** `banda_hit_calibrado` > `0.8139` → IC=+0.246 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8139 (IC base=+0.078)

- **PATRÓN** `banda_z` > `8.174` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `banda_z` > 8.174 (IC base=+0.078)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.141 (n=90)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.02 (IC base=+0.078)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.495 (IC base=-0.024)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `148.73` → IC=-0.278 (n=2154)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 148.73
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=6465)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `n_ballenas` < `6.0` → IC=-0.167 (n=163)

  - _Acción_: SKIP cuando `n_ballenas` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=494)

- **FILTRO** `restante_s_al_confirmar` < `382.08` → IC=-0.283 (n=164)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 382.08
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=493)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `85.16` → IC=-0.450 (n=258)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 85.16
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=776)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `158.28` → IC=-0.196 (n=583)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 158.28
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=1749)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `149.25` → IC=-0.280 (n=525)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 149.25
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1578)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `156.39` → IC=-0.338 (n=491)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 156.39
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=997)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.7` → IC=+0.190 (n=4952)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.7 (IC base=+0.099)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.174 (n=1501)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `2383.976` → IC=+0.177 (n=1449)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2383.976 (IC base=+0.099)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.147 (n=3173)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.154 (n=3874)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.138)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.257 (n=3016)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.187 (n=2774)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.02 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `1813.4701` → IC=+0.177 (n=2315)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 1813.4701 (IC base=+0.138)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.226 (n=589)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.211)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.400 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.215 (n=728)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `12123.9122` → IC=+0.220 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12123.9122 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.193 (n=525)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 7.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.190 (n=404)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 11.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.285 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.182)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.183 (n=752)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.01 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `11757.2155` → IC=+0.189 (n=194)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 11757.2155 (IC base=+0.182)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=513)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.139 (n=444)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 15.0 (IC base=+0.122)

- **PATRÓN** `py_entrada` > `0.555` → IC=+0.143 (n=516)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` > 0.555 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `4978.014` → IC=+0.163 (n=200)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 4978.014 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.210 (n=198)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.138)

- **PATRÓN** `py_entrada` < `0.415` → IC=+0.181 (n=296)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.415 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `4247.4138` → IC=+0.157 (n=278)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 4247.4138 (IC base=+0.138)

### FAVORITO_CONFIRMADO#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.136 (n=1129)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.131 (n=967)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 15.0 (IC base=+0.127)

- **PATRÓN** `py_entrada` > `0.69` → IC=+0.305 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.289 (n=434)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.284)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.292 (n=435)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.284)

- **PATRÓN** `py_entrada` < `0.375` → IC=+0.329 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.375 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.284 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `2826.4245` → IC=+0.298 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2826.4245 (IC base=+0.284)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.148 (n=319)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.168 (n=272)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 15.0 (IC base=+0.146)

- **PATRÓN** `py_entrada` > `0.66` → IC=+0.262 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.66 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.147 (n=381)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.02 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `2043.1794` → IC=+0.166 (n=306)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2043.1794 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `4420.281` → IC=+0.157 (n=141)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 4420.281 (IC base=+0.079)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.199 (n=895)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.197 (n=760)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.84` → IC=+0.445 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.84 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.251 (n=195)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `py_entrada` < `0.205` → IC=+0.349 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.205 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.228 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `841.0684` → IC=+0.233 (n=563)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 841.0684 (IC base=+0.217)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `19.0` → IC=+0.265 (n=79)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 19.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.192 (n=105)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 8.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.342 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.239 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.189)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.206 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.101)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.146 (n=272)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.02 (IC base=+0.101)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.292 (n=70)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=87)

- **FILTRO** `py_entrada` > `0.845` → IC=-0.379 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.845
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=126)

- **FILTRO** `libro_liquidez` < `7404.7045` → IC=-0.248 (n=117)

  - _Acción_: SKIP cuando `libro_liquidez` < 7404.7045
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=40)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.195 (n=4196)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.196 (n=3612)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.203 (n=2039)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `3258.7888` → IC=+0.354 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3258.7888 (IC base=+0.190)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.174 (n=721)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 11.0 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.181 (n=1042)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 17.0 (IC base=+0.171)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.190 (n=1019)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.73 (IC base=+0.171)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.219 (n=55)

- **FILTRO** `py_entrada` > `0.795` → IC=-0.393 (n=26)

  - _Acción_: SKIP cuando `py_entrada` > 0.795
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=52)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.417 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.326)

- **PATRÓN** `py_entrada` > `0.835` → IC=+0.370 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.835 (IC base=+0.326)

- **PATRÓN** `libro_liquidez` > `2916.5858` → IC=+0.343 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2916.5858 (IC base=+0.326)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=1071)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.169 (n=916)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 15.0 (IC base=+0.162)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.174 (n=391)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.7 (IC base=+0.162)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.169 (n=545)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.73 (IC base=+0.162)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.242 (n=956)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.232)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.233 (n=821)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.232)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.315 (n=343)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.197 (n=1024)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.194 (n=886)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.198 (n=504)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.7 (IC base=+0.190)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.454 (n=194)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.442)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.447 (n=185)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.453 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.442)

- **PATRÓN** `libro_liquidez` > `3341.8059` → IC=+0.464 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3341.8059 (IC base=+0.442)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.451 (n=79)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.443)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.445 (n=71)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.443)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.456 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.443)

- **PATRÓN** `libro_liquidez` > `12146.257` → IC=+0.474 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12146.257 (IC base=+0.443)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `4.0` → IC=+0.441 (n=83)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.425)

- **PATRÓN** `py_entrada` < `0.91` → IC=+0.431 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.91 (IC base=+0.425)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.425 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.424 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.425)

- **PATRÓN** `libro_liquidez` > `3697.0572` → IC=+0.474 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3697.0572 (IC base=+0.425)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.457 (n=44)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.92` → IC=+0.438 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.92 (IC base=+0.440)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.433 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.440)

- **PATRÓN** `libro_liquidez` > `1582.3645` → IC=+0.447 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1582.3645 (IC base=+0.440)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.197 (n=10943)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 6.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.193 (n=7871)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 12.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.222 (n=7686)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.193)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.129 (n=2109)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.133 (n=1340)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 11.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.160 (n=1452)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` > 0.71 (IC base=+0.125)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.248 (n=1694)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.238)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.270 (n=1278)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.238)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.174 (n=701)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.166 (n=1353)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 12.0 (IC base=+0.163)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.215 (n=657)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.163)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.244 (n=1546)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.234)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.286 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.234)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.231 (n=649)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.249 (n=1048)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.220)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=675)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.194 (n=1223)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 11.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.235 (n=665)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.189)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=1510)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.131)

- **PATRÓN** `restante_min` < `3.92` → IC=+0.138 (n=1309)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` < 3.92 (IC base=+0.131)

- **PATRÓN** `restante_min` > `4.92` → IC=+0.158 (n=1409)

  - _Acción_: Kelly boost +0.79€ cuando `restante_min` > 4.92 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.150 (n=1755)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 7.0 (IC base=+0.131)

- **PATRÓN** `lag_apertura_s` < `4.53` → IC=+0.158 (n=1309)

  - _Acción_: Kelly boost +0.79€ cuando `lag_apertura_s` < 4.53 (IC base=+0.131)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.204 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.139)

- **PATRÓN** `restante_min` < `3.88` → IC=+0.146 (n=650)

  - _Acción_: Kelly boost +0.73€ cuando `restante_min` < 3.88 (IC base=+0.139)

- **PATRÓN** `restante_min` > `4.9` → IC=+0.172 (n=682)

  - _Acción_: Kelly boost +0.86€ cuando `restante_min` > 4.9 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.162 (n=866)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 7.0 (IC base=+0.139)

- **PATRÓN** `lag_apertura_s` < `5.75` → IC=+0.176 (n=652)

  - _Acción_: Kelly boost +0.88€ cuando `lag_apertura_s` < 5.75 (IC base=+0.139)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.189 (n=759)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.122)

- **PATRÓN** `restante_min` < `3.95` → IC=+0.136 (n=663)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` < 3.95 (IC base=+0.122)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.153 (n=710)

  - _Acción_: Kelly boost +0.77€ cuando `restante_min` > 4.94 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.123 (n=2072)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 5.0 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.138 (n=889)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.122)

- **PATRÓN** `lag_apertura_s` < `3.48` → IC=+0.156 (n=660)

  - _Acción_: Kelly boost +0.78€ cuando `lag_apertura_s` < 3.48 (IC base=+0.122)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.316 (n=394)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.300)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.303 (n=501)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.300)

- **PATRÓN** `py_entrada` > `0.825` → IC=+0.379 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.825 (IC base=+0.300)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.287 (n=237)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.279)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.282 (n=218)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.279)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.345 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.279)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.279 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `5623.4735` → IC=+0.315 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5623.4735 (IC base=+0.279)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.337 (n=182)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.303)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.310 (n=267)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.303)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.391 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.303)

- **PATRÓN** `libro_liquidez` > `1876.0591` → IC=+0.324 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1876.0591 (IC base=+0.303)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.391 (n=53)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.359)

- **PATRÓN** `py_entrada` > `0.88` → IC=+0.429 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.88 (IC base=+0.359)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.357 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.359)

- **PATRÓN** `libro_liquidez` > `786.7393` → IC=+0.381 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 786.7393 (IC base=+0.359)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.419 (n=244)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.409)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.420 (n=236)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.409)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.418 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.409)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.423 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.409)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.408 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.409)

- **PATRÓN** `libro_liquidez` > `1864.6918` → IC=+0.422 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1864.6918 (IC base=+0.409)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.415 (n=104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.406)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.425 (n=105)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.406)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.411 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.406)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.417 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.406)

- **PATRÓN** `libro_liquidez` > `5705.9228` → IC=+0.444 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5705.9228 (IC base=+0.406)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.420 (n=98)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.415)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.436 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.415)

- **PATRÓN** `py_entrada` > `0.91` → IC=+0.420 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.91 (IC base=+0.415)

- **PATRÓN** `libro_liquidez` > `1921.0334` → IC=+0.438 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1921.0334 (IC base=+0.415)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.298 (n=271)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.283)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.435 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.283)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.307 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `821.9118` → IC=+0.297 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 821.9118 (IC base=+0.283)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.298 (n=271)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.283)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.435 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.283)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.307 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `821.9118` → IC=+0.297 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 821.9118 (IC base=+0.283)

### GBM_LATE_15M
- **PATRÓN** `ibs_20min` > `0.9463` → IC=+0.216 (n=667)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9463 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` > `0.2069` → IC=+0.237 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2069 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` < `1.0161` → IC=+0.225 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 1.0161 (IC base=+0.069)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.1` → IC=+0.181 (n=826)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 5.1 (IC base=+0.069)

- **PATRÓN** `volumen_regimen` < `0.63` → IC=+0.234 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.63 (IC base=+0.069)

- **PATRÓN** `volumen_regimen` > `1.067` → IC=+0.258 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.067 (IC base=+0.069)

- **PATRÓN** `volumen_pendiente_norm` < `0.1063` → IC=+0.135 (n=1004)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` < 0.1063 (IC base=+0.069)

- **PATRÓN** `volumen_pendiente_norm` > `0.3023` → IC=+0.142 (n=146)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.3023 (IC base=+0.069)

- **PATRÓN** `volumen_spike_ratio` < `2.4423` → IC=+0.141 (n=925)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.4423 (IC base=+0.069)

- **PATRÓN** `volumen_spike_ratio` > `1.9475` → IC=+0.134 (n=700)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.9475 (IC base=+0.069)

- **PATRÓN** `ibs_20min` < `0.2129` → IC=+0.125 (n=1381)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.2129 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` < `0.1326` → IC=+0.151 (n=648)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1326 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` < `0.6279` → IC=+0.151 (n=227)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6279 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` > `1.0483` → IC=+0.143 (n=309)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.0483 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.1742` → IC=+0.252 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1742 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` < `1.6176` → IC=+0.217 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6176 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` > `2.9495` → IC=+0.221 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9495 (IC base=+0.028)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.268 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.028)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.197 (n=150)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0075 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.181 (n=161)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 6.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.296 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.496` → IC=+0.336 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.496 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.153 (n=223)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.04 (IC base=+0.119)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.315 (n=144)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.287)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.336 (n=71)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.2028` → IC=+0.326 (n=188)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2028 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.291 (n=199)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.287)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.301 (n=149)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.287)

- **PATRÓN** `ibs_20min` < `0.4739` → IC=+0.337 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4739 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` < `0.0596` → IC=+0.326 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0596 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.318 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.287)

- **PATRÓN** `volumen_spike_ratio` < `1.7889` → IC=+0.342 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7889 (IC base=+0.287)

- **PATRÓN** `volumen_spike_ratio` > `1.4617` → IC=+0.296 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4617 (IC base=+0.287)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.341 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `1989.8695` → IC=+0.322 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1989.8695 (IC base=+0.287)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.379 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.287)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.261 (n=111)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.221)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.227 (n=108)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.4409` → IC=+0.222 (n=325)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4409 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.250 (n=326)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.223 (n=298)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` > `0.9595` → IC=+0.245 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9595 (IC base=+0.221)

- **PATRÓN** `dist_vwap_pct` > `0.308` → IC=+0.238 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.308 (IC base=+0.221)

- **PATRÓN** `dist_vwap_pct` < `1.0239` → IC=+0.225 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 1.0239 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.421` → IC=+0.267 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.421 (IC base=+0.221)

- **PATRÓN** `volumen_regimen` < `1.2894` → IC=+0.222 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2894 (IC base=+0.221)

- **PATRÓN** `volumen_regimen` > `1.1032` → IC=+0.252 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1032 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` < `0.0771` → IC=+0.230 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0771 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.2714` → IC=+0.273 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2714 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` < `1.4472` → IC=+0.263 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4472 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `11116.6074` → IC=+0.236 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11116.6074 (IC base=+0.221)

- **PATRÓN** `ballena_activa_n` < `369.0` → IC=+0.224 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 369.0 (IC base=+0.221)

- **PATRÓN** `sigma_h` < `0.0021` → IC=+0.186 (n=135)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0021 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.1677` → IC=+0.153 (n=266)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1677 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.145 (n=361)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 8.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.149 (n=417)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 18.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.4179` → IC=+0.171 (n=350)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.4179 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.1939` → IC=+0.170 (n=343)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1939 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.981` → IC=+0.235 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.981 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.6279` → IC=+0.174 (n=133)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6279 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `1.0216` → IC=+0.145 (n=181)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.0216 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.094` → IC=+0.218 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.094 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.7548` → IC=+0.183 (n=197)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.7548 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.4133` → IC=+0.159 (n=294)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.4133 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=514)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `12702.6869` → IC=+0.172 (n=181)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 12702.6869 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `233.0` → IC=+0.176 (n=69)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 233.0 (IC base=+0.139)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.186 (n=135)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0076 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.066` → IC=+0.130 (n=133)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.066 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.209 (n=146)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.272 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.923` → IC=+0.275 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.923 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.163 (n=185)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `1917.67` → IC=+0.143 (n=180)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 1917.67 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.128 (n=84)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 31.0 (IC base=+0.129)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.317 (n=91)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.274)

- **PATRÓN** `drift_60min` |x|≤ `0.0886` → IC=+0.296 (n=91)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0886 (IC base=+0.274)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.280 (n=184)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.274)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.300 (n=133)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.274)

- **PATRÓN** `ibs_20min` < `0.5146` → IC=+0.309 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5146 (IC base=+0.274)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.013` → IC=+0.292 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.013 (IC base=+0.274)

- **PATRÓN** `volumen_pendiente_norm` > `0.4202` → IC=+0.413 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.4202 (IC base=+0.274)

- **PATRÓN** `volumen_spike_ratio` < `4.4965` → IC=+0.255 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 4.4965 (IC base=+0.274)

- **PATRÓN** `volumen_spike_ratio` > `2.9394` → IC=+0.262 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9394 (IC base=+0.274)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.297 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.274)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.242 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 30.0 (IC base=+0.274)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `ibs_20min` > `0.8764` → IC=-0.174 (n=179)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8764
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=538)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.151 (n=61)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=656)

- **PATRÓN** `dist_vwap_pct` > `0.1188` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1188 (IC base=-0.028)

- **PATRÓN** `dist_vwap_pct` < `0.0784` → IC=+0.352 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0784 (IC base=-0.028)

- **PATRÓN** `volumen_regimen` > `0.8004` → IC=+0.333 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8004 (IC base=-0.028)

- **PATRÓN** `dist_vwap_pct` > `0.1302` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1302 (IC base=-0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.0567` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0567 (IC base=-0.059)

- **PATRÓN** `volumen_spike_ratio` < `1.7203` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.7203 (IC base=-0.059)

- **PATRÓN** `volumen_spike_ratio` > `2.1285` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1285 (IC base=-0.059)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `ibs_20min` > `0.48` → IC=-0.121 (n=603)

  - _Acción_: SKIP cuando `ibs_20min` > 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=606)

- **FILTRO** `sigma_ewma_delta_pct` > `4.888` → IC=-0.147 (n=259)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.888
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=950)

- **FILTRO** `volumen_pendiente_norm` < `0.0964` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.0964
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

- **FILTRO** `volumen_spike_ratio` > `1.6234` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.6234
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.184 (n=36)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0057 (IC base=+0.065)

- **PATRÓN** `drift_60min` |x|≤ `0.46` → IC=+0.122 (n=80)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.61€ cuando `drift_60min` |x|≤ 0.46 (IC base=+0.065)

- **PATRÓN** `hora_utc` > `23.0` → IC=+0.250 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 23.0 (IC base=+0.065)

- **PATRÓN** `ibs_20min` > `0.5455` → IC=+0.154 (n=53)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` > 0.5455 (IC base=+0.065)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.4466` → IC=-0.154 (n=304)

  - _Acción_: SKIP cuando `ibs_20min` < 0.4466
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=304)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=94)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=514)

- **FILTRO** `ibs_20min` > `0.775` → IC=-0.172 (n=269)

  - _Acción_: SKIP cuando `ibs_20min` > 0.775
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=813)

- **FILTRO** `sigma_ewma_delta_pct` > `6.547` → IC=-0.185 (n=179)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.547
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=903)

- **PATRÓN** `dist_vwap_pct` < `0.2396` → IC=+0.175 (n=38)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.2396 (IC base=-0.079)

- **PATRÓN** `volumen_regimen` > `0.6932` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 0.6932 (IC base=-0.079)

- **PATRÓN** `dist_vwap_pct` < `0.2029` → IC=+0.229 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2029 (IC base=-0.036)

- **PATRÓN** `volumen_regimen` < `0.6961` → IC=+0.221 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6961 (IC base=-0.036)

- **PATRÓN** `volumen_regimen` > `1.1355` → IC=+0.246 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1355 (IC base=-0.036)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.136 (n=1159)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.0073 (IC base=+0.055)

- **PATRÓN** `ibs_20min` > `0.9461` → IC=+0.246 (n=850)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9461 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` > `0.9303` → IC=+0.279 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9303 (IC base=+0.055)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.09` → IC=+0.123 (n=1012)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 5.09 (IC base=+0.055)

- **PATRÓN** `volumen_regimen` > `1.1593` → IC=+0.191 (n=296)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` > 1.1593 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` < `0.1152` → IC=+0.166 (n=1116)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` < 0.1152 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.2437` → IC=+0.216 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2437 (IC base=+0.055)

- **PATRÓN** `volumen_spike_ratio` < `1.4831` → IC=+0.191 (n=383)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.4831 (IC base=+0.055)

- **PATRÓN** `volumen_spike_ratio` > `2.8724` → IC=+0.175 (n=383)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.8724 (IC base=+0.055)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.271 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 102.0 (IC base=+0.055)

- **PATRÓN** `ibs_20min` < `0.0968` → IC=+0.176 (n=1102)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.0968 (IC base=+0.035)

- **PATRÓN** `dist_vwap_pct` > `0.642` → IC=+0.219 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.642 (IC base=+0.035)

- **PATRÓN** `dist_vwap_pct` < `0.1458` → IC=+0.195 (n=653)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.1458 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` > `0.63` → IC=+0.206 (n=698)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.63 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` > `0.248` → IC=+0.342 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.248 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` > `2.9255` → IC=+0.280 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9255 (IC base=+0.035)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.253 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 58.0 (IC base=+0.035)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `sigma_ewma_delta_pct` > `5.002` → IC=-0.208 (n=111)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.002
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=554)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.047` → IC=+0.180 (n=98)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 5.047 (IC base=-0.016)

- **PATRÓN** `volumen_pendiente_norm` > `0.0542` → IC=+0.233 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0542 (IC base=-0.016)

- **PATRÓN** `volumen_spike_ratio` > `2.242` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.242 (IC base=-0.016)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `volumen_regimen` > `0.9983` → IC=+0.129 (n=33)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.9983 (IC base=-0.041)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.279 (n=129)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0076 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.0628` → IC=+0.218 (n=129)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0628 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.263 (n=137)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.295 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.932` → IC=+0.298 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.932 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` < `0.1444` → IC=+0.188 (n=283)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` < 0.1444 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.425` → IC=+0.233 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.425 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` < `2.0838` → IC=+0.176 (n=134)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 2.0838 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `3.8943` → IC=+0.216 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.8943 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.222 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `1915.1084` → IC=+0.206 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1915.1084 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.405 (n=82)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.368)

- **PATRÓN** `drift_60min` |x|≤ `0.1856` → IC=+0.378 (n=121)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1856 (IC base=+0.368)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.390 (n=170)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.368)

- **PATRÓN** `ibs_20min` < `0.2398` → IC=+0.383 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2398 (IC base=+0.368)

- **PATRÓN** `volumen_pendiente_norm` < `0.1045` → IC=+0.384 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1045 (IC base=+0.368)

- **PATRÓN** `volumen_pendiente_norm` > `0.1384` → IC=+0.396 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1384 (IC base=+0.368)

- **PATRÓN** `volumen_spike_ratio` < `2.9702` → IC=+0.419 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.9702 (IC base=+0.368)

- **PATRÓN** `libro_liquidez` > `1881.0184` → IC=+0.405 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1881.0184 (IC base=+0.368)

- **PATRÓN** `ballena_activa_n` < `32.0` → IC=+0.371 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 32.0 (IC base=+0.368)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.159 (n=136)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=284)

- **FILTRO** `dist_vwap_pct` < `0.6615` → IC=-0.211 (n=43)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.6615
  - _Potencial_: sin este filtro IC_bueno=+0.269 (n=24)

- **FILTRO** `volumen_regimen` > `1.0046` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.0046
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=51)

- **FILTRO** `dist_vwap_pct` < `0.0964` → IC=-0.136 (n=53)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0964
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

- **FILTRO** `volumen_regimen` > `0.8819` → IC=-0.231 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8819
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=49)

- **FILTRO** `volumen_regimen` < `0.6828` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.6828
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=49)

- **FILTRO** `volumen_pendiente_norm` < `0.0424` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.0424
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.156 (n=62)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=862)

- **PATRÓN** `dist_vwap_pct` > `0.6615` → IC=+0.269 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6615 (IC base=-0.069)

- **PATRÓN** `volumen_spike_ratio` < `1.3934` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3934 (IC base=-0.069)

- **PATRÓN** `volumen_spike_ratio` > `2.091` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.091 (IC base=-0.069)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.5294` → IC=-0.147 (n=284)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5294
  - _Potencial_: sin este filtro IC_bueno=+0.138 (n=291)

- **FILTRO** `ibs_20min` > `0.7391` → IC=-0.162 (n=214)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7391
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=646)

- **FILTRO** `dist_vwap_pct` > `0.1358` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1358
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=50)

- **FILTRO** `volumen_regimen` > `1.3709` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.3709
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=50)

- **FILTRO** `volumen_spike_ratio` < `2.3381` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 2.3381
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

- **PATRÓN** `ibs_20min` > `0.8511` → IC=+0.247 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8511 (IC base=-0.003)

- **PATRÓN** `dist_vwap_pct` > `0.3274` → IC=+0.263 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3274 (IC base=-0.003)

- **PATRÓN** `volumen_regimen` < `0.8622` → IC=+0.179 (n=110)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.8622 (IC base=-0.003)

- **PATRÓN** `volumen_regimen` > `1.1426` → IC=+0.184 (n=55)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 1.1426 (IC base=-0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2631` → IC=+0.292 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2631 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` < `1.4966` → IC=+0.179 (n=51)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.4966 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` > `1.5794` → IC=+0.159 (n=136)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.5794 (IC base=-0.003)

- **PATRÓN** `ballena_activa_n` < `78.0` → IC=+0.208 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 78.0 (IC base=-0.003)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=192)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.227 (n=196)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.9048` → IC=+0.287 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9048 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` > `0.8873` → IC=+0.327 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8873 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.128` → IC=+0.270 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.128 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` > `0.8342` → IC=+0.247 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8342 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` < `0.0807` → IC=+0.212 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0807 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.2828` → IC=+0.268 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2828 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.4115` → IC=+0.250 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4115 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.228 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `3101.1726` → IC=+0.249 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3101.1726 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.277 (n=231)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.260)

- **PATRÓN** `sigma_h` > `0.0212` → IC=+0.273 (n=174)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0212 (IC base=+0.260)

- **PATRÓN** `drift_60min` |x|≤ `0.4365` → IC=+0.268 (n=459)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4365 (IC base=+0.260)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.270 (n=484)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.260)

- **PATRÓN** `ibs_20min` < `0.2727` → IC=+0.318 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2727 (IC base=+0.260)

- **PATRÓN** `dist_vwap_pct` < `0.244` → IC=+0.271 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.244 (IC base=+0.260)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.5` → IC=+0.280 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.5 (IC base=+0.260)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.02` → IC=+0.261 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.02 (IC base=+0.260)

- **PATRÓN** `volumen_regimen` > `1.0789` → IC=+0.294 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0789 (IC base=+0.260)

- **PATRÓN** `volumen_pendiente_norm` > `0.2909` → IC=+0.354 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2909 (IC base=+0.260)

- **PATRÓN** `volumen_spike_ratio` > `2.1847` → IC=+0.281 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1847 (IC base=+0.260)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.243 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.260)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.183 (n=1466)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0066 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=753)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.157)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.162 (n=843)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 6.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` > `0.8935` → IC=+0.259 (n=1464)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8935 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.7937` → IC=+0.251 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7937 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.249` → IC=+0.255 (n=941)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.249 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` < `1.2275` → IC=+0.162 (n=1528)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2275 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` > `0.6896` → IC=+0.173 (n=1365)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 0.6896 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.104` → IC=+0.184 (n=780)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.104 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `2.2948` → IC=+0.158 (n=1716)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.2948 (IC base=+0.157)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.168 (n=1791)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `3744.3772` → IC=+0.198 (n=732)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 3744.3772 (IC base=+0.157)

- **PATRÓN** `ballena_activa_n` < `133.0` → IC=+0.180 (n=971)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 133.0 (IC base=+0.157)

- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.199 (n=1914)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0081 (IC base=+0.184)

- **PATRÓN** `drift_60min` |x|≤ `0.3761` → IC=+0.198 (n=1911)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.3761 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.208 (n=875)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.186 (n=916)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 7.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` < `0.4013` → IC=+0.240 (n=1911)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4013 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` < `0.3513` → IC=+0.176 (n=1685)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.3513 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.805` → IC=+0.207 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.805 (IC base=+0.184)

- **PATRÓN** `volumen_regimen` < `1.1729` → IC=+0.164 (n=1585)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1729 (IC base=+0.184)

- **PATRÓN** `volumen_regimen` > `0.8533` → IC=+0.174 (n=1057)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 0.8533 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` > `0.2903` → IC=+0.232 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2903 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` < `1.5782` → IC=+0.184 (n=574)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.5782 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` > `2.6536` → IC=+0.199 (n=436)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.6536 (IC base=+0.184)

- **PATRÓN** `ballena_activa_n` < `218.0` → IC=+0.173 (n=870)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 218.0 (IC base=+0.184)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.227 (n=159)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.222 (n=131)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.322 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.618` → IC=+0.347 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.618 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.1402` → IC=+0.159 (n=80)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.1402 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.4192` → IC=+0.133 (n=273)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 1.4192 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.183 (n=181)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.04 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.298 (n=102)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.287)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.308 (n=50)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.2252` → IC=+0.315 (n=133)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2252 (IC base=+0.287)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.312 (n=110)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.287)

- **PATRÓN** `ibs_20min` < `0.0253` → IC=+0.387 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0253 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.657` → IC=+0.300 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.657 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` < `0.0812` → IC=+0.308 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0812 (IC base=+0.287)

- **PATRÓN** `volumen_spike_ratio` < `1.8142` → IC=+0.385 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8142 (IC base=+0.287)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.338 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `1982.2745` → IC=+0.365 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1982.2745 (IC base=+0.287)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.350 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.287)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.250 (n=102)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.188)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.211 (n=102)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.225 (n=321)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` > `0.5086` → IC=+0.226 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5086 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` > `0.2059` → IC=+0.255 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2059 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.802` → IC=+0.278 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.802 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` < `1.3057` → IC=+0.193 (n=304)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 1.3057 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` > `0.9006` → IC=+0.212 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9006 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.2715` → IC=+0.283 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2715 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` < `1.3995` → IC=+0.237 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3995 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `11847.0948` → IC=+0.227 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11847.0948 (IC base=+0.188)

- **PATRÓN** `ballena_activa_n` < `378.0` → IC=+0.186 (n=151)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 378.0 (IC base=+0.188)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.188 (n=350)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0044 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.286` → IC=+0.182 (n=397)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.286 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.174 (n=366)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 7.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.3843` → IC=+0.192 (n=397)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.3843 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.1617` → IC=+0.184 (n=384)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.1617 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.574` → IC=+0.229 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.574 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `0.637` → IC=+0.218 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.637 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.0712` → IC=+0.211 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0712 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `1.7388` → IC=+0.184 (n=194)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.7388 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `13901.1612` → IC=+0.159 (n=133)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 13901.1612 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `248.0` → IC=+0.176 (n=69)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 248.0 (IC base=+0.153)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.188 (n=107)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0077 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.1433` → IC=+0.161 (n=213)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1433 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.156 (n=123)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 16.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.212 (n=109)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.289 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.877` → IC=+0.307 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.877 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` < `0.2301` → IC=+0.133 (n=257)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` < 0.2301 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.0146` → IC=+0.198 (n=114)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.0146 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `3.8523` → IC=+0.142 (n=118)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 3.8523 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.172 (n=254)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.04 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `1961.8084` → IC=+0.170 (n=107)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 1961.8084 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.325 (n=118)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.297)

- **PATRÓN** `drift_60min` |x|≤ `0.1743` → IC=+0.342 (n=118)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1743 (IC base=+0.297)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.320 (n=120)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.297)

- **PATRÓN** `ibs_20min` < `0.3636` → IC=+0.326 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3636 (IC base=+0.297)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.093` → IC=+0.333 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.093 (IC base=+0.297)

- **PATRÓN** `volumen_pendiente_norm` > `0.4063` → IC=+0.447 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.4063 (IC base=+0.297)

- **PATRÓN** `volumen_spike_ratio` < `4.276` → IC=+0.293 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 4.276 (IC base=+0.297)

- **PATRÓN** `volumen_spike_ratio` > `2.1697` → IC=+0.306 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1697 (IC base=+0.297)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.237 (n=268)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.4992` → IC=+0.204 (n=305)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4992 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.211 (n=310)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` > `0.4502` → IC=+0.249 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4502 (IC base=+0.189)

- **PATRÓN** `dist_vwap_pct` > `1.0398` → IC=+0.247 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0398 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.711` → IC=+0.344 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.711 (IC base=+0.189)

- **PATRÓN** `volumen_regimen` > `0.6366` → IC=+0.207 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6366 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.1012` → IC=+0.257 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1012 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` < `1.4394` → IC=+0.210 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4394 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `2.4658` → IC=+0.230 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4658 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.190 (n=343)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.01 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `9742.9195` → IC=+0.202 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9742.9195 (IC base=+0.189)

- **PATRÓN** `ballena_activa_n` < `113.0` → IC=+0.211 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 113.0 (IC base=+0.189)

- **PATRÓN** `sigma_h` < `0.0024` → IC=+0.250 (n=130)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0024 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.3699` → IC=+0.172 (n=382)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.3699 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.171 (n=174)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 15.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.150 (n=181)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 7.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.332` → IC=+0.213 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.332 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` < `0.5306` → IC=+0.161 (n=444)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.5306 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.457` → IC=+0.223 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.457 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `0.8485` → IC=+0.154 (n=255)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8485 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` > `0.6129` → IC=+0.158 (n=381)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.6129 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.1018` → IC=+0.154 (n=108)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.1018 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.8878` → IC=+0.199 (n=184)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.8878 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `196.0` → IC=+0.124 (n=171)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 196.0 (IC base=+0.145)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **FILTRO** `ibs_20min` > `0.4286` → IC=-0.224 (n=121)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4286
  - _Potencial_: sin este filtro IC_bueno=+0.224 (n=367)

- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.198 (n=147)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0118 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.134 (n=457)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.8519` → IC=+0.229 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8519 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `0.7903` → IC=+0.270 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7903 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.202` → IC=+0.286 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.202 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` > `0.6182` → IC=+0.131 (n=440)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 0.6182 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.0998` → IC=+0.141 (n=154)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.0998 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2853.2159` → IC=+0.188 (n=200)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 2853.2159 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.189 (n=162)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 44.0 (IC base=+0.117)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.196 (n=123)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0048 (IC base=+0.112)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.185 (n=176)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 14.0 (IC base=+0.112)

- **PATRÓN** `ibs_20min` < `0.4286` → IC=+0.224 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4286 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` < `0.22` → IC=+0.126 (n=332)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` < 0.22 (IC base=+0.112)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.673` → IC=+0.161 (n=57)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 7.673 (IC base=+0.112)

- **PATRÓN** `volumen_regimen` > `0.853` → IC=+0.150 (n=244)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.853 (IC base=+0.112)

- **PATRÓN** `volumen_pendiente_norm` > `0.1104` → IC=+0.177 (n=94)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1104 (IC base=+0.112)

- **PATRÓN** `volumen_spike_ratio` > `2.2766` → IC=+0.204 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2766 (IC base=+0.112)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=315)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.01 (IC base=+0.112)

- **PATRÓN** `libro_liquidez` > `1978.8412` → IC=+0.159 (n=244)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 1978.8412 (IC base=+0.112)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0219` → IC=+0.196 (n=218)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0219 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.1617` → IC=+0.178 (n=212)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.1617 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.187 (n=164)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.165 (n=216)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 7.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `0.7013` → IC=+0.209 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7013 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.9847` → IC=+0.238 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9847 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.04` → IC=+0.241 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.04 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `1.2177` → IC=+0.167 (n=481)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2177 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` > `0.8308` → IC=+0.189 (n=320)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 0.8308 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.0805` → IC=+0.217 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0805 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `2.1697` → IC=+0.179 (n=390)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 2.1697 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` > `1.8145` → IC=+0.167 (n=295)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.8145 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.167 (n=539)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.164)

- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.258 (n=295)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0074 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.3766` → IC=+0.232 (n=389)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3766 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.221 (n=213)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.258 (n=209)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` < `0.1341` → IC=+0.308 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1341 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` < `1.0935` → IC=+0.228 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 1.0935 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.892` → IC=+0.267 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.892 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `0.7153` → IC=+0.245 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7153 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.2833` → IC=+0.330 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2833 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.7671` → IC=+0.266 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7671 (IC base=+0.220)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.186 (n=224)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 30.0 (IC base=+0.220)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.131 (n=166)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` > 0.0063 (IC base=+0.085)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.200 (n=181)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.085)

- **PATRÓN** `ibs_20min` > `0.617` → IC=+0.153 (n=327)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` > 0.617 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` > `0.7744` → IC=+0.240 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7744 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.104` → IC=+0.210 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.104 (IC base=+0.085)

- **PATRÓN** `volumen_pendiente_norm` > `0.1796` → IC=+0.228 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1796 (IC base=+0.085)

- **PATRÓN** `libro_liquidez` > `2961.7524` → IC=+0.126 (n=244)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 2961.7524 (IC base=+0.085)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.219 (n=112)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.060)

- **PATRÓN** `ibs_20min` < `0.4755` → IC=+0.122 (n=289)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.4755 (IC base=+0.060)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.58` → IC=+0.217 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.58 (IC base=+0.060)

- **PATRÓN** `volumen_regimen` < `0.6412` → IC=+0.136 (n=108)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.6412 (IC base=+0.060)

- **PATRÓN** `volumen_spike_ratio` < `1.6286` → IC=+0.126 (n=121)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.6286 (IC base=+0.060)

- **PATRÓN** `libro_liquidez` > `3871.0971` → IC=+0.124 (n=219)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 3871.0971 (IC base=+0.060)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.200 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=65)

- **FILTRO** `ibs_20min` < `0.3107` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3107
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=70)

- **FILTRO** `volumen_spike_ratio` > `2.223` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.223
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=54)

- **FILTRO** `libro_liquidez` < `5689.8897` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `libro_liquidez` < 5689.8897
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=70)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.147 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 15.0 (IC base=+0.016)

- **PATRÓN** `ibs_20min` > `0.9142` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9142 (IC base=+0.016)

- **PATRÓN** `dist_vwap_pct` > `0.1862` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.1862 (IC base=+0.016)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.351` → IC=+0.129 (n=33)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 4.351 (IC base=+0.016)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.229 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.165)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.189 (n=59)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0049 (IC base=+0.165)

- **PATRÓN** `drift_60min` |x|≤ `0.3358` → IC=+0.195 (n=129)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.3358 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=43)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.165)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.178 (n=116)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 14.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` < `0.6346` → IC=+0.195 (n=129)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.6346 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.0393` → IC=+0.167 (n=115)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.0393 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` > `0.5182` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.5182 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` < `0.2398` → IC=+0.189 (n=117)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.2398 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.016` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.016 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` < `1.2361` → IC=+0.195 (n=129)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 1.2361 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.091` → IC=+0.320 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.091 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `1.5475` → IC=+0.245 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5475 (IC base=+0.165)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.273 (n=73)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.259)

- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.289 (n=55)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0045 (IC base=+0.259)

- **PATRÓN** `drift_60min` |x|≤ `0.224` → IC=+0.276 (n=56)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.224 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.292 (n=75)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.259)

- **PATRÓN** `ibs_20min` > `0.9989` → IC=+0.300 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9989 (IC base=+0.259)

- **PATRÓN** `dist_vwap_pct` > `0.1417` → IC=+0.316 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1417 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.648` → IC=+0.367 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.648 (IC base=+0.259)

- **PATRÓN** `volumen_regimen` < `0.7015` → IC=+0.372 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7015 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` > `0.184` → IC=+0.379 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.184 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` < `2.3129` → IC=+0.275 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3129 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` > `1.9173` → IC=+0.296 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9173 (IC base=+0.259)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.367 (n=28)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.058)

- **PATRÓN** `drift_60min` |x|≤ `0.2707` → IC=+0.155 (n=56)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.2707 (IC base=+0.058)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.227 (n=42)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.058)

- **PATRÓN** `ibs_20min` < `0.6219` → IC=+0.136 (n=64)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.6219 (IC base=+0.058)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.025` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 6.025 (IC base=+0.058)

- **PATRÓN** `volumen_regimen` < `0.7011` → IC=+0.267 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7011 (IC base=+0.058)

- **PATRÓN** `libro_liquidez` > `9491.207` → IC=+0.283 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9491.207 (IC base=+0.058)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` < `0.5417` → IC=-0.208 (n=46)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5417
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=138)

- **FILTRO** `ibs_20min` > `0.66` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `ibs_20min` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=81)

- **FILTRO** `ballena_activa_n` > `20.0` → IC=-0.292 (n=22)

  - _Acción_: SKIP cuando `ballena_activa_n` > 20.0
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.125 (n=70)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 14.0 (IC base=+0.021)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.177 (n=63)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 1.0 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` > `0.5948` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.5948 (IC base=+0.021)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.856` → IC=+0.140 (n=48)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 6.856 (IC base=+0.021)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.006` → IC=+0.214 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.085)

- **PATRÓN** `ibs_20min` > `0.6522` → IC=+0.143 (n=54)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.6522 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` > `0.2226` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.2226 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.99` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.99 (IC base=+0.085)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=54)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.085)

- **PATRÓN** `ibs_20min` < `0.0773` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0773 (IC base=+0.029)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.205 (n=1155)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0077 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.169 (n=1287)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 15.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `0.9434` → IC=+0.288 (n=1156)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9434 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `1.0594` → IC=+0.254 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0594 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.496` → IC=+0.230 (n=1532)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.496 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `0.6307` → IC=+0.158 (n=600)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.6307 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `1.0839` → IC=+0.153 (n=816)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 1.0839 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.1654` → IC=+0.180 (n=639)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.1654 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.8959` → IC=+0.153 (n=1490)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.8959 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=2068)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `3104.3643` → IC=+0.191 (n=1155)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 3104.3643 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `168.0` → IC=+0.188 (n=1030)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 168.0 (IC base=+0.144)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.224 (n=1499)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0063 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.4333` → IC=+0.199 (n=2246)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4333 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.196 (n=1032)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.194 (n=1057)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 7.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` < `0.5455` → IC=+0.245 (n=2247)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5455 (IC base=+0.190)

- **PATRÓN** `dist_vwap_pct` < `0.7127` → IC=+0.178 (n=1850)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.7127 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.472` → IC=+0.202 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.472 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.61` → IC=+0.195 (n=2103)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` < 2.61 (IC base=+0.190)

- **PATRÓN** `volumen_regimen` < `0.6203` → IC=+0.177 (n=580)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6203 (IC base=+0.190)

- **PATRÓN** `volumen_regimen` > `1.1929` → IC=+0.189 (n=579)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` > 1.1929 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.2332` → IC=+0.252 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2332 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `2.257` → IC=+0.198 (n=704)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.257 (IC base=+0.190)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.159 (n=493)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 35.0 (IC base=+0.190)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.212 (n=189)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.159 (n=282)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 11.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `0.9489` → IC=+0.285 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9489 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.288` → IC=+0.348 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.288 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.1438` → IC=+0.150 (n=98)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.1438 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.163 (n=194)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.04 (IC base=+0.128)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.316 (n=145)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0063 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.215` → IC=+0.324 (n=191)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.215 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.291 (n=204)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.286)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.288 (n=154)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.286)

- **PATRÓN** `ibs_20min` < `0.578` → IC=+0.340 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.578 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.09` → IC=+0.314 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.09 (IC base=+0.286)

- **PATRÓN** `volumen_pendiente_norm` < `0.0647` → IC=+0.308 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0647 (IC base=+0.286)

- **PATRÓN** `volumen_pendiente_norm` > `0.2255` → IC=+0.306 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2255 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` > `1.5851` → IC=+0.294 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5851 (IC base=+0.286)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.321 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `1990.5404` → IC=+0.351 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1990.5404 (IC base=+0.286)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.282 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 69.0 (IC base=+0.286)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.189 (n=133)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0027 (IC base=+0.165)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.211 (n=133)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.190 (n=401)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 6.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.3404` → IC=+0.217 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3404 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` > `0.2633` → IC=+0.246 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2633 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.757` → IC=+0.227 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.757 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` < `0.6563` → IC=+0.189 (n=133)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.6563 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` > `1.099` → IC=+0.194 (n=181)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` > 1.099 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.1441` → IC=+0.230 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1441 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `2.5257` → IC=+0.201 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5257 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` > `1.4672` → IC=+0.204 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4672 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `11552.7989` → IC=+0.204 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11552.7989 (IC base=+0.165)

- **PATRÓN** `sigma_h` < `0.0021` → IC=+0.204 (n=133)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0021 (IC base=+0.168)

- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.172 (n=132)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0057 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.2546` → IC=+0.181 (n=349)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.2546 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.175 (n=377)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 7.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.175 (n=413)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 18.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` < `0.3628` → IC=+0.209 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3628 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` < `0.7539` → IC=+0.177 (n=435)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.7539 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.674` → IC=+0.228 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.674 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `0.6237` → IC=+0.233 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6237 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` > `1.2206` → IC=+0.179 (n=132)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 1.2206 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.1514` → IC=+0.285 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1514 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `1.7476` → IC=+0.214 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7476 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `1.4122` → IC=+0.190 (n=301)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 1.4122 (IC base=+0.168)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.169 (n=512)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.01 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `13218.3877` → IC=+0.179 (n=132)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 13218.3877 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `315.0` → IC=+0.225 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 315.0 (IC base=+0.168)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.270 (n=111)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0078 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.0714` → IC=+0.178 (n=113)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.0714 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.237 (n=154)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `0.717` → IC=+0.249 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.717 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.923` → IC=+0.345 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.923 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` < `0.2327` → IC=+0.173 (n=264)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` < 0.2327 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` < `2.1733` → IC=+0.158 (n=115)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1733 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `3.9033` → IC=+0.175 (n=118)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 3.9033 (IC base=+0.174)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.210 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.174)

- **PATRÓN** `libro_liquidez` > `1854.1544` → IC=+0.188 (n=222)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 1854.1544 (IC base=+0.174)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.340 (n=98)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.268)

- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.277 (n=101)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0078 (IC base=+0.268)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.272 (n=134)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.268)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.275 (n=296)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.268)

- **PATRÓN** `ibs_20min` < `0.5597` → IC=+0.337 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5597 (IC base=+0.268)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.008` → IC=+0.272 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.008 (IC base=+0.268)

- **PATRÓN** `volumen_pendiente_norm` < `0.1577` → IC=+0.224 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1577 (IC base=+0.268)

- **PATRÓN** `volumen_pendiente_norm` > `0.378` → IC=+0.267 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.378 (IC base=+0.268)

- **PATRÓN** `volumen_spike_ratio` < `3.6286` → IC=+0.263 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.6286 (IC base=+0.268)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.275 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.268)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.268)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.009` → IC=+0.149 (n=397)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.009 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.169 (n=361)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 8.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.3557` → IC=+0.197 (n=397)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.3557 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.8943` → IC=+0.206 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8943 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.539` → IC=+0.192 (n=193)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 4.539 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.6307` → IC=+0.189 (n=133)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.6307 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `1.2094` → IC=+0.159 (n=133)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 1.2094 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2693` → IC=+0.318 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2693 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.4166` → IC=+0.197 (n=364)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4166 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `3078.5215` → IC=+0.192 (n=355)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 3078.5215 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `170.0` → IC=+0.187 (n=180)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 170.0 (IC base=+0.138)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.230 (n=109)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.5023` → IC=+0.154 (n=325)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.5023 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.174 (n=228)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 11.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` < `0.0801` → IC=+0.245 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0801 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` < `0.727` → IC=+0.167 (n=343)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.727 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.474` → IC=+0.250 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.474 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `0.5836` → IC=+0.167 (n=109)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.5836 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` > `1.0934` → IC=+0.154 (n=108)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 1.0934 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.2603` → IC=+0.344 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2603 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `2.1688` → IC=+0.181 (n=236)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 2.1688 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `1.4473` → IC=+0.170 (n=268)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.4473 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `9053.953` → IC=+0.178 (n=147)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 9053.953 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `133.0` → IC=+0.227 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 133.0 (IC base=+0.143)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.165 (n=207)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0106 (IC base=+0.090)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.135 (n=313)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 12.0 (IC base=+0.090)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.163 (n=461)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.5 (IC base=+0.090)

- **PATRÓN** `dist_vwap_pct` > `0.7696` → IC=+0.254 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7696 (IC base=+0.090)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.503` → IC=+0.228 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.503 (IC base=+0.090)

- **PATRÓN** `libro_liquidez` > `2815.6056` → IC=+0.266 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2815.6056 (IC base=+0.090)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.172 (n=230)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 69.0 (IC base=+0.090)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.186 (n=189)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0058 (IC base=+0.111)

- **PATRÓN** `drift_60min` |x|≤ `0.1512` → IC=+0.147 (n=188)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.1512 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.177 (n=199)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 15.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` < `0.5833` → IC=+0.191 (n=428)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.5833 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` < `0.4697` → IC=+0.130 (n=384)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.4697 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.042` → IC=+0.130 (n=414)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` < 3.042 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `0.7026` → IC=+0.137 (n=188)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.7026 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` > `1.0506` → IC=+0.128 (n=194)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 1.0506 (IC base=+0.111)

- **PATRÓN** `volumen_pendiente_norm` > `0.0719` → IC=+0.161 (n=116)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.0719 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` > `1.7794` → IC=+0.172 (n=187)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.7794 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `1086.3059` → IC=+0.141 (n=382)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 1086.3059 (IC base=+0.111)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0255` → IC=+0.215 (n=184)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0255 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.189 (n=278)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 15.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` > `0.9684` → IC=+0.298 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9684 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` > `1.3437` → IC=+0.291 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.3437 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.048` → IC=+0.250 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.048 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` < `0.6122` → IC=+0.188 (n=184)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.6122 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` > `1.041` → IC=+0.191 (n=250)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 1.041 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.1732` → IC=+0.250 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1732 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` < `1.5675` → IC=+0.173 (n=221)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5675 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` > `1.8456` → IC=+0.179 (n=334)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 1.8456 (IC base=+0.170)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.183 (n=616)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.170)

- **PATRÓN** `libro_liquidez` > `3123.9012` → IC=+0.177 (n=184)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 3123.9012 (IC base=+0.170)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.216 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.170)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.300 (n=263)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.622` → IC=+0.222 (n=591)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.622 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.221 (n=549)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` < `0.4887` → IC=+0.276 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4887 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` < `1.1239` → IC=+0.219 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 1.1239 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.235` → IC=+0.268 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.235 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.977` → IC=+0.216 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.977 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` > `1.2332` → IC=+0.249 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2332 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.2857` → IC=+0.306 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2857 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.6341` → IC=+0.231 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6341 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.170 (n=310)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 37.0 (IC base=+0.210)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.149 (n=731)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.145 (n=119)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 17.0 (IC base=+0.079)

- **PATRÓN** `dist_vwap_pct` > `1.7325` → IC=+0.203 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.7325 (IC base=+0.079)

- **PATRÓN** `libro_liquidez` > `8352.5828` → IC=+0.132 (n=221)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 8352.5828 (IC base=+0.079)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.207 (n=247)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.3376` → IC=+0.167 (n=493)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.3376 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.177 (n=193)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.210 (n=222)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` < `0.6304` → IC=+0.154 (n=493)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.6304 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.6205` → IC=+0.165 (n=156)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.6205 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` < `0.7666` → IC=+0.143 (n=622)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.7666 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.898` → IC=+0.159 (n=256)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.898 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `1.2456` → IC=+0.158 (n=560)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.2456 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` > `0.7193` → IC=+0.141 (n=500)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.7193 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.0723` → IC=+0.169 (n=270)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.0723 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `2.508` → IC=+0.166 (n=554)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.508 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.149 (n=731)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `8306.7713` → IC=+0.155 (n=560)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 8306.7713 (IC base=+0.142)

### GBM_LATE_5M#BTC#5min
- **FILTRO** `dist_vwap_pct` < `0.6194` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.6194
  - _Potencial_: sin este filtro IC_bueno=+0.188 (n=46)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.146 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 12.0 (IC base=+0.059)

- **PATRÓN** `ibs_20min` < `0.9366` → IC=+0.135 (n=50)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.9366 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` > `0.6194` → IC=+0.188 (n=46)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.6194 (IC base=+0.059)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.972` → IC=+0.160 (n=48)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` < 3.972 (IC base=+0.059)

- **PATRÓN** `volumen_regimen` < `0.5135` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.5135 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` < `0.0831` → IC=+0.135 (n=50)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` < 0.0831 (IC base=+0.059)

- **PATRÓN** `libro_liquidez` > `12213.6971` → IC=+0.160 (n=45)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 12213.6971 (IC base=+0.059)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.201 (n=205)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.3098` → IC=+0.157 (n=307)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.3098 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.215 (n=121)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.1235` → IC=+0.201 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1235 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.6845` → IC=+0.174 (n=41)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.6845 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.369` → IC=+0.153 (n=309)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 6.369 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.1909` → IC=+0.144 (n=307)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.1909 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `0.6677` → IC=+0.150 (n=275)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.6677 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.0724` → IC=+0.197 (n=143)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.0724 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.5834` → IC=+0.163 (n=307)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 2.5834 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `11683.1626` → IC=+0.153 (n=275)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 11683.1626 (IC base=+0.140)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.149 (n=146)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0094 (IC base=+0.105)

- **PATRÓN** `drift_60min` |x|≤ `0.2077` → IC=+0.140 (n=73)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.2077 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.218 (n=69)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.105)

- **PATRÓN** `ibs_20min` < `0.2849` → IC=+0.132 (n=74)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.2849 (IC base=+0.105)

- **PATRÓN** `ibs_20min` > `0.7734` → IC=+0.141 (n=76)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.7734 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `1.1467` → IC=+0.232 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1467 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.326` → IC=+0.159 (n=39)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 10.326 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` < `1.372` → IC=+0.196 (n=54)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.372 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `7751.0166` → IC=+0.149 (n=166)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 7751.0166 (IC base=+0.105)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.254 (n=59)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.171)

- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.183 (n=118)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0065 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.2923` → IC=+0.225 (n=118)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2923 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.207 (n=121)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` < `0.5868` → IC=+0.183 (n=156)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.5868 (IC base=+0.171)

- **PATRÓN** `ibs_20min` > `0.1096` → IC=+0.204 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1096 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` > `0.198` → IC=+0.171 (n=77)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.198 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` < `0.6876` → IC=+0.181 (n=186)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.6876 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.54` → IC=+0.254 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.54 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `1.1701` → IC=+0.215 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1701 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` < `0.0898` → IC=+0.195 (n=162)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.0898 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `2.1612` → IC=+0.227 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1612 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `1.4319` → IC=+0.191 (n=173)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 1.4319 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `9437.7622` → IC=+0.175 (n=118)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 9437.7622 (IC base=+0.171)

### GBM_LATE_5M#SOL#5min
- **FILTRO** `hora_utc` > `5.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=55)

- **FILTRO** `sigma_ewma_delta_pct` < `3.03` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 3.03
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=22)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.773` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 4.773 (IC base=-0.006)

### GBM_LATE_60M
- **FILTRO** `ibs_20min` < `0.7736` → IC=-0.161 (n=57)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7736
  - _Potencial_: sin este filtro IC_bueno=+0.212 (n=116)

- **FILTRO** `sigma_h` > `0.0111` → IC=-0.296 (n=52)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0111
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=160)

- **FILTRO** `drift_60min` |x|> `0.0909` → IC=-0.262 (n=19)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.0909
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=37)

- **FILTRO** `hora_utc` > `9.0` → IC=-0.260 (n=102)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=110)

- **FILTRO** `dist_vwap_pct` > `0.1067` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1067
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=53)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.173 (n=148)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0054 (IC base=+0.052)

- **PATRÓN** `ibs_20min` > `0.9873` → IC=+0.275 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9873 (IC base=+0.052)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.157` → IC=+0.208 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.157 (IC base=+0.052)

- **PATRÓN** `volumen_pendiente_norm` < `0.0847` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0847 (IC base=+0.052)

- **PATRÓN** `volumen_spike_ratio` > `1.788` → IC=+0.283 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.788 (IC base=+0.052)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.133 (n=115)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.052)

- **PATRÓN** `libro_liquidez` > `1987.6172` → IC=+0.129 (n=95)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 1987.6172 (IC base=+0.052)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `sigma_h` > `0.0058` → IC=-0.149 (n=35)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0058
  - _Potencial_: sin este filtro IC_bueno=+0.162 (n=69)

- **FILTRO** `ibs_20min` < `0.7342` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7342
  - _Potencial_: sin este filtro IC_bueno=+0.189 (n=43)

- **FILTRO** `sigma_h` > `0.0036` → IC=-0.167 (n=34)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0036
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=36)

- **FILTRO** `hora_utc` > `2.0` → IC=-0.179 (n=51)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 2.0
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=19)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.328 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.057)

- **PATRÓN** `ibs_20min` > `0.7342` → IC=+0.189 (n=43)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.7342 (IC base=+0.057)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.15` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 13.15 (IC base=+0.057)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0071` → IC=-0.326 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0071
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=43)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.360 (n=41)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=23)

- **FILTRO** `ibs_20min` > `0.2768` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2768
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `volumen_regimen` > `0.8876` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8876
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=18)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.163 (n=78)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0059 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.133 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 15.0 (IC base=+0.097)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.346 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` < `0.2422` → IC=+0.214 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2422 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.138` → IC=+0.308 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.138 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` < `0.6023` → IC=+0.214 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6023 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` > `1.0919` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 1.0919 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `1923.3872` → IC=+0.191 (n=53)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 1923.3872 (IC base=+0.097)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.146 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=28)

- **FILTRO** `ibs_20min` < `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `ibs_20min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=19)

- **FILTRO** `sigma_h` > `0.0165` → IC=-0.309 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0165
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=59)

- **FILTRO** `hora_utc` < `17.0` → IC=-0.217 (n=58)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=20)

- **FILTRO** `hora_utc` > `4.0` → IC=-0.272 (n=55)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=23)

- **FILTRO** `ibs_20min` > `0.4286` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4286
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

- **FILTRO** `volumen_regimen` > `0.903` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.903
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=19)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=28)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=-0.026)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `7.0` → IC=-0.423 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=58)

- **FILTRO** `dist_vwap_pct` > `0.0767` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.0767
  - _Potencial_: sin este filtro IC_bueno=-0.290 (n=79)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.380 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.266 (n=75)

- **FILTRO** `dist_vwap_pct` < `0.1009` → IC=-0.354 (n=53)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1009
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=45)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `sigma_h` > `0.002` → IC=-0.237 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.002
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=18)

- **FILTRO** `sigma_h` < `0.002` → IC=-0.237 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.002
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=18)

- **FILTRO** `hora_utc` > `6.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=20)

- **FILTRO** `ibs_20min` > `0.0328` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `ibs_20min` > 0.0328
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=12)

- **FILTRO** `ibs_20min` < `0.5407` → IC=-0.286 (n=26)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5407
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `sigma_ewma_delta_pct` < `8.204` → IC=-0.250 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 8.204
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=5)

- **FILTRO** `volumen_regimen` < `1.6138` → IC=-0.286 (n=26)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.6138
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `sigma_h` < `0.0019` → IC=-0.318 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0019
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=21)

- **FILTRO** `drift_60min` |x|> `0.0966` → IC=-0.262 (n=19)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.0966
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=20)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=21)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.274 (n=29)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=12)

- **FILTRO** `ibs_20min` > `0.6267` → IC=-0.364 (n=20)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6267
  - _Potencial_: sin este filtro IC_bueno=-0.152 (n=21)

- **FILTRO** `dist_vwap_pct` < `0.0931` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0931
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=14)

- **FILTRO** `sigma_ewma_delta_pct` < `7.79` → IC=-0.294 (n=32)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 7.79
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **FILTRO** `sigma_ewma_delta_pct` > `4.524` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.524
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=26)

- **FILTRO** `volumen_regimen` > `0.807` → IC=-0.318 (n=20)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.807
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=21)

- **FILTRO** `libro_liquidez` < `4361.6218` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `libro_liquidez` < 4361.6218
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=21)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_h` > `0.0019` → IC=-0.420 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0019
  - _Potencial_: sin este filtro IC_bueno=-0.318 (n=9)

- **FILTRO** `drift_60min` |x|> `0.046` → IC=-0.413 (n=21)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.046
  - _Potencial_: sin este filtro IC_bueno=-0.346 (n=11)

- **FILTRO** `hora_utc` > `3.0` → IC=-0.413 (n=21)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.346 (n=11)

- **FILTRO** `ibs_20min` < `0.6354` → IC=-0.462 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6354
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **FILTRO** `dist_vwap_pct` < `0.1247` → IC=-0.403 (n=29)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1247
  - _Potencial_: sin este filtro IC_bueno=-0.300 (n=3)

- **FILTRO** `sigma_ewma_delta_pct` < `10.347` → IC=-0.463 (n=25)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 10.347
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **FILTRO** `volumen_regimen` < `1.0933` → IC=-0.423 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.0933
  - _Potencial_: sin este filtro IC_bueno=-0.300 (n=8)

- **FILTRO** `libro_liquidez` < `2178.6163` → IC=-0.457 (n=21)

  - _Acción_: SKIP cuando `libro_liquidez` < 2178.6163
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=11)

- **FILTRO** `sigma_h` > `0.0018` → IC=-0.346 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0018
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `drift_60min` |x|> `0.0425` → IC=-0.250 (n=22)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.0425
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=18)

- **FILTRO** `ibs_20min` > `0.8144` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8144
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=17)

- **FILTRO** `dist_vwap_pct` < `0.2821` → IC=-0.286 (n=26)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.2821
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **FILTRO** `dist_vwap_pct` > `0.0802` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.0802
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=15)

- **FILTRO** `sigma_ewma_delta_pct` < `5.949` → IC=-0.318 (n=20)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 5.949
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=13)

- **FILTRO** `volumen_regimen` > `0.6161` → IC=-0.346 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.6161
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `sigma_h` > `0.0046` → IC=-0.273 (n=20)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0046
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `sigma_h` < `0.0063` → IC=-0.250 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `drift_60min` |x|> `0.0825` → IC=-0.350 (n=18)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.0825
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=11)

- **FILTRO** `ibs_20min` < `0.6` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `sigma_ewma_delta_pct` < `5.022` → IC=-0.269 (n=24)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 5.022
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=4)

- **FILTRO** `volumen_regimen` > `0.5422` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.5422
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **FILTRO** `volumen_regimen` < `1.0086` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.0086
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `libro_liquidez` < `1333.5577` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 1333.5577
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `sigma_h` > `0.0052` → IC=-0.342 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0052
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `sigma_h` < `0.0065` → IC=-0.382 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0065
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.382 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **FILTRO** `ibs_20min` > `0.2759` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2759
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `ibs_20min` < `0.7391` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7391
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **FILTRO** `dist_vwap_pct` < `0.3782` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.3782
  - _Potencial_: sin este filtro IC_bueno=-0.300 (n=8)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.441 (n=15)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **FILTRO** `libro_liquidez` < `1344.8221` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 1344.8221
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=6)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` < `0.5964` → IC=-0.245 (n=45)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5964
  - _Potencial_: sin este filtro IC_bueno=+0.152 (n=136)

- **FILTRO** `ibs_20min` > `0.5131` → IC=-0.194 (n=34)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5131
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=103)

- **PATRÓN** `ibs_20min` > `0.5964` → IC=+0.152 (n=136)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.5964 (IC base=+0.052)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.127 (n=73)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 12.0 (IC base=+0.025)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `hora_utc` > `6.0` → IC=-0.125 (n=38)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=20)

- **FILTRO** `ibs_20min` < `0.3927` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3927
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=39)

- **PATRÓN** `ibs_20min` > `0.7184` → IC=+0.177 (n=29)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.7184 (IC base=-0.067)

- **PATRÓN** `sigma_h` > `0.0031` → IC=+0.140 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` > 0.0031 (IC base=+0.097)

- **PATRÓN** `drift_60min` |x|≤ `0.1242` → IC=+0.167 (n=31)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1242 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.237 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.097)

- **PATRÓN** `ibs_20min` < `0.3394` → IC=+0.167 (n=49)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.3394 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.84` → IC=+0.176 (n=35)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 3.84 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` < `1.0498` → IC=+0.122 (n=43)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.0498 (IC base=+0.097)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.258 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.1051` → IC=+0.192 (n=24)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1051 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.8361` → IC=+0.258 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8361 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.212` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.212 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `0.6735` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.6735 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2399.5952` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2399.5952 (IC base=+0.125)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `hora_utc` < `16.0` → IC=-0.167 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14)

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
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.134 (n=99)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 6.0 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `2605.1459` → IC=+0.219 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2605.1459 (IC base=+0.111)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.143 (n=110)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 18.0 (IC base=+0.117)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.152 (n=44)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` < 0.495 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2554.1675` → IC=+0.156 (n=94)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2554.1675 (IC base=+0.117)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.134 (n=99)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 6.0 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `2605.1459` → IC=+0.219 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2605.1459 (IC base=+0.111)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.143 (n=110)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 18.0 (IC base=+0.117)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.152 (n=44)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` < 0.495 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2554.1675` → IC=+0.156 (n=94)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2554.1675 (IC base=+0.117)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `9.0` → IC=-0.185 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=42)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=97)

- **FILTRO** `libro_liquidez` < `2110.4161` → IC=-0.367 (n=28)

  - _Acción_: SKIP cuando `libro_liquidez` < 2110.4161
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=85)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=82)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `11321.3584` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 11321.3584
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=15)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.136 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

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
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=380)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.124 (n=131)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=334)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=88)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.285 (n=63)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=46)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_usd_total` < `35151.71` → IC=-0.176 (n=32)

  - _Acción_: SKIP cuando `liq_usd_total` < 35151.71
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=32)

- **FILTRO** `libro_liquidez` < `13988.6712` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 13988.6712
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

- **PATRÓN** `liq_usd_total` > `35151.71` → IC=+0.147 (n=32)

  - _Acción_: Kelly boost +0.74€ cuando `liq_usd_total` > 35151.71 (IC base=-0.015)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `0.8738` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.8738
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=48)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.155 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=36)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=46)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=110)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.139 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=92)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.123 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 11.0 (IC base=+0.039)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=115)

- **FILTRO** `liq_n` < `8.0` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `liq_n` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **FILTRO** `liq_usd_total` < `24810.11` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `liq_usd_total` < 24810.11
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

### LIQUIDACIONES_5M#XRP#5min
- **FILTRO** `liq_usd_total` < `5231.58` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `liq_usd_total` < 5231.58
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=18)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=20)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9861` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9861
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=79)

- **FILTRO** `py_entrada` > `0.56` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=79)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `hora_utc` > `12.0` → IC=-0.152 (n=44)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=53)

- **FILTRO** `libro_liquidez` < `4860.4415` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `libro_liquidez` < 4860.4415
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=11)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=72)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_usd_total` < `20545.57` → IC=-0.133 (n=28)

  - _Acción_: SKIP cuando `liq_usd_total` < 20545.57
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=10)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2155.7963` → IC=-0.176 (n=35)

  - _Acción_: SKIP cuando `libro_liquidez` < 2155.7963
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=105)

### MOMENTUM_IBS_15M#DOGE#15min
- **FILTRO** `ibs_20min` > `0.9587` → IC=-0.197 (n=74)

  - _Acción_: SKIP cuando `ibs_20min` > 0.9587
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=226)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=348)

### MOMENTUM_IBS_15M#SOL#15min
- **FILTRO** `drift_20min_pct` |x|> `0.1933` → IC=-0.137 (n=89)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1933
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=174)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.46` → IC=-0.167 (n=691)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=2155)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.224 (n=675)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=2114)

- **FILTRO** `ibs_20min` > `0.2738` → IC=-0.195 (n=697)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2738
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=2092)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.224 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=315)

- **FILTRO** `ibs_20min` < `0.7279` → IC=-0.189 (n=104)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7279
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=314)

- **FILTRO** `ibs_20min` > `0.76` → IC=-0.158 (n=118)

  - _Acción_: SKIP cuando `ibs_20min` > 0.76
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=358)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.123 (n=221)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=256)

- **FILTRO** `py_entrada` > `0.56` → IC=-0.220 (n=116)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=361)

- **FILTRO** `ballena_activa_n` > `42.0` → IC=-0.150 (n=161)

  - _Acción_: SKIP cuando `ballena_activa_n` > 42.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=316)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.186 (n=183)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=249)

- **FILTRO** `ibs_20min` < `0.7273` → IC=-0.209 (n=108)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7273
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=324)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.224 (n=114)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=354)

- **FILTRO** `ibs_20min` > `0.766` → IC=-0.212 (n=116)

  - _Acción_: SKIP cuando `ibs_20min` > 0.766
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=352)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.139 (n=128)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=385)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.203 (n=126)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=369)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.156 (n=120)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=375)

### MOMENTUM_IBS_15M_BALLENA#SOL#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.259 (n=106)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=332)

- **FILTRO** `ibs_20min` > `0.2759` → IC=-0.212 (n=109)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2759
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=329)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.188 (n=107)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=331)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.475` → IC=-0.192 (n=118)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=357)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=460)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.279 (n=143)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=292)

- **FILTRO** `drift_20min_pct` |x|> `0.2772` → IC=-0.130 (n=217)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.2772
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=218)

- **FILTRO** `ibs_20min` > `0.2917` → IC=-0.291 (n=108)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2917
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=327)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `hora_utc` < `16.0` → IC=-0.300 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=126)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=374)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=380)

### MOMENTUM_IBS_15M_FADE#BNB#15min
- **FILTRO** `libro_liquidez` < `2063.3848` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 2063.3848
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=55)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `ibs_20min` < `1.0` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=19)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `hora_utc` < `19.0` → IC=-0.300 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=13)

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
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=348)

### MOMENTUM_IBS_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=630)

### MOMENTUM_IBS_5M_BALLENA
- **FILTRO** `hora_utc` < `8.0` → IC=-0.142 (n=2031)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=4939)

- **FILTRO** `py_entrada` < `0.36` → IC=-0.285 (n=1676)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=5294)

- **FILTRO** `ibs_7min` < `0.7377` → IC=-0.231 (n=1741)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7377
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=5229)

- **FILTRO** `ballena_activa_n` > `19.0` → IC=-0.174 (n=2360)

  - _Acción_: SKIP cuando `ballena_activa_n` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=4610)

- **FILTRO** `py_entrada` > `0.69` → IC=-0.229 (n=1994)

  - _Acción_: SKIP cuando `py_entrada` > 0.69
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=6531)

- **FILTRO** `ibs_7min` > `0.7209` → IC=-0.171 (n=2131)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7209
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=6394)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.154 (n=218)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=731)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.327 (n=229)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=720)

- **FILTRO** `ibs_7min` < `0.9833` → IC=-0.199 (n=626)

  - _Acción_: SKIP cuando `ibs_7min` < 0.9833
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=323)

- **FILTRO** `ballena_activa_n` > `16.0` → IC=-0.264 (n=235)

  - _Acción_: SKIP cuando `ballena_activa_n` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=714)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.242 (n=354)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=1083)

- **FILTRO** `drift_7min_pct` |x|> `0.1047` → IC=-0.133 (n=718)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1047
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=719)

- **FILTRO** `ibs_7min` > `0.8333` → IC=-0.198 (n=359)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8333
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=1078)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.161 (n=290)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=1121)

- **FILTRO** `py_entrada` < `0.38` → IC=-0.252 (n=332)

  - _Acción_: SKIP cuando `py_entrada` < 0.38
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1079)

- **FILTRO** `ballena_activa_n` > `150.0` → IC=-0.170 (n=352)

  - _Acción_: SKIP cuando `ballena_activa_n` > 150.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=1059)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.222 (n=350)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1086)

- **FILTRO** `ballena_activa_n` > `120.0` → IC=-0.174 (n=357)

  - _Acción_: SKIP cuando `ballena_activa_n` > 120.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=1079)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.198 (n=243)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=731)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.333 (n=231)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=743)

- **FILTRO** `ibs_7min` < `0.2143` → IC=-0.279 (n=242)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2143
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=732)

- **FILTRO** `ballena_activa_n` > `16.0` → IC=-0.275 (n=242)

  - _Acción_: SKIP cuando `ballena_activa_n` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=732)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.262 (n=321)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=1170)

- **FILTRO** `ibs_7min` > `0.8184` → IC=-0.187 (n=372)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8184
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=1119)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.157 (n=359)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=828)

- **FILTRO** `py_entrada` < `0.36` → IC=-0.265 (n=292)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=895)

- **FILTRO** `ibs_7min` < `0.7689` → IC=-0.185 (n=296)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7689
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=891)

- **FILTRO** `ballena_activa_n` > `44.0` → IC=-0.212 (n=293)

  - _Acción_: SKIP cuando `ballena_activa_n` > 44.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=894)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.136 (n=374)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=803)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.286 (n=278)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=899)

- **FILTRO** `ibs_7min` > `0.1818` → IC=-0.156 (n=399)

  - _Acción_: SKIP cuando `ibs_7min` > 0.1818
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=778)

- **FILTRO** `ballena_activa_n` > `39.0` → IC=-0.216 (n=290)

  - _Acción_: SKIP cuando `ballena_activa_n` > 39.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=887)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.228 (n=314)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=991)

- **FILTRO** `ibs_7min` < `0.7727` → IC=-0.196 (n=324)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7727
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=981)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.196 (n=324)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=981)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.173 (n=387)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=1162)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.38` → IC=-0.290 (n=274)

  - _Acción_: SKIP cuando `py_entrada` < 0.38
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=870)

- **FILTRO** `ibs_7min` < `0.75` → IC=-0.240 (n=275)

  - _Acción_: SKIP cuando `ibs_7min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=869)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.245 (n=284)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=860)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.276 (n=293)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=1142)

- **FILTRO** `ibs_7min` > `0.8393` → IC=-0.150 (n=358)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8393
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=1077)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.123 (n=483)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=952)

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

- **PATRÓN** `delta_ratio` |x|> `0.3996` → IC=+0.146 (n=255)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.73€ cuando `delta_ratio` |x|> 0.3996 (IC base=+0.117)

- **PATRÓN** `total_vol_5m` < `451.5692` → IC=+0.200 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 451.5692 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `3571.4392` → IC=+0.151 (n=61)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3571.4392 (IC base=+0.117)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.244 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.127)

- **PATRÓN** `total_vol_5m` < `600.958` → IC=+0.149 (n=55)

  - _Acción_: Kelly boost +0.75€ cuando `total_vol_5m` < 600.958 (IC base=+0.127)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `libro_liquidez` > `3657.0978` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3657.0978 (IC base=+0.100)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.141 (n=37)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 15.0 (IC base=+0.069)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.069)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` < `0.0147` → IC=-0.141 (n=62)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0147
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=32)

- **FILTRO** `sigma_h` > `0.0084` → IC=-0.317 (n=80)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0084
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=82)

- **FILTRO** `T_h` > `111.9853` → IC=-0.373 (n=61)

  - _Acción_: SKIP cuando `T_h` > 111.9853
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=63)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `98.7549` → IC=-0.457 (n=21)

  - _Acción_: SKIP cuando `T_h` > 98.7549
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=23)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.265 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=-0.172)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0129` → IC=-0.184 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0129
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0048` → IC=-0.128 (n=49)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0048
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=50)

- **FILTRO** `T_h` > `143.1632` → IC=-0.344 (n=30)

  - _Acción_: SKIP cuando `T_h` > 143.1632
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=69)

- **FILTRO** `T_h` < `111.9668` → IC=-0.463 (n=25)

  - _Acción_: SKIP cuando `T_h` < 111.9668
  - _Potencial_: sin este filtro IC_bueno=-0.259 (n=52)

- **PATRÓN** `pct_vs_K` |x|≤ `1.3968` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 1.3968 (IC base=-0.025)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.283 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0045 (IC base=+0.143)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.005` → IC=-0.180 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `T_h` > `87.9947` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `T_h` > 87.9947
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.326 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=12)

### STREAK_FADE_15M
- **FILTRO** `hora_utc` < `8.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=25)

- **FILTRO** `streak_estiramiento` > `0.359` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.359
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

- **FILTRO** `py_entrada` < `0.49` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=74)

- **FILTRO** `streak_estiramiento` > `0.437` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.437
  - _Potencial_: sin este filtro IC_bueno=+0.389 (n=7)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 44.0 (IC base=+0.017)

### STREAK_FADE_5M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=182)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `12.0` → IC=-0.265 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=49)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.138 (n=56)

- **FILTRO** `hora_utc` > `4.0` → IC=-0.167 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.157 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 10.0 (IC base=+0.028)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.138 (n=56)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.5 (IC base=+0.028)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.250 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=82)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=91)

- **FILTRO** `streak_estiramiento` > `0.644` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.644
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=49)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=92)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=111)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=252)

- **FILTRO** `streak_estiramiento` > `0.5355` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.5355
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=46)

- **PATRÓN** `streak_len` < `3.0` → IC=+0.143 (n=124)

  - _Acción_: Kelly boost +0.71€ cuando `streak_len` < 3.0 (IC base=+0.060)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=124)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=183)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.125 (n=134)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 14.0 (IC base=+0.070)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.139 (n=70)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 25.0 (IC base=+0.070)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=1106)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=636)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=644)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.146 (n=125)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0029 (IC base=+0.109)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0676` → IC=+0.122 (n=376)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.61€ cuando `delta_ratio_macro` |x|> 0.0676 (IC base=+0.109)

- **PATRÓN** `ibs_15` > `0.5166` → IC=+0.195 (n=375)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.97€ cuando `ibs_15` > 0.5166 (IC base=+0.109)

- **PATRÓN** `dist_vwap_pct` > `0.3848` → IC=+0.173 (n=102)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.3848 (IC base=+0.109)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.629` → IC=+0.241 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.629 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `7101.5791` → IC=+0.146 (n=125)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 7101.5791 (IC base=+0.109)

- **PATRÓN** `ballena_activa_n` < `86.0` → IC=+0.167 (n=40)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 86.0 (IC base=+0.109)

### UPDOWN_GBM#5min
- **FILTRO** `ibs_15` < `0.1916` → IC=-0.216 (n=100)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1916
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=303)

- **FILTRO** `sigma_ewma_delta_pct` > `6.694` → IC=-0.204 (n=52)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.694
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=351)

### UPDOWN_GBM#60min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0397` → IC=-0.227 (n=20)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0397
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=41)

- **FILTRO** `sigma_h` < `0.0059` → IC=-0.206 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0059
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=46)

- **FILTRO** `ibs_15` < `0.1983` → IC=-0.265 (n=15)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1983
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=32)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `ibs_15` > `0.7305` → IC=-0.250 (n=18)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.7305
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=58)

- **FILTRO** `dist_vwap_pct` < `0.4006` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.4006
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=51)

- **FILTRO** `libro_liquidez` < `13834.2565` → IC=-0.278 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 13834.2565
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=51)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.160 (n=92)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0034 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.1945` → IC=+0.160 (n=104)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1945 (IC base=+0.136)

- **PATRÓN** `drift_15min` |x|≤ `0.4717` → IC=+0.153 (n=70)

  - _Acción_: Kelly boost +0.76€ cuando `drift_15min` |x|≤ 0.4717 (IC base=+0.136)

- **PATRÓN** `delta_ratio_macro` |x|> `0.262` → IC=+0.203 (n=35)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.262 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.160 (n=95)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 6.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.145 (n=105)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 16.0 (IC base=+0.136)

- **PATRÓN** `ibs_15` > `0.8714` → IC=+0.246 (n=69)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8714 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.2998` → IC=+0.173 (n=47)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.2998 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.5371` → IC=+0.150 (n=115)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.5371 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.252` → IC=+0.203 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.252 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `23.949` → IC=+0.137 (n=111)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 23.949 (IC base=+0.136)

### UPDOWN_GBM#BTC#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.015` → IC=-0.167 (n=31)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.015
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=11)

- **FILTRO** `sigma_h` < `0.0035` → IC=-0.196 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0035
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=21)

- **FILTRO** `ibs_15` < `0.1827` → IC=-0.239 (n=21)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1827
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=21)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `ibs_15` < `0.6404` → IC=-0.239 (n=21)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6404
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=66)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `ibs_15` < `0.617` → IC=-0.237 (n=36)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.617
  - _Potencial_: sin este filtro IC_bueno=+0.237 (n=74)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.127 (n=73)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0044 (IC base=+0.080)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1911` → IC=+0.200 (n=38)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1911 (IC base=+0.080)

- **PATRÓN** `ibs_15` > `0.617` → IC=+0.237 (n=74)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.617 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` < `0.0929` → IC=+0.146 (n=46)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.0929 (IC base=+0.080)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.463` → IC=+0.192 (n=37)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 9.463 (IC base=+0.080)

### UPDOWN_GBM#ETH#5min
- **FILTRO** `hora_utc` > `8.0` → IC=-0.167 (n=25)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=54)

- **FILTRO** `dist_vwap_pct` > `0.1641` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1641
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=64)

- **FILTRO** `sigma_h` > `0.006` → IC=-0.122 (n=117)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.006
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=228)

- **FILTRO** `drift_15min` |x|> `0.589` → IC=-0.182 (n=86)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.589
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=259)

### UPDOWN_GBM#ETH#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `13.193` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 13.193 (IC base=+0.038)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=42)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.038)

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
- **FILTRO** `ibs_15` < `0.1667` → IC=-0.382 (n=15)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1667
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=34)

- **FILTRO** `dist_vwap_pct` < `0.116` → IC=-0.156 (n=30)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.116
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=19)

- **FILTRO** `sigma_ewma_delta_pct` < `2.366` → IC=-0.158 (n=36)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 2.366
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=13)

### UPDOWN_GBM#SOL#60min
- **FILTRO** `sigma_h` > `0.0106` → IC=-0.179 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0106
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=27)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.155 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0106 (IC base=-0.009)

- **PATRÓN** `dist_vwap_pct` < `0.4088` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4088 (IC base=-0.009)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `hora_utc` < `6.0` → IC=+0.167 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 6.0 (IC base=+0.090)

- **PATRÓN** `ibs_15` > `0.55` → IC=+0.181 (n=89)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.91€ cuando `ibs_15` > 0.55 (IC base=+0.090)

- **PATRÓN** `dist_vwap_pct` > `0.4747` → IC=+0.269 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4747 (IC base=+0.090)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.569` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.569 (IC base=+0.090)

- **PATRÓN** `libro_liquidez` > `2503.3208` → IC=+0.148 (n=89)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 2503.3208 (IC base=+0.090)

- **PATRÓN** `ibs_15` < `0.1282` → IC=+0.190 (n=98)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.95€ cuando `ibs_15` < 0.1282 (IC base=+0.042)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.394 (n=45)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0055 (IC base=+0.301)

- **PATRÓN** `drift_60min` |x|≤ `0.0603` → IC=+0.351 (n=45)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0603 (IC base=+0.301)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1549` → IC=+0.315 (n=90)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1549 (IC base=+0.301)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.4171` → IC=+0.377 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.4171 (IC base=+0.301)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.324 (n=123)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.301)

- **PATRÓN** `ibs_15` > `0.8055` → IC=+0.361 (n=120)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8055 (IC base=+0.301)

- **PATRÓN** `dist_vwap_pct` > `0.4531` → IC=+0.375 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4531 (IC base=+0.301)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.489` → IC=+0.329 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.489 (IC base=+0.301)

- **PATRÓN** `libro_liquidez` > `6403.6866` → IC=+0.341 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6403.6866 (IC base=+0.301)

- **PATRÓN** `ballena_activa_n` < `540.0` → IC=+0.375 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 540.0 (IC base=+0.301)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1421` → IC=+0.306 (n=34)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1421 (IC base=+0.271)

- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.306 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0022 (IC base=+0.271)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.289 (n=36)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0033 (IC base=+0.271)

- **PATRÓN** `drift_60min` |x|≤ `0.1567` → IC=+0.300 (n=68)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1567 (IC base=+0.271)

- **PATRÓN** `drift_15min` |x|≤ `0.4366` → IC=+0.306 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4366 (IC base=+0.271)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.311 (n=72)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.271)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.275 (n=69)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.271)

- **PATRÓN** `ibs_15` > `0.8246` → IC=+0.319 (n=70)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8246 (IC base=+0.271)

- **PATRÓN** `dist_vwap_pct` > `0.4311` → IC=+0.380 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4311 (IC base=+0.271)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.871` → IC=+0.287 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.871 (IC base=+0.271)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.729` → IC=+0.271 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.729 (IC base=+0.271)

- **PATRÓN** `libro_liquidez` > `7959.8654` → IC=+0.342 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7959.8654 (IC base=+0.271)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.393 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.333)

- **PATRÓN** `drift_60min` |x|≤ `0.0534` → IC=+0.409 (n=20)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0534 (IC base=+0.333)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1506` → IC=+0.400 (n=38)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1506 (IC base=+0.333)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.341 (n=42)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.333)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.339 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.333)

- **PATRÓN** `ibs_15` > `0.7904` → IC=+0.424 (n=51)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7904 (IC base=+0.333)

- **PATRÓN** `dist_vwap_pct` > `0.1297` → IC=+0.338 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1297 (IC base=+0.333)

- **PATRÓN** `dist_vwap_pct` < `0.3157` → IC=+0.333 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3157 (IC base=+0.333)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.86` → IC=+0.393 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.86 (IC base=+0.333)

- **PATRÓN** `libro_liquidez` > `3128.4304` → IC=+0.350 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3128.4304 (IC base=+0.333)

- **PATRÓN** `ballena_activa_n` < `198.0` → IC=+0.340 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 198.0 (IC base=+0.333)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `ibs_15` < `0.4476` → IC=-0.279 (n=93)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.4476
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=281)

- **FILTRO** `sigma_ewma_delta_pct` > `16.973` → IC=-0.187 (n=314)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 16.973
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=2171)

- **PATRÓN** `ibs_15` > `0.4476` → IC=+0.147 (n=281)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.73€ cuando `ibs_15` > 0.4476 (IC base=-0.054)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0628` → IC=+0.382 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0628 (IC base=-0.094)

- **PATRÓN** `ibs_15` < `0.3345` → IC=+0.344 (n=88)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3345 (IC base=-0.094)

- **PATRÓN** `dist_vwap_pct` < `0.1207` → IC=+0.253 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1207 (IC base=-0.094)

- **PATRÓN** `ballena_activa_n` < `152.0` → IC=+0.287 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 152.0 (IC base=-0.094)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `hora_utc` > `16.0` → IC=-0.244 (n=135)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=421)

- **FILTRO** `sigma_ewma_delta_pct` > `18.835` → IC=-0.245 (n=108)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.835
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=448)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.4359` → IC=-0.378 (n=39)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.4359
  - _Potencial_: sin este filtro IC_bueno=+0.164 (n=117)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=139)

- **PATRÓN** `drift_60min` |x|≤ `0.0629` → IC=+0.167 (n=40)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.0629 (IC base=+0.025)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3346` → IC=+0.196 (n=54)

  - _Acción_: Kelly boost +0.98€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3346 (IC base=+0.025)

- **PATRÓN** `ibs_15` > `0.4359` → IC=+0.164 (n=117)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.82€ cuando `ibs_15` > 0.4359 (IC base=+0.025)

- **PATRÓN** `libro_liquidez` > `10575.7678` → IC=+0.232 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10575.7678 (IC base=+0.025)

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1584` → IC=+0.241 (n=52)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1584 (IC base=+0.225)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.281 (n=39)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.225)

- **PATRÓN** `drift_15min` |x|≤ `0.4361` → IC=+0.318 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4361 (IC base=+0.225)

- **PATRÓN** `delta_ratio_macro` |x|> `0.111` → IC=+0.227 (n=53)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.111 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.241 (n=56)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.226 (n=60)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.225)

- **PATRÓN** `ibs_15` < `0.3879` → IC=+0.352 (n=59)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3879 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` < `0.1085` → IC=+0.246 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1085 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` < `11.326` → IC=+0.267 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 11.326 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `7056.133` → IC=+0.328 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7056.133 (IC base=+0.225)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0085` → IC=-0.233 (n=73)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0085
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=144)

- **FILTRO** `sigma_ewma_delta_pct` > `8.908` → IC=-0.143 (n=197)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.908
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=668)

- **PATRÓN** `ibs_15` > `0.8125` → IC=+0.206 (n=15)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8125 (IC base=-0.089)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `hora_utc` > `6.0` → IC=-0.180 (n=148)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=80)

- **FILTRO** `sigma_ewma_delta_pct` > `14.308` → IC=-0.167 (n=28)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 14.308
  - _Potencial_: sin este filtro IC_bueno=-0.114 (n=200)

- **FILTRO** `libro_liquidez` < `2584.1244` → IC=-0.175 (n=75)

  - _Acción_: SKIP cuando `libro_liquidez` < 2584.1244
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=153)

- **FILTRO** `drift_15min` |x|> `1.5354` → IC=-0.142 (n=199)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.5354
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=599)

- **FILTRO** `sigma_ewma_delta_pct` > `15.454` → IC=-0.170 (n=98)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 15.454
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=700)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` > `0.0053` → IC=+0.294 (n=95)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0053 (IC base=+0.272)

- **PATRÓN** `drift_60min` |x|≤ `0.0529` → IC=+0.319 (n=70)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0529 (IC base=+0.272)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1908` → IC=+0.325 (n=95)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1908 (IC base=+0.272)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3917` → IC=+0.313 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3917 (IC base=+0.272)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.310 (n=214)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.272)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.272 (n=213)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.272)

- **PATRÓN** `ibs_15` > `0.8606` → IC=+0.315 (n=187)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8606 (IC base=+0.272)

- **PATRÓN** `dist_vwap_pct` > `0.2899` → IC=+0.361 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2899 (IC base=+0.272)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.866` → IC=+0.284 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.866 (IC base=+0.272)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.694` → IC=+0.271 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.694 (IC base=+0.272)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.271 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.272)

- **PATRÓN** `libro_liquidez` > `11817.8916` → IC=+0.333 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11817.8916 (IC base=+0.272)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.265 (n=79)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.255)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.309 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.255)

- **PATRÓN** `drift_60min` |x|≤ `0.1596` → IC=+0.292 (n=104)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1596 (IC base=+0.255)

- **PATRÓN** `drift_15min` |x|≤ `0.6649` → IC=+0.274 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.6649 (IC base=+0.255)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1425` → IC=+0.278 (n=79)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1425 (IC base=+0.255)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1313` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1313 (IC base=+0.255)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.275 (n=109)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.255)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.252 (n=119)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.255)

- **PATRÓN** `ibs_15` > `0.9661` → IC=+0.339 (n=54)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9661 (IC base=+0.255)

- **PATRÓN** `dist_vwap_pct` > `0.2911` → IC=+0.357 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2911 (IC base=+0.255)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.453` → IC=+0.306 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.453 (IC base=+0.255)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.438` → IC=+0.260 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.438 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `13108.0743` → IC=+0.286 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13108.0743 (IC base=+0.255)

- **PATRÓN** `ballena_activa_n` < `581.0` → IC=+0.278 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 581.0 (IC base=+0.255)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.297 (n=62)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.290)

- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.295 (n=42)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.0655` → IC=+0.314 (n=41)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0655 (IC base=+0.290)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1882` → IC=+0.364 (n=42)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1882 (IC base=+0.290)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3802` → IC=+0.336 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3802 (IC base=+0.290)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.330 (n=92)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.290)

- **PATRÓN** `ibs_15` > `0.863` → IC=+0.333 (n=82)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.863 (IC base=+0.290)

- **PATRÓN** `dist_vwap_pct` > `0.6145` → IC=+0.409 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6145 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.888` → IC=+0.308 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.888 (IC base=+0.290)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.298 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.290)

- **PATRÓN** `libro_liquidez` > `10408.2229` → IC=+0.409 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10408.2229 (IC base=+0.290)

- **PATRÓN** `ballena_activa_n` < `121.0` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 121.0 (IC base=+0.290)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1065` → IC=-0.208 (n=22)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1065
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=23)

- **FILTRO** `sigma_h` > `0.0048` → IC=-0.167 (n=22)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=23)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1233` → IC=-0.193 (n=86)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1233
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=261)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.159 (n=86)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=261)

### UPDOWN_OU_5M#DOGE#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1055` → IC=-0.289 (n=17)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1055
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `sigma_h` > `0.0068` → IC=-0.262 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

- **FILTRO** `drift_15min` |x|> `0.3434` → IC=-0.184 (n=17)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3434
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### WEEKLY_PRICE
- **PATRÓN** `T_h` < `63.9965` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 63.9965 (IC base=+0.081)

- **PATRÓN** `ratio` < `0.9722` → IC=+0.450 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9722 (IC base=+0.081)

- **PATRÓN** `T_h` > `146.1038` → IC=+0.441 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1038 (IC base=+0.341)

- **PATRÓN** `ratio` < `1.0177` → IC=+0.243 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 1.0177 (IC base=+0.341)

- **PATRÓN** `ratio` > `1.0126` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `ratio` > 1.0126 (IC base=+0.341)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` < `111.996` → IC=+0.333 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 111.996 (IC base=+0.259)

- **PATRÓN** `pct_dist` |x|≤ `0.6014` → IC=+0.284 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `pct_dist` |x|≤ 0.6014 (IC base=+0.259)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` < `87.9936` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 87.9936 (IC base=+0.115)

- **PATRÓN** `T_h` > `145.7785` → IC=+0.309 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7785 (IC base=+0.300)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1118` → IC=+0.454 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1118 (IC base=+0.417)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-SIGMA-SOL-60MIN**: `UPDOWN_GBM#SOL#60min` gana cuando sigma_h < 0.0106 (IC=+0.155 n=27). Implementar como filtro pre-predicción en shadow_predict.py.
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5166 sube el IC de +0.109 a +0.195 en UPDOWN_GBM#15min (n=375). Ya aplicado como kelly_boost=+0.97€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.8714 sube el IC de +0.136 a +0.246 en UPDOWN_GBM#BTC#15min (n=69). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.617 sube el IC de +0.080 a +0.237 en UPDOWN_GBM#ETH#15min (n=74). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.056 a +0.265 en UPDOWN_GBM#SOL#15min (n=32). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.55 sube el IC de +0.090 a +0.181 en UPDOWN_GBM#XRP#15min (n=89). Ya aplicado como kelly_boost=+0.91€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1282 sube el IC de +0.042 a +0.190 en UPDOWN_GBM#XRP#15min (n=98). Ya aplicado como kelly_boost=+0.95€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3345 sube el IC de -0.094 a +0.344 en UPDOWN_GBM_15M_TARDIO (n=88). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.4359 sube el IC de +0.025 a +0.164 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=117). Ya aplicado como kelly_boost=+0.82€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3879 sube el IC de +0.225 a +0.352 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=59). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8125 sube el IC de -0.089 a +0.206 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=15). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8606 sube el IC de +0.272 a +0.315 en UPDOWN_GBM_IBS_ALTO (n=187). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.9661 sube el IC de +0.255 a +0.339 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=54). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.863 sube el IC de +0.290 a +0.333 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=82). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.8055 sube el IC de +0.301 a +0.361 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=120). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8246 sube el IC de +0.271 a +0.319 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=70). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7904 sube el IC de +0.333 a +0.424 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=51). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min` — IC=+0.348 n=31. Faltan ~9 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL` — IC=+0.348 n=31. Faltan ~9 resoluciones para umbral n≥40. ETA: ~6h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 584 | +0.085 | +46.31€ | 2 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 584 | +0.085 | +46.31€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 340 | +0.111 | +35.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 340 | +0.111 | +35.30€ | 0 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 215 | +0.030 | +0.07€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 215 | +0.030 | +0.07€ | 5 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 29 | +0.177 | +10.93€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 29 | +0.177 | +10.93€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 6337 | -0.098 | -827.74€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 657 | -0.086 | -112.53€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 5680 | -0.099 | -715.21€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 1005 | +0.020 | -108.09€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 1005 | +0.020 | -108.09€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 657 | -0.086 | -112.53€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 657 | -0.086 | -112.53€ | 2 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 359 | -0.137 | -154.67€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 359 | -0.137 | -154.67€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 725 | -0.137 | -38.80€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 725 | -0.137 | -38.80€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 2103 | -0.076 | -101.56€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 2103 | -0.076 | -101.56€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 1488 | -0.186 | -312.09€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 1488 | -0.186 | -312.09€ | 1 | 0 |
| ✅ FAVORITO_CONFIRMADO | 28934 | +0.114 | -1891.02€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 5472 | +0.187 | -184.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 107 | -0.105 | -50.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 20272 | +0.094 | -1626.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 3083 | +0.122 | -29.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 3401 | +0.063 | -585.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 19 | -0.068 | +0.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#240min | 5 | -0.089 | -6.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 3377 | +0.064 | -579.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 6033 | +0.134 | -126.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 1537 | +0.197 | -86.11€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 3379 | +0.110 | -78.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 1075 | +0.132 | +60.61€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 3410 | +0.077 | -463.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 19 | +0.023 | -2.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 3390 | +0.077 | -458.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 6469 | +0.130 | -53.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 1989 | +0.171 | -1.27€ | 0 | 8 |
| 🚫 FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 3375 | +0.116 | -28.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 1093 | +0.105 | -15.73€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 6219 | +0.131 | -419.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 1891 | +0.203 | -94.17€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 46 | +0.000 | -9.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 3367 | +0.092 | -240.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 915 | +0.131 | -74.60€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 3402 | +0.105 | -243.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 17 | -0.022 | -0.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 3384 | +0.105 | -241.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 5447 | +0.176 | -401.39€ | 3 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 5447 | +0.176 | -401.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 1370 | +0.171 | -137.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 1370 | +0.171 | -137.52€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 107 | -0.124 | +1.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 107 | -0.124 | +1.58€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 1360 | +0.162 | -157.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 1360 | +0.162 | -157.56€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 1220 | +0.232 | -30.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 1220 | +0.232 | -30.70€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 1311 | +0.190 | -90.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 1311 | +0.190 | -90.94€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 276 | +0.442 | +1.16€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 276 | +0.442 | +1.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 103 | +0.443 | +1.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 103 | +0.443 | +1.74€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 105 | +0.425 | -1.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 105 | +0.425 | -1.99€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 65 | +0.440 | +1.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 65 | +0.440 | +1.28€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 14518 | +0.193 | -1243.21€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 14518 | +0.193 | -1243.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 2674 | +0.125 | -494.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 2674 | +0.125 | -494.12€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 2256 | +0.238 | -45.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 2256 | +0.238 | -45.08€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 2510 | +0.163 | -321.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 2510 | +0.163 | -321.06€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 2298 | +0.234 | -53.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 2298 | +0.234 | -53.74€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 2336 | +0.220 | -101.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 2336 | +0.220 | -101.77€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 2444 | +0.189 | -227.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 2444 | +0.189 | -227.43€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 5235 | +0.131 | +146.79€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 5235 | +0.131 | +146.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 2599 | +0.139 | +112.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 2599 | +0.139 | +112.39€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 2636 | +0.122 | +34.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 2636 | +0.122 | +34.40€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 734 | +0.300 | +8.10€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 734 | +0.300 | +8.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 314 | +0.279 | -7.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 314 | +0.279 | -7.66€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 344 | +0.303 | +10.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 344 | +0.303 | +10.69€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 76 | +0.359 | +5.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 76 | +0.359 | +5.06€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 306 | +0.409 | -16.19€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 306 | +0.409 | -16.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 136 | +0.406 | -7.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 136 | +0.406 | -7.91€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 139 | +0.415 | -6.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 139 | +0.415 | -6.97€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 31 | +0.348 | -1.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 31 | +0.348 | -1.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 187 | +0.103 | +1.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 57 | +0.110 | +0.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 130 | +0.099 | +0.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 6 | +0.075 | +2.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 6 | +0.075 | +2.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 153 | +0.106 | +2.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 23 | +0.140 | +1.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 130 | +0.099 | +0.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 28 | +0.033 | -3.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 28 | +0.033 | -3.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 5068 | +0.097 | -179.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 519 | +0.049 | -35.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 4549 | +0.102 | -144.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 3502 | +0.096 | -89.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 519 | +0.049 | -35.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 2983 | +0.104 | -54.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 1566 | +0.100 | -89.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 1566 | +0.100 | -89.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 403 | +0.283 | -27.14€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 403 | +0.283 | -27.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 403 | +0.283 | -27.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 403 | +0.283 | -27.14€ | 0 | 4 |
| ✅ GBM_LATE_15M | 6851 | +0.044 | +2085.47€ | 0 | 18 |
| ✅ GBM_LATE_15M#15min | 6851 | +0.044 | +2085.47€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 881 | +0.174 | +553.31€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 881 | +0.174 | +553.31€ | 0 | 18 |
| ✅ GBM_LATE_15M#BTC | 962 | +0.176 | +560.77€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 962 | +0.176 | +560.77€ | 0 | 31 |
| ✅ GBM_LATE_15M#DOGE | 890 | +0.188 | +604.04€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 890 | +0.188 | +604.04€ | 0 | 19 |
| ✅ GBM_LATE_15M#ETH | 1113 | -0.048 | +23.54€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 1113 | -0.048 | +23.54€ | 2 | 7 |
| ✅ GBM_LATE_15M#SOL | 1315 | -0.039 | +150.49€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 1315 | -0.039 | +150.49€ | 4 | 4 |
| ✅ GBM_LATE_15M#XRP | 1690 | -0.051 | +193.33€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 1690 | -0.051 | +193.33€ | 4 | 5 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 7804 | +0.044 | +2931.07€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 7804 | +0.044 | +2931.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 1163 | -0.029 | +504.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 1163 | -0.029 | +504.04€ | 1 | 3 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 1722 | -0.033 | +172.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 1722 | -0.033 | +172.91€ | 0 | 1 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 755 | +0.241 | +692.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 755 | +0.241 | +692.98€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 1344 | -0.042 | +15.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 1344 | -0.042 | +15.04€ | 8 | 3 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 1435 | -0.014 | +295.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 1435 | -0.014 | +295.68€ | 5 | 8 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 1385 | +0.235 | +1250.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 1385 | +0.235 | +1250.42€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 5475 | +0.169 | +3733.88€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 5475 | +0.169 | +3733.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 666 | +0.190 | +481.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 666 | +0.190 | +481.12€ | 0 | 18 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 934 | +0.169 | +636.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 934 | +0.169 | +636.50€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 659 | +0.201 | +507.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 659 | +0.201 | +507.48€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 914 | +0.165 | +587.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 914 | +0.165 | +587.68€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 1074 | +0.115 | +601.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 1074 | +0.115 | +601.39€ | 1 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 1228 | +0.191 | +919.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 1228 | +0.191 | +919.70€ | 0 | 24 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 924 | +0.073 | +164.79€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 924 | +0.073 | +164.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 26 | +0.071 | +4.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 26 | +0.071 | +4.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 264 | +0.113 | +88.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 264 | +0.113 | +88.44€ | 4 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 194 | +0.173 | +58.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 194 | +0.173 | +58.00€ | 1 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 291 | -0.022 | +0.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 291 | -0.022 | +0.07€ | 3 | 4 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 148 | +0.060 | +14.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 148 | +0.060 | +14.84€ | 0 | 6 |
| ✅ GBM_LATE_15M_TARDIO | 6391 | +0.166 | +4139.20€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#15min | 6391 | +0.166 | +4139.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 843 | +0.183 | +580.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 843 | +0.183 | +580.60€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 1058 | +0.167 | +680.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 1058 | +0.167 | +680.32€ | 0 | 28 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 833 | +0.219 | +692.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 833 | +0.219 | +692.33€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 961 | +0.141 | +515.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 961 | +0.141 | +515.95€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 1175 | +0.101 | +563.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 1175 | +0.101 | +563.46€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 1521 | +0.191 | +1106.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 1521 | +0.191 | +1106.55€ | 0 | 24 |
| ✅ GBM_LATE_5M | 1188 | +0.118 | +494.44€ | 1 | 17 |
| ✅ GBM_LATE_5M#5min | 1188 | +0.118 | +494.44€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 6 | +0.000 | -0.36€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 6 | +0.000 | -0.36€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 475 | +0.129 | +253.19€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 475 | +0.129 | +253.19€ | 1 | 19 |
| ✅ GBM_LATE_5M#DOGE | 13 | -0.108 | -4.42€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 13 | -0.108 | -4.42€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH | 456 | +0.140 | +188.18€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 456 | +0.140 | +188.18€ | 0 | 23 |
| ✅ GBM_LATE_5M#SOL | 114 | -0.017 | +2.12€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 114 | -0.017 | +2.12€ | 2 | 1 |
| ✅ GBM_LATE_5M#XRP | 124 | +0.159 | +55.72€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 124 | +0.159 | +55.72€ | 0 | 0 |
| ✅ GBM_LATE_60M | 507 | -0.046 | +77.59€ | 5 | 7 |
| ✅ GBM_LATE_60M#60min | 507 | -0.046 | +77.59€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 174 | -0.006 | +4.02€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 174 | -0.006 | +4.02€ | 4 | 3 |
| ✅ GBM_LATE_60M#ETH | 181 | -0.019 | +50.80€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 181 | -0.019 | +50.80€ | 4 | 8 |
| ✅ GBM_LATE_60M#SOL | 152 | -0.123 | +22.77€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 152 | -0.123 | +22.77€ | 7 | 1 |
| 🚫 GBM_LATE_60M_FADE | 193 | -0.305 | -34.48€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 193 | -0.305 | -34.48€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 76 | -0.256 | -7.36€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 76 | -0.256 | -7.36€ | 17 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 65 | -0.351 | -19.05€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 65 | -0.351 | -19.05€ | 16 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 52 | -0.296 | -8.07€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 52 | -0.296 | -8.07€ | 17 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 318 | +0.041 | +7.18€ | 2 | 2 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 318 | +0.041 | +7.18€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 123 | +0.020 | +5.30€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 123 | +0.020 | +5.30€ | 2 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 79 | +0.080 | +5.19€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 79 | +0.080 | +5.19€ | 0 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 116 | +0.034 | -3.31€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 116 | +0.034 | -3.31€ | 1 | 5 |
| ✅ LATE_WINDOW_5MIN | 9 | +0.143 | +3.37€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 9 | +0.143 | +3.37€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 9 | +0.143 | +3.37€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 9 | +0.143 | +3.37€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 268 | +0.115 | +76.24€ | 0 | 5 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 268 | +0.115 | +76.24€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 268 | +0.115 | +76.24€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 268 | +0.115 | +76.24€ | 0 | 5 |
| ✅ LIQUIDACIONES_15M | 215 | -0.108 | -28.95€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 215 | -0.108 | -28.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 54 | -0.125 | -8.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 54 | -0.125 | -8.64€ | 2 | 0 |
| 🚫 LIQUIDACIONES_15M#DOGE | 22 | -0.208 | -5.32€ | 0 | 0 |
| 🚫 LIQUIDACIONES_15M#DOGE#15min | 22 | -0.208 | -5.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 44 | -0.043 | -3.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 44 | -0.043 | -3.91€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 44 | +0.000 | -0.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 44 | +0.000 | -0.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 46 | -0.167 | -8.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 46 | -0.167 | -8.95€ | 2 | 0 |
| ✅ LIQUIDACIONES_5M | 574 | -0.059 | -41.90€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 574 | -0.059 | -41.90€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 34 | -0.028 | -2.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 34 | -0.028 | -2.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 96 | -0.071 | -7.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 96 | -0.071 | -7.52€ | 2 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 67 | -0.094 | -7.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 67 | -0.094 | -7.35€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 155 | -0.022 | -4.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 155 | -0.022 | -4.09€ | 3 | 1 |
| ✅ LIQUIDACIONES_5M#SOL | 173 | -0.043 | -10.90€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 173 | -0.043 | -10.90€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 49 | -0.167 | -9.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 49 | -0.167 | -9.12€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M | 408 | -0.012 | -6.79€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 408 | -0.012 | -6.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 128 | -0.046 | -11.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 128 | -0.046 | -11.71€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 129 | -0.011 | -0.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 129 | -0.011 | -0.75€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 151 | +0.016 | +5.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 151 | +0.016 | +5.67€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 3835 | +0.002 | -49.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 3835 | +0.002 | -49.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 394 | +0.005 | +7.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 394 | +0.005 | +7.78€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 598 | +0.005 | -8.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 598 | +0.005 | -8.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 636 | -0.002 | -20.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 636 | -0.002 | -20.12€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 752 | +0.008 | +13.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 752 | +0.008 | +13.17€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 695 | -0.001 | -22.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 695 | -0.001 | -22.20€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 760 | -0.004 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 760 | -0.004 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 5635 | -0.037 | +156.22€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 5635 | -0.037 | +156.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 894 | -0.028 | +128.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 894 | -0.028 | +128.68€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 1009 | -0.032 | -21.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 1009 | -0.032 | -21.81€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 900 | -0.043 | +93.67€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 900 | -0.043 | +93.67€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 1008 | -0.037 | -32.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 1008 | -0.037 | -32.59€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 914 | -0.050 | -0.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 914 | -0.050 | -0.74€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 910 | -0.033 | -10.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 910 | -0.033 | -10.99€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 554 | -0.059 | -41.50€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 554 | -0.059 | -41.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 104 | -0.038 | -5.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 104 | -0.038 | -5.15€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 66 | -0.059 | -4.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 66 | -0.059 | -4.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 35 | -0.095 | -3.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 35 | -0.095 | -3.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 108 | -0.118 | -14.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 108 | -0.118 | -14.05€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 140 | -0.028 | -6.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 140 | -0.028 | -6.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 101 | -0.044 | -7.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 101 | -0.044 | -7.92€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M | 3019 | +0.005 | -2.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3019 | +0.005 | -2.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 126 | -0.039 | -1.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 126 | -0.039 | -1.34€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 185 | +0.008 | -2.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 185 | +0.008 | -2.27€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 136 | +0.000 | -1.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 136 | +0.000 | -1.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1009 | +0.010 | +10.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1009 | +0.010 | +10.56€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1385 | +0.006 | -2.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1385 | +0.006 | -2.03€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 178 | -0.006 | -5.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 178 | -0.006 | -5.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 15495 | -0.073 | +251.13€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 15495 | -0.073 | +251.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 2386 | -0.093 | +252.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 2386 | -0.093 | +252.35€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 2847 | -0.056 | +5.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 2847 | -0.056 | +5.87€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 2465 | -0.086 | +8.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 2465 | -0.086 | +8.50€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 2364 | -0.097 | -171.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 2364 | -0.097 | -171.83€ | 8 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 2854 | -0.049 | +24.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 2854 | -0.049 | +24.02€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 2579 | -0.066 | +132.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 2579 | -0.066 | +132.22€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6011 | -0.010 | -119.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6011 | -0.010 | -119.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 992 | -0.018 | -21.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 992 | -0.018 | -21.41€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1204 | +0.000 | -15.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1204 | +0.000 | -15.38€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1000 | -0.019 | -29.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1000 | -0.019 | -29.77€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1310 | -0.002 | -14.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1310 | -0.002 | -14.24€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 780 | -0.010 | -14.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 780 | -0.010 | -14.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 725 | -0.020 | -23.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 725 | -0.020 | -23.89€ | 2 | 0 |
| ✅ ORDER_FLOW_5M | 378 | +0.087 | +77.32€ | 1 | 3 |
| ✅ ORDER_FLOW_5M#5min | 242 | +0.102 | +64.72€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 73 | +0.127 | +31.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 73 | +0.127 | +31.94€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#DOGE | 41 | +0.081 | +7.34€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 41 | +0.081 | +7.34€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 29 | +0.113 | +7.99€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 29 | +0.113 | +7.99€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL | 43 | +0.100 | +9.30€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 43 | +0.100 | +9.30€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#XRP | 56 | +0.069 | +8.16€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 56 | +0.069 | +8.16€ | 0 | 2 |
| ✅ PRICE_TARGET_GBM | 256 | -0.163 | -20.27€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC | 114 | -0.233 | -32.63€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 99 | -0.262 | -31.90€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 15 | -0.022 | -0.74€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 97 | -0.146 | -3.16€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 78 | -0.163 | -6.13€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 19 | -0.068 | +2.97€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 45 | -0.011 | +15.52€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 38 | +0.000 | +14.95€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 7 | -0.019 | +0.57€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 215 | -0.182 | -23.08€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 41 | -0.058 | +2.80€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE | 176 | -0.163 | +30.67€ | 3 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 76 | -0.077 | +22.08€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 74 | -0.066 | +23.10€ | 0 | 1 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 68 | -0.243 | -5.68€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 64 | -0.242 | -7.07€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 32 | -0.176 | +14.27€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 30 | -0.156 | +16.11€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#atexpiry | 168 | -0.153 | +32.14€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#reach | 8 | -0.120 | -1.47€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 53 | +0.264 | +9.60€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC | 17 | -0.022 | -2.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 17 | -0.022 | -2.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 15 | +0.199 | +1.27€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 15 | +0.199 | +1.27€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 21 | +0.457 | +11.28€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 21 | +0.457 | +11.28€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 53 | +0.264 | +9.60€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 131 | -0.026 | -12.65€ | 4 | 1 |
| ✅ STREAK_FADE_15M#15min | 131 | -0.026 | -12.65€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 54 | -0.018 | -6.89€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 54 | -0.018 | -6.89€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 9 | -0.021 | -0.61€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 9 | -0.021 | -0.61€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 11 | +0.064 | +1.43€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 11 | +0.064 | +1.43€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 57 | -0.059 | -6.58€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 57 | -0.059 | -6.58€ | 0 | 0 |
| ✅ STREAK_FADE_5M | 939 | -0.007 | -31.66€ | 1 | 0 |
| ✅ STREAK_FADE_5M#5min | 939 | -0.007 | -31.66€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 322 | +0.000 | -5.50€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 322 | +0.000 | -5.50€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 313 | +0.011 | -3.80€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 313 | +0.011 | -3.80€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 117 | -0.013 | -7.68€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 117 | -0.013 | -7.68€ | 2 | 2 |
| ✅ STREAK_FADE_5M#XRP | 187 | -0.045 | -14.68€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 187 | -0.045 | -14.68€ | 4 | 0 |
| ✅ STREAK_FADE_60M | 29 | -0.081 | -3.00€ | 0 | 0 |
| ✅ STREAK_FADE_60M#60min | 29 | -0.081 | -3.00€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 18 | -0.135 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 18 | -0.135 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 11 | +0.021 | +0.31€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 11 | +0.021 | +0.31€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 1833 | +0.024 | +26.21€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 1833 | +0.024 | +26.21€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 611 | +0.022 | +4.84€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 611 | +0.022 | +4.84€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 323 | +0.014 | +2.05€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 323 | +0.014 | +2.05€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 550 | +0.025 | +6.28€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 550 | +0.025 | +6.28€ | 2 | 1 |
| ✅ STREAK_MOM_5M#XRP | 349 | +0.033 | +13.03€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 349 | +0.033 | +13.03€ | 2 | 2 |
| ✅ STRUCT_NO_15M | 2914 | +0.006 | -32.61€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 2914 | +0.006 | -32.61€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 1125 | +0.007 | -13.08€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 1125 | +0.007 | -13.08€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 1121 | +0.014 | -4.18€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 1121 | +0.014 | -4.18€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 668 | -0.007 | -15.36€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 668 | -0.007 | -15.36€ | 2 | 0 |
| ✅ UPDOWN_GBM | 5320 | +0.007 | +138.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 2056 | +0.043 | +189.65€ | 0 | 7 |
| ✅ UPDOWN_GBM#240min | 228 | +0.030 | +7.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 2643 | -0.018 | -55.70€ | 2 | 0 |
| ✅ UPDOWN_GBM#60min | 346 | -0.009 | -2.03€ | 3 | 0 |
| ✅ UPDOWN_GBM#BNB | 189 | +0.086 | +33.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 174 | +0.108 | +36.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 6 | +0.000 | +0.01€ | 0 | 0 |
| 🚫 UPDOWN_GBM#BNB#5min | 9 | -0.102 | -2.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 1148 | +0.015 | +51.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 214 | +0.065 | +22.92€ | 3 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 67 | +0.094 | +9.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 735 | +0.006 | +24.35€ | 3 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 114 | -0.043 | -6.57€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 673 | -0.002 | +2.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 117 | +0.097 | +27.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 8 | +0.000 | -0.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 548 | -0.024 | -24.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 1215 | +0.010 | +17.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 564 | +0.030 | +23.42€ | 1 | 5 |
| ✅ UPDOWN_GBM#ETH#240min | 66 | +0.088 | +6.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 424 | -0.026 | -16.90€ | 4 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 146 | +0.027 | +5.32€ | 0 | 2 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 1264 | -0.009 | -16.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 464 | -0.002 | -5.48€ | 1 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 51 | -0.028 | -3.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 651 | -0.005 | -5.97€ | 3 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 86 | -0.023 | -0.78€ | 1 | 2 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 829 | +0.003 | +50.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 523 | +0.054 | +85.40€ | 0 | 6 |
| ✅ UPDOWN_GBM#XRP#240min | 30 | -0.125 | -4.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 276 | -0.079 | -30.11€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 179 | +0.301 | +27.02€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 179 | +0.301 | +27.02€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 103 | +0.271 | +4.07€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 103 | +0.271 | +4.07€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 76 | +0.333 | +22.95€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 76 | +0.333 | +22.95€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO | 3397 | -0.083 | +391.19€ | 2 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 3397 | -0.083 | +391.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 279 | -0.059 | +130.15€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 279 | -0.059 | +130.15€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 702 | -0.169 | -87.63€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 702 | -0.169 | -87.63€ | 2 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 74 | +0.053 | +10.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 74 | +0.053 | +10.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 234 | +0.093 | +85.96€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 234 | +0.093 | +85.96€ | 2 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 1082 | -0.073 | +158.00€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 1082 | -0.073 | +158.00€ | 2 | 1 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 1026 | -0.091 | +94.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 1026 | -0.091 | +94.59€ | 5 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 26 | +0.000 | -1.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 26 | +0.000 | -1.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 26 | +0.000 | -1.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 26 | +0.000 | -1.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 279 | +0.272 | +194.61€ | 0 | 12 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 279 | +0.272 | +194.61€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 157 | +0.255 | +95.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 157 | +0.255 | +95.85€ | 0 | 14 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 122 | +0.290 | +98.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 122 | +0.290 | +98.76€ | 0 | 12 |
| ✅ UPDOWN_OU_5M | 392 | -0.071 | -33.76€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 392 | -0.071 | -33.76€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 239 | -0.015 | -13.20€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 239 | -0.015 | -13.20€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 32 | +0.000 | +2.54€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 32 | +0.000 | +2.54€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 28 | -0.200 | -6.19€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 28 | -0.200 | -6.19€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 31 | -0.167 | -4.88€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 31 | -0.167 | -4.88€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#SOL | 33 | -0.214 | -6.24€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#SOL#5min | 33 | -0.214 | -6.24€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 29 | -0.177 | -5.78€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 29 | -0.177 | -5.78€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 1057 | +0.286 | +427.80€ | 0 | 5 |
| ✅ WEEKLY_PRICE#BTC | 314 | +0.199 | -2.94€ | 0 | 2 |
| ✅ WEEKLY_PRICE#ETH | 329 | +0.255 | +70.48€ | 0 | 2 |
| ✅ WEEKLY_PRICE#SOL | 414 | +0.373 | +360.27€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.087) — sin ventaja clara. oversold(IBS<0.3): IC=+0.003 n=1842 | neutral: IC=+0.002 n=1998 | overbought(IBS>0.7): IC=+0.089 n=2107
  - _Datos_: n=6233 IC=+0.033 PNL=+482.11€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 5 celda(s) pasan gate riguroso completo de 201 evaluadas (n>=40) y 572 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=-0.002 < 0.08 — monitorear
  - _Datos_: n=464 IC=-0.002 PNL=-5.48€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=329/15 IC=+0.255 PNL=+70.48€ | BTC: n=314/15 IC=+0.199 PNL=-2.94€ | SOL: n=414/15 IC=+0.373 PNL=+360.27€

**🟡 H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.076 n=86165 | tras_1loss IC=+0.044 n=67071 | tras_2loss IC=+0.008 n=30488/40 | gap=+0.068 (umbral 0.05)

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
  - _Estado_: 5258 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.119 n=40/60 | contraria IC=-0.045 n=20 | gap=+0.165 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=48, boost estimado=+0.005. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 43/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=146/40 IC=+0.027 PNL=+5.32€ | BTC#60min: n=114/40 IC=-0.043 PNL=-6.57€ | SOL#60min: n=86/40 IC=-0.023 PNL=-0.78€

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=-0.003 n=533 | contrario_BTC IC=-0.012 n=404/40 | gap=-0.009 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.180 > 0.08 con n=73 PNL=+42.34€
  - _Datos_: n=73 IC=+0.180 PNL=+42.34€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.124 > 0.08 con n=91 PNL=+20.70€
  - _Datos_: n=91 IC=+0.124 PNL=+20.70€

**⏳ H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: 25
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: 11/25 ops en el filtro definido (IC actual=+0.190 PNL=+11.09€)
  - _Datos_: n=11 IC=+0.190 PNL=+11.09€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.331 > 0.1 con n=899 PNL=+432.52€
  - _Datos_: n=899 IC=+0.331 PNL=+432.52€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=51 IC=+0.047 PNL=+11.33€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=51 IC=+0.047 PNL=+11.33€

**⏳ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: 30
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: 13/30 ops en el filtro definido (IC actual=+0.065 PNL=+1.67€)
  - _Datos_: n=13 IC=+0.065 PNL=+1.67€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=5079 IC=+0.003 PNL=+87.69€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=5079 IC=+0.003 PNL=+87.69€

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

**〰️ H-CUSTOM-GBM-60MIN-BUYYES** — GBM 60min BUY_YES — ¿edge superior al BUY_NO?
  - _Hipótesis_: Análisis actual muestra BUY_YES 60min: 22/36 (61%) IC=+0.105 vs BUY_NO 60min: 8/14 (57%) IC=+0.044. En 60min parece que BUY_YES es la dirección dominante, al contrario que en 15min.
  - _Umbral_: n≥30 y IC>+0.08
  - _Acción_: Si BUY_YES 60min confirma IC≥0.10 n≥40 → prioridad live por encima de BUY_NO
  - _Estado_: n=285 IC=+0.012 PNL=+5.35€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=285 IC=+0.012 PNL=+5.35€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=61 IC=-0.103 PNL=-7.38€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=61 IC=-0.103 PNL=-7.38€

**🔴 H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.094 < -0.08 con n=94 PNL=-8.72€
  - _Datos_: n=94 IC=-0.094 PNL=-8.72€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.109 > 0.1 con n=499 PNL=+101.45€
  - _Datos_: n=499 IC=+0.109 PNL=+101.45€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=169 IC=+0.085 PNL=+40.94€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=169 IC=+0.085 PNL=+40.94€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=214 IC=+0.065 PNL=+22.92€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=214 IC=+0.065 PNL=+22.92€

**⏳ H-CUSTOM-DRIFT15-ZONA-MUERTA** — GBM#15min drift_15min ∈ [-0.3,+0.3] — zona muerta de señal
  - _Hipótesis_: Análisis n=127 GBM#15min: cuando drift_15min está entre -0.3 y +0.3 (mercado sin dirección clara) el IC es negativo (-0.043). Cuando drift>0.3 IC=+0.100 (n=28). Cuando drift<-1 IC=+0.048 (reversión). La señal requiere mercado con dirección clara.
  - _Umbral_: 50
  - _Acción_: Filtrar señales GBM#15min cuando drift_15min ∈ [-0.3, +0.3] — validar con n≥50 antes de implementar
  - _Estado_: 0/50 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-DRIFT15-MOMENTUM** — GBM#15min drift_15min > 0.3 — zona de momentum (señal fuerte)
  - _Hipótesis_: Cuando drift_15min > 0.3%/h el GBM captura bien la dirección: IC=+0.100 n=28 en todos GBM#15min; IC=+0.152 n=13 solo BTC. El mercado tiene dirección clara y el GBM la sigue. Hipótesis: este rango es donde la señal es real.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma IC>0.10 con n≥40 → boost ×1.2 en GBM#15min cuando drift_15min>0.3
  - _Estado_: n=1206 IC=+0.036 PNL=+78.55€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1206 IC=+0.036 PNL=+78.55€

**⏳ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: 17/30 ops en el filtro definido (IC actual=-0.201 PNL=-3.48€)
  - _Datos_: n=17 IC=-0.201 PNL=-3.48€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=65 IC=-0.007 PNL=+9.89€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=65 IC=-0.007 PNL=+9.89€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=73 IC=+0.020 PNL=+6.16€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=73 IC=+0.020 PNL=+6.16€

**⏳ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: 15
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: 4/15 ops en el filtro definido (IC actual=+0.000 PNL=-0.05€)
  - _Datos_: n=4 IC=+0.000 PNL=-0.05€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=1969 IC=-0.016 PNL=-46.97€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1969 IC=-0.016 PNL=-46.97€

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
  - _Estado_: 9/30 ops en el filtro definido (IC actual=+0.143 PNL=+3.37€)
  - _Datos_: n=9 IC=+0.143 PNL=+3.37€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=1440 IC=+0.023 PNL=+83.59€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1440 IC=+0.023 PNL=+83.59€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=416 IC=+0.034 PNL=-1.33€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=416 IC=+0.034 PNL=-1.33€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.105 > 0.08 con n=79 PNL=+18.39€
  - _Datos_: n=79 IC=+0.105 PNL=+18.39€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.164 > 0.08 con n=108 PNL=+3.02€
  - _Datos_: n=108 IC=+0.164 PNL=+3.02€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.098 > 0.08 con n=110 PNL=+27.17€
  - _Datos_: n=110 IC=+0.098 PNL=+27.17€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=3268 IC=+0.094 PNL=+641.92€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=3268 IC=+0.094 PNL=+641.92€

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
  - _Estado_: n=734 IC=+0.026 PNL=+42.51€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=734 IC=+0.026 PNL=+42.51€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.126 > 0.02 con n=196 PNL=+55.28€
  - _Datos_: n=196 IC=+0.126 PNL=+55.28€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.440 > 0.1 con n=579 PNL=+478.10€
  - _Datos_: n=579 IC=+0.440 PNL=+478.10€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=1364 IC=+0.026 PNL=+74.71€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=1364 IC=+0.026 PNL=+74.71€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.159 > 0.1 con n=739 PNL=+254.66€
  - _Datos_: n=739 IC=+0.159 PNL=+254.66€

**⏳ H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: 40
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: 18/40 ops en el filtro definido (IC actual=-0.225 PNL=-3.72€)
  - _Datos_: n=18 IC=-0.225 PNL=-3.72€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=391 IC=+0.042 PNL=+48.00€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=391 IC=+0.042 PNL=+48.00€

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
  - _Estado_: n=61 IC=+0.040 PNL=-7.01€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=61 IC=+0.040 PNL=-7.01€

**⏳ H-CUSTOM-ETH15-BUYNO-PRECIO-ALTO** — ETH#15min BUY_NO con precio_yes>0.55 pierde (NO longshot contra favorito)
  - _Hipótesis_: Detectado 2026-07-02: ult.60 shadow ETH15 BUY_NO — py_mkt~0.5 wr=0.67 PNL=+29.3 (n=49); py_mkt 0.6-0.8 wr 0.33-0 PNL=-5.75 (n=9). Filtro RETURN NONE (no SKIP) aplicado en shadow_predict.py (PY_MKT_MAX_BUY_NO_ETH15=0.55) el mismo dia -- bloquea la GENERACIÓN de la fila, no solo la decisión. Esta hipotesis trackea la zona filtrada: si las ops que HABRIAN caido aqui siguen apareciendo en otras estrategias o el IC forward de la zona se vuelve positivo, revisar el filtro. CAVEAT: n=9, muestra chica — el filtro se aplico por asimetria de riesgo (afecta a dinero live), no por significancia. ⚠️ 05-Ago (fix): la clave del filtro decía 'py_mkt', que NUNCA existió ni en features de UPDOWN_GBM (T_h/delta_ratio_macro/drift_15min/drift_60min/pct_spot_vs_ref/sigma_h) ni como columna top-level de results.csv -- corregida a 'precio_yes_mercado' (columna real). Aun así, con la clave correcta esta hipótesis NUNCA podrá acumular n mientras el filtro RETURN NONE siga activo -- es el mismo patrón 'frozen by design' que H-CUSTOM-LATE15-PHOTO-FINISH (más abajo): la propia protección impide generar los datos necesarios para volver a evaluarla. Para monitorearla de verdad haría falta un logger separado que capture la señal SIN aplicar el filtro (mismo patrón que gate_bucket_propio con data/markets histórico) -- no construido, pendiente decisión.
  - _Umbral_: 20
  - _Acción_: Si IC forward de la zona >0 con n>=20 → retirar filtro; si confirma negativo → considerar extender a BTC/SOL 15min
  - _Estado_: 0/20 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-PRECIO-YES-BARATO** — BUY_YES con precio de mercado 0.30-0.40 — mercado infravalora YES
  - _Hipótesis_: Detectado 2026-07-03 en benchmark de calibración del mercado (7d, estrategias GBM): en el bucket precio_yes_mercado [0.3-0.4) la frecuencia real de YES fue 0.45 vs 0.35 implícito (+0.10, n=38). Posible sesgo favorito-longshot suave en binarios de 15min (complemento del LONGSHOT ya activo para BUY_NO con py<0.20). Si se confirma, BUY_YES comprado en esa banda lleva viento de cola estructural del propio mercado, independiente del modelo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → kelly_boost ×1.1 para BUY_YES con precio_yes_mercado en [0.30,0.40), simétrico al longshot BUY_NO existente
  - _Estado_: n=3747 IC=-0.131 PNL=+299.11€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3747 IC=-0.131 PNL=+299.11€

**⏳ H-CUSTOM-LATE15-PHOTO-FINISH** — GBM_LATE_15M photo finish — entrar pegado al strike es moneda al aire cobrada como favorito
  - _Hipótesis_: Detectado 2026-07-05 validando contra nuestros datos la única idea aprovechable de un artículo-anuncio de copy-bot: GBM_LATE_15M con |drift_ventana_pct|<0.02 tenía IC=-0.145 n=181 (win 35%, -9.70€), estable en ambas mitades temporales (-0.163/-0.127), monótono con la distancia (0.02-0.05: IC=+0.061; ≥0.05: IC=+0.14..0.19) y consistente en crudo y normalizado por sigma (|d_gbm|<0.1 IC=-0.081 n=244). BTC (IC=-0.163 n=90) y ETH (-0.130 n=79) concentraban el daño; SOL/XRP apenas entran en esa zona. Mecanismo: sin distancia real al strike el resultado es ~50/50 pero py_entrada ya cobra favorito. Filtro GBM_LATE_DRIFT_VENT_MIN_PCT=0.02 aplicado en shadow_predict el 2026-07-05. Esta hipótesis trackea la zona filtrada: si vuelven a aparecer ops aquí, el filtro se ha roto.
  - _Umbral_: 200
  - _Acción_: Si aparecen ops nuevas en la zona → el filtro está roto, revisar shadow_predict. Si el buffer [0.02,0.05) se vuelve negativo con n≥60 forward → subir el corte a 0.05.
  - _Estado_: 0/200 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

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
  - _Estado_: n=530 IC=+0.139 PNL=+200.25€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=530 IC=+0.139 PNL=+200.25€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.109 > 0.08 con n=499 PNL=+101.45€
  - _Datos_: n=499 IC=+0.109 PNL=+101.45€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=533 IC=+0.006 PNL=+5.86€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=533 IC=+0.006 PNL=+5.86€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.094 > 0.08 con n=538 PNL=+319.36€
  - _Datos_: n=538 IC=+0.094 PNL=+319.36€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.136 > 0.08 con n=138 PNL=+28.80€
  - _Datos_: n=138 IC=+0.136 PNL=+28.80€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.228 < -0.1 con n=399 PNL=-30.03€
  - _Datos_: n=399 IC=-0.228 PNL=-30.03€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=933 IC=+0.150 PNL=+506.19€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=933 IC=+0.150 PNL=+506.19€

**⏳ H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: 40
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: 22/40 ops en el filtro definido (IC actual=+0.042 PNL=+0.30€)
  - _Datos_: n=22 IC=+0.042 PNL=+0.30€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=580 IC=-0.026 PNL=+35.16€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=580 IC=-0.026 PNL=+35.16€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.184 > 0.08 con n=498 PNL=+292.95€
  - _Datos_: n=498 IC=+0.184 PNL=+292.95€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=887 IC=-0.043 PNL=+111.65€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=887 IC=-0.043 PNL=+111.65€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.122 > 0.08 con n=231 PNL=-27.10€
  - _Datos_: n=231 IC=+0.122 PNL=-27.10€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.242 > 0.08 con n=1268 PNL=-110.67€
  - _Datos_: n=1268 IC=+0.242 PNL=-110.67€

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 9/40 ops en el filtro definido (IC actual=-0.021 PNL=+2.00€)
  - _Datos_: n=9 IC=-0.021 PNL=+2.00€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.117 n=139) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=139 IC=+0.117 PNL=+35.69€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.344 > 0.08 con n=62 PNL=+46.59€
  - _Datos_: n=62 IC=+0.344 PNL=+46.59€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.433 n=223) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=223 IC=+0.433 PNL=+302.61€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=2674 IC=+0.125 PNL=-494.12€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=2674 IC=+0.125 PNL=-494.12€

**⏳ H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: 40
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: 39/40 ops en el filtro definido (IC actual=+0.159 PNL=+19.22€)
  - _Datos_: n=39 IC=+0.159 PNL=+19.22€
