# Hipótesis automáticas — 2026-08-20 15:04 UTC
_Generado por shadow_postmortem.py sobre 90308 resoluciones (PNL=+8228.57€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.365` → IC=-0.150 (n=78)

  - _Acción_: SKIP cuando `py_entrada` < 0.365
  - _Potencial_: sin este filtro IC_bueno=+0.230 (n=161)

- **FILTRO** `banda_hit_calibrado` < `0.616` → IC=-0.205 (n=59)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.616
  - _Potencial_: sin este filtro IC_bueno=+0.209 (n=180)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.377 (n=63)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=215)

- **PATRÓN** `py_entrada` > `0.365` → IC=+0.230 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.365 (IC base=+0.106)

- **PATRÓN** `n_total_lado` > `75.0` → IC=+0.223 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 75.0 (IC base=+0.106)

- **PATRÓN** `banda_hit_calibrado` > `0.616` → IC=+0.209 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.616 (IC base=+0.106)

- **PATRÓN** `banda_z` > `8.976` → IC=+0.167 (n=82)

  - _Acción_: Kelly boost +0.83€ cuando `banda_z` > 8.976 (IC base=+0.106)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.129 (n=184)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.106)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.136 (n=215)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.5 (IC base=+0.018)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `banda_hit_calibrado` < `0.6206` → IC=-0.151 (n=41)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6206
  - _Potencial_: sin este filtro IC_bueno=+0.261 (n=86)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.338 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.126 (n=113)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.261 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.128)

- **PATRÓN** `n_ballena_banda` > `26.0` → IC=+0.152 (n=87)

  - _Acción_: Kelly boost +0.76€ cuando `n_ballena_banda` > 26.0 (IC base=+0.128)

- **PATRÓN** `n_total_lado` > `84.0` → IC=+0.261 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 84.0 (IC base=+0.128)

- **PATRÓN** `banda_hit_calibrado` > `0.8088` → IC=+0.273 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8088 (IC base=+0.128)

- **PATRÓN** `ballenas_wallet_edge_medio` > `3.404` → IC=+0.167 (n=43)

  - _Acción_: Kelly boost +0.83€ cuando `ballenas_wallet_edge_medio` > 3.404 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.167 (n=70)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 11.0 (IC base=+0.128)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.126 (n=113)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.495 (IC base=+0.013)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.335` → IC=-0.267 (n=28)

  - _Acción_: SKIP cuando `py_entrada` < 0.335
  - _Potencial_: sin este filtro IC_bueno=+0.198 (n=84)

- **FILTRO** `banda_hit_calibrado` < `0.6274` → IC=-0.210 (n=36)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6274
  - _Potencial_: sin este filtro IC_bueno=+0.218 (n=76)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.144 (n=88)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.353 (n=32)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.134 (n=69)

- **FILTRO** `n_ballena_banda` < `30.0` → IC=-0.128 (n=49)

  - _Acción_: SKIP cuando `n_ballena_banda` < 30.0
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=52)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=86)

- **PATRÓN** `py_entrada` > `0.335` → IC=+0.198 (n=84)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.335 (IC base=+0.079)

- **PATRÓN** `banda_hit_calibrado` > `0.6274` → IC=+0.218 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6274 (IC base=+0.079)

- **PATRÓN** `banda_z` > `8.673` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.673 (IC base=+0.079)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.144 (n=88)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.02 (IC base=+0.079)

- **PATRÓN** `libro_liquidez` > `847.8323` → IC=+0.128 (n=84)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 847.8323 (IC base=+0.079)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.495 (IC base=-0.024)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `153.4` → IC=-0.259 (n=1211)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 153.4
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=3636)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `n_ballenas` < `4.0` → IC=-0.189 (n=310)

  - _Acción_: SKIP cuando `n_ballenas` < 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=162)

- **FILTRO** `restante_s_al_confirmar` < `123.0` → IC=-0.375 (n=118)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 123.0
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=354)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` > `641.05` → IC=-0.246 (n=128)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` > 641.05
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=387)

- **FILTRO** `restante_s_al_confirmar` < `511.01` → IC=-0.155 (n=169)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 511.01
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=346)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `20.43` → IC=-0.492 (n=131)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 20.43
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=393)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `186.65` → IC=-0.130 (n=409)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 186.65
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=833)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `168.27` → IC=-0.319 (n=318)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 168.27
  - _Potencial_: sin este filtro IC_bueno=-0.161 (n=646)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.7` → IC=+0.181 (n=3090)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.7 (IC base=+0.094)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.165 (n=1243)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.094)

- **PATRÓN** `libro_liquidez` > `2371.8427` → IC=+0.169 (n=1200)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2371.8427 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.145 (n=1908)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.151 (n=2427)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 7.0 (IC base=+0.140)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.271 (n=1747)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.188 (n=2200)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.02 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `4171.2658` → IC=+0.179 (n=910)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 4171.2658 (IC base=+0.140)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.210 (n=419)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.785` → IC=+0.366 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.785 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.202 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.207 (n=357)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.197 (n=285)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 11.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.301 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.198 (n=511)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.196)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.148 (n=424)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.156 (n=370)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 15.0 (IC base=+0.133)

- **PATRÓN** `py_entrada` > `0.555` → IC=+0.147 (n=448)

  - _Acción_: Kelly boost +0.73€ cuando `py_entrada` > 0.555 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `5033.4098` → IC=+0.165 (n=195)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 5033.4098 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.139 (n=142)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.204 (n=167)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.139)

- **PATRÓN** `py_entrada` < `0.395` → IC=+0.210 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.395 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `5296.1268` → IC=+0.173 (n=218)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 5296.1268 (IC base=+0.139)

### FAVORITO_CONFIRMADO#ETH#15min
- **PATRÓN** `hora_utc` < `11.0` → IC=+0.149 (n=525)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 11.0 (IC base=+0.123)

- **PATRÓN** `py_entrada` > `0.7` → IC=+0.301 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.7 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.301 (n=310)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.293)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.293 (n=297)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.293)

- **PATRÓN** `py_entrada` < `0.195` → IC=+0.417 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.195 (IC base=+0.293)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.292 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `1762.5654` → IC=+0.309 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1762.5654 (IC base=+0.293)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.150 (n=292)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.173 (n=249)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 15.0 (IC base=+0.145)

- **PATRÓN** `py_entrada` > `0.655` → IC=+0.241 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.655 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.148 (n=353)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.02 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `2119.7584` → IC=+0.169 (n=282)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2119.7584 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `4420.281` → IC=+0.160 (n=139)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 4420.281 (IC base=+0.090)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=642)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.200 (n=547)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.407 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.263 (n=133)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.216)

- **PATRÓN** `py_entrada` < `0.215` → IC=+0.385 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.215 (IC base=+0.216)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.232 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `749.7149` → IC=+0.238 (n=395)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 749.7149 (IC base=+0.216)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `19.0` → IC=+0.260 (n=77)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 19.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.189 (n=101)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 8.0 (IC base=+0.186)

- **PATRÓN** `py_entrada` > `0.725` → IC=+0.361 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.186)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.211 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.186)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.218 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.107)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.160 (n=260)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.02 (IC base=+0.107)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `11.0` → IC=-0.297 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.216 (n=72)

- **FILTRO** `py_entrada` > `0.845` → IC=-0.379 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.845
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=103)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=3066)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.189 (n=2708)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 15.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.184 (n=1153)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` < 0.7 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.200 (n=1021)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.183)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.169 (n=696)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 15.0 (IC base=+0.158)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.179 (n=756)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.74 (IC base=+0.158)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `py_entrada` > `0.795` → IC=-0.393 (n=26)

  - _Acción_: SKIP cuando `py_entrada` > 0.795
  - _Potencial_: sin este filtro IC_bueno=-0.242 (n=29)

- **FILTRO** `libro_liquidez` < `8070.1547` → IC=-0.337 (n=41)

  - _Acción_: SKIP cuando `libro_liquidez` < 8070.1547
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=14)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.417 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.326)

- **PATRÓN** `py_entrada` > `0.835` → IC=+0.370 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.835 (IC base=+0.326)

- **PATRÓN** `libro_liquidez` > `2916.5858` → IC=+0.343 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2916.5858 (IC base=+0.326)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.160 (n=785)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.159 (n=685)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 15.0 (IC base=+0.154)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.174 (n=262)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.7 (IC base=+0.154)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.162 (n=436)

  - _Acción_: Kelly boost +0.81€ cuando `py_entrada` > 0.73 (IC base=+0.154)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.229 (n=692)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.235 (n=605)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.226)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.322 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.226)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min
- **FILTRO** `hora_utc` < `18.0` → IC=-0.217 (n=58)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=20)

- **FILTRO** `py_entrada` > `0.845` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `py_entrada` > 0.845
  - _Potencial_: sin este filtro IC_bueno=-0.156 (n=59)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.207 (n=251)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.205 (n=323)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.186)

- **PATRÓN** `py_entrada` < `0.72` → IC=+0.201 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.72 (IC base=+0.186)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.440 (n=147)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.422)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.429 (n=138)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.422)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.441 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.422)

- **PATRÓN** `libro_liquidez` > `3567.0608` → IC=+0.444 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3567.0608 (IC base=+0.422)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.426 (n=52)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.421)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.422 (n=49)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.421)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.444 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.421)

- **PATRÓN** `libro_liquidez` > `10601.0016` → IC=+0.452 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10601.0016 (IC base=+0.421)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `4.0` → IC=+0.422 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.401)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.406 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.401)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.409 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.401)

- **PATRÓN** `libro_liquidez` > `2048.1399` → IC=+0.427 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2048.1399 (IC base=+0.401)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.441 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.418)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.406 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.418)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.198 (n=2176)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.188 (n=4248)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 11.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.216 (n=4492)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.188)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.284 (n=322)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.242)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.294 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.242)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` < `11.0` → IC=+0.156 (n=742)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 11.0 (IC base=+0.148)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.196 (n=425)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.76 (IC base=+0.148)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.241 (n=985)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.237 (n=671)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.236)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.298 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.236)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.243 (n=341)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.232)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.235 (n=379)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.232)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.264 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.232)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.226 (n=367)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.225 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.188)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.208 (n=772)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.137)

- **PATRÓN** `restante_min` < `3.87` → IC=+0.153 (n=735)

  - _Acción_: Kelly boost +0.76€ cuando `restante_min` < 3.87 (IC base=+0.137)

- **PATRÓN** `restante_min` > `4.91` → IC=+0.179 (n=767)

  - _Acción_: Kelly boost +0.89€ cuando `restante_min` > 4.91 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.147 (n=2234)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 17.0 (IC base=+0.137)

- **PATRÓN** `lag_apertura_s` < `5.37` → IC=+0.183 (n=730)

  - _Acción_: Kelly boost +0.92€ cuando `lag_apertura_s` < 5.37 (IC base=+0.137)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.226 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.149)

- **PATRÓN** `restante_min` < `3.78` → IC=+0.162 (n=362)

  - _Acción_: Kelly boost +0.81€ cuando `restante_min` < 3.78 (IC base=+0.149)

- **PATRÓN** `restante_min` > `4.88` → IC=+0.189 (n=397)

  - _Acción_: Kelly boost +0.95€ cuando `restante_min` > 4.88 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.150 (n=1131)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.162 (n=980)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 15.0 (IC base=+0.149)

- **PATRÓN** `lag_apertura_s` < `6.97` → IC=+0.192 (n=362)

  - _Acción_: Kelly boost +0.96€ cuando `lag_apertura_s` < 6.97 (IC base=+0.149)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.190 (n=391)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.37 (IC base=+0.124)

- **PATRÓN** `restante_min` < `3.94` → IC=+0.141 (n=371)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` < 3.94 (IC base=+0.124)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.174 (n=382)

  - _Acción_: Kelly boost +0.87€ cuando `restante_min` > 4.95 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.136 (n=1131)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 17.0 (IC base=+0.124)

- **PATRÓN** `lag_apertura_s` < `3.26` → IC=+0.181 (n=371)

  - _Acción_: Kelly boost +0.90€ cuando `lag_apertura_s` < 3.26 (IC base=+0.124)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.309 (n=449)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.301)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.309 (n=406)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.301)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.379 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.8 (IC base=+0.301)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.295 (n=169)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.276)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.280 (n=175)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.276)

- **PATRÓN** `py_entrada` < `0.725` → IC=+0.294 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.725 (IC base=+0.276)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.347 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.276)

- **PATRÓN** `libro_liquidez` > `5707.6363` → IC=+0.331 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5707.6363 (IC base=+0.276)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.314 (n=218)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.302)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.315 (n=214)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.302)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.407 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.302)

- **PATRÓN** `libro_liquidez` > `2591.029` → IC=+0.345 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2591.029 (IC base=+0.302)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.373 (n=53)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.371)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.415 (n=45)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.371)

- **PATRÓN** `py_entrada` > `0.855` → IC=+0.429 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.855 (IC base=+0.371)

- **PATRÓN** `libro_liquidez` > `866.0223` → IC=+0.387 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 866.0223 (IC base=+0.371)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.414 (n=173)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.412)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.431 (n=187)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.412)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.419 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.412)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.429 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.412)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.409 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.412)

- **PATRÓN** `libro_liquidez` > `1864.6918` → IC=+0.425 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1864.6918 (IC base=+0.412)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.407 (n=73)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.409)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.441 (n=83)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.409)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.421 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.409)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.424 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.409)

- **PATRÓN** `libro_liquidez` > `5849.2071` → IC=+0.431 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5849.2071 (IC base=+0.409)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.423 (n=63)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.413)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.411 (n=77)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.413)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.422 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.413)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.421 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.413)

- **PATRÓN** `libro_liquidez` > `1957.89` → IC=+0.436 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1957.89 (IC base=+0.413)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.318 (n=75)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.275)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.407 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.275)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.284 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.275)

- **PATRÓN** `libro_liquidez` > `788.6906` → IC=+0.277 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 788.6906 (IC base=+0.275)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.318 (n=75)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.275)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.407 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.275)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.284 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.275)

- **PATRÓN** `libro_liquidez` > `788.6906` → IC=+0.277 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 788.6906 (IC base=+0.275)

### GBM_LATE_15M
- **PATRÓN** `ibs_20min` > `0.9714` → IC=+0.272 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9714 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` > `0.1095` → IC=+0.256 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1095 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` < `0.6695` → IC=+0.232 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6695 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.784` → IC=+0.228 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.784 (IC base=+0.095)

