# Hipótesis automáticas — 2026-09-12 05:53 UTC
_Generado por shadow_postmortem.py sobre 400187 resoluciones (PNL=+42057.80€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.505` → IC=-0.153 (n=191)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.249 (n=389)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=382)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.249 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.117)

- **PATRÓN** `n_total_lado` > `69.0` → IC=+0.213 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 69.0 (IC base=+0.117)

- **PATRÓN** `banda_hit_calibrado` > `0.8071` → IC=+0.267 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8071 (IC base=+0.117)

- **PATRÓN** `banda_z` > `10.822` → IC=+0.235 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 10.822 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.134 (n=301)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 11.0 (IC base=+0.117)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=457)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.117)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.125 (n=382)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.495 (IC base=+0.036)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.385` → IC=-0.128 (n=146)

  - _Acción_: SKIP cuando `py_entrada` < 0.385
  - _Potencial_: sin este filtro IC_bueno=+0.251 (n=299)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=277)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=302)

- **PATRÓN** `py_entrada` > `0.385` → IC=+0.251 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.385 (IC base=+0.126)

- **PATRÓN** `n_total_lado` > `58.0` → IC=+0.200 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 58.0 (IC base=+0.126)

- **PATRÓN** `banda_hit_calibrado` > `0.8057` → IC=+0.269 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8057 (IC base=+0.126)

- **PATRÓN** `banda_z` > `11.788` → IC=+0.272 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.788 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.147 (n=236)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 11.0 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=375)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.146 (n=63)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 88.0 (IC base=+0.032)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.335` → IC=-0.267 (n=28)

  - _Acción_: SKIP cuando `py_entrada` < 0.335
  - _Potencial_: sin este filtro IC_bueno=+0.201 (n=95)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.153 (n=99)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=88)

- **PATRÓN** `py_entrada` > `0.51` → IC=+0.241 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.51 (IC base=+0.092)

- **PATRÓN** `banda_hit_calibrado` > `0.6329` → IC=+0.241 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6329 (IC base=+0.092)

- **PATRÓN** `banda_z` > `6.173` → IC=+0.162 (n=63)

  - _Acción_: Kelly boost +0.81€ cuando `banda_z` > 6.173 (IC base=+0.092)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.153 (n=99)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.02 (IC base=+0.092)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.130 (n=71)

  - _Acción_: Kelly boost +0.65€ cuando `py_entrada` < 0.495 (IC base=-0.024)

### BALLENAS_CONFIRMADAS_15M#XRP#15min
- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `147.73` → IC=-0.266 (n=5158)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 147.73
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=15476)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `143.19` → IC=-0.272 (n=717)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 143.19
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=2151)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `132.44` → IC=-0.299 (n=664)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 132.44
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=1994)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `146.06` → IC=-0.176 (n=1336)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 146.06
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=4009)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `156.37` → IC=-0.261 (n=1185)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 156.37
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=3555)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `158.35` → IC=-0.340 (n=1287)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 158.35
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=2619)

### CANDIDATA9_BOT_CONSENSO
- **FILTRO** `py_entrada` < `0.5` → IC=-0.257 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=89)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.217 (n=58)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=77)

### CANDIDATA9_BOT_CONSENSO#BTC#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.309 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=84)

- **PATRÓN** `py_entrada` > `0.52` → IC=+0.167 (n=34)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.52 (IC base=+0.028)

### CANDIDATA9_BOT_CONSENSO#ETH#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=19)

- **FILTRO** `py_entrada` > `0.29` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `py_entrada` > 0.29
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=16)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.7` → IC=+0.197 (n=9701)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.7 (IC base=+0.095)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.156 (n=2605)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `11137.3038` → IC=+0.191 (n=834)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 11137.3038 (IC base=+0.095)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.142 (n=7829)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 17.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.145 (n=9356)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 7.0 (IC base=+0.135)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.246 (n=6835)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.172 (n=5152)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.02 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `4713.235` → IC=+0.171 (n=2226)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 4713.235 (IC base=+0.135)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.216 (n=1205)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.353 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=1487)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `14609.4318` → IC=+0.216 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14609.4318 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.208 (n=1103)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.210 (n=1213)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` < `0.37` → IC=+0.268 (n=1062)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.202 (n=1556)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `12842.7063` → IC=+0.205 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12842.7063 (IC base=+0.201)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.615` → IC=+0.177 (n=258)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` > 0.615 (IC base=+0.108)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=278)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `4713.7937` → IC=+0.153 (n=223)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 4713.7937 (IC base=+0.108)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.191 (n=263)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 7.0 (IC base=+0.136)

- **PATRÓN** `py_entrada` < `0.425` → IC=+0.164 (n=536)

  - _Acción_: Kelly boost +0.82€ cuando `py_entrada` < 0.425 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `3895.7732` → IC=+0.165 (n=407)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3895.7732 (IC base=+0.136)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=2105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.139 (n=1787)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.137)

- **PATRÓN** `py_entrada` > `0.7` → IC=+0.329 (n=672)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.7 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.241 (n=907)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.236)

- **PATRÓN** `py_entrada` < `0.355` → IC=+0.297 (n=898)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.355 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.236 (n=1045)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `2387.758` → IC=+0.240 (n=889)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2387.758 (IC base=+0.236)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.128 (n=508)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 5.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.136 (n=438)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 15.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` > `0.665` → IC=+0.219 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.665 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.136 (n=580)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.02 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `1512.3969` → IC=+0.150 (n=435)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1512.3969 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `4449.086` → IC=+0.167 (n=145)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 4449.086 (IC base=+0.082)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.209 (n=476)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.193 (n=981)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 12.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.85` → IC=+0.427 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.85 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.185 (n=906)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 7.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.183 (n=478)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 7.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` < `0.345` → IC=+0.285 (n=672)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.345 (IC base=+0.182)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.187 (n=1034)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.03 (IC base=+0.182)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.186 (n=297)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.171)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.333 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.171)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.191 (n=176)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.02 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `3435.4625` → IC=+0.181 (n=70)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 3435.4625 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.139 (n=633)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 7.0 (IC base=+0.122)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.220 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.141 (n=313)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.02 (IC base=+0.122)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `9.0` → IC=-0.298 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=104)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=8065)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.201 (n=6839)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.217 (n=2879)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.335 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `3425.1488` → IC=+0.329 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3425.1488 (IC base=+0.197)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.181 (n=1950)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 17.0 (IC base=+0.170)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.183 (n=2055)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` < 0.74 (IC base=+0.170)

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

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.386 (n=103)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.331)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.356 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.331)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=2024)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.184 (n=1705)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 15.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.179 (n=1952)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.73 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.186 (n=1296)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.72 (IC base=+0.177)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.247 (n=1807)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.238 (n=1536)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.238)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.328 (n=574)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.238)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.326 (n=44)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.198 (n=1952)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.192 (n=1671)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.192 (n=1035)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.7 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.190 (n=821)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.73 (IC base=+0.189)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.446 (n=332)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.443)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.447 (n=321)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.443)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.484 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.443)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.442 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.443)

- **PATRÓN** `libro_liquidez` > `9523.4542` → IC=+0.468 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9523.4542 (IC base=+0.443)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.445 (n=144)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.443)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.440 (n=132)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.443)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.456 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.443)

- **PATRÓN** `libro_liquidez` > `11667.7741` → IC=+0.459 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11667.7741 (IC base=+0.443)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.454 (n=129)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.441)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.438 (n=143)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.459 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.441)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.440 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.441)

- **PATRÓN** `libro_liquidez` > `3939.3842` → IC=+0.454 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3939.3842 (IC base=+0.441)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.418 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.425)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.429 (n=83)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.425)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.425 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.425)

- **PATRÓN** `py_entrada` > `0.932` → IC=+0.421 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.932 (IC base=+0.425)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `hora_utc` < `12.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.233 (n=13)

- **FILTRO** `py_entrada` > `0.775` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=11)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.194 (n=23726)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 8.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.226 (n=13061)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.192)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=4886)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.168 (n=3343)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 12.0 (IC base=+0.162)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.181 (n=4350)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` > 0.71 (IC base=+0.162)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.224 (n=4192)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.250 (n=3096)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.177 (n=1778)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.165)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.181 (n=4336)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.71 (IC base=+0.165)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.232 (n=2135)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.220 (n=1628)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.265 (n=1501)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.204 (n=1466)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.199 (n=3888)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 15.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.234 (n=2623)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.192 (n=1729)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 17.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.190 (n=3191)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 12.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.243 (n=1596)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.188)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.201 (n=3552)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.124)

- **PATRÓN** `restante_min` < `4.07` → IC=+0.136 (n=3290)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` < 4.07 (IC base=+0.124)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.144 (n=3582)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.94 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.139 (n=4335)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `lag_apertura_s` < `3.41` → IC=+0.149 (n=3285)

  - _Acción_: Kelly boost +0.75€ cuando `lag_apertura_s` < 3.41 (IC base=+0.124)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.208 (n=1774)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.131)

- **PATRÓN** `restante_min` < `4.01` → IC=+0.144 (n=1629)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` < 4.01 (IC base=+0.131)

- **PATRÓN** `restante_min` > `4.89` → IC=+0.144 (n=2265)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.89 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.150 (n=2403)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 8.0 (IC base=+0.131)

- **PATRÓN** `lag_apertura_s` < `6.47` → IC=+0.145 (n=2144)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 6.47 (IC base=+0.131)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=1778)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.118)

- **PATRÓN** `restante_min` < `4.48` → IC=+0.126 (n=2193)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.48 (IC base=+0.118)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.147 (n=1802)

  - _Acción_: Kelly boost +0.73€ cuando `restante_min` > 4.95 (IC base=+0.118)

- **PATRÓN** `lag_apertura_s` < `3.03` → IC=+0.146 (n=1655)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 3.03 (IC base=+0.118)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.318 (n=607)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.289)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.379 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `1653.8347` → IC=+0.298 (n=859)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1653.8347 (IC base=+0.289)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.301 (n=265)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.277)

- **PATRÓN** `py_entrada` > `0.785` → IC=+0.327 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.785 (IC base=+0.277)

- **PATRÓN** `libro_liquidez` > `5195.0219` → IC=+0.291 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5195.0219 (IC base=+0.277)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.329 (n=284)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.291)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.291 (n=409)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.291)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.380 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `1534.2889` → IC=+0.309 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1534.2889 (IC base=+0.291)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.335 (n=77)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.328)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.357 (n=68)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.328)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.372 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.328)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.371 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.328)

- **PATRÓN** `libro_liquidez` > `763.8012` → IC=+0.366 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 763.8012 (IC base=+0.328)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.438 (n=401)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.427)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.435 (n=335)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.427)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.431 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.427)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.435 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.427)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.429 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.427)

- **PATRÓN** `libro_liquidez` > `1921.0334` → IC=+0.435 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1921.0334 (IC base=+0.427)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.439 (n=179)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.428)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.439 (n=177)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.428)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.433 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.428)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.435 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.428)

- **PATRÓN** `libro_liquidez` > `5267.3578` → IC=+0.434 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5267.3578 (IC base=+0.428)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.433 (n=176)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.428)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.444 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.428)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.429 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.428)

- **PATRÓN** `libro_liquidez` > `1841.4992` → IC=+0.450 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1841.4992 (IC base=+0.428)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` < `12.0` → IC=+0.364 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.372)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.444 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.372)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.286 (n=442)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.262)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.401 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.262)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.283 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.262)

- **PATRÓN** `libro_liquidez` > `2200.2248` → IC=+0.296 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2200.2248 (IC base=+0.262)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.286 (n=442)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.262)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.401 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.262)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.283 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.262)

- **PATRÓN** `libro_liquidez` > `2200.2248` → IC=+0.296 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2200.2248 (IC base=+0.262)

### GBM_LATE_15M
- **PATRÓN** `ibs_20min` > `0.9709` → IC=+0.231 (n=1785)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9709 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` < `0.155` → IC=+0.243 (n=1022)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.155 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.83` → IC=+0.168 (n=2049)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 5.83 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` < `0.6162` → IC=+0.252 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6162 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` > `1.0681` → IC=+0.244 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0681 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.1093` → IC=+0.202 (n=1319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1093 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` > `1.4655` → IC=+0.195 (n=3441)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4655 (IC base=+0.096)

- **PATRÓN** `ibs_20min` < `0.5798` → IC=+0.122 (n=6601)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.5798 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` < `0.1332` → IC=+0.163 (n=1929)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1332 (IC base=+0.054)

- **PATRÓN** `volumen_regimen` > `1.0558` → IC=+0.169 (n=918)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 1.0558 (IC base=+0.054)

- **PATRÓN** `volumen_pendiente_norm` > `0.1685` → IC=+0.225 (n=972)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1685 (IC base=+0.054)

- **PATRÓN** `volumen_spike_ratio` > `1.4601` → IC=+0.193 (n=3350)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 1.4601 (IC base=+0.054)

- **PATRÓN** `ballena_activa_n` < `171.0` → IC=+0.202 (n=3114)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 171.0 (IC base=+0.054)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.194 (n=403)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.005 (IC base=+0.168)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.187 (n=401)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0076 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.3282` → IC=+0.172 (n=1203)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.3282 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.192 (n=593)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 8.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.275 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.936` → IC=+0.289 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.936 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.2291` → IC=+0.213 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2291 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `2.6036` → IC=+0.158 (n=1097)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.6036 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `1.4344` → IC=+0.166 (n=1097)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.4344 (IC base=+0.168)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.185 (n=1270)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.06 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `65.0` → IC=+0.191 (n=863)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 65.0 (IC base=+0.168)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.260 (n=790)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.1954` → IC=+0.280 (n=590)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1954 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.249 (n=799)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.239 (n=894)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.0662` → IC=+0.286 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0662 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.331` → IC=+0.251 (n=918)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.331 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` < `0.0681` → IC=+0.238 (n=693)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0681 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.273 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.8725` → IC=+0.234 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8725 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `2.6424` → IC=+0.261 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6424 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.243 (n=927)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `1560.5772` → IC=+0.248 (n=789)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1560.5772 (IC base=+0.239)

- **PATRÓN** `ballena_activa_n` < `67.0` → IC=+0.235 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 67.0 (IC base=+0.239)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.237 (n=306)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.211)

- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.213 (n=305)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.1172` → IC=+0.235 (n=402)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1172 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.229 (n=955)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.9278` → IC=+0.251 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9278 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.2184` → IC=+0.213 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2184 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.921` → IC=+0.233 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.921 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` < `1.2628` → IC=+0.221 (n=914)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2628 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` > `0.8793` → IC=+0.217 (n=610)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8793 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` < `0.1644` → IC=+0.211 (n=933)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1644 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.2338` → IC=+0.220 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2338 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.4857` → IC=+0.228 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4857 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.3839` → IC=+0.216 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3839 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `10979.8664` → IC=+0.225 (n=914)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10979.8664 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.161 (n=866)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0049 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.0782` → IC=+0.170 (n=328)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.0782 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.160 (n=330)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 18.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.140 (n=340)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 5.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.319` → IC=+0.196 (n=656)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.319 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.496` → IC=+0.192 (n=170)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 11.496 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `1.1954` → IC=+0.149 (n=984)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.1954 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` > `0.6827` → IC=+0.141 (n=879)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.6827 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.1536` → IC=+0.210 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1536 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `2.3943` → IC=+0.154 (n=875)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.3943 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.41` → IC=+0.151 (n=875)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.41 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `12929.8594` → IC=+0.152 (n=656)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 12929.8594 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `218.0` → IC=+0.170 (n=265)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 218.0 (IC base=+0.141)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` < `0.0089` → IC=+0.183 (n=1020)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0089 (IC base=+0.180)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.191 (n=1160)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0059 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.181 (n=1159)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 6.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.198 (n=445)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.259 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.369` → IC=+0.250 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.369 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` < `0.1063` → IC=+0.182 (n=976)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` < 0.1063 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `1.6619` → IC=+0.185 (n=1073)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 1.6619 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.195 (n=1294)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.04 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.200 (n=857)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 50.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.217 (n=1006)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.209)

- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.212 (n=671)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0079 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.1535` → IC=+0.212 (n=443)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1535 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.236 (n=335)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.209)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.216 (n=474)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` < `0.0708` → IC=+0.246 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0708 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.688` → IC=+0.237 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.688 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.3645` → IC=+0.282 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3645 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `2.289` → IC=+0.218 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.289 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.226 (n=505)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `1881.0184` → IC=+0.224 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1881.0184 (IC base=+0.209)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.205 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.209)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.163 (n=87)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=1481)

- **PATRÓN** `dist_vwap_pct` < `0.4575` → IC=+0.339 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4575 (IC base=+0.002)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.538` → IC=+0.131 (n=423)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 5.538 (IC base=+0.002)

- **PATRÓN** `volumen_regimen` < `0.6044` → IC=+0.402 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6044 (IC base=+0.002)

