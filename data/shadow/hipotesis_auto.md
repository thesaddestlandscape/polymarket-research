# Hipótesis automáticas — 2026-08-27 02:54 UTC
_Generado por shadow_postmortem.py sobre 169424 resoluciones (PNL=+12275.88€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.705` → IC=-0.167 (n=88)

  - _Acción_: SKIP cuando `py_entrada` < 0.705
  - _Potencial_: sin este filtro IC_bueno=+0.267 (n=230)

- **PATRÓN** `py_entrada` > `0.725` → IC=+0.280 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.147)

- **PATRÓN** `n_ballena_banda` > `20.0` → IC=+0.162 (n=220)

  - _Acción_: Kelly boost +0.81€ cuando `n_ballena_banda` > 20.0 (IC base=+0.147)

- **PATRÓN** `n_total_lado` > `58.0` → IC=+0.235 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 58.0 (IC base=+0.147)

- **PATRÓN** `banda_hit_calibrado` > `0.8213` → IC=+0.259 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8213 (IC base=+0.147)

- **PATRÓN** `banda_z` > `9.751` → IC=+0.230 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.751 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.181 (n=164)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 11.0 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.171 (n=250)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `3103.76` → IC=+0.230 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3103.76 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `288.0` → IC=+0.288 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 288.0 (IC base=+0.147)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.136 (n=215)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.5 (IC base=+0.012)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.725` → IC=+0.280 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.184)

- **PATRÓN** `n_ballena_banda` > `20.0` → IC=+0.196 (n=156)

  - _Acción_: Kelly boost +0.98€ cuando `n_ballena_banda` > 20.0 (IC base=+0.184)

- **PATRÓN** `n_total_lado` > `52.0` → IC=+0.237 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 52.0 (IC base=+0.184)

- **PATRÓN** `banda_hit_calibrado` > `0.8208` → IC=+0.270 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8208 (IC base=+0.184)

- **PATRÓN** `banda_z` > `11.818` → IC=+0.274 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.818 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.214 (n=138)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.184 (n=112)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 12.0 (IC base=+0.184)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.192 (n=180)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.01 (IC base=+0.184)

- **PATRÓN** `libro_liquidez` > `3838.6557` → IC=+0.250 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3838.6557 (IC base=+0.184)

- **PATRÓN** `ballena_activa_n` < `295.0` → IC=+0.300 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 295.0 (IC base=+0.184)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.129 (n=114)

  - _Acción_: Kelly boost +0.65€ cuando `py_entrada` < 0.5 (IC base=+0.003)

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

- **PATRÓN** `py_entrada` > `0.335` → IC=+0.193 (n=86)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.335 (IC base=+0.078)

- **PATRÓN** `banda_hit_calibrado` > `0.6284` → IC=+0.222 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6284 (IC base=+0.078)

- **PATRÓN** `banda_z` > `8.174` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `banda_z` > 8.174 (IC base=+0.078)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.141 (n=90)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.02 (IC base=+0.078)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.495 (IC base=-0.024)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `147.45` → IC=-0.285 (n=2347)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 147.45
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=7042)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `148.64` → IC=-0.202 (n=290)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 148.64
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=872)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `n_ballenas` < `6.0` → IC=-0.173 (n=166)

  - _Acción_: SKIP cuando `n_ballenas` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=515)

- **FILTRO** `restante_s_al_confirmar` < `390.04` → IC=-0.285 (n=170)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 390.04
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=511)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `96.72` → IC=-0.435 (n=289)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 96.72
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=869)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `158.83` → IC=-0.187 (n=637)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 158.83
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=1914)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `154.28` → IC=-0.265 (n=551)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 154.28
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=1654)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `149.51` → IC=-0.363 (n=538)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 149.51
  - _Potencial_: sin este filtro IC_bueno=-0.124 (n=1094)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.7` → IC=+0.187 (n=5304)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.7 (IC base=+0.097)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.170 (n=1568)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.01 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `2382.8902` → IC=+0.173 (n=1513)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2382.8902 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.145 (n=3128)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 18.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.155 (n=4169)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.141)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.259 (n=3271)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.190 (n=2909)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.02 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `1855.8565` → IC=+0.182 (n=2432)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 1855.8565 (IC base=+0.141)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.222 (n=628)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.207)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.394 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.210 (n=774)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `12753.7064` → IC=+0.217 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12753.7064 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.195 (n=566)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 7.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.192 (n=430)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.292 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.185)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.185 (n=807)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.01 (IC base=+0.185)

- **PATRÓN** `libro_liquidez` > `12164.5258` → IC=+0.211 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12164.5258 (IC base=+0.185)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.129 (n=535)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.136 (n=457)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 15.0 (IC base=+0.118)

- **PATRÓN** `py_entrada` > `0.555` → IC=+0.138 (n=534)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` > 0.555 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `4922.6447` → IC=+0.160 (n=204)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 4922.6447 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.197 (n=183)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 7.0 (IC base=+0.135)

- **PATRÓN** `py_entrada` < `0.415` → IC=+0.179 (n=300)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.415 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `4198.5556` → IC=+0.155 (n=282)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 4198.5556 (IC base=+0.135)

### FAVORITO_CONFIRMADO#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.134 (n=1199)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.126 (n=1017)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 15.0 (IC base=+0.123)

- **PATRÓN** `py_entrada` > `0.69` → IC=+0.309 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.292 (n=417)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.284)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.285 (n=464)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.284)

- **PATRÓN** `py_entrada` < `0.195` → IC=+0.418 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.195 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.284 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `2877.1517` → IC=+0.295 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2877.1517 (IC base=+0.284)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.162 (n=279)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 15.0 (IC base=+0.141)

- **PATRÓN** `py_entrada` > `0.655` → IC=+0.252 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.655 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.145 (n=390)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.02 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `1994.5639` → IC=+0.160 (n=316)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 1994.5639 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `4420.281` → IC=+0.157 (n=141)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 4420.281 (IC base=+0.078)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.218 (n=307)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.194 (n=626)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 12.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.84` → IC=+0.445 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.84 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.256 (n=211)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.336 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.223)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.232 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `2047.7732` → IC=+0.253 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2047.7732 (IC base=+0.223)

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

- **PATRÓN** `py_entrada` < `0.355` → IC=+0.203 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.355 (IC base=+0.103)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.146 (n=272)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.02 (IC base=+0.103)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.292 (n=70)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=91)

- **FILTRO** `py_entrada` > `0.845` → IC=-0.379 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.845
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=130)

- **FILTRO** `libro_liquidez` < `7570.2535` → IC=-0.254 (n=120)

  - _Acción_: SKIP cuando `libro_liquidez` < 7570.2535
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=41)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.192 (n=4452)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.190 (n=3784)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.199 (n=2138)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.185)

- **PATRÓN** `libro_liquidez` > `3258.7888` → IC=+0.357 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3258.7888 (IC base=+0.185)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.171 (n=773)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 11.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.178 (n=970)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 15.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` < `0.72` → IC=+0.175 (n=969)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.72 (IC base=+0.167)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=59)

- **FILTRO** `py_entrada` > `0.815` → IC=-0.409 (n=20)

  - _Acción_: SKIP cuando `py_entrada` > 0.815
  - _Potencial_: sin este filtro IC_bueno=-0.219 (n=62)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.417 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.328)

- **PATRÓN** `py_entrada` > `0.835` → IC=+0.372 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.835 (IC base=+0.328)

- **PATRÓN** `libro_liquidez` > `2916.5858` → IC=+0.343 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2916.5858 (IC base=+0.328)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=1138)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.159)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.165 (n=958)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 15.0 (IC base=+0.159)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.168 (n=411)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` < 0.7 (IC base=+0.159)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.169 (n=569)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.73 (IC base=+0.159)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.240 (n=1015)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.229)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.229 (n=862)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.229)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.314 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.229)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.192 (n=1089)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.183 (n=931)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 15.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.196 (n=548)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.7 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.457 (n=208)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.446)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.446 (n=202)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.446)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.456 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.446)

- **PATRÓN** `libro_liquidez` > `3355.2252` → IC=+0.466 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3355.2252 (IC base=+0.446)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.454 (n=84)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.447)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.448 (n=75)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.447)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.454 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.447)

- **PATRÓN** `libro_liquidez` > `12728.4996` → IC=+0.475 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12728.4996 (IC base=+0.447)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `4.0` → IC=+0.444 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.428)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.430 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.428)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.429 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.428)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.427 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.428)

- **PATRÓN** `libro_liquidez` > `3806.2335` → IC=+0.475 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3806.2335 (IC base=+0.428)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.440 (n=48)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.445)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.448 (n=56)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.445)

- **PATRÓN** `py_entrada` > `0.92` → IC=+0.441 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.92 (IC base=+0.445)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.440 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.445)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.207 (n=4018)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.220 (n=8527)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.190)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.130 (n=2205)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 6.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.129 (n=1568)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 12.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.156 (n=1653)

  - _Acción_: Kelly boost +0.78€ cuando `py_entrada` > 0.71 (IC base=+0.125)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.243 (n=1875)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.236)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.273 (n=1380)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.236)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.196 (n=691)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 18.0 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.163 (n=1457)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 12.0 (IC base=+0.163)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.212 (n=709)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.163)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.238 (n=1727)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.230)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.289 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.230)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.239 (n=656)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.216)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.247 (n=1158)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.216)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.198 (n=681)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 18.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.189 (n=1430)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 12.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.210 (n=1463)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.183)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.199 (n=1621)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.134)

- **PATRÓN** `restante_min` < `3.95` → IC=+0.138 (n=1466)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` < 3.95 (IC base=+0.134)

- **PATRÓN** `restante_min` > `4.93` → IC=+0.161 (n=1471)

  - _Acción_: Kelly boost +0.80€ cuando `restante_min` > 4.93 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.151 (n=2131)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 8.0 (IC base=+0.134)

- **PATRÓN** `lag_apertura_s` < `4.46` → IC=+0.158 (n=1457)

  - _Acción_: Kelly boost +0.79€ cuando `lag_apertura_s` < 4.46 (IC base=+0.134)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.204 (n=809)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.140)

- **PATRÓN** `restante_min` < `4.28` → IC=+0.141 (n=960)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` < 4.28 (IC base=+0.140)

- **PATRÓN** `restante_min` > `4.91` → IC=+0.168 (n=750)

  - _Acción_: Kelly boost +0.84€ cuando `restante_min` > 4.91 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.161 (n=1055)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 8.0 (IC base=+0.140)

- **PATRÓN** `lag_apertura_s` < `5.52` → IC=+0.169 (n=723)

  - _Acción_: Kelly boost +0.84€ cuando `lag_apertura_s` < 5.52 (IC base=+0.140)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=812)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.127)

- **PATRÓN** `restante_min` < `4.42` → IC=+0.130 (n=973)

  - _Acción_: Kelly boost +0.65€ cuando `restante_min` < 4.42 (IC base=+0.127)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.160 (n=784)

  - _Acción_: Kelly boost +0.80€ cuando `restante_min` > 4.94 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.129 (n=2286)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 5.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.141 (n=1076)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 8.0 (IC base=+0.127)

- **PATRÓN** `lag_apertura_s` < `3.49` → IC=+0.162 (n=732)

  - _Acción_: Kelly boost +0.81€ cuando `lag_apertura_s` < 3.49 (IC base=+0.127)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.316 (n=410)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.300)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.305 (n=592)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.300)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.374 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.8 (IC base=+0.300)

- **PATRÓN** `libro_liquidez` > `1876.0591` → IC=+0.301 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1876.0591 (IC base=+0.300)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.286 (n=246)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.281)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.283 (n=224)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.281)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.356 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.281)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.283 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `5612.6302` → IC=+0.321 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5612.6302 (IC base=+0.281)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.334 (n=191)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.303)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.312 (n=275)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.303)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.387 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.303)

- **PATRÓN** `libro_liquidez` > `1864.2726` → IC=+0.322 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1864.2726 (IC base=+0.303)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.422 (n=254)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.414)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.423 (n=245)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.414)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.422 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.414)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.427 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.414)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.413 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.414)

- **PATRÓN** `libro_liquidez` > `1852.2015` → IC=+0.426 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1852.2015 (IC base=+0.414)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.420 (n=110)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.412)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.429 (n=110)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.412)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.417 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.412)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.422 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.412)

- **PATRÓN** `libro_liquidez` > `5548.4507` → IC=+0.449 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5548.4507 (IC base=+0.412)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.423 (n=102)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.419)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.440 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.419)

- **PATRÓN** `py_entrada` > `0.91` → IC=+0.424 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.91 (IC base=+0.419)

- **PATRÓN** `libro_liquidez` > `1854.0504` → IC=+0.440 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1854.0504 (IC base=+0.419)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.308 (n=289)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.288)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.439 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.288)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.306 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `1582.3645` → IC=+0.338 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1582.3645 (IC base=+0.288)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.308 (n=289)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.288)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.439 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.288)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.306 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `1582.3645` → IC=+0.338 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1582.3645 (IC base=+0.288)

### GBM_LATE_15M
- **PATRÓN** `ibs_20min` > `0.9494` → IC=+0.208 (n=741)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9494 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` > `0.2046` → IC=+0.232 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2046 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` < `0.7362` → IC=+0.213 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7362 (IC base=+0.064)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.206` → IC=+0.169 (n=904)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 5.206 (IC base=+0.064)

- **PATRÓN** `volumen_regimen` < `0.6324` → IC=+0.225 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6324 (IC base=+0.064)

- **PATRÓN** `volumen_regimen` > `1.0608` → IC=+0.245 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0608 (IC base=+0.064)

- **PATRÓN** `volumen_pendiente_norm` > `0.3083` → IC=+0.151 (n=170)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.3083 (IC base=+0.064)

- **PATRÓN** `volumen_spike_ratio` < `2.4423` → IC=+0.143 (n=1049)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.4423 (IC base=+0.064)

- **PATRÓN** `ibs_20min` < `0.2136` → IC=+0.134 (n=1508)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.2136 (IC base=+0.031)

- **PATRÓN** `dist_vwap_pct` < `0.2976` → IC=+0.147 (n=765)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.2976 (IC base=+0.031)

- **PATRÓN** `volumen_regimen` < `0.6357` → IC=+0.156 (n=245)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6357 (IC base=+0.031)

- **PATRÓN** `volumen_regimen` > `1.06` → IC=+0.147 (n=332)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.06 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.1721` → IC=+0.255 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1721 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` < `1.6226` → IC=+0.199 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6226 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` > `2.924` → IC=+0.236 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.924 (IC base=+0.031)

- **PATRÓN** `ballena_activa_n` < `97.0` → IC=+0.231 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 97.0 (IC base=+0.031)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.186 (n=167)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0075 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.164 (n=236)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 8.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.290 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.81` → IC=+0.331 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.81 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.15` → IC=+0.133 (n=118)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.15 (IC base=+0.118)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.299 (n=177)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.276)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.300 (n=88)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.276)

- **PATRÓN** `drift_60min` |x|≤ `0.0689` → IC=+0.344 (n=88)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0689 (IC base=+0.276)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.276 (n=248)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.276)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.289 (n=235)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.276)

- **PATRÓN** `ibs_20min` < `0.4375` → IC=+0.316 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4375 (IC base=+0.276)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.939` → IC=+0.311 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.939 (IC base=+0.276)

- **PATRÓN** `volumen_pendiente_norm` < `0.0561` → IC=+0.304 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0561 (IC base=+0.276)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.300 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.276)

- **PATRÓN** `volumen_spike_ratio` < `1.7987` → IC=+0.296 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7987 (IC base=+0.276)

- **PATRÓN** `volumen_spike_ratio` > `1.549` → IC=+0.292 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.549 (IC base=+0.276)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.336 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.276)