- **PATRÓN** `volumen_regimen` < `0.7215` → IC=+0.232 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7215 (IC base=+0.095)

- **PATRÓN** `volumen_regimen` > `1.1082` → IC=+0.250 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1082 (IC base=+0.095)

- **PATRÓN** `volumen_spike_ratio` > `1.5121` → IC=+0.127 (n=816)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.5121 (IC base=+0.095)

- **PATRÓN** `ibs_20min` < `0.3916` → IC=+0.144 (n=1627)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.3916 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` < `0.4095` → IC=+0.142 (n=654)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.4095 (IC base=+0.059)

- **PATRÓN** `volumen_regimen` < `0.8624` → IC=+0.140 (n=367)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.8624 (IC base=+0.059)

- **PATRÓN** `volumen_regimen` > `0.6895` → IC=+0.136 (n=492)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.6895 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.3263` → IC=+0.289 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3263 (IC base=+0.059)

- **PATRÓN** `volumen_spike_ratio` < `1.6765` → IC=+0.234 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6765 (IC base=+0.059)

- **PATRÓN** `volumen_spike_ratio` > `2.7406` → IC=+0.223 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7406 (IC base=+0.059)

- **PATRÓN** `ballena_activa_n` < `221.0` → IC=+0.254 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 221.0 (IC base=+0.059)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.170 (n=195)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0071 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.163 (n=295)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 11.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.304 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.349` → IC=+0.343 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.349 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.154 (n=325)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.06 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.319 (n=136)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.287)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.329 (n=68)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.1819` → IC=+0.329 (n=179)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1819 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.293 (n=186)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.287)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.297 (n=205)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.287)

- **PATRÓN** `ibs_20min` < `0.5765` → IC=+0.330 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5765 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` < `0.0645` → IC=+0.324 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0645 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.339 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.287)

- **PATRÓN** `volumen_spike_ratio` < `1.7987` → IC=+0.343 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7987 (IC base=+0.287)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.334 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `1982.2745` → IC=+0.329 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1982.2745 (IC base=+0.287)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.385 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 36.0 (IC base=+0.287)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0019` → IC=+0.330 (n=51)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0019 (IC base=+0.250)

- **PATRÓN** `drift_60min` |x|≤ `0.3276` → IC=+0.260 (n=152)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3276 (IC base=+0.250)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.287 (n=158)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.250)

- **PATRÓN** `ibs_20min` > `0.5283` → IC=+0.273 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5283 (IC base=+0.250)

- **PATRÓN** `dist_vwap_pct` > `0.3423` → IC=+0.309 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3423 (IC base=+0.250)

- **PATRÓN** `dist_vwap_pct` < `0.7257` → IC=+0.255 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7257 (IC base=+0.250)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.619` → IC=+0.310 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.619 (IC base=+0.250)

- **PATRÓN** `volumen_regimen` < `0.6694` → IC=+0.274 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6694 (IC base=+0.250)

- **PATRÓN** `volumen_regimen` > `1.1457` → IC=+0.261 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1457 (IC base=+0.250)

- **PATRÓN** `volumen_pendiente_norm` < `0.1144` → IC=+0.287 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1144 (IC base=+0.250)

- **PATRÓN** `volumen_pendiente_norm` > `0.3178` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3178 (IC base=+0.250)

- **PATRÓN** `volumen_spike_ratio` < `1.4256` → IC=+0.300 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4256 (IC base=+0.250)

- **PATRÓN** `volumen_spike_ratio` > `1.7306` → IC=+0.259 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7306 (IC base=+0.250)

- **PATRÓN** `libro_liquidez` > `11338.6336` → IC=+0.267 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11338.6336 (IC base=+0.250)

- **PATRÓN** `ballena_activa_n` < `425.0` → IC=+0.295 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 425.0 (IC base=+0.250)

- **PATRÓN** `sigma_h` < `0.0021` → IC=+0.192 (n=128)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0021 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.2121` → IC=+0.171 (n=253)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.2121 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.165 (n=204)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 12.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.147 (n=298)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 18.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.3777` → IC=+0.202 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3777 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` < `0.1544` → IC=+0.172 (n=285)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.1544 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.172` → IC=+0.246 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.172 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.2637` → IC=+0.152 (n=288)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.2637 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `0.6809` → IC=+0.152 (n=257)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6809 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.1155` → IC=+0.259 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1155 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.5799` → IC=+0.235 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5799 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `11633.3746` → IC=+0.162 (n=131)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 11633.3746 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `205.0` → IC=+0.235 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 205.0 (IC base=+0.144)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.182 (n=177)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0071 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.0858` → IC=+0.136 (n=171)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.0858 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.209 (n=146)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.273 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.912` → IC=+0.287 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.912 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.147 (n=432)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.06 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `1917.67` → IC=+0.146 (n=176)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 1917.67 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.136 (n=64)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 23.0 (IC base=+0.129)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.328 (n=85)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.0858` → IC=+0.305 (n=85)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0858 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.289 (n=169)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.285)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.292 (n=262)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.285)

- **PATRÓN** `ibs_20min` < `0.5027` → IC=+0.312 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5027 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.013` → IC=+0.286 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.013 (IC base=+0.285)

- **PATRÓN** `volumen_pendiente_norm` > `0.3362` → IC=+0.403 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3362 (IC base=+0.285)

- **PATRÓN** `volumen_spike_ratio` < `4.5585` → IC=+0.267 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 4.5585 (IC base=+0.285)

- **PATRÓN** `volumen_spike_ratio` > `2.9495` → IC=+0.286 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9495 (IC base=+0.285)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.287 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.285)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `ibs_20min` > `0.8764` → IC=-0.196 (n=133)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8764
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=402)

- **PATRÓN** `ibs_20min` > `0.7614` → IC=+0.127 (n=65)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` > 0.7614 (IC base=+0.016)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.129` → IC=+0.144 (n=43)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 10.129 (IC base=+0.016)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` > `4.603` → IC=-0.132 (n=207)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.603
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=705)

- **FILTRO** `volumen_pendiente_norm` < `0.0964` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.0964
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

- **FILTRO** `volumen_spike_ratio` > `1.6234` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.6234
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

- **FILTRO** `volumen_spike_ratio` < `2.8678` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 2.8678
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=6)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.188 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0057 (IC base=+0.100)

- **PATRÓN** `drift_60min` |x|≤ `0.2929` → IC=+0.159 (n=39)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2929 (IC base=+0.100)

- **PATRÓN** `hora_utc` > `23.0` → IC=+0.333 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 23.0 (IC base=+0.100)

- **PATRÓN** `ibs_20min` > `0.375` → IC=+0.207 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.375 (IC base=+0.100)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.149 (n=35)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.100)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `sigma_ewma_delta_pct` > `7.98` → IC=-0.143 (n=96)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.98
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=717)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.093` → IC=+0.139 (n=59)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 8.093 (IC base=-0.034)

- **PATRÓN** `volumen_regimen` < `0.7863` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.7863 (IC base=-0.034)

- **PATRÓN** `dist_vwap_pct` < `0.3335` → IC=+0.226 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3335 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` < `0.6966` → IC=+0.254 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6966 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` > `1.1355` → IC=+0.229 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1355 (IC base=+0.008)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.154 (n=616)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.007 (IC base=+0.050)

- **PATRÓN** `ibs_20min` > `0.9429` → IC=+0.249 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9429 (IC base=+0.050)

- **PATRÓN** `dist_vwap_pct` > `0.4298` → IC=+0.244 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4298 (IC base=+0.050)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.298` → IC=+0.127 (n=1116)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 2.298 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` > `1.1718` → IC=+0.153 (n=174)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 1.1718 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` > `0.3343` → IC=+0.221 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3343 (IC base=+0.050)

- **PATRÓN** `volumen_spike_ratio` > `2.7927` → IC=+0.172 (n=349)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.7927 (IC base=+0.050)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.271 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 85.0 (IC base=+0.050)

- **PATRÓN** `ibs_20min` < `0.1049` → IC=+0.166 (n=929)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.1049 (IC base=+0.043)

- **PATRÓN** `dist_vwap_pct` < `0.264` → IC=+0.184 (n=552)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.264 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` > `1.2432` → IC=+0.204 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2432 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.2757` → IC=+0.340 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2757 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` > `3.4261` → IC=+0.307 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.4261 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.233 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 69.0 (IC base=+0.043)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `sigma_ewma_delta_pct` > `4.936` → IC=-0.214 (n=110)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.936
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=552)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.418` → IC=+0.177 (n=128)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 3.418 (IC base=-0.013)

- **PATRÓN** `volumen_pendiente_norm` > `0.0542` → IC=+0.224 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0542 (IC base=-0.013)

- **PATRÓN** `volumen_spike_ratio` > `2.317` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.317 (IC base=-0.013)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` < `0.0672` → IC=-0.173 (n=105)

  - _Acción_: SKIP cuando `ibs_20min` < 0.0672
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=317)

- **PATRÓN** `dist_vwap_pct` > `0.5859` → IC=+0.140 (n=23)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.5859 (IC base=-0.035)

- **PATRÓN** `volumen_regimen` < `0.5591` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.5591 (IC base=-0.022)

- **PATRÓN** `volumen_regimen` > `1.1068` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 1.1068 (IC base=-0.022)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.292 (n=123)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0075 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.0614` → IC=+0.222 (n=124)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0614 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.263 (n=137)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.294 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.923` → IC=+0.303 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.923 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` < `0.1444` → IC=+0.187 (n=266)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.1444 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.425` → IC=+0.221 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.425 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` < `2.0881` → IC=+0.167 (n=127)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.0881 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `3.9033` → IC=+0.207 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.9033 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.198 (n=405)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.06 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `1914.9184` → IC=+0.206 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1914.9184 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.224 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 31.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.402 (n=151)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.372)

- **PATRÓN** `drift_60min` |x|≤ `0.1764` → IC=+0.378 (n=113)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1764 (IC base=+0.372)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.397 (n=154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.372)

- **PATRÓN** `ibs_20min` < `0.3009` → IC=+0.389 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3009 (IC base=+0.372)

- **PATRÓN** `ibs_20min` > `0.0514` → IC=+0.369 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0514 (IC base=+0.372)

- **PATRÓN** `volumen_pendiente_norm` < `0.2282` → IC=+0.403 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2282 (IC base=+0.372)

- **PATRÓN** `volumen_pendiente_norm` > `0.1384` → IC=+0.389 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1384 (IC base=+0.372)

- **PATRÓN** `volumen_spike_ratio` < `2.9764` → IC=+0.444 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.9764 (IC base=+0.372)

- **PATRÓN** `libro_liquidez` > `1874.461` → IC=+0.415 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1874.461 (IC base=+0.372)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.136 (n=64)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=215)

- **FILTRO** `dist_vwap_pct` < `0.6861` → IC=-0.227 (n=42)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.6861
  - _Potencial_: sin este filtro IC_bueno=+0.300 (n=3)

- **FILTRO** `volumen_regimen` > `1.0124` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.0124
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=30)

- **FILTRO** `libro_liquidez` < `8738.1618` → IC=-0.190 (n=69)

  - _Acción_: SKIP cuando `libro_liquidez` < 8738.1618
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=210)

- **FILTRO** `dist_vwap_pct` < `0.0941` → IC=-0.136 (n=53)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0941
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=15)

- **FILTRO** `volumen_regimen` > `0.9083` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.9083
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=45)

- **FILTRO** `volumen_regimen` < `0.6698` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.6698
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=46)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=750)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.45` → IC=-0.163 (n=173)

  - _Acción_: SKIP cuando `ibs_20min` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=173)

- **FILTRO** `dist_vwap_pct` > `0.1326` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1326
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=44)

- **FILTRO** `volumen_pendiente_norm` < `0.1045` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.1045
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **PATRÓN** `ibs_20min` > `0.45` → IC=+0.146 (n=173)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.45 (IC base=-0.009)

- **PATRÓN** `dist_vwap_pct` > `0.1881` → IC=+0.182 (n=42)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1881 (IC base=-0.009)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.337 (n=157)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0066 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.182 (n=130)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.169)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.233 (n=129)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.9123` → IC=+0.249 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9123 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.4977` → IC=+0.294 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4977 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.172` → IC=+0.247 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.172 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` > `0.8248` → IC=+0.201 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8248 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.3097` → IC=+0.261 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3097 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.6893` → IC=+0.198 (n=127)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.6893 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.5739` → IC=+0.174 (n=130)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.5739 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.184 (n=353)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.01 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `2502.6824` → IC=+0.193 (n=307)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2502.6824 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.379 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 57.0 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.277 (n=321)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0071 (IC base=+0.258)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.260 (n=364)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.258)

- **PATRÓN** `drift_60min` |x|≤ `0.3574` → IC=+0.268 (n=364)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3574 (IC base=+0.258)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.310 (n=182)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.258)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.261 (n=132)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.258)

- **PATRÓN** `ibs_20min` < `0.2804` → IC=+0.333 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2804 (IC base=+0.258)

- **PATRÓN** `dist_vwap_pct` < `0.1236` → IC=+0.266 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1236 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.471` → IC=+0.262 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.471 (IC base=+0.258)