- **PATRÓN** `volumen_regimen` > `1.1808` → IC=+0.336 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1808 (IC base=+0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.1585` → IC=+0.339 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1585 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` < `1.4916` → IC=+0.357 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4916 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` > `1.8203` → IC=+0.336 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8203 (IC base=+0.002)

- **PATRÓN** `ballena_activa_n` < `171.0` → IC=+0.332 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 171.0 (IC base=+0.002)

- **PATRÓN** `dist_vwap_pct` > `0.1556` → IC=+0.183 (n=137)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.1556 (IC base=-0.014)

- **PATRÓN** `volumen_regimen` < `0.8549` → IC=+0.133 (n=287)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.8549 (IC base=-0.014)

- **PATRÓN** `volumen_regimen` > `0.6123` → IC=+0.129 (n=429)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.6123 (IC base=-0.014)

- **PATRÓN** `volumen_pendiente_norm` > `0.2153` → IC=+0.216 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2153 (IC base=-0.014)

- **PATRÓN** `volumen_spike_ratio` > `1.5064` → IC=+0.167 (n=340)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.5064 (IC base=-0.014)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.125 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=214)

- **FILTRO** `ibs_20min` < `0.2381` → IC=-0.187 (n=65)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2381
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=195)

- **FILTRO** `ibs_20min` > `0.2885` → IC=-0.127 (n=1548)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2885
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=763)

- **FILTRO** `sigma_ewma_delta_pct` > `8.595` → IC=-0.194 (n=256)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.595
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=2055)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.203 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.75 (IC base=+0.042)

- **PATRÓN** `dist_vwap_pct` < `0.6239` → IC=+0.310 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6239 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` < `0.6466` → IC=+0.274 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6466 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` > `1.1487` → IC=+0.375 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1487 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` < `0.0735` → IC=+0.333 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0735 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` < `3.085` → IC=+0.288 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.085 (IC base=+0.042)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.325 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.042)

- **PATRÓN** `dist_vwap_pct` > `0.3265` → IC=+0.269 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3265 (IC base=-0.048)

- **PATRÓN** `volumen_regimen` < `1.1257` → IC=+0.177 (n=156)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 1.1257 (IC base=-0.048)

- **PATRÓN** `volumen_regimen` > `0.9228` → IC=+0.183 (n=118)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 0.9228 (IC base=-0.048)

- **PATRÓN** `volumen_pendiente_norm` < `0.1972` → IC=+0.195 (n=126)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.1972 (IC base=-0.048)

- **PATRÓN** `volumen_pendiente_norm` > `0.1481` → IC=+0.235 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1481 (IC base=-0.048)

- **PATRÓN** `volumen_spike_ratio` < `2.4196` → IC=+0.219 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4196 (IC base=-0.048)

- **PATRÓN** `volumen_spike_ratio` > `1.4755` → IC=+0.194 (n=106)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.4755 (IC base=-0.048)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.268 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 51.0 (IC base=-0.048)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6615` → IC=-0.189 (n=374)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6615
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=1126)

- **FILTRO** `ibs_20min` < `0.633` → IC=-0.156 (n=990)

  - _Acción_: SKIP cuando `ibs_20min` < 0.633
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=510)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.184 (n=283)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=1217)

- **FILTRO** `ibs_20min` > `0.7761` → IC=-0.199 (n=573)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7761
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=1720)

- **PATRÓN** `dist_vwap_pct` > `0.8898` → IC=+0.292 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8898 (IC base=-0.088)

- **PATRÓN** `dist_vwap_pct` < `0.2379` → IC=+0.288 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2379 (IC base=-0.088)

- **PATRÓN** `volumen_regimen` > `0.6107` → IC=+0.281 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6107 (IC base=-0.088)

- **PATRÓN** `volumen_pendiente_norm` > `0.0744` → IC=+0.291 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0744 (IC base=-0.088)

- **PATRÓN** `volumen_spike_ratio` > `1.8015` → IC=+0.272 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8015 (IC base=-0.088)

- **PATRÓN** `dist_vwap_pct` > `0.4844` → IC=+0.256 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4844 (IC base=-0.032)

- **PATRÓN** `dist_vwap_pct` < `0.2677` → IC=+0.231 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2677 (IC base=-0.032)

- **PATRÓN** `volumen_regimen` > `1.0828` → IC=+0.294 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0828 (IC base=-0.032)

- **PATRÓN** `volumen_pendiente_norm` < `0.1702` → IC=+0.226 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1702 (IC base=-0.032)

- **PATRÓN** `volumen_pendiente_norm` > `0.1065` → IC=+0.245 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1065 (IC base=-0.032)

- **PATRÓN** `volumen_spike_ratio` < `2.1737` → IC=+0.250 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1737 (IC base=-0.032)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.233 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=-0.032)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.170 (n=2223)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0092 (IC base=+0.084)

- **PATRÓN** `ibs_20min` > `0.4525` → IC=+0.172 (n=5945)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.4525 (IC base=+0.084)

- **PATRÓN** `dist_vwap_pct` > `0.7322` → IC=+0.273 (n=607)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7322 (IC base=+0.084)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.468` → IC=+0.138 (n=3138)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 3.468 (IC base=+0.084)

- **PATRÓN** `volumen_regimen` > `0.6753` → IC=+0.228 (n=1987)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6753 (IC base=+0.084)

- **PATRÓN** `volumen_pendiente_norm` > `0.2481` → IC=+0.255 (n=693)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2481 (IC base=+0.084)

- **PATRÓN** `volumen_spike_ratio` < `1.4787` → IC=+0.234 (n=1165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4787 (IC base=+0.084)

- **PATRÓN** `volumen_spike_ratio` > `2.7844` → IC=+0.234 (n=1164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7844 (IC base=+0.084)

- **PATRÓN** `ballena_activa_n` < `106.0` → IC=+0.281 (n=2972)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 106.0 (IC base=+0.084)

- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.139 (n=2284)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` > 0.0085 (IC base=+0.063)

- **PATRÓN** `ibs_20min` < `0.5635` → IC=+0.145 (n=6027)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.5635 (IC base=+0.063)

- **PATRÓN** `dist_vwap_pct` > `0.6789` → IC=+0.246 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6789 (IC base=+0.063)

- **PATRÓN** `dist_vwap_pct` < `0.162` → IC=+0.233 (n=1652)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.162 (IC base=+0.063)

- **PATRÓN** `volumen_regimen` > `1.1961` → IC=+0.261 (n=588)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1961 (IC base=+0.063)

- **PATRÓN** `volumen_pendiente_norm` > `0.2505` → IC=+0.326 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2505 (IC base=+0.063)

- **PATRÓN** `volumen_spike_ratio` > `2.36` → IC=+0.263 (n=1029)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.36 (IC base=+0.063)

- **PATRÓN** `ballena_activa_n` < `77.0` → IC=+0.258 (n=2113)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 77.0 (IC base=+0.063)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.3367` → IC=-0.128 (n=597)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3367
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=1215)

- **FILTRO** `sigma_ewma_delta_pct` > `2.53` → IC=-0.156 (n=443)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.53
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=1008)

- **PATRÓN** `ibs_20min` > `0.8469` → IC=+0.249 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8469 (IC base=+0.035)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.963` → IC=+0.160 (n=468)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 4.963 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` > `0.216` → IC=+0.305 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.216 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` < `1.8477` → IC=+0.198 (n=279)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.8477 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` > `1.5631` → IC=+0.202 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5631 (IC base=+0.035)

- **PATRÓN** `ballena_activa_n` < `80.0` → IC=+0.232 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 80.0 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` < `0.1791` → IC=+0.470 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1791 (IC base=-0.024)

- **PATRÓN** `volumen_spike_ratio` < `1.4617` → IC=+0.444 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4617 (IC base=-0.024)

- **PATRÓN** `volumen_spike_ratio` > `2.3568` → IC=+0.444 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3568 (IC base=-0.024)

- **PATRÓN** `ballena_activa_n` < `65.0` → IC=+0.462 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 65.0 (IC base=-0.024)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.8399` → IC=-0.158 (n=512)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8399
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=1539)

- **PATRÓN** `dist_vwap_pct` > `0.3154` → IC=+0.127 (n=210)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` > 0.3154 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` > `0.6687` → IC=+0.122 (n=506)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` > 0.6687 (IC base=+0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.2218` → IC=+0.187 (n=97)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2218 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` < `1.4206` → IC=+0.165 (n=183)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.4206 (IC base=+0.006)

- **PATRÓN** `ballena_activa_n` < `271.0` → IC=+0.168 (n=236)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 271.0 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` > `1.1336` → IC=+0.241 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1336 (IC base=-0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.346 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.275 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` < `1.7482` → IC=+0.213 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7482 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` > `2.1128` → IC=+0.224 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1128 (IC base=-0.006)

- **PATRÓN** `ballena_activa_n` < `518.0` → IC=+0.207 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 518.0 (IC base=-0.006)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.281 (n=705)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0074 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.099` → IC=+0.244 (n=353)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.099 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.243 (n=531)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.254 (n=401)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` > `0.7148` → IC=+0.270 (n=944)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7148 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.607` → IC=+0.293 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.607 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` < `0.1111` → IC=+0.254 (n=875)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1111 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `2.3625` → IC=+0.240 (n=648)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3625 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `3.1142` → IC=+0.251 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.1142 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.260 (n=1168)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.240)

- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.298 (n=834)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0057 (IC base=+0.279)

- **PATRÓN** `drift_60min` |x|≤ `0.1655` → IC=+0.281 (n=367)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1655 (IC base=+0.279)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.314 (n=283)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.279)

- **PATRÓN** `ibs_20min` < `0.3433` → IC=+0.288 (n=835)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3433 (IC base=+0.279)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.885` → IC=+0.309 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.885 (IC base=+0.279)

- **PATRÓN** `volumen_pendiente_norm` > `0.3445` → IC=+0.327 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3445 (IC base=+0.279)

- **PATRÓN** `volumen_spike_ratio` < `3.353` → IC=+0.274 (n=742)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.353 (IC base=+0.279)

- **PATRÓN** `volumen_spike_ratio` > `2.2087` → IC=+0.288 (n=494)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2087 (IC base=+0.279)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.295 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `1872.8576` → IC=+0.300 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1872.8576 (IC base=+0.279)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.278 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 29.0 (IC base=+0.279)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.142 (n=252)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=891)

- **FILTRO** `ibs_20min` < `0.2163` → IC=-0.207 (n=285)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2163
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=858)

- **FILTRO** `ibs_20min` > `0.8343` → IC=-0.178 (n=396)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8343
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=1189)

- **PATRÓN** `ibs_20min` > `0.7996` → IC=+0.124 (n=389)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` > 0.7996 (IC base=-0.028)

- **PATRÓN** `dist_vwap_pct` > `0.4826` → IC=+0.202 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4826 (IC base=-0.028)

- **PATRÓN** `volumen_regimen` < `0.9122` → IC=+0.187 (n=193)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.9122 (IC base=-0.028)

- **PATRÓN** `volumen_regimen` > `0.6044` → IC=+0.167 (n=196)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.6044 (IC base=-0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.2746` → IC=+0.308 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2746 (IC base=-0.028)

- **PATRÓN** `volumen_spike_ratio` < `1.5078` → IC=+0.233 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5078 (IC base=-0.028)

- **PATRÓN** `volumen_spike_ratio` > `1.4` → IC=+0.210 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4 (IC base=-0.028)

- **PATRÓN** `ballena_activa_n` < `185.0` → IC=+0.223 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 185.0 (IC base=-0.028)

- **PATRÓN** `dist_vwap_pct` > `0.1077` → IC=+0.155 (n=56)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1077 (IC base=-0.036)

- **PATRÓN** `volumen_regimen` > `0.6808` → IC=+0.129 (n=138)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.6808 (IC base=-0.036)

- **PATRÓN** `volumen_pendiente_norm` > `0.0595` → IC=+0.333 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0595 (IC base=-0.036)

- **PATRÓN** `volumen_spike_ratio` > `1.411` → IC=+0.230 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.411 (IC base=-0.036)

- **PATRÓN** `ballena_activa_n` < `162.0` → IC=+0.220 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 162.0 (IC base=-0.036)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.6522` → IC=-0.199 (n=726)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6522
  - _Potencial_: sin este filtro IC_bueno=+0.244 (n=728)

- **FILTRO** `ibs_20min` > `0.7255` → IC=-0.233 (n=388)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7255
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=1167)

- **FILTRO** `sigma_ewma_delta_pct` > `4.714` → IC=-0.158 (n=378)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.714
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=1177)

- **PATRÓN** `ibs_20min` > `0.6522` → IC=+0.244 (n=728)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6522 (IC base=+0.023)

- **PATRÓN** `dist_vwap_pct` > `0.1881` → IC=+0.305 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1881 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` < `0.86` → IC=+0.279 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.86 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` > `0.7156` → IC=+0.265 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7156 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` < `0.105` → IC=+0.269 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.105 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` > `0.274` → IC=+0.279 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.274 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` < `1.443` → IC=+0.307 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.443 (IC base=+0.023)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.314 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.023)

- **PATRÓN** `ibs_20min` < `0.42` → IC=+0.122 (n=778)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.42 (IC base=-0.001)

- **PATRÓN** `dist_vwap_pct` > `0.5417` → IC=+0.183 (n=58)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.5417 (IC base=-0.001)

- **PATRÓN** `dist_vwap_pct` < `0.1702` → IC=+0.199 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1702 (IC base=-0.001)

- **PATRÓN** `volumen_regimen` < `1.0883` → IC=+0.207 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0883 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` < `0.1003` → IC=+0.196 (n=238)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.1003 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2188` → IC=+0.227 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2188 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` < `2.5615` → IC=+0.215 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5615 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` > `1.5131` → IC=+0.191 (n=247)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 1.5131 (IC base=-0.001)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.227 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=-0.001)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0144` → IC=+0.327 (n=633)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0144 (IC base=+0.263)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.276 (n=454)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.263)

- **PATRÓN** `ibs_20min` > `0.9014` → IC=+0.332 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9014 (IC base=+0.263)

- **PATRÓN** `dist_vwap_pct` > `0.1772` → IC=+0.311 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1772 (IC base=+0.263)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.371` → IC=+0.288 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.371 (IC base=+0.263)

- **PATRÓN** `volumen_regimen` > `0.8513` → IC=+0.291 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8513 (IC base=+0.263)

- **PATRÓN** `volumen_pendiente_norm` < `0.11` → IC=+0.270 (n=827)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.11 (IC base=+0.263)

- **PATRÓN** `volumen_pendiente_norm` > `0.2391` → IC=+0.292 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2391 (IC base=+0.263)

- **PATRÓN** `volumen_spike_ratio` < `1.5517` → IC=+0.276 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5517 (IC base=+0.263)

- **PATRÓN** `volumen_spike_ratio` > `2.213` → IC=+0.269 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.213 (IC base=+0.263)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.267 (n=1009)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.263)

- **PATRÓN** `libro_liquidez` > `2441.3379` → IC=+0.270 (n=849)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2441.3379 (IC base=+0.263)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.275 (n=344)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.271)

- **PATRÓN** `sigma_h` > `0.0138` → IC=+0.299 (n=688)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0138 (IC base=+0.271)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.285 (n=514)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.271)

- **PATRÓN** `ibs_20min` < `0.38` → IC=+0.303 (n=1032)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.38 (IC base=+0.271)

- **PATRÓN** `dist_vwap_pct` > `0.5341` → IC=+0.288 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5341 (IC base=+0.271)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.383` → IC=+0.282 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.383 (IC base=+0.271)

- **PATRÓN** `volumen_regimen` < `0.6351` → IC=+0.272 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6351 (IC base=+0.271)

- **PATRÓN** `volumen_regimen` > `1.2432` → IC=+0.312 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2432 (IC base=+0.271)

- **PATRÓN** `volumen_pendiente_norm` > `0.2921` → IC=+0.348 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2921 (IC base=+0.271)

- **PATRÓN** `volumen_spike_ratio` < `2.559` → IC=+0.268 (n=874)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.559 (IC base=+0.271)

- **PATRÓN** `volumen_spike_ratio` > `1.4425` → IC=+0.264 (n=874)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4425 (IC base=+0.271)

- **PATRÓN** `libro_liquidez` > `2322.8611` → IC=+0.275 (n=922)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2322.8611 (IC base=+0.271)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.171 (n=1786)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0048 (IC base=+0.169)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.204 (n=1787)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.3416` → IC=+0.176 (n=4710)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.3416 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.179 (n=5577)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.6946` → IC=+0.231 (n=4781)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6946 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.1646` → IC=+0.198 (n=2339)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1646 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.216` → IC=+0.252 (n=1098)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.216 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `1.2145` → IC=+0.162 (n=3587)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2145 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` > `0.6228` → IC=+0.160 (n=3587)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6228 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.1064` → IC=+0.189 (n=2080)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.1064 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `2.2998` → IC=+0.169 (n=4455)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 2.2998 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `3861.5494` → IC=+0.174 (n=1784)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 3861.5494 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `130.0` → IC=+0.187 (n=4260)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 130.0 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.183 (n=3438)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0064 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.0794` → IC=+0.203 (n=1717)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0794 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.198 (n=2487)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 15.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` < `0.4561` → IC=+0.224 (n=5147)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4561 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.742` → IC=+0.190 (n=2138)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 3.742 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `1.18` → IC=+0.153 (n=3781)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.18 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` > `0.6237` → IC=+0.152 (n=3780)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6237 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.2907` → IC=+0.232 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2907 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.8671` → IC=+0.168 (n=3003)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.8671 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.6167` → IC=+0.172 (n=1501)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.6167 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `134.0` → IC=+0.168 (n=4107)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 134.0 (IC base=+0.169)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.226 (n=301)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.191)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.209 (n=410)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.191)

- **PATRÓN** `drift_60min` |x|≤ `0.3232` → IC=+0.211 (n=900)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3232 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.224 (n=397)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.304 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.966` → IC=+0.315 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.966 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` > `0.2255` → IC=+0.247 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2255 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` < `2.5428` → IC=+0.187 (n=809)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 2.5428 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` > `1.5477` → IC=+0.187 (n=723)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.5477 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.214 (n=799)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.191)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.208 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 58.0 (IC base=+0.191)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.239 (n=557)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.236)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.258 (n=567)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.1803` → IC=+0.297 (n=422)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1803 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.245 (n=575)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.246 (n=668)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` < `0.1143` → IC=+0.271 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1143 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.926` → IC=+0.248 (n=685)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.926 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` < `0.0683` → IC=+0.233 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0683 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.2316` → IC=+0.258 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2316 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` < `1.8606` → IC=+0.261 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8606 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.239 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `1563.22` → IC=+0.251 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1563.22 (IC base=+0.236)

