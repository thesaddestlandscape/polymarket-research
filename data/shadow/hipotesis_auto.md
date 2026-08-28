# Hipótesis automáticas — 2026-08-28 17:37 UTC
_Generado por shadow_postmortem.py sobre 190903 resoluciones (PNL=+14218.44€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.7` → IC=-0.174 (n=84)

  - _Acción_: SKIP cuando `py_entrada` < 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.269 (n=262)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.284 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.161)

- **PATRÓN** `n_ballena_banda` > `17.0` → IC=+0.173 (n=261)

  - _Acción_: Kelly boost +0.87€ cuando `n_ballena_banda` > 17.0 (IC base=+0.161)

- **PATRÓN** `n_total_lado` > `58.0` → IC=+0.239 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 58.0 (IC base=+0.161)

- **PATRÓN** `banda_hit_calibrado` > `0.8175` → IC=+0.290 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8175 (IC base=+0.161)

- **PATRÓN** `banda_z` > `10.085` → IC=+0.267 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 10.085 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.184 (n=232)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 7.0 (IC base=+0.161)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.185 (n=271)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.01 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `3120.8362` → IC=+0.242 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3120.8362 (IC base=+0.161)

- **PATRÓN** `ballena_activa_n` < `237.0` → IC=+0.293 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 237.0 (IC base=+0.161)

- **PATRÓN** `py_entrada` < `0.805` → IC=+0.130 (n=217)

  - _Acción_: Kelly boost +0.65€ cuando `py_entrada` < 0.805 (IC base=+0.003)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.123 (n=51)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=107)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.284 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.203)

- **PATRÓN** `n_ballena_banda` > `19.0` → IC=+0.214 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `n_ballena_banda` > 19.0 (IC base=+0.203)

- **PATRÓN** `n_total_lado` > `51.0` → IC=+0.240 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 51.0 (IC base=+0.203)

- **PATRÓN** `banda_hit_calibrado` > `0.8191` → IC=+0.310 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8191 (IC base=+0.203)

- **PATRÓN** `banda_z` > `12.414` → IC=+0.314 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 12.414 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.230 (n=157)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.202 (n=122)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.215 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `3120.8362` → IC=+0.241 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3120.8362 (IC base=+0.203)

- **PATRÓN** `ballena_activa_n` < `265.0` → IC=+0.327 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 265.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.126 (n=113)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.495 (IC base=-0.013)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.335` → IC=-0.267 (n=28)

  - _Acción_: SKIP cuando `py_entrada` < 0.335
  - _Potencial_: sin este filtro IC_bueno=+0.188 (n=91)

- **FILTRO** `banda_hit_calibrado` < `0.6329` → IC=-0.232 (n=39)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6329
  - _Potencial_: sin este filtro IC_bueno=+0.232 (n=80)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.139 (n=95)

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

- **PATRÓN** `py_entrada` > `0.335` → IC=+0.188 (n=91)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.335 (IC base=+0.079)

- **PATRÓN** `banda_hit_calibrado` > `0.6329` → IC=+0.232 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6329 (IC base=+0.079)

- **PATRÓN** `banda_z` > `8.059` → IC=+0.174 (n=41)

  - _Acción_: Kelly boost +0.87€ cuando `banda_z` > 8.059 (IC base=+0.079)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.139 (n=95)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.02 (IC base=+0.079)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.495 (IC base=-0.024)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `147.28` → IC=-0.288 (n=2669)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 147.28
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=8008)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `131.38` → IC=-0.277 (n=334)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 131.38
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=1004)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `n_ballenas` < `8.0` → IC=-0.133 (n=235)

  - _Acción_: SKIP cuando `n_ballenas` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=522)

- **FILTRO** `restante_s_al_confirmar` > `626.37` → IC=-0.178 (n=256)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` > 626.37
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=501)

- **FILTRO** `restante_s_al_confirmar` < `409.18` → IC=-0.223 (n=189)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 409.18
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=568)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `113.22` → IC=-0.393 (n=343)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 113.22
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=1031)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `161.45` → IC=-0.160 (n=718)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 161.45
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=2156)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `140.2` → IC=-0.312 (n=619)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 140.2
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=1858)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `155.05` → IC=-0.353 (n=612)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 155.05
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=1245)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.7` → IC=+0.188 (n=5812)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.7 (IC base=+0.096)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.171 (n=1665)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.01 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `2376.0723` → IC=+0.172 (n=1606)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2376.0723 (IC base=+0.096)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.145 (n=3925)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.160 (n=4660)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 7.0 (IC base=+0.143)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.261 (n=3640)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.191 (n=3099)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.02 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `1903.4863` → IC=+0.184 (n=2599)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 1903.4863 (IC base=+0.143)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.223 (n=688)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.397 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.209 (n=846)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.198 (n=621)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 7.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.196 (n=693)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 17.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` < `0.365` → IC=+0.261 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.365 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.190 (n=881)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.01 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `12863.3755` → IC=+0.234 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12863.3755 (IC base=+0.189)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.131 (n=561)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.131 (n=483)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 15.0 (IC base=+0.117)

- **PATRÓN** `py_entrada` > `0.555` → IC=+0.134 (n=555)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` > 0.555 (IC base=+0.117)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=261)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `4886.5239` → IC=+0.160 (n=207)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 4886.5239 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.191 (n=189)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 7.0 (IC base=+0.132)

- **PATRÓN** `py_entrada` < `0.415` → IC=+0.174 (n=311)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.415 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `4171.1992` → IC=+0.149 (n=294)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 4171.1992 (IC base=+0.132)

### FAVORITO_CONFIRMADO#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.134 (n=1302)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.128 (n=1107)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 15.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` > `0.69` → IC=+0.314 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.279 (n=504)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.276)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.277 (n=483)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.276)

- **PATRÓN** `py_entrada` < `0.195` → IC=+0.412 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.195 (IC base=+0.276)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.277 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.276)

- **PATRÓN** `libro_liquidez` > `2877.1517` → IC=+0.283 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2877.1517 (IC base=+0.276)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.153 (n=289)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 15.0 (IC base=+0.135)

- **PATRÓN** `py_entrada` > `0.655` → IC=+0.254 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.655 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.145 (n=398)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.02 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `2117.8922` → IC=+0.162 (n=291)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2117.8922 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `4420.281` → IC=+0.157 (n=141)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 4420.281 (IC base=+0.079)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.195 (n=976)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 6.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.186 (n=862)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 15.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.84` → IC=+0.444 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.84 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.260 (n=227)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` < `0.205` → IC=+0.362 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.205 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.232 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `1923.6066` → IC=+0.250 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1923.6066 (IC base=+0.225)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.219 (n=94)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.184)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.345 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.184)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.230 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.184)

- **PATRÓN** `py_entrada` < `0.355` → IC=+0.199 (n=217)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.355 (IC base=+0.104)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.146 (n=275)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.02 (IC base=+0.104)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `9.0` → IC=-0.286 (n=82)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=86)

- **FILTRO** `py_entrada` > `0.84` → IC=-0.360 (n=41)

  - _Acción_: SKIP cuando `py_entrada` > 0.84
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=127)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.193 (n=4830)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.191 (n=4125)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.187)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.200 (n=2293)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.187)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.168 (n=838)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 11.0 (IC base=+0.166)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.174 (n=1192)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 17.0 (IC base=+0.166)

- **PATRÓN** `py_entrada` < `0.72` → IC=+0.175 (n=1049)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.72 (IC base=+0.166)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `12.0` → IC=-0.375 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.225 (n=67)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=67)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.420 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.324)

- **PATRÓN** `py_entrada` > `0.845` → IC=+0.372 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.845 (IC base=+0.324)

- **PATRÓN** `libro_liquidez` > `2916.5858` → IC=+0.343 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2916.5858 (IC base=+0.324)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.171 (n=1168)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 6.0 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.171 (n=1040)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 15.0 (IC base=+0.164)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.166 (n=1163)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.73 (IC base=+0.164)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.174 (n=813)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` > 0.72 (IC base=+0.164)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.242 (n=1102)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.230)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.322 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.230)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.193 (n=1182)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.183 (n=1017)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 15.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.188 (n=1175)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.73 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.457 (n=228)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.446)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.448 (n=208)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.446)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.451 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.446)

- **PATRÓN** `libro_liquidez` > `3363.9486` → IC=+0.463 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3363.9486 (IC base=+0.446)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.447 (n=92)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.443)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.441 (n=83)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.443)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.440 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.443)

- **PATRÓN** `libro_liquidez` > `13228.9065` → IC=+0.454 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13228.9065 (IC base=+0.443)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.454 (n=85)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.433)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.436 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.433)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.433 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.433)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.433)

- **PATRÓN** `libro_liquidez` > `3860.0656` → IC=+0.476 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3860.0656 (IC base=+0.433)

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
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.195 (n=12165)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 8.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.191 (n=9624)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 12.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.218 (n=9725)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.190)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.134 (n=2457)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 6.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.132 (n=1763)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 12.0 (IC base=+0.128)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.156 (n=1654)

  - _Acción_: Kelly boost +0.78€ cuando `py_entrada` > 0.72 (IC base=+0.128)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.240 (n=2114)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.234)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.281 (n=1201)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.234)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.180 (n=874)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.166)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.167 (n=1641)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 12.0 (IC base=+0.166)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.203 (n=1096)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.166)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.231 (n=1940)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.286 (n=752)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.224 (n=831)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.213)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.239 (n=1326)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.213)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.194 (n=857)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.193 (n=1621)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 12.0 (IC base=+0.186)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.223 (n=1116)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.186)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.203 (n=1768)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.133)

- **PATRÓN** `restante_min` < `3.97` → IC=+0.137 (n=1644)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` < 3.97 (IC base=+0.133)

- **PATRÓN** `restante_min` > `4.93` → IC=+0.159 (n=1735)

  - _Acción_: Kelly boost +0.79€ cuando `restante_min` > 4.93 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.151 (n=2423)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 8.0 (IC base=+0.133)

- **PATRÓN** `lag_apertura_s` < `4.26` → IC=+0.160 (n=1643)

  - _Acción_: Kelly boost +0.80€ cuando `lag_apertura_s` < 4.26 (IC base=+0.133)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.207 (n=893)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.140)

- **PATRÓN** `restante_min` < `3.93` → IC=+0.143 (n=816)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` < 3.93 (IC base=+0.140)

- **PATRÓN** `restante_min` > `4.91` → IC=+0.160 (n=893)

  - _Acción_: Kelly boost +0.80€ cuando `restante_min` > 4.91 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.165 (n=1200)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 8.0 (IC base=+0.140)

- **PATRÓN** `lag_apertura_s` < `7.13` → IC=+0.159 (n=1077)

  - _Acción_: Kelly boost +0.79€ cuando `lag_apertura_s` < 7.13 (IC base=+0.140)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.198 (n=875)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.38 (IC base=+0.127)

- **PATRÓN** `restante_min` < `4.03` → IC=+0.127 (n=824)

  - _Acción_: Kelly boost +0.64€ cuando `restante_min` < 4.03 (IC base=+0.127)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.167 (n=911)

  - _Acción_: Kelly boost +0.84€ cuando `restante_min` > 4.94 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.129 (n=2585)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 5.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.135 (n=1087)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.127)

- **PATRÓN** `lag_apertura_s` < `3.38` → IC=+0.174 (n=823)

  - _Acción_: Kelly boost +0.87€ cuando `lag_apertura_s` < 3.38 (IC base=+0.127)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.318 (n=431)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.297)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.298 (n=549)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.297)

- **PATRÓN** `py_entrada` > `0.825` → IC=+0.384 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.825 (IC base=+0.297)

- **PATRÓN** `libro_liquidez` > `3872.2908` → IC=+0.301 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3872.2908 (IC base=+0.297)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.293 (n=259)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.281)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.280 (n=239)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.281)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.362 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.281)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.286 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `5115.2204` → IC=+0.317 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5115.2204 (IC base=+0.281)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.331 (n=199)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.299)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.308 (n=290)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.299)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.381 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.299)

- **PATRÓN** `libro_liquidez` > `1758.8943` → IC=+0.310 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1758.8943 (IC base=+0.299)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `12.0` → IC=+0.333 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.337)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.346 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.337)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.370 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.337)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.353 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.337)

- **PATRÓN** `libro_liquidez` > `761.0655` → IC=+0.361 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 761.0655 (IC base=+0.337)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.427 (n=271)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.413)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.420 (n=262)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.413)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.421 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.413)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.423 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.413)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.415 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.413)

- **PATRÓN** `libro_liquidez` > `2084.3627` → IC=+0.427 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2084.3627 (IC base=+0.413)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.424 (n=116)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.410)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.424 (n=116)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.410)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.414 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.410)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.417 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.410)

- **PATRÓN** `libro_liquidez` > `5531.9875` → IC=+0.451 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5531.9875 (IC base=+0.410)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.429 (n=110)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.419)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.437 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.419)

- **PATRÓN** `py_entrada` > `0.91` → IC=+0.421 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.91 (IC base=+0.419)

- **PATRÓN** `libro_liquidez` > `2084.3627` → IC=+0.451 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2084.3627 (IC base=+0.419)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.304 (n=315)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.282)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.443 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.282)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.298 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.282)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.304 (n=315)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.282)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.443 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.282)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.298 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.282)

### GBM_LATE_15M
- **PATRÓN** `ibs_20min` > `0.9498` → IC=+0.207 (n=828)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9498 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` > `0.2069` → IC=+0.229 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2069 (IC base=+0.064)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.262` → IC=+0.155 (n=994)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 5.262 (IC base=+0.064)

- **PATRÓN** `volumen_regimen` < `0.6324` → IC=+0.215 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6324 (IC base=+0.064)

- **PATRÓN** `volumen_regimen` > `1.0803` → IC=+0.233 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0803 (IC base=+0.064)

- **PATRÓN** `volumen_pendiente_norm` < `0.1061` → IC=+0.141 (n=1313)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` < 0.1061 (IC base=+0.064)