- **PATRÓN** `volumen_regimen` > `1.2624` → IC=+0.298 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2624 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` > `0.2628` → IC=+0.389 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2628 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` > `3.0855` → IC=+0.308 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.0855 (IC base=+0.258)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.188 (n=110)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 48.0 (IC base=+0.258)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.206 (n=689)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.163 (n=509)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.173 (n=583)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 6.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.913` → IC=+0.260 (n=1012)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.913 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.5895` → IC=+0.239 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5895 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.004` → IC=+0.266 (n=720)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.004 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` > `0.8611` → IC=+0.168 (n=580)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 0.8611 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.1069` → IC=+0.175 (n=527)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1069 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `3.0487` → IC=+0.133 (n=1280)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 3.0487 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.5005` → IC=+0.134 (n=1280)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.5005 (IC base=+0.150)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.161 (n=1533)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.04 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `3088.6936` → IC=+0.195 (n=506)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 3088.6936 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.217 (n=1413)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.3003` → IC=+0.207 (n=1410)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3003 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.249 (n=712)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.3878` → IC=+0.264 (n=1410)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3878 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` < `0.2595` → IC=+0.187 (n=1208)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.2595 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.6` → IC=+0.220 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.6 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.255` → IC=+0.200 (n=1416)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.255 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` < `1.2288` → IC=+0.174 (n=1110)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 1.2288 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `0.856` → IC=+0.185 (n=740)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 0.856 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2587` → IC=+0.258 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2587 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `1.9864` → IC=+0.199 (n=539)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.9864 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `2.9516` → IC=+0.231 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9516 (IC base=+0.200)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.197 (n=163)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 30.0 (IC base=+0.200)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.210 (n=153)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.222 (n=131)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.333 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.377` → IC=+0.359 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.377 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.1402` → IC=+0.150 (n=78)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.1402 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `1.4192` → IC=+0.134 (n=260)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.4192 (IC base=+0.152)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.186 (n=269)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.06 (IC base=+0.152)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.302 (n=94)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.291)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.316 (n=47)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.2108` → IC=+0.332 (n=123)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2108 (IC base=+0.291)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.315 (n=144)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.291)

- **PATRÓN** `ibs_20min` < `0.4177` → IC=+0.323 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4177 (IC base=+0.291)

- **PATRÓN** `volumen_pendiente_norm` < `0.0686` → IC=+0.323 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0686 (IC base=+0.291)

- **PATRÓN** `volumen_spike_ratio` < `1.8747` → IC=+0.389 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8747 (IC base=+0.291)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.374 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `1966.1335` → IC=+0.378 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1966.1335 (IC base=+0.291)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.002` → IC=+0.245 (n=53)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.002 (IC base=+0.211)

- **PATRÓN** `sigma_h` > `0.0039` → IC=+0.257 (n=72)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0039 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.278 (n=142)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.5545` → IC=+0.280 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5545 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.1661` → IC=+0.292 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1661 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.037` → IC=+0.274 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.037 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` > `0.9205` → IC=+0.257 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9205 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` < `0.1173` → IC=+0.213 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1173 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.3178` → IC=+0.326 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3178 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.4524` → IC=+0.278 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4524 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.8508` → IC=+0.224 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8508 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `7185.4978` → IC=+0.241 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7185.4978 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.200 (n=268)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.1928` → IC=+0.214 (n=236)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1928 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.228 (n=189)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` < `0.3142` → IC=+0.241 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3142 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` < `0.251` → IC=+0.201 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.251 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.625` → IC=+0.270 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.625 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` < `0.627` → IC=+0.239 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.627 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.083` → IC=+0.239 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.083 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` < `1.8414` → IC=+0.273 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8414 (IC base=+0.185)

- **PATRÓN** `libro_liquidez` > `13046.7768` → IC=+0.217 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13046.7768 (IC base=+0.185)

- **PATRÓN** `ballena_activa_n` < `203.0` → IC=+0.241 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 203.0 (IC base=+0.185)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.198 (n=104)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0076 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.1433` → IC=+0.157 (n=208)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1433 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.156 (n=120)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 16.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.212 (n=109)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.292 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.804` → IC=+0.328 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.804 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` < `0.2317` → IC=+0.134 (n=249)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` < 0.2317 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.0183` → IC=+0.199 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0183 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `3.9092` → IC=+0.138 (n=114)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 3.9092 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.175 (n=244)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.04 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `1970.8484` → IC=+0.160 (n=104)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 1970.8484 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.339 (n=54)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.302)

- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.304 (n=54)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0073 (IC base=+0.302)

- **PATRÓN** `drift_60min` |x|≤ `0.2366` → IC=+0.326 (n=142)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2366 (IC base=+0.302)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.329 (n=109)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.302)

- **PATRÓN** `ibs_20min` < `0.3486` → IC=+0.323 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3486 (IC base=+0.302)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.578` → IC=+0.311 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.578 (IC base=+0.302)

- **PATRÓN** `volumen_pendiente_norm` > `0.3308` → IC=+0.375 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3308 (IC base=+0.302)

- **PATRÓN** `volumen_spike_ratio` < `4.3528` → IC=+0.285 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 4.3528 (IC base=+0.302)

- **PATRÓN** `volumen_spike_ratio` > `2.1697` → IC=+0.312 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1697 (IC base=+0.302)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.255 (n=145)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.1163` → IC=+0.318 (n=64)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1163 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.256 (n=133)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.233)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.241 (n=137)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` > `0.5341` → IC=+0.303 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5341 (IC base=+0.233)

- **PATRÓN** `dist_vwap_pct` > `0.1426` → IC=+0.255 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1426 (IC base=+0.233)

- **PATRÓN** `dist_vwap_pct` < `0.2993` → IC=+0.250 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2993 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.112` → IC=+0.382 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.112 (IC base=+0.233)

- **PATRÓN** `volumen_regimen` > `0.7026` → IC=+0.258 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7026 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.1047` → IC=+0.300 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1047 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` < `1.5375` → IC=+0.250 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5375 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.3878` → IC=+0.281 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3878 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.236 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.233)

- **PATRÓN** `ballena_activa_n` < `236.0` → IC=+0.211 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 236.0 (IC base=+0.233)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.211 (n=261)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.165)

- **PATRÓN** `drift_60min` |x|≤ `0.2955` → IC=+0.173 (n=261)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2955 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.182 (n=265)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` < `0.4013` → IC=+0.239 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4013 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` < `0.2323` → IC=+0.181 (n=290)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.2323 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.853` → IC=+0.273 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.853 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` < `1.2252` → IC=+0.184 (n=261)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 1.2252 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` > `0.6199` → IC=+0.165 (n=261)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.6199 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` < `0.1688` → IC=+0.158 (n=159)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` < 0.1688 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.1088` → IC=+0.176 (n=66)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1088 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `1.9099` → IC=+0.220 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9099 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `3329.707` → IC=+0.165 (n=174)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 3329.707 (IC base=+0.165)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **FILTRO** `ibs_20min` > `0.5` → IC=-0.242 (n=91)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.212 (n=279)

- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.177 (n=125)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0065 (IC base=+0.066)

- **PATRÓN** `ibs_20min` > `0.8667` → IC=+0.202 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8667 (IC base=+0.066)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.947` → IC=+0.171 (n=150)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 3.947 (IC base=+0.066)

- **PATRÓN** `libro_liquidez` > `2853.2159` → IC=+0.141 (n=90)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2853.2159 (IC base=+0.066)

- **PATRÓN** `ballena_activa_n` < `32.0` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 32.0 (IC base=+0.066)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.226 (n=93)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.100)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.219 (n=126)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.100)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.212 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.906` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 6.906 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` > `0.8537` → IC=+0.142 (n=185)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.8537 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` > `0.0979` → IC=+0.158 (n=71)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.0979 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` > `2.4742` → IC=+0.173 (n=50)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.4742 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `2361.288` → IC=+0.172 (n=126)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2361.288 (IC base=+0.100)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.006` → IC=+0.229 (n=201)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.0938` → IC=+0.170 (n=101)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.0938 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=101)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.183 (n=118)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 6.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.241 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.4108` → IC=+0.209 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4108 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.396` → IC=+0.238 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.396 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `1.2177` → IC=+0.153 (n=301)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.2177 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` > `0.8308` → IC=+0.165 (n=201)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.8308 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.1883` → IC=+0.243 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1883 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.0105` → IC=+0.176 (n=177)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 2.0105 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.149 (n=311)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `2507.6219` → IC=+0.161 (n=269)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2507.6219 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.252 (n=268)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.007 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.279 (n=138)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.232)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.260 (n=119)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` < `0.1125` → IC=+0.344 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1125 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.642` → IC=+0.254 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.642 (IC base=+0.232)

- **PATRÓN** `volumen_regimen` > `0.6886` → IC=+0.259 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6886 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.2612` → IC=+0.337 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2612 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `3.1733` → IC=+0.303 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.1733 (IC base=+0.232)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.159 (n=86)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 41.0 (IC base=+0.232)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.167 (n=85)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0061 (IC base=+0.061)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.217 (n=118)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.061)

- **PATRÓN** `ibs_20min` > `0.5122` → IC=+0.123 (n=255)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` > 0.5122 (IC base=+0.061)

- **PATRÓN** `dist_vwap_pct` > `0.5433` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.5433 (IC base=+0.061)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.914` → IC=+0.267 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.914 (IC base=+0.061)

- **PATRÓN** `volumen_pendiente_norm` > `0.184` → IC=+0.178 (n=57)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.184 (IC base=+0.061)

- **PATRÓN** `ballena_activa_n` < `32.0` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 32.0 (IC base=+0.061)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.300 (n=78)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.056)

- **PATRÓN** `ibs_20min` < `0.2308` → IC=+0.146 (n=156)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.2308 (IC base=+0.056)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.614` → IC=+0.236 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.614 (IC base=+0.056)

- **PATRÓN** `volumen_spike_ratio` < `1.604` → IC=+0.177 (n=60)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.604 (IC base=+0.056)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.214 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.056)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **FILTRO** `hora_utc` < `11.0` → IC=-0.214 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=26)

- **FILTRO** `ibs_20min` < `0.2178` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2178
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=35)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.143 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 11.0 (IC base=-0.037)

- **PATRÓN** `ibs_20min` > `0.2178` → IC=+0.122 (n=35)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` > 0.2178 (IC base=-0.037)

- **PATRÓN** `libro_liquidez` > `6332.2628` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 6332.2628 (IC base=-0.037)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.245 (n=53)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.0923` → IC=+0.283 (n=21)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0923 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.167 (n=61)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 4.0 (IC base=+0.159)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.219 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` < `0.2407` → IC=+0.209 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2407 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.287` → IC=+0.346 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.287 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` < `1.2895` → IC=+0.182 (n=61)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 1.2895 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` > `0.7034` → IC=+0.161 (n=54)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.7034 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` > `0.091` → IC=+0.352 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.091 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` < `1.602` → IC=+0.340 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.602 (IC base=+0.159)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **FILTRO** `sigma_h` > `0.0045` → IC=-0.154 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0045
  - _Potencial_: sin este filtro IC_bueno=+0.211 (n=50)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.232 (n=39)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.217)

- **PATRÓN** `sigma_h` > `0.0028` → IC=+0.250 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0028 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.1812` → IC=+0.250 (n=30)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1812 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.382 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` > `0.9648` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9648 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` < `0.0952` → IC=+0.238 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0952 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.836` → IC=+0.460 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.836 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` < `0.6618` → IC=+0.382 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6618 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` > `1.1837` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1837 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.184` → IC=+0.342 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.184 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` < `2.3331` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3331 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `1.5527` → IC=+0.257 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5527 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `3088.7155` → IC=+0.232 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3088.7155 (IC base=+0.217)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.352 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.092)

- **PATRÓN** `drift_60min` |x|≤ `0.2707` → IC=+0.186 (n=49)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.2707 (IC base=+0.092)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.232 (n=39)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.092)

- **PATRÓN** `ibs_20min` < `0.529` → IC=+0.121 (n=56)

  - _Acción_: Kelly boost +0.60€ cuando `ibs_20min` < 0.529 (IC base=+0.092)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.121` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.121 (IC base=+0.092)

- **PATRÓN** `volumen_regimen` < `0.7011` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7011 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `9493.103` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9493.103 (IC base=+0.092)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` > `0.6154` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6154
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=67)

- **FILTRO** `dist_vwap_pct` > `0.177` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.177
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=72)

- **FILTRO** `volumen_pendiente_norm` > `0.0819` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0819
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=44)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.127 (n=57)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 14.0 (IC base=+0.023)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` > 1.0 (IC base=+0.023)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.989` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.989 (IC base=+0.023)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.006` → IC=+0.214 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.085)

- **PATRÓN** `ibs_20min` > `0.781` → IC=+0.143 (n=40)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.781 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.99` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.99 (IC base=+0.085)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=54)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.085)

- **PATRÓN** `ibs_20min` < `0.0773` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0773 (IC base=+0.029)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.221 (n=582)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.157 (n=852)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 15.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.147 (n=649)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 6.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` > `0.6571` → IC=+0.209 (n=1561)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6571 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `0.5323` → IC=+0.251 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5323 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.304` → IC=+0.233 (n=1141)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.304 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.8973` → IC=+0.132 (n=682)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.8973 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` > `1.2577` → IC=+0.136 (n=341)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 1.2577 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.175` → IC=+0.160 (n=427)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.175 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `3.0052` → IC=+0.129 (n=1436)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 3.0052 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `2.0293` → IC=+0.138 (n=957)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.0293 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.141 (n=1784)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.05 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `3013.6279` → IC=+0.188 (n=582)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 3013.6279 (IC base=+0.133)

- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.225 (n=1637)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0074 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.3194` → IC=+0.208 (n=1637)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3194 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.226 (n=593)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.5322` → IC=+0.268 (n=1637)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5322 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` < `0.4343` → IC=+0.184 (n=1247)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.4343 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.055` → IC=+0.232 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.055 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.498` → IC=+0.205 (n=1535)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.498 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` < `0.6076` → IC=+0.186 (n=386)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.6076 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `1.2185` → IC=+0.180 (n=386)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 1.2185 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2426` → IC=+0.242 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2426 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `1.9399` → IC=+0.203 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9399 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `2.8438` → IC=+0.217 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8438 (IC base=+0.200)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.210 (n=184)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.158 (n=276)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 11.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` > `0.9489` → IC=+0.289 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9489 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.154` → IC=+0.356 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.154 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2113` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.2113 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.159 (n=297)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.06 (IC base=+0.129)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.312 (n=136)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0063 (IC base=+0.287)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.287 (n=92)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.2086` → IC=+0.329 (n=179)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2086 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.293 (n=186)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.287)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.300 (n=138)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.287)

- **PATRÓN** `ibs_20min` < `0.5819` → IC=+0.339 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5819 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` < `0.0647` → IC=+0.312 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0647 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` > `0.23` → IC=+0.318 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.23 (IC base=+0.287)