- **PATRÓN** `libro_liquidez` > `1985.6048` → IC=+0.300 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1985.6048 (IC base=+0.276)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.307 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 59.0 (IC base=+0.276)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.242 (n=165)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.208)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.220 (n=123)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.0953` → IC=+0.228 (n=123)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0953 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.233 (n=373)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.208 (n=351)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `0.4206` → IC=+0.220 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4206 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `0.2185` → IC=+0.231 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2185 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` < `0.5446` → IC=+0.208 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5446 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.353` → IC=+0.237 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.353 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.05` → IC=+0.209 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.05 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` < `1.2653` → IC=+0.214 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2653 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` > `1.0851` → IC=+0.240 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0851 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.267` → IC=+0.265 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.267 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` < `1.349` → IC=+0.252 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.349 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `11295.2956` → IC=+0.216 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11295.2956 (IC base=+0.208)

- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.183 (n=143)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0022 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.0739` → IC=+0.167 (n=142)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.0739 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.151 (n=399)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.151 (n=445)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 18.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.5892` → IC=+0.169 (n=424)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.5892 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` < `0.1407` → IC=+0.169 (n=358)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1407 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.981` → IC=+0.238 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.981 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `0.6331` → IC=+0.181 (n=142)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.6331 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` > `1.025` → IC=+0.149 (n=192)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 1.025 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.094` → IC=+0.215 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.094 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `1.7452` → IC=+0.181 (n=214)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.7452 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.4133` → IC=+0.162 (n=320)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.4133 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=546)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `14181.4555` → IC=+0.185 (n=141)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 14181.4555 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `254.0` → IC=+0.183 (n=102)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 254.0 (IC base=+0.141)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `drift_60min` |x|≤ `0.0944` → IC=+0.133 (n=194)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.66€ cuando `drift_60min` |x|≤ 0.0944 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.215 (n=156)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.277 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.923` → IC=+0.265 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.923 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` < `0.1064` → IC=+0.124 (n=325)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1064 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.174 (n=210)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `1917.9762` → IC=+0.144 (n=200)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 1917.9762 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.130 (n=44)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 15.0 (IC base=+0.132)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.293 (n=143)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.265)

- **PATRÓN** `drift_60min` |x|≤ `0.1276` → IC=+0.283 (n=141)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1276 (IC base=+0.265)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.277 (n=218)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.265)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.270 (n=333)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.265)

- **PATRÓN** `ibs_20min` < `0.5146` → IC=+0.302 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5146 (IC base=+0.265)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.037` → IC=+0.318 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.037 (IC base=+0.265)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.571` → IC=+0.265 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.571 (IC base=+0.265)

- **PATRÓN** `volumen_pendiente_norm` > `0.4178` → IC=+0.433 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.4178 (IC base=+0.265)

- **PATRÓN** `volumen_spike_ratio` < `3.6802` → IC=+0.234 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.6802 (IC base=+0.265)

- **PATRÓN** `volumen_spike_ratio` > `2.003` → IC=+0.237 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.003 (IC base=+0.265)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.280 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.265)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.241 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 28.0 (IC base=+0.265)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `ibs_20min` > `0.8711` → IC=-0.162 (n=196)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8711
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=593)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.162 (n=63)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=726)

- **PATRÓN** `dist_vwap_pct` > `0.1404` → IC=+0.326 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1404 (IC base=-0.032)

- **PATRÓN** `dist_vwap_pct` < `0.278` → IC=+0.306 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.278 (IC base=-0.032)

- **PATRÓN** `volumen_regimen` < `0.8497` → IC=+0.321 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8497 (IC base=-0.032)

- **PATRÓN** `volumen_regimen` > `0.7485` → IC=+0.306 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7485 (IC base=-0.032)

- **PATRÓN** `volumen_spike_ratio` < `1.4384` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4384 (IC base=-0.032)

- **PATRÓN** `dist_vwap_pct` > `0.2366` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2366 (IC base=-0.051)

- **PATRÓN** `volumen_pendiente_norm` > `0.0567` → IC=+0.269 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0567 (IC base=-0.051)

- **PATRÓN** `volumen_spike_ratio` > `2.3406` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3406 (IC base=-0.051)

- **PATRÓN** `ballena_activa_n` < `114.0` → IC=+0.167 (n=31)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 114.0 (IC base=-0.051)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.121 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=92)

- **FILTRO** `ibs_20min` > `0.7619` → IC=-0.160 (n=319)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7619
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=965)

- **FILTRO** `sigma_ewma_delta_pct` > `4.921` → IC=-0.153 (n=272)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.921
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=1012)

- **FILTRO** `volumen_pendiente_norm` < `0.0964` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.0964
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

- **FILTRO** `volumen_spike_ratio` > `1.6234` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.6234
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.197 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0055 (IC base=+0.045)

- **PATRÓN** `drift_60min` |x|≤ `0.2691` → IC=+0.145 (n=60)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.2691 (IC base=+0.045)

- **PATRÓN** `ibs_20min` > `0.6842` → IC=+0.198 (n=41)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.6842 (IC base=+0.045)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.5171` → IC=-0.156 (n=225)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.5171
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=438)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.164 (n=117)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=546)

- **FILTRO** `ibs_20min` > `0.7778` → IC=-0.171 (n=287)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7778
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=868)

- **FILTRO** `sigma_ewma_delta_pct` > `6.649` → IC=-0.155 (n=192)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.649
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=963)

- **PATRÓN** `dist_vwap_pct` < `0.2396` → IC=+0.175 (n=38)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.2396 (IC base=-0.091)

- **PATRÓN** `volumen_regimen` > `0.6932` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 0.6932 (IC base=-0.091)

- **PATRÓN** `dist_vwap_pct` < `0.2029` → IC=+0.222 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2029 (IC base=-0.035)

- **PATRÓN** `volumen_regimen` < `0.6966` → IC=+0.226 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6966 (IC base=-0.035)

- **PATRÓN** `volumen_regimen` > `1.1355` → IC=+0.250 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1355 (IC base=-0.035)

- **PATRÓN** `volumen_spike_ratio` > `1.9721` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.9721 (IC base=-0.035)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.133 (n=1271)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` > 0.0075 (IC base=+0.053)

- **PATRÓN** `ibs_20min` > `0.9449` → IC=+0.249 (n=933)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9449 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` > `1.2605` → IC=+0.288 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2605 (IC base=+0.053)

- **PATRÓN** `volumen_regimen` > `1.1561` → IC=+0.198 (n=322)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` > 1.1561 (IC base=+0.053)

- **PATRÓN** `volumen_pendiente_norm` < `0.1149` → IC=+0.168 (n=1250)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` < 0.1149 (IC base=+0.053)

- **PATRÓN** `volumen_pendiente_norm` > `0.2472` → IC=+0.207 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2472 (IC base=+0.053)

- **PATRÓN** `volumen_spike_ratio` < `1.4785` → IC=+0.195 (n=428)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4785 (IC base=+0.053)

- **PATRÓN** `volumen_spike_ratio` > `2.8359` → IC=+0.170 (n=428)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.8359 (IC base=+0.053)

- **PATRÓN** `ballena_activa_n` < `99.0` → IC=+0.266 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 99.0 (IC base=+0.053)

- **PATRÓN** `ibs_20min` < `0.0939` → IC=+0.185 (n=1187)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.0939 (IC base=+0.040)

- **PATRÓN** `dist_vwap_pct` > `1.1146` → IC=+0.214 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1146 (IC base=+0.040)

- **PATRÓN** `dist_vwap_pct` < `0.2092` → IC=+0.206 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2092 (IC base=+0.040)

- **PATRÓN** `volumen_regimen` > `1.229` → IC=+0.234 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.229 (IC base=+0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.2514` → IC=+0.361 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2514 (IC base=+0.040)

- **PATRÓN** `volumen_spike_ratio` > `2.3705` → IC=+0.289 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3705 (IC base=+0.040)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.261 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 58.0 (IC base=+0.040)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2448` → IC=-0.150 (n=181)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2448
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=370)

- **FILTRO** `sigma_ewma_delta_pct` > `3.504` → IC=-0.192 (n=170)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 3.504
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=577)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.142` → IC=+0.185 (n=106)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 5.142 (IC base=-0.012)

- **PATRÓN** `volumen_pendiente_norm` > `0.0542` → IC=+0.271 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0542 (IC base=-0.012)

- **PATRÓN** `volumen_spike_ratio` > `2.3584` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3584 (IC base=-0.012)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.8844` → IC=-0.140 (n=270)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8844
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=814)

- **PATRÓN** `volumen_regimen` > `0.9955` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.9955 (IC base=-0.041)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `drift_60min` |x|≤ `0.1` → IC=+0.205 (n=191)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.180 (n=145)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 18.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.253 (n=152)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.294 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.996` → IC=+0.290 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.996 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` < `0.1441` → IC=+0.189 (n=332)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` < 0.1441 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.4216` → IC=+0.179 (n=51)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.4216 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` < `2.0094` → IC=+0.196 (n=156)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.0094 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `3.625` → IC=+0.179 (n=160)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 3.625 (IC base=+0.179)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.228 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `1915.1184` → IC=+0.219 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1915.1184 (IC base=+0.179)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.353 (n=202)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.350)

- **PATRÓN** `drift_60min` |x|≤ `0.2221` → IC=+0.358 (n=153)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2221 (IC base=+0.350)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.391 (n=154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.350)

- **PATRÓN** `ibs_20min` < `0.3056` → IC=+0.357 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3056 (IC base=+0.350)

- **PATRÓN** `ibs_20min` > `0.1308` → IC=+0.358 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1308 (IC base=+0.350)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.378` → IC=+0.354 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.378 (IC base=+0.350)

- **PATRÓN** `volumen_pendiente_norm` > `0.1228` → IC=+0.379 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1228 (IC base=+0.350)

- **PATRÓN** `volumen_spike_ratio` < `1.732` → IC=+0.375 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.732 (IC base=+0.350)

- **PATRÓN** `volumen_spike_ratio` > `2.5357` → IC=+0.349 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5357 (IC base=+0.350)

- **PATRÓN** `libro_liquidez` > `1903.1828` → IC=+0.361 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1903.1828 (IC base=+0.350)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.156 (n=149)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=309)

- **FILTRO** `dist_vwap_pct` < `0.7343` → IC=-0.211 (n=43)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.7343
  - _Potencial_: sin este filtro IC_bueno=+0.259 (n=27)

- **FILTRO** `volumen_regimen` > `1.0041` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.0041
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=53)

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

- **FILTRO** `libro_spread` > `0.01` → IC=-0.162 (n=66)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=900)

- **PATRÓN** `dist_vwap_pct` > `0.7343` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7343 (IC base=-0.072)

- **PATRÓN** `volumen_spike_ratio` < `1.3975` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3975 (IC base=-0.072)

- **PATRÓN** `volumen_spike_ratio` > `1.7258` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.7258 (IC base=-0.072)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7368` → IC=-0.123 (n=415)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7368
  - _Potencial_: sin este filtro IC_bueno=+0.211 (n=216)

- **FILTRO** `ibs_20min` > `0.75` → IC=-0.182 (n=215)

  - _Acción_: SKIP cuando `ibs_20min` > 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=671)

- **FILTRO** `dist_vwap_pct` > `0.1326` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1326
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=53)

- **FILTRO** `sigma_ewma_delta_pct` > `4.583` → IC=-0.127 (n=215)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.583
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=671)

- **FILTRO** `volumen_regimen` > `1.3339` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.3339
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=52)

- **FILTRO** `volumen_spike_ratio` < `1.7495` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.7495
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=17)

- **PATRÓN** `ibs_20min` > `0.8519` → IC=+0.264 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8519 (IC base=-0.009)

- **PATRÓN** `dist_vwap_pct` > `0.3259` → IC=+0.264 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3259 (IC base=-0.009)

- **PATRÓN** `volumen_regimen` < `0.8598` → IC=+0.191 (n=121)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.8598 (IC base=-0.009)

- **PATRÓN** `volumen_regimen` > `1.1463` → IC=+0.226 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1463 (IC base=-0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.2337` → IC=+0.263 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2337 (IC base=-0.009)

- **PATRÓN** `volumen_spike_ratio` < `1.4917` → IC=+0.178 (n=57)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.4917 (IC base=-0.009)

- **PATRÓN** `volumen_spike_ratio` > `2.0524` → IC=+0.183 (n=77)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.0524 (IC base=-0.009)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.228 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 51.0 (IC base=-0.009)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0244` → IC=+0.319 (n=186)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0244 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.227 (n=214)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.226 (n=210)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `0.8983` → IC=+0.296 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8983 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` > `1.3817` → IC=+0.336 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.3817 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.12` → IC=+0.275 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.12 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` > `0.8368` → IC=+0.245 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8368 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` < `0.0802` → IC=+0.221 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0802 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.2775` → IC=+0.267 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2775 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` < `1.4052` → IC=+0.262 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4052 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.234 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `3084.4124` → IC=+0.245 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3084.4124 (IC base=+0.214)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.280 (n=252)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.268)

- **PATRÓN** `drift_60min` |x|≤ `0.4819` → IC=+0.273 (n=501)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4819 (IC base=+0.268)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.279 (n=531)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.268)

- **PATRÓN** `ibs_20min` < `0.2766` → IC=+0.327 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2766 (IC base=+0.268)

- **PATRÓN** `dist_vwap_pct` < `0.8839` → IC=+0.275 (n=650)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8839 (IC base=+0.268)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.746` → IC=+0.322 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.746 (IC base=+0.268)

- **PATRÓN** `volumen_regimen` > `1.2513` → IC=+0.302 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2513 (IC base=+0.268)

- **PATRÓN** `volumen_pendiente_norm` > `0.2435` → IC=+0.366 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2435 (IC base=+0.268)

- **PATRÓN** `volumen_spike_ratio` > `2.167` → IC=+0.301 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.167 (IC base=+0.268)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.254 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.268)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.196 (n=808)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0099 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.3315` → IC=+0.157 (n=2132)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.3315 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.182 (n=891)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.155)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.158 (n=916)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 6.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.284 (n=1201)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.7889` → IC=+0.252 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7889 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.334` → IC=+0.248 (n=1029)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.334 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` > `0.686` → IC=+0.171 (n=1504)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 0.686 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.1017` → IC=+0.183 (n=869)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1017 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `2.2796` → IC=+0.152 (n=1914)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.2796 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `1.8508` → IC=+0.149 (n=1450)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.8508 (IC base=+0.155)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.167 (n=1980)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `3197.545` → IC=+0.183 (n=1098)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 3197.545 (IC base=+0.155)

- **PATRÓN** `ballena_activa_n` < `123.0` → IC=+0.176 (n=1170)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 123.0 (IC base=+0.155)

- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.200 (n=1896)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0074 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.4119` → IC=+0.199 (n=2153)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4119 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=821)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` < `0.4082` → IC=+0.240 (n=2153)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4082 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` < `0.3565` → IC=+0.178 (n=1890)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.3565 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.766` → IC=+0.222 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.766 (IC base=+0.186)

- **PATRÓN** `volumen_regimen` < `1.174` → IC=+0.168 (n=1741)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.174 (IC base=+0.186)

- **PATRÓN** `volumen_regimen` > `0.8585` → IC=+0.173 (n=1160)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 0.8585 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.2874` → IC=+0.249 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2874 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` < `1.8722` → IC=+0.179 (n=1029)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.8722 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `2.6198` → IC=+0.212 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6198 (IC base=+0.186)

- **PATRÓN** `ballena_activa_n` < `201.0` → IC=+0.185 (n=1112)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 201.0 (IC base=+0.186)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.217 (n=178)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.253` → IC=+0.151 (n=391)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.253 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.203 (n=190)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.306 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.031` → IC=+0.343 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.031 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.1485` → IC=+0.177 (n=94)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1485 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `1.5512` → IC=+0.128 (n=280)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.5512 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.172 (n=236)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.04 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.277 (n=168)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.269)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.277 (n=191)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.269)