- **PATRÓN** `volumen_pendiente_norm` > `0.3083` → IC=+0.153 (n=194)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.3083 (IC base=+0.064)

- **PATRÓN** `volumen_spike_ratio` < `2.4282` → IC=+0.150 (n=1204)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4282 (IC base=+0.064)

- **PATRÓN** `ibs_20min` < `0.2105` → IC=+0.134 (n=1672)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.2105 (IC base=+0.031)

- **PATRÓN** `dist_vwap_pct` < `0.1347` → IC=+0.146 (n=786)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.1347 (IC base=+0.031)

- **PATRÓN** `volumen_regimen` < `0.6267` → IC=+0.156 (n=274)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6267 (IC base=+0.031)

- **PATRÓN** `volumen_regimen` > `1.0613` → IC=+0.137 (n=373)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 1.0613 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.307` → IC=+0.280 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.307 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` > `2.924` → IC=+0.243 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.924 (IC base=+0.031)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.244 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.031)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.190 (n=185)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0075 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.169 (n=267)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 8.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.287 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.973` → IC=+0.316 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.973 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2159` → IC=+0.156 (n=91)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.2159 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.158 (n=366)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.04 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `61.0` → IC=+0.133 (n=205)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 61.0 (IC base=+0.128)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.273 (n=214)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.258)

- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.289 (n=107)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0074 (IC base=+0.258)

- **PATRÓN** `drift_60min` |x|≤ `0.2521` → IC=+0.291 (n=280)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2521 (IC base=+0.258)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.261 (n=303)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.258)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.272 (n=287)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.258)

- **PATRÓN** `ibs_20min` < `0.4231` → IC=+0.295 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4231 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.939` → IC=+0.287 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.939 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` > `0.2471` → IC=+0.312 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2471 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` < `1.854` → IC=+0.257 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.854 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` > `2.7667` → IC=+0.308 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7667 (IC base=+0.258)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.321 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `1961.4408` → IC=+0.296 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1961.4408 (IC base=+0.258)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.278 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.258)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.221 (n=281)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.201)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.218 (n=140)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.0937` → IC=+0.234 (n=141)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0937 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.227 (n=426)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` > `0.412` → IC=+0.220 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.412 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `0.2322` → IC=+0.228 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2322 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.343` → IC=+0.221 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.343 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` < `1.2653` → IC=+0.207 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2653 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` > `1.0851` → IC=+0.231 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0851 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` < `0.0964` → IC=+0.205 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0964 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.2699` → IC=+0.207 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2699 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` < `1.4526` → IC=+0.257 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4526 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `11554.4878` → IC=+0.212 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11554.4878 (IC base=+0.201)

- **PATRÓN** `sigma_h` < `0.0023` → IC=+0.163 (n=161)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0023 (IC base=+0.144)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.148 (n=217)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0049 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.0766` → IC=+0.167 (n=160)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.0766 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.153 (n=450)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 7.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.154 (n=486)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 17.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.4406` → IC=+0.177 (n=422)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.4406 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` < `0.1407` → IC=+0.170 (n=410)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1407 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.981` → IC=+0.225 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.981 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `0.6283` → IC=+0.185 (n=160)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.6283 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `1.0218` → IC=+0.144 (n=217)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.0218 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.216 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.7604` → IC=+0.167 (n=250)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.7604 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.4103` → IC=+0.168 (n=375)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.4103 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=619)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `13831.1061` → IC=+0.185 (n=217)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 13831.1061 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `222.0` → IC=+0.173 (n=96)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 222.0 (IC base=+0.144)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `hora_utc` < `6.0` → IC=+0.218 (n=179)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.275 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.02` → IC=+0.273 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.02 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` < `0.1346` → IC=+0.140 (n=398)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` < 0.1346 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.4138` → IC=+0.145 (n=60)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.4138 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.7005` → IC=+0.142 (n=420)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.7005 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.175 (n=457)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.04 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.179 (n=163)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 39.0 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.304 (n=166)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.259)

- **PATRÓN** `drift_60min` |x|≤ `0.46` → IC=+0.270 (n=376)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.46 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.273 (n=254)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.259)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.279 (n=147)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.259)

- **PATRÓN** `ibs_20min` < `0.5208` → IC=+0.302 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5208 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.01` → IC=+0.321 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.01 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.613` → IC=+0.265 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.613 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` > `0.396` → IC=+0.427 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.396 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` > `2.6202` → IC=+0.254 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6202 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.285 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.259)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.243 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 52.0 (IC base=+0.259)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.161 (n=113)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=382)

- **FILTRO** `ibs_20min` < `0.3016` → IC=-0.130 (n=163)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3016
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=332)

- **FILTRO** `ibs_20min` > `0.8686` → IC=-0.168 (n=218)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8686
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=658)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.172 (n=65)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=811)

- **PATRÓN** `dist_vwap_pct` > `0.124` → IC=+0.300 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.124 (IC base=-0.045)

- **PATRÓN** `volumen_regimen` < `0.6297` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6297 (IC base=-0.045)

- **PATRÓN** `volumen_regimen` > `0.7485` → IC=+0.256 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7485 (IC base=-0.045)

- **PATRÓN** `volumen_pendiente_norm` < `0.1203` → IC=+0.227 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1203 (IC base=-0.045)

- **PATRÓN** `volumen_pendiente_norm` > `0.2291` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2291 (IC base=-0.045)

- **PATRÓN** `volumen_spike_ratio` < `1.4943` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4943 (IC base=-0.045)

- **PATRÓN** `volumen_spike_ratio` > `2.1749` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1749 (IC base=-0.045)

- **PATRÓN** `dist_vwap_pct` > `0.2768` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.2768 (IC base=-0.052)

- **PATRÓN** `volumen_pendiente_norm` > `0.0689` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.0689 (IC base=-0.052)

- **PATRÓN** `volumen_spike_ratio` > `2.4256` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.4256 (IC base=-0.052)

- **PATRÓN** `ballena_activa_n` < `134.0` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 134.0 (IC base=-0.052)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.136 (n=31)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=95)

- **FILTRO** `ibs_20min` > `0.5` → IC=-0.133 (n=666)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=716)

- **FILTRO** `sigma_ewma_delta_pct` > `5.027` → IC=-0.152 (n=291)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.027
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=1091)

- **FILTRO** `volumen_pendiente_norm` < `0.0964` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.0964
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

- **FILTRO** `volumen_spike_ratio` > `1.6234` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.6234
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.176 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0055 (IC base=+0.039)

- **PATRÓN** `drift_60min` |x|≤ `0.2929` → IC=+0.121 (n=64)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.61€ cuando `drift_60min` |x|≤ 0.2929 (IC base=+0.039)

- **PATRÓN** `hora_utc` > `23.0` → IC=+0.203 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 23.0 (IC base=+0.039)

- **PATRÓN** `ibs_20min` > `0.5263` → IC=+0.177 (n=63)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.5263 (IC base=+0.039)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.5298` → IC=-0.161 (n=246)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.5298
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=478)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.204 (n=160)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=564)

- **FILTRO** `ibs_20min` > `0.7876` → IC=-0.167 (n=310)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7876
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=934)

- **FILTRO** `sigma_ewma_delta_pct` > `6.731` → IC=-0.152 (n=202)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.731
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=1042)

- **PATRÓN** `dist_vwap_pct` < `0.2396` → IC=+0.175 (n=38)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.2396 (IC base=-0.106)

- **PATRÓN** `volumen_regimen` > `0.6932` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 0.6932 (IC base=-0.106)

- **PATRÓN** `dist_vwap_pct` < `0.2072` → IC=+0.225 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2072 (IC base=-0.043)

- **PATRÓN** `volumen_regimen` < `0.6973` → IC=+0.230 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6973 (IC base=-0.043)

- **PATRÓN** `volumen_regimen` > `1.1434` → IC=+0.250 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1434 (IC base=-0.043)

- **PATRÓN** `volumen_spike_ratio` > `1.8639` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.8639 (IC base=-0.043)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.136 (n=1414)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.0078 (IC base=+0.055)

- **PATRÓN** `ibs_20min` > `0.9463` → IC=+0.245 (n=1037)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9463 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` > `1.2681` → IC=+0.290 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2681 (IC base=+0.055)

- **PATRÓN** `volumen_regimen` > `1.1729` → IC=+0.209 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1729 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` < `0.1149` → IC=+0.179 (n=1406)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` < 0.1149 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.2486` → IC=+0.202 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2486 (IC base=+0.055)

- **PATRÓN** `volumen_spike_ratio` < `1.4785` → IC=+0.204 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4785 (IC base=+0.055)

- **PATRÓN** `ballena_activa_n` < `99.0` → IC=+0.276 (n=894)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 99.0 (IC base=+0.055)

- **PATRÓN** `ibs_20min` < `0.093` → IC=+0.191 (n=1278)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.093 (IC base=+0.041)

- **PATRÓN** `dist_vwap_pct` > `0.7716` → IC=+0.225 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7716 (IC base=+0.041)

- **PATRÓN** `dist_vwap_pct` < `0.2189` → IC=+0.211 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2189 (IC base=+0.041)

- **PATRÓN** `volumen_regimen` < `0.8624` → IC=+0.210 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8624 (IC base=+0.041)

- **PATRÓN** `volumen_regimen` > `1.2365` → IC=+0.238 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2365 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.2567` → IC=+0.366 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2567 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` > `2.3783` → IC=+0.287 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3783 (IC base=+0.041)

- **PATRÓN** `ballena_activa_n` < `60.0` → IC=+0.269 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 60.0 (IC base=+0.041)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2469` → IC=-0.157 (n=214)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2469
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=435)

- **FILTRO** `sigma_ewma_delta_pct` > `2.143` → IC=-0.172 (n=248)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.143
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=564)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.34` → IC=+0.159 (n=124)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 5.34 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.211` → IC=+0.342 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.211 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` > `2.7084` → IC=+0.242 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7084 (IC base=-0.002)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.400 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 45.0 (IC base=-0.002)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.8836` → IC=-0.149 (n=289)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8836
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=868)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `drift_60min` |x|≤ `0.0753` → IC=+0.213 (n=165)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0753 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.257 (n=175)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.192)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.290 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.165` → IC=+0.300 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.165 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` < `0.1415` → IC=+0.202 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1415 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` > `0.4152` → IC=+0.190 (n=56)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.4152 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` < `2.52` → IC=+0.200 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.52 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` > `4.1999` → IC=+0.191 (n=137)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 4.1999 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.219 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `1936.1714` → IC=+0.207 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1936.1714 (IC base=+0.192)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.224 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.192)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.339 (n=247)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.335)

- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.335 (n=95)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0095 (IC base=+0.335)

- **PATRÓN** `drift_60min` |x|≤ `0.252` → IC=+0.342 (n=188)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.252 (IC base=+0.335)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.385 (n=137)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.335)

- **PATRÓN** `ibs_20min` < `0.3296` → IC=+0.348 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3296 (IC base=+0.335)

- **PATRÓN** `ibs_20min` > `0.1333` → IC=+0.341 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1333 (IC base=+0.335)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.492` → IC=+0.345 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.492 (IC base=+0.335)

- **PATRÓN** `volumen_pendiente_norm` > `0.3635` → IC=+0.439 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3635 (IC base=+0.335)

- **PATRÓN** `volumen_spike_ratio` < `1.7067` → IC=+0.331 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7067 (IC base=+0.335)

- **PATRÓN** `volumen_spike_ratio` > `1.9441` → IC=+0.343 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9441 (IC base=+0.335)

- **PATRÓN** `libro_liquidez` > `1874.4798` → IC=+0.375 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1874.4798 (IC base=+0.335)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.337 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 29.0 (IC base=+0.335)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.175 (n=124)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=373)

- **FILTRO** `dist_vwap_pct` < `0.7343` → IC=-0.211 (n=43)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.7343
  - _Potencial_: sin este filtro IC_bueno=+0.233 (n=28)

- **FILTRO** `volumen_regimen` > `1.0041` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.0041
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=54)

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
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=953)

- **PATRÓN** `dist_vwap_pct` > `0.7343` → IC=+0.233 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7343 (IC base=-0.081)

- **PATRÓN** `volumen_spike_ratio` < `1.4` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4 (IC base=-0.081)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7468` → IC=-0.130 (n=458)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7468
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=236)

- **FILTRO** `ibs_20min` > `0.75` → IC=-0.198 (n=230)

  - _Acción_: SKIP cuando `ibs_20min` > 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=691)

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

- **PATRÓN** `ibs_20min` > `0.8571` → IC=+0.268 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8571 (IC base=-0.013)

- **PATRÓN** `dist_vwap_pct` > `0.6469` → IC=+0.293 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6469 (IC base=-0.013)

- **PATRÓN** `volumen_regimen` < `0.8566` → IC=+0.189 (n=133)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.8566 (IC base=-0.013)

- **PATRÓN** `volumen_regimen` > `1.1463` → IC=+0.250 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1463 (IC base=-0.013)

- **PATRÓN** `volumen_pendiente_norm` < `0.1202` → IC=+0.174 (n=185)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` < 0.1202 (IC base=-0.013)

- **PATRÓN** `volumen_pendiente_norm` > `0.2649` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2649 (IC base=-0.013)

- **PATRÓN** `volumen_spike_ratio` < `1.4599` → IC=+0.208 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4599 (IC base=-0.013)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.243 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 50.0 (IC base=-0.013)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0249` → IC=+0.326 (n=199)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0249 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.238 (n=223)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.230 (n=527)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.898` → IC=+0.307 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.898 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `1.3546` → IC=+0.348 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.3546 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.201` → IC=+0.281 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.201 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `0.8369` → IC=+0.259 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8369 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` < `0.0805` → IC=+0.231 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0805 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2797` → IC=+0.263 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2797 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `2.1781` → IC=+0.240 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1781 (IC base=+0.226)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.237 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2452.6608` → IC=+0.235 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2452.6608 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.280 (n=207)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.272)

- **PATRÓN** `sigma_h` > `0.0237` → IC=+0.284 (n=206)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0237 (IC base=+0.272)

- **PATRÓN** `drift_60min` |x|≤ `0.2933` → IC=+0.276 (n=413)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2933 (IC base=+0.272)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.281 (n=579)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.272)

- **PATRÓN** `ibs_20min` < `0.2766` → IC=+0.330 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2766 (IC base=+0.272)

- **PATRÓN** `dist_vwap_pct` < `0.2695` → IC=+0.284 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2695 (IC base=+0.272)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.938` → IC=+0.319 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.938 (IC base=+0.272)