- **PATRÓN** `volumen_spike_ratio` > `2.7667` → IC=+0.338 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7667 (IC base=+0.287)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.316 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `1989.2275` → IC=+0.329 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1989.2275 (IC base=+0.287)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0023` → IC=+0.163 (n=90)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0023 (IC base=+0.159)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.229 (n=68)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.193 (n=210)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` > `0.3308` → IC=+0.257 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3308 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` > `0.2839` → IC=+0.300 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2839 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.061` → IC=+0.267 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.061 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` < `0.6819` → IC=+0.186 (n=68)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.6819 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` > `1.4432` → IC=+0.171 (n=68)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 1.4432 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` < `0.0779` → IC=+0.219 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0779 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` < `2.4203` → IC=+0.250 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4203 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` > `1.403` → IC=+0.203 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.403 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `8479.5773` → IC=+0.261 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8479.5773 (IC base=+0.159)

- **PATRÓN** `sigma_h` < `0.0021` → IC=+0.203 (n=126)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0021 (IC base=+0.174)

- **PATRÓN** `sigma_h` > `0.0026` → IC=+0.175 (n=189)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0026 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.2699` → IC=+0.182 (n=284)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.2699 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.182 (n=272)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 7.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.179 (n=294)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 18.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` < `0.4746` → IC=+0.231 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4746 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` < `0.1607` → IC=+0.198 (n=283)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.1607 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.479` → IC=+0.256 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.479 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` < `0.618` → IC=+0.222 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.618 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` > `0.8408` → IC=+0.191 (n=189)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` > 0.8408 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.0973` → IC=+0.297 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0973 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` < `1.4452` → IC=+0.285 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4452 (IC base=+0.174)

- **PATRÓN** `libro_liquidez` > `11633.3746` → IC=+0.211 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11633.3746 (IC base=+0.174)

- **PATRÓN** `ballena_activa_n` < `298.0` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 298.0 (IC base=+0.174)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.245 (n=108)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0075 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.237 (n=154)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` > `0.717` → IC=+0.247 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.717 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.864` → IC=+0.340 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.864 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` < `0.2327` → IC=+0.168 (n=251)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` < 0.2327 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `2.1733` → IC=+0.149 (n=109)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.1733 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `4.0128` → IC=+0.170 (n=113)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 4.0128 (IC base=+0.171)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.190 (n=349)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.06 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `1854.4986` → IC=+0.185 (n=214)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 1854.4986 (IC base=+0.171)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.332 (n=123)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.267)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.273 (n=130)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.267)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.282 (n=99)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.267)

- **PATRÓN** `ibs_20min` < `0.5575` → IC=+0.340 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5575 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` < `0.2282` → IC=+0.224 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2282 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` > `0.4009` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.4009 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` < `2.5357` → IC=+0.276 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5357 (IC base=+0.267)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.280 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.267)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.267)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0021` → IC=+0.153 (n=70)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0021 (IC base=+0.138)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.180 (n=95)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0044 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0613` → IC=+0.167 (n=70)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.0613 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.163 (n=191)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 8.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.3787` → IC=+0.229 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3787 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.2393` → IC=+0.214 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2393 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.513` → IC=+0.191 (n=124)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 3.513 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.7618` → IC=+0.223 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7618 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `1.1223` → IC=+0.149 (n=95)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 1.1223 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2879` → IC=+0.324 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2879 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.4367` → IC=+0.232 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4367 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `3633.9451` → IC=+0.231 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3633.9451 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `231.0` → IC=+0.259 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 231.0 (IC base=+0.138)

- **PATRÓN** `sigma_h` < `0.0023` → IC=+0.266 (n=75)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0023 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.3476` → IC=+0.155 (n=169)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.3476 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.143 (n=180)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 4.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.152 (n=113)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 10.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.2192` → IC=+0.257 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2192 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.1323` → IC=+0.143 (n=82)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.1323 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.3499` → IC=+0.146 (n=176)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.3499 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.864` → IC=+0.263 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.864 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.7474` → IC=+0.178 (n=113)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.7474 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` < `0.0861` → IC=+0.203 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0861 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2263` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2263 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.1429` → IC=+0.209 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1429 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.5496` → IC=+0.214 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5496 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `10007.3401` → IC=+0.161 (n=57)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 10007.3401 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `122.0` → IC=+0.235 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 122.0 (IC base=+0.139)

### GBM_LATE_15M_TARDIO#SOL#15min
- **FILTRO** `ibs_20min` > `0.6` → IC=-0.177 (n=94)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.203 (n=284)

- **PATRÓN** `ibs_20min` > `0.9412` → IC=+0.233 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9412 (IC base=+0.039)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.923` → IC=+0.184 (n=153)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 2.923 (IC base=+0.039)

- **PATRÓN** `libro_liquidez` > `2514.0969` → IC=+0.185 (n=87)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2514.0969 (IC base=+0.039)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.039)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.160 (n=251)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0069 (IC base=+0.108)

- **PATRÓN** `drift_60min` |x|≤ `0.199` → IC=+0.141 (n=190)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.199 (IC base=+0.108)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.184 (n=131)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.108)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.203 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6 (IC base=+0.108)

- **PATRÓN** `dist_vwap_pct` < `0.7224` → IC=+0.129 (n=300)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.7224 (IC base=+0.108)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.269` → IC=+0.175 (n=38)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 7.269 (IC base=+0.108)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.391` → IC=+0.123 (n=295)

  - _Acción_: Kelly boost +0.61€ cuando `sigma_ewma_delta_pct` < 4.391 (IC base=+0.108)

- **PATRÓN** `volumen_regimen` < `0.6969` → IC=+0.146 (n=125)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.6969 (IC base=+0.108)

- **PATRÓN** `volumen_regimen` > `1.0706` → IC=+0.141 (n=129)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.0706 (IC base=+0.108)

- **PATRÓN** `volumen_pendiente_norm` < `0.1535` → IC=+0.182 (n=146)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` < 0.1535 (IC base=+0.108)

- **PATRÓN** `volumen_pendiente_norm` > `0.072` → IC=+0.172 (n=59)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.072 (IC base=+0.108)

- **PATRÓN** `volumen_spike_ratio` > `1.5635` → IC=+0.191 (n=124)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 1.5635 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `1568.0425` → IC=+0.164 (n=129)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 1568.0425 (IC base=+0.108)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.242 (n=118)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0077 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.0796` → IC=+0.203 (n=119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0796 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.196 (n=133)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 17.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.179 (n=129)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 6.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.8507` → IC=+0.247 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8507 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.2178` → IC=+0.252 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2178 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.298` → IC=+0.229 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.298 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `1.2317` → IC=+0.150 (n=352)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.2317 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` > `0.6734` → IC=+0.159 (n=315)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6734 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.3172` → IC=+0.250 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3172 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.6383` → IC=+0.147 (n=267)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.6383 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.6893` → IC=+0.159 (n=271)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.6893 (IC base=+0.150)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.165 (n=362)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `2663.9798` → IC=+0.162 (n=235)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2663.9798 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.250 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.277 (n=370)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0073 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.3502` → IC=+0.228 (n=421)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3502 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.270 (n=207)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` < `0.4643` → IC=+0.287 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4643 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` < `0.1176` → IC=+0.232 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1176 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.597` → IC=+0.278 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.597 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.782` → IC=+0.221 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.782 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` > `0.883` → IC=+0.234 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.883 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.2442` → IC=+0.293 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2442 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `2.9324` → IC=+0.238 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9324 (IC base=+0.213)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.151 (n=299)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.130 (n=90)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` > 0.0051 (IC base=+0.059)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.183 (n=39)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 16.0 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` > `0.2409` → IC=+0.192 (n=63)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.2409 (IC base=+0.059)

- **PATRÓN** `volumen_spike_ratio` < `1.4285` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.4285 (IC base=+0.059)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.182 (n=209)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0041 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.2281` → IC=+0.181 (n=208)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.2281 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.197 (n=97)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 4.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.6635` → IC=+0.164 (n=236)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.6635 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.3593` → IC=+0.147 (n=247)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.3593 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.369` → IC=+0.136 (n=127)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 2.369 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.475` → IC=+0.134 (n=225)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 5.475 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `1.3627` → IC=+0.164 (n=236)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.3627 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` < `0.0965` → IC=+0.139 (n=200)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` < 0.0965 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.7248` → IC=+0.165 (n=234)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.7248 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=299)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `7268.8224` → IC=+0.198 (n=236)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 7268.8224 (IC base=+0.133)

### GBM_LATE_5M#BTC#5min
- **FILTRO** `hora_utc` < `16.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.269 (n=11)

- **FILTRO** `dist_vwap_pct` < `0.5259` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.5259
  - _Potencial_: sin este filtro IC_bueno=+0.269 (n=11)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.181 (n=136)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0036 (IC base=+0.152)

- **PATRÓN** `sigma_h` > `0.0021` → IC=+0.152 (n=136)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0021 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.0633` → IC=+0.223 (n=45)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0633 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.160 (n=48)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 15.0 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.284 (n=49)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` < `0.023` → IC=+0.226 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.023 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` < `0.1867` → IC=+0.169 (n=134)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1867 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.868` → IC=+0.172 (n=126)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` < 5.868 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `1.2781` → IC=+0.164 (n=135)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2781 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` > `0.7036` → IC=+0.172 (n=120)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 0.7036 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.1596` → IC=+0.229 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1596 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `2.3292` → IC=+0.178 (n=119)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 2.3292 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `1.4126` → IC=+0.164 (n=135)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.4126 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `9861.9143` → IC=+0.164 (n=135)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 9861.9143 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `669.0` → IC=+0.203 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 669.0 (IC base=+0.152)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.239 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0055 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.1682` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1682 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.19` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.19 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` < `0.1138` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1138 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `8480.9672` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 8480.9672 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.278 (n=43)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.212` → IC=+0.295 (n=42)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.212 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.256 (n=43)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` < `0.6417` → IC=+0.238 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6417 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `0.0863` → IC=+0.259 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0863 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` > `0.4317` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4317 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` < `0.1106` → IC=+0.219 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1106 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.567` → IC=+0.300 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.567 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` < `1.2693` → IC=+0.307 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2693 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` < `0.1284` → IC=+0.250 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1284 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` < `1.8733` → IC=+0.314 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8733 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `7268.8224` → IC=+0.285 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7268.8224 (IC base=+0.218)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.223 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.218)

### GBM_LATE_5M#SOL#5min
- **FILTRO** `sigma_ewma_delta_pct` < `1.963` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 1.963
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### GBM_LATE_60M
- **FILTRO** `ibs_20min` < `0.7342` → IC=-0.149 (n=55)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7342
  - _Potencial_: sin este filtro IC_bueno=+0.219 (n=112)

- **FILTRO** `sigma_h` > `0.0111` → IC=-0.296 (n=52)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0111
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=160)

- **FILTRO** `drift_60min` |x|> `0.0909` → IC=-0.262 (n=19)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.0909
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=37)

- **FILTRO** `dist_vwap_pct` > `0.1067` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1067
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=53)

- **FILTRO** `volumen_regimen` > `0.8876` → IC=-0.196 (n=54)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8876
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=56)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.180 (n=145)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0054 (IC base=+0.057)

- **PATRÓN** `drift_60min` |x|≤ `0.1151` → IC=+0.151 (n=41)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1151 (IC base=+0.057)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.291 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.057)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.379` → IC=+0.213 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.379 (IC base=+0.057)

- **PATRÓN** `volumen_regimen` > `1.0949` → IC=+0.182 (n=42)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.0949 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` < `0.0847` → IC=+0.283 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0847 (IC base=+0.057)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.137 (n=111)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.02 (IC base=+0.057)

- **PATRÓN** `libro_liquidez` > `2013.1835` → IC=+0.134 (n=91)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2013.1835 (IC base=+0.057)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.7342` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7342
  - _Potencial_: sin este filtro IC_bueno=+0.204 (n=42)

- **FILTRO** `sigma_h` > `0.0036` → IC=-0.167 (n=34)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0036
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=36)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.194 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=36)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.321 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.062)

- **PATRÓN** `ibs_20min` > `0.7342` → IC=+0.204 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7342 (IC base=+0.062)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.15` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 13.15 (IC base=+0.062)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0071` → IC=-0.326 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0071
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=43)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.360 (n=41)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=23)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.242 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.100)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.125 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 7.0 (IC base=+0.100)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.368 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` < `0.1209` → IC=+0.211 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1209 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.41` → IC=+0.304 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.41 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` < `0.8241` → IC=+0.192 (n=37)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.8241 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` > `1.0919` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0919 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `2340.5972` → IC=+0.214 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2340.5972 (IC base=+0.100)

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

- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.214 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=-0.020)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.167 (n=25)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 18.0 (IC base=-0.020)

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

- **FILTRO** `ibs_20min` < `0.3707` → IC=-0.308 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3707
  - _Potencial_: sin este filtro IC_bueno=-0.289 (n=74)

- **FILTRO** `dist_vwap_pct` < `0.1009` → IC=-0.354 (n=53)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1009
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=45)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `ibs_20min` < `0.5407` → IC=-0.286 (n=26)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5407
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `ibs_20min` > `0.6267` → IC=-0.364 (n=20)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6267
  - _Potencial_: sin este filtro IC_bueno=-0.152 (n=21)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` < `10.347` → IC=-0.463 (n=25)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 10.347
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **FILTRO** `sigma_h` > `0.0018` → IC=-0.346 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0018
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `dist_vwap_pct` > `0.0802` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.0802
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=15)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `ibs_20min` < `0.6` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `ibs_20min` < `0.7391` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7391
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.441 (n=15)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.5333` → IC=-0.186 (n=33)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5333
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=101)

- **PATRÓN** `ibs_20min` > `0.6429` → IC=+0.144 (n=133)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.6429 (IC base=+0.059)

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

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.085)

- **PATRÓN** `ibs_20min` < `0.3803` → IC=+0.140 (n=48)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.3803 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.84` → IC=+0.167 (n=34)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 3.84 (IC base=+0.085)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.991` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.991 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `2399.5952` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2399.5952 (IC base=+0.159)

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
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.220 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.172)

- **PATRÓN** `py_entrada` < `0.485` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.485 (IC base=+0.172)