- **PATRÓN** `ballena_activa_n` < `74.0` → IC=+0.229 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 74.0 (IC base=+0.236)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.251 (n=259)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.3668` → IC=+0.175 (n=777)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.3668 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.192 (n=702)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 8.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `0.4506` → IC=+0.221 (n=778)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4506 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.2253` → IC=+0.218 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2253 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.697` → IC=+0.237 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.697 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `1.2719` → IC=+0.174 (n=777)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 1.2719 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.2392` → IC=+0.202 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2392 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `1.4035` → IC=+0.209 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4035 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `11275.7432` → IC=+0.187 (n=694)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 11275.7432 (IC base=+0.164)

- **PATRÓN** `ballena_activa_n` < `416.0` → IC=+0.161 (n=614)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 416.0 (IC base=+0.164)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.178 (n=785)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.005 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.2906` → IC=+0.170 (n=892)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.2906 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.168 (n=816)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 7.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.5135` → IC=+0.192 (n=892)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.5135 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.123` → IC=+0.224 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.123 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `1.1939` → IC=+0.166 (n=892)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1939 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.1578` → IC=+0.205 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1578 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.4003` → IC=+0.162 (n=783)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.4003 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.4073` → IC=+0.152 (n=783)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.4073 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `238.0` → IC=+0.165 (n=234)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 238.0 (IC base=+0.151)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.006` → IC=+0.200 (n=867)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.1994` → IC=+0.202 (n=578)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1994 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.220 (n=298)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.190 (n=405)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 7.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.293 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.56` → IC=+0.284 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.56 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` < `0.2187` → IC=+0.184 (n=819)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.2187 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.1338` → IC=+0.194 (n=331)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1338 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` < `1.6649` → IC=+0.191 (n=267)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.6649 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `3.6425` → IC=+0.203 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.6425 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.206 (n=952)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.190)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.229 (n=735)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.218)

- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.222 (n=490)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0079 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.0898` → IC=+0.246 (n=246)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0898 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.256 (n=362)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` < `0.36` → IC=+0.249 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.36 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.677` → IC=+0.274 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.677 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.3597` → IC=+0.285 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3597 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` < `1.8317` → IC=+0.209 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8317 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `2.2419` → IC=+0.223 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2419 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `1881.693` → IC=+0.233 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1881.693 (IC base=+0.218)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.212 (n=279)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0035 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.4335` → IC=+0.168 (n=835)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.4335 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.170 (n=837)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 6.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` > `0.4158` → IC=+0.204 (n=834)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4158 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.1335` → IC=+0.192 (n=549)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1335 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.328` → IC=+0.252 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.328 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `0.8633` → IC=+0.162 (n=557)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8633 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` > `1.2001` → IC=+0.179 (n=278)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 1.2001 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.2902` → IC=+0.241 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2902 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `1.4124` → IC=+0.172 (n=272)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.4124 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `2.5584` → IC=+0.186 (n=272)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.5584 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `7649.1944` → IC=+0.195 (n=556)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 7649.1944 (IC base=+0.156)

- **PATRÓN** `ballena_activa_n` < `126.0` → IC=+0.171 (n=514)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 126.0 (IC base=+0.156)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.156 (n=794)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0061 (IC base=+0.122)

- **PATRÓN** `drift_60min` |x|≤ `0.3776` → IC=+0.140 (n=899)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.3776 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.178 (n=302)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 18.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.5951` → IC=+0.170 (n=899)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.5951 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.142` → IC=+0.183 (n=178)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 12.142 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `0.8631` → IC=+0.131 (n=600)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.8631 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.6129` → IC=+0.128 (n=900)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.6129 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2871` → IC=+0.187 (n=129)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2871 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.7906` → IC=+0.124 (n=524)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.7906 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `11661.2722` → IC=+0.149 (n=300)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 11661.2722 (IC base=+0.122)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.161 (n=461)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0099 (IC base=+0.112)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.131 (n=1041)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.112)

- **PATRÓN** `ibs_20min` > `0.5111` → IC=+0.196 (n=1014)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.5111 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` > `1.0291` → IC=+0.225 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0291 (IC base=+0.112)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.378` → IC=+0.257 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.378 (IC base=+0.112)

- **PATRÓN** `volumen_regimen` < `1.2184` → IC=+0.121 (n=1015)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.2184 (IC base=+0.112)

- **PATRÓN** `volumen_spike_ratio` < `2.1437` → IC=+0.123 (n=858)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.1437 (IC base=+0.112)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.124 (n=1030)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.112)

- **PATRÓN** `libro_liquidez` > `2920.7709` → IC=+0.199 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2920.7709 (IC base=+0.112)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.139 (n=719)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 49.0 (IC base=+0.112)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.144 (n=324)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0054 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.179 (n=447)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.5283` → IC=+0.205 (n=972)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5283 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` < `0.191` → IC=+0.134 (n=897)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.191 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.294` → IC=+0.147 (n=205)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 7.294 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` < `1.0367` → IC=+0.127 (n=855)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.0367 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` > `0.2724` → IC=+0.170 (n=113)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2724 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` > `2.1312` → IC=+0.132 (n=378)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.1312 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `3139.7348` → IC=+0.150 (n=324)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3139.7348 (IC base=+0.114)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0177` → IC=+0.211 (n=642)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0177 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.1655` → IC=+0.225 (n=424)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1655 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.206 (n=997)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.202 (n=444)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `0.72` → IC=+0.256 (n=861)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.72 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` > `0.1718` → IC=+0.224 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1718 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.339` → IC=+0.239 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.339 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` < `1.1991` → IC=+0.201 (n=963)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1991 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `0.8467` → IC=+0.227 (n=642)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8467 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2393` → IC=+0.260 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2393 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `2.199` → IC=+0.218 (n=811)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.199 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `1.8148` → IC=+0.208 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8148 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.201 (n=1006)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.200)

- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.243 (n=340)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0074 (IC base=+0.202)

- **PATRÓN** `sigma_h` > `0.0159` → IC=+0.207 (n=680)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0159 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.0901` → IC=+0.216 (n=340)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0901 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.210 (n=511)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.206 (n=1065)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` < `0.425` → IC=+0.241 (n=1021)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.425 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.938` → IC=+0.240 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.938 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` > `0.6258` → IC=+0.217 (n=1020)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6258 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.307 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` < `2.2351` → IC=+0.192 (n=780)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 2.2351 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` > `1.4597` → IC=+0.189 (n=886)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 1.4597 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `2535.8754` → IC=+0.211 (n=680)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2535.8754 (IC base=+0.202)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.153 (n=563)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0073 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.159 (n=1155)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 8.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` > `0.4` → IC=+0.163 (n=1241)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.4 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `0.805` → IC=+0.193 (n=164)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.805 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.676` → IC=+0.171 (n=551)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 3.676 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.8605` → IC=+0.156 (n=701)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8605 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.1659` → IC=+0.165 (n=338)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.1659 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `1.4352` → IC=+0.141 (n=394)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4352 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.8216` → IC=+0.148 (n=786)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.8216 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.140 (n=1360)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.02 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `7829.088` → IC=+0.170 (n=562)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 7829.088 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.163 (n=357)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 20.0 (IC base=+0.134)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.132 (n=427)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0038 (IC base=+0.103)

- **PATRÓN** `ibs_20min` < `0.308` → IC=+0.160 (n=854)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.308 (IC base=+0.103)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.807` → IC=+0.135 (n=510)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 3.807 (IC base=+0.103)

- **PATRÓN** `volumen_pendiente_norm` > `0.1666` → IC=+0.145 (n=325)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.1666 (IC base=+0.103)

- **PATRÓN** `volumen_spike_ratio` < `2.221` → IC=+0.127 (n=1069)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 2.221 (IC base=+0.103)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.141 (n=377)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 20.0 (IC base=+0.103)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` > `0.0038` → IC=+0.139 (n=178)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` > 0.0038 (IC base=+0.106)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.159 (n=250)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 10.0 (IC base=+0.106)

- **PATRÓN** `ibs_20min` > `0.9018` → IC=+0.185 (n=122)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.9018 (IC base=+0.106)

- **PATRÓN** `dist_vwap_pct` > `0.3374` → IC=+0.194 (n=83)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.3374 (IC base=+0.106)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.137` → IC=+0.185 (n=122)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 3.137 (IC base=+0.106)

- **PATRÓN** `volumen_regimen` < `0.6933` → IC=+0.167 (n=118)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.6933 (IC base=+0.106)

- **PATRÓN** `volumen_pendiente_norm` > `0.2933` → IC=+0.167 (n=40)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2933 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `10387.6961` → IC=+0.151 (n=267)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 10387.6961 (IC base=+0.106)

- **PATRÓN** `ballena_activa_n` < `146.0` → IC=+0.155 (n=82)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 146.0 (IC base=+0.106)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.197 (n=143)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0027 (IC base=+0.109)

- **PATRÓN** `drift_60min` |x|≤ `0.2764` → IC=+0.134 (n=375)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.2764 (IC base=+0.109)

- **PATRÓN** `ibs_20min` < `0.6193` → IC=+0.166 (n=375)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.6193 (IC base=+0.109)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.021` → IC=+0.156 (n=88)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 9.021 (IC base=+0.109)

- **PATRÓN** `volumen_regimen` > `0.7034` → IC=+0.129 (n=381)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 0.7034 (IC base=+0.109)

- **PATRÓN** `volumen_pendiente_norm` > `0.1546` → IC=+0.207 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1546 (IC base=+0.109)

- **PATRÓN** `volumen_spike_ratio` < `2.0634` → IC=+0.137 (n=367)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.0634 (IC base=+0.109)

- **PATRÓN** `ballena_activa_n` < `155.0` → IC=+0.159 (n=133)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 155.0 (IC base=+0.109)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.234 (n=167)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.201)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.229 (n=127)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.244 (n=264)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` > `0.2663` → IC=+0.243 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2663 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `0.9619` → IC=+0.250 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9619 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.93` → IC=+0.247 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.93 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` < `0.6827` → IC=+0.228 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6827 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` > `1.1605` → IC=+0.236 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1605 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.2451` → IC=+0.323 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2451 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` < `1.3686` → IC=+0.209 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3686 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` > `2.0296` → IC=+0.266 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.0296 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `12519.8254` → IC=+0.236 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12519.8254 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.0998` → IC=+0.164 (n=108)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.0998 (IC base=+0.084)

- **PATRÓN** `ibs_20min` < `0.3132` → IC=+0.141 (n=215)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.3132 (IC base=+0.084)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.016` → IC=+0.133 (n=115)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 4.016 (IC base=+0.084)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` < `0.7368` → IC=-0.138 (n=114)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7368
  - _Potencial_: sin este filtro IC_bueno=+0.151 (n=236)

- **FILTRO** `dist_vwap_pct` > `0.3645` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3645
  - _Potencial_: sin este filtro IC_bueno=+0.102 (n=269)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.177 (n=97)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.057)

- **PATRÓN** `ibs_20min` > `0.8966` → IC=+0.206 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8966 (IC base=+0.057)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.239` → IC=+0.129 (n=114)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 5.239 (IC base=+0.057)

- **PATRÓN** `libro_liquidez` > `2982.5482` → IC=+0.178 (n=88)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 2982.5482 (IC base=+0.057)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.151 (n=84)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 16.0 (IC base=+0.077)

- **PATRÓN** `ibs_20min` < `0.4481` → IC=+0.158 (n=217)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.4481 (IC base=+0.077)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.589` → IC=+0.182 (n=42)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 8.589 (IC base=+0.077)

- **PATRÓN** `volumen_regimen` < `0.7387` → IC=+0.143 (n=96)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.7387 (IC base=+0.077)

- **PATRÓN** `volumen_pendiente_norm` < `0.099` → IC=+0.124 (n=192)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.099 (IC base=+0.077)

- **PATRÓN** `volumen_spike_ratio` < `2.4885` → IC=+0.136 (n=196)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.4885 (IC base=+0.077)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.154 (n=160)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 48.0 (IC base=+0.077)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0226` → IC=+0.146 (n=142)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0226 (IC base=+0.134)

- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.174 (n=142)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0061 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.31` → IC=+0.161 (n=125)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.31 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.186 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 16.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.136 (n=53)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 6.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` > `0.4` → IC=+0.162 (n=143)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.4 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `0.2912` → IC=+0.149 (n=55)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.2912 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` < `0.6865` → IC=+0.142 (n=174)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.6865 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.317` → IC=+0.169 (n=122)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` < 3.317 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.9833` → IC=+0.138 (n=125)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.9833 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` > `0.6571` → IC=+0.151 (n=127)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6571 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` < `0.2672` → IC=+0.159 (n=136)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` < 0.2672 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `1.899` → IC=+0.179 (n=79)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.899 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.4996` → IC=+0.142 (n=118)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.4996 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.177 (n=97)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.01 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.208 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=+0.134)

- **PATRÓN** `sigma_h` > `0.0152` → IC=+0.213 (n=99)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0152 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.141 (n=51)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.141 (n=104)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 10.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.129 (n=149)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.6 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.129 (n=68)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` > 0.5 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `0.9736` → IC=+0.350 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9736 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.507` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.507 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` > `0.6197` → IC=+0.149 (n=149)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.6197 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2451` → IC=+0.242 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2451 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `1.5677` → IC=+0.138 (n=136)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.5677 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2567.2585` → IC=+0.143 (n=68)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2567.2585 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.158 (n=112)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 16.0 (IC base=+0.125)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0087` → IC=+0.194 (n=3046)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0087 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.176 (n=7011)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.4749` → IC=+0.213 (n=6718)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4749 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` > `0.9142` → IC=+0.200 (n=895)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9142 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.559` → IC=+0.225 (n=3271)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.559 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` < `0.8828` → IC=+0.161 (n=3046)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8828 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.169` → IC=+0.188 (n=1835)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.169 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` > `1.8707` → IC=+0.175 (n=4243)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.8707 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `3820.3005` → IC=+0.171 (n=2240)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 3820.3005 (IC base=+0.165)

- **PATRÓN** `ballena_activa_n` < `101.0` → IC=+0.194 (n=4710)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 101.0 (IC base=+0.165)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.201 (n=2704)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.4821` → IC=+0.186 (n=6143)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.4821 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.199 (n=2347)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.186 (n=2841)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 7.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` < `0.5597` → IC=+0.237 (n=6142)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5597 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` < `0.2336` → IC=+0.167 (n=3887)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.2336 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.772` → IC=+0.208 (n=900)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.772 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `1.0549` → IC=+0.157 (n=3739)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.0549 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` > `1.198` → IC=+0.162 (n=1417)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 1.198 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.2359` → IC=+0.249 (n=1052)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2359 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` < `1.5742` → IC=+0.181 (n=2387)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.5742 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.2819` → IC=+0.190 (n=2458)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.2819 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `133.0` → IC=+0.178 (n=5018)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 133.0 (IC base=+0.183)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.229 (n=375)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.197)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.234 (n=510)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.3229` → IC=+0.197 (n=1120)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.3229 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.215 (n=749)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.331 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.728` → IC=+0.331 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.728 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.2267` → IC=+0.239 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2267 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` < `1.5561` → IC=+0.199 (n=456)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.5561 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` > `2.5418` → IC=+0.192 (n=345)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.5418 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.217 (n=1172)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.197)

- **PATRÓN** `ballena_activa_n` < `81.0` → IC=+0.238 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 81.0 (IC base=+0.197)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.262 (n=770)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.259)

- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.273 (n=875)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0045 (IC base=+0.259)

- **PATRÓN** `drift_60min` |x|≤ `0.2076` → IC=+0.287 (n=584)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2076 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.272 (n=789)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.259)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.261 (n=805)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.259)

- **PATRÓN** `ibs_20min` < `0.2067` → IC=+0.299 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2067 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.611` → IC=+0.270 (n=872)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.611 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` > `0.2258` → IC=+0.311 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2258 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` > `2.6706` → IC=+0.288 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6706 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.265 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1566.6196` → IC=+0.269 (n=782)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1566.6196 (IC base=+0.259)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.260 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 71.0 (IC base=+0.259)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.194 (n=361)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0028 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.1153` → IC=+0.158 (n=471)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1153 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=1117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.695` → IC=+0.241 (n=713)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.695 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.3461` → IC=+0.202 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3461 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.866` → IC=+0.171 (n=247)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 9.866 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.34` → IC=+0.153 (n=951)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 4.34 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.2804` → IC=+0.159 (n=1069)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2804 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.155` → IC=+0.186 (n=294)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.155 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.4203` → IC=+0.160 (n=1017)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.4203 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.7574` → IC=+0.160 (n=678)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.7574 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `10708.3557` → IC=+0.174 (n=955)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 10708.3557 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `503.0` → IC=+0.163 (n=945)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 503.0 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.176 (n=846)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.005 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.3275` → IC=+0.173 (n=958)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.3275 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.172 (n=321)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 18.0 (IC base=+0.159)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.161 (n=686)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 12.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` < `0.6443` → IC=+0.207 (n=958)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6443 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.693` → IC=+0.203 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.693 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` < `1.1847` → IC=+0.169 (n=958)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1847 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` > `0.1489` → IC=+0.233 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1489 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` < `2.38` → IC=+0.172 (n=861)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 2.38 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` > `2.0828` → IC=+0.173 (n=390)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.0828 (IC base=+0.159)

- **PATRÓN** `ballena_activa_n` < `322.0` → IC=+0.173 (n=338)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 322.0 (IC base=+0.159)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.006` → IC=+0.227 (n=1031)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.222 (n=1082)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.231 (n=508)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` > `0.6739` → IC=+0.256 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6739 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.84` → IC=+0.313 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.84 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` < `0.2179` → IC=+0.222 (n=979)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2179 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `1.6898` → IC=+0.222 (n=955)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6898 (IC base=+0.216)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.233 (n=1145)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.216)