- **PATRÓN** `volumen_regimen` > `1.2624` → IC=+0.308 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2624 (IC base=+0.272)

- **PATRÓN** `volumen_pendiente_norm` > `0.2896` → IC=+0.382 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2896 (IC base=+0.272)

- **PATRÓN** `volumen_spike_ratio` > `2.1632` → IC=+0.293 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1632 (IC base=+0.272)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.191 (n=892)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0103 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.3391` → IC=+0.160 (n=2355)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.3391 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.164 (n=2701)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 6.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.282 (n=1317)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.8078` → IC=+0.253 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8078 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.423` → IC=+0.243 (n=1113)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.423 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` > `0.6895` → IC=+0.171 (n=1658)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 0.6895 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.2389` → IC=+0.188 (n=504)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2389 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `2.2895` → IC=+0.159 (n=2132)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.2895 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` > `1.8546` → IC=+0.151 (n=1615)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.8546 (IC base=+0.157)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.165 (n=2145)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `3204.0646` → IC=+0.182 (n=1214)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 3204.0646 (IC base=+0.157)

- **PATRÓN** `ballena_activa_n` < `113.0` → IC=+0.180 (n=1394)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 113.0 (IC base=+0.157)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.201 (n=1621)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.0821` → IC=+0.213 (n=811)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0821 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.215 (n=1221)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` < `0.4107` → IC=+0.241 (n=2431)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4107 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` < `0.2203` → IC=+0.182 (n=1973)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.2203 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.929` → IC=+0.217 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.929 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `1.1777` → IC=+0.171 (n=1926)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.1777 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` > `0.8519` → IC=+0.174 (n=1284)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 0.8519 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.2919` → IC=+0.261 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2919 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `2.6688` → IC=+0.212 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6688 (IC base=+0.187)

- **PATRÓN** `ballena_activa_n` < `124.0` → IC=+0.197 (n=1224)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 124.0 (IC base=+0.187)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.155 (n=192)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0059 (IC base=+0.152)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.210 (n=198)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.2695` → IC=+0.160 (n=436)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.2695 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.178 (n=396)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 15.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.752` → IC=+0.304 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.752 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.1423` → IC=+0.192 (n=105)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.1423 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `1.4412` → IC=+0.138 (n=357)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.4412 (IC base=+0.152)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.178 (n=296)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.04 (IC base=+0.152)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.257 (n=204)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.255)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.268 (n=231)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.255)

- **PATRÓN** `drift_60min` |x|≤ `0.3311` → IC=+0.282 (n=232)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3311 (IC base=+0.255)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.272 (n=204)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.255)

- **PATRÓN** `ibs_20min` < `0.4013` → IC=+0.286 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4013 (IC base=+0.255)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.501` → IC=+0.273 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.501 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` > `0.1779` → IC=+0.276 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1779 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` < `1.9291` → IC=+0.272 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9291 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` > `2.8455` → IC=+0.293 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8455 (IC base=+0.255)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.333 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `1952.5048` → IC=+0.335 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1952.5048 (IC base=+0.255)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.250 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.255)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.193 (n=340)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0062 (IC base=+0.170)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.187 (n=129)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0072 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.4326` → IC=+0.174 (n=385)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.4326 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.196 (n=389)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 6.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` > `0.6307` → IC=+0.220 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6307 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` > `0.2143` → IC=+0.234 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2143 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.599` → IC=+0.239 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.599 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` < `0.6395` → IC=+0.179 (n=129)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.6395 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` > `1.0855` → IC=+0.195 (n=175)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` > 1.0855 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.2234` → IC=+0.240 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2234 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` < `1.3802` → IC=+0.227 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3802 (IC base=+0.170)

- **PATRÓN** `libro_liquidez` > `12677.1215` → IC=+0.183 (n=257)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 12677.1215 (IC base=+0.170)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.170 (n=483)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0059 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.2334` → IC=+0.174 (n=425)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2334 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.173 (n=442)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 7.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.4271` → IC=+0.195 (n=483)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.4271 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `0.1617` → IC=+0.177 (n=478)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.1617 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.392` → IC=+0.234 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.392 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.705` → IC=+0.216 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.705 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.17` → IC=+0.224 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.17 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.6037` → IC=+0.161 (n=375)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.6037 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.41` → IC=+0.150 (n=375)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.41 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `14712.0502` → IC=+0.181 (n=161)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 14712.0502 (IC base=+0.151)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `drift_60min` |x|≤ `0.1502` → IC=+0.177 (n=258)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.1502 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.195 (n=129)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.165)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.229 (n=149)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.307 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.958` → IC=+0.292 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.958 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` < `0.226` → IC=+0.162 (n=326)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` < 0.226 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `1.9744` → IC=+0.212 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9744 (IC base=+0.165)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.192 (n=342)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.04 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `1947.8684` → IC=+0.172 (n=129)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 1947.8684 (IC base=+0.165)

- **PATRÓN** `sigma_h` < `0.0101` → IC=+0.290 (n=274)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0101 (IC base=+0.268)

- **PATRÓN** `drift_60min` |x|≤ `0.2281` → IC=+0.316 (n=183)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2281 (IC base=+0.268)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.313 (n=185)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.268)

- **PATRÓN** `ibs_20min` < `0.3077` → IC=+0.325 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3077 (IC base=+0.268)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.311` → IC=+0.344 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.311 (IC base=+0.268)

- **PATRÓN** `volumen_pendiente_norm` > `0.3709` → IC=+0.443 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3709 (IC base=+0.268)

- **PATRÓN** `volumen_spike_ratio` > `1.671` → IC=+0.267 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.671 (IC base=+0.268)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.211 (n=385)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0093 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.5056` → IC=+0.190 (n=385)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.5056 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.192 (n=397)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 6.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.4362` → IC=+0.228 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4362 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.9552` → IC=+0.232 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9552 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.408` → IC=+0.329 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.408 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `0.7026` → IC=+0.194 (n=344)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` > 0.7026 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.101` → IC=+0.214 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.101 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` < `1.4303` → IC=+0.191 (n=124)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.4303 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.5013` → IC=+0.230 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5013 (IC base=+0.173)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.175 (n=441)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `8750.1763` → IC=+0.202 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8750.1763 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.185 (n=141)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 115.0 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.245 (n=155)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.3825` → IC=+0.158 (n=463)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.3825 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.175 (n=232)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 14.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.154 (n=177)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 5.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.3583` → IC=+0.210 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3583 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.569` → IC=+0.188 (n=107)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 12.569 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `1.176` → IC=+0.154 (n=463)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.176 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` > `0.6106` → IC=+0.156 (n=463)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.6106 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.1018` → IC=+0.167 (n=142)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.1018 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `1.9099` → IC=+0.175 (n=238)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.9099 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `2.5391` → IC=+0.153 (n=119)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 2.5391 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `10807.3356` → IC=+0.162 (n=155)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 10807.3356 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `124.0` → IC=+0.148 (n=123)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 124.0 (IC base=+0.141)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.186 (n=240)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0109 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.140 (n=554)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` > `0.5588` → IC=+0.183 (n=528)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.5588 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `0.9064` → IC=+0.271 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9064 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.259` → IC=+0.300 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.259 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` > `0.6193` → IC=+0.138 (n=528)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.6193 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.163` → IC=+0.131 (n=518)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.163 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.0948` → IC=+0.122 (n=186)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` > 0.0948 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.4403` → IC=+0.129 (n=165)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.4403 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `1.7764` → IC=+0.133 (n=330)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 1.7764 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `3238.6192` → IC=+0.225 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3238.6192 (IC base=+0.120)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.180 (n=148)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.005 (IC base=+0.138)

- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.205 (n=147)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.217 (n=150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.4085` → IC=+0.235 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4085 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.7275` → IC=+0.139 (n=95)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.7275 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.2288` → IC=+0.153 (n=419)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.2288 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.213` → IC=+0.199 (n=174)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 3.213 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.1607` → IC=+0.149 (n=440)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.1607 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `0.853` → IC=+0.171 (n=293)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 0.853 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2176` → IC=+0.214 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2176 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.2667` → IC=+0.224 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2667 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `2115.5526` → IC=+0.192 (n=293)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2115.5526 (IC base=+0.138)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0239` → IC=+0.199 (n=254)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0239 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.1642` → IC=+0.198 (n=246)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.1642 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.204 (n=194)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.9117` → IC=+0.265 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9117 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `1.0522` → IC=+0.250 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0522 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.138` → IC=+0.240 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.138 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` > `0.6793` → IC=+0.185 (n=500)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 0.6793 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.2392` → IC=+0.250 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2392 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `2.1464` → IC=+0.187 (n=458)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 2.1464 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.174 (n=568)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `2452.6608` → IC=+0.170 (n=559)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2452.6608 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.275 (n=238)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.6757` → IC=+0.234 (n=544)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6757 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.236 (n=259)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.254 (n=258)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` < `0.375` → IC=+0.264 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.375 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` < `0.2569` → IC=+0.234 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2569 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.181` → IC=+0.288 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.181 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` > `0.6963` → IC=+0.245 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6963 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.355 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `2.6983` → IC=+0.257 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6983 (IC base=+0.223)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.198 (n=200)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.099)

- **PATRÓN** `ibs_20min` > `0.6176` → IC=+0.165 (n=457)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.6176 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `0.8459` → IC=+0.264 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8459 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.314` → IC=+0.178 (n=141)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 8.314 (IC base=+0.099)

- **PATRÓN** `volumen_pendiente_norm` > `0.18` → IC=+0.162 (n=140)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.18 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `2664.8945` → IC=+0.139 (n=341)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2664.8945 (IC base=+0.099)

- **PATRÓN** `ibs_20min` < `0.3033` → IC=+0.149 (n=320)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.3033 (IC base=+0.059)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.783` → IC=+0.161 (n=110)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 7.783 (IC base=+0.059)

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

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.233 (n=58)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.109)

- **PATRÓN** `drift_60min` |x|≤ `0.3657` → IC=+0.142 (n=174)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.3657 (IC base=+0.109)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.172 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 4.0 (IC base=+0.109)

- **PATRÓN** `ibs_20min` < `0.5916` → IC=+0.177 (n=153)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.5916 (IC base=+0.109)

- **PATRÓN** `dist_vwap_pct` < `0.2319` → IC=+0.129 (n=165)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.2319 (IC base=+0.109)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.767` → IC=+0.222 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.767 (IC base=+0.109)

- **PATRÓN** `volumen_regimen` < `1.1856` → IC=+0.136 (n=174)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.1856 (IC base=+0.109)

- **PATRÓN** `volumen_pendiente_norm` > `0.0817` → IC=+0.293 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0817 (IC base=+0.109)

- **PATRÓN** `volumen_spike_ratio` < `1.7313` → IC=+0.152 (n=110)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.7313 (IC base=+0.109)

- **PATRÓN** `volumen_spike_ratio` > `1.4187` → IC=+0.127 (n=164)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 1.4187 (IC base=+0.109)

- **PATRÓN** `ballena_activa_n` < `316.0` → IC=+0.130 (n=125)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 316.0 (IC base=+0.109)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **FILTRO** `sigma_h` > `0.0064` → IC=-0.231 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0064
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=76)

- **FILTRO** `ibs_20min` > `0.6889` → IC=-0.269 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6889
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=76)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.289 (n=88)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.291)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.324 (n=66)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.349 (n=51)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.291)

- **PATRÓN** `ibs_20min` > `0.6988` → IC=+0.313 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6988 (IC base=+0.291)

- **PATRÓN** `dist_vwap_pct` > `0.1466` → IC=+0.351 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1466 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.561` → IC=+0.377 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.561 (IC base=+0.291)

- **PATRÓN** `volumen_regimen` < `0.7015` → IC=+0.370 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7015 (IC base=+0.291)

- **PATRÓN** `volumen_regimen` > `1.0786` → IC=+0.308 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0786 (IC base=+0.291)

- **PATRÓN** `volumen_pendiente_norm` > `0.1782` → IC=+0.400 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1782 (IC base=+0.291)

- **PATRÓN** `volumen_spike_ratio` < `2.3129` → IC=+0.302 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3129 (IC base=+0.291)

- **PATRÓN** `volumen_spike_ratio` > `1.8383` → IC=+0.315 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8383 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `2746.5037` → IC=+0.302 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2746.5037 (IC base=+0.291)

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
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=151)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.155 (n=56)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.027)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.194 (n=70)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 1.0 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` > `0.4915` → IC=+0.179 (n=26)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.4915 (IC base=+0.027)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `hora_utc` > `16.0` → IC=+0.177 (n=29)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 16.0 (IC base=+0.080)

- **PATRÓN** `ibs_20min` > `0.7425` → IC=+0.132 (n=55)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` > 0.7425 (IC base=+0.080)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.745` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.745 (IC base=+0.080)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.129 (n=60)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.080)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 9.0 (IC base=+0.080)

- **PATRÓN** `ibs_20min` < `0.0488` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0488 (IC base=+0.048)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.183 (n=2094)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0066 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.157 (n=3185)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 6.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.9396` → IC=+0.289 (n=1422)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9396 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `1.0953` → IC=+0.236 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0953 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.529` → IC=+0.227 (n=1828)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.529 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.8783` → IC=+0.145 (n=1475)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.8783 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` > `1.0803` → IC=+0.153 (n=1003)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 1.0803 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.1654` → IC=+0.174 (n=811)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1654 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.3086` → IC=+0.150 (n=2479)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.3086 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.8603` → IC=+0.156 (n=1878)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.8603 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=2510)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `2484.1984` → IC=+0.173 (n=2091)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2484.1984 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.188 (n=1551)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 143.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.217 (n=1905)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.191)

- **PATRÓN** `drift_60min` |x|≤ `0.4845` → IC=+0.201 (n=2854)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4845 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.195 (n=1025)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 17.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.206 (n=1029)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` < `0.562` → IC=+0.246 (n=2854)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.562 (IC base=+0.191)