- **PATRÓN** `py_entrada` > `0.495` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.495 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `2785.0379` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2785.0379 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.167 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 4.0 (IC base=+0.107)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` > 0.505 (IC base=+0.107)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.220 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.172)

- **PATRÓN** `py_entrada` < `0.485` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.485 (IC base=+0.172)

- **PATRÓN** `py_entrada` > `0.495` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.495 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `2785.0379` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2785.0379 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.167 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 4.0 (IC base=+0.107)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` > 0.505 (IC base=+0.107)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=70)

- **FILTRO** `hora_utc` > `17.0` → IC=-0.333 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=87)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=87)

- **FILTRO** `libro_liquidez` < `1970.6128` → IC=-0.389 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 1970.6128
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=78)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.156 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=72)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=82)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=71)

- **FILTRO** `libro_liquidez` < `4259.049` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `libro_liquidez` < 4259.049
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=65)

- **FILTRO** `ballena_activa_n` > `474.0` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `ballena_activa_n` > 474.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=38)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=76)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=70)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `hora_utc` > `1.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=12)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=17)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.250 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9753` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9753
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=63)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.204 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=59)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=46)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.125 (n=38)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=43)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `hora_utc` < `5.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=63)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=54)

### LIQUIDACIONES_60M#SOL#60min
- **PATRÓN** `hora_utc` < `6.0` → IC=+0.180 (n=23)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 6.0 (IC base=+0.057)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2159.7894` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `libro_liquidez` < 2159.7894
  - _Potencial_: sin este filtro IC_bueno=+0.181 (n=45)

- **PATRÓN** `ibs_20min` > `0.9821` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.9821 (IC base=+0.044)

- **PATRÓN** `libro_liquidez` > `2159.7894` → IC=+0.181 (n=45)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 2159.7894 (IC base=+0.044)

- **PATRÓN** `drift_20min_pct` |x|≤ `0.0597` → IC=+0.188 (n=30)

  - _Acción_: Kelly boost +0.94€ cuando `drift_20min_pct` |x|≤ 0.0597 (IC base=+0.043)

### MOMENTUM_IBS_15M#BTC#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.159 (n=39)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=82)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.167 (n=49)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 5.0 (IC base=+0.032)

- **PATRÓN** `drift_20min_pct` |x|≤ `0.0544` → IC=+0.133 (n=47)

  - _Acción_: Kelly boost +0.66€ cuando `drift_20min_pct` |x|≤ 0.0544 (IC base=+0.032)

### MOMENTUM_IBS_15M#DOGE#15min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=62)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=107)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.174 (n=41)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 3.0 (IC base=+0.033)

- **PATRÓN** `drift_20min_pct` |x|≤ `0.0655` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `drift_20min_pct` |x|≤ 0.0655 (IC base=+0.033)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.42` → IC=-0.200 (n=231)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=719)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.218 (n=250)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=781)

- **FILTRO** `ibs_20min` > `0.2685` → IC=-0.199 (n=257)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2685
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=774)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.244 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=95)

- **FILTRO** `ibs_20min` < `0.7083` → IC=-0.222 (n=34)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7083
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=102)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.139 (n=70)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=101)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.287 (n=45)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=136)

- **FILTRO** `ibs_20min` > `0.2136` → IC=-0.287 (n=45)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2136
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=136)

- **FILTRO** `ballena_activa_n` > `68.0` → IC=-0.202 (n=45)

  - _Acción_: SKIP cuando `ballena_activa_n` > 68.0
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=136)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.143 (n=68)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=80)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=131)

- **FILTRO** `ibs_20min` > `0.7585` → IC=-0.182 (n=42)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7585
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=128)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` > `0.505` → IC=-0.225 (n=38)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=148)

- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=124)

### MOMENTUM_IBS_15M_BALLENA#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=58)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=103)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.237 (n=36)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=126)

- **FILTRO** `ibs_20min` > `0.1471` → IC=-0.125 (n=78)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1471
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=84)

- **FILTRO** `ballena_activa_n` > `2.0` → IC=-0.205 (n=59)

  - _Acción_: SKIP cuando `ballena_activa_n` > 2.0
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=103)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.250 (n=42)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=126)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=153)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.333 (n=40)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=121)

- **FILTRO** `drift_20min_pct` |x|> `0.2905` → IC=-0.214 (n=40)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.2905
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=121)

- **FILTRO** `ibs_20min` > `0.2724` → IC=-0.286 (n=40)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2724
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=121)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `hora_utc` < `16.0` → IC=-0.300 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=126)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=372)

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

- **FILTRO** `drift_7min_pct` |x|> `0.0741` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.0741
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=25)

- **PATRÓN** `drift_7min_pct` |x|≤ `0.0741` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `drift_7min_pct` |x|≤ 0.0741 (IC base=+0.000)

### MOMENTUM_IBS_5M#BTC#5min
- **FILTRO** `hora_utc` > `18.0` → IC=-0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 18.0
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=74)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.143 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 17.0 (IC base=+0.033)

### MOMENTUM_IBS_5M#DOGE#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=38)

- **PATRÓN** `drift_7min_pct` |x|≤ `0.0611` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `drift_7min_pct` |x|≤ 0.0611 (IC base=+0.029)

### MOMENTUM_IBS_5M#ETH#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=33)

- **PATRÓN** `libro_liquidez` > `9401.8411` → IC=+0.138 (n=45)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 9401.8411 (IC base=+0.041)

### MOMENTUM_IBS_5M#SOL#5min
- **PATRÓN** `drift_7min_pct` |x|≤ `0.0658` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `drift_7min_pct` |x|≤ 0.0658 (IC base=+0.050)

### MOMENTUM_IBS_5M_BALLENA
- **FILTRO** `hora_utc` < `6.0` → IC=-0.169 (n=548)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=2009)

- **FILTRO** `py_entrada` < `0.36` → IC=-0.266 (n=634)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=1923)

- **FILTRO** `ibs_7min` < `0.7342` → IC=-0.201 (n=639)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7342
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=1918)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.176 (n=856)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=1701)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.209 (n=784)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=2356)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.3` → IC=-0.269 (n=89)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=284)

- **FILTRO** `ibs_7min` < `0.9405` → IC=-0.165 (n=246)

  - _Acción_: SKIP cuando `ibs_7min` < 0.9405
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=127)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.184 (n=229)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=240)

- **FILTRO** `drift_7min_pct` |x|> `0.1194` → IC=-0.171 (n=159)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1194
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=310)

- **FILTRO** `ibs_7min` > `0.8333` → IC=-0.189 (n=117)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8333
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=352)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.217 (n=111)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=425)

- **FILTRO** `py_entrada` < `0.38` → IC=-0.264 (n=125)

  - _Acción_: SKIP cuando `py_entrada` < 0.38
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=411)

- **FILTRO** `ballena_activa_n` > `112.0` → IC=-0.174 (n=133)

  - _Acción_: SKIP cuando `ballena_activa_n` > 112.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=403)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.189 (n=120)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=440)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.192 (n=105)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=226)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.340 (n=79)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=252)

- **FILTRO** `ibs_7min` < `0.7041` → IC=-0.239 (n=109)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7041
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=222)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.290 (n=79)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=252)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.239 (n=117)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=409)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.38` → IC=-0.213 (n=113)

  - _Acción_: SKIP cuando `py_entrada` < 0.38
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=358)

- **FILTRO** `ibs_7min` < `0.8374` → IC=-0.164 (n=117)

  - _Acción_: SKIP cuando `ibs_7min` < 0.8374
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=354)

- **FILTRO** `ballena_activa_n` > `31.0` → IC=-0.158 (n=112)

  - _Acción_: SKIP cuando `ballena_activa_n` > 31.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=359)

- **FILTRO** `py_entrada` > `0.56` → IC=-0.169 (n=122)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=382)

- **FILTRO** `ballena_activa_n` > `17.0` → IC=-0.182 (n=124)

  - _Acción_: SKIP cuando `ballena_activa_n` > 17.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=380)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.228 (n=112)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=360)

- **FILTRO** `ibs_7min` < `0.7692` → IC=-0.192 (n=115)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7692
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=357)

- **FILTRO** `ballena_activa_n` > `17.0` → IC=-0.239 (n=117)

  - _Acción_: SKIP cuando `ballena_activa_n` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=355)

- **FILTRO** `py_entrada` > `0.52` → IC=-0.147 (n=188)

  - _Acción_: SKIP cuando `py_entrada` > 0.52
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=370)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.167 (n=109)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=265)

- **FILTRO** `py_entrada` < `0.41` → IC=-0.256 (n=121)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=253)

- **FILTRO** `ibs_7min` < `0.7348` → IC=-0.300 (n=93)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7348
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=281)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.268 (n=93)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=281)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.252 (n=127)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=396)

- **FILTRO** `drift_7min_pct` |x|> `0.1093` → IC=-0.131 (n=261)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1093
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=262)

- **FILTRO** `ibs_7min` > `0.8621` → IC=-0.197 (n=130)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8621
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=393)

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
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=205)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=337)

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

- **PATRÓN** `delta_ratio` |x|> `0.401` → IC=+0.158 (n=194)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.79€ cuando `delta_ratio` |x|> 0.401 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.167 (n=61)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 5.0 (IC base=+0.123)

- **PATRÓN** `total_vol_5m` < `596.006` → IC=+0.201 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 596.006 (IC base=+0.123)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `12.0` → IC=+0.269 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.152)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.2125` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.2125
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=38)

- **FILTRO** `pct_vs_K` |x|> `4.502` → IC=-0.470 (n=31)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.502
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=66)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.202 (n=45)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=-0.150)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `87.9756` → IC=-0.429 (n=26)

  - _Acción_: SKIP cuando `T_h` > 87.9756
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=13)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0132` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0132
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0048` → IC=-0.256 (n=39)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=22)

- **FILTRO** `T_h` > `143.1632` → IC=-0.371 (n=29)

  - _Acción_: SKIP cuando `T_h` > 143.1632
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=32)

- **FILTRO** `T_h` < `111.9668` → IC=-0.452 (n=19)

  - _Acción_: SKIP cuando `T_h` < 111.9668
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=41)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` > `0.0029` → IC=-0.309 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0029
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0033` → IC=-0.237 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **FILTRO** `T_h` > `95.1632` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `T_h` > 95.1632
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `sigma_h` < `0.0049` → IC=-0.289 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0049
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### STREAK_FADE_15M
- **FILTRO** `hora_utc` < `8.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=12)

- **FILTRO** `streak_len` > `4.0` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `streak_len` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=12)

- **FILTRO** `streak_estiramiento` > `0.4086` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4086
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `py_entrada` < `0.49` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=37)

- **FILTRO** `streak_estiramiento` > `0.437` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.437
  - _Potencial_: sin este filtro IC_bueno=+0.389 (n=7)

### STREAK_FADE_5M
- **FILTRO** `hora_utc` > `14.0` → IC=-0.147 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=112)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=117)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `ballena_activa_n` > `20.0` → IC=-0.167 (n=28)

  - _Acción_: SKIP cuando `ballena_activa_n` > 20.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=18)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.265 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=30)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=33)

- **FILTRO** `libro_liquidez` < `3614.0796` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 3614.0796
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=37)

- **FILTRO** `hora_utc` < `14.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `hora_utc` > `8.0` → IC=-0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=43)

- **FILTRO** `streak_estiramiento` > `0.644` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.644
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=49)

- **FILTRO** `ballena_activa_n` > `4.0` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `ballena_activa_n` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=13)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=23)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.068)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `hora_utc` < `10.0` → IC=-0.214 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.139 (n=59)

- **FILTRO** `hora_utc` > `9.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=52)

- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=40)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.139 (n=59)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 10.0 (IC base=+0.050)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.495 (IC base=+0.050)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `hora_utc` < `19.0` → IC=-0.141 (n=37)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=+0.152 (n=21)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=99)

- **PATRÓN** `hora_utc` > `20.0` → IC=+0.184 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 20.0 (IC base=-0.033)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.130 (n=90)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 16.0 (IC base=+0.078)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.149 (n=35)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 23.0 (IC base=+0.078)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=811)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=470)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=478)

### UPDOWN_GBM#15min
- **FILTRO** `ibs_15` < `0.5` → IC=-0.170 (n=101)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.201 (n=343)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.147 (n=148)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0035 (IC base=+0.117)

- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.141 (n=151)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` > 0.0054 (IC base=+0.117)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0679` → IC=+0.133 (n=333)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio_macro` |x|> 0.0679 (IC base=+0.117)

- **PATRÓN** `ibs_15` > `0.5` → IC=+0.201 (n=343)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `0.4266` → IC=+0.204 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4266 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` < `0.083` → IC=+0.138 (n=186)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.083 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.463` → IC=+0.246 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.463 (IC base=+0.117)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.127 (n=341)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `5583.7388` → IC=+0.181 (n=111)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 5583.7388 (IC base=+0.117)

- **PATRÓN** `ibs_15` < `0.1384` → IC=+0.141 (n=293)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.70€ cuando `ibs_15` < 0.1384 (IC base=+0.044)

### UPDOWN_GBM#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1701` → IC=-0.135 (n=146)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1701
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=146)

- **FILTRO** `ibs_15` < `0.1827` → IC=-0.235 (n=96)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1827
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=196)

- **FILTRO** `sigma_ewma_delta_pct` > `6.818` → IC=-0.186 (n=49)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.818
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=243)

- **FILTRO** `ballena_activa_n` > `1.0` → IC=-0.177 (n=29)

  - _Acción_: SKIP cuando `ballena_activa_n` > 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=31)

### UPDOWN_GBM#60min
- **FILTRO** `hora_utc` < `11.0` → IC=-0.269 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=160)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.0397` → IC=-0.227 (n=20)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0397
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=39)

- **FILTRO** `hora_utc` < `19.0` → IC=-0.200 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=17)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.701` → IC=+0.136 (n=31)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 11.701 (IC base=+0.027)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.145 (n=108)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.03 (IC base=+0.027)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `sigma_h` < `0.0044` → IC=-0.239 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0044
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=21)

- **FILTRO** `dist_vwap_pct` < `0.6313` → IC=-0.219 (n=30)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.6313
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=12)

- **FILTRO** `libro_liquidez` < `13081.8522` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `libro_liquidez` < 13081.8522
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=21)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.167 (n=82)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0029 (IC base=+0.158)