- **PATRÓN** `ballena_activa_n` < `64.0` → IC=+0.246 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 64.0 (IC base=+0.216)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.246 (n=340)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.226)

- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.234 (n=679)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0078 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.247 (n=385)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.237 (n=378)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` < `0.3889` → IC=+0.265 (n=897)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3889 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.661` → IC=+0.280 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.661 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.3579` → IC=+0.300 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3579 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `1.7875` → IC=+0.220 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7875 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `2.2483` → IC=+0.221 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2483 (IC base=+0.226)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.241 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `1884.0848` → IC=+0.228 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1884.0848 (IC base=+0.226)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.222 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 25.0 (IC base=+0.226)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.171 (n=500)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0039 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.149 (n=1183)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.7132` → IC=+0.236 (n=755)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7132 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.7586` → IC=+0.190 (n=227)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.7586 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.371` → IC=+0.169 (n=496)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 4.371 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.8812` → IC=+0.160 (n=756)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8812 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2744` → IC=+0.229 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2744 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.7416` → IC=+0.163 (n=724)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.7416 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.137 (n=1229)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `9055.4459` → IC=+0.234 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9055.4459 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `171.0` → IC=+0.143 (n=885)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 171.0 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.162 (n=599)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0052 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.4319` → IC=+0.146 (n=898)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.4319 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.156 (n=344)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.157 (n=403)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.6898` → IC=+0.178 (n=898)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.6898 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` < `0.2016` → IC=+0.131 (n=833)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.2016 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.137` → IC=+0.184 (n=134)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 11.137 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.8536` → IC=+0.134 (n=599)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.8536 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` > `1.1685` → IC=+0.149 (n=300)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 1.1685 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2739` → IC=+0.257 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2739 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `2.1503` → IC=+0.158 (n=378)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.1503 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `11175.6364` → IC=+0.169 (n=300)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 11175.6364 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `179.0` → IC=+0.132 (n=728)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 179.0 (IC base=+0.129)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.160 (n=451)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.091)

- **PATRÓN** `ibs_20min` > `0.4565` → IC=+0.173 (n=1181)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.4565 (IC base=+0.091)

- **PATRÓN** `dist_vwap_pct` > `1.0154` → IC=+0.176 (n=208)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 1.0154 (IC base=+0.091)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.364` → IC=+0.215 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.364 (IC base=+0.091)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.123 (n=813)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.01 (IC base=+0.091)

- **PATRÓN** `libro_liquidez` > `2947.9426` → IC=+0.245 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2947.9426 (IC base=+0.091)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.200 (n=365)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.122)

- **PATRÓN** `drift_60min` |x|≤ `0.1259` → IC=+0.169 (n=364)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1259 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.158 (n=516)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 15.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.6154` → IC=+0.213 (n=1093)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6154 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` < `0.4678` → IC=+0.142 (n=1068)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.4678 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.31` → IC=+0.128 (n=1051)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 3.31 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `0.7144` → IC=+0.153 (n=480)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.7144 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2176` → IC=+0.185 (n=163)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2176 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.577` → IC=+0.155 (n=412)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.577 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.130 (n=1194)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.03 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2976.88` → IC=+0.159 (n=364)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2976.88 (IC base=+0.122)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0239` → IC=+0.218 (n=538)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0239 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.213 (n=1237)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.205 (n=1057)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.308 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `0.1751` → IC=+0.242 (n=676)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1751 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.539` → IC=+0.240 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.539 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` < `1.2371` → IC=+0.207 (n=1186)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2371 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` > `0.6229` → IC=+0.210 (n=1186)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6229 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.2361` → IC=+0.229 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2361 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `2.6001` → IC=+0.232 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6001 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.212 (n=1227)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.206)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.247 (n=436)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.202)

- **PATRÓN** `sigma_h` > `0.0251` → IC=+0.230 (n=435)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0251 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.206 (n=1221)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.206 (n=1377)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.254 (n=1305)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.4998` → IC=+0.202 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4998 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` < `0.2701` → IC=+0.205 (n=1217)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2701 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.952` → IC=+0.265 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.952 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` > `1.2318` → IC=+0.239 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2318 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` > `0.2872` → IC=+0.265 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2872 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` < `2.2213` → IC=+0.192 (n=992)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 2.2213 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` > `1.4437` → IC=+0.199 (n=1127)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4437 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.210 (n=973)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `2545.8702` → IC=+0.205 (n=869)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2545.8702 (IC base=+0.202)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.183 (n=1040)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 37.0 (IC base=+0.202)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.142 (n=2308)

- **PATRÓN** `sigma_h` < `0.0095` → IC=+0.146 (n=1837)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0095 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.5376` → IC=+0.138 (n=2086)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.5376 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.159 (n=713)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 18.0 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.136 (n=701)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 4.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` > `0.9295` → IC=+0.199 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9295 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` > `0.1866` → IC=+0.127 (n=719)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` > 0.1866 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.22` → IC=+0.149 (n=334)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 10.22 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.1728` → IC=+0.150 (n=573)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.1728 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `1.4515` → IC=+0.150 (n=689)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4515 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `1.8824` → IC=+0.142 (n=1376)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.8824 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.131 (n=1397)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `8897.0886` → IC=+0.152 (n=946)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 8897.0886 (IC base=+0.130)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.203 (n=583)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.4826` → IC=+0.163 (n=1743)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.4826 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=649)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.158 (n=659)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.1843` → IC=+0.155 (n=767)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.1843 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.7013` → IC=+0.150 (n=287)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.7013 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.241` → IC=+0.149 (n=1723)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 6.241 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.1041` → IC=+0.148 (n=1454)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.1041 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.0715` → IC=+0.155 (n=818)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.0715 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.5638` → IC=+0.145 (n=1725)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.5638 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.8093` → IC=+0.153 (n=1150)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.8093 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=2308)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `12052.6582` → IC=+0.159 (n=790)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 12052.6582 (IC base=+0.140)

### GBM_LATE_5M#BTC#5min
- **FILTRO** `sigma_ewma_delta_pct` > `4.996` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.996
  - _Potencial_: sin este filtro IC_bueno=+0.162 (n=338)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.167 (n=235)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0058 (IC base=+0.144)

- **PATRÓN** `sigma_h` > `0.0035` → IC=+0.158 (n=238)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0035 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.0951` → IC=+0.181 (n=89)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.0951 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `19.0` → IC=+0.181 (n=92)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 19.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.516` → IC=+0.194 (n=178)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.516 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.2407` → IC=+0.156 (n=120)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.2407 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.996` → IC=+0.162 (n=338)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 4.996 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.1856` → IC=+0.151 (n=267)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.1856 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `0.8077` → IC=+0.178 (n=178)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.8077 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` < `0.1087` → IC=+0.153 (n=298)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.1087 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.2272` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2272 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.4115` → IC=+0.214 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4115 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `2.6405` → IC=+0.170 (n=89)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.6405 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `12670.6541` → IC=+0.196 (n=238)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 12670.6541 (IC base=+0.144)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.212 (n=359)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.0856` → IC=+0.175 (n=272)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.0856 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=309)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.167 (n=295)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 5.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.157` → IC=+0.158 (n=358)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.157 (IC base=+0.135)

- **PATRÓN** `ibs_20min` > `0.6103` → IC=+0.144 (n=369)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.6103 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.6118` → IC=+0.173 (n=105)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.6118 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.318` → IC=+0.158 (n=794)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 6.318 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `0.8763` → IC=+0.178 (n=542)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.8763 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.0682` → IC=+0.161 (n=381)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.0682 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `2.538` → IC=+0.140 (n=810)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.538 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `2.1636` → IC=+0.153 (n=367)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.1636 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `12053.6057` → IC=+0.148 (n=726)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 12053.6057 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `712.0` → IC=+0.139 (n=767)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 712.0 (IC base=+0.135)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.212 (n=144)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.153)

- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.182 (n=196)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0106 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.6204` → IC=+0.158 (n=431)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.6204 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.237 (n=154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.988` → IC=+0.226 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.988 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.285` → IC=+0.218 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.285 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.2126` → IC=+0.172 (n=120)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2126 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.9185` → IC=+0.161 (n=378)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.9185 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.8333` → IC=+0.155 (n=384)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.8333 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `2307.5732` → IC=+0.185 (n=144)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2307.5732 (IC base=+0.153)

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
- **PATRÓN** `sigma_h` < `0.0088` → IC=+0.144 (n=691)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0088 (IC base=+0.135)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.138 (n=692)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` > 0.0046 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.4977` → IC=+0.142 (n=691)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.4977 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.164 (n=236)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 18.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.137 (n=246)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 4.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` > `0.7971` → IC=+0.158 (n=314)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.7971 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.9872` → IC=+0.182 (n=152)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.9872 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.4203` → IC=+0.143 (n=648)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.4203 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.796` → IC=+0.146 (n=690)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 6.796 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `1.1119` → IC=+0.143 (n=608)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.1119 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` > `0.6457` → IC=+0.135 (n=691)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` > 0.6457 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.175` → IC=+0.149 (n=209)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.175 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `1.4358` → IC=+0.159 (n=227)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.4358 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=638)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `8873.6006` → IC=+0.153 (n=618)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 8873.6006 (IC base=+0.135)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.176 (n=485)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0071 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.5088` → IC=+0.196 (n=551)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.5088 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=207)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.156)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.170 (n=377)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 11.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` > `0.1015` → IC=+0.169 (n=551)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.1015 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.1525` → IC=+0.167 (n=253)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1525 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` < `0.3663` → IC=+0.163 (n=562)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.3663 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.058` → IC=+0.168 (n=263)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.058 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `0.6505` → IC=+0.188 (n=184)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.6505 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` > `0.7336` → IC=+0.160 (n=492)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.7336 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.0735` → IC=+0.183 (n=241)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.0735 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `2.1843` → IC=+0.172 (n=476)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 2.1843 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `1.4479` → IC=+0.170 (n=541)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.4479 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `8205.2722` → IC=+0.167 (n=551)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 8205.2722 (IC base=+0.156)

### GBM_LATE_5M#SOL#5min
- **FILTRO** `hora_utc` > `6.0` → IC=-0.176 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=121)

- **FILTRO** `ibs_20min` < `0.5909` → IC=-0.123 (n=51)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5909
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=105)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=141)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.157` → IC=+0.214 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.157 (IC base=-0.019)

- **PATRÓN** `dist_vwap_pct` > `0.7139` → IC=+0.184 (n=36)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.7139 (IC base=+0.018)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0068` → IC=-0.228 (n=112)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=218)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.210 (n=105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=225)

- **FILTRO** `ibs_20min` > `0.6552` → IC=-0.172 (n=56)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6552
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=172)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.177 (n=370)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0053 (IC base=+0.089)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.157 (n=199)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 18.0 (IC base=+0.089)

- **PATRÓN** `ibs_20min` > `0.6355` → IC=+0.191 (n=461)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.6355 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` > `0.1383` → IC=+0.147 (n=239)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.1383 (IC base=+0.089)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.556` → IC=+0.176 (n=288)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 3.556 (IC base=+0.089)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.238 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` < `2.0912` → IC=+0.148 (n=313)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.0912 (IC base=+0.089)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.133 (n=371)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.089)

- **PATRÓN** `libro_liquidez` > `2498.7472` → IC=+0.165 (n=198)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2498.7472 (IC base=+0.089)

- **PATRÓN** `ibs_20min` < `0.1005` → IC=+0.269 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1005 (IC base=-0.051)

- **PATRÓN** `volumen_pendiente_norm` > `0.0818` → IC=+0.173 (n=47)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.0818 (IC base=-0.051)

- **PATRÓN** `volumen_spike_ratio` < `2.4496` → IC=+0.157 (n=100)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4496 (IC base=-0.051)

- **PATRÓN** `libro_liquidez` > `2560.0731` → IC=+0.129 (n=60)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2560.0731 (IC base=-0.051)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.208 (n=166)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.101)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.203 (n=72)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.101)

- **PATRÓN** `ibs_20min` > `0.5881` → IC=+0.188 (n=158)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.5881 (IC base=+0.101)

- **PATRÓN** `dist_vwap_pct` > `0.1435` → IC=+0.158 (n=77)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1435 (IC base=+0.101)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.739` → IC=+0.137 (n=100)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 3.739 (IC base=+0.101)

- **PATRÓN** `volumen_regimen` < `0.6409` → IC=+0.153 (n=70)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6409 (IC base=+0.101)

- **PATRÓN** `volumen_pendiente_norm` > `0.2496` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2496 (IC base=+0.101)

- **PATRÓN** `volumen_spike_ratio` < `1.9806` → IC=+0.185 (n=106)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.9806 (IC base=+0.101)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.123 (n=160)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.01 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `2890.2457` → IC=+0.123 (n=144)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 2890.2457 (IC base=+0.101)

- **PATRÓN** `drift_60min` |x|≤ `0.0426` → IC=+0.227 (n=20)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0426 (IC base=+0.024)

- **PATRÓN** `ibs_20min` < `0.4946` → IC=+0.210 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4946 (IC base=+0.024)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.914` → IC=+0.189 (n=59)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 5.914 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` < `0.8132` → IC=+0.167 (n=46)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8132 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.0796` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.0796 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` < `2.2976` → IC=+0.262 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2976 (IC base=+0.024)

- **PATRÓN** `libro_liquidez` > `2678.2434` → IC=+0.144 (n=57)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 2678.2434 (IC base=+0.024)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` < `0.6306` → IC=-0.167 (n=55)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6306
  - _Potencial_: sin este filtro IC_bueno=+0.220 (n=166)

- **FILTRO** `sigma_h` > `0.0067` → IC=-0.346 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=75)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.157 (n=132)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0049 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.126 (n=177)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 8.0 (IC base=+0.102)

- **PATRÓN** `ibs_20min` > `0.6306` → IC=+0.220 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6306 (IC base=+0.102)

- **PATRÓN** `dist_vwap_pct` > `0.1208` → IC=+0.159 (n=86)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1208 (IC base=+0.102)

- **PATRÓN** `dist_vwap_pct` < `0.285` → IC=+0.131 (n=155)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.285 (IC base=+0.102)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.21` → IC=+0.290 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.21 (IC base=+0.102)

- **PATRÓN** `volumen_regimen` < `0.7864` → IC=+0.137 (n=111)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.7864 (IC base=+0.102)

- **PATRÓN** `volumen_regimen` > `0.6214` → IC=+0.136 (n=149)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.6214 (IC base=+0.102)

- **PATRÓN** `volumen_pendiente_norm` > `0.3066` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3066 (IC base=+0.102)

- **PATRÓN** `volumen_spike_ratio` > `1.3908` → IC=+0.139 (n=117)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.3908 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.144 (n=172)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.02 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `1360.1033` → IC=+0.191 (n=108)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 1360.1033 (IC base=+0.102)

- **PATRÓN** `ibs_20min` < `0.1005` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1005 (IC base=-0.084)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.082` → IC=+0.156 (n=30)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 4.082 (IC base=-0.084)

- **PATRÓN** `volumen_spike_ratio` > `1.3921` → IC=+0.129 (n=33)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.3921 (IC base=-0.084)

- **PATRÓN** `libro_liquidez` > `1081.2727` → IC=+0.176 (n=35)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 1081.2727 (IC base=-0.084)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `ibs_20min` < `0.6667` → IC=-0.174 (n=44)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6667
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=139)

- **FILTRO** `ibs_20min` > `0.2105` → IC=-0.300 (n=33)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2105
  - _Potencial_: sin este filtro IC_bueno=+0.203 (n=35)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.155 (n=56)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0057 (IC base=+0.060)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.167 (n=139)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.6667 (IC base=+0.060)

- **PATRÓN** `dist_vwap_pct` > `0.8863` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.8863 (IC base=+0.060)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.59` → IC=+0.162 (n=75)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 3.59 (IC base=+0.060)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.060)

- **PATRÓN** `volumen_spike_ratio` < `2.5266` → IC=+0.161 (n=119)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.5266 (IC base=+0.060)

- **PATRÓN** `libro_liquidez` > `363.9251` → IC=+0.150 (n=118)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 363.9251 (IC base=+0.060)

### GBM_LATE_60M_FADE
- **FILTRO** `drift_60min` |x|> `0.1646` → IC=-0.386 (n=33)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1646
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=100)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.466 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=108)

- **FILTRO** `dist_vwap_pct` > `0.2334` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2334
  - _Potencial_: sin este filtro IC_bueno=-0.235 (n=119)

- **FILTRO** `volumen_pendiente_norm` > `0.1172` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1172
  - _Potencial_: sin este filtro IC_bueno=-0.122 (n=43)

- **FILTRO** `sigma_h` > `0.0036` → IC=-0.326 (n=67)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0036
  - _Potencial_: sin este filtro IC_bueno=-0.257 (n=68)

- **FILTRO** `dist_vwap_pct` > `0.4126` → IC=-0.400 (n=18)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4126
  - _Potencial_: sin este filtro IC_bueno=-0.273 (n=117)

- **FILTRO** `volumen_pendiente_norm` > `0.074` → IC=-0.389 (n=16)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.074
  - _Potencial_: sin este filtro IC_bueno=-0.289 (n=36)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `volumen_regimen` < `1.6316` → IC=-0.294 (n=32)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.6316
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **FILTRO** `dist_vwap_pct` < `0.1009` → IC=-0.312 (n=30)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1009
  - _Potencial_: sin este filtro IC_bueno=-0.130 (n=25)

- **FILTRO** `volumen_regimen` > `0.9258` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.9258
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=37)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.5777` → IC=-0.460 (n=23)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5777
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=24)

- **FILTRO** `volumen_regimen` > `0.6161` → IC=-0.333 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.6161
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=15)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `volumen_regimen` < `1.0152` → IC=-0.315 (n=25)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.0152
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.450 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=19)

- **FILTRO** `dist_vwap_pct` < `0.1871` → IC=-0.364 (n=20)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1871
  - _Potencial_: sin este filtro IC_bueno=-0.289 (n=17)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` < `0.641` → IC=-0.242 (n=60)

  - _Acción_: SKIP cuando `ibs_20min` < 0.641
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=183)