- **PATRÓN** `dist_vwap_pct` < `0.4258` → IC=+0.182 (n=2100)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.4258 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.419` → IC=+0.206 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.419 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.657` → IC=+0.195 (n=2676)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 2.657 (IC base=+0.191)

- **PATRÓN** `volumen_regimen` < `0.6236` → IC=+0.184 (n=706)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6236 (IC base=+0.191)

- **PATRÓN** `volumen_regimen` > `1.2098` → IC=+0.176 (n=705)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 1.2098 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` > `0.2882` → IC=+0.273 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2882 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` > `2.3099` → IC=+0.210 (n=977)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3099 (IC base=+0.191)

- **PATRÓN** `ballena_activa_n` < `176.0` → IC=+0.171 (n=1728)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 176.0 (IC base=+0.191)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.223 (n=233)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.154 (n=521)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 6.0 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.173 (n=347)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 11.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.311 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.341` → IC=+0.303 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.341 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.2113` → IC=+0.220 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2113 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.9052` → IC=+0.147 (n=287)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.9052 (IC base=+0.151)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.199 (n=320)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.301 (n=219)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.269)

- **PATRÓN** `drift_60min` |x|≤ `0.1082` → IC=+0.315 (n=144)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1082 (IC base=+0.269)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.273 (n=311)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.269)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.282 (n=296)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.269)

- **PATRÓN** `ibs_20min` < `0.562` → IC=+0.312 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.562 (IC base=+0.269)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.116` → IC=+0.289 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.116 (IC base=+0.269)

- **PATRÓN** `volumen_pendiente_norm` > `0.3023` → IC=+0.321 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3023 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` > `2.7638` → IC=+0.321 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7638 (IC base=+0.269)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.315 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.269)

- **PATRÓN** `libro_liquidez` > `1964.426` → IC=+0.311 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1964.426 (IC base=+0.269)

- **PATRÓN** `ballena_activa_n` < `74.0` → IC=+0.253 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 74.0 (IC base=+0.269)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.161 (n=169)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0029 (IC base=+0.151)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.176 (n=168)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0071 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.4183` → IC=+0.153 (n=502)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.4183 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.171 (n=508)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 6.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.3308` → IC=+0.206 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3308 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.2661` → IC=+0.230 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2661 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.622` → IC=+0.209 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.622 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `1.2714` → IC=+0.157 (n=502)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.2714 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` > `1.099` → IC=+0.170 (n=228)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 1.099 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` < `0.0733` → IC=+0.168 (n=404)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` < 0.0733 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.2057` → IC=+0.197 (n=97)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2057 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.4168` → IC=+0.181 (n=453)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 2.4168 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.3642` → IC=+0.170 (n=453)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.3642 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `12219.7812` → IC=+0.167 (n=334)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 12219.7812 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.174 (n=476)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0061 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.1754` → IC=+0.185 (n=316)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.1754 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.173 (n=442)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 7.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.181 (n=478)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 17.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` < `0.5681` → IC=+0.202 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5681 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` < `0.1493` → IC=+0.182 (n=419)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.1493 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.842` → IC=+0.220 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.842 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `0.6257` → IC=+0.231 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6257 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.1472` → IC=+0.278 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1472 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `2.5136` → IC=+0.187 (n=378)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 2.5136 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `1.5117` → IC=+0.185 (n=338)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.5117 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.167 (n=613)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `12755.4107` → IC=+0.182 (n=215)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 12755.4107 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `307.0` → IC=+0.184 (n=93)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 307.0 (IC base=+0.167)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.263 (n=188)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0079 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.249 (n=193)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` > `0.7037` → IC=+0.262 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7037 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.275` → IC=+0.347 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.275 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` < `0.2217` → IC=+0.190 (n=349)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.2217 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` < `1.9553` → IC=+0.199 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9553 (IC base=+0.186)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.217 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.186)

- **PATRÓN** `libro_liquidez` > `1835.7067` → IC=+0.198 (n=276)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 1835.7067 (IC base=+0.186)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.236 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 48.0 (IC base=+0.186)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.321 (n=138)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.245)

- **PATRÓN** `drift_60min` |x|≤ `0.2115` → IC=+0.251 (n=275)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2115 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.250 (n=278)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.281 (n=162)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.5567` → IC=+0.309 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5567 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.153` → IC=+0.276 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.153 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.3579` → IC=+0.348 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3579 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` < `1.7665` → IC=+0.247 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7665 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `2.4083` → IC=+0.218 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4083 (IC base=+0.245)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.275 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.202 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 58.0 (IC base=+0.245)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0089` → IC=+0.153 (n=503)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0089 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.1495` → IC=+0.138 (n=222)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.1495 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.165 (n=458)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 8.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.3491` → IC=+0.195 (n=503)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.3491 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.8095` → IC=+0.218 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8095 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.485` → IC=+0.186 (n=243)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 4.485 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.6268` → IC=+0.176 (n=168)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6268 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `1.2091` → IC=+0.159 (n=168)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 1.2091 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2693` → IC=+0.265 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2693 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.4658` → IC=+0.234 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4658 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `5139.067` → IC=+0.218 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5139.067 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `162.0` → IC=+0.179 (n=250)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 162.0 (IC base=+0.138)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.197 (n=143)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0032 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.5115` → IC=+0.162 (n=427)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.5115 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.168 (n=305)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 11.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.6499` → IC=+0.181 (n=427)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.6499 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.1716` → IC=+0.152 (n=202)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.1716 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` < `0.3847` → IC=+0.147 (n=423)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.3847 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.901` → IC=+0.211 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.901 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `0.5857` → IC=+0.148 (n=143)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.5857 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `0.6484` → IC=+0.154 (n=382)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.6484 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.2392` → IC=+0.292 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2392 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.8173` → IC=+0.163 (n=247)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.8173 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `2.4896` → IC=+0.196 (n=123)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.4896 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `9771.3836` → IC=+0.204 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9771.3836 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `136.0` → IC=+0.203 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 136.0 (IC base=+0.144)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.143 (n=253)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0113 (IC base=+0.091)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.134 (n=380)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 12.0 (IC base=+0.091)

- **PATRÓN** `ibs_20min` > `0.4872` → IC=+0.176 (n=556)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.4872 (IC base=+0.091)

- **PATRÓN** `dist_vwap_pct` > `0.8962` → IC=+0.232 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8962 (IC base=+0.091)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.478` → IC=+0.226 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.478 (IC base=+0.091)

- **PATRÓN** `libro_liquidez` > `2971.573` → IC=+0.266 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2971.573 (IC base=+0.091)

- **PATRÓN** `ballena_activa_n` < `66.0` → IC=+0.154 (n=330)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 66.0 (IC base=+0.091)

- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.184 (n=172)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0055 (IC base=+0.117)

- **PATRÓN** `drift_60min` |x|≤ `0.1238` → IC=+0.155 (n=172)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1238 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.170 (n=237)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 15.0 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.139 (n=178)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 5.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.5938` → IC=+0.202 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5938 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` < `0.4894` → IC=+0.143 (n=480)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.4894 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.087` → IC=+0.140 (n=501)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 3.087 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.7141` → IC=+0.145 (n=226)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.7141 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.0719` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.0719 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `2.0903` → IC=+0.144 (n=321)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.0903 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` > `1.7794` → IC=+0.145 (n=243)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.7794 (IC base=+0.117)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.124 (n=536)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2673.0949` → IC=+0.172 (n=233)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2673.0949 (IC base=+0.117)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0272` → IC=+0.218 (n=218)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0272 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.188 (n=654)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 6.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` > `0.9588` → IC=+0.299 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9588 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` > `1.0171` → IC=+0.286 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0171 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.116` → IC=+0.248 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.116 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` > `1.0359` → IC=+0.208 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0359 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.1687` → IC=+0.240 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1687 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` < `2.2016` → IC=+0.175 (n=530)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 2.2016 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `1.8148` → IC=+0.188 (n=402)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 1.8148 (IC base=+0.177)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.188 (n=656)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.01 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `2453.0908` → IC=+0.180 (n=652)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 2453.0908 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.216 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.177)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.291 (n=309)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.493` → IC=+0.227 (n=618)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.493 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.225 (n=655)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` < `0.493` → IC=+0.282 (n=703)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.493 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` < `0.1699` → IC=+0.235 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1699 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.6` → IC=+0.292 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.6 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` > `1.0866` → IC=+0.235 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0866 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.2827` → IC=+0.326 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2827 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `2.2043` → IC=+0.231 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2043 (IC base=+0.219)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.187 (n=420)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 37.0 (IC base=+0.219)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=1206)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.160 (n=286)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.106)

- **PATRÓN** `ibs_20min` > `0.9174` → IC=+0.163 (n=265)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.9174 (IC base=+0.106)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.379` → IC=+0.156 (n=123)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 10.379 (IC base=+0.106)

- **PATRÓN** `volumen_pendiente_norm` > `0.245` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.245 (IC base=+0.106)

- **PATRÓN** `volumen_spike_ratio` < `1.438` → IC=+0.135 (n=261)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.438 (IC base=+0.106)

- **PATRÓN** `volumen_spike_ratio` > `2.6002` → IC=+0.135 (n=261)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.6002 (IC base=+0.106)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.189 (n=307)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0037 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.3821` → IC=+0.163 (n=806)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.3821 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.159 (n=321)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.194 (n=331)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 4.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.193` → IC=+0.162 (n=403)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.193 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.0889` → IC=+0.145 (n=916)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.0889 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.6915` → IC=+0.157 (n=176)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.6915 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.162` → IC=+0.149 (n=918)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 6.162 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `1.2232` → IC=+0.151 (n=892)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.2232 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` < `0.0935` → IC=+0.150 (n=822)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` < 0.0935 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `2.5638` → IC=+0.159 (n=908)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.5638 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.425` → IC=+0.149 (n=908)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.425 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.146 (n=1206)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `10633.6945` → IC=+0.149 (n=611)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 10633.6945 (IC base=+0.141)

### GBM_LATE_5M#BTC#5min
- **FILTRO** `sigma_ewma_delta_pct` > `2.944` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.944
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=115)

- **FILTRO** `volumen_pendiente_norm` > `0.1016` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1016
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=117)

- **PATRÓN** `volumen_spike_ratio` < `1.4949` → IC=+0.138 (n=45)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.4949 (IC base=+0.047)

- **PATRÓN** `libro_liquidez` > `12574.1361` → IC=+0.135 (n=102)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 12574.1361 (IC base=+0.047)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.192 (n=222)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0036 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.3904` → IC=+0.150 (n=504)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.3904 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.187 (n=180)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.186 (n=189)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.1762` → IC=+0.174 (n=222)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.1762 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.3799` → IC=+0.142 (n=336)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.3799 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.6584` → IC=+0.196 (n=67)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.6584 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.363` → IC=+0.158 (n=504)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 6.363 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.1909` → IC=+0.156 (n=504)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.1909 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `0.6229` → IC=+0.146 (n=504)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.6229 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.0698` → IC=+0.168 (n=239)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.0698 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.5675` → IC=+0.157 (n=502)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.5675 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.8123` → IC=+0.149 (n=334)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.8123 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `11974.8913` → IC=+0.153 (n=450)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 11974.8913 (IC base=+0.140)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.180 (n=98)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0104 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.198 (n=104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 11.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` < `0.4662` → IC=+0.157 (n=65)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.4662 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.9219` → IC=+0.265 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9219 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.371` → IC=+0.271 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.371 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.215` → IC=+0.182 (n=42)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.215 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.8976` → IC=+0.147 (n=66)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 2.8976 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `1824.9454` → IC=+0.164 (n=147)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 1824.9454 (IC base=+0.124)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.160 (n=295)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0094 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.4394` → IC=+0.151 (n=259)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.4394 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.188 (n=107)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 18.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` < `0.5342` → IC=+0.128 (n=197)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.5342 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.8027` → IC=+0.162 (n=134)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.8027 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.8504` → IC=+0.162 (n=75)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.8504 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` < `0.2211` → IC=+0.136 (n=245)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.2211 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.031` → IC=+0.167 (n=46)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.031 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.861` → IC=+0.133 (n=295)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 6.861 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.6457` → IC=+0.173 (n=99)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6457 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` < `0.1191` → IC=+0.129 (n=265)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1191 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.1754` → IC=+0.134 (n=91)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.1754 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.4204` → IC=+0.163 (n=96)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.4204 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `1.8447` → IC=+0.137 (n=191)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.8447 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `8958.19` → IC=+0.145 (n=263)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 8958.19 (IC base=+0.127)

- **PATRÓN** `sigma_h` < `0.0089` → IC=+0.148 (n=268)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0089 (IC base=+0.134)

- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.144 (n=178)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0062 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.4118` → IC=+0.188 (n=235)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.4118 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.161 (n=181)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 10.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.612` → IC=+0.146 (n=235)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.612 (IC base=+0.134)

- **PATRÓN** `ibs_20min` > `0.1055` → IC=+0.158 (n=267)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.1055 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `0.1508` → IC=+0.157 (n=103)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1508 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.368` → IC=+0.200 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.368 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.6472` → IC=+0.206 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6472 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` < `0.135` → IC=+0.162 (n=273)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` < 0.135 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `2.2019` → IC=+0.175 (n=232)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 2.2019 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.4508` → IC=+0.157 (n=263)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.4508 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `10375.0696` → IC=+0.137 (n=89)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 10375.0696 (IC base=+0.134)

### GBM_LATE_5M#SOL#5min
- **FILTRO** `libro_liquidez` < `2854.2595` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_liquidez` < 2854.2595
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=63)

- **FILTRO** `sigma_h` < `0.011` → IC=-0.196 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.011
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=21)