- **PATRÓN** `drift_60min` |x|≤ `0.3308` → IC=+0.312 (n=190)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3308 (IC base=+0.269)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.292 (n=176)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.269)

- **PATRÓN** `ibs_20min` < `0.0737` → IC=+0.360 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0737 (IC base=+0.269)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.838` → IC=+0.283 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.838 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` < `1.7907` → IC=+0.316 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7907 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` > `2.8103` → IC=+0.300 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8103 (IC base=+0.269)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.333 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.269)

- **PATRÓN** `libro_liquidez` > `1981.9929` → IC=+0.348 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1981.9929 (IC base=+0.269)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.289 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 51.0 (IC base=+0.269)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.237 (n=116)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.179)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.198 (n=114)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0072 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.208 (n=344)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `0.9974` → IC=+0.279 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9974 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.2093` → IC=+0.245 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2093 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.757` → IC=+0.236 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.757 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `1.2907` → IC=+0.187 (n=343)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 1.2907 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` > `0.8896` → IC=+0.196 (n=228)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` > 0.8896 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.2178` → IC=+0.268 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2178 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` < `1.378` → IC=+0.220 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.378 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `12172.2264` → IC=+0.200 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12172.2264 (IC base=+0.179)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.171 (n=436)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0056 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.2908` → IC=+0.176 (n=436)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2908 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.173 (n=399)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 7.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.4065` → IC=+0.190 (n=436)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.4065 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `0.1569` → IC=+0.177 (n=429)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.1569 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.387` → IC=+0.243 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.387 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.7208` → IC=+0.222 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7208 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.1009` → IC=+0.213 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1009 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `1.7388` → IC=+0.174 (n=219)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.7388 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `14307.4169` → IC=+0.160 (n=145)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 14307.4169 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `244.0` → IC=+0.163 (n=81)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 244.0 (IC base=+0.151)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `drift_60min` |x|≤ `0.147` → IC=+0.160 (n=233)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.147 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.181 (n=117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.214 (n=117)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.294 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.904` → IC=+0.300 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.904 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` < `0.226` → IC=+0.144 (n=287)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` < 0.226 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `1.9887` → IC=+0.200 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9887 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `3.6503` → IC=+0.139 (n=131)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 3.6503 (IC base=+0.151)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.201 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `1960.841` → IC=+0.181 (n=117)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 1960.841 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.312 (n=99)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.280)

- **PATRÓN** `drift_60min` |x|≤ `0.2002` → IC=+0.322 (n=150)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2002 (IC base=+0.280)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.318 (n=152)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.280)

- **PATRÓN** `ibs_20min` < `0.3046` → IC=+0.319 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3046 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.244` → IC=+0.321 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.244 (IC base=+0.280)

- **PATRÓN** `volumen_pendiente_norm` > `0.3755` → IC=+0.426 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3755 (IC base=+0.280)

- **PATRÓN** `volumen_spike_ratio` > `1.9742` → IC=+0.279 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9742 (IC base=+0.280)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.248 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 59.0 (IC base=+0.280)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.218 (n=346)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0093 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.1378` → IC=+0.227 (n=152)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1378 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.210 (n=312)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `0.4502` → IC=+0.238 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4502 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` > `1.0398` → IC=+0.244 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0398 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.194` → IC=+0.312 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.194 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` > `0.6366` → IC=+0.195 (n=345)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` > 0.6366 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.1003` → IC=+0.239 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1003 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` < `1.4299` → IC=+0.202 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4299 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.4478` → IC=+0.228 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4478 (IC base=+0.182)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.184 (n=394)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.01 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `8728.1176` → IC=+0.203 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8728.1176 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `107.0` → IC=+0.190 (n=98)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 107.0 (IC base=+0.182)

- **PATRÓN** `sigma_h` < `0.0024` → IC=+0.252 (n=139)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0024 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.3788` → IC=+0.167 (n=415)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.3788 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=160)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.1102` → IC=+0.245 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1102 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.3199` → IC=+0.166 (n=459)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.3199 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.227` → IC=+0.215 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.227 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `0.8554` → IC=+0.160 (n=277)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8554 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` > `0.6177` → IC=+0.155 (n=415)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.6177 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.0996` → IC=+0.167 (n=121)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0996 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `1.8875` → IC=+0.188 (n=206)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.8875 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `10007.3401` → IC=+0.152 (n=139)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 10007.3401 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `196.0` → IC=+0.129 (n=200)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 196.0 (IC base=+0.147)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **FILTRO** `ibs_20min` > `0.4107` → IC=-0.194 (n=132)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4107
  - _Potencial_: sin este filtro IC_bueno=+0.233 (n=399)

- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.204 (n=218)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0103 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.134 (n=501)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.8542` → IC=+0.236 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8542 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `0.7937` → IC=+0.276 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7937 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.191` → IC=+0.293 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.191 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` > `0.6804` → IC=+0.143 (n=429)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.6804 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.2789` → IC=+0.130 (n=71)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` > 0.2789 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `1.5631` → IC=+0.132 (n=400)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 1.5631 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `3206.3834` → IC=+0.216 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3206.3834 (IC base=+0.119)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.189 (n=133)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0049 (IC base=+0.127)

- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.189 (n=133)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0097 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=142)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` < `0.4107` → IC=+0.233 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4107 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` < `0.2166` → IC=+0.143 (n=371)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.2166 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.682` → IC=+0.196 (n=77)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 6.682 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `1.1954` → IC=+0.138 (n=399)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.1954 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` > `0.8536` → IC=+0.164 (n=266)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.8536 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2198` → IC=+0.196 (n=54)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2198 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `2.2466` → IC=+0.206 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2466 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `2065.7928` → IC=+0.175 (n=266)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2065.7928 (IC base=+0.127)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0227` → IC=+0.191 (n=234)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0227 (IC base=+0.162)

- **PATRÓN** `drift_60min` |x|≤ `0.1638` → IC=+0.191 (n=228)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1638 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.199 (n=184)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` > `0.9167` → IC=+0.261 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9167 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` > `1.6268` → IC=+0.254 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.6268 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.082` → IC=+0.245 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.082 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` > `0.8248` → IC=+0.188 (n=344)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` > 0.8248 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` > `0.0805` → IC=+0.221 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0805 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` < `2.1643` → IC=+0.174 (n=422)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 2.1643 (IC base=+0.162)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.172 (n=562)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.01 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `2453.0908` → IC=+0.164 (n=516)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2453.0908 (IC base=+0.162)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.277 (n=164)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.6677` → IC=+0.237 (n=492)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6677 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.224 (n=237)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.255 (n=235)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` < `0.1333` → IC=+0.300 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1333 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` < `0.8176` → IC=+0.230 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8176 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.175` → IC=+0.286 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.175 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` > `0.7127` → IC=+0.244 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7127 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.336 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `1.5893` → IC=+0.222 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5893 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `32.0` → IC=+0.188 (n=274)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 32.0 (IC base=+0.222)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `hora_utc` > `16.0` → IC=+0.187 (n=215)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 16.0 (IC base=+0.086)

- **PATRÓN** `ibs_20min` > `0.6275` → IC=+0.154 (n=380)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` > 0.6275 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` > `0.7807` → IC=+0.250 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7807 (IC base=+0.086)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.273` → IC=+0.194 (n=122)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 8.273 (IC base=+0.086)

- **PATRÓN** `volumen_pendiente_norm` > `0.1727` → IC=+0.188 (n=110)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.1727 (IC base=+0.086)

- **PATRÓN** `libro_liquidez` > `2920.0962` → IC=+0.128 (n=283)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 2920.0962 (IC base=+0.086)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.165 (n=168)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0041 (IC base=+0.082)

- **PATRÓN** `drift_60min` |x|≤ `0.1135` → IC=+0.129 (n=168)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.1135 (IC base=+0.082)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.132 (n=188)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 14.0 (IC base=+0.082)

- **PATRÓN** `ibs_20min` < `0.6296` → IC=+0.133 (n=382)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.6296 (IC base=+0.082)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.17` → IC=+0.206 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.17 (IC base=+0.082)

- **PATRÓN** `volumen_regimen` < `0.7418` → IC=+0.143 (n=155)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.7418 (IC base=+0.082)

- **PATRÓN** `volumen_spike_ratio` < `1.852` → IC=+0.145 (n=218)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.852 (IC base=+0.082)

- **PATRÓN** `libro_liquidez` > `3871.0971` → IC=+0.129 (n=254)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 3871.0971 (IC base=+0.082)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.214 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=85)

- **FILTRO** `ibs_20min` < `0.4225` → IC=-0.224 (n=27)

  - _Acción_: SKIP cuando `ibs_20min` < 0.4225
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=84)

- **FILTRO** `libro_liquidez` < `6436.909` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `libro_liquidez` < 6436.909
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=84)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.210 (n=29)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.031)

- **PATRÓN** `ibs_20min` > `0.9306` → IC=+0.225 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9306 (IC base=+0.031)

- **PATRÓN** `dist_vwap_pct` > `0.7767` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.7767 (IC base=+0.031)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.351` → IC=+0.150 (n=38)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 4.351 (IC base=+0.031)

- **PATRÓN** `libro_liquidez` > `11800.2375` → IC=+0.138 (n=56)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 11800.2375 (IC base=+0.031)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.232 (n=69)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.164)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.212 (n=71)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.3512` → IC=+0.194 (n=155)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.3512 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=53)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.179 (n=138)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 14.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` < `0.6705` → IC=+0.188 (n=155)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.6705 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` < `0.2207` → IC=+0.178 (n=144)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.2207 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.286` → IC=+0.357 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.286 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `1.2044` → IC=+0.188 (n=155)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 1.2044 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.0873` → IC=+0.333 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0873 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `1.7117` → IC=+0.217 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7117 (IC base=+0.164)

- **PATRÓN** `ballena_activa_n` < `137.0` → IC=+0.179 (n=54)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 137.0 (IC base=+0.164)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.281 (n=80)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.279)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.306 (n=60)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.279)

- **PATRÓN** `drift_60min` |x|≤ `0.2275` → IC=+0.278 (n=61)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2275 (IC base=+0.279)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.343 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.279)

- **PATRÓN** `ibs_20min` > `0.8134` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8134 (IC base=+0.279)

- **PATRÓN** `dist_vwap_pct` > `0.9351` → IC=+0.389 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9351 (IC base=+0.279)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.561` → IC=+0.378 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.561 (IC base=+0.279)

- **PATRÓN** `volumen_regimen` < `0.6873` → IC=+0.381 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6873 (IC base=+0.279)

- **PATRÓN** `volumen_pendiente_norm` > `0.184` → IC=+0.389 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.184 (IC base=+0.279)

- **PATRÓN** `volumen_spike_ratio` < `2.3129` → IC=+0.295 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3129 (IC base=+0.279)

- **PATRÓN** `volumen_spike_ratio` > `1.5464` → IC=+0.297 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5464 (IC base=+0.279)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.371 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.068)

- **PATRÓN** `drift_60min` |x|≤ `0.3482` → IC=+0.142 (n=65)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.3482 (IC base=+0.068)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.233 (n=43)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.068)

- **PATRÓN** `ibs_20min` < `0.5743` → IC=+0.142 (n=65)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.5743 (IC base=+0.068)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.025` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 6.025 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` < `0.7011` → IC=+0.274 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7011 (IC base=+0.068)

- **PATRÓN** `libro_liquidez` > `9388.7076` → IC=+0.292 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9388.7076 (IC base=+0.068)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` < `0.619` → IC=-0.151 (n=64)

  - _Acción_: SKIP cuando `ibs_20min` < 0.619
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=132)

- **FILTRO** `ibs_20min` > `0.66` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `ibs_20min` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=82)

- **FILTRO** `dist_vwap_pct` > `0.1911` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1911
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=88)

- **FILTRO** `volumen_spike_ratio` > `3.1841` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 3.1841
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=65)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.155 (n=56)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.020)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.186 (n=68)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 1.0 (IC base=+0.020)

- **PATRÓN** `dist_vwap_pct` > `0.6172` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.6172 (IC base=+0.020)

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
- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.207 (n=1278)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0079 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.173 (n=941)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 18.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.9432` → IC=+0.292 (n=1276)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9432 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `1.0701` → IC=+0.254 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0701 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.33` → IC=+0.246 (n=1185)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.33 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.8808` → IC=+0.148 (n=1328)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8808 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` > `1.0803` → IC=+0.154 (n=903)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 1.0803 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.1649` → IC=+0.184 (n=716)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1649 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.8707` → IC=+0.160 (n=1664)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.8707 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=2296)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `3925.9545` → IC=+0.193 (n=938)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 3925.9545 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `158.0` → IC=+0.191 (n=1268)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 158.0 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.228 (n=1677)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.4629` → IC=+0.205 (n=2513)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4629 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.202 (n=939)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.208 (n=923)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` < `0.5552` → IC=+0.253 (n=2512)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5552 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` < `0.7149` → IC=+0.185 (n=2052)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.7149 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.373` → IC=+0.227 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.373 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.646` → IC=+0.200 (n=2363)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.646 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` < `0.6242` → IC=+0.190 (n=633)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.6242 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` > `1.1929` → IC=+0.191 (n=632)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 1.1929 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.2339` → IC=+0.271 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2339 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` > `2.256` → IC=+0.214 (n=823)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.256 (IC base=+0.197)

- **PATRÓN** `ballena_activa_n` < `180.0` → IC=+0.179 (n=1386)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 180.0 (IC base=+0.197)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.220 (n=205)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.168 (n=302)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 11.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.8271` → IC=+0.256 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8271 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.503` → IC=+0.355 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.503 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.2156` → IC=+0.199 (n=71)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2156 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.9026` → IC=+0.140 (n=248)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.9026 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.187 (n=241)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.04 (IC base=+0.141)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.326 (n=182)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.1024` → IC=+0.328 (n=120)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1024 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.283 (n=256)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.284)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.296 (n=248)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.284)

- **PATRÓN** `ibs_20min` < `0.5833` → IC=+0.340 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5833 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` < `0.0678` → IC=+0.295 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0678 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` > `0.226` → IC=+0.295 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.226 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` > `2.7158` → IC=+0.350 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7158 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.318 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `1990.5404` → IC=+0.339 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1990.5404 (IC base=+0.284)

- **PATRÓN** `ballena_activa_n` < `72.0` → IC=+0.288 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 72.0 (IC base=+0.284)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.178 (n=150)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0028 (IC base=+0.155)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.202 (n=149)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.184 (n=400)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 8.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `0.3271` → IC=+0.207 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3271 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.2561` → IC=+0.249 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2561 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.707` → IC=+0.205 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.707 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `1.2673` → IC=+0.160 (n=445)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2673 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` > `1.099` → IC=+0.176 (n=202)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 1.099 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.2054` → IC=+0.229 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2054 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `2.109` → IC=+0.181 (n=349)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 2.109 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `1.4628` → IC=+0.188 (n=354)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 1.4628 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `11800.2375` → IC=+0.182 (n=297)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 11800.2375 (IC base=+0.155)

- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.206 (n=141)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0022 (IC base=+0.168)

- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.171 (n=141)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0057 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.2654` → IC=+0.181 (n=371)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.2654 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.173 (n=396)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 7.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.181 (n=437)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 18.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` < `0.376` → IC=+0.221 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.376 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` < `0.7428` → IC=+0.177 (n=469)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.7428 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.638` → IC=+0.231 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.638 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `0.6257` → IC=+0.241 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6257 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` > `1.1856` → IC=+0.171 (n=141)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 1.1856 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.1496` → IC=+0.290 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1496 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `2.4777` → IC=+0.195 (n=326)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.4777 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `1.5054` → IC=+0.189 (n=291)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 1.5054 (IC base=+0.168)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.169 (n=545)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.01 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `12049.3014` → IC=+0.175 (n=192)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 12049.3014 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `313.0` → IC=+0.179 (n=76)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 313.0 (IC base=+0.168)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `hora_utc` < `8.0` → IC=+0.237 (n=169)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `0.7078` → IC=+0.264 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7078 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.096` → IC=+0.345 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.096 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` < `0.2274` → IC=+0.183 (n=304)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.2274 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` < `2.035` → IC=+0.209 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.035 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `3.686` → IC=+0.174 (n=136)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 3.686 (IC base=+0.179)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `1917.9762` → IC=+0.202 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1917.9762 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.227 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 59.0 (IC base=+0.179)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.326 (n=153)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.267)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.283 (n=233)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.267)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.292 (n=118)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.267)

- **PATRÓN** `ibs_20min` < `0.5652` → IC=+0.333 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5652 (IC base=+0.267)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.093` → IC=+0.311 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.093 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` > `0.3655` → IC=+0.306 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3655 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` < `1.7663` → IC=+0.305 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7663 (IC base=+0.267)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.273 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.267)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.214 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.267)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0089` → IC=+0.153 (n=450)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0089 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.168 (n=410)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 8.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` > `0.34` → IC=+0.199 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.34 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.8989` → IC=+0.214 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8989 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.433` → IC=+0.197 (n=216)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 4.433 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `0.6307` → IC=+0.184 (n=150)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6307 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` > `1.1984` → IC=+0.165 (n=150)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 1.1984 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.2675` → IC=+0.281 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2675 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `1.4` → IC=+0.195 (n=414)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.4 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `5388.027` → IC=+0.229 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5388.027 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `167.0` → IC=+0.177 (n=218)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 167.0 (IC base=+0.142)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.183 (n=326)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0076 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.5098` → IC=+0.169 (n=369)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.5098 (IC base=+0.157)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.186 (n=259)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 11.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` < `0.0817` → IC=+0.252 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0817 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.1609` → IC=+0.165 (n=189)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.1609 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` < `0.6682` → IC=+0.179 (n=394)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.6682 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.454` → IC=+0.254 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.454 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` < `0.596` → IC=+0.180 (n=123)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.596 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` > `1.1275` → IC=+0.188 (n=123)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` > 1.1275 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.231` → IC=+0.360 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.231 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `2.1819` → IC=+0.196 (n=274)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.1819 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` > `1.4584` → IC=+0.180 (n=311)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.4584 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `9483.0008` → IC=+0.216 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9483.0008 (IC base=+0.157)

- **PATRÓN** `ballena_activa_n` < `138.0` → IC=+0.238 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 138.0 (IC base=+0.157)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.174 (n=228)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0107 (IC base=+0.099)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.161 (n=178)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 18.0 (IC base=+0.099)

- **PATRÓN** `ibs_20min` > `0.9091` → IC=+0.309 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9091 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `1.0536` → IC=+0.279 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0536 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.428` → IC=+0.228 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.428 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `2942.126` → IC=+0.282 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2942.126 (IC base=+0.099)

- **PATRÓN** `ballena_activa_n` < `68.0` → IC=+0.175 (n=278)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 68.0 (IC base=+0.099)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.178 (n=203)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0059 (IC base=+0.123)

- **PATRÓN** `drift_60min` |x|≤ `0.2624` → IC=+0.141 (n=307)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.2624 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.181 (n=214)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.130 (n=163)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 5.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` < `0.5789` → IC=+0.204 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5789 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` < `0.4623` → IC=+0.142 (n=420)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.4623 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.03` → IC=+0.140 (n=451)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 3.03 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `0.7055` → IC=+0.154 (n=203)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.7055 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.072` → IC=+0.177 (n=125)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.072 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `1.7463` → IC=+0.171 (n=208)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.7463 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.129 (n=480)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.02 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `2581.4636` → IC=+0.173 (n=209)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2581.4636 (IC base=+0.123)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0264` → IC=+0.211 (n=199)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0264 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.195 (n=231)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 17.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` > `0.9655` → IC=+0.294 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9655 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` > `1.4549` → IC=+0.288 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.4549 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.048` → IC=+0.246 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.048 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` < `0.611` → IC=+0.177 (n=199)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.611 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` > `1.0359` → IC=+0.195 (n=270)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` > 1.0359 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.1713` → IC=+0.248 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1713 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` > `1.8207` → IC=+0.186 (n=364)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.8207 (IC base=+0.170)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.186 (n=644)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.170)

- **PATRÓN** `libro_liquidez` > `3104.3643` → IC=+0.187 (n=199)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 3104.3643 (IC base=+0.170)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.210 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.170)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.302 (n=215)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.4762` → IC=+0.229 (n=567)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4762 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.225 (n=598)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.215)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.217 (n=686)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` < `0.4884` → IC=+0.281 (n=645)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4884 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` < `1.2142` → IC=+0.224 (n=755)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 1.2142 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.527` → IC=+0.281 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.527 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.03` → IC=+0.218 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.03 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` > `1.2292` → IC=+0.256 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2292 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.2827` → IC=+0.313 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2827 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `2.5394` → IC=+0.242 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5394 (IC base=+0.215)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.178 (n=358)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 37.0 (IC base=+0.215)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.156 (n=946)

- **PATRÓN** `sigma_h` < `0.0098` → IC=+0.134 (n=405)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0098 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.160 (n=186)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` > `0.8291` → IC=+0.151 (n=210)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` > 0.8291 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` > `1.4484` → IC=+0.189 (n=117)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 1.4484 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.261` → IC=+0.194 (n=70)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 10.261 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `0.6118` → IC=+0.147 (n=131)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.6118 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` > `0.8942` → IC=+0.127 (n=261)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.8942 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.1529` → IC=+0.167 (n=130)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.1529 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` < `1.4889` → IC=+0.148 (n=200)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.4889 (IC base=+0.113)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.130 (n=430)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `8162.0536` → IC=+0.150 (n=307)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 8162.0536 (IC base=+0.113)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.209 (n=242)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0035 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.3567` → IC=+0.169 (n=635)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.3567 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.169 (n=267)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.207 (n=281)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` < `0.6304` → IC=+0.159 (n=635)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.6304 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.0862` → IC=+0.157 (n=721)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.0862 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.6223` → IC=+0.171 (n=159)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.6223 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.7855` → IC=+0.148 (n=818)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.7855 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.057` → IC=+0.163 (n=321)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 4.057 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.039` → IC=+0.151 (n=726)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 6.039 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `1.2228` → IC=+0.164 (n=707)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2228 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.0707` → IC=+0.167 (n=343)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0707 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.4757` → IC=+0.168 (n=714)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 2.4757 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.5115` → IC=+0.156 (n=638)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.5115 (IC base=+0.150)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.156 (n=946)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `8505.7624` → IC=+0.154 (n=721)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 8505.7624 (IC base=+0.150)

### GBM_LATE_5M#BTC#5min
- **FILTRO** `hora_utc` < `10.0` → IC=-0.167 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.142 (n=65)

- **FILTRO** `sigma_ewma_delta_pct` > `5.401` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.401
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=68)

- **FILTRO** `volumen_pendiente_norm` > `0.0946` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0946
  - _Potencial_: sin este filtro IC_bueno=+0.129 (n=68)

- **FILTRO** `libro_liquidez` < `12732.4097` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `libro_liquidez` < 12732.4097
  - _Potencial_: sin este filtro IC_bueno=+0.178 (n=57)

- **PATRÓN** `sigma_h` > `0.0037` → IC=+0.144 (n=57)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0037 (IC base=+0.070)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.142 (n=65)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 10.0 (IC base=+0.070)

- **PATRÓN** `ibs_20min` < `0.8908` → IC=+0.121 (n=64)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.8908 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.5895` → IC=+0.173 (n=47)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.5895 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.401` → IC=+0.143 (n=68)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 5.401 (IC base=+0.070)

- **PATRÓN** `volumen_regimen` > `0.7732` → IC=+0.136 (n=42)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.7732 (IC base=+0.070)

- **PATRÓN** `volumen_pendiente_norm` < `0.0946` → IC=+0.129 (n=68)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.0946 (IC base=+0.070)

- **PATRÓN** `libro_liquidez` > `12732.4097` → IC=+0.178 (n=57)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 12732.4097 (IC base=+0.070)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.170 (n=407)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0063 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.3549` → IC=+0.155 (n=407)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.3549 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.194 (n=158)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.198 (n=157)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 5.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.1706` → IC=+0.174 (n=179)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.1706 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.6097` → IC=+0.172 (n=59)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.6097 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.318` → IC=+0.159 (n=412)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` < 6.318 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.1834` → IC=+0.155 (n=407)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.1834 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` > `0.6229` → IC=+0.155 (n=407)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.6229 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.0724` → IC=+0.184 (n=188)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.0724 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.5395` → IC=+0.162 (n=406)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.5395 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.7781` → IC=+0.151 (n=270)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.7781 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `11900.5247` → IC=+0.150 (n=364)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 11900.5247 (IC base=+0.147)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0089` → IC=+0.187 (n=193)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0089 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.4517` → IC=+0.156 (n=193)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.4517 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.223 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` < `0.1748` → IC=+0.180 (n=73)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.1748 (IC base=+0.142)

- **PATRÓN** `ibs_20min` > `0.8027` → IC=+0.183 (n=99)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.8027 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `1.1467` → IC=+0.223 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1467 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` < `0.4203` → IC=+0.158 (n=185)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.4203 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.126` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 11.126 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.678` → IC=+0.144 (n=217)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 6.678 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `0.6457` → IC=+0.180 (n=73)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.6457 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.0798` → IC=+0.160 (n=98)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.0798 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `1.4017` → IC=+0.226 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4017 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `8958.3045` → IC=+0.185 (n=195)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 8958.3045 (IC base=+0.142)

- **PATRÓN** `sigma_h` < `0.0088` → IC=+0.176 (n=214)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0088 (IC base=+0.155)

- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.162 (n=143)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0062 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.497` → IC=+0.190 (n=214)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.497 (IC base=+0.155)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.190 (n=143)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 9.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` < `0.612` → IC=+0.154 (n=189)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.612 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `0.0983` → IC=+0.190 (n=214)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.0983 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.1925` → IC=+0.156 (n=91)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1925 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` < `0.3474` → IC=+0.170 (n=207)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.3474 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.347` → IC=+0.200 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.347 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `1.1886` → IC=+0.194 (n=214)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 1.1886 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` < `0.0653` → IC=+0.178 (n=181)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` < 0.0653 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `2.1395` → IC=+0.206 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1395 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `1.5125` → IC=+0.193 (n=187)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.5125 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `10370.4756` → IC=+0.189 (n=72)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 10370.4756 (IC base=+0.155)

### GBM_LATE_5M#SOL#5min
- **FILTRO** `sigma_h` < `0.0141` → IC=-0.167 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0141
  - _Potencial_: sin este filtro IC_bueno=+0.188 (n=14)

- **FILTRO** `sigma_ewma_delta_pct` < `3.03` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 3.03
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=22)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.704` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 4.704 (IC base=+0.000)

### GBM_LATE_60M
- **FILTRO** `ibs_20min` < `0.6481` → IC=-0.196 (n=44)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6481
  - _Potencial_: sin este filtro IC_bueno=+0.201 (n=135)

- **FILTRO** `sigma_h` > `0.0111` → IC=-0.296 (n=52)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0111
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=160)

- **FILTRO** `ibs_20min` > `0.2` → IC=-0.191 (n=82)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=28)

- **FILTRO** `dist_vwap_pct` > `0.1067` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1067
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=53)

- **FILTRO** `volumen_regimen` > `0.8876` → IC=-0.196 (n=54)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8876
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=56)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.180 (n=151)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0054 (IC base=+0.061)

- **PATRÓN** `drift_60min` |x|≤ `0.1288` → IC=+0.153 (n=47)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1288 (IC base=+0.061)

- **PATRÓN** `ibs_20min` > `0.6481` → IC=+0.201 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6481 (IC base=+0.061)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.134` → IC=+0.211 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.134 (IC base=+0.061)

- **PATRÓN** `volumen_pendiente_norm` < `0.0801` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0801 (IC base=+0.061)

- **PATRÓN** `volumen_spike_ratio` > `1.4971` → IC=+0.300 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4971 (IC base=+0.061)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.147 (n=120)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.02 (IC base=+0.061)

- **PATRÓN** `libro_liquidez` > `1942.5119` → IC=+0.134 (n=99)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 1942.5119 (IC base=+0.061)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.7741` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7741
  - _Potencial_: sin este filtro IC_bueno=+0.217 (n=44)

- **FILTRO** `hora_utc` > `2.0` → IC=-0.179 (n=51)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 2.0
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=19)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.328 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.065)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.125 (n=38)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 10.0 (IC base=+0.065)

- **PATRÓN** `ibs_20min` > `0.7741` → IC=+0.217 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7741 (IC base=+0.065)

- **PATRÓN** `dist_vwap_pct` > `0.1647` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1647 (IC base=+0.065)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.15` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 13.15 (IC base=+0.065)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0071` → IC=-0.326 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0071
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=43)

- **FILTRO** `hora_utc` > `9.0` → IC=-0.318 (n=31)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.129 (n=33)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.171 (n=80)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0059 (IC base=+0.107)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.123 (n=83)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 7.0 (IC base=+0.107)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.350 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.107)

- **PATRÓN** `dist_vwap_pct` < `0.2422` → IC=+0.224 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2422 (IC base=+0.107)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.06` → IC=+0.312 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.06 (IC base=+0.107)

- **PATRÓN** `volumen_regimen` < `0.6214` → IC=+0.224 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6214 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2519.6873` → IC=+0.241 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2519.6873 (IC base=+0.107)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `hora_utc` < `18.0` → IC=-0.128 (n=49)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 18.0
  - _Potencial_: sin este filtro IC_bueno=+0.179 (n=26)

- **FILTRO** `sigma_h` > `0.0165` → IC=-0.309 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0165
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=59)

- **FILTRO** `ibs_20min` > `0.4286` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4286
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` < `0.004` → IC=-0.312 (n=62)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.004
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=33)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.423 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=58)

- **FILTRO** `ibs_20min` < `0.3707` → IC=-0.308 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3707
  - _Potencial_: sin este filtro IC_bueno=-0.289 (n=74)

- **FILTRO** `dist_vwap_pct` < `0.1009` → IC=-0.354 (n=53)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1009
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=45)

- **FILTRO** `dist_vwap_pct` > `0.3507` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3507
  - _Potencial_: sin este filtro IC_bueno=-0.281 (n=80)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `sigma_h` < `0.002` → IC=-0.237 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.002
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=18)

- **FILTRO** `ibs_20min` < `0.5407` → IC=-0.286 (n=26)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5407
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `sigma_h` < `0.0019` → IC=-0.318 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0019
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=21)

- **FILTRO** `ibs_20min` > `0.6267` → IC=-0.364 (n=20)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6267
  - _Potencial_: sin este filtro IC_bueno=-0.152 (n=21)