- **FILTRO** `ibs_20min` > `0.371` → IC=-0.151 (n=61)

  - _Acción_: SKIP cuando `ibs_20min` > 0.371
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=186)

- **PATRÓN** `ibs_20min` > `0.641` → IC=+0.143 (n=183)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.641 (IC base=+0.047)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.133 (n=88)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 15.0 (IC base=+0.042)

- **PATRÓN** `ibs_20min` < `0.0967` → IC=+0.167 (n=124)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.0967 (IC base=+0.042)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.717` → IC=+0.125 (n=78)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 5.717 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.0687` → IC=+0.154 (n=53)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.0687 (IC base=+0.042)

- **PATRÓN** `libro_liquidez` > `3787.1326` → IC=+0.151 (n=84)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3787.1326 (IC base=+0.042)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=63)

- **FILTRO** `ibs_20min` < `0.3927` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3927
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=60)

- **FILTRO** `volumen_regimen` < `0.7102` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7102
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=60)

- **PATRÓN** `sigma_h` > `0.0028` → IC=+0.149 (n=55)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0028 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` < `0.1622` → IC=+0.193 (n=73)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.1622 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` < `14.217` → IC=+0.133 (n=88)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 14.217 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` < `1.1293` → IC=+0.135 (n=83)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.1293 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` < `3.3907` → IC=+0.148 (n=52)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 3.3907 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` > `1.5879` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.5879 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `3644.5187` → IC=+0.135 (n=83)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 3644.5187 (IC base=+0.116)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `ibs_20min` < `0.6061` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6061
  - _Potencial_: sin este filtro IC_bueno=+0.188 (n=46)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.151 (n=41)

- **FILTRO** `ibs_20min` > `0.3115` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `ibs_20min` > 0.3115
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=50)

- **PATRÓN** `sigma_h` < `0.0025` → IC=+0.288 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0025 (IC base=+0.056)

- **PATRÓN** `drift_60min` |x|≤ `0.111` → IC=+0.136 (n=31)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.111 (IC base=+0.056)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.056)

- **PATRÓN** `ibs_20min` > `0.8029` → IC=+0.174 (n=41)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.8029 (IC base=+0.056)

- **PATRÓN** `dist_vwap_pct` < `0.1167` → IC=+0.136 (n=42)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.1167 (IC base=+0.056)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.056)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.061` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.061 (IC base=-0.006)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.5556` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5556
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=47)

- **FILTRO** `dist_vwap_pct` > `0.1813` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1813
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=45)

- **FILTRO** `volumen_regimen` < `0.6649` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.6649
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=47)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.179 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0047 (IC base=+0.110)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.125 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.110)

- **PATRÓN** `ibs_20min` < `0.9714` → IC=+0.130 (n=52)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.9714 (IC base=+0.110)

- **PATRÓN** `dist_vwap_pct` < `0.1848` → IC=+0.127 (n=65)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` < 0.1848 (IC base=+0.110)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.624` → IC=+0.173 (n=47)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 3.624 (IC base=+0.110)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.204 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.110)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.132 (n=392)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.110)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.125 (n=353)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` > 0.5 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `2828.8084` → IC=+0.169 (n=131)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2828.8084 (IC base=+0.110)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.122 (n=392)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 7.0 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `2309.0554` → IC=+0.130 (n=439)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2309.0554 (IC base=+0.096)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.132 (n=392)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.110)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.125 (n=353)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` > 0.5 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `2828.8084` → IC=+0.169 (n=131)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2828.8084 (IC base=+0.110)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.122 (n=392)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 7.0 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `2309.0554` → IC=+0.130 (n=439)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2309.0554 (IC base=+0.096)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `11.0` → IC=-0.198 (n=61)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=71)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=116)

- **FILTRO** `libro_liquidez` < `2359.8786` → IC=-0.300 (n=33)

  - _Acción_: SKIP cuando `libro_liquidez` < 2359.8786
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=99)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=178)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.124 (n=99)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=100)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=164)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=23)

- **FILTRO** `libro_liquidez` < `12409.8631` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `libro_liquidez` < 12409.8631
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=20)

- **FILTRO** `liq_n` < `4.0` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `liq_n` < 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=16)

- **FILTRO** `libro_liquidez` < `14445.5423` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 14445.5423
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `4919.88` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `liq_usd_total` < 4919.88
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=11)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=1242)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=91)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.140 (n=48)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=80)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=91)

- **FILTRO** `libro_liquidez` < `10665.27` → IC=-0.233 (n=84)

  - _Acción_: SKIP cuando `libro_liquidez` < 10665.27
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=28)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `16.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=49)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_usd_total` < `31327.3` → IC=-0.136 (n=42)

  - _Acción_: SKIP cuando `liq_usd_total` < 31327.3
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=87)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=19)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.167 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=12)

- **PATRÓN** `liq_usd_total` > `54982.77` → IC=+0.157 (n=65)

  - _Acción_: Kelly boost +0.78€ cuando `liq_usd_total` > 54982.77 (IC base=+0.019)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `hora_utc` > `13.0` → IC=-0.154 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=73)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=500)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9593` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9593
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=15)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=418)

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
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=67)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=67)

### LIQUIDACIONES_60M
- **FILTRO** `py_entrada` < `0.425` → IC=-0.140 (n=145)

  - _Acción_: SKIP cuando `py_entrada` < 0.425
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=449)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=206)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=206)

- **FILTRO** `py_entrada` > `0.555` → IC=-0.167 (n=43)

  - _Acción_: SKIP cuando `py_entrada` > 0.555
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=178)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=150)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=150)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.123 (n=75)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=90)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.151 (n=41)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=124)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.197 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=43)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=59)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.167 (n=40)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=153)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=47)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=206)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=206)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=68)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=5399)

### MOMENTUM_IBS_15M#BTC#15min
- **FILTRO** `py_entrada` > `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=925)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=1047)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.46` → IC=-0.180 (n=2134)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=6873)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.177 (n=2174)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=7179)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.208 (n=361)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=1136)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.42` → IC=-0.201 (n=383)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=1175)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.215 (n=394)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=1241)

- **FILTRO** `ibs_20min` > `0.2889` → IC=-0.180 (n=408)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2889
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=1227)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.200 (n=345)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=1106)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.191 (n=406)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=1244)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `libro_spread` > `0.01` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=1850)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=1708)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=1714)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `14.0` → IC=-0.132 (n=74)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=171)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `hora_utc` < `16.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=160)

- **FILTRO** `py_entrada` > `0.615` → IC=-0.315 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.615
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=115)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=517)

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
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=88)

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
- **FILTRO** `py_entrada` < `0.35` → IC=-0.273 (n=5307)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=16229)

- **FILTRO** `ibs_7min` < `0.7112` → IC=-0.233 (n=5383)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7112
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=16153)

- **FILTRO** `ballena_activa_n` > `17.0` → IC=-0.166 (n=7173)

  - _Acción_: SKIP cuando `ballena_activa_n` > 17.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=14363)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.219 (n=6694)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=20239)

- **FILTRO** `ibs_7min` > `0.2993` → IC=-0.176 (n=6733)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2993
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=20200)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.310 (n=794)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=2554)

- **FILTRO** `ibs_7min` < `0.7091` → IC=-0.253 (n=1104)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7091
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=2244)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.208 (n=769)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=2579)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.248 (n=1135)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=3530)

- **FILTRO** `drift_7min_pct` |x|> `0.1118` → IC=-0.129 (n=1586)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1118
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=3079)

- **FILTRO** `ibs_7min` > `0.8043` → IC=-0.204 (n=1166)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8043
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=3499)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.146 (n=888)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=2928)

- **FILTRO** `py_entrada` < `0.36` → IC=-0.252 (n=949)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=2867)

- **FILTRO** `ibs_7min` < `0.7617` → IC=-0.183 (n=954)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7617
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=2862)

- **FILTRO** `ballena_activa_n` > `163.0` → IC=-0.173 (n=947)

  - _Acción_: SKIP cuando `ballena_activa_n` > 163.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=2869)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.260 (n=890)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2954)

- **FILTRO** `ibs_7min` > `0.2506` → IC=-0.169 (n=960)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2506
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=2884)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.175 (n=955)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=2889)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.176 (n=779)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=2380)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.319 (n=745)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=2414)

- **FILTRO** `ibs_7min` < `0.2097` → IC=-0.272 (n=789)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2097
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=2370)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.215 (n=764)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=2395)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.227 (n=1130)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=3793)

- **FILTRO** `ibs_7min` > `0.2667` → IC=-0.154 (n=1670)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2667
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=3253)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.131 (n=1113)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=2443)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.252 (n=854)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=2702)

- **FILTRO** `ibs_7min` < `0.75` → IC=-0.187 (n=889)

  - _Acción_: SKIP cuando `ibs_7min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=2667)

- **FILTRO** `ballena_activa_n` > `35.0` → IC=-0.184 (n=880)

  - _Acción_: SKIP cuando `ballena_activa_n` > 35.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=2676)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.262 (n=892)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=2725)

- **FILTRO** `ibs_7min` > `0.2766` → IC=-0.173 (n=904)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2766
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=2713)

- **FILTRO** `ballena_activa_n` > `32.0` → IC=-0.177 (n=888)

  - _Acción_: SKIP cuando `ballena_activa_n` > 32.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=2729)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.233 (n=986)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=3050)

- **FILTRO** `ibs_7min` < `0.7381` → IC=-0.197 (n=1009)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7381
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=3027)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.169 (n=1222)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=3872)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.282 (n=868)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=2753)

- **FILTRO** `ibs_7min` < `0.7333` → IC=-0.223 (n=904)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7333
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=2717)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.210 (n=870)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=2751)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.192 (n=1162)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=3628)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=905)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.122 (n=43)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=466)

### MOMENTUM_IBS_5M_FADE#DOGE#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=596)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=568)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=512)

### ORDER_FLOW_5M
- **FILTRO** `total_vol_5m` > `215.224` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `total_vol_5m` > 215.224
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `delta_ratio` |x|> `0.3982` → IC=+0.142 (n=626)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.71€ cuando `delta_ratio` |x|> 0.3982 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.140 (n=493)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 6.0 (IC base=+0.130)

- **PATRÓN** `total_vol_5m` < `340643.0` → IC=+0.142 (n=602)

  - _Acción_: Kelly boost +0.71€ cuando `total_vol_5m` < 340643.0 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `3589.6144` → IC=+0.139 (n=250)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 3589.6144 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `78.0` → IC=+0.132 (n=519)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 78.0 (IC base=+0.130)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.266 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.135)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `libro_spread` < `0.02` → IC=+0.121 (n=85)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.02 (IC base=+0.097)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4131` → IC=+0.197 (n=74)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.99€ cuando `delta_ratio` |x|> 0.4131 (IC base=+0.113)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.134 (n=80)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 8.0 (IC base=+0.113)

- **PATRÓN** `total_vol_5m` < `498.2784` → IC=+0.201 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 498.2784 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `7995.4997` → IC=+0.137 (n=100)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 7995.4997 (IC base=+0.113)

- **PATRÓN** `ballena_activa_n` < `75.0` → IC=+0.192 (n=37)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 75.0 (IC base=+0.113)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3997` → IC=+0.217 (n=97)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.3997 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.278 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.172)

- **PATRÓN** `total_vol_5m` < `6300.756` → IC=+0.182 (n=86)

  - _Acción_: Kelly boost +0.91€ cuando `total_vol_5m` < 6300.756 (IC base=+0.172)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.179 (n=54)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.01 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `3632.1507` → IC=+0.187 (n=65)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 3632.1507 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `77.0` → IC=+0.193 (n=86)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 77.0 (IC base=+0.172)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.401` → IC=+0.143 (n=96)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.71€ cuando `delta_ratio` |x|> 0.401 (IC base=+0.114)

- **PATRÓN** `total_vol_5m` < `370723.7` → IC=+0.139 (n=95)

  - _Acción_: Kelly boost +0.70€ cuando `total_vol_5m` < 370723.7 (IC base=+0.114)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.234 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `3502.4912` → IC=+0.184 (n=36)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 3502.4912 (IC base=+0.114)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.152 (n=87)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 52.0 (IC base=+0.114)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.275` → IC=-0.139 (n=34)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.275
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=68)

- **FILTRO** `T_h` > `51.7047` → IC=-0.279 (n=161)

  - _Acción_: SKIP cuando `T_h` > 51.7047
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=80)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.194 (n=70)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0029 (IC base=-0.123)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0041` → IC=-0.243 (n=68)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0041
  - _Potencial_: sin este filtro IC_bueno=+0.340 (n=23)

- **FILTRO** `T_h` > `63.9544` → IC=-0.397 (n=37)

  - _Acción_: SKIP cuando `T_h` > 63.9544
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=39)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.340 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=-0.091)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0087` → IC=-0.152 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0087
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `T_h` < `291.9853` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `T_h` < 291.9853
  - _Potencial_: sin este filtro IC_bueno=+0.192 (n=11)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0132` → IC=-0.184 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0132
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=34)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `pct_vs_K` |x|> `4.085` → IC=-0.256 (n=84)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.085
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=166)

- **FILTRO** `T_h` > `144.6658` → IC=-0.361 (n=70)

  - _Acción_: SKIP cuando `T_h` > 144.6658
  - _Potencial_: sin este filtro IC_bueno=-0.248 (n=137)

- **FILTRO** `pct_vs_K` |x|> `3.96` → IC=-0.431 (n=70)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.96
  - _Potencial_: sin este filtro IC_bueno=-0.212 (n=137)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `pct_vs_K` |x|> `2.8026` → IC=-0.348 (n=31)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.8026
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=63)

- **FILTRO** `T_h` > `144.5878` → IC=-0.315 (n=25)

  - _Acción_: SKIP cuando `T_h` > 144.5878
  - _Potencial_: sin este filtro IC_bueno=-0.245 (n=49)

- **FILTRO** `pct_vs_K` |x|> `2.2737` → IC=-0.447 (n=36)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.2737
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=38)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `T_h` > `135.9851` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `T_h` > 135.9851
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=50)

- **FILTRO** `pct_vs_K` |x|> `4.5365` → IC=-0.444 (n=16)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.5365
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=50)

- **FILTRO** `sigma_h` > `0.0083` → IC=-0.342 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0083
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=54)

- **FILTRO** `sigma_h` < `0.0045` → IC=-0.380 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0045
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=48)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0063` → IC=-0.357 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **FILTRO** `T_h` > `87.8116` → IC=-0.393 (n=26)

  - _Acción_: SKIP cuando `T_h` > 87.8116
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### RESOLUTION_SNIPER
- **PATRÓN** `dist_50` > `0.4444` → IC=+0.457 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4444 (IC base=+0.343)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.447 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.343)

- **PATRÓN** `edge` > `0.1043` → IC=+0.440 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1043 (IC base=+0.402)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.467 (n=58)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.402)

- **PATRÓN** `T_h` > `0.8774` → IC=+0.433 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8774 (IC base=+0.402)

- **PATRÓN** `dist_50` > `0.3811` → IC=+0.485 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3811 (IC base=+0.402)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.439 (n=63)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.402)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.2063` → IC=+0.469 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2063 (IC base=+0.486)

- **PATRÓN** `sigma_h` < `0.0135` → IC=+0.476 (n=39)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0135 (IC base=+0.486)

- **PATRÓN** `sigma_h` > `0.0087` → IC=+0.476 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0087 (IC base=+0.486)

- **PATRÓN** `T_h` > `1.1323` → IC=+0.476 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.1323 (IC base=+0.486)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.476 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.486)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.478 (n=44)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.486)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=103)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=198)

- **PATRÓN** `streak_estiramiento` < `0.4345` → IC=+0.149 (n=35)

  - _Acción_: Kelly boost +0.74€ cuando `streak_estiramiento` < 0.4345 (IC base=+0.000)

- **PATRÓN** `streak_estiramiento` < `0.4159` → IC=+0.204 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.4159 (IC base=+0.025)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `libro_liquidez` < `2197.7726` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `libro_liquidez` < 2197.7726
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=67)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.250 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=80)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=82)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=27)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=402)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=408)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=272)

### STREAK_FADE_60M
- **FILTRO** `hora_utc` > `5.0` → IC=-0.147 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=396)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=784)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=444)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=501)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=2071)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=1100)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1108)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.184 (n=305)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0039 (IC base=+0.168)

- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.194 (n=305)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0085 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.0587` → IC=+0.175 (n=306)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.0587 (IC base=+0.168)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0592` → IC=+0.168 (n=917)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.84€ cuando `delta_ratio_macro` |x|> 0.0592 (IC base=+0.168)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.093` → IC=+0.228 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.093 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.170 (n=644)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 11.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.190 (n=447)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 6.0 (IC base=+0.168)

- **PATRÓN** `ibs_15` > `0.617` → IC=+0.241 (n=915)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.617 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` < `0.1019` → IC=+0.173 (n=609)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.1019 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.695` → IC=+0.244 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.695 (IC base=+0.168)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.169 (n=837)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `3020.8724` → IC=+0.180 (n=610)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 3020.8724 (IC base=+0.168)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=242)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `ibs_15` > `0.5956` → IC=-0.129 (n=122)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.5956
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=237)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.233 (n=159)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.198)

- **PATRÓN** `sigma_h` > `0.0023` → IC=+0.199 (n=237)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0023 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.1873` → IC=+0.218 (n=239)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1873 (IC base=+0.198)

- **PATRÓN** `drift_15min` |x|≤ `0.3761` → IC=+0.220 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3761 (IC base=+0.198)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2368` → IC=+0.204 (n=79)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2368 (IC base=+0.198)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1084` → IC=+0.237 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1084 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.215 (n=244)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.202 (n=246)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.198)