- **FILTRO** `sigma_ewma_delta_pct` < `3.941` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 3.941
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=25)

### GBM_LATE_60M
- **FILTRO** `ibs_20min` < `0.6741` → IC=-0.200 (n=48)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6741
  - _Potencial_: sin este filtro IC_bueno=+0.225 (n=147)

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

- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.183 (n=159)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0055 (IC base=+0.074)

- **PATRÓN** `ibs_20min` > `0.6741` → IC=+0.225 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6741 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.1267` → IC=+0.175 (n=75)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.1267 (IC base=+0.074)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.134` → IC=+0.229 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.134 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `0.6655` → IC=+0.127 (n=65)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 0.6655 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.1984` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 1.1984 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` < `0.0665` → IC=+0.237 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0665 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `2.0129` → IC=+0.256 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0129 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` > `1.4935` → IC=+0.300 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4935 (IC base=+0.074)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.164 (n=132)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.02 (IC base=+0.074)

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

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.171 (n=83)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0059 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.144 (n=88)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 7.0 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.126 (n=97)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 17.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.360 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.469` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.469 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` < `0.2466` → IC=+0.226 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2466 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.949` → IC=+0.308 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.949 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `0.6214` → IC=+0.233 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6214 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `1.0949` → IC=+0.283 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0949 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2498.7472` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2498.7472 (IC base=+0.122)

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

- **PATRÓN** `sigma_h` > `0.0137` → IC=+0.182 (n=20)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0137 (IC base=-0.006)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.177 (n=29)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=-0.006)

### GBM_LATE_60M_FADE
- **FILTRO** `drift_60min` |x|> `0.1243` → IC=-0.382 (n=32)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1243
  - _Potencial_: sin este filtro IC_bueno=-0.238 (n=63)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.462 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.233 (n=73)

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

- **FILTRO** `libro_liquidez` < `4361.6218` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `libro_liquidez` < 4361.6218
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=21)

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

- **FILTRO** `ibs_20min` < `0.7391` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7391
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.441 (n=15)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` < `0.5882` → IC=-0.250 (n=46)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5882
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=141)

- **FILTRO** `dist_vwap_pct` > `0.1314` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1314
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=124)

- **PATRÓN** `ibs_20min` > `0.5882` → IC=+0.136 (n=141)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 0.5882 (IC base=+0.040)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.131 (n=82)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 12.0 (IC base=+0.034)

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

- **PATRÓN** `sigma_h` > `0.0035` → IC=+0.167 (n=28)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0035 (IC base=+0.098)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.219 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.098)

- **PATRÓN** `ibs_20min` < `0.3394` → IC=+0.167 (n=61)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.3394 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.519` → IC=+0.159 (n=39)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.519 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` < `1.0741` → IC=+0.136 (n=53)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.0741 (IC base=+0.098)

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
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.125 (n=126)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.099)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.127 (n=65)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` > 0.505 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `2547.7568` → IC=+0.173 (n=108)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2547.7568 (IC base=+0.099)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.132 (n=142)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 18.0 (IC base=+0.119)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.128 (n=49)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.495 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2545.8374` → IC=+0.164 (n=117)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2545.8374 (IC base=+0.119)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.125 (n=126)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.099)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.127 (n=65)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` > 0.505 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `2547.7568` → IC=+0.173 (n=108)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2547.7568 (IC base=+0.099)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.132 (n=142)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 18.0 (IC base=+0.119)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.128 (n=49)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.495 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2545.8374` → IC=+0.164 (n=117)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2545.8374 (IC base=+0.119)

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
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=101)

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

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=591)

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
- **FILTRO** `liq_usd_total` < `26870.64` → IC=-0.177 (n=29)

  - _Acción_: SKIP cuando `liq_usd_total` < 26870.64
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=60)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=17)

- **FILTRO** `libro_liquidez` < `15381.0964` → IC=-0.231 (n=24)

  - _Acción_: SKIP cuando `libro_liquidez` < 15381.0964
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `ballena_activa_n` > `630.0` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `ballena_activa_n` > 630.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=8)

- **PATRÓN** `liq_usd_total` > `46708.62` → IC=+0.138 (n=45)

  - _Acción_: Kelly boost +0.69€ cuando `liq_usd_total` > 46708.62 (IC base=+0.017)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.495 (IC base=+0.017)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `0.8749` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.8749
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=48)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=45)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=172)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9593` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9593
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=15)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

- **PATRÓN** `liq_usd_total` > `16143.83` → IC=+0.194 (n=47)

  - _Acción_: Kelly boost +0.97€ cuando `liq_usd_total` > 16143.83 (IC base=+0.068)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.126 (n=145)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 8.0 (IC base=+0.068)

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
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=102)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.128 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=56)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=28)

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
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=26)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2179.6408` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `libro_liquidez` < 2179.6408
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=126)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=487)

### MOMENTUM_IBS_15M#SOL#15min
- **FILTRO** `drift_20min_pct` |x|> `0.178` → IC=-0.131 (n=109)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.178
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=214)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.46` → IC=-0.172 (n=923)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=2815)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.208 (n=951)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=2865)

- **FILTRO** `ibs_20min` > `0.27` → IC=-0.173 (n=952)

  - _Acción_: SKIP cuando `ibs_20min` > 0.27
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=2864)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.221 (n=134)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=408)

- **FILTRO** `ibs_20min` < `0.7353` → IC=-0.164 (n=135)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7353
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=407)

- **FILTRO** `ibs_20min` > `0.7435` → IC=-0.163 (n=164)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7435
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=493)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.192 (n=154)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=474)

- **FILTRO** `ballena_activa_n` > `78.0` → IC=-0.139 (n=156)

  - _Acción_: SKIP cuando `ballena_activa_n` > 78.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=472)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.136 (n=174)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=397)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.185 (n=249)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=322)

- **FILTRO** `ibs_20min` < `0.7248` → IC=-0.194 (n=142)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7248
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=429)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.210 (n=205)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=436)

- **FILTRO** `ibs_20min` > `0.7289` → IC=-0.222 (n=160)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7289
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=481)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.131 (n=174)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=493)

- **FILTRO** `py_entrada` > `0.53` → IC=-0.196 (n=159)

  - _Acción_: SKIP cuando `py_entrada` > 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=509)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.165 (n=165)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=503)

### MOMENTUM_IBS_15M_BALLENA#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.129 (n=184)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=456)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.217 (n=143)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=464)

- **FILTRO** `ibs_20min` > `0.2759` → IC=-0.160 (n=151)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2759
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=456)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.156 (n=149)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=458)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.214 (n=152)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=474)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=611)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.248 (n=204)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=411)

- **FILTRO** `ibs_20min` > `0.2747` → IC=-0.216 (n=153)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2747
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=462)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.143 (n=2723)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=6722)

- **FILTRO** `py_entrada` < `0.36` → IC=-0.280 (n=2301)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=7144)

- **FILTRO** `ibs_7min` < `0.7308` → IC=-0.232 (n=2360)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7308
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=7085)

- **FILTRO** `ballena_activa_n` > `19.0` → IC=-0.172 (n=3194)

  - _Acción_: SKIP cuando `ballena_activa_n` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=6251)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.221 (n=2864)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=8644)

- **FILTRO** `ibs_7min` > `0.7187` → IC=-0.173 (n=2876)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7187
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=8632)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.315 (n=312)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=970)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.187 (n=895)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=387)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.243 (n=309)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=973)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.226 (n=473)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=1510)

- **FILTRO** `drift_7min_pct` |x|> `0.1335` → IC=-0.142 (n=674)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1335
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=1309)

- **FILTRO** `ibs_7min` > `0.7048` → IC=-0.167 (n=674)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7048
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=1309)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.142 (n=392)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=1439)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.252 (n=434)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=1397)

- **FILTRO** `ibs_7min` < `0.792` → IC=-0.184 (n=457)

  - _Acción_: SKIP cuando `ibs_7min` < 0.792
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=1374)

- **FILTRO** `ballena_activa_n` > `161.0` → IC=-0.182 (n=454)

  - _Acción_: SKIP cuando `ballena_activa_n` > 161.0
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=1377)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.215 (n=440)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=1385)

- **FILTRO** `ballena_activa_n` > `97.0` → IC=-0.159 (n=616)

  - _Acción_: SKIP cuando `ballena_activa_n` > 97.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1209)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.202 (n=333)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=1030)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.313 (n=436)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=927)

- **FILTRO** `ibs_7min` < `0.2143` → IC=-0.282 (n=338)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2143
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=1025)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.279 (n=328)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=1035)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.253 (n=435)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=1584)

- **FILTRO** `ibs_7min` > `0.8128` → IC=-0.190 (n=504)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8128
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=1515)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.151 (n=480)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=1108)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.214 (n=765)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=823)

- **FILTRO** `ibs_7min` < `0.7549` → IC=-0.192 (n=397)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7549
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=1191)

- **FILTRO** `ballena_activa_n` > `42.0` → IC=-0.202 (n=394)

  - _Acción_: SKIP cuando `ballena_activa_n` > 42.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=1194)

- **FILTRO** `hora_utc` > `17.0` → IC=-0.127 (n=371)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=1214)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.266 (n=382)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=1203)

- **FILTRO** `ibs_7min` > `0.1833` → IC=-0.163 (n=538)

  - _Acción_: SKIP cuando `ibs_7min` > 0.1833
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=1047)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.174 (n=535)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=1050)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.228 (n=443)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=1378)

- **FILTRO** `ibs_7min` < `0.7714` → IC=-0.196 (n=455)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7714
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=1366)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.185 (n=433)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=1388)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.185 (n=513)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=1616)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.37` → IC=-0.294 (n=372)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1188)

- **FILTRO** `ibs_7min` < `0.75` → IC=-0.226 (n=378)

  - _Acción_: SKIP cuando `ibs_7min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=1182)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.230 (n=383)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=1177)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.268 (n=395)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=1572)

- **FILTRO** `ibs_7min` > `0.8` → IC=-0.167 (n=488)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=1479)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.122 (n=644)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=1323)

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

- **PATRÓN** `delta_ratio` |x|> `0.3987` → IC=+0.139 (n=344)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio` |x|> 0.3987 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.147 (n=137)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 15.0 (IC base=+0.122)

- **PATRÓN** `total_vol_5m` < `456.268` → IC=+0.170 (n=107)

  - _Acción_: Kelly boost +0.85€ cuando `total_vol_5m` < 456.268 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `3204.915` → IC=+0.140 (n=123)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 3204.915 (IC base=+0.122)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `12.0` → IC=+0.255 (n=51)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.125)

- **PATRÓN** `total_vol_5m` < `637.367` → IC=+0.133 (n=77)

  - _Acción_: Kelly boost +0.66€ cuando `total_vol_5m` < 637.367 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.139 (n=70)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 53.0 (IC base=+0.125)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.42` → IC=+0.139 (n=34)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio` |x|> 0.42 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.158 (n=36)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 12.0 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.146 (n=46)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.03 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `2022.4544` → IC=+0.160 (n=51)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2022.4544 (IC base=+0.123)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `hora_utc` < `8.0` → IC=+0.157 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 8.0 (IC base=+0.110)

- **PATRÓN** `total_vol_5m` < `549.0615` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 549.0615 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `8041.6082` → IC=+0.134 (n=39)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 8041.6082 (IC base=+0.110)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4044` → IC=+0.214 (n=40)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4044 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.222 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.139)

- **PATRÓN** `total_vol_5m` < `4950.202` → IC=+0.156 (n=30)

  - _Acción_: Kelly boost +0.78€ cuando `total_vol_5m` < 4950.202 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `3228.9504` → IC=+0.167 (n=40)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3228.9504 (IC base=+0.139)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.395` → IC=+0.127 (n=57)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.64€ cuando `delta_ratio` |x|> 0.395 (IC base=+0.058)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.152 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 4.0 (IC base=+0.058)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=31)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.058)

- **PATRÓN** `libro_liquidez` > `3395.535` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3395.535 (IC base=+0.058)

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
- **FILTRO** `hora_utc` < `5.0` → IC=-0.333 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=38)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=85)

- **PATRÓN** `streak_estiramiento` < `0.4813` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.4813 (IC base=+0.036)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 34.0 (IC base=+0.036)

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

- **FILTRO** `hora_utc` > `4.0` → IC=-0.167 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

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
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=164)

- **PATRÓN** `streak_estiramiento` < `0.2837` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `streak_estiramiento` < 0.2837 (IC base=+0.008)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=330)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=176)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=239)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.162 (n=69)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 5.0 (IC base=+0.062)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=1237)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=702)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=710)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.151 (n=130)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.003 (IC base=+0.115)

- **PATRÓN** `drift_60min` |x|≤ `0.188` → IC=+0.124 (n=389)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.62€ cuando `drift_60min` |x|≤ 0.188 (IC base=+0.115)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0679` → IC=+0.124 (n=389)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.62€ cuando `delta_ratio_macro` |x|> 0.0679 (IC base=+0.115)

- **PATRÓN** `ibs_15` > `0.5294` → IC=+0.203 (n=389)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5294 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` > `0.3946` → IC=+0.176 (n=103)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.3946 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.763` → IC=+0.243 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.763 (IC base=+0.115)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.122 (n=408)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.01 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `7475.8985` → IC=+0.159 (n=130)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 7475.8985 (IC base=+0.115)

### UPDOWN_GBM#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.076` → IC=-0.137 (n=133)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.076
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=400)

- **FILTRO** `ibs_15` < `0.25` → IC=-0.192 (n=131)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.25
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=402)

- **FILTRO** `sigma_ewma_delta_pct` > `6.565` → IC=-0.209 (n=53)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.565
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=480)

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

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.157 (n=100)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0037 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.1944` → IC=+0.178 (n=113)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.1944 (IC base=+0.151)

- **PATRÓN** `drift_15min` |x|≤ `0.4671` → IC=+0.179 (n=76)

  - _Acción_: Kelly boost +0.90€ cuando `drift_15min` |x|≤ 0.4671 (IC base=+0.151)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2457` → IC=+0.200 (n=38)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2457 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.175 (n=115)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 4.0 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.172 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 6.0 (IC base=+0.151)