- **PATRÓN** `sigma_h` > `0.0021` → IC=+0.171 (n=74)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0021 (IC base=+0.158)

- **PATRÓN** `drift_60min` |x|≤ `0.1916` → IC=+0.179 (n=82)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.1916 (IC base=+0.158)

- **PATRÓN** `drift_15min` |x|≤ `0.4532` → IC=+0.184 (n=55)

  - _Acción_: Kelly boost +0.92€ cuando `drift_15min` |x|≤ 0.4532 (IC base=+0.158)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0911` → IC=+0.171 (n=74)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.86€ cuando `delta_ratio_macro` |x|> 0.0911 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.210 (n=74)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.158)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.167 (n=73)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 13.0 (IC base=+0.158)

- **PATRÓN** `ibs_15` > `0.8877` → IC=+0.272 (n=55)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8877 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `0.3582` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3582 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` < `0.1019` → IC=+0.235 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1019 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.367` → IC=+0.214 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.367 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` < `23.949` → IC=+0.159 (n=86)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` < 23.949 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `9189.8912` → IC=+0.250 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9189.8912 (IC base=+0.158)

### UPDOWN_GBM#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2056` → IC=-0.204 (n=25)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2056
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=14)

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.0099` → IC=+0.130 (n=71)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +0.65€ cuando `pct_spot_vs_ref` |x|≤ 0.0099 (IC base=+0.046)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.136 (n=141)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.003 (IC base=+0.046)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.035` → IC=+0.167 (n=55)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.035 (IC base=+0.046)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `hora_utc` > `19.0` → IC=-0.132 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 19.0
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=52)

- **FILTRO** `ibs_15` < `0.6248` → IC=-0.237 (n=17)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6248
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=52)

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1026` → IC=+0.167 (n=22)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +0.83€ cuando `pct_spot_vs_ref` |x|≤ 0.1026 (IC base=+0.012)

- **PATRÓN** `ibs_15` > `0.9209` → IC=+0.154 (n=24)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.77€ cuando `ibs_15` > 0.9209 (IC base=+0.012)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `ibs_15` < `0.5408` → IC=-0.235 (n=32)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5408
  - _Potencial_: sin este filtro IC_bueno=+0.297 (n=67)

- **PATRÓN** `sigma_h` > `0.0028` → IC=+0.152 (n=67)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0028 (IC base=+0.124)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2385` → IC=+0.278 (n=25)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2385 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.155 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.148 (n=52)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 12.0 (IC base=+0.124)

- **PATRÓN** `ibs_15` > `0.5408` → IC=+0.297 (n=67)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5408 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` < `0.0929` → IC=+0.214 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0929 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.57` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.57 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `8988.4246` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 8988.4246 (IC base=+0.124)

- **PATRÓN** `ibs_15` < `0.447` → IC=+0.136 (n=160)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.68€ cuando `ibs_15` < 0.447 (IC base=+0.091)

- **PATRÓN** `dist_vwap_pct` > `0.46` → IC=+0.218 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.46 (IC base=+0.091)

- **PATRÓN** `sigma_ewma_delta_pct` < `16.415` → IC=+0.135 (n=146)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 16.415 (IC base=+0.091)

### UPDOWN_GBM#ETH#5min
- **FILTRO** `ibs_15` < `0.0049` → IC=-0.206 (n=15)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.0049
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=48)

- **FILTRO** `dist_vwap_pct` > `0.1641` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1641
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=48)

- **FILTRO** `sigma_ewma_delta_pct` > `5.384` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.384
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=38)

- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=132)

- **PATRÓN** `sigma_h` < `0.0023` → IC=+0.189 (n=43)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0023 (IC base=+0.017)

### UPDOWN_GBM#ETH#60min
- **PATRÓN** `libro_spread` < `0.03` → IC=+0.182 (n=42)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.03 (IC base=+0.045)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `ibs_15` < `0.6` → IC=-0.177 (n=29)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=30)

- **PATRÓN** `ibs_15` > `0.6` → IC=+0.250 (n=30)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6 (IC base=+0.041)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.764` → IC=+0.318 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.764 (IC base=+0.041)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `ibs_15` < `0.1667` → IC=-0.382 (n=15)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1667
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=32)

- **FILTRO** `sigma_ewma_delta_pct` < `2.288` → IC=-0.158 (n=36)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 2.288
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=11)

- **PATRÓN** `ibs_15` < `0.1` → IC=+0.143 (n=54)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.71€ cuando `ibs_15` < 0.1 (IC base=+0.051)

### UPDOWN_GBM#SOL#60min
- **FILTRO** `sigma_h` > `0.0126` → IC=-0.182 (n=20)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0126
  - _Potencial_: sin este filtro IC_bueno=+0.196 (n=21)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.005` → IC=+0.163 (n=96)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.005 (IC base=+0.085)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0626` → IC=+0.133 (n=96)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio_macro` |x|> 0.0626 (IC base=+0.085)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.167 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 6.0 (IC base=+0.085)

- **PATRÓN** `ibs_15` > `0.55` → IC=+0.182 (n=86)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.91€ cuando `ibs_15` > 0.55 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` > `0.4287` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4287 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.54` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.54 (IC base=+0.085)

- **PATRÓN** `libro_liquidez` > `2507.0533` → IC=+0.136 (n=86)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2507.0533 (IC base=+0.085)

- **PATRÓN** `ibs_15` < `0.15` → IC=+0.178 (n=85)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.89€ cuando `ibs_15` < 0.15 (IC base=+0.045)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1986` → IC=+0.288 (n=83)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1986 (IC base=+0.280)

- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.295 (n=42)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0022 (IC base=+0.280)

- **PATRÓN** `sigma_h` > `0.0026` → IC=+0.300 (n=63)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0026 (IC base=+0.280)

- **PATRÓN** `drift_60min` |x|≤ `0.16` → IC=+0.300 (n=83)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.16 (IC base=+0.280)

- **PATRÓN** `drift_15min` |x|≤ `0.4136` → IC=+0.295 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4136 (IC base=+0.280)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0706` → IC=+0.286 (n=96)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0706 (IC base=+0.280)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.302 (n=84)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.280)

- **PATRÓN** `ibs_15` > `0.7199` → IC=+0.333 (n=94)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7199 (IC base=+0.280)

- **PATRÓN** `dist_vwap_pct` > `0.3682` → IC=+0.389 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3682 (IC base=+0.280)

- **PATRÓN** `dist_vwap_pct` < `0.0842` → IC=+0.288 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0842 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` > `14.744` → IC=+0.304 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 14.744 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `3288.4647` → IC=+0.291 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3288.4647 (IC base=+0.280)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1934` → IC=+0.286 (n=54)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1934 (IC base=+0.241)

- **PATRÓN** `sigma_h` < `0.002` → IC=+0.318 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.002 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.1567` → IC=+0.264 (n=53)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1567 (IC base=+0.241)

- **PATRÓN** `drift_15min` |x|≤ `0.4089` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4089 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.274 (n=60)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.241)

- **PATRÓN** `ibs_15` < `0.9993` → IC=+0.242 (n=60)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.9993 (IC base=+0.241)

- **PATRÓN** `ibs_15` > `0.9071` → IC=+0.286 (n=40)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9071 (IC base=+0.241)

- **PATRÓN** `dist_vwap_pct` > `0.3017` → IC=+0.370 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3017 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.438` → IC=+0.244 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.438 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` < `15.813` → IC=+0.255 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 15.813 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `6696.5886` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6696.5886 (IC base=+0.241)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0031` → IC=+0.379 (n=31)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0031 (IC base=+0.333)

- **PATRÓN** `drift_60min` |x|≤ `0.1188` → IC=+0.385 (n=24)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1188 (IC base=+0.333)

- **PATRÓN** `delta_ratio_macro` |x|> `0.13` → IC=+0.420 (n=23)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.13 (IC base=+0.333)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.400 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.333)

- **PATRÓN** `ibs_15` > `0.785` → IC=+0.439 (n=31)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.785 (IC base=+0.333)

- **PATRÓN** `dist_vwap_pct` < `0.058` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.058 (IC base=+0.333)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.588` → IC=+0.405 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.588 (IC base=+0.333)

- **PATRÓN** `libro_liquidez` > `2844.0749` → IC=+0.340 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2844.0749 (IC base=+0.333)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `ibs_15` < `0.4444` → IC=-0.320 (n=87)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.4444
  - _Potencial_: sin este filtro IC_bueno=+0.189 (n=181)

- **FILTRO** `sigma_h` > `0.0076` → IC=-0.168 (n=375)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0076
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=1129)

- **FILTRO** `ibs_15` > `0.531` → IC=-0.278 (n=16)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.531
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=52)

- **FILTRO** `sigma_ewma_delta_pct` > `13.3` → IC=-0.200 (n=288)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 13.3
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=1216)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3433` → IC=+0.176 (n=35)

  - _Acción_: Kelly boost +0.88€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3433 (IC base=-0.037)

- **PATRÓN** `ibs_15` > `0.4444` → IC=+0.189 (n=181)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.94€ cuando `ibs_15` > 0.4444 (IC base=-0.037)

- **PATRÓN** `ibs_15` < `0.531` → IC=+0.278 (n=52)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.531 (IC base=-0.080)

- **PATRÓN** `dist_vwap_pct` < `0.1453` → IC=+0.173 (n=50)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.1453 (IC base=-0.080)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.232 (n=106)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=226)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.233 (n=73)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=259)

- **FILTRO** `sigma_ewma_delta_pct` > `20.971` → IC=-0.227 (n=75)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 20.971
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=257)

- **FILTRO** `libro_liquidez` < `13678.2586` → IC=-0.215 (n=219)

  - _Acción_: SKIP cuando `libro_liquidez` < 13678.2586
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=113)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.123 (n=59)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.003 (IC base=+0.067)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `drift_60min` |x|> `0.1985` → IC=-0.231 (n=24)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1985
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=75)

- **FILTRO** `ibs_15` < `0.5659` → IC=-0.343 (n=49)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5659
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=50)

- **PATRÓN** `ibs_15` > `0.5659` → IC=+0.250 (n=50)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5659 (IC base=-0.045)

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.0954` → IC=+0.204 (n=25)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.0954 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0039` → IC=+0.186 (n=33)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0039 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.2431` → IC=+0.186 (n=33)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.2431 (IC base=+0.167)

- **PATRÓN** `drift_15min` |x|≤ `0.6645` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `drift_15min` |x|≤ 0.6645 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.194 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 7.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.186 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 14.0 (IC base=+0.167)

- **PATRÓN** `ibs_15` < `0.428` → IC=+0.329 (n=33)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.428 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.899` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 7.899 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.182` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` < 12.182 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `3807.5396` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3807.5396 (IC base=+0.167)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0069` → IC=-0.218 (n=37)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0069
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=115)

- **FILTRO** `sigma_h` > `0.0078` → IC=-0.159 (n=133)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0078
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=401)

- **FILTRO** `sigma_ewma_delta_pct` > `14.141` → IC=-0.224 (n=74)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 14.141
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=460)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.371` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 10.371 (IC base=-0.039)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `hora_utc` > `6.0` → IC=-0.146 (n=111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=58)

- **FILTRO** `libro_liquidez` < `2497.8056` → IC=-0.204 (n=42)

  - _Acción_: SKIP cuando `libro_liquidez` < 2497.8056
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=127)

- **FILTRO** `sigma_h` > `0.0081` → IC=-0.218 (n=122)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0081
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=369)

- **FILTRO** `drift_15min` |x|> `0.7882` → IC=-0.137 (n=122)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.7882
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=369)

- **FILTRO** `sigma_ewma_delta_pct` > `14.393` → IC=-0.246 (n=61)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 14.393
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=430)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.328 (n=62)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.1826` → IC=+0.297 (n=136)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1826 (IC base=+0.287)

- **PATRÓN** `drift_15min` |x|≤ `0.6311` → IC=+0.287 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.6311 (IC base=+0.287)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1879` → IC=+0.344 (n=62)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1879 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.315 (n=144)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.287)

- **PATRÓN** `ibs_15` > `0.9358` → IC=+0.360 (n=91)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9358 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` > `0.3789` → IC=+0.357 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3789 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` < `0.0774` → IC=+0.321 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0774 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.127` → IC=+0.298 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.127 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `6215.1452` → IC=+0.296 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6215.1452 (IC base=+0.287)

- **PATRÓN** `ballena_activa_n` < `200.0` → IC=+0.370 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 200.0 (IC base=+0.287)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.2` → IC=+0.286 (n=82)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.2 (IC base=+0.266)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.300 (n=28)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0033 (IC base=+0.266)

- **PATRÓN** `drift_60min` |x|≤ `0.1826` → IC=+0.298 (n=82)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1826 (IC base=+0.266)

- **PATRÓN** `drift_15min` |x|≤ `0.571` → IC=+0.284 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.571 (IC base=+0.266)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0919` → IC=+0.289 (n=74)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0919 (IC base=+0.266)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.312 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.266)

- **PATRÓN** `ibs_15` > `0.8877` → IC=+0.316 (n=74)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8877 (IC base=+0.266)

- **PATRÓN** `dist_vwap_pct` > `0.3582` → IC=+0.400 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3582 (IC base=+0.266)

- **PATRÓN** `dist_vwap_pct` < `0.0966` → IC=+0.296 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0966 (IC base=+0.266)

- **PATRÓN** `sigma_ewma_delta_pct` > `27.622` → IC=+0.283 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 27.622 (IC base=+0.266)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.699` → IC=+0.271 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.699 (IC base=+0.266)

- **PATRÓN** `libro_liquidez` > `9931.1033` → IC=+0.275 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9931.1033 (IC base=+0.266)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` > `0.0026` → IC=+0.339 (n=54)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0026 (IC base=+0.311)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0469` → IC=+0.339 (n=54)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0469 (IC base=+0.311)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.350 (n=38)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.311)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.304 (n=49)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.311)

- **PATRÓN** `ibs_15` > `0.9678` → IC=+0.426 (n=25)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9678 (IC base=+0.311)

- **PATRÓN** `dist_vwap_pct` > `0.2815` → IC=+0.333 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2815 (IC base=+0.311)