- **PATRÓN** `ibs_15` > `0.8766` → IC=+0.312 (n=158)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8766 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` > `0.3842` → IC=+0.238 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3842 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` < `0.1089` → IC=+0.216 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1089 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.624` → IC=+0.264 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.624 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `8599.8756` → IC=+0.229 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8599.8756 (IC base=+0.198)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `ibs_15` < `0.6973` → IC=-0.129 (n=95)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6973
  - _Potencial_: sin este filtro IC_bueno=+0.260 (n=194)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.148 (n=217)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0062 (IC base=+0.132)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.134 (n=99)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` > 0.0056 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.0772` → IC=+0.163 (n=96)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.0772 (IC base=+0.132)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2488` → IC=+0.180 (n=73)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.2488 (IC base=+0.132)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2712` → IC=+0.159 (n=130)

  - _Acción_: Kelly boost +0.80€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2712 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.139 (n=164)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 11.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.148 (n=225)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 17.0 (IC base=+0.132)

- **PATRÓN** `ibs_15` > `0.6973` → IC=+0.260 (n=194)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6973 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` < `0.2372` → IC=+0.157 (n=208)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.2372 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.024` → IC=+0.204 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.024 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=256)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `11798.8331` → IC=+0.140 (n=73)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 11798.8331 (IC base=+0.132)

### UPDOWN_GBM#ETH#5min
- **FILTRO** `dist_vwap_pct` > `0.2547` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2547
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=416)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `ibs_15` > `0.1909` → IC=-0.204 (n=25)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.1909
  - _Potencial_: sin este filtro IC_bueno=+0.179 (n=26)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.189 (n=59)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0076 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.1676` → IC=+0.149 (n=129)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.1676 (IC base=+0.124)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0662` → IC=+0.150 (n=115)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.75€ cuando `delta_ratio_macro` |x|> 0.0662 (IC base=+0.124)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3186` → IC=+0.206 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3186 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.146 (n=97)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 8.0 (IC base=+0.124)

- **PATRÓN** `ibs_15` > `0.55` → IC=+0.233 (n=129)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.55 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` < `0.213` → IC=+0.139 (n=128)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.213 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.61` → IC=+0.380 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.61 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=113)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `3002.1997` → IC=+0.254 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3002.1997 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.210 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 36.0 (IC base=+0.124)

### UPDOWN_GBM#SOL#60min
- **FILTRO** `ibs_15` < `0.4286` → IC=-0.180 (n=23)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.4286
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=24)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0219` → IC=+0.247 (n=85)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0219 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.09` → IC=+0.187 (n=113)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.09 (IC base=+0.170)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0498` → IC=+0.193 (n=255)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.96€ cuando `delta_ratio_macro` |x|> 0.0498 (IC base=+0.170)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0848` → IC=+0.268 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0848 (IC base=+0.170)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.214 (n=89)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.170)

- **PATRÓN** `ibs_15` > `0.5294` → IC=+0.260 (n=256)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5294 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` > `0.1584` → IC=+0.200 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1584 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `14.987` → IC=+0.212 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 14.987 (IC base=+0.170)

- **PATRÓN** `libro_liquidez` > `2719.6799` → IC=+0.195 (n=116)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2719.6799 (IC base=+0.170)

- **PATRÓN** `ibs_15` < `0.1053` → IC=+0.164 (n=281)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.82€ cuando `ibs_15` < 0.1053 (IC base=+0.045)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.333 (n=184)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.334)

- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.394 (n=92)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0055 (IC base=+0.334)

- **PATRÓN** `drift_60min` |x|≤ `0.16` → IC=+0.344 (n=242)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.16 (IC base=+0.334)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0665` → IC=+0.338 (n=275)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0665 (IC base=+0.334)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.359 (n=267)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.334)

- **PATRÓN** `ibs_15` > `0.8365` → IC=+0.399 (n=246)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8365 (IC base=+0.334)

- **PATRÓN** `dist_vwap_pct` > `0.4169` → IC=+0.357 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4169 (IC base=+0.334)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.664` → IC=+0.353 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.664 (IC base=+0.334)

- **PATRÓN** `sigma_ewma_delta_pct` < `23.866` → IC=+0.333 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 23.866 (IC base=+0.334)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.341 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.334)

- **PATRÓN** `libro_liquidez` > `3951.6306` → IC=+0.347 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3951.6306 (IC base=+0.334)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1118` → IC=+0.354 (n=53)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1118 (IC base=+0.334)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.336 (n=138)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.334)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.354 (n=53)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.334)

- **PATRÓN** `drift_60min` |x|≤ `0.1544` → IC=+0.343 (n=138)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1544 (IC base=+0.334)

- **PATRÓN** `drift_15min` |x|≤ `0.4089` → IC=+0.345 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4089 (IC base=+0.334)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0919` → IC=+0.339 (n=141)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0919 (IC base=+0.334)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1236` → IC=+0.394 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1236 (IC base=+0.334)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.361 (n=149)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.334)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.332 (n=165)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.334)

- **PATRÓN** `ibs_15` > `0.8066` → IC=+0.374 (n=157)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8066 (IC base=+0.334)

- **PATRÓN** `dist_vwap_pct` > `0.242` → IC=+0.375 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.242 (IC base=+0.334)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.152` → IC=+0.339 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.152 (IC base=+0.334)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.187` → IC=+0.345 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.187 (IC base=+0.334)

- **PATRÓN** `libro_liquidez` > `8997.0825` → IC=+0.360 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8997.0825 (IC base=+0.334)

- **PATRÓN** `ballena_activa_n` < `613.0` → IC=+0.401 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 613.0 (IC base=+0.334)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.393 (n=54)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.330)

- **PATRÓN** `drift_60min` |x|≤ `0.0736` → IC=+0.370 (n=52)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0736 (IC base=+0.330)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0624` → IC=+0.350 (n=118)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0624 (IC base=+0.330)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.342 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.330)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.350 (n=118)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.330)

- **PATRÓN** `ibs_15` > `0.7601` → IC=+0.400 (n=118)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7601 (IC base=+0.330)

- **PATRÓN** `dist_vwap_pct` > `0.0995` → IC=+0.329 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.0995 (IC base=+0.330)

- **PATRÓN** `dist_vwap_pct` < `0.2797` → IC=+0.344 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2797 (IC base=+0.330)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.891` → IC=+0.389 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.891 (IC base=+0.330)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.347 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.330)

- **PATRÓN** `libro_liquidez` > `2980.3742` → IC=+0.343 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2980.3742 (IC base=+0.330)

- **PATRÓN** `ballena_activa_n` < `159.0` → IC=+0.348 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 159.0 (IC base=+0.330)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0121` → IC=-0.200 (n=481)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0121
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1446)

- **FILTRO** `ibs_15` < `0.5762` → IC=-0.187 (n=161)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5762
  - _Potencial_: sin este filtro IC_bueno=+0.244 (n=486)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.160 (n=577)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=1350)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.210 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=-0.056)

- **PATRÓN** `ibs_15` > `0.5762` → IC=+0.244 (n=486)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5762 (IC base=-0.056)

- **PATRÓN** `dist_vwap_pct` < `0.2658` → IC=+0.173 (n=380)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.2658 (IC base=-0.056)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1192` → IC=+0.226 (n=614)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1192 (IC base=-0.051)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1809` → IC=+0.232 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1809 (IC base=-0.051)

- **PATRÓN** `ibs_15` < `0.3571` → IC=+0.269 (n=921)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3571 (IC base=-0.051)

- **PATRÓN** `dist_vwap_pct` > `0.6383` → IC=+0.260 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6383 (IC base=-0.051)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0071` → IC=-0.212 (n=290)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0071
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=873)

- **FILTRO** `sigma_h` < `0.0037` → IC=-0.230 (n=383)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0037
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=780)

- **FILTRO** `sigma_ewma_delta_pct` > `20.172` → IC=-0.248 (n=212)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 20.172
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=951)

- **FILTRO** `libro_liquidez` < `14861.3557` → IC=-0.214 (n=581)

  - _Acción_: SKIP cuando `libro_liquidez` < 14861.3557
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=582)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.163 (n=99)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0026 (IC base=+0.067)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1079` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1079 (IC base=+0.067)

- **PATRÓN** `ibs_15` > `0.7661` → IC=+0.356 (n=88)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7661 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` < `0.2346` → IC=+0.278 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2346 (IC base=+0.067)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.6341` → IC=-0.250 (n=78)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6341
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=234)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=295)

- **PATRÓN** `sigma_h` > `0.004` → IC=+0.160 (n=210)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.004 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.0794` → IC=+0.214 (n=103)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0794 (IC base=+0.124)

- **PATRÓN** `drift_15min` |x|≤ `0.4193` → IC=+0.154 (n=79)

  - _Acción_: Kelly boost +0.77€ cuando `drift_15min` |x|≤ 0.4193 (IC base=+0.124)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0547` → IC=+0.127 (n=234)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.64€ cuando `delta_ratio_macro` |x|> 0.0547 (IC base=+0.124)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3059` → IC=+0.222 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3059 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.164 (n=108)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.124)

- **PATRÓN** `ibs_15` > `0.6341` → IC=+0.250 (n=234)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6341 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` < `0.1041` → IC=+0.159 (n=171)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1041 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.094` → IC=+0.134 (n=184)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 7.094 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=295)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `10544.7398` → IC=+0.206 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10544.7398 (IC base=+0.124)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.227 (n=338)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.3518` → IC=+0.227 (n=339)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3518 (IC base=+0.211)

- **PATRÓN** `drift_15min` |x|≤ `0.463` → IC=+0.219 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.463 (IC base=+0.211)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1994` → IC=+0.233 (n=174)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1994 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `19.0` → IC=+0.242 (n=130)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 19.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.227 (n=141)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.211)

- **PATRÓN** `ibs_15` < `0.366` → IC=+0.259 (n=384)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.366 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.7494` → IC=+0.244 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7494 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.951` → IC=+0.222 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.951 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` < `11.621` → IC=+0.217 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 11.621 (IC base=+0.211)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1657` → IC=-0.212 (n=161)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1657
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=313)

- **FILTRO** `drift_15min` |x|> `0.8505` → IC=-0.233 (n=118)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8505
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=356)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.205 (n=171)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=303)

- **PATRÓN** `ibs_15` > `0.8889` → IC=+0.333 (n=16)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8889 (IC base=-0.145)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1145` → IC=+0.208 (n=135)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1145 (IC base=-0.043)

- **PATRÓN** `ibs_15` < `0.3667` → IC=+0.240 (n=202)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3667 (IC base=-0.043)

- **PATRÓN** `dist_vwap_pct` < `0.1451` → IC=+0.186 (n=186)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.1451 (IC base=-0.043)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0187` → IC=-0.245 (n=280)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0187
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=281)

- **FILTRO** `drift_15min` |x|> `1.1577` → IC=-0.239 (n=140)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.1577
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=421)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.229 (n=131)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.150 (n=430)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0965` → IC=+0.366 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0965 (IC base=-0.051)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.291 (n=257)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.051)

- **PATRÓN** `dist_vwap_pct` > `0.4952` → IC=+0.389 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4952 (IC base=-0.051)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.154 (n=50)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0071 (IC base=+0.088)

- **PATRÓN** `drift_60min` |x|≤ `0.4249` → IC=+0.154 (n=50)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4249 (IC base=+0.088)

- **PATRÓN** `drift_15min` |x|≤ `0.588` → IC=+0.167 (n=34)

  - _Acción_: Kelly boost +0.83€ cuando `drift_15min` |x|≤ 0.588 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.1147` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1147 (IC base=+0.088)

- **PATRÓN** `libro_liquidez` > `13398.7443` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13398.7443 (IC base=+0.088)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.154 (n=50)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0071 (IC base=+0.088)

- **PATRÓN** `drift_60min` |x|≤ `0.4249` → IC=+0.154 (n=50)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4249 (IC base=+0.088)

- **PATRÓN** `drift_15min` |x|≤ `0.588` → IC=+0.167 (n=34)

  - _Acción_: Kelly boost +0.83€ cuando `drift_15min` |x|≤ 0.588 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.1147` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1147 (IC base=+0.088)

- **PATRÓN** `libro_liquidez` > `13398.7443` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13398.7443 (IC base=+0.088)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.299 (n=207)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.0587` → IC=+0.343 (n=157)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0587 (IC base=+0.289)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2289` → IC=+0.330 (n=157)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2289 (IC base=+0.289)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1069` → IC=+0.313 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1069 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.307 (n=484)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.8348` → IC=+0.334 (n=469)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8348 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.2698` → IC=+0.316 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2698 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.899` → IC=+0.312 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.899 (IC base=+0.289)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.295 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `12445.3624` → IC=+0.314 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12445.3624 (IC base=+0.289)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.305 (n=116)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.285 (n=119)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.0625` → IC=+0.311 (n=88)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0625 (IC base=+0.284)

- **PATRÓN** `drift_15min` |x|≤ `0.3845` → IC=+0.289 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3845 (IC base=+0.284)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2368` → IC=+0.322 (n=88)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2368 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.333 (n=124)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.284)

- **PATRÓN** `ibs_15` > `0.8592` → IC=+0.319 (n=235)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8592 (IC base=+0.284)

- **PATRÓN** `dist_vwap_pct` > `0.447` → IC=+0.338 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.447 (IC base=+0.284)

- **PATRÓN** `dist_vwap_pct` < `0.1089` → IC=+0.283 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1089 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `24.276` → IC=+0.336 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 24.276 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `15203.8562` → IC=+0.333 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15203.8562 (IC base=+0.284)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.299 (n=182)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.294)

- **PATRÓN** `sigma_h` > `0.0036` → IC=+0.304 (n=207)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0036 (IC base=+0.294)

- **PATRÓN** `drift_60min` |x|≤ `0.0733` → IC=+0.340 (n=92)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0733 (IC base=+0.294)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1898` → IC=+0.333 (n=94)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1898 (IC base=+0.294)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2248` → IC=+0.350 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2248 (IC base=+0.294)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.319 (n=197)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.294)

- **PATRÓN** `ibs_15` > `0.8489` → IC=+0.342 (n=207)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8489 (IC base=+0.294)

- **PATRÓN** `dist_vwap_pct` > `0.2769` → IC=+0.302 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2769 (IC base=+0.294)

- **PATRÓN** `dist_vwap_pct` < `0.1594` → IC=+0.297 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1594 (IC base=+0.294)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.398` → IC=+0.322 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.398 (IC base=+0.294)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.309 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.294)

- **PATRÓN** `libro_liquidez` > `10425.7161` → IC=+0.302 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10425.7161 (IC base=+0.294)

- **PATRÓN** `ballena_activa_n` < `168.0` → IC=+0.301 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 168.0 (IC base=+0.294)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0876` → IC=-0.271 (n=59)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0876
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=179)

- **FILTRO** `sigma_h` > `0.0044` → IC=-0.244 (n=80)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0044
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=158)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1209` → IC=-0.157 (n=106)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1209
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=320)

- **FILTRO** `drift_15min` |x|> `0.5291` → IC=-0.130 (n=106)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.5291
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=320)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.2192` → IC=-0.162 (n=63)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.2192
  - _Potencial_: sin este filtro IC_bueno=-0.151 (n=64)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.126` → IC=-0.167 (n=43)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.126
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=89)

- **FILTRO** `drift_60min` |x|> `0.1544` → IC=-0.200 (n=18)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1544
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=20)