- **PATRÓN** `ibs_15` > `0.8791` → IC=+0.253 (n=75)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8791 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.3112` → IC=+0.211 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3112 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `0.5427` → IC=+0.159 (n=124)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.5427 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.945` → IC=+0.196 (n=67)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 6.945 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `11686.9744` → IC=+0.160 (n=51)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 11686.9744 (IC base=+0.151)

### UPDOWN_GBM#BTC#5min
- **FILTRO** `sigma_h` > `0.0048` → IC=-0.222 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0048
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=50)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.196 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=45)

- **FILTRO** `ibs_15` < `0.077` → IC=-0.278 (n=16)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.077
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=50)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `ibs_15` < `0.8328` → IC=-0.147 (n=49)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8328
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=50)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1858` → IC=-0.189 (n=59)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1858
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=31)

- **FILTRO** `dist_vwap_pct` > `0.1635` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1635
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=75)

- **FILTRO** `drift_15min` |x|> `0.5132` → IC=-0.146 (n=125)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.5132
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=377)

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
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0265` → IC=-0.192 (n=24)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0265
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=54)

- **FILTRO** `ibs_15` < `0.2187` → IC=-0.405 (n=19)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.2187
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=59)

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

- **PATRÓN** `ibs_15` < `0.125` → IC=+0.210 (n=112)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.125 (IC base=+0.049)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.005` → IC=+0.368 (n=74)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.309)

- **PATRÓN** `drift_60min` |x|≤ `0.1155` → IC=+0.335 (n=107)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1155 (IC base=+0.309)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1506` → IC=+0.326 (n=107)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1506 (IC base=+0.309)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.340 (n=148)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.309)

- **PATRÓN** `ibs_15` > `0.8123` → IC=+0.355 (n=143)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8123 (IC base=+0.309)

- **PATRÓN** `dist_vwap_pct` > `0.4531` → IC=+0.354 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4531 (IC base=+0.309)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.631` → IC=+0.323 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.631 (IC base=+0.309)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.696` → IC=+0.308 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.696 (IC base=+0.309)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.309 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.309)

- **PATRÓN** `libro_liquidez` > `8557.9163` → IC=+0.339 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8557.9163 (IC base=+0.309)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1986` → IC=+0.305 (n=80)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1986 (IC base=+0.287)

- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.288 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0022 (IC base=+0.287)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.375 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.16` → IC=+0.317 (n=80)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.16 (IC base=+0.287)

- **PATRÓN** `drift_15min` |x|≤ `0.4136` → IC=+0.309 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4136 (IC base=+0.287)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1021` → IC=+0.283 (n=81)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1021 (IC base=+0.287)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1236` → IC=+0.395 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1236 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.318 (n=97)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.287)

- **PATRÓN** `ibs_15` > `0.8374` → IC=+0.331 (n=81)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8374 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` > `0.4531` → IC=+0.385 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4531 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.39` → IC=+0.290 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.39 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `8910.53` → IC=+0.337 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8910.53 (IC base=+0.287)

- **PATRÓN** `ballena_activa_n` < `582.0` → IC=+0.397 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 582.0 (IC base=+0.287)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.348 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.332)

- **PATRÓN** `sigma_h` > `0.006` → IC=+0.353 (n=32)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.332)

- **PATRÓN** `drift_60min` |x|≤ `0.1189` → IC=+0.378 (n=47)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1189 (IC base=+0.332)

- **PATRÓN** `delta_ratio_macro` |x|> `0.13` → IC=+0.378 (n=47)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.13 (IC base=+0.332)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2773` → IC=+0.350 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2773 (IC base=+0.332)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.336 (n=65)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.332)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.328 (n=62)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.332)

- **PATRÓN** `ibs_15` > `0.8044` → IC=+0.408 (n=63)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8044 (IC base=+0.332)

- **PATRÓN** `dist_vwap_pct` < `0.3445` → IC=+0.344 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3445 (IC base=+0.332)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.664` → IC=+0.368 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.664 (IC base=+0.332)

- **PATRÓN** `libro_liquidez` > `3261.6008` → IC=+0.337 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3261.6008 (IC base=+0.332)

- **PATRÓN** `ballena_activa_n` < `184.0` → IC=+0.348 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 184.0 (IC base=+0.332)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0098` → IC=-0.182 (n=262)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0098
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=789)

- **FILTRO** `ibs_15` < `0.6952` → IC=-0.149 (n=203)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6952
  - _Potencial_: sin este filtro IC_bueno=+0.252 (n=204)

- **FILTRO** `sigma_ewma_delta_pct` > `17.671` → IC=-0.172 (n=361)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.671
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=2715)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.357` → IC=+0.141 (n=143)

  - _Acción_: Kelly boost +0.71€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.357 (IC base=-0.067)

- **PATRÓN** `ibs_15` > `0.6952` → IC=+0.252 (n=204)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6952 (IC base=-0.067)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0648` → IC=+0.259 (n=197)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0648 (IC base=-0.074)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2976` → IC=+0.291 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2976 (IC base=-0.074)

- **PATRÓN** `ibs_15` < `0.3542` → IC=+0.329 (n=197)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3542 (IC base=-0.074)

- **PATRÓN** `dist_vwap_pct` < `0.1503` → IC=+0.272 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1503 (IC base=-0.074)

- **PATRÓN** `ballena_activa_n` < `67.0` → IC=+0.280 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 67.0 (IC base=-0.074)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0075` → IC=-0.244 (n=166)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0075
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=499)

- **FILTRO** `sigma_h` < `0.0036` → IC=-0.220 (n=219)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0036
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=446)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.247 (n=160)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=505)

- **FILTRO** `sigma_ewma_delta_pct` > `19.957` → IC=-0.264 (n=125)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.957
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=540)

- **PATRÓN** `ibs_15` > `0.7496` → IC=+0.292 (n=22)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7496 (IC base=+0.014)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.4646` → IC=-0.351 (n=45)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.4646
  - _Potencial_: sin este filtro IC_bueno=+0.179 (n=135)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=163)

- **PATRÓN** `drift_60min` |x|≤ `0.0637` → IC=+0.188 (n=46)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.0637 (IC base=+0.044)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3719` → IC=+0.216 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3719 (IC base=+0.044)

- **PATRÓN** `ibs_15` > `0.4646` → IC=+0.179 (n=135)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.89€ cuando `ibs_15` > 0.4646 (IC base=+0.044)

- **PATRÓN** `libro_liquidez` > `10004.8873` → IC=+0.172 (n=62)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 10004.8873 (IC base=+0.044)

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1043` → IC=+0.269 (n=76)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1043 (IC base=+0.243)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.257 (n=113)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.243)

- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.266 (n=75)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.2315` → IC=+0.244 (n=76)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2315 (IC base=+0.243)

- **PATRÓN** `drift_15min` |x|≤ `0.4277` → IC=+0.275 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4277 (IC base=+0.243)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1555` → IC=+0.266 (n=75)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1555 (IC base=+0.243)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3069` → IC=+0.253 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3069 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.256 (n=84)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.243)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.318 (n=42)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.243)

- **PATRÓN** `ibs_15` < `0.3707` → IC=+0.326 (n=113)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3707 (IC base=+0.243)

- **PATRÓN** `dist_vwap_pct` < `0.1242` → IC=+0.263 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1242 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.486` → IC=+0.274 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.486 (IC base=+0.243)

- **PATRÓN** `libro_liquidez` > `13721.2442` → IC=+0.300 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13721.2442 (IC base=+0.243)

- **PATRÓN** `ballena_activa_n` < `206.0` → IC=+0.253 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 206.0 (IC base=+0.243)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1589` → IC=-0.178 (n=85)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1589
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=167)

- **FILTRO** `drift_15min` |x|> `0.7956` → IC=-0.234 (n=62)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.7956
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=190)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.114 (n=231)

- **PATRÓN** `ibs_15` > `0.8125` → IC=+0.206 (n=15)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8125 (IC base=-0.118)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1866` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1866 (IC base=-0.056)

- **PATRÓN** `ibs_15` < `0.2796` → IC=+0.243 (n=33)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2796 (IC base=-0.056)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 39.0 (IC base=-0.056)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `drift_15min` |x|> `1.159` → IC=-0.268 (n=67)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.159
  - _Potencial_: sin este filtro IC_bueno=-0.118 (n=202)

- **FILTRO** `sigma_ewma_delta_pct` > `14.546` → IC=-0.210 (n=36)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 14.546
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=233)

- **FILTRO** `libro_liquidez` < `2507.6219` → IC=-0.225 (n=67)

  - _Acción_: SKIP cuando `libro_liquidez` < 2507.6219
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=202)

- **PATRÓN** `ibs_15` < `0.0937` → IC=+0.342 (n=17)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.0937 (IC base=-0.066)

- **PATRÓN** `ibs_15` > `0.122` → IC=+0.352 (n=25)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.122 (IC base=-0.066)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.342 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=-0.066)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.275 (n=251)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.274)

- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.284 (n=114)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0054 (IC base=+0.274)

- **PATRÓN** `drift_60min` |x|≤ `0.0798` → IC=+0.314 (n=111)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0798 (IC base=+0.274)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0567` → IC=+0.290 (n=251)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0567 (IC base=+0.274)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.12` → IC=+0.343 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.12 (IC base=+0.274)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.303 (n=262)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.274)

- **PATRÓN** `ibs_15` > `0.9673` → IC=+0.345 (n=114)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9673 (IC base=+0.274)

- **PATRÓN** `dist_vwap_pct` > `0.3041` → IC=+0.345 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3041 (IC base=+0.274)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.915` → IC=+0.282 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.915 (IC base=+0.274)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.274 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.274)

- **PATRÓN** `libro_liquidez` > `13081.1746` → IC=+0.302 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13081.1746 (IC base=+0.274)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0024` → IC=+0.260 (n=48)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0024 (IC base=+0.258)

- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.296 (n=47)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0057 (IC base=+0.258)

- **PATRÓN** `drift_60min` |x|≤ `0.1625` → IC=+0.287 (n=125)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1625 (IC base=+0.258)

- **PATRÓN** `drift_15min` |x|≤ `0.6649` → IC=+0.264 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.6649 (IC base=+0.258)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1438` → IC=+0.292 (n=94)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1438 (IC base=+0.258)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1224` → IC=+0.321 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1224 (IC base=+0.258)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.287 (n=148)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.258)

- **PATRÓN** `ibs_15` > `0.968` → IC=+0.303 (n=64)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.968 (IC base=+0.258)

- **PATRÓN** `dist_vwap_pct` > `0.3306` → IC=+0.352 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3306 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.789` → IC=+0.265 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.789 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.866` → IC=+0.271 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.866 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `14354.3614` → IC=+0.276 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14354.3614 (IC base=+0.258)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.298 (n=97)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.0655` → IC=+0.343 (n=49)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0655 (IC base=+0.290)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0676` → IC=+0.320 (n=98)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0676 (IC base=+0.290)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3059` → IC=+0.346 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3059 (IC base=+0.290)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.319 (n=114)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.290)

- **PATRÓN** `ibs_15` > `0.963` → IC=+0.365 (n=50)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.963 (IC base=+0.290)

- **PATRÓN** `dist_vwap_pct` > `0.6145` → IC=+0.389 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6145 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.98` → IC=+0.291 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.98 (IC base=+0.290)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.300 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.290)

- **PATRÓN** `libro_liquidez` > `9459.3828` → IC=+0.346 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9459.3828 (IC base=+0.290)