- **PATRÓN** `dist_vwap_pct` < `0.0758` → IC=+0.371 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0758 (IC base=+0.311)

- **PATRÓN** `sigma_ewma_delta_pct` < `21.182` → IC=+0.345 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 21.182 (IC base=+0.311)

- **PATRÓN** `libro_liquidez` > `10575.7678` → IC=+0.350 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10575.7678 (IC base=+0.311)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0492` → IC=-0.167 (n=22)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0492
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=12)

- **FILTRO** `sigma_h` > `0.0036` → IC=-0.222 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0036
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

- **FILTRO** `drift_60min` |x|> `0.1447` → IC=-0.222 (n=16)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1447
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

- **FILTRO** `drift_15min` |x|> `0.3418` → IC=-0.167 (n=16)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3418
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=18)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.147 (n=83)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=251)

### UPDOWN_OU_5M#DOGE#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1055` → IC=-0.289 (n=17)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1055
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `sigma_h` > `0.0068` → IC=-0.262 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2236` → IC=-0.237 (n=17)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2236
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0931` → IC=-0.278 (n=16)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0931
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `sigma_h` > `0.0045` → IC=-0.289 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0045
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

### WEEKLY_PRICE
- **PATRÓN** `T_h` < `63.9965` → IC=+0.227 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 63.9965 (IC base=+0.041)

- **PATRÓN** `T_h` > `146.1131` → IC=+0.455 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1131 (IC base=+0.349)