- **FILTRO** `drift_15min` |x|> `0.2287` → IC=-0.250 (n=18)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.2287
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1977` → IC=-0.143 (n=26)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1977
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=14)

- **FILTRO** `sigma_h` < `0.0033` → IC=-0.324 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1979` → IC=-0.382 (n=15)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1979
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `drift_60min` |x|> `0.1352` → IC=-0.167 (n=16)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1352
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.0931` → IC=-0.214 (n=19)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0931
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `63.9922` → IC=+0.124 (n=187)

  - _Acción_: Kelly boost +0.62€ cuando `T_h` > 63.9922 (IC base=+0.122)

- **PATRÓN** `ratio` < `0.9937` → IC=+0.337 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9937 (IC base=+0.122)

- **PATRÓN** `T_h` > `145.9123` → IC=+0.408 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.9123 (IC base=+0.347)

- **PATRÓN** `ratio` > `1.012` → IC=+0.356 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.012 (IC base=+0.347)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `111.9997` → IC=+0.133 (n=58)

  - _Acción_: Kelly boost +0.67€ cuando `T_h` > 111.9997 (IC base=+0.090)

- **PATRÓN** `ratio` < `0.9956` → IC=+0.294 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9956 (IC base=+0.090)

- **PATRÓN** `T_h` > `87.9882` → IC=+0.296 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.9882 (IC base=+0.293)

- **PATRÓN** `ratio` > `1.0349` → IC=+0.433 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0349 (IC base=+0.293)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `111.9922` → IC=+0.196 (n=54)

  - _Acción_: Kelly boost +0.98€ cuando `T_h` > 111.9922 (IC base=+0.179)

- **PATRÓN** `ratio` < `0.9911` → IC=+0.415 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9911 (IC base=+0.179)

- **PATRÓN** `T_h` > `87.9955` → IC=+0.347 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.9955 (IC base=+0.326)

- **PATRÓN** `ratio` > `1.0151` → IC=+0.346 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0151 (IC base=+0.326)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1132` → IC=+0.455 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1132 (IC base=+0.406)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.617 sube el IC de +0.168 a +0.241 en UPDOWN_GBM#15min (n=915). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.8766 sube el IC de +0.198 a +0.312 en UPDOWN_GBM#BTC#15min (n=158). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6973 sube el IC de +0.132 a +0.260 en UPDOWN_GBM#ETH#15min (n=194). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.55 sube el IC de +0.124 a +0.233 en UPDOWN_GBM#SOL#15min (n=129). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5294 sube el IC de +0.170 a +0.260 en UPDOWN_GBM#XRP#15min (n=256). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1053 sube el IC de +0.045 a +0.164 en UPDOWN_GBM#XRP#15min (n=281). Ya aplicado como kelly_boost=+0.82€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.5762 sube el IC de -0.056 a +0.244 en UPDOWN_GBM_15M_TARDIO (n=486). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3571 sube el IC de -0.051 a +0.269 en UPDOWN_GBM_15M_TARDIO (n=921). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7661 sube el IC de +0.067 a +0.356 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=88). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6341 sube el IC de +0.124 a +0.250 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=234). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.366 sube el IC de +0.211 a +0.259 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=384). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8889 sube el IC de -0.145 a +0.333 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=16). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3667 sube el IC de -0.043 a +0.240 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=202). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.051 a +0.291 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=257). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8348 sube el IC de +0.289 a +0.334 en UPDOWN_GBM_IBS_ALTO (n=469). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8592 sube el IC de +0.284 a +0.319 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=235). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.294 a +0.342 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=207). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.8365 sube el IC de +0.334 a +0.399 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=246). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.334 a +0.374 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=157). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7601 sube el IC de +0.330 a +0.400 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=118). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#ETH#sniper` — IC=+0.321 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#ETH` — IC=+0.321 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min` — IC=+0.372 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL` — IC=+0.372 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1074 | +0.080 | +103.56€ | 2 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1074 | +0.080 | +103.56€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 774 | +0.086 | +82.93€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 774 | +0.086 | +82.93€ | 3 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 226 | +0.040 | +1.43€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 226 | +0.040 | +1.43€ | 3 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 48 | +0.180 | +20.69€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 48 | +0.180 | +20.69€ | 0 | 1 |
| ✅ BALLENAS_TARDIAS | 20634 | -0.106 | -3079.70€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1117 | -0.028 | -187.35€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 19517 | -0.111 | -2892.35€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 2868 | -0.107 | -503.98€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 2868 | -0.107 | -503.98€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1117 | -0.028 | -187.35€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1117 | -0.028 | -187.35€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 2658 | -0.095 | -606.78€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 2658 | -0.095 | -606.78€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 5345 | -0.068 | -489.44€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 5345 | -0.068 | -489.44€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 4740 | -0.116 | -366.85€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 4740 | -0.116 | -366.85€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 3906 | -0.177 | -925.30€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 3906 | -0.177 | -925.30€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 9379 | -0.053 | +3864.89€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 2584 | -0.010 | +1643.13€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 6795 | -0.069 | +2221.76€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 9379 | -0.053 | +3864.89€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 2584 | -0.010 | +1643.13€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 6795 | -0.069 | +2221.76€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 296 | -0.097 | -50.73€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#15min | 5 | +0.018 | +0.75€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 291 | -0.101 | -51.48€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB | 16 | -0.089 | -0.58€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB#5min | 16 | -0.089 | -0.58€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 192 | -0.036 | -16.73€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 192 | -0.036 | -16.73€ | 1 | 1 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH | 77 | -0.196 | -23.16€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#15min | 5 | +0.018 | +0.75€ | 0 | 0 |
| 🚫 CANDIDATA9_BOT_CONSENSO#ETH#5min | 72 | -0.216 | -23.90€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL | 6 | -0.113 | -6.43€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL#5min | 6 | -0.113 | -6.43€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP | 5 | -0.054 | -3.83€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP#5min | 5 | -0.054 | -3.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 65303 | +0.112 | -3708.13€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 10465 | +0.182 | -322.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 250 | -0.111 | -46.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 50203 | +0.098 | -3260.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 4385 | +0.117 | -78.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 8379 | +0.092 | -886.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 35 | -0.176 | -2.14€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 8329 | +0.094 | -872.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 12940 | +0.132 | -260.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 3150 | +0.203 | -87.97€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 8323 | +0.108 | -188.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 1425 | +0.119 | +38.92€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 8414 | +0.086 | -905.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 40 | -0.048 | -3.03€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 8359 | +0.087 | -890.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 14076 | +0.125 | -280.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 4001 | +0.170 | -75.09€ | 1 | 7 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 8372 | +0.109 | -153.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 1691 | +0.099 | -43.40€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 13098 | +0.116 | -803.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 3205 | +0.186 | -159.04€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 153 | -0.055 | +7.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 8471 | +0.090 | -578.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1269 | +0.137 | -73.52€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 8396 | +0.100 | -572.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 34 | -0.028 | +4.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 8349 | +0.101 | -576.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 10179 | +0.184 | -728.63€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 10179 | +0.184 | -728.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 2599 | +0.170 | -270.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 2599 | +0.170 | -270.22€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 149 | -0.136 | -0.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 149 | -0.136 | -0.83€ | 4 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 2556 | +0.177 | -236.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 2556 | +0.177 | -236.42€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 2296 | +0.238 | -60.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 2296 | +0.238 | -60.02€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 2500 | +0.189 | -174.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 2500 | +0.189 | -174.89€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 485 | +0.443 | -0.11€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 485 | +0.443 | -0.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 190 | +0.443 | +0.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 190 | +0.443 | +0.96€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 184 | +0.441 | +0.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 184 | +0.441 | +0.66€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 105 | +0.425 | -2.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 105 | +0.425 | -2.15€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 35400 | +0.191 | -3130.73€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 35400 | +0.191 | -3130.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 6219 | +0.162 | -852.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 6219 | +0.162 | -852.58€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 5568 | +0.222 | -221.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 5568 | +0.222 | -221.01€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 6131 | +0.165 | -808.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 6131 | +0.165 | -808.63€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 5671 | +0.218 | -235.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 5671 | +0.218 | -235.54€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 5854 | +0.197 | -437.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 5854 | +0.197 | -437.20€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 5957 | +0.188 | -575.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 5957 | +0.188 | -575.78€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 13113 | +0.124 | +269.23€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 13113 | +0.124 | +269.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 6494 | +0.131 | +206.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 6494 | +0.131 | +206.39€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 6619 | +0.118 | +62.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 6619 | +0.118 | +62.84€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1145 | +0.289 | -20.16€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1145 | +0.289 | -20.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 505 | +0.277 | -13.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 505 | +0.277 | -13.39€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 543 | +0.291 | -5.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 543 | +0.291 | -5.45€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 97 | +0.328 | -1.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 97 | +0.328 | -1.32€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 503 | +0.427 | -10.59€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 503 | +0.427 | -10.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 233 | +0.428 | -4.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 233 | +0.428 | -4.51€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 233 | +0.428 | -5.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 233 | +0.428 | -5.63€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 37 | +0.372 | -0.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 37 | +0.372 | -0.46€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 726 | +0.073 | -32.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 256 | +0.070 | -16.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 470 | +0.074 | -16.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 47 | +0.092 | +0.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 47 | +0.092 | +0.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 565 | +0.082 | -11.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 95 | +0.119 | +4.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 470 | +0.074 | -16.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 114 | +0.017 | -20.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 114 | +0.017 | -20.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 22374 | +0.095 | -775.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 1915 | +0.087 | +10.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 20459 | +0.096 | -786.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 12907 | +0.100 | -238.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 1915 | +0.087 | +10.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 10992 | +0.102 | -248.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 3658 | +0.112 | +16.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 3658 | +0.112 | +16.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 5809 | +0.075 | -554.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 5809 | +0.075 | -554.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 658 | +0.262 | -75.53€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 658 | +0.262 | -75.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 658 | +0.262 | -75.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 658 | +0.262 | -75.53€ | 0 | 4 |
| ✅ GBM_LATE_15M | 17136 | +0.072 | +7660.54€ | 0 | 13 |
| ✅ GBM_LATE_15M#15min | 17136 | +0.072 | +7660.54€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 2779 | +0.198 | +2068.85€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 2779 | +0.198 | +2068.85€ | 0 | 24 |
| ✅ GBM_LATE_15M#BTC | 2529 | +0.174 | +1698.03€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 2529 | +0.174 | +1698.03€ | 0 | 27 |
| ✅ GBM_LATE_15M#DOGE | 2884 | +0.194 | +2088.58€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 2884 | +0.194 | +2088.58€ | 0 | 22 |
| ✅ GBM_LATE_15M#ETH | 2580 | -0.008 | +332.08€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 2580 | -0.008 | +332.08€ | 1 | 13 |
| ✅ GBM_LATE_15M#SOL | 2571 | -0.039 | +587.61€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 2571 | -0.039 | +587.61€ | 4 | 15 |
| ✅ GBM_LATE_15M#XRP | 3793 | -0.054 | +885.40€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 3793 | -0.054 | +885.40€ | 4 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 18001 | +0.074 | +9065.72€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 18001 | +0.074 | +9065.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 3263 | +0.009 | +1881.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 3263 | +0.009 | +1881.18€ | 2 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 3840 | -0.001 | +695.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 3840 | -0.001 | +695.36€ | 1 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 2520 | +0.257 | +2486.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 2520 | +0.257 | +2486.21€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 2728 | -0.033 | +199.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 2728 | -0.033 | +199.80€ | 3 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 3009 | +0.011 | +1074.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 3009 | +0.011 | +1074.02€ | 3 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 2641 | +0.268 | +2729.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 2641 | +0.268 | +2729.15€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 13997 | +0.169 | +10064.19€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 13997 | +0.169 | +10064.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 2042 | +0.210 | +1645.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 2042 | +0.210 | +1645.32€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 2223 | +0.158 | +1557.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 2223 | +0.158 | +1557.84€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 2133 | +0.203 | +1656.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 2133 | +0.203 | +1656.00€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 2310 | +0.138 | +1472.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 2310 | +0.138 | +1472.46€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 2647 | +0.113 | +1659.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 2647 | +0.113 | +1659.97€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 2642 | +0.201 | +2072.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 2642 | +0.201 | +2072.59€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 3357 | +0.118 | +1231.16€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 3357 | +0.118 | +1231.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 105 | +0.107 | +39.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 105 | +0.107 | +39.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 924 | +0.108 | +327.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 924 | +0.108 | +327.25€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 368 | +0.149 | +182.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 368 | +0.149 | +182.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 934 | +0.147 | +386.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 934 | +0.147 | +386.83€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 639 | +0.066 | +143.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 639 | +0.066 | +143.04€ | 2 | 11 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 387 | +0.130 | +151.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 387 | +0.130 | +151.73€ | 0 | 28 |
| ✅ GBM_LATE_15M_TARDIO | 17146 | +0.173 | +12311.83€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#15min | 17146 | +0.173 | +12311.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 2659 | +0.225 | +2278.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 2659 | +0.225 | +2278.93€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 2701 | +0.153 | +1793.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 2701 | +0.153 | +1793.64€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 2732 | +0.221 | +2298.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 2732 | +0.221 | +2298.62€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 2707 | +0.133 | +1682.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 2707 | +0.133 | +1682.38€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 3028 | +0.106 | +1660.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 3028 | +0.106 | +1660.74€ | 0 | 17 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 3319 | +0.204 | +2597.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 3319 | +0.204 | +2597.53€ | 0 | 26 |
| ✅ GBM_LATE_5M | 5104 | +0.134 | +2623.36€ | 1 | 25 |
| ✅ GBM_LATE_5M#5min | 5104 | +0.134 | +2623.36€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 474 | +0.176 | +313.59€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 474 | +0.176 | +313.59€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1438 | +0.138 | +848.66€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1438 | +0.138 | +848.66€ | 1 | 28 |
| ✅ GBM_LATE_5M#DOGE | 633 | +0.163 | +380.44€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 633 | +0.163 | +380.44€ | 0 | 21 |
| ✅ GBM_LATE_5M#ETH | 1655 | +0.144 | +871.27€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 1655 | +0.144 | +871.27€ | 0 | 29 |
| ✅ GBM_LATE_5M#SOL | 262 | -0.004 | +10.11€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 262 | -0.004 | +10.11€ | 3 | 2 |
| ✅ GBM_LATE_5M#XRP | 642 | +0.096 | +199.29€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 642 | +0.096 | +199.29€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1066 | +0.046 | +345.26€ | 3 | 13 |
| ✅ GBM_LATE_60M#60min | 1066 | +0.046 | +345.26€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 373 | +0.076 | +129.36€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 373 | +0.076 | +129.36€ | 0 | 17 |
| ✅ GBM_LATE_60M#ETH | 361 | +0.051 | +127.90€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 361 | +0.051 | +127.90€ | 2 | 16 |
| ✅ GBM_LATE_60M#SOL | 332 | +0.006 | +88.00€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 332 | +0.006 | +88.00€ | 2 | 7 |
| 🚫 GBM_LATE_60M_FADE | 270 | -0.276 | -32.82€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 270 | -0.276 | -32.82€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 104 | -0.217 | -6.69€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 104 | -0.217 | -6.69€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 90 | -0.337 | -22.27€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 90 | -0.337 | -22.27€ | 2 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 76 | -0.269 | -3.85€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 76 | -0.269 | -3.85€ | 3 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 490 | +0.045 | +69.10€ | 2 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 490 | +0.045 | +69.10€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 189 | +0.050 | +25.61€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 189 | +0.050 | +25.61€ | 3 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 136 | +0.022 | -10.26€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 136 | +0.022 | -10.26€ | 3 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 165 | +0.057 | +53.75€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 165 | +0.057 | +53.75€ | 3 | 6 |
| ✅ LATE_WINDOW_5MIN | 53 | +0.227 | +25.89€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 53 | +0.227 | +25.89€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 53 | +0.227 | +25.89€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 53 | +0.227 | +25.89€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 1106 | +0.103 | +316.64€ | 0 | 5 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 1106 | +0.103 | +316.64€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 1106 | +0.103 | +316.64€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 1106 | +0.103 | +316.64€ | 0 | 5 |
| ✅ LIQUIDACIONES_15M | 331 | -0.095 | -37.20€ | 6 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 331 | -0.095 | -37.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 78 | -0.100 | -9.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 78 | -0.100 | -9.01€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 66 | -0.073 | -6.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 66 | -0.073 | -6.94€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 106 | -0.028 | -4.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 106 | -0.028 | -4.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 1439 | -0.007 | -12.09€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1439 | -0.007 | -12.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 75 | -0.033 | -5.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 75 | -0.033 | -5.22€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 163 | -0.021 | +0.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 163 | -0.021 | +0.58€ | 3 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 101 | -0.053 | -6.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 101 | -0.053 | -6.47€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 546 | +0.020 | +13.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 546 | +0.020 | +13.21€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 458 | -0.006 | -8.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 458 | -0.006 | -8.22€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 96 | -0.061 | -5.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 96 | -0.061 | -5.96€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M | 815 | -0.043 | -22.28€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 815 | -0.043 | -22.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 239 | -0.064 | -16.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 239 | -0.064 | -16.95€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 257 | -0.017 | +0.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 257 | -0.017 | +0.81€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 319 | -0.048 | -6.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 319 | -0.048 | -6.14€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M | 11338 | -0.010 | -155.44€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 11338 | -0.010 | -155.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 577 | -0.009 | +0.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 577 | -0.009 | +0.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 1900 | -0.019 | -36.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 1900 | -0.019 | -36.79€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2556 | +0.008 | -17.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2556 | +0.008 | -17.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 2137 | -0.015 | -10.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 2137 | -0.015 | -10.49€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 2680 | -0.018 | -60.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 2680 | -0.018 | -60.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1488 | -0.005 | -30.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1488 | -0.005 | -30.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 18360 | -0.017 | +889.56€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 18360 | -0.017 | +889.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 3158 | +0.005 | +473.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 3158 | +0.005 | +473.12€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 2966 | -0.027 | -12.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 2966 | -0.027 | -12.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 3193 | -0.004 | +262.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 3193 | -0.004 | +262.99€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 2845 | -0.046 | -55.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 2845 | -0.046 | -55.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 3097 | -0.021 | +128.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 3097 | -0.021 | +128.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 3101 | -0.011 | +92.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 3101 | -0.011 | +92.56€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 3659 | -0.029 | -78.71€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 3659 | -0.029 | -78.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 697 | -0.001 | -13.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 697 | -0.001 | -13.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 611 | -0.042 | -16.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 611 | -0.042 | -16.57€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 40 | -0.119 | -5.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 40 | -0.119 | -5.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 344 | -0.110 | -7.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 344 | -0.110 | -7.93€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1126 | -0.023 | -11.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1126 | -0.023 | -11.09€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 841 | -0.015 | -24.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 841 | -0.015 | -24.63€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3186 | +0.004 | -3.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3186 | +0.004 | -3.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 185 | +0.008 | -2.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 185 | +0.008 | -2.27€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE | 136 | +0.000 | -1.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 136 | +0.000 | -1.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1163 | +0.008 | +8.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1163 | +0.008 | +8.30€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1387 | +0.007 | -0.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1387 | +0.007 | -0.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 48469 | -0.073 | +950.76€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 48469 | -0.073 | +950.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 8013 | -0.084 | +453.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 8013 | -0.084 | +453.21€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 7660 | -0.087 | -277.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 7660 | -0.087 | -277.19€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 8082 | -0.072 | +398.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 8082 | -0.072 | +398.94€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 7173 | -0.096 | -268.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 7173 | -0.096 | -268.80€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 9130 | -0.045 | +263.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 9130 | -0.045 | +263.59€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 8411 | -0.064 | +381.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 8411 | -0.064 | +381.02€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6560 | -0.019 | -114.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6560 | -0.019 | -114.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1429 | -0.017 | -14.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1429 | -0.017 | -14.57€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1002 | -0.020 | -30.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1002 | -0.020 | -30.79€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1437 | -0.011 | -10.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1437 | -0.011 | -10.59€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 959 | -0.031 | -14.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 959 | -0.031 | -14.32€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 737 | -0.021 | -24.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 737 | -0.021 | -24.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 871 | +0.116 | +310.17€ | 1 | 5 |
| ✅ ORDER_FLOW_5M#5min | 735 | +0.127 | +297.58€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 168 | +0.135 | +81.11€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 168 | +0.135 | +81.11€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#DOGE | 147 | +0.097 | +35.56€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 147 | +0.097 | +35.56€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 148 | +0.113 | +56.74€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 148 | +0.113 | +56.74€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 129 | +0.172 | +77.59€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 129 | +0.172 | +77.59€ | 0 | 7 |
| ✅ ORDER_FLOW_5M#XRP | 143 | +0.114 | +46.58€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 143 | +0.114 | +46.58€ | 0 | 5 |
| ✅ PRICE_TARGET_GBM | 410 | -0.100 | -12.69€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 180 | -0.154 | -36.52€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 146 | -0.196 | -37.41€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 34 | +0.028 | +0.89€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 148 | -0.087 | +4.75€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 110 | -0.098 | -1.87€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 38 | -0.050 | +6.62€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 82 | +0.000 | +19.08€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 63 | -0.023 | +12.47€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 19 | +0.068 | +6.61€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 319 | -0.129 | -26.81€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 91 | +0.005 | +14.12€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 457 | -0.219 | -30.11€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 194 | -0.199 | -26.68€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 168 | -0.188 | -24.38€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 26 | -0.250 | -2.30€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 160 | -0.247 | -19.85€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 137 | -0.255 | -23.72€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 23 | -0.180 | +3.88€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 103 | -0.205 | +16.41€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#atexpiry | 89 | -0.203 | +13.35€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 14 | -0.131 | +3.06€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 394 | -0.217 | -34.75€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#reach | 63 | -0.223 | +4.64€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 159 | +0.388 | +106.60€ | 0 | 7 |
| ✅ RESOLUTION_SNIPER#BTC | 21 | -0.022 | -5.36€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 21 | -0.022 | -5.36€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 37 | +0.321 | +34.38€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 37 | +0.321 | +34.38€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 101 | +0.490 | +77.58€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 101 | +0.490 | +77.58€ | 0 | 6 |
| ✅ RESOLUTION_SNIPER#sniper | 159 | +0.388 | +106.60€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 339 | +0.016 | -3.79€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 339 | +0.016 | -3.79€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 148 | +0.040 | +2.51€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 148 | +0.040 | +2.51€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 22 | +0.042 | +1.24€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 22 | +0.042 | +1.24€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 37 | -0.064 | -6.20€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 37 | -0.064 | -6.20€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 132 | +0.007 | -1.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 132 | +0.007 | -1.34€ | 1 | 0 |
| ✅ STREAK_FADE_5M | 2243 | -0.025 | -100.63€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2243 | -0.025 | -100.63€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 559 | -0.024 | -23.97€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 559 | -0.024 | -23.97€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 146 | -0.041 | -13.44€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 146 | -0.041 | -13.44€ | 3 | 0 |
| ✅ STREAK_FADE_5M#XRP | 734 | -0.029 | -36.28€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 734 | -0.029 | -36.28€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 48 | +0.020 | +0.80€ | 1 | 0 |
| ✅ STREAK_FADE_60M#60min | 48 | +0.020 | +0.80€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 29 | -0.048 | -1.89€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 29 | -0.048 | -1.89€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 19 | +0.113 | +2.69€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 19 | +0.113 | +2.69€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 5535 | +0.023 | +82.72€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 5535 | +0.023 | +82.72€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 1799 | +0.024 | +22.08€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 1799 | +0.024 | +22.08€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1143 | +0.037 | +38.56€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1143 | +0.037 | +38.56€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 1606 | +0.010 | -2.50€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 1606 | +0.010 | -2.50€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 987 | +0.026 | +24.58€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 987 | +0.026 | +24.58€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 5353 | +0.013 | -23.60€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 5353 | +0.013 | -23.60€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 2090 | +0.019 | +0.36€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 2090 | +0.019 | +0.36€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 2131 | +0.017 | -1.66€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 2131 | +0.017 | -1.66€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1132 | -0.004 | -22.29€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1132 | -0.004 | -22.29€ | 2 | 0 |
| ✅ UPDOWN_GBM | 19600 | +0.025 | +1010.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 5699 | +0.054 | +859.98€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 763 | +0.001 | +5.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 11885 | +0.017 | +155.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 1166 | -0.006 | -14.53€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 1555 | +0.065 | +139.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 253 | +0.123 | +77.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 18 | -0.045 | -1.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 1284 | +0.054 | +63.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 3393 | +0.030 | +237.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 675 | +0.084 | +162.75€ | 1 | 13 |
| ✅ UPDOWN_GBM#BTC#240min | 221 | +0.029 | +7.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 1958 | +0.021 | +67.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 507 | -0.001 | -2.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 32 | -0.118 | +2.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 2349 | +0.022 | +54.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 215 | +0.108 | +50.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 14 | -0.044 | -1.32€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 2120 | +0.014 | +4.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 3962 | +0.012 | +142.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 1573 | +0.036 | +147.56€ | 1 | 12 |
| ✅ UPDOWN_GBM#ETH#240min | 209 | +0.007 | +8.33€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 1716 | -0.001 | -11.22€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 435 | -0.010 | -6.10€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 29 | -0.145 | +4.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 5255 | +0.015 | +111.50€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 1523 | +0.022 | +83.28€ | 0 | 11 |
| ✅ UPDOWN_GBM#SOL#240min | 203 | -0.007 | -2.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 3281 | +0.015 | +37.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 224 | -0.009 | -5.74€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 24 | -0.154 | -0.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 3084 | +0.037 | +327.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 1460 | +0.074 | +338.66€ | 0 | 10 |
| ✅ UPDOWN_GBM#XRP#240min | 98 | -0.040 | -5.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 1526 | +0.007 | -5.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 85 | -0.144 | +5.83€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 366 | +0.334 | +95.41€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 366 | +0.334 | +95.41€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 209 | +0.334 | +50.96€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 209 | +0.334 | +50.96€ | 0 | 15 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 157 | +0.330 | +44.45€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 157 | +0.330 | +44.45€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 7940 | -0.052 | +1630.86€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 7940 | -0.052 | +1630.86€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 379 | -0.049 | +344.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 379 | -0.049 | +344.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 1556 | -0.133 | -71.20€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 1556 | -0.133 | -71.20€ | 4 | 4 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 136 | +0.116 | +52.67€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 136 | +0.116 | +52.67€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 823 | +0.179 | +444.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 823 | +0.179 | +444.19€ | 2 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 2562 | -0.062 | +424.40€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 2562 | -0.062 | +424.40€ | 3 | 4 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 2484 | -0.078 | +435.91€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 2484 | -0.078 | +435.91€ | 3 | 3 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 83 | +0.065 | +8.06€ | 0 | 5 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 83 | +0.065 | +8.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 83 | +0.065 | +8.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 83 | +0.065 | +8.06€ | 0 | 5 |
| ✅ UPDOWN_GBM_IBS_ALTO | 625 | +0.289 | +509.90€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 625 | +0.289 | +509.90€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 350 | +0.284 | +271.23€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 350 | +0.284 | +271.23€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 275 | +0.294 | +238.66€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 275 | +0.294 | +238.66€ | 0 | 13 |
| ✅ UPDOWN_OU_5M | 664 | -0.105 | -76.93€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#5min | 664 | -0.105 | -76.93€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 170 | -0.064 | -11.65€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 170 | -0.064 | -11.65€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 64 | -0.182 | -10.25€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 64 | -0.182 | -10.25€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 52 | -0.167 | -5.48€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 52 | -0.167 | -5.48€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 1696 | +0.300 | +841.58€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 557 | +0.235 | +67.93€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 585 | +0.289 | +222.97€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 554 | +0.374 | +550.68€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.066) — sin ventaja clara. oversold(IBS<0.3): IC=+0.039 n=6820 | neutral: IC=+0.023 n=7522 | overbought(IBS>0.7): IC=+0.089 n=7327
  - _Datos_: n=22436 IC=+0.051 PNL=+2642.11€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 383 celda(s) pasan gate riguroso completo de 1907 evaluadas (n>=40) y 2863 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.022 < 0.08 — monitorear
  - _Datos_: n=1520 IC=+0.022 PNL=+82.81€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=585/15 IC=+0.289 PNL=+222.97€ | BTC: n=557/15 IC=+0.235 PNL=+67.93€ | SOL: n=554/15 IC=+0.374 PNL=+550.68€

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 29 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH#60min, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC#60min
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
  - _Estado_: 19489 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.062 n=144/60 | contraria IC=+0.129 n=130 | gap=-0.067 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=205, boost estimado=+0.001. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 129 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=435/40 IC=-0.010 PNL=-6.10€ | BTC#60min: n=507/40 IC=-0.001 PNL=-2.69€ | SOL#60min: n=224/40 IC=-0.009 PNL=-5.74€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.056 n=223733 | tras_1loss IC=+0.066 n=175763 | tras_2loss IC=+0.033 n=76327/40 | gap=+0.023 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=-0.000 n=1853 | contrario_BTC IC=+0.017 n=1738/40 | gap=+0.017 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.196 > 0.08 con n=166 PNL=+108.29€
  - _Datos_: n=166 IC=+0.196 PNL=+108.29€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.192 > 0.08 con n=225 PNL=+136.14€
  - _Datos_: n=225 IC=+0.192 PNL=+136.14€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.242 > 0.08 con n=29 PNL=+21.27€
  - _Datos_: n=29 IC=+0.242 PNL=+21.27€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.340 > 0.1 con n=1425 PNL=+834.71€
  - _Datos_: n=1425 IC=+0.340 PNL=+834.71€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=138 IC=+0.071 PNL=+19.45€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=138 IC=+0.071 PNL=+19.45€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=41 IC=+0.198 PNL=+28.61€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=41 IC=+0.198 PNL=+28.61€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=18942 IC=+0.024 PNL=+923.82€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=18942 IC=+0.024 PNL=+923.82€