- **FILTRO** `volumen_regimen` > `0.807` → IC=-0.318 (n=20)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.807
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=21)

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
- **FILTRO** `sigma_h` < `0.0063` → IC=-0.250 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `ibs_20min` < `0.6` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `sigma_h` < `0.0065` → IC=-0.382 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0065
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.441 (n=15)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` < `0.5842` → IC=-0.245 (n=45)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5842
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=138)

- **FILTRO** `dist_vwap_pct` > `0.2258` → IC=-0.145 (n=29)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2258
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=116)

- **PATRÓN** `ibs_20min` > `0.5842` → IC=+0.143 (n=138)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.5842 (IC base=+0.046)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.120 (n=77)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 12.0 (IC base=+0.024)

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

- **PATRÓN** `drift_60min` |x|≤ `0.129` → IC=+0.157 (n=33)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.129 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.250 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.097)

- **PATRÓN** `ibs_20min` < `0.3394` → IC=+0.173 (n=53)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.3394 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` < `1.0741` → IC=+0.133 (n=47)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.0741 (IC base=+0.097)

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
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.129 (n=114)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 6.0 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `2580.0317` → IC=+0.200 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2580.0317 (IC base=+0.101)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.159 (n=127)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 18.0 (IC base=+0.138)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `py_entrada` < 0.495 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `2495.3515` → IC=+0.169 (n=119)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2495.3515 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.149 (n=35)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 10.0 (IC base=+0.138)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.129 (n=114)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 6.0 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `2580.0317` → IC=+0.200 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2580.0317 (IC base=+0.101)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.159 (n=127)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 18.0 (IC base=+0.138)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `py_entrada` < 0.495 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `2495.3515` → IC=+0.169 (n=119)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2495.3515 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.149 (n=35)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 10.0 (IC base=+0.138)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `9.0` → IC=-0.185 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=43)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=98)

- **FILTRO** `libro_liquidez` < `2110.4161` → IC=-0.367 (n=28)

  - _Acción_: SKIP cuando `libro_liquidez` < 2110.4161
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=86)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=82)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `11321.3584` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 11321.3584
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=16)

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
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=427)

- **FILTRO** `hora_utc` < `7.0` → IC=-0.142 (n=121)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=391)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=88)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.285 (n=63)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=46)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_usd_total` < `35898.38` → IC=-0.139 (n=34)

  - _Acción_: SKIP cuando `liq_usd_total` < 35898.38
  - _Potencial_: sin este filtro IC_bueno=+0.139 (n=34)

- **PATRÓN** `liq_usd_total` > `92083.41` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `liq_usd_total` > 92083.41 (IC base=+0.000)

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
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=128)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.149 (n=35)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=109)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **PATRÓN** `liq_usd_total` > `9741.83` → IC=+0.128 (n=49)

  - _Acción_: Kelly boost +0.64€ cuando `liq_usd_total` > 9741.83 (IC base=+0.041)

### LIQUIDACIONES_5M#SOL#5min
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
- **FILTRO** `py_entrada` > `0.56` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=87)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.128 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=52)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=76)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=26)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=24)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2179.3878` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `libro_liquidez` < 2179.3878
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=125)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=407)

### MOMENTUM_IBS_15M#SOL#15min
- **FILTRO** `drift_20min_pct` |x|> `0.1848` → IC=-0.133 (n=96)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1848
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=189)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.46` → IC=-0.171 (n=795)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=2449)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.215 (n=759)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=2481)

- **FILTRO** `ibs_20min` > `0.272` → IC=-0.174 (n=809)

  - _Acción_: SKIP cuando `ibs_20min` > 0.272
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=2431)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.242 (n=118)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=354)

- **FILTRO** `ibs_20min` < `0.7263` → IC=-0.208 (n=118)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7263
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=354)

- **FILTRO** `ibs_20min` > `0.7424` → IC=-0.145 (n=139)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7424
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=418)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.227 (n=130)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=412)

- **FILTRO** `ballena_activa_n` > `80.0` → IC=-0.164 (n=135)

  - _Acción_: SKIP cuando `ballena_activa_n` > 80.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=407)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.186 (n=208)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=278)

- **FILTRO** `ibs_20min` < `0.7285` → IC=-0.207 (n=121)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7285
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=365)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.192 (n=183)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=361)

- **FILTRO** `ibs_20min` > `0.7585` → IC=-0.201 (n=135)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7585
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=409)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.129 (n=141)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=447)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.181 (n=155)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=419)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.150 (n=141)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=433)

### MOMENTUM_IBS_15M_BALLENA#SOL#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.225 (n=118)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=390)

- **FILTRO** `drift_20min_pct` |x|> `0.2833` → IC=-0.138 (n=172)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.2833
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=336)

- **FILTRO** `ibs_20min` > `0.2759` → IC=-0.172 (n=126)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2759
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=382)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.161 (n=125)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=383)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.225 (n=129)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=410)

- **FILTRO** `ibs_20min` < `0.756` → IC=-0.154 (n=134)

  - _Acción_: SKIP cuando `ibs_20min` < 0.756
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=405)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=524)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.285 (n=128)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=387)

- **FILTRO** `ibs_20min` > `0.28` → IC=-0.231 (n=128)

  - _Acción_: SKIP cuando `ibs_20min` > 0.28
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=387)

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

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `ibs_20min` < `1.0` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=19)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `libro_liquidez` < `15251.0076` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `libro_liquidez` < 15251.0076
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=11)

- **FILTRO** `drift_20min_pct` |x|> `0.1906` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1906
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=58)

### MOMENTUM_IBS_15M_FADE#XRP#15min
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
- **FILTRO** `hora_utc` < `7.0` → IC=-0.138 (n=1990)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=6038)

- **FILTRO** `py_entrada` < `0.36` → IC=-0.282 (n=1921)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=6107)

- **FILTRO** `ibs_7min` < `0.7368` → IC=-0.232 (n=1999)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7368
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=6029)

- **FILTRO** `ballena_activa_n` > `19.0` → IC=-0.174 (n=2726)

  - _Acción_: SKIP cuando `ballena_activa_n` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=5302)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.223 (n=2447)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=7349)

- **FILTRO** `ibs_7min` > `0.7153` → IC=-0.172 (n=2448)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7153
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=7348)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.161 (n=252)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=834)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.328 (n=266)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=820)

- **FILTRO** `ibs_7min` < `0.9819` → IC=-0.201 (n=716)

  - _Acción_: SKIP cuando `ibs_7min` < 0.9819
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=370)

- **FILTRO** `ballena_activa_n` > `16.0` → IC=-0.257 (n=269)

  - _Acción_: SKIP cuando `ballena_activa_n` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=817)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.226 (n=410)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=1262)

- **FILTRO** `drift_7min_pct` |x|> `0.1393` → IC=-0.157 (n=567)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1393
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=1105)

- **FILTRO** `ibs_7min` > `0.8364` → IC=-0.195 (n=417)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8364
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=1255)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.38` → IC=-0.227 (n=394)

  - _Acción_: SKIP cuando `py_entrada` < 0.38
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=1186)

- **FILTRO** `ibs_7min` < `0.8031` → IC=-0.163 (n=395)

  - _Acción_: SKIP cuando `ibs_7min` < 0.8031
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=1185)

- **FILTRO** `ballena_activa_n` > `155.0` → IC=-0.170 (n=392)

  - _Acción_: SKIP cuando `ballena_activa_n` > 155.0
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=1188)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.218 (n=391)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=-0.000 (n=1219)

- **FILTRO** `ballena_activa_n` > `129.0` → IC=-0.165 (n=401)

  - _Acción_: SKIP cuando `ballena_activa_n` > 129.0
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=1209)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.192 (n=274)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=865)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.313 (n=367)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=772)

- **FILTRO** `ibs_7min` < `0.2143` → IC=-0.280 (n=284)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2143
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=855)

- **FILTRO** `ballena_activa_n` > `16.0` → IC=-0.275 (n=283)

  - _Acción_: SKIP cuando `ballena_activa_n` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=856)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.260 (n=361)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=1347)

- **FILTRO** `ibs_7min` > `0.8164` → IC=-0.187 (n=426)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8164
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=1282)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.156 (n=405)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=955)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.261 (n=316)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=1044)

- **FILTRO** `ibs_7min` < `0.763` → IC=-0.187 (n=340)

  - _Acción_: SKIP cuando `ibs_7min` < 0.763
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=1020)

- **FILTRO** `ballena_activa_n` > `43.0` → IC=-0.216 (n=333)

  - _Acción_: SKIP cuando `ballena_activa_n` > 43.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=1027)

- **FILTRO** `hora_utc` > `18.0` → IC=-0.146 (n=289)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=1060)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.281 (n=327)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=1022)

- **FILTRO** `ibs_7min` > `0.1818` → IC=-0.163 (n=458)

  - _Acción_: SKIP cuando `ibs_7min` > 0.1818
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=891)

- **FILTRO** `ballena_activa_n` > `37.0` → IC=-0.205 (n=337)

  - _Acción_: SKIP cuando `ballena_activa_n` > 37.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=1012)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.234 (n=377)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=1152)

- **FILTRO** `ibs_7min` < `0.7761` → IC=-0.195 (n=382)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7761
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1147)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.192 (n=374)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1155)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.184 (n=447)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=1362)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.123 (n=425)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=909)

- **FILTRO** `py_entrada` < `0.39` → IC=-0.272 (n=327)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1007)

- **FILTRO** `ibs_7min` < `0.7544` → IC=-0.207 (n=333)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7544
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=1001)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.238 (n=319)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=1015)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.270 (n=332)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=1316)

- **FILTRO** `ibs_7min` > `0.83` → IC=-0.159 (n=411)

  - _Acción_: SKIP cuando `ibs_7min` > 0.83
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=1237)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=149)

- **FILTRO** `drift_7min_pct` |x|> `0.106` → IC=-0.139 (n=59)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.106
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=116)

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

- **PATRÓN** `delta_ratio` |x|> `0.4498` → IC=+0.184 (n=93)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.92€ cuando `delta_ratio` |x|> 0.4498 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.157 (n=97)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 15.0 (IC base=+0.127)

- **PATRÓN** `total_vol_5m` < `411.7048` → IC=+0.227 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 411.7048 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.128 (n=119)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `3589.6144` → IC=+0.176 (n=69)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 3589.6144 (IC base=+0.127)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.283 (n=44)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.144)

- **PATRÓN** `total_vol_5m` < `584.855` → IC=+0.167 (n=64)

  - _Acción_: Kelly boost +0.83€ cuando `total_vol_5m` < 584.855 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 52.0 (IC base=+0.144)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `libro_liquidez` > `2157.4034` → IC=+0.129 (n=33)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 2157.4034 (IC base=+0.080)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `hora_utc` < `8.0` → IC=+0.222 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=27)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `3221.1629` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 3221.1629 (IC base=+0.125)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.4028` → IC=+0.134 (n=39)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio` |x|> 0.4028 (IC base=+0.076)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.150 (n=38)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 15.0 (IC base=+0.076)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.076)

- **PATRÓN** `libro_liquidez` > `3436.4906` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 3436.4906 (IC base=+0.076)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` < `0.0084` → IC=-0.180 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0084
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=71)

- **FILTRO** `T_h` > `63.9866` → IC=-0.345 (n=95)

  - _Acción_: SKIP cuando `T_h` > 63.9866
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=32)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0069` → IC=-0.357 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0069
  - _Potencial_: sin este filtro IC_bueno=+0.239 (n=21)

- **FILTRO** `T_h` > `87.9981` → IC=-0.458 (n=22)

  - _Acción_: SKIP cuando `T_h` > 87.9981
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=24)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.239 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=-0.151)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0129` → IC=-0.184 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0129
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.006` → IC=-0.129 (n=68)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.006
  - _Potencial_: sin este filtro IC_bueno=+0.132 (n=36)

- **FILTRO** `T_h` > `144.6177` → IC=-0.352 (n=25)

  - _Acción_: SKIP cuando `T_h` > 144.6177
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=79)

- **FILTRO** `T_h` < `87.9947` → IC=-0.452 (n=19)

  - _Acción_: SKIP cuando `T_h` < 87.9947
  - _Potencial_: sin este filtro IC_bueno=-0.297 (n=62)

- **PATRÓN** `pct_vs_K` |x|≤ `1.4454` → IC=+0.176 (n=35)

  - _Acción_: Kelly boost +0.88€ cuando `pct_vs_K` |x|≤ 1.4454 (IC base=-0.038)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.005` → IC=-0.180 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `T_h` > `111.9957` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `T_h` > 111.9957
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=17)

- **FILTRO** `sigma_h` < `0.0055` → IC=-0.328 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0055
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

### STREAK_FADE_15M
- **FILTRO** `hora_utc` < `4.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=31)

- **FILTRO** `streak_estiramiento` > `0.4429` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4429
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=17)

- **FILTRO** `ballena_activa_n` > `58.0` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `ballena_activa_n` > 58.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=22)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=69)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.150 (n=38)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 44.0 (IC base=+0.021)

### STREAK_FADE_5M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.167 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=187)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `12.0` → IC=-0.265 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=49)

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
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=87)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=96)

- **FILTRO** `streak_estiramiento` > `0.6136` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.6136
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=53)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=97)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=134)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=286)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.123 (n=157)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.505 (IC base=+0.075)

- **PATRÓN** `streak_len` < `3.0` → IC=+0.144 (n=147)

  - _Acción_: Kelly boost +0.72€ cuando `streak_len` < 3.0 (IC base=+0.075)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=152)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=206)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.132 (n=150)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 14.0 (IC base=+0.070)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=1163)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=665)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=673)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.143 (n=127)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0029 (IC base=+0.113)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0676` → IC=+0.125 (n=382)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.62€ cuando `delta_ratio_macro` |x|> 0.0676 (IC base=+0.113)

- **PATRÓN** `ibs_15` > `0.5217` → IC=+0.202 (n=381)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5217 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` > `0.3854` → IC=+0.170 (n=101)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.3854 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.763` → IC=+0.250 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.763 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `7219.8643` → IC=+0.159 (n=127)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 7219.8643 (IC base=+0.113)

- **PATRÓN** `ballena_activa_n` < `86.0` → IC=+0.182 (n=42)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 86.0 (IC base=+0.113)

- **PATRÓN** `ibs_15` < `0.1151` → IC=+0.141 (n=430)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.71€ cuando `ibs_15` < 0.1151 (IC base=+0.027)

### UPDOWN_GBM#5min
- **FILTRO** `ibs_15` < `0.2222` → IC=-0.223 (n=117)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.2222
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=352)

- **FILTRO** `sigma_ewma_delta_pct` > `6.565` → IC=-0.209 (n=53)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.565
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=416)

### UPDOWN_GBM#60min
- **FILTRO** `sigma_ewma_delta_pct` < `7.975` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 7.975
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `ibs_15` < `0.3286` → IC=-0.167 (n=25)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.3286
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=53)

- **FILTRO** `dist_vwap_pct` < `0.4006` → IC=-0.224 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.4006
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=51)

- **FILTRO** `libro_liquidez` < `13834.2565` → IC=-0.278 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 13834.2565
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=53)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.156 (n=94)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0035 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.0853` → IC=+0.214 (n=47)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0853 (IC base=+0.146)

- **PATRÓN** `drift_15min` |x|≤ `0.4671` → IC=+0.176 (n=72)

  - _Acción_: Kelly boost +0.88€ cuando `drift_15min` |x|≤ 0.4671 (IC base=+0.146)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2616` → IC=+0.210 (n=36)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2616 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.173 (n=108)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 4.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.158 (n=109)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 16.0 (IC base=+0.146)

- **PATRÓN** `ibs_15` > `0.8714` → IC=+0.253 (n=71)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8714 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.3041` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.3041 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.5371` → IC=+0.161 (n=119)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.5371 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.029` → IC=+0.197 (n=64)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 7.029 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `12311.9188` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 12311.9188 (IC base=+0.146)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.182 (n=20)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0099 (IC base=-0.062)