- **PATRÓN** `ballena_activa_n` < `245.0` → IC=+0.300 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 245.0 (IC base=+0.290)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1143` → IC=-0.274 (n=29)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1143
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=90)

- **FILTRO** `drift_15min` |x|> `0.8193` → IC=-0.177 (n=29)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8193
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=90)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1212` → IC=-0.170 (n=98)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1212
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=298)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.154 (n=53)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=27)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0838` → IC=-0.136 (n=20)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0838
  - _Potencial_: sin este filtro IC_bueno=+0.128 (n=41)

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
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5294 sube el IC de +0.115 a +0.203 en UPDOWN_GBM#15min (n=389). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.8791 sube el IC de +0.151 a +0.253 en UPDOWN_GBM#BTC#15min (n=75). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.617 sube el IC de +0.079 a +0.231 en UPDOWN_GBM#ETH#15min (n=76). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.056 a +0.265 en UPDOWN_GBM#SOL#15min (n=32). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.4444 sube el IC de +0.099 a +0.167 en UPDOWN_GBM#XRP#15min (n=103). Ya aplicado como kelly_boost=+0.83€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.125 sube el IC de +0.049 a +0.210 en UPDOWN_GBM#XRP#15min (n=112). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6952 sube el IC de -0.067 a +0.252 en UPDOWN_GBM_15M_TARDIO (n=204). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3542 sube el IC de -0.074 a +0.329 en UPDOWN_GBM_15M_TARDIO (n=197). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7496 sube el IC de +0.014 a +0.292 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=22). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.4646 sube el IC de +0.044 a +0.179 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=135). Ya aplicado como kelly_boost=+0.89€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3707 sube el IC de +0.243 a +0.326 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=113). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8125 sube el IC de -0.118 a +0.206 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=15). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.2796 sube el IC de -0.056 a +0.243 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=33). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.0937 sube el IC de -0.066 a +0.342 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS > 0.122 sube el IC de -0.066 a +0.352 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=25). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.9673 sube el IC de +0.274 a +0.345 en UPDOWN_GBM_IBS_ALTO (n=114). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.968 sube el IC de +0.258 a +0.303 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=64). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.963 sube el IC de +0.290 a +0.365 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=50). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.8123 sube el IC de +0.309 a +0.355 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=143). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8374 sube el IC de +0.287 a +0.331 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=81). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.8044 sube el IC de +0.332 a +0.408 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=63). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#SOL#sniper` — IC=+0.472 n=34. Faltan ~6 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#SOL` — IC=+0.472 n=34. Faltan ~6 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min` — IC=+0.353 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL` — IC=+0.353 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min` — IC=+0.167 n=31. Faltan ~9 resoluciones para umbral n≥40. ETA: ~6h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 634 | +0.090 | +45.29€ | 1 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 634 | +0.090 | +45.29€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 385 | +0.115 | +36.51€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 385 | +0.115 | +36.51€ | 1 | 11 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 220 | +0.032 | -2.15€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 220 | +0.032 | -2.15€ | 7 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 29 | +0.177 | +10.93€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 29 | +0.177 | +10.93€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 10677 | -0.095 | -1750.86€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 757 | -0.061 | -135.52€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 9920 | -0.098 | -1615.33€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 1338 | -0.028 | -252.43€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 1338 | -0.028 | -252.43€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 757 | -0.061 | -135.52€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 757 | -0.061 | -135.52€ | 3 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 1374 | -0.152 | -430.31€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 1374 | -0.152 | -430.31€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 2874 | -0.066 | -285.95€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 2874 | -0.066 | -285.95€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 2477 | -0.091 | -194.57€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 2477 | -0.091 | -194.57€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 1857 | -0.167 | -452.08€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 1857 | -0.167 | -452.08€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 585 | -0.055 | +283.96€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 167 | -0.009 | +33.02€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 418 | -0.074 | +250.94€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 585 | -0.055 | +283.96€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 167 | -0.009 | +33.02€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 418 | -0.074 | +250.94€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 8 | -0.040 | -2.18€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 8 | -0.040 | -2.18€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 8 | -0.040 | -2.18€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 8 | -0.040 | -2.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 34942 | +0.114 | -2228.00€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 6322 | +0.186 | -222.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 111 | -0.093 | -48.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 25221 | +0.096 | -1904.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 3288 | +0.119 | -53.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 4231 | +0.066 | -691.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 21 | -0.065 | +2.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#240min | 5 | -0.089 | -6.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 4205 | +0.068 | -687.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 7166 | +0.133 | -162.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 1792 | +0.198 | -91.63€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 4197 | +0.109 | -101.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 1135 | +0.128 | +53.11€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 4241 | +0.082 | -513.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 22 | +0.083 | +3.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 4218 | +0.082 | -515.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 7689 | +0.126 | -130.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 2297 | +0.167 | -19.39€ | 0 | 8 |
| 🚫 FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 4199 | +0.112 | -74.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 1181 | +0.100 | -27.67€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 7387 | +0.133 | -454.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 2173 | +0.201 | -116.17€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 50 | +0.019 | -7.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 4192 | +0.099 | -251.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 972 | +0.131 | -78.82€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#XRP | 4228 | +0.107 | -275.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 17 | -0.022 | -0.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 4210 | +0.108 | -272.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 6247 | +0.173 | -490.08€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 6247 | +0.173 | -490.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 1577 | +0.166 | -169.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 1577 | +0.166 | -169.88€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 123 | -0.116 | +1.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 123 | -0.116 | +1.57€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 1553 | +0.164 | -173.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 1553 | +0.164 | -173.16€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 1403 | +0.230 | -41.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 1403 | +0.230 | -41.17€ | 0 | 2 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 1512 | +0.182 | -121.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 1512 | +0.182 | -121.19€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 315 | +0.446 | +3.83€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 315 | +0.446 | +3.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 120 | +0.443 | +1.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 120 | +0.443 | +1.54€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 117 | +0.433 | -0.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 117 | +0.433 | -0.50€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 75 | +0.448 | +2.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 75 | +0.448 | +2.65€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 17959 | +0.190 | -1593.33€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 17959 | +0.190 | -1593.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 3268 | +0.128 | -591.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 3268 | +0.128 | -591.74€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 2803 | +0.234 | -62.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 2803 | +0.234 | -62.60€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 3076 | +0.166 | -382.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 3076 | +0.166 | -382.13€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 2858 | +0.225 | -103.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 2858 | +0.225 | -103.44€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 2931 | +0.213 | -156.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 2931 | +0.213 | -156.84€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 3023 | +0.186 | -296.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 3023 | +0.186 | -296.58€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 6550 | +0.133 | +245.96€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 6550 | +0.133 | +245.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 3263 | +0.140 | +159.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 3263 | +0.140 | +159.18€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 3287 | +0.127 | +86.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 3287 | +0.127 | +86.77€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 805 | +0.297 | -0.24€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 805 | +0.297 | -0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 345 | +0.281 | -8.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 345 | +0.281 | -8.10€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 376 | +0.299 | +6.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 376 | +0.299 | +6.83€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 84 | +0.337 | +1.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 84 | +0.337 | +1.03€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 343 | +0.413 | -15.56€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 343 | +0.413 | -15.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 153 | +0.410 | -7.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 153 | +0.410 | -7.87€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 158 | +0.419 | -6.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 158 | +0.419 | -6.53€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 32 | +0.353 | -1.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 32 | +0.353 | -1.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 271 | +0.086 | -6.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 80 | +0.110 | +0.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 191 | +0.075 | -7.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 10 | +0.083 | +2.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 10 | +0.083 | +2.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 222 | +0.089 | -3.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 31 | +0.167 | +3.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 191 | +0.075 | -7.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 39 | +0.037 | -5.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 39 | +0.037 | -5.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 7725 | +0.096 | -258.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 757 | +0.070 | -19.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 6968 | +0.099 | -239.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 5102 | +0.096 | -110.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 757 | +0.070 | -19.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 4345 | +0.101 | -90.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 339 | +0.133 | +15.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 339 | +0.133 | +15.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 2284 | +0.089 | -164.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 2284 | +0.089 | -164.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 457 | +0.282 | -33.71€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 457 | +0.282 | -33.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 457 | +0.282 | -33.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 457 | +0.282 | -33.71€ | 0 | 3 |
| ✅ GBM_LATE_15M | 8377 | +0.044 | +2709.69€ | 0 | 15 |
| ✅ GBM_LATE_15M#15min | 8377 | +0.044 | +2709.69€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 1164 | +0.176 | +744.85€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 1164 | +0.176 | +744.85€ | 0 | 20 |
| ✅ GBM_LATE_15M#BTC | 1198 | +0.171 | +694.44€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 1198 | +0.171 | +694.44€ | 0 | 29 |
| ✅ GBM_LATE_15M#DOGE | 1168 | +0.196 | +836.60€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 1168 | +0.196 | +836.60€ | 0 | 19 |
| ✅ GBM_LATE_15M#ETH | 1371 | -0.050 | +22.81€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 1371 | -0.050 | +22.81€ | 4 | 11 |
| ✅ GBM_LATE_15M#SOL | 1508 | -0.047 | +149.96€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 1508 | -0.047 | +149.96€ | 5 | 4 |
| ✅ GBM_LATE_15M#XRP | 1968 | -0.067 | +261.03€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 1968 | -0.067 | +261.03€ | 4 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 9255 | +0.047 | +3673.86€ | 0 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 9255 | +0.047 | +3673.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 1461 | -0.017 | +677.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 1461 | -0.017 | +677.16€ | 2 | 4 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 2012 | -0.039 | +161.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 2012 | -0.039 | +161.22€ | 1 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 1032 | +0.245 | +961.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 1032 | +0.245 | +961.84€ | 0 | 23 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 1518 | -0.052 | -15.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 1518 | -0.052 | -15.53€ | 8 | 2 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 1615 | -0.026 | +335.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 1615 | -0.026 | +335.41€ | 7 | 8 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 1617 | +0.250 | +1553.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 1617 | +0.250 | +1553.77€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 6808 | +0.171 | +4739.50€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 6808 | +0.171 | +4739.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 889 | +0.188 | +636.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 889 | +0.188 | +636.16€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 1156 | +0.160 | +762.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 1156 | +0.160 | +762.11€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 879 | +0.208 | +702.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 879 | +0.208 | +702.59€ | 0 | 16 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 1129 | +0.156 | +714.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 1129 | +0.156 | +714.28€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 1289 | +0.128 | +799.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 1289 | +0.128 | +799.46€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 1466 | +0.196 | +1124.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 1466 | +0.196 | +1124.90€ | 0 | 21 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 1321 | +0.080 | +288.70€ | 0 | 8 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 1321 | +0.080 | +288.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 56 | +0.086 | +14.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 56 | +0.086 | +14.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 348 | +0.089 | +100.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 348 | +0.089 | +100.51€ | 3 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 173 | +0.129 | +68.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 173 | +0.129 | +68.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 232 | +0.175 | +76.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 232 | +0.175 | +76.66€ | 2 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 320 | -0.022 | +3.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 320 | -0.022 | +3.43€ | 4 | 3 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 192 | +0.067 | +24.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 192 | +0.067 | +24.38€ | 0 | 6 |
| ✅ GBM_LATE_15M_TARDIO | 7985 | +0.169 | +5344.07€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#15min | 7985 | +0.169 | +5344.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 1117 | +0.198 | +835.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 1117 | +0.198 | +835.21€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 1299 | +0.159 | +818.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 1299 | +0.159 | +818.15€ | 0 | 28 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 1100 | +0.216 | +901.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 1100 | +0.216 | +901.74€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 1239 | +0.141 | +705.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 1239 | +0.141 | +705.60€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 1425 | +0.103 | +712.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 1425 | +0.103 | +712.20€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 1805 | +0.199 | +1371.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 1805 | +0.199 | +1371.18€ | 0 | 22 |
| ✅ GBM_LATE_5M | 2281 | +0.125 | +1011.15€ | 1 | 20 |
| ✅ GBM_LATE_5M#5min | 2281 | +0.125 | +1011.15€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 95 | +0.222 | +72.24€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 95 | +0.222 | +72.24€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 806 | +0.125 | +403.48€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 806 | +0.125 | +403.48€ | 2 | 16 |
| ✅ GBM_LATE_5M#DOGE | 204 | +0.141 | +94.85€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 204 | +0.141 | +94.85€ | 0 | 8 |
| ✅ GBM_LATE_5M#ETH | 748 | +0.131 | +316.88€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 748 | +0.131 | +316.88€ | 0 | 28 |
| ✅ GBM_LATE_5M#SOL | 125 | -0.020 | +0.12€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 125 | -0.020 | +0.12€ | 3 | 0 |
| ✅ GBM_LATE_5M#XRP | 303 | +0.126 | +123.58€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 303 | +0.126 | +123.58€ | 0 | 0 |
| ✅ GBM_LATE_60M | 533 | -0.025 | +98.49€ | 5 | 10 |
| ✅ GBM_LATE_60M#60min | 533 | -0.025 | +98.49€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 184 | +0.011 | +6.74€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 184 | +0.011 | +6.74€ | 2 | 4 |
| ✅ GBM_LATE_60M#ETH | 192 | +0.010 | +65.59€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 192 | +0.010 | +65.59€ | 2 | 10 |
| ✅ GBM_LATE_60M#SOL | 157 | -0.110 | +26.15€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 157 | -0.110 | +26.15€ | 3 | 2 |
| 🚫 GBM_LATE_60M_FADE | 195 | -0.302 | -33.28€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 195 | -0.302 | -33.28€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 77 | -0.260 | -7.87€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 77 | -0.260 | -7.87€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 65 | -0.351 | -19.05€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 65 | -0.351 | -19.05€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 53 | -0.282 | -6.35€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 53 | -0.282 | -6.35€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 346 | +0.037 | +0.21€ | 2 | 2 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 346 | +0.037 | +0.21€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 142 | +0.021 | +4.37€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 142 | +0.021 | +4.37€ | 3 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 87 | +0.073 | +0.32€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 87 | +0.073 | +0.32€ | 0 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 117 | +0.029 | -4.47€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 117 | +0.029 | -4.47€ | 2 | 5 |
| ✅ LATE_WINDOW_5MIN | 25 | +0.278 | +10.54€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 25 | +0.278 | +10.54€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 25 | +0.278 | +10.54€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 25 | +0.278 | +10.54€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 334 | +0.110 | +95.06€ | 0 | 6 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 334 | +0.110 | +95.06€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 334 | +0.110 | +95.06€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 334 | +0.110 | +95.06€ | 0 | 6 |
| ✅ LIQUIDACIONES_15M | 237 | -0.102 | -30.05€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 237 | -0.102 | -30.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 59 | -0.090 | -7.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 59 | -0.090 | -7.07€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 23 | -0.180 | -4.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 23 | -0.180 | -4.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 49 | -0.088 | -6.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 49 | -0.088 | -6.46€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 54 | +0.000 | -0.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 54 | +0.000 | -0.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 47 | -0.173 | -9.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 47 | -0.173 | -9.46€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 786 | -0.017 | -12.16€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 786 | -0.017 | -12.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 50 | +0.019 | -1.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 50 | +0.019 | -1.14€ | 0 | 1 |
| ✅ LIQUIDACIONES_5M#BTC | 121 | -0.037 | -2.78€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 121 | -0.037 | -2.78€ | 4 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 68 | -0.100 | -7.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 68 | -0.100 | -7.86€ | 2 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 218 | +0.023 | +11.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 218 | +0.023 | +11.83€ | 3 | 2 |
| ✅ LIQUIDACIONES_5M#SOL | 273 | -0.002 | -4.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 273 | -0.002 | -4.59€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 56 | -0.121 | -7.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 56 | -0.121 | -7.62€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M | 466 | -0.006 | -1.87€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 466 | -0.006 | -1.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 148 | -0.033 | -9.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 148 | -0.033 | -9.82€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 144 | +0.000 | +1.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 144 | +0.000 | +1.50€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 174 | +0.011 | +6.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 174 | +0.011 | +6.45€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 4842 | -0.002 | -75.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 4842 | -0.002 | -75.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 521 | -0.007 | +0.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 521 | -0.007 | +0.91€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 599 | +0.004 | -9.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 599 | +0.004 | -9.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 884 | +0.000 | -21.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 884 | +0.000 | -21.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 1035 | +0.010 | +15.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 1035 | +0.010 | +15.28€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 891 | -0.007 | -30.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 891 | -0.007 | -30.27€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 912 | -0.014 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 912 | -0.014 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 7554 | -0.035 | +186.74€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 7554 | -0.035 | +186.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 1199 | -0.030 | +133.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 1199 | -0.030 | +133.70€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 1320 | -0.031 | -13.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 1320 | -0.031 | -13.07€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 1212 | -0.048 | +76.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 1212 | -0.048 | +76.86€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 1335 | -0.032 | -35.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 1335 | -0.032 | -35.32€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 1247 | -0.039 | +35.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 1247 | -0.039 | +35.38€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 1241 | -0.029 | -10.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 1241 | -0.029 | -10.80€ | 4 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 20953 | -0.075 | +381.20€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 20953 | -0.075 | +381.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 3265 | -0.087 | +411.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 3265 | -0.087 | +411.95€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 3656 | -0.065 | -27.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 3656 | -0.065 | -27.39€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 3382 | -0.084 | +27.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 3382 | -0.084 | +27.21€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 3173 | -0.098 | -169.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 3173 | -0.098 | -169.94€ | 8 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 3950 | -0.050 | +5.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 3950 | -0.050 | +5.83€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 3527 | -0.074 | +133.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 3527 | -0.074 | +133.55€ | 6 | 0 |
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
| ✅ ORDER_FLOW_5M | 496 | +0.098 | +128.96€ | 1 | 4 |
| ✅ ORDER_FLOW_5M#5min | 360 | +0.113 | +116.37€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 102 | +0.125 | +44.52€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 102 | +0.125 | +44.52€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#DOGE | 67 | +0.123 | +21.56€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 67 | +0.123 | +21.56€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#ETH | 57 | +0.110 | +17.79€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 57 | +0.110 | +17.79€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#SOL | 59 | +0.139 | +24.38€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 59 | +0.139 | +24.38€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 75 | +0.058 | +8.12€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 75 | +0.058 | +8.12€ | 0 | 4 |
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
| ✅ STREAK_FADE_15M | 162 | +0.012 | -5.66€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 162 | +0.012 | -5.66€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 65 | -0.007 | -6.45€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 65 | -0.007 | -6.45€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 10 | +0.000 | -0.13€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 10 | +0.000 | -0.13€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 16 | +0.089 | +1.68€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 16 | +0.089 | +1.68€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 71 | +0.007 | -0.76€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 71 | +0.007 | -0.76€ | 1 | 0 |
| ✅ STREAK_FADE_5M | 1186 | -0.020 | -52.92€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 1186 | -0.020 | -52.92€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 403 | -0.018 | -13.68€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 403 | -0.018 | -13.68€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 426 | -0.007 | -11.83€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 426 | -0.007 | -11.83€ | 3 | 0 |
| ✅ STREAK_FADE_5M#SOL | 132 | -0.037 | -12.47€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 132 | -0.037 | -12.47€ | 2 | 0 |
| ✅ STREAK_FADE_5M#XRP | 225 | -0.037 | -14.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 225 | -0.037 | -14.94€ | 4 | 0 |
| ✅ STREAK_FADE_60M | 33 | -0.014 | -1.06€ | 0 | 0 |
| ✅ STREAK_FADE_60M#60min | 33 | -0.014 | -1.06€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 20 | -0.091 | -2.33€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 20 | -0.091 | -2.33€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 13 | +0.065 | +1.26€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 13 | +0.065 | +1.26€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 2465 | +0.027 | +44.79€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 2465 | +0.027 | +44.79€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 819 | +0.032 | +15.84€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 819 | +0.032 | +15.84€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 462 | +0.022 | +6.11€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 462 | +0.022 | +6.11€ | 1 | 1 |
| ✅ STREAK_MOM_5M#SOL | 727 | +0.025 | +7.36€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 727 | +0.025 | +7.36€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 457 | +0.027 | +15.48€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 457 | +0.027 | +15.48€ | 2 | 1 |
| ✅ STRUCT_NO_15M | 3263 | +0.011 | -22.71€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 3263 | +0.011 | -22.71€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 1256 | +0.013 | -6.37€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 1256 | +0.013 | -6.37€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 1273 | +0.016 | -1.98€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 1273 | +0.016 | -1.98€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 734 | -0.004 | -14.36€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 734 | -0.004 | -14.36€ | 2 | 0 |
| ✅ UPDOWN_GBM | 6610 | +0.004 | +149.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 2397 | +0.044 | +233.92€ | 0 | 8 |
| ✅ UPDOWN_GBM#240min | 271 | +0.017 | +2.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 3493 | -0.019 | -79.31€ | 3 | 0 |
| ✅ UPDOWN_GBM#60min | 402 | -0.010 | -7.16€ | 3 | 0 |
| ✅ UPDOWN_GBM#BNB | 196 | +0.091 | +38.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 179 | +0.119 | +42.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 8 | -0.040 | -1.01€ | 0 | 0 |
| 🚫 UPDOWN_GBM#BNB#5min | 9 | -0.102 | -2.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 1492 | +0.013 | +61.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 242 | +0.070 | +36.95€ | 5 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 79 | +0.056 | +4.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 1024 | +0.006 | +24.12€ | 3 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 129 | -0.034 | -6.64€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 821 | -0.003 | +0.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 122 | +0.105 | +29.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 9 | +0.021 | +0.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 690 | -0.023 | -28.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 1572 | -0.002 | -4.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 708 | +0.021 | +17.89€ | 1 | 5 |
| ✅ UPDOWN_GBM#ETH#240min | 79 | +0.068 | +5.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 592 | -0.037 | -28.59€ | 3 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 178 | +0.011 | +0.72€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 1612 | -0.007 | -18.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 565 | +0.006 | +0.26€ | 1 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 64 | +0.000 | -2.32€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 876 | -0.013 | -15.16€ | 2 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 95 | -0.015 | -1.24€ | 2 | 3 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 915 | +0.011 | +73.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 581 | +0.061 | +107.19€ | 0 | 8 |
| ✅ UPDOWN_GBM#XRP#240min | 32 | -0.147 | -5.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 302 | -0.066 | -28.08€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 213 | +0.309 | +38.63€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 213 | +0.309 | +38.63€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 120 | +0.287 | +11.92€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 120 | +0.287 | +11.92€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 93 | +0.332 | +26.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 93 | +0.332 | +26.71€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 4127 | -0.072 | +871.26€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 4127 | -0.072 | +871.26€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 303 | -0.051 | +341.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 303 | -0.051 | +341.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 844 | -0.162 | -89.95€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 844 | -0.162 | -89.95€ | 4 | 1 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 77 | +0.070 | +14.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 77 | +0.070 | +14.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 330 | +0.136 | +154.32€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 330 | +0.136 | +154.32€ | 2 | 18 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 1323 | -0.068 | +234.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 1323 | -0.068 | +234.59€ | 3 | 4 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 1250 | -0.086 | +216.50€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 1250 | -0.086 | +216.50€ | 3 | 3 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 33 | -0.014 | -2.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 33 | -0.014 | -2.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 33 | -0.014 | -2.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 33 | -0.014 | -2.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 334 | +0.274 | +244.58€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 334 | +0.274 | +244.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 188 | +0.258 | +128.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 188 | +0.258 | +128.12€ | 0 | 12 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 146 | +0.290 | +116.47€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 146 | +0.290 | +116.47€ | 0 | 11 |
| ✅ UPDOWN_OU_5M | 515 | -0.088 | -53.54€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#5min | 515 | -0.088 | -53.54€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 284 | -0.063 | -28.78€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 284 | -0.063 | -28.78€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 95 | -0.005 | +0.88€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 95 | -0.005 | +0.88€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 30 | -0.188 | -6.21€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 30 | -0.188 | -6.21€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 38 | -0.175 | -6.34€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 38 | -0.175 | -6.34€ | 0 | 0 |
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
  - _Estado_: Spread bajo (0.081) — sin ventaja clara. oversold(IBS<0.3): IC=+0.017 n=2366 | neutral: IC=+0.002 n=2528 | overbought(IBS>0.7): IC=+0.083 n=2578
  - _Datos_: n=7797 IC=+0.035 PNL=+691.65€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: (cache 493s) 28 celda(s) GATE OK de 2158 trackeadas

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.006 < 0.08 — monitorear
  - _Datos_: n=565 IC=+0.006 PNL=+0.26€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=359/15 IC=+0.265 PNL=+92.97€ | BTC: n=342/15 IC=+0.209 PNL=+2.62€ | SOL: n=433/15 IC=+0.371 PNL=+380.41€