**⏳ H-CUSTOM-OF-02H-BTCSOL** — ORDER_FLOW H=02h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 02h está en el blacklist basado en TODOS los pares. Con BTC+SOL solo, el historial muestra 4/5 (80%) IC=+0.054. ¿Se confirma la señal positiva con más datos?
  - _Umbral_: 15
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 02h del blacklist ORDER_FLOW
  - _Estado_: 2/15 ops en el filtro definido (IC actual=+0.025 PNL=+3.18€)
  - _Datos_: n=2 IC=+0.025 PNL=+3.18€

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
  - _Estado_: n=870 IC=-0.003 PNL=-12.51€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=870 IC=-0.003 PNL=-12.51€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=296 IC=-0.013 PNL=-2.02€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=296 IC=-0.013 PNL=-2.02€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=295 IC=+0.025 PNL=+18.62€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=295 IC=+0.025 PNL=+18.62€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.167 > 0.1 con n=1218 PNL=+645.78€
  - _Datos_: n=1218 IC=+0.167 PNL=+645.78€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=398 IC=+0.050 PNL=+51.37€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=398 IC=+0.050 PNL=+51.37€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=675 IC=+0.084 PNL=+162.75€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=675 IC=+0.084 PNL=+162.75€

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
  - _Estado_: n=3270 IC=+0.056 PNL=+566.67€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3270 IC=+0.056 PNL=+566.67€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=89 IC=-0.214 PNL=-3.22€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=89 IC=-0.214 PNL=-3.22€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=162 IC=-0.018 PNL=+14.75€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=162 IC=-0.018 PNL=+14.75€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=268 IC=+0.018 PNL=+19.23€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=268 IC=+0.018 PNL=+19.23€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=17 IC=-0.022 PNL=-1.11€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=17 IC=-0.022 PNL=-1.11€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=2938 IC=-0.009 PNL=-29.43€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2938 IC=-0.009 PNL=-29.43€

**🟡 H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.156 > 0.08 con n=59 PNL=+12.92€
  - _Datos_: n=59 IC=+0.156 PNL=+12.92€

**🔶 H-LATE-WINDOW-5MIN** — Late-window BTC 5min — arbitraje timing vs Polymarket
  - _Hipótesis_: Inspirado en VyvanseWithMarijuana (36.5% ROI, $42k vol). A T+160-270s dentro de una ventana BTC 5min, si BTC ya se movió >0.3%, Polymarket no ha actualizado precio → edge estructural. Estrategia LATE_WINDOW_5MIN en shadow hasta n≥30. FIX 2026-07-02: la estrategia llevaba 0 predicciones desde su creacion porque HORIZONTE_MIN_HORAS=0.05 (3min) descartaba todo mercado a <3min de expirar — y su zona de entrada (160-270s de una ventana de 5min) deja 30-140s restantes, siempre bajo el suelo. Corregido en shadow_predict (zona late-window marcada _solo_late, 30s-3min, solo evaluada por esta estrategia). El reloj de acumulacion empieza de verdad hoy. Contexto extra: el estudio de ballenas de hoy confirma que comprar el lado ganador a mitad/final de ventana es el playbook comun de los 3 mayores ganadores verificados de estos mercados (Bonereaper +$19.9k/mes, wowitsamazing +$10k/mes, zhangfan151 +$8.7k/mes).
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si IC≥0.08 con n≥30 → proponer pasar a live con stake mínimo (0.50€). Si IC<0 con n≥30 → el lag de Polymarket en BTC es insuficiente.
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.227 n=53) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=53 IC=+0.227 PNL=+25.89€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=4081 IC=+0.025 PNL=+202.58€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=4081 IC=+0.025 PNL=+202.58€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=1335 IC=+0.047 PNL=+128.06€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1335 IC=+0.047 PNL=+128.06€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.107 > 0.08 con n=263 PNL=+73.91€
  - _Datos_: n=263 IC=+0.107 PNL=+73.91€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.155 > 0.08 con n=340 PNL=+73.48€
  - _Datos_: n=340 IC=+0.155 PNL=+73.48€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.130 > 0.08 con n=279 PNL=+148.95€
  - _Datos_: n=279 IC=+0.130 PNL=+148.95€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=27153 IC=+0.103 PNL=+8552.65€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=27153 IC=+0.103 PNL=+8552.65€

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
  - _Estado_: n=2666 IC=+0.035 PNL=+174.44€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2666 IC=+0.035 PNL=+174.44€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.127 > 0.02 con n=489 PNL=+188.29€
  - _Datos_: n=489 IC=+0.127 PNL=+188.29€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=131 IC=-0.049 PNL=+33.33€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=131 IC=-0.049 PNL=+33.33€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.450 > 0.1 con n=870 PNL=+849.21€
  - _Datos_: n=870 IC=+0.450 PNL=+849.21€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=5888 IC=+0.048 PNL=+693.43€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=5888 IC=+0.048 PNL=+693.43€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.189 > 0.1 con n=1912 PNL=+949.91€
  - _Datos_: n=1912 IC=+0.189 PNL=+949.91€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.120 < -0.1 con n=127 PNL=+18.93€
  - _Datos_: n=127 IC=-0.120 PNL=+18.93€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=1119 IC=+0.044 PNL=+125.20€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1119 IC=+0.044 PNL=+125.20€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=49 IC=-0.108 PNL=+7.40€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=49 IC=-0.108 PNL=+7.40€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.127 > 0.1 con n=215 PNL=+63.77€
  - _Datos_: n=215 IC=+0.127 PNL=+63.77€

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
  - _Estado_: n=11675 IC=-0.141 PNL=+611.13€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=11675 IC=-0.141 PNL=+611.13€

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
  - _Estado_: n=1310 IC=+0.141 PNL=+702.80€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=1310 IC=+0.141 PNL=+702.80€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.170 > 0.08 con n=1179 PNL=+633.15€
  - _Datos_: n=1179 IC=+0.170 PNL=+633.15€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=2019 IC=+0.015 PNL=+41.32€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2019 IC=+0.015 PNL=+41.32€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.081 > 0.08 con n=1369 PNL=+739.70€
  - _Datos_: n=1369 IC=+0.081 PNL=+739.70€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.197 > 0.08 con n=315 PNL=+151.41€
  - _Datos_: n=315 IC=+0.197 PNL=+151.41€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.239 < -0.1 con n=1202 PNL=-165.24€
  - _Datos_: n=1202 IC=-0.239 PNL=-165.24€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=3367 IC=+0.141 PNL=+1971.43€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=3367 IC=+0.141 PNL=+1971.43€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.127 > 0.08 con n=57 PNL=+24.53€
  - _Datos_: n=57 IC=+0.127 PNL=+24.53€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=1337 IC=+0.035 PNL=+262.03€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1337 IC=+0.035 PNL=+262.03€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.186 > 0.08 con n=1206 PNL=+823.08€
  - _Datos_: n=1206 IC=+0.186 PNL=+823.08€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=1988 IC=-0.042 PNL=+468.59€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1988 IC=-0.042 PNL=+468.59€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.097 > 0.08 con n=422 PNL=-44.45€
  - _Datos_: n=422 IC=+0.097 PNL=-44.45€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.227 > 0.08 con n=2487 PNL=-255.07€
  - _Datos_: n=2487 IC=+0.227 PNL=-255.07€

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 24/40 ops en el filtro definido (IC actual=+0.038 PNL=+7.24€)
  - _Datos_: n=24 IC=+0.038 PNL=+7.24€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.097 n=584) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=584 IC=+0.097 PNL=+157.34€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.332 > 0.08 con n=159 PNL=+69.03€
  - _Datos_: n=159 IC=+0.332 PNL=+69.03€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.418 n=350) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=350 IC=+0.418 PNL=+491.48€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=6215 IC=+0.162 PNL=-852.72€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=6215 IC=+0.162 PNL=-852.72€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.217 > 0.1 con n=90 PNL=+57.75€
  - _Datos_: n=90 IC=+0.217 PNL=+57.75€