### UPDOWN_GBM#BTC#5min
- **FILTRO** `sigma_h` < `0.0032` → IC=-0.184 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0032
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=35)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1001` → IC=-0.184 (n=17)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1001
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=35)

- **FILTRO** `hora_utc` < `4.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=36)

- **FILTRO** `ibs_15` < `0.1271` → IC=-0.289 (n=17)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1271
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=35)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `hora_utc` > `19.0` → IC=-0.132 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=76)

- **FILTRO** `ibs_15` < `0.8231` → IC=-0.167 (n=46)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8231
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=47)

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

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.129 (n=173)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0054 (IC base=+0.017)

### UPDOWN_GBM#ETH#5min
- **FILTRO** `hora_utc` < `3.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=67)

- **FILTRO** `ibs_15` < `0.4524` → IC=-0.125 (n=54)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.4524
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=29)

- **FILTRO** `dist_vwap_pct` > `0.1635` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1635
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=68)

- **FILTRO** `libro_liquidez` < `6390.4813` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `libro_liquidez` < 6390.4813
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=63)

- **FILTRO** `drift_15min` |x|> `0.559` → IC=-0.173 (n=102)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.559
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=309)

### UPDOWN_GBM#ETH#60min
- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=45)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.017)

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
- **FILTRO** `pct_spot_vs_ref` |x|> `0.012` → IC=-0.197 (n=31)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.012
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=35)

- **FILTRO** `ibs_15` < `0.225` → IC=-0.370 (n=21)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.225
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=45)

### UPDOWN_GBM#SOL#60min
- **FILTRO** `sigma_h` > `0.0127` → IC=-0.214 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0127
  - _Potencial_: sin este filtro IC_bueno=+0.090 (n=37)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.265 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=-0.017)

- **PATRÓN** `dist_vwap_pct` < `0.4088` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.4088 (IC base=-0.017)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `hora_utc` < `6.0` → IC=+0.167 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 6.0 (IC base=+0.096)

- **PATRÓN** `ibs_15` > `0.5556` → IC=+0.185 (n=90)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.92€ cuando `ibs_15` > 0.5556 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.3338` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3338 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.845` → IC=+0.235 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.845 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `2451.9374` → IC=+0.141 (n=101)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 2451.9374 (IC base=+0.096)

- **PATRÓN** `ibs_15` < `0.1304` → IC=+0.209 (n=108)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1304 (IC base=+0.052)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.005` → IC=+0.397 (n=66)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.310)

- **PATRÓN** `drift_60min` |x|≤ `0.058` → IC=+0.343 (n=49)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.058 (IC base=+0.310)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1528` → IC=+0.328 (n=97)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1528 (IC base=+0.310)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3802` → IC=+0.382 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3802 (IC base=+0.310)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.333 (n=136)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.310)

- **PATRÓN** `ibs_15` > `0.7314` → IC=+0.378 (n=145)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7314 (IC base=+0.310)

- **PATRÓN** `dist_vwap_pct` > `0.4531` → IC=+0.364 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4531 (IC base=+0.310)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.489` → IC=+0.340 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.489 (IC base=+0.310)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.311 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.310)

- **PATRÓN** `libro_liquidez` > `7959.8654` → IC=+0.382 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7959.8654 (IC base=+0.310)

- **PATRÓN** `ballena_activa_n` < `546.0` → IC=+0.380 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 546.0 (IC base=+0.310)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1971` → IC=+0.300 (n=73)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1971 (IC base=+0.286)

- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.400 (n=28)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0045 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.16` → IC=+0.313 (n=73)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.16 (IC base=+0.286)

- **PATRÓN** `drift_15min` |x|≤ `0.4155` → IC=+0.321 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4155 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.325 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.286)

- **PATRÓN** `ibs_15` > `0.7363` → IC=+0.324 (n=83)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7363 (IC base=+0.286)

- **PATRÓN** `dist_vwap_pct` > `0.4267` → IC=+0.385 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4267 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.871` → IC=+0.296 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.871 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.538` → IC=+0.287 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.538 (IC base=+0.286)

- **PATRÓN** `ballena_activa_n` < `480.0` → IC=+0.441 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 480.0 (IC base=+0.286)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.333 (n=28)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.335)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.403 (n=29)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.335)

- **PATRÓN** `drift_60min` |x|≤ `0.1189` → IC=+0.364 (n=42)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1189 (IC base=+0.335)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1322` → IC=+0.386 (n=42)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1322 (IC base=+0.335)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2773` → IC=+0.353 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2773 (IC base=+0.335)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.344 (n=43)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.335)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.336 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.335)

- **PATRÓN** `ibs_15` > `0.7053` → IC=+0.423 (n=63)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7053 (IC base=+0.335)

- **PATRÓN** `dist_vwap_pct` > `0.4682` → IC=+0.357 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4682 (IC base=+0.335)

- **PATRÓN** `dist_vwap_pct` < `0.156` → IC=+0.333 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.156 (IC base=+0.335)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.588` → IC=+0.403 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.588 (IC base=+0.335)

- **PATRÓN** `libro_liquidez` > `3271.2182` → IC=+0.364 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3271.2182 (IC base=+0.335)

- **PATRÓN** `ballena_activa_n` < `162.0` → IC=+0.342 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 162.0 (IC base=+0.335)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `ibs_15` < `0.4545` → IC=-0.270 (n=98)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.4545
  - _Potencial_: sin este filtro IC_bueno=+0.162 (n=294)

- **FILTRO** `sigma_ewma_delta_pct` > `17.262` → IC=-0.172 (n=340)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.262
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=2448)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.087` → IC=+0.130 (n=44)

  - _Acción_: Kelly boost +0.65€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.087 (IC base=-0.056)

- **PATRÓN** `ibs_15` > `0.4545` → IC=+0.162 (n=294)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.81€ cuando `ibs_15` > 0.4545 (IC base=-0.056)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1369` → IC=+0.268 (n=93)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1369 (IC base=-0.077)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.095` → IC=+0.364 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.095 (IC base=-0.077)

- **PATRÓN** `ibs_15` < `0.32` → IC=+0.345 (n=140)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.32 (IC base=-0.077)

- **PATRÓN** `dist_vwap_pct` < `0.1156` → IC=+0.273 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1156 (IC base=-0.077)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.296 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=-0.077)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0074` → IC=-0.235 (n=153)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0074
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=461)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.211 (n=202)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=412)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.247 (n=152)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=462)

- **FILTRO** `sigma_ewma_delta_pct` > `19.944` → IC=-0.261 (n=115)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.944
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=499)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.4477` → IC=-0.364 (n=42)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.4477
  - _Potencial_: sin este filtro IC_bueno=+0.182 (n=127)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=152)

- **PATRÓN** `drift_60min` |x|≤ `0.0629` → IC=+0.189 (n=43)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.0629 (IC base=+0.044)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3346` → IC=+0.227 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3346 (IC base=+0.044)

- **PATRÓN** `ibs_15` > `0.4477` → IC=+0.182 (n=127)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.91€ cuando `ibs_15` > 0.4477 (IC base=+0.044)

- **PATRÓN** `libro_liquidez` > `9861.0594` → IC=+0.217 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9861.0594 (IC base=+0.044)

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1045` → IC=+0.271 (n=59)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1045 (IC base=+0.254)

- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.300 (n=58)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0061 (IC base=+0.254)

- **PATRÓN** `drift_60min` |x|≤ `0.2361` → IC=+0.254 (n=59)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2361 (IC base=+0.254)

- **PATRÓN** `drift_15min` |x|≤ `0.4361` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4361 (IC base=+0.254)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0822` → IC=+0.275 (n=87)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0822 (IC base=+0.254)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.068` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.068 (IC base=+0.254)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.294 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.254)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.281 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.254)

- **PATRÓN** `ibs_15` < `0.3345` → IC=+0.344 (n=88)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3345 (IC base=+0.254)

- **PATRÓN** `dist_vwap_pct` > `0.1628` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1628 (IC base=+0.254)

- **PATRÓN** `dist_vwap_pct` < `0.3303` → IC=+0.258 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3303 (IC base=+0.254)

- **PATRÓN** `sigma_ewma_delta_pct` < `11.337` → IC=+0.285 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 11.337 (IC base=+0.254)

- **PATRÓN** `libro_liquidez` > `12249.9576` → IC=+0.309 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12249.9576 (IC base=+0.254)

- **PATRÓN** `ballena_activa_n` < `210.0` → IC=+0.283 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 210.0 (IC base=+0.254)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_15min` |x|> `0.5304` → IC=-0.147 (n=117)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.5304
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=119)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.096 (n=216)

- **FILTRO** `sigma_ewma_delta_pct` > `12.777` → IC=-0.144 (n=147)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 12.777
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=811)

- **PATRÓN** `ibs_15` > `0.8125` → IC=+0.206 (n=15)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8125 (IC base=-0.101)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `drift_15min` |x|> `1.0562` → IC=-0.210 (n=60)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.0562
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=184)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=49)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.135 (n=195)

- **FILTRO** `libro_liquidez` < `2584.1244` → IC=-0.195 (n=80)

  - _Acción_: SKIP cuando `libro_liquidez` < 2584.1244
  - _Potencial_: sin este filtro IC_bueno=-0.108 (n=164)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.302 (n=104)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0054 (IC base=+0.277)

- **PATRÓN** `drift_60min` |x|≤ `0.0527` → IC=+0.321 (n=76)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0527 (IC base=+0.277)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1881` → IC=+0.321 (n=104)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1881 (IC base=+0.277)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3802` → IC=+0.324 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3802 (IC base=+0.277)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.309 (n=234)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.277)

- **PATRÓN** `ibs_15` > `0.8606` → IC=+0.316 (n=204)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8606 (IC base=+0.277)

- **PATRÓN** `dist_vwap_pct` > `0.3` → IC=+0.353 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3 (IC base=+0.277)

- **PATRÓN** `sigma_ewma_delta_pct` > `24.523` → IC=+0.284 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 24.523 (IC base=+0.277)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.915` → IC=+0.277 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.915 (IC base=+0.277)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.276 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.277)

- **PATRÓN** `libro_liquidez` > `12288.7036` → IC=+0.346 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12288.7036 (IC base=+0.277)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.263 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.257)

- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.300 (n=43)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0057 (IC base=+0.257)

- **PATRÓN** `drift_60min` |x|≤ `0.1871` → IC=+0.279 (n=129)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1871 (IC base=+0.257)

- **PATRÓN** `drift_15min` |x|≤ `0.6649` → IC=+0.265 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.6649 (IC base=+0.257)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1425` → IC=+0.273 (n=86)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1425 (IC base=+0.257)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3906` → IC=+0.300 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3906 (IC base=+0.257)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.275 (n=118)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.257)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.256 (n=133)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.257)

- **PATRÓN** `ibs_15` > `0.9661` → IC=+0.320 (n=59)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9661 (IC base=+0.257)

- **PATRÓN** `dist_vwap_pct` > `0.3041` → IC=+0.347 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3041 (IC base=+0.257)

- **PATRÓN** `sigma_ewma_delta_pct` > `24.523` → IC=+0.306 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 24.523 (IC base=+0.257)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.866` → IC=+0.262 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.866 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `13561.3229` → IC=+0.322 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13561.3229 (IC base=+0.257)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.304 (n=100)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0073 (IC base=+0.298)

- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.308 (n=45)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.298)

- **PATRÓN** `drift_60min` |x|≤ `0.0603` → IC=+0.330 (n=45)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0603 (IC base=+0.298)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1881` → IC=+0.372 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1881 (IC base=+0.298)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.354 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=+0.298)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.375 (n=70)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.298)

- **PATRÓN** `ibs_15` > `0.864` → IC=+0.346 (n=89)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.864 (IC base=+0.298)

- **PATRÓN** `dist_vwap_pct` > `0.6569` → IC=+0.417 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6569 (IC base=+0.298)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.98` → IC=+0.300 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.98 (IC base=+0.298)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.664` → IC=+0.298 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.664 (IC base=+0.298)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.307 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.298)

- **PATRÓN** `libro_liquidez` > `10575.7678` → IC=+0.414 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10575.7678 (IC base=+0.298)

- **PATRÓN** `ballena_activa_n` < `263.0` → IC=+0.312 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 263.0 (IC base=+0.298)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1224` → IC=-0.260 (n=23)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1224
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=46)

- **FILTRO** `sigma_h` > `0.0068` → IC=-0.184 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=52)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1222` → IC=-0.184 (n=93)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1222
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=281)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.163 (n=93)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=281)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1533` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1533
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=11)

- **FILTRO** `ballena_activa_n` > `34.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `ballena_activa_n` > 34.0
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=49)

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
- **PATRÓN** `T_h` < `63.9936` → IC=+0.237 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 63.9936 (IC base=+0.083)

- **PATRÓN** `ratio` < `0.9722` → IC=+0.452 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9722 (IC base=+0.083)

- **PATRÓN** `T_h` > `146.1038` → IC=+0.441 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1038 (IC base=+0.342)

- **PATRÓN** `ratio` < `1.0177` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 1.0177 (IC base=+0.342)

- **PATRÓN** `ratio` > `1.0126` → IC=+0.174 (n=44)

  - _Acción_: Kelly boost +0.87€ cuando `ratio` > 1.0126 (IC base=+0.342)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` < `111.9957` → IC=+0.335 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 111.9957 (IC base=+0.262)