**🟡 H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.074 n=107090 | tras_1loss IC=+0.046 n=83508 | tras_2loss IC=+0.009 n=37870/40 | gap=+0.065 (umbral 0.05)

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
  - _Estado_: 6548 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.096 n=45/60 | contraria IC=+0.000 n=24 | gap=+0.096 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=80, boost estimado=+0.007. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 59 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=178/40 IC=+0.011 PNL=+0.72€ | BTC#60min: n=129/40 IC=-0.034 PNL=-6.64€ | SOL#60min: n=95/40 IC=-0.015 PNL=-1.24€

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=-0.013 n=721 | contrario_BTC IC=-0.012 n=537/40 | gap=+0.001 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.135 > 0.08 con n=94 PNL=+25.23€
  - _Datos_: n=94 IC=+0.135 PNL=+25.23€

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
  - _Estado_: n=6363 IC=+0.002 PNL=+99.48€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=6363 IC=+0.002 PNL=+99.48€

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
  - _Estado_: n=329 IC=+0.004 PNL=-0.99€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=329 IC=+0.004 PNL=-0.99€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=73 IC=-0.073 PNL=-6.17€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=73 IC=-0.073 PNL=-6.17€

**🔴 H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.089 < -0.08 con n=105 PNL=-9.28€
  - _Datos_: n=105 IC=-0.089 PNL=-9.28€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.115 > 0.1 con n=518 PNL=+120.82€
  - _Datos_: n=518 IC=+0.115 PNL=+120.82€

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
  - _Estado_: n=242 IC=+0.070 PNL=+36.95€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=242 IC=+0.070 PNL=+36.95€

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
  - _Estado_: n=1388 IC=+0.027 PNL=+83.38€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1388 IC=+0.027 PNL=+83.38€

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
  - _Estado_: n=2231 IC=-0.021 PNL=-54.62€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2231 IC=-0.021 PNL=-54.62€

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
  - _Estado_: n=1753 IC=+0.024 PNL=+105.13€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1753 IC=+0.024 PNL=+105.13€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=459 IC=+0.034 PNL=+0.49€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=459 IC=+0.034 PNL=+0.49€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.103 > 0.08 con n=124 PNL=+29.21€
  - _Datos_: n=124 IC=+0.103 PNL=+29.21€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.133 > 0.08 con n=126 PNL=+2.94€
  - _Datos_: n=126 IC=+0.133 PNL=+2.94€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.120 > 0.08 con n=119 PNL=+38.10€
  - _Datos_: n=119 IC=+0.120 PNL=+38.10€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=17051 IC=+0.101 PNL=+5042.79€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=17051 IC=+0.101 PNL=+5042.79€

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
  - _Estado_: n=872 IC=+0.026 PNL=+48.41€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=872 IC=+0.026 PNL=+48.41€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.124 > 0.02 con n=264 PNL=+80.54€
  - _Datos_: n=264 IC=+0.124 PNL=+80.54€

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
  - _Estado_: n=1584 IC=+0.019 PNL=+76.64€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=1584 IC=+0.019 PNL=+76.64€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.165 > 0.1 con n=789 PNL=+290.21€
  - _Datos_: n=789 IC=+0.165 PNL=+290.21€

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
  - _Estado_: n=446 IC=+0.049 PNL=+64.13€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=446 IC=+0.049 PNL=+64.13€

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
  - _Estado_: n=68 IC=+0.043 PNL=-1.19€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=68 IC=+0.043 PNL=-1.19€

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
  - _Estado_: n=4976 IC=-0.146 PNL=+156.63€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4976 IC=-0.146 PNL=+156.63€

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
  - _Estado_: n=638 IC=+0.144 PNL=+280.91€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=638 IC=+0.144 PNL=+280.91€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.115 > 0.08 con n=518 PNL=+120.82€
  - _Datos_: n=518 IC=+0.115 PNL=+120.82€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.151 > 0.08 con n=150 PNL=+43.28€
  - _Datos_: n=150 IC=+0.151 PNL=+43.28€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.241 < -0.1 con n=550 PNL=-76.18€
  - _Datos_: n=550 IC=-0.241 PNL=-76.18€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=1314 IC=+0.136 PNL=+679.66€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=1314 IC=+0.136 PNL=+679.66€

**⏳ H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: 40
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: 30/40 ops en el filtro definido (IC actual=+0.062 PNL=+3.81€)
  - _Datos_: n=30 IC=+0.062 PNL=+3.81€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=704 IC=-0.031 PNL=+33.39€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=704 IC=-0.031 PNL=+33.39€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.179 > 0.08 con n=612 PNL=+363.79€
  - _Datos_: n=612 IC=+0.179 PNL=+363.79€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=1038 IC=-0.058 PNL=+153.79€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1038 IC=-0.058 PNL=+153.79€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.115 > 0.08 con n=263 PNL=-35.06€
  - _Datos_: n=263 IC=+0.115 PNL=-35.06€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.234 > 0.08 con n=1520 PNL=-152.32€
  - _Datos_: n=1520 IC=+0.234 PNL=-152.32€

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 10/40 ops en el filtro definido (IC actual=+0.000 PNL=+2.51€)
  - _Datos_: n=10 IC=+0.000 PNL=+2.51€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.119 n=174) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=174 IC=+0.119 PNL=+50.37€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.353 > 0.08 con n=73 PNL=+50.59€
  - _Datos_: n=73 IC=+0.353 PNL=+50.59€

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
  - _Estado_: n=3268 IC=+0.128 PNL=-591.74€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=3268 IC=+0.128 PNL=-591.74€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.182 > 0.1 con n=42 PNL=+22.66€
  - _Datos_: n=42 IC=+0.182 PNL=+22.66€