- **PATRÓN** `ratio` > `1.016` → IC=+0.375 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.016 (IC base=+0.349)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` < `111.996` → IC=+0.345 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 111.996 (IC base=+0.272)

- **PATRÓN** `pct_dist` |x|≤ `0.6014` → IC=+0.280 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `pct_dist` |x|≤ 0.6014 (IC base=+0.272)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `111.9838` → IC=+0.313 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9838 (IC base=+0.309)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1332` → IC=+0.459 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1332 (IC base=+0.424)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5 sube el IC de +0.117 a +0.201 en UPDOWN_GBM#15min (n=343). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.8877 sube el IC de +0.158 a +0.272 en UPDOWN_GBM#BTC#15min (n=55). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5408 sube el IC de +0.124 a +0.297 en UPDOWN_GBM#ETH#15min (n=67). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.041 a +0.250 en UPDOWN_GBM#SOL#15min (n=30). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.55 sube el IC de +0.085 a +0.182 en UPDOWN_GBM#XRP#15min (n=86). Ya aplicado como kelly_boost=+0.91€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.15 sube el IC de +0.045 a +0.178 en UPDOWN_GBM#XRP#15min (n=85). Ya aplicado como kelly_boost=+0.89€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#60min**: dentro de BUY_YES, IBS > 0.9209 sube el IC de +0.012 a +0.154 en UPDOWN_GBM#BTC#60min (n=24). Ya aplicado como kelly_boost=+0.77€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.4444 sube el IC de -0.037 a +0.189 en UPDOWN_GBM_15M_TARDIO (n=181). Ya aplicado como kelly_boost=+0.94€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.531 sube el IC de -0.080 a +0.278 en UPDOWN_GBM_15M_TARDIO (n=52). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5659 sube el IC de -0.045 a +0.250 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=50). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.428 sube el IC de +0.167 a +0.329 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=33). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.9358 sube el IC de +0.287 a +0.360 en UPDOWN_GBM_IBS_ALTO (n=91). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8877 sube el IC de +0.266 a +0.316 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=74). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.9678 sube el IC de +0.311 a +0.426 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=25). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7199 sube el IC de +0.280 a +0.333 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=94). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS < 0.9993 sube el IC de +0.241 a +0.242 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=60). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.9071 sube el IC de +0.241 a +0.286 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=40). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.785 sube el IC de +0.333 a +0.439 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=31). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `ORDER_FLOW_5M#SOL#5min` — IC=+0.100 n=33. Faltan ~7 resoluciones para umbral n≥40. ETA: ~5h.
- **LIVE-CANDIDATA**: `ORDER_FLOW_5M#SOL` — IC=+0.100 n=33. Faltan ~7 resoluciones para umbral n≥40. ETA: ~5h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0` — IC=+0.184 n=36. Faltan ~4 resoluciones para umbral n≥40. ETA: ~3h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 517 | +0.059 | +42.36€ | 3 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 517 | +0.059 | +42.36€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 275 | +0.067 | +30.17€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 275 | +0.067 | +30.17€ | 2 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 213 | +0.030 | +1.26€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 213 | +0.030 | +1.26€ | 6 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 29 | +0.177 | +10.93€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 29 | +0.177 | +10.93€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 4141 | -0.113 | -588.24€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 515 | -0.051 | -56.82€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 3626 | -0.122 | -531.42€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 472 | -0.179 | -94.58€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 472 | -0.179 | -94.58€ | 2 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 515 | -0.051 | -56.82€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 515 | -0.051 | -56.82€ | 2 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 335 | -0.141 | -150.04€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 335 | -0.141 | -150.04€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 725 | -0.137 | -38.80€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 725 | -0.137 | -38.80€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 1130 | -0.004 | -58.42€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 1130 | -0.004 | -58.42€ | 0 | 0 |
| 🚫 BALLENAS_TARDIAS#XRP | 964 | -0.213 | -189.58€ | 0 | 0 |
| 🚫 BALLENAS_TARDIAS#XRP#5min | 964 | -0.213 | -189.58€ | 1 | 0 |
| ✅ FAVORITO_CONFIRMADO | 18161 | +0.111 | -1252.17€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 3904 | +0.186 | -122.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 106 | -0.102 | -48.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 11424 | +0.084 | -1085.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 2727 | +0.129 | +4.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 1928 | +0.036 | -423.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 15 | -0.066 | -1.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#240min | 5 | -0.089 | -6.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 1908 | +0.039 | -416.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 3981 | +0.138 | -41.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 1077 | +0.197 | -48.77€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 1897 | +0.109 | -37.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 965 | +0.139 | +66.93€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 1931 | +0.061 | -321.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 14 | +0.044 | -1.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 1916 | +0.061 | -317.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 4297 | +0.127 | -52.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 1439 | +0.170 | -3.40€ | 0 | 7 |
| 🚫 FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 1897 | +0.104 | -35.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 949 | +0.112 | -4.98€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 4104 | +0.128 | -303.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 1346 | +0.200 | -67.54€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 45 | +0.011 | -8.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 1900 | +0.076 | -170.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 813 | +0.137 | -57.29€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 1920 | +0.110 | -109.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 13 | +0.022 | +0.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 1906 | +0.111 | -108.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 4002 | +0.166 | -355.83€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 4002 | +0.166 | -355.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 1004 | +0.158 | -125.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 1004 | +0.158 | -125.87€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 84 | -0.116 | -4.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 84 | -0.116 | -4.02€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 999 | +0.154 | -132.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 999 | +0.154 | -132.28€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 888 | +0.226 | -32.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 888 | +0.226 | -32.22€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 2 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 948 | +0.186 | -75.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 948 | +0.186 | -75.20€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 203 | +0.422 | -8.05€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 203 | +0.422 | -8.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 74 | +0.421 | -1.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 74 | +0.421 | -1.97€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 79 | +0.401 | -5.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 79 | +0.401 | -5.39€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 47 | +0.418 | -0.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 47 | +0.418 | -0.83€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 8222 | +0.188 | -790.93€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 8222 | +0.188 | -790.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 1542 | +0.100 | -345.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 1542 | +0.100 | -345.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 1256 | +0.242 | -19.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 1256 | +0.242 | -19.58€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 1446 | +0.148 | -221.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 1446 | +0.148 | -221.07€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 1306 | +0.236 | -27.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 1306 | +0.236 | -27.87€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 1291 | +0.232 | -41.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 1291 | +0.232 | -41.27€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 1381 | +0.188 | -136.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 1381 | +0.188 | -136.11€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 2916 | +0.137 | +107.31€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 2916 | +0.137 | +107.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 1441 | +0.149 | +86.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 1441 | +0.149 | +86.81€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 1475 | +0.124 | +20.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 1475 | +0.124 | +20.49€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 596 | +0.301 | +5.97€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 596 | +0.301 | +5.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 252 | +0.276 | -8.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 252 | +0.276 | -8.45€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 276 | +0.302 | +6.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 276 | +0.302 | +6.91€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 68 | +0.371 | +7.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 68 | +0.371 | +7.51€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 247 | +0.412 | -10.79€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 247 | +0.412 | -10.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 108 | +0.409 | -5.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 108 | +0.409 | -5.09€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 113 | +0.413 | -6.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 113 | +0.413 | -6.02€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 26 | +0.357 | +0.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 26 | +0.357 | +0.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 36 | +0.184 | +6.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 12 | +0.129 | +3.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 24 | +0.154 | +3.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 29 | +0.145 | +3.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 5 | +0.018 | -0.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 24 | +0.154 | +3.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 5 | +0.054 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 5 | +0.054 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 960 | +0.096 | -32.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 95 | +0.036 | -7.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 865 | +0.102 | -25.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 655 | +0.092 | -17.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 95 | +0.036 | -7.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 560 | +0.101 | -10.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 305 | +0.103 | -14.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 305 | +0.103 | -14.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 283 | +0.275 | -21.11€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 283 | +0.275 | -21.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 283 | +0.275 | -21.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 283 | +0.275 | -21.11€ | 0 | 4 |
| ✅ GBM_LATE_15M | 5186 | +0.073 | +1855.75€ | 0 | 15 |
| ✅ GBM_LATE_15M#15min | 5186 | +0.073 | +1855.75€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 843 | +0.176 | +534.73€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 843 | +0.176 | +534.73€ | 0 | 17 |
| ✅ GBM_LATE_15M#BTC | 585 | +0.181 | +324.31€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 585 | +0.181 | +324.31€ | 0 | 28 |
| ✅ GBM_LATE_15M#DOGE | 853 | +0.191 | +587.35€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 853 | +0.191 | +587.35€ | 0 | 18 |
| ✅ GBM_LATE_15M#ETH | 725 | -0.028 | +25.93€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 725 | -0.028 | +25.93€ | 1 | 2 |
| ✅ GBM_LATE_15M#SOL | 970 | -0.014 | +161.71€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 970 | -0.014 | +161.71€ | 4 | 5 |
| ✅ GBM_LATE_15M#XRP | 1210 | -0.006 | +221.72€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 1210 | -0.006 | +221.72€ | 1 | 5 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 6172 | +0.046 | +2263.05€ | 0 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 6172 | +0.046 | +2263.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 1126 | -0.028 | +510.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 1126 | -0.028 | +510.46€ | 1 | 3 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 1225 | -0.026 | +92.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 1225 | -0.026 | +92.44€ | 1 | 3 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 717 | +0.241 | +658.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 717 | +0.241 | +658.57€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 1079 | -0.030 | +38.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 1079 | -0.030 | +38.75€ | 8 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 1083 | +0.001 | +189.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 1083 | +0.001 | +189.46€ | 3 | 2 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 942 | +0.215 | +773.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 942 | +0.215 | +773.38€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 3903 | +0.174 | +2645.52€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 3903 | +0.174 | +2645.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 634 | +0.193 | +466.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 634 | +0.193 | +466.11€ | 0 | 16 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 566 | +0.195 | +402.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 566 | +0.195 | +402.92€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 630 | +0.201 | +486.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 630 | +0.201 | +486.64€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 540 | +0.190 | +371.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 540 | +0.190 | +371.97€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 727 | +0.083 | +309.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 727 | +0.083 | +309.98€ | 1 | 13 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 806 | +0.191 | +607.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 806 | +0.191 | +607.90€ | 0 | 22 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 651 | +0.059 | +84.43€ | 0 | 12 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 651 | +0.059 | +84.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 132 | +0.082 | +19.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 132 | +0.082 | +19.14€ | 2 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 132 | +0.149 | +41.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 132 | +0.149 | +41.87€ | 1 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 238 | -0.004 | +9.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 238 | -0.004 | +9.85€ | 3 | 3 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 148 | +0.060 | +14.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 148 | +0.060 | +14.84€ | 0 | 5 |
| ✅ GBM_LATE_15M_TARDIO | 4508 | +0.165 | +2897.30€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#15min | 4508 | +0.165 | +2897.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 807 | +0.182 | +553.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 807 | +0.182 | +553.90€ | 0 | 17 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 649 | +0.168 | +400.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 649 | +0.168 | +400.50€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 798 | +0.216 | +655.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 798 | +0.216 | +655.60€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 502 | +0.139 | +247.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 502 | +0.139 | +247.49€ | 0 | 28 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 723 | +0.075 | +315.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 723 | +0.075 | +315.34€ | 1 | 17 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 1029 | +0.185 | +724.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 1029 | +0.185 | +724.47€ | 0 | 25 |
| ✅ GBM_LATE_5M | 448 | +0.111 | +160.81€ | 1 | 16 |
| ✅ GBM_LATE_5M#5min | 448 | +0.111 | +160.81€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 205 | +0.133 | +91.93€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 205 | +0.133 | +91.93€ | 2 | 15 |
| ✅ GBM_LATE_5M#DOGE | 13 | -0.108 | -4.42€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 13 | -0.108 | -4.42€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH | 125 | +0.193 | +71.92€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 125 | +0.193 | +71.92€ | 0 | 19 |
| ✅ GBM_LATE_5M#SOL | 54 | -0.036 | +2.39€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 54 | -0.036 | +2.39€ | 1 | 0 |
| ✅ GBM_LATE_5M#XRP | 51 | +0.047 | -1.01€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 51 | +0.047 | -1.01€ | 0 | 0 |
| ✅ GBM_LATE_60M | 501 | -0.045 | +74.00€ | 5 | 8 |
| ✅ GBM_LATE_60M#60min | 501 | -0.045 | +74.00€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 173 | -0.003 | +5.67€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 173 | -0.003 | +5.67€ | 3 | 3 |
| ✅ GBM_LATE_60M#ETH | 177 | -0.020 | +44.02€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 177 | -0.020 | +44.02€ | 2 | 8 |
| ✅ GBM_LATE_60M#SOL | 151 | -0.121 | +24.30€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 151 | -0.121 | +24.30€ | 3 | 2 |
| 🚫 GBM_LATE_60M_FADE | 193 | -0.305 | -34.48€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 193 | -0.305 | -34.48€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 76 | -0.256 | -7.36€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 76 | -0.256 | -7.36€ | 2 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 65 | -0.351 | -19.05€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 65 | -0.351 | -19.05€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 52 | -0.296 | -8.07€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 52 | -0.296 | -8.07€ | 3 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 311 | +0.040 | +5.51€ | 1 | 1 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 311 | +0.040 | +5.51€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 121 | +0.012 | +3.09€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 121 | +0.012 | +3.09€ | 2 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 74 | +0.092 | +5.73€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 74 | +0.092 | +5.73€ | 0 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 116 | +0.034 | -3.31€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 116 | +0.034 | -3.31€ | 1 | 5 |
| ✅ LEADLAG_BTC_XRP_15M | 115 | +0.141 | +36.86€ | 0 | 6 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 115 | +0.141 | +36.86€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 115 | +0.141 | +36.86€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 115 | +0.141 | +36.86€ | 0 | 6 |
| ✅ LIQUIDACIONES_15M | 205 | -0.109 | -28.50€ | 6 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 205 | -0.109 | -28.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 49 | -0.108 | -7.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 49 | -0.108 | -7.24€ | 1 | 0 |
| 🚫 LIQUIDACIONES_15M#DOGE | 22 | -0.208 | -5.32€ | 0 | 0 |
| 🚫 LIQUIDACIONES_15M#DOGE#15min | 22 | -0.208 | -5.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 43 | -0.033 | -3.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 43 | -0.033 | -3.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 40 | -0.024 | -2.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 40 | -0.024 | -2.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 46 | -0.167 | -8.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 46 | -0.167 | -8.95€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 177 | -0.159 | -32.34€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 177 | -0.159 | -32.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 59 | -0.172 | -11.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 59 | -0.172 | -11.39€ | 2 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE | 8 | -0.040 | -1.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 8 | -0.040 | -1.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 54 | -0.107 | -8.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 54 | -0.107 | -8.21€ | 1 | 0 |
| 🚫 LIQUIDACIONES_5M#SOL | 35 | -0.203 | -7.91€ | 0 | 0 |
| 🚫 LIQUIDACIONES_5M#SOL#5min | 35 | -0.203 | -7.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 20 | -0.182 | -4.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 20 | -0.182 | -4.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M | 321 | -0.008 | -7.38€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 321 | -0.008 | -7.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 106 | -0.018 | -8.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 106 | -0.018 | -8.62€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 106 | -0.037 | -4.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 106 | -0.037 | -4.12€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 109 | +0.032 | +5.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 109 | +0.032 | +5.36€ | 0 | 1 |
| ✅ MOMENTUM_IBS_15M | 1447 | +0.017 | +2.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 1447 | +0.017 | +2.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 180 | +0.044 | +20.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 180 | +0.044 | +20.05€ | 1 | 3 |
| ✅ MOMENTUM_IBS_15M#BTC | 262 | +0.026 | +0.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 262 | +0.026 | +0.83€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M#DOGE | 209 | -0.002 | -14.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 209 | -0.002 | -14.76€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 272 | +0.033 | +22.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 272 | +0.033 | +22.57€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M#SOL | 261 | +0.006 | -14.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 261 | +0.006 | -14.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 263 | -0.002 | -11.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 263 | -0.002 | -11.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 1981 | -0.028 | +78.09€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 1981 | -0.028 | +78.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 307 | -0.015 | +53.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 307 | -0.015 | +53.08€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 352 | -0.048 | -18.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 352 | -0.048 | -18.98€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 318 | -0.016 | +50.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 318 | -0.016 | +50.60€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 352 | -0.017 | +2.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 352 | -0.017 | +2.38€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 323 | -0.045 | -2.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 323 | -0.045 | -2.48€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 329 | -0.023 | -6.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 329 | -0.023 | -6.52€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 552 | -0.060 | -42.37€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 552 | -0.060 | -42.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 104 | -0.038 | -5.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 104 | -0.038 | -5.15€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 66 | -0.059 | -4.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 66 | -0.059 | -4.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 34 | -0.083 | -3.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 34 | -0.083 | -3.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 108 | -0.118 | -14.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 108 | -0.118 | -14.05€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 139 | -0.032 | -7.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 139 | -0.032 | -7.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 101 | -0.044 | -7.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 101 | -0.044 | -7.92€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M | 971 | +0.002 | +1.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 971 | +0.002 | +1.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 119 | -0.029 | -0.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 119 | -0.029 | -0.78€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 171 | +0.009 | -2.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 171 | +0.009 | -2.20€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 123 | +0.012 | +0.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 123 | +0.012 | +0.52€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#ETH | 194 | +0.005 | +5.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 194 | +0.005 | +5.37€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#SOL | 198 | +0.010 | +3.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 198 | +0.010 | +3.49€ | 0 | 1 |
| ✅ MOMENTUM_IBS_5M#XRP | 166 | -0.006 | -5.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 166 | -0.006 | -5.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 5697 | -0.062 | +208.71€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 5697 | -0.062 | +208.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 842 | -0.091 | +108.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 842 | -0.091 | +108.19€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 1096 | -0.053 | +50.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 1096 | -0.053 | +50.22€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 857 | -0.062 | +66.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 857 | -0.062 | +66.84€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 975 | -0.076 | -55.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 975 | -0.076 | -55.46€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 1030 | -0.037 | -0.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 1030 | -0.037 | -0.62€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 897 | -0.059 | +39.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 897 | -0.059 | +39.54€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 4549 | -0.002 | -53.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 4549 | -0.002 | -53.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 800 | -0.010 | -10.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 800 | -0.010 | -10.35€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 613 | +0.024 | +5.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 613 | +0.024 | +5.87€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 838 | -0.007 | -14.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 838 | -0.007 | -14.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 793 | +0.015 | +4.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 793 | +0.015 | +4.28€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 780 | -0.010 | -14.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 780 | -0.010 | -14.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 725 | -0.020 | -23.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 725 | -0.020 | -23.89€ | 2 | 0 |
| ✅ ORDER_FLOW_5M | 296 | +0.084 | +57.55€ | 1 | 3 |
| ✅ ORDER_FLOW_5M#5min | 160 | +0.105 | +44.95€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 44 | +0.152 | +23.39€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 44 | +0.152 | +23.39€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#DOGE | 28 | +0.100 | +7.69€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 28 | +0.100 | +7.69€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 19 | +0.023 | +1.51€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 19 | +0.023 | +1.51€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL | 33 | +0.100 | +6.66€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 33 | +0.100 | +6.66€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP | 36 | +0.079 | +5.70€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 36 | +0.079 | +5.70€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 221 | -0.141 | -9.51€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 91 | -0.188 | -20.78€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 78 | -0.200 | -17.82€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 13 | -0.065 | -2.96€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 88 | -0.144 | -2.94€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 73 | -0.153 | -4.17€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 15 | -0.066 | +1.23€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 42 | -0.023 | +14.21€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 37 | +0.013 | +15.46€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 5 | -0.054 | -1.25€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 188 | -0.142 | -6.53€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 33 | -0.129 | -2.99€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 121 | -0.256 | -21.75€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 50 | -0.192 | -4.96€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 48 | -0.180 | -3.94€ | 1 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 54 | -0.250 | -11.24€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 52 | -0.241 | -10.22€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 17 | -0.336 | -5.54€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#atexpiry | 16 | -0.311 | -5.04€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 116 | -0.246 | -19.20€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 5 | -0.089 | -2.55€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 49 | +0.245 | +6.70€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC | 17 | -0.022 | -2.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 17 | -0.022 | -2.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 15 | +0.199 | +1.27€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 15 | +0.199 | +1.27€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 17 | +0.380 | +8.37€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 17 | +0.380 | +8.37€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 49 | +0.245 | +6.70€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 81 | -0.090 | -14.74€ | 5 | 0 |
| ✅ STREAK_FADE_15M#15min | 81 | -0.090 | -14.74€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 37 | -0.013 | -3.98€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 37 | -0.013 | -3.98€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 6 | +0.000 | -0.77€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 6 | +0.000 | -0.77€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 35 | -0.149 | -8.47€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 35 | -0.149 | -8.47€ | 0 | 0 |
| ✅ STREAK_FADE_5M | 505 | -0.007 | -19.63€ | 2 | 0 |
| ✅ STREAK_FADE_5M#5min | 505 | -0.007 | -19.63€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 166 | +0.030 | +2.57€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 166 | +0.030 | +2.57€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 152 | -0.013 | -7.43€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 152 | -0.013 | -7.43€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 80 | -0.037 | -8.13€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 80 | -0.037 | -8.13€ | 3 | 0 |
| ✅ STREAK_FADE_5M#XRP | 107 | -0.032 | -6.64€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 107 | -0.032 | -6.64€ | 3 | 1 |
| ✅ STREAK_FADE_60M | 17 | -0.067 | -1.76€ | 0 | 0 |
| ✅ STREAK_FADE_60M#60min | 17 | -0.067 | -1.76€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 10 | -0.083 | -2.14€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 10 | -0.083 | -2.14€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 7 | +0.019 | +0.38€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 7 | +0.019 | +0.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 835 | +0.011 | -2.17€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 835 | +0.011 | -2.17€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 287 | +0.002 | -4.84€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 287 | +0.002 | -4.84€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 145 | -0.010 | -2.15€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 145 | -0.010 | -2.15€ | 3 | 2 |
| ✅ STREAK_MOM_5M#SOL | 231 | +0.015 | -0.64€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 231 | +0.015 | -0.64€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP | 172 | +0.040 | +5.47€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 172 | +0.040 | +5.47€ | 2 | 3 |
| ✅ STRUCT_NO_15M | 2180 | +0.010 | -16.20€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 2180 | +0.010 | -16.20€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 830 | +0.006 | -10.25€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 830 | +0.006 | -10.25€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 848 | +0.015 | -1.99€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 848 | +0.015 | -1.99€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 502 | +0.008 | -3.96€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 502 | +0.008 | -3.96€ | 2 | 0 |
| ✅ UPDOWN_GBM | 3183 | +0.018 | +169.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 1330 | +0.068 | +193.94€ | 1 | 10 |
| ✅ UPDOWN_GBM#240min | 141 | +0.004 | -3.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 1384 | -0.017 | -23.35€ | 4 | 0 |
| ✅ UPDOWN_GBM#60min | 281 | -0.002 | +2.94€ | 3 | 2 |
| ✅ UPDOWN_GBM#BNB | 140 | +0.085 | +27.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 129 | +0.111 | +30.02€ | 0 | 0 |
| 🚫 UPDOWN_GBM#BNB#5min | 9 | -0.102 | -2.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 627 | +0.029 | +48.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 151 | +0.088 | +17.70€ | 3 | 13 |
| ✅ UPDOWN_GBM#BTC#240min | 44 | +0.065 | +3.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 319 | +0.023 | +28.60€ | 1 | 3 |
| ✅ UPDOWN_GBM#BTC#60min | 95 | -0.026 | -3.05€ | 2 | 2 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 361 | +0.001 | +4.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 75 | +0.123 | +22.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 286 | -0.031 | -18.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 716 | +0.043 | +59.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 312 | +0.102 | +60.94€ | 1 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 43 | +0.033 | -0.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 233 | -0.011 | -6.41€ | 4 | 1 |
| ✅ UPDOWN_GBM#ETH#60min | 113 | +0.030 | +5.75€ | 0 | 1 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 659 | -0.002 | -3.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 280 | -0.004 | -5.58€ | 1 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 33 | -0.043 | -3.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 261 | +0.021 | +5.44€ | 2 | 1 |
| ✅ UPDOWN_GBM#SOL#60min | 73 | -0.020 | +0.25€ | 1 | 0 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 678 | -0.003 | +35.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 383 | +0.058 | +68.43€ | 0 | 8 |
| ✅ UPDOWN_GBM#XRP#240min | 19 | -0.113 | -2.93€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 276 | -0.079 | -30.11€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 125 | +0.280 | +7.65€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 125 | +0.280 | +7.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 79 | +0.241 | -4.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 79 | +0.241 | -4.25€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 46 | +0.333 | +11.90€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 46 | +0.333 | +11.90€ | 0 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO | 2131 | -0.067 | +445.25€ | 4 | 4 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 2131 | -0.067 | +445.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 164 | -0.060 | +106.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 164 | -0.060 | +106.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 420 | -0.149 | -14.50€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 420 | -0.149 | -14.50€ | 4 | 1 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 53 | +0.009 | +3.34€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 53 | +0.009 | +3.34€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 148 | +0.027 | +32.60€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 148 | +0.027 | +32.60€ | 2 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 686 | -0.044 | +208.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 686 | -0.044 | +208.27€ | 3 | 1 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 660 | -0.068 | +108.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 660 | -0.068 | +108.84€ | 5 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 13 | -0.022 | -1.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 13 | -0.022 | -1.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 13 | -0.022 | -1.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 13 | -0.022 | -1.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 181 | +0.287 | +123.66€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 181 | +0.287 | +123.66€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 109 | +0.266 | +63.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 109 | +0.266 | +63.12€ | 0 | 12 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 72 | +0.311 | +60.54€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 72 | +0.311 | +60.54€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 368 | -0.062 | -28.63€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#5min | 368 | -0.062 | -28.63€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 233 | -0.006 | -11.15€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 233 | -0.006 | -11.15€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 23 | +0.020 | +3.10€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 23 | +0.020 | +3.10€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 26 | -0.179 | -5.17€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 26 | -0.179 | -5.17€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 29 | -0.177 | -4.93€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 29 | -0.177 | -4.93€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 28 | -0.200 | -4.70€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 28 | -0.200 | -4.70€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 29 | -0.177 | -5.78€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 29 | -0.177 | -5.78€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 957 | +0.285 | +381.93€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 284 | +0.199 | +4.00€ | 0 | 2 |
| ✅ WEEKLY_PRICE#ETH | 304 | +0.255 | +66.23€ | 0 | 1 |
| ✅ WEEKLY_PRICE#SOL | 369 | +0.373 | +311.70€ | 0 | 1 |