- **PATRÓN** `pct_dist` |x|≤ `0.6014` → IC=+0.284 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `pct_dist` |x|≤ 0.6014 (IC base=+0.262)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` < `82.5234` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 82.5234 (IC base=+0.123)

- **PATRÓN** `T_h` < `111.9838` → IC=+0.312 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 111.9838 (IC base=+0.302)

- **PATRÓN** `T_h` > `145.7785` → IC=+0.309 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7785 (IC base=+0.302)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1118` → IC=+0.454 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1118 (IC base=+0.415)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-SIGMA-SOL-60MIN**: `UPDOWN_GBM#SOL#60min` gana cuando sigma_h < 0.0058 (IC=+0.265 n=15). Implementar como filtro pre-predicción en shadow_predict.py.
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5217 sube el IC de +0.113 a +0.202 en UPDOWN_GBM#15min (n=381). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.8714 sube el IC de +0.146 a +0.253 en UPDOWN_GBM#BTC#15min (n=71). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.617 sube el IC de +0.080 a +0.237 en UPDOWN_GBM#ETH#15min (n=74). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.056 a +0.265 en UPDOWN_GBM#SOL#15min (n=32). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5556 sube el IC de +0.096 a +0.185 en UPDOWN_GBM#XRP#15min (n=90). Ya aplicado como kelly_boost=+0.92€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1304 sube el IC de +0.052 a +0.209 en UPDOWN_GBM#XRP#15min (n=108). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.4545 sube el IC de -0.056 a +0.162 en UPDOWN_GBM_15M_TARDIO (n=294). Ya aplicado como kelly_boost=+0.81€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.32 sube el IC de -0.077 a +0.345 en UPDOWN_GBM_15M_TARDIO (n=140). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.4477 sube el IC de +0.044 a +0.182 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=127). Ya aplicado como kelly_boost=+0.91€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3345 sube el IC de +0.254 a +0.344 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=88). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8125 sube el IC de -0.101 a +0.206 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=15). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8606 sube el IC de +0.277 a +0.316 en UPDOWN_GBM_IBS_ALTO (n=204). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.9661 sube el IC de +0.257 a +0.320 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=59). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.864 sube el IC de +0.298 a +0.346 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=89). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7314 sube el IC de +0.310 a +0.378 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=145). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.7363 sube el IC de +0.286 a +0.324 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=83). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7053 sube el IC de +0.335 a +0.423 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=63). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min` — IC=+0.348 n=31. Faltan ~9 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL` — IC=+0.348 n=31. Faltan ~9 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `ORDER_FLOW_5M#ETH#5min` — IC=+0.141 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.
- **LIVE-CANDIDATA**: `ORDER_FLOW_5M#ETH` — IC=+0.141 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 599 | +0.084 | +41.69€ | 1 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 599 | +0.084 | +41.69€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 355 | +0.108 | +30.68€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 355 | +0.108 | +30.68€ | 0 | 11 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 215 | +0.030 | +0.07€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 215 | +0.030 | +0.07€ | 7 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 29 | +0.177 | +10.93€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 29 | +0.177 | +10.93€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 6764 | -0.104 | -1026.07€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 681 | -0.091 | -126.98€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 6083 | -0.106 | -899.09€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 1162 | +0.000 | -170.97€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 1162 | +0.000 | -170.97€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 681 | -0.091 | -126.98€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 681 | -0.091 | -126.98€ | 2 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 359 | -0.137 | -154.67€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 359 | -0.137 | -154.67€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 725 | -0.137 | -38.80€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 725 | -0.137 | -38.80€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 2205 | -0.074 | -110.85€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 2205 | -0.074 | -110.85€ | 1 | 0 |
| 🚫 BALLENAS_TARDIAS#XRP | 1632 | -0.203 | -423.81€ | 0 | 0 |
| 🚫 BALLENAS_TARDIAS#XRP#5min | 1632 | -0.203 | -423.81€ | 1 | 0 |
| ✅ FAVORITO_CONFIRMADO | 31489 | +0.114 | -2025.56€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 5832 | +0.186 | -197.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 107 | -0.105 | -50.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 22382 | +0.095 | -1738.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 3168 | +0.120 | -39.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 3757 | +0.063 | -642.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 21 | -0.065 | +2.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#240min | 5 | -0.089 | -6.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 3731 | +0.064 | -637.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 6513 | +0.132 | -152.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 1644 | +0.196 | -91.78€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 3725 | +0.108 | -94.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 1102 | +0.130 | +56.38€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 3765 | +0.079 | -477.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 21 | +0.065 | +3.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 3743 | +0.079 | -478.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 6994 | +0.127 | -97.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 2123 | +0.168 | -12.96€ | 0 | 8 |
| 🚫 FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 3727 | +0.113 | -52.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 1132 | +0.101 | -23.97€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 6706 | +0.135 | -396.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 2006 | +0.204 | -97.19€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 46 | +0.000 | -9.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 3720 | +0.100 | -217.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 934 | +0.133 | -71.94€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 3754 | +0.105 | -259.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 17 | -0.022 | -0.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 3736 | +0.106 | -257.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 5785 | +0.172 | -463.00€ | 3 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 5785 | +0.172 | -463.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 1454 | +0.167 | -154.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 1454 | +0.167 | -154.31€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 112 | -0.123 | +2.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 112 | -0.123 | +2.06€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 1443 | +0.159 | -173.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 1443 | +0.159 | -173.61€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 1299 | +0.229 | -39.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 1299 | +0.229 | -39.02€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 1398 | +0.182 | -111.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 1398 | +0.182 | -111.87€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 294 | +0.446 | +3.35€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 294 | +0.446 | +3.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 111 | +0.447 | +2.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 111 | +0.447 | +2.72€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 109 | +0.428 | -1.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 109 | +0.428 | -1.55€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 71 | +0.445 | +2.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 71 | +0.445 | +2.04€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 16005 | +0.190 | -1427.36€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 16005 | +0.190 | -1427.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 2936 | +0.125 | -544.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 2936 | +0.125 | -544.42€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 2488 | +0.236 | -53.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 2488 | +0.236 | -53.30€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 2752 | +0.163 | -353.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 2752 | +0.163 | -353.30€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 2539 | +0.230 | -75.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 2539 | +0.230 | -75.68€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 2593 | +0.216 | -126.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 2593 | +0.216 | -126.32€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 2697 | +0.183 | -274.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 2697 | +0.183 | -274.33€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 5804 | +0.134 | +211.15€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 5804 | +0.134 | +211.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 2887 | +0.140 | +139.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 2887 | +0.140 | +139.56€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 2917 | +0.127 | +71.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 2917 | +0.127 | +71.59€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 760 | +0.300 | +6.60€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 760 | +0.300 | +6.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 326 | +0.281 | -8.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 326 | +0.281 | -8.47€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 358 | +0.303 | +10.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 358 | +0.303 | +10.01€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 76 | +0.359 | +5.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 76 | +0.359 | +5.06€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 322 | +0.414 | -14.14€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 322 | +0.414 | -14.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 145 | +0.412 | -6.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 145 | +0.412 | -6.77€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 146 | +0.419 | -6.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 146 | +0.419 | -6.05€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 31 | +0.348 | -1.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 31 | +0.348 | -1.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 228 | +0.104 | +1.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 70 | +0.139 | +4.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 158 | +0.087 | -3.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 8 | +0.120 | +4.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 8 | +0.120 | +4.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 186 | +0.101 | +0.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 28 | +0.167 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 158 | +0.087 | -3.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 34 | +0.056 | -3.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 34 | +0.056 | -3.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 6071 | +0.095 | -227.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 624 | +0.061 | -27.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 5447 | +0.099 | -199.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 4195 | +0.095 | -103.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 624 | +0.061 | -27.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 3571 | +0.101 | -75.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 1876 | +0.094 | -124.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 1876 | +0.094 | -124.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 427 | +0.288 | -23.87€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 427 | +0.288 | -23.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 427 | +0.288 | -23.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 427 | +0.288 | -23.87€ | 0 | 4 |
| ✅ GBM_LATE_15M | 7532 | +0.044 | +2404.27€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 7532 | +0.044 | +2404.27€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 1011 | +0.173 | +634.35€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 1011 | +0.173 | +634.35€ | 0 | 19 |
| ✅ GBM_LATE_15M#BTC | 1055 | +0.173 | +611.02€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 1055 | +0.173 | +611.02€ | 0 | 30 |
| ✅ GBM_LATE_15M#DOGE | 1014 | +0.188 | +692.96€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 1014 | +0.188 | +692.96€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 1231 | -0.044 | +37.86€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 1231 | -0.044 | +37.86€ | 2 | 9 |
| ✅ GBM_LATE_15M#SOL | 1403 | -0.043 | +141.68€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 1403 | -0.043 | +141.68€ | 5 | 3 |
| ✅ GBM_LATE_15M#XRP | 1818 | -0.056 | +286.40€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 1818 | -0.056 | +286.40€ | 4 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 8475 | +0.046 | +3294.37€ | 0 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 8475 | +0.046 | +3294.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 1298 | -0.021 | +627.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 1298 | -0.021 | +627.58€ | 2 | 3 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 1853 | -0.035 | +168.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 1853 | -0.035 | +168.98€ | 1 | 1 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 883 | +0.239 | +803.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 883 | +0.239 | +803.81€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 1424 | -0.043 | +10.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 1424 | -0.043 | +10.71€ | 8 | 3 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 1517 | -0.020 | +290.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 1517 | -0.020 | +290.12€ | 6 | 8 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 1500 | +0.242 | +1393.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 1500 | +0.242 | +1393.18€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 6099 | +0.170 | +4191.37€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 6099 | +0.170 | +4191.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 774 | +0.187 | +550.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 774 | +0.187 | +550.52€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 1036 | +0.164 | +699.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 1036 | +0.164 | +699.36€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 763 | +0.202 | +592.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 763 | +0.202 | +592.58€ | 0 | 18 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 1013 | +0.163 | +658.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 1013 | +0.163 | +658.27€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 1170 | +0.123 | +683.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 1170 | +0.123 | +683.23€ | 1 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 1343 | +0.191 | +1007.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 1343 | +0.191 | +1007.40€ | 0 | 22 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 1074 | +0.085 | +236.09€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 1074 | +0.085 | +236.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 56 | +0.086 | +14.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 56 | +0.086 | +14.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 317 | +0.118 | +115.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 317 | +0.118 | +115.33€ | 3 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 43 | +0.144 | +19.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 43 | +0.144 | +19.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 206 | +0.192 | +72.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 206 | +0.192 | +72.10€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 304 | -0.023 | -0.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 304 | -0.023 | -0.81€ | 4 | 3 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 148 | +0.060 | +14.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 148 | +0.060 | +14.84€ | 0 | 6 |
| ✅ GBM_LATE_15M_TARDIO | 7101 | +0.171 | +4753.58€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#15min | 7101 | +0.171 | +4753.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 965 | +0.195 | +710.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 965 | +0.195 | +710.59€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 1155 | +0.162 | +728.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 1155 | +0.162 | +728.19€ | 0 | 28 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 957 | +0.222 | +807.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 957 | +0.222 | +807.19€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 1090 | +0.149 | +632.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 1090 | +0.149 | +632.75€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 1282 | +0.111 | +651.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 1282 | +0.111 | +651.09€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 1652 | +0.194 | +1223.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 1652 | +0.194 | +1223.77€ | 0 | 24 |
| ✅ GBM_LATE_5M | 1574 | +0.136 | +769.18€ | 1 | 27 |
| ✅ GBM_LATE_5M#5min | 1574 | +0.136 | +769.18€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 79 | +0.191 | +48.83€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 79 | +0.191 | +48.83€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 626 | +0.137 | +347.72€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 626 | +0.137 | +347.72€ | 4 | 21 |
| ✅ GBM_LATE_5M#DOGE | 31 | +0.045 | +5.39€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 31 | +0.045 | +5.39€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH | 576 | +0.149 | +283.54€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 576 | +0.149 | +283.54€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 117 | -0.013 | +3.27€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 117 | -0.013 | +3.27€ | 2 | 1 |
| ✅ GBM_LATE_5M#XRP | 145 | +0.180 | +80.43€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 145 | +0.180 | +80.43€ | 0 | 0 |
| ✅ GBM_LATE_60M | 513 | -0.040 | +83.26€ | 5 | 8 |
| ✅ GBM_LATE_60M#60min | 513 | -0.040 | +83.26€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 176 | +0.000 | +4.29€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 176 | +0.000 | +4.29€ | 2 | 5 |
| ✅ GBM_LATE_60M#ETH | 184 | -0.011 | +56.06€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 184 | -0.011 | +56.06€ | 2 | 7 |
| ✅ GBM_LATE_60M#SOL | 153 | -0.119 | +22.91€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 153 | -0.119 | +22.91€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE | 193 | -0.305 | -34.48€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 193 | -0.305 | -34.48€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 76 | -0.256 | -7.36€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 76 | -0.256 | -7.36€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 65 | -0.351 | -19.05€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 65 | -0.351 | -19.05€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 52 | -0.296 | -8.07€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 52 | -0.296 | -8.07€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 328 | +0.036 | +2.61€ | 2 | 2 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 328 | +0.036 | +2.61€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 128 | +0.023 | +6.17€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 128 | +0.023 | +6.17€ | 2 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 83 | +0.065 | +0.92€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 83 | +0.065 | +0.92€ | 0 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 117 | +0.029 | -4.47€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 117 | +0.029 | -4.47€ | 2 | 5 |
| ✅ LATE_WINDOW_5MIN | 10 | +0.167 | +4.09€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 10 | +0.167 | +4.09€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 10 | +0.167 | +4.09€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 10 | +0.167 | +4.09€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 304 | +0.121 | +98.98€ | 0 | 6 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 304 | +0.121 | +98.98€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 304 | +0.121 | +98.98€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 304 | +0.121 | +98.98€ | 0 | 6 |
| ✅ LIQUIDACIONES_15M | 216 | -0.110 | -29.46€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 216 | -0.110 | -29.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 55 | -0.132 | -9.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 55 | -0.132 | -9.15€ | 2 | 0 |
| 🚫 LIQUIDACIONES_15M#DOGE | 22 | -0.208 | -5.32€ | 0 | 0 |
| 🚫 LIQUIDACIONES_15M#DOGE#15min | 22 | -0.208 | -5.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 44 | -0.043 | -3.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 44 | -0.043 | -3.91€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 44 | +0.000 | -0.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 44 | +0.000 | -0.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 46 | -0.167 | -8.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 46 | -0.167 | -8.95€ | 2 | 0 |
| ✅ LIQUIDACIONES_5M | 621 | -0.046 | -35.20€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 621 | -0.046 | -35.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 36 | -0.026 | -2.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 36 | -0.026 | -2.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 100 | -0.059 | -5.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 100 | -0.059 | -5.00€ | 1 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 67 | -0.094 | -7.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 67 | -0.094 | -7.35€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 173 | -0.014 | -3.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 173 | -0.014 | -3.20€ | 3 | 1 |
| ✅ LIQUIDACIONES_5M#SOL | 196 | -0.020 | -7.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 196 | -0.020 | -7.59€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 49 | -0.167 | -9.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 49 | -0.167 | -9.12€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M | 433 | -0.008 | -3.95€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 433 | -0.008 | -3.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 134 | -0.037 | -10.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 134 | -0.037 | -10.29€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 138 | -0.007 | +0.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 138 | -0.007 | +0.11€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 161 | +0.015 | +6.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 161 | +0.015 | +6.23€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 4418 | -0.003 | -77.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 4418 | -0.003 | -77.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 509 | -0.011 | -1.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 509 | -0.011 | -1.03€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 598 | +0.005 | -8.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 598 | +0.005 | -8.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 755 | -0.007 | -25.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 755 | -0.007 | -25.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 881 | +0.011 | +15.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 881 | +0.011 | +15.46€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 782 | -0.006 | -27.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 782 | -0.006 | -27.59€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 893 | -0.013 | -29.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 893 | -0.013 | -29.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 6484 | -0.034 | +193.01€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 6484 | -0.034 | +193.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 1029 | -0.023 | +134.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 1029 | -0.023 | +134.83€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 1158 | -0.035 | -27.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 1158 | -0.035 | -27.89€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 1030 | -0.042 | +97.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 1030 | -0.042 | +97.79€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 1162 | -0.034 | -32.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 1162 | -0.034 | -32.58€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 1051 | -0.040 | +30.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 1051 | -0.040 | +30.76€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 1054 | -0.029 | -9.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 1054 | -0.029 | -9.89€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 554 | -0.059 | -41.50€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 554 | -0.059 | -41.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 104 | -0.038 | -5.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 104 | -0.038 | -5.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 66 | -0.059 | -4.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 66 | -0.059 | -4.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 35 | -0.095 | -3.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 35 | -0.095 | -3.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 108 | -0.118 | -14.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 108 | -0.118 | -14.05€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 140 | -0.028 | -6.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 140 | -0.028 | -6.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 101 | -0.044 | -7.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 101 | -0.044 | -7.92€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3159 | +0.003 | -7.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3159 | +0.003 | -7.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 126 | -0.039 | -1.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 126 | -0.039 | -1.34€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 185 | +0.008 | -2.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 185 | +0.008 | -2.27€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 136 | +0.000 | -1.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 136 | +0.000 | -1.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1149 | +0.006 | +5.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1149 | +0.006 | +5.23€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1385 | +0.006 | -2.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1385 | +0.006 | -2.03€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 178 | -0.006 | -5.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 178 | -0.006 | -5.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 17824 | -0.073 | +285.27€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 17824 | -0.073 | +285.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 2758 | -0.090 | +305.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 2758 | -0.090 | +305.40€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 3190 | -0.059 | +5.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 3190 | -0.059 | +5.70€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 2847 | -0.083 | +15.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 2847 | -0.083 | +15.86€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 2709 | -0.098 | -199.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 2709 | -0.098 | -199.81€ | 8 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 3338 | -0.045 | +12.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 3338 | -0.045 | +12.98€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 2982 | -0.068 | +145.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 2982 | -0.068 | +145.15€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6012 | -0.010 | -119.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6012 | -0.010 | -119.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 992 | -0.018 | -21.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 992 | -0.018 | -21.41€ | 2 | 0 |
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
| ✅ ORDER_FLOW_5M | 409 | +0.099 | +104.40€ | 1 | 5 |
| ✅ ORDER_FLOW_5M#5min | 273 | +0.118 | +91.81€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 85 | +0.144 | +43.50€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 85 | +0.144 | +43.50€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#DOGE | 48 | +0.080 | +8.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 48 | +0.080 | +8.24€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 37 | +0.141 | +15.59€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 37 | +0.141 | +15.59€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL | 46 | +0.125 | +14.98€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 46 | +0.125 | +14.98€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 57 | +0.076 | +9.50€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 57 | +0.076 | +9.50€ | 0 | 4 |
| ✅ PRICE_TARGET_GBM | 259 | -0.159 | -20.62€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC | 115 | -0.235 | -33.14€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 100 | -0.265 | -32.41€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 15 | -0.022 | -0.74€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 99 | -0.134 | -3.00€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 80 | -0.146 | -5.97€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 19 | -0.068 | +2.97€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 45 | -0.011 | +15.52€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 38 | +0.000 | +14.95€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 7 | -0.019 | +0.57€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 218 | -0.177 | -23.43€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 41 | -0.058 | +2.80€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE | 185 | -0.174 | +23.59€ | 3 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 77 | -0.082 | +20.24€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 75 | -0.071 | +21.26€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 73 | -0.260 | -9.78€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 69 | -0.261 | -11.17€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 35 | -0.176 | +13.13€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 33 | -0.157 | +14.96€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#atexpiry | 177 | -0.165 | +25.06€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#reach | 8 | -0.120 | -1.47€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 58 | +0.283 | +10.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC | 17 | -0.022 | -2.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 17 | -0.022 | -2.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 16 | +0.222 | +1.47€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 16 | +0.222 | +1.47€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 25 | +0.463 | +12.41€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 25 | +0.463 | +12.41€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 58 | +0.283 | +10.94€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 138 | -0.021 | -12.25€ | 4 | 1 |
| ✅ STREAK_FADE_15M#15min | 138 | -0.021 | -12.25€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 57 | -0.009 | -6.41€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 57 | -0.009 | -6.41€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 9 | -0.021 | -0.61€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 9 | -0.021 | -0.61€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 13 | +0.065 | +2.23€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 13 | +0.065 | +2.23€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 59 | -0.057 | -7.46€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 59 | -0.057 | -7.46€ | 0 | 0 |
| ✅ STREAK_FADE_5M | 1070 | -0.022 | -51.78€ | 1 | 0 |
| ✅ STREAK_FADE_5M#5min | 1070 | -0.022 | -51.78€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 382 | -0.023 | -15.13€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 382 | -0.023 | -15.13€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 361 | -0.001 | -8.39€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 361 | -0.001 | -8.39€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 132 | -0.037 | -12.47€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 132 | -0.037 | -12.47€ | 2 | 0 |
| ✅ STREAK_FADE_5M#XRP | 195 | -0.048 | -15.79€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 195 | -0.048 | -15.79€ | 4 | 0 |
| ✅ STREAK_FADE_60M | 29 | -0.081 | -3.00€ | 0 | 0 |
| ✅ STREAK_FADE_60M#60min | 29 | -0.081 | -3.00€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 18 | -0.135 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 18 | -0.135 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 11 | +0.021 | +0.31€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 11 | +0.021 | +0.31€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 2132 | +0.034 | +55.34€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 2132 | +0.034 | +55.34€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 710 | +0.038 | +17.36€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 710 | +0.038 | +17.36€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 384 | +0.018 | +3.91€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 384 | +0.018 | +3.91€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 638 | +0.042 | +18.93€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 638 | +0.042 | +18.93€ | 1 | 2 |
| ✅ STREAK_MOM_5M#XRP | 400 | +0.027 | +15.13€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 400 | +0.027 | +15.13€ | 2 | 1 |
| ✅ STRUCT_NO_15M | 3073 | +0.009 | -26.13€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 3073 | +0.009 | -26.13€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 1182 | +0.009 | -10.83€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 1182 | +0.009 | -10.83€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 1194 | +0.018 | -0.01€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 1194 | +0.018 | -0.01€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 697 | -0.006 | -15.29€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 697 | -0.006 | -15.29€ | 2 | 0 |
| ✅ UPDOWN_GBM | 5954 | +0.007 | +157.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 2223 | +0.047 | +225.71€ | 0 | 8 |
| ✅ UPDOWN_GBM#240min | 250 | +0.020 | +3.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 3063 | -0.016 | -61.31€ | 2 | 0 |
| ✅ UPDOWN_GBM#60min | 371 | -0.017 | -10.58€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 195 | +0.094 | +38.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 179 | +0.119 | +42.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 7 | -0.019 | -0.50€ | 0 | 0 |
| 🚫 UPDOWN_GBM#BNB#5min | 9 | -0.102 | -2.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 1304 | +0.020 | +62.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 220 | +0.072 | +28.43€ | 3 | 12 |
| ✅ UPDOWN_GBM#BTC#240min | 72 | +0.081 | +7.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 873 | +0.013 | +30.51€ | 4 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 121 | -0.037 | -6.65€ | 2 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 766 | -0.004 | +0.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 122 | +0.105 | +29.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 9 | +0.021 | +0.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 635 | -0.026 | -29.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 1375 | +0.007 | +12.50€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 634 | +0.028 | +25.37€ | 1 | 6 |
| ✅ UPDOWN_GBM#ETH#240min | 72 | +0.081 | +5.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 494 | -0.024 | -18.35€ | 5 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 160 | +0.006 | -0.08€ | 0 | 1 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 1445 | -0.010 | -21.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 510 | +0.002 | -2.38€ | 1 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 58 | -0.033 | -4.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 775 | -0.010 | -11.04€ | 2 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 90 | -0.033 | -3.85€ | 1 | 2 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 867 | +0.009 | +66.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 558 | +0.062 | +102.68€ | 0 | 6 |
| ✅ UPDOWN_GBM#XRP#240min | 32 | -0.147 | -5.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 277 | -0.081 | -30.62€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 193 | +0.310 | +34.63€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 193 | +0.310 | +34.63€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 110 | +0.286 | +8.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 110 | +0.286 | +8.64€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 83 | +0.335 | +25.99€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 83 | +0.335 | +25.99€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 3768 | -0.072 | +850.74€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 3768 | -0.072 | +850.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 303 | -0.051 | +341.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 303 | -0.051 | +341.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 774 | -0.159 | -76.73€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 774 | -0.159 | -76.73€ | 4 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 77 | +0.070 | +14.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 77 | +0.070 | +14.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 285 | +0.131 | +133.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 285 | +0.131 | +133.53€ | 2 | 18 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 1194 | -0.069 | +221.36€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 1194 | -0.069 | +221.36€ | 3 | 1 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 1135 | -0.082 | +216.78€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 1135 | -0.082 | +216.78€ | 3 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 28 | +0.000 | -0.96€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 28 | +0.000 | -0.96€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 28 | +0.000 | -0.96€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 28 | +0.000 | -0.96€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 303 | +0.277 | +221.25€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 303 | +0.277 | +221.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 171 | +0.257 | +108.21€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 171 | +0.257 | +108.21€ | 0 | 13 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 132 | +0.298 | +113.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 132 | +0.298 | +113.04€ | 0 | 13 |
| ✅ UPDOWN_OU_5M | 443 | -0.075 | -40.77€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 443 | -0.075 | -40.77€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 258 | -0.038 | -20.57€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 258 | -0.038 | -20.57€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 55 | +0.026 | +3.45€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 55 | +0.026 | +3.45€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 30 | -0.188 | -6.21€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 30 | -0.188 | -6.21€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 33 | -0.157 | -4.86€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 33 | -0.157 | -4.86€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 36 | -0.184 | -5.77€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 36 | -0.184 | -5.77€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 31 | -0.197 | -6.80€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 31 | -0.197 | -6.80€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 1070 | +0.286 | +432.37€ | 0 | 5 |
| ✅ WEEKLY_PRICE#BTC | 319 | +0.201 | -2.54€ | 0 | 2 |
| ✅ WEEKLY_PRICE#ETH | 333 | +0.258 | +73.24€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 418 | +0.371 | +361.66€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.089) — sin ventaja clara. oversold(IBS<0.3): IC=+0.014 n=2109 | neutral: IC=+0.001 n=2244 | overbought(IBS>0.7): IC=+0.090 n=2331
  - _Datos_: n=6994 IC=+0.036 PNL=+621.80€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: (cache 610s) 17 celda(s) GATE OK de 2038 trackeadas

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.002 < 0.08 — monitorear
  - _Datos_: n=510 IC=+0.002 PNL=-2.38€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=333/15 IC=+0.258 PNL=+73.24€ | BTC: n=319/15 IC=+0.201 PNL=-2.54€ | SOL: n=418/15 IC=+0.371 PNL=+361.66€

**🟡 H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.076 n=95111 | tras_1loss IC=+0.044 n=74005 | tras_2loss IC=+0.008 n=33657/40 | gap=+0.069 (umbral 0.05)

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
  - _Estado_: 5892 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.128 n=41/60 | contraria IC=-0.022 n=21 | gap=+0.150 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=59, boost estimado=+0.019. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 46/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=160/40 IC=+0.006 PNL=-0.08€ | BTC#60min: n=121/40 IC=-0.037 PNL=-6.65€ | SOL#60min: n=90/40 IC=-0.033 PNL=-3.85€

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=-0.008 n=632 | contrario_BTC IC=-0.004 n=460/40 | gap=+0.004 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.135 > 0.08 con n=94 PNL=+25.23€
  - _Datos_: n=94 IC=+0.135 PNL=+25.23€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.332 > 0.1 con n=909 PNL=+438.10€
  - _Datos_: n=909 IC=+0.332 PNL=+438.10€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=53 IC=+0.045 PNL=+11.43€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=53 IC=+0.045 PNL=+11.43€

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
  - _Estado_: n=5712 IC=+0.004 PNL=+106.87€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=5712 IC=+0.004 PNL=+106.87€

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
  - _Estado_: n=307 IC=+0.002 PNL=-2.63€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=307 IC=+0.002 PNL=-2.63€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=64 IC=-0.106 PNL=-7.95€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=64 IC=-0.106 PNL=-7.95€

**🔴 H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.102 < -0.08 con n=101 PNL=-10.33€
  - _Datos_: n=101 IC=-0.102 PNL=-10.33€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.113 > 0.1 con n=507 PNL=+110.81€
  - _Datos_: n=507 IC=+0.113 PNL=+110.81€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=170 IC=+0.081 PNL=+40.43€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=170 IC=+0.081 PNL=+40.43€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=220 IC=+0.072 PNL=+28.43€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=220 IC=+0.072 PNL=+28.43€

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
  - _Estado_: n=1284 IC=+0.031 PNL=+80.99€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1284 IC=+0.031 PNL=+80.99€

**⏳ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: 20/30 ops en el filtro definido (IC actual=-0.182 PNL=-2.99€)
  - _Datos_: n=20 IC=-0.182 PNL=-2.99€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=71 IC=-0.007 PNL=+9.84€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=71 IC=-0.007 PNL=+9.84€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=80 IC=+0.024 PNL=+5.36€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=80 IC=+0.024 PNL=+5.36€

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
  - _Estado_: n=2108 IC=-0.015 PNL=-41.26€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2108 IC=-0.015 PNL=-41.26€

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
  - _Estado_: 10/30 ops en el filtro definido (IC actual=+0.167 PNL=+4.09€)
  - _Datos_: n=10 IC=+0.167 PNL=+4.09€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=1597 IC=+0.028 PNL=+109.29€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1597 IC=+0.028 PNL=+109.29€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=435 IC=+0.033 PNL=-0.11€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=435 IC=+0.033 PNL=-0.11€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.107 > 0.08 con n=87 PNL=+20.64€
  - _Datos_: n=87 IC=+0.107 PNL=+20.64€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.164 > 0.08 con n=111 PNL=+3.37€
  - _Datos_: n=111 IC=+0.164 PNL=+3.37€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.109 > 0.08 con n=113 PNL=+30.75€
  - _Datos_: n=113 IC=+0.109 PNL=+30.75€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=9438 IC=+0.105 PNL=+2794.09€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=9438 IC=+0.105 PNL=+2794.09€

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
  - _Estado_: n=798 IC=+0.028 PNL=+46.44€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=798 IC=+0.028 PNL=+46.44€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.130 > 0.02 con n=209 PNL=+64.44€
  - _Datos_: n=209 IC=+0.130 PNL=+64.44€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.440 > 0.1 con n=581 PNL=+479.95€
  - _Datos_: n=581 IC=+0.440 PNL=+479.95€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=1474 IC=+0.022 PNL=+72.17€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=1474 IC=+0.022 PNL=+72.17€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.166 > 0.1 con n=764 PNL=+275.96€
  - _Datos_: n=764 IC=+0.166 PNL=+275.96€

**⏳ H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: 40
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: 19/40 ops en el filtro definido (IC actual=-0.249 PNL=-4.23€)
  - _Datos_: n=19 IC=-0.249 PNL=-4.23€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=424 IC=+0.052 PNL=+61.36€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=424 IC=+0.052 PNL=+61.36€

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
  - _Estado_: n=62 IC=+0.047 PNL=-6.40€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=62 IC=+0.047 PNL=-6.40€

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
  - _Estado_: n=4219 IC=-0.139 PNL=+231.29€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4219 IC=-0.139 PNL=+231.29€

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
  - _Estado_: n=564 IC=+0.141 PNL=+229.25€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=564 IC=+0.141 PNL=+229.25€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.113 > 0.08 con n=507 PNL=+110.81€
  - _Datos_: n=507 IC=+0.113 PNL=+110.81€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=582 IC=+0.005 PNL=+5.35€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=582 IC=+0.005 PNL=+5.35€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.099 > 0.08 con n=576 PNL=+339.05€
  - _Datos_: n=576 IC=+0.099 PNL=+339.05€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.146 > 0.08 con n=142 PNL=+34.33€
  - _Datos_: n=142 IC=+0.146 PNL=+34.33€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.239 < -0.1 con n=462 PNL=-61.00€
  - _Datos_: n=462 IC=-0.239 PNL=-61.00€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=1124 IC=+0.134 PNL=+558.86€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=1124 IC=+0.134 PNL=+558.86€

**⏳ H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: 40
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: 23/40 ops en el filtro definido (IC actual=+0.060 PNL=+2.13€)
  - _Datos_: n=23 IC=+0.060 PNL=+2.13€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=634 IC=-0.025 PNL=+39.61€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=634 IC=-0.025 PNL=+39.61€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.181 > 0.08 con n=541 PNL=+323.46€
  - _Datos_: n=541 IC=+0.181 PNL=+323.46€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=962 IC=-0.048 PNL=+163.31€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=962 IC=-0.048 PNL=+163.31€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.122 > 0.08 con n=244 PNL=-28.51€
  - _Datos_: n=244 IC=+0.122 PNL=-28.51€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.242 > 0.08 con n=1372 PNL=-116.83€
  - _Datos_: n=1372 IC=+0.242 PNL=-116.83€

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
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.138 n=158) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=158 IC=+0.138 PNL=+55.82€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.347 > 0.08 con n=70 PNL=+49.38€
  - _Datos_: n=70 IC=+0.347 PNL=+49.38€

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
  - _Estado_: n=2936 IC=+0.125 PNL=-544.42€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=2936 IC=+0.125 PNL=-544.42€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.174 > 0.1 con n=41 PNL=+21.67€
  - _Datos_: n=41 IC=+0.174 PNL=+21.67€
