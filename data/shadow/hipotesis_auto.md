# Hipótesis automáticas — 2026-08-19 21:49 UTC
_Generado por shadow_postmortem.py sobre 80730 resoluciones (PNL=+8276.82€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.355` → IC=-0.143 (n=68)

  - _Acción_: SKIP cuando `py_entrada` < 0.355
  - _Potencial_: sin este filtro IC_bueno=+0.194 (n=155)

- **FILTRO** `banda_hit_calibrado` < `0.624` → IC=-0.193 (n=73)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.624
  - _Potencial_: sin este filtro IC_bueno=+0.230 (n=150)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.377 (n=63)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=215)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.250 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.091)

- **PATRÓN** `n_total_lado` > `75.0` → IC=+0.212 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 75.0 (IC base=+0.091)

- **PATRÓN** `banda_hit_calibrado` > `0.624` → IC=+0.230 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.624 (IC base=+0.091)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.136 (n=215)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.5 (IC base=+0.018)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `banda_hit_calibrado` < `0.6151` → IC=-0.200 (n=28)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6151
  - _Potencial_: sin este filtro IC_bueno=+0.209 (n=84)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.338 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.126 (n=113)

- **PATRÓN** `py_entrada` > `0.705` → IC=+0.257 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.705 (IC base=+0.105)

- **PATRÓN** `n_total_lado` > `94.0` → IC=+0.267 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 94.0 (IC base=+0.105)

- **PATRÓN** `banda_hit_calibrado` > `0.6151` → IC=+0.209 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6151 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.105)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.126 (n=113)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.495 (IC base=+0.013)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.278 (n=25)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=+0.182 (n=86)

- **FILTRO** `banda_hit_calibrado` < `0.6274` → IC=-0.210 (n=36)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6274
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=75)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=87)

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

- **PATRÓN** `py_entrada` > `0.33` → IC=+0.182 (n=86)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.33 (IC base=+0.075)

- **PATRÓN** `banda_hit_calibrado` > `0.6274` → IC=+0.214 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6274 (IC base=+0.075)

- **PATRÓN** `banda_z` > `8.673` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.673 (IC base=+0.075)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.140 (n=87)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.02 (IC base=+0.075)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.495 (IC base=-0.024)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `154.88` → IC=-0.252 (n=1073)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 154.88
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=3221)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `122.58` → IC=-0.396 (n=113)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 122.58
  - _Potencial_: sin este filtro IC_bueno=-0.130 (n=341)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` > `643.08` → IC=-0.254 (n=120)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` > 643.08
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=362)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `77.49` → IC=-0.468 (n=154)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 77.49
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=315)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `n_ballenas` < `4.0` → IC=-0.134 (n=249)

  - _Acción_: SKIP cuando `n_ballenas` < 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=825)

- **FILTRO** `restante_s_al_confirmar` < `182.68` → IC=-0.126 (n=354)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 182.68
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=720)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `146.79` → IC=-0.321 (n=210)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 146.79
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=632)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.7` → IC=+0.187 (n=2794)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.7 (IC base=+0.094)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.163 (n=1207)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.094)

- **PATRÓN** `libro_liquidez` > `2361.0666` → IC=+0.168 (n=1169)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2361.0666 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.147 (n=1808)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.154 (n=3444)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 12.0 (IC base=+0.144)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.274 (n=1596)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.186 (n=2120)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.02 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `4104.0126` → IC=+0.174 (n=870)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 4104.0126 (IC base=+0.144)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.207 (n=397)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.785` → IC=+0.363 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.785 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.198 (n=492)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.208 (n=337)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.298 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.191 (n=477)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.01 (IC base=+0.189)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.148 (n=413)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.159 (n=356)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 15.0 (IC base=+0.133)

- **PATRÓN** `py_entrada` > `0.555` → IC=+0.145 (n=438)

  - _Acción_: Kelly boost +0.73€ cuando `py_entrada` > 0.555 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `5033.4098` → IC=+0.165 (n=195)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 5033.4098 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.202 (n=166)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.139)

- **PATRÓN** `py_entrada` < `0.395` → IC=+0.209 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.395 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `5287.6073` → IC=+0.174 (n=216)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 5287.6073 (IC base=+0.139)

### FAVORITO_CONFIRMADO#ETH#15min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.132 (n=663)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 15.0 (IC base=+0.119)

- **PATRÓN** `py_entrada` > `0.7` → IC=+0.303 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.7 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.305 (n=291)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.294)

- **PATRÓN** `py_entrada` < `0.195` → IC=+0.408 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.195 (IC base=+0.294)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.295 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.294)

- **PATRÓN** `libro_liquidez` > `3445.7351` → IC=+0.342 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3445.7351 (IC base=+0.294)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.152 (n=291)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.174 (n=256)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 16.0 (IC base=+0.149)

- **PATRÓN** `py_entrada` > `0.655` → IC=+0.248 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.655 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.152 (n=349)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.02 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `2142.9957` → IC=+0.173 (n=279)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2142.9957 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `4388.7927` → IC=+0.157 (n=138)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 4388.7927 (IC base=+0.090)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.205 (n=198)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.190 (n=523)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.402 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.269 (n=128)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` < `0.215` → IC=+0.383 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.215 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.237 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `789.7295` → IC=+0.238 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 789.7295 (IC base=+0.221)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `19.0` → IC=+0.256 (n=76)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 19.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.193 (n=99)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 8.0 (IC base=+0.187)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.342 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.187)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.211 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.187)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.215 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.106)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.159 (n=259)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.02 (IC base=+0.106)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `11.0` → IC=-0.297 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=68)

- **FILTRO** `py_entrada` > `0.845` → IC=-0.379 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.845
  - _Potencial_: sin este filtro IC_bueno=-0.213 (n=99)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.187 (n=1028)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.191 (n=1251)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 7.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.199 (n=993)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.75 (IC base=+0.183)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.163 (n=496)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 11.0 (IC base=+0.156)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.162 (n=652)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 15.0 (IC base=+0.156)

- **PATRÓN** `py_entrada` < `0.75` → IC=+0.176 (n=748)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.75 (IC base=+0.156)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.333 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.311 (n=35)

- **FILTRO** `py_entrada` > `0.8` → IC=-0.389 (n=25)

  - _Acción_: SKIP cuando `py_entrada` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=26)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.417 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.326)

- **PATRÓN** `py_entrada` > `0.835` → IC=+0.370 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.835 (IC base=+0.326)

- **PATRÓN** `libro_liquidez` > `2916.5858` → IC=+0.343 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2916.5858 (IC base=+0.326)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.161 (n=708)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 6.0 (IC base=+0.158)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.177 (n=277)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 6.0 (IC base=+0.158)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.184 (n=248)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` < 0.7 (IC base=+0.158)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.162 (n=415)

  - _Acción_: Kelly boost +0.81€ cuando `py_entrada` > 0.73 (IC base=+0.158)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.228 (n=659)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.234 (n=562)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.322 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.225)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min
- **FILTRO** `hora_utc` > `12.0` → IC=-0.250 (n=38)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=40)

- **FILTRO** `py_entrada` > `0.845` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `py_entrada` > 0.845
  - _Potencial_: sin este filtro IC_bueno=-0.156 (n=59)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.207 (n=244)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.199 (n=300)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 7.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` < `0.72` → IC=+0.196 (n=548)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.72 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.439 (n=130)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.416)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.417 (n=131)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.416)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.435 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.416)

- **PATRÓN** `libro_liquidez` > `3424.0167` → IC=+0.425 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3424.0167 (IC base=+0.416)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.423 (n=50)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.415)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.439 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.415)

- **PATRÓN** `libro_liquidez` > `9189.8912` → IC=+0.450 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9189.8912 (IC base=+0.415)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.422 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.390)

- **PATRÓN** `py_entrada` < `0.91` → IC=+0.405 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.91 (IC base=+0.390)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.400 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.390)

- **PATRÓN** `libro_liquidez` > `2008.7424` → IC=+0.400 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2008.7424 (IC base=+0.390)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.441 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.418)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.406 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.418)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.200 (n=2055)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.187 (n=2109)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 6.0 (IC base=+0.187)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.219 (n=3975)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.187)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `py_entrada` > `0.71` → IC=+0.142 (n=685)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` > 0.71 (IC base=+0.098)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.289 (n=301)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.242)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.316 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.242)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.154 (n=486)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 15.0 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.171 (n=375)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 6.0 (IC base=+0.152)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.211 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.152)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.241 (n=789)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.230)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.287 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.230)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.241 (n=322)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.244 (n=764)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.238)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.260 (n=574)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.238)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.227 (n=346)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.229 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.182)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.218 (n=704)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.141)

- **PATRÓN** `restante_min` < `3.81` → IC=+0.157 (n=645)

  - _Acción_: Kelly boost +0.78€ cuando `restante_min` < 3.81 (IC base=+0.141)

- **PATRÓN** `restante_min` > `4.91` → IC=+0.201 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `restante_min` > 4.91 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.144 (n=2032)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.153 (n=1944)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 17.0 (IC base=+0.141)

- **PATRÓN** `lag_apertura_s` < `5.59` → IC=+0.204 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `lag_apertura_s` < 5.59 (IC base=+0.141)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.236 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.148)

- **PATRÓN** `restante_min` < `3.74` → IC=+0.161 (n=322)

  - _Acción_: Kelly boost +0.80€ cuando `restante_min` < 3.74 (IC base=+0.148)

- **PATRÓN** `restante_min` > `4.88` → IC=+0.197 (n=335)

  - _Acción_: Kelly boost +0.99€ cuando `restante_min` > 4.88 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.152 (n=1008)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.168 (n=679)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 12.0 (IC base=+0.148)

- **PATRÓN** `lag_apertura_s` < `7.36` → IC=+0.201 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `lag_apertura_s` < 7.36 (IC base=+0.148)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.199 (n=350)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.37 (IC base=+0.135)

- **PATRÓN** `restante_min` < `3.91` → IC=+0.150 (n=327)

  - _Acción_: Kelly boost +0.75€ cuando `restante_min` < 3.91 (IC base=+0.135)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.198 (n=329)

  - _Acción_: Kelly boost +0.99€ cuando `restante_min` > 4.95 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.136 (n=1024)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.148 (n=983)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 17.0 (IC base=+0.135)

- **PATRÓN** `lag_apertura_s` < `3.28` → IC=+0.198 (n=326)

  - _Acción_: Kelly boost +0.99€ cuando `lag_apertura_s` < 3.28 (IC base=+0.135)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.314 (n=386)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.303)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.313 (n=447)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.303)

- **PATRÓN** `py_entrada` > `0.825` → IC=+0.392 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.825 (IC base=+0.303)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.294 (n=163)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.274)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.280 (n=166)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.274)

- **PATRÓN** `py_entrada` < `0.725` → IC=+0.285 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.725 (IC base=+0.274)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.353 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.274)

- **PATRÓN** `libro_liquidez` > `5555.6091` → IC=+0.309 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5555.6091 (IC base=+0.274)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.326 (n=142)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.305)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.321 (n=205)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.305)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.400 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.305)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.305)

- **PATRÓN** `libro_liquidez` > `2566.6853` → IC=+0.341 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2566.6853 (IC base=+0.305)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.433 (n=43)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.381)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.417 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.381)

- **PATRÓN** `libro_liquidez` > `909.4383` → IC=+0.382 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 909.4383 (IC base=+0.381)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.412 (n=169)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.409)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.429 (n=182)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.409)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.416 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.409)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.427 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.409)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.406 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.409)

- **PATRÓN** `libro_liquidez` > `1933.7222` → IC=+0.423 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1933.7222 (IC base=+0.409)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.405 (n=82)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.406)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.440 (n=81)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.406)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.419 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.406)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.422 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.406)

- **PATRÓN** `libro_liquidez` > `5722.415` → IC=+0.431 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5722.415 (IC base=+0.406)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `9.0` → IC=+0.421 (n=74)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.411)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.409 (n=75)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.411)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.420 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.411)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.419 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.411)

- **PATRÓN** `libro_liquidez` > `1957.89` → IC=+0.434 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1957.89 (IC base=+0.411)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.291 (n=185)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.273)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.405 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.273)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.281 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.273)

- **PATRÓN** `libro_liquidez` > `1362.2836` → IC=+0.289 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1362.2836 (IC base=+0.273)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.291 (n=185)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.273)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.405 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.273)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.281 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.273)

- **PATRÓN** `libro_liquidez` > `1362.2836` → IC=+0.289 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1362.2836 (IC base=+0.273)

### GBM_LATE_15M
- **PATRÓN** `hora_utc` < `6.0` → IC=+0.132 (n=493)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 6.0 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.9802` → IC=+0.270 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9802 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `0.4633` → IC=+0.284 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4633 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.715` → IC=+0.231 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.715 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` < `1.3035` → IC=+0.243 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.3035 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` > `0.8707` → IC=+0.250 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8707 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` > `0.3247` → IC=+0.146 (n=111)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.3247 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` > `1.5272` → IC=+0.122 (n=789)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` > 1.5272 (IC base=+0.098)

- **PATRÓN** `ibs_20min` < `0.5588` → IC=+0.129 (n=2053)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.5588 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` < `0.1187` → IC=+0.144 (n=566)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1187 (IC base=+0.066)

- **PATRÓN** `volumen_regimen` < `1.2895` → IC=+0.135 (n=526)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.2895 (IC base=+0.066)

- **PATRÓN** `volumen_regimen` > `1.1115` → IC=+0.133 (n=238)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` > 1.1115 (IC base=+0.066)

- **PATRÓN** `volumen_pendiente_norm` > `0.328` → IC=+0.282 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.328 (IC base=+0.066)

- **PATRÓN** `volumen_spike_ratio` < `1.702` → IC=+0.239 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.702 (IC base=+0.066)

- **PATRÓN** `volumen_spike_ratio` > `2.8143` → IC=+0.218 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8143 (IC base=+0.066)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.281 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 49.0 (IC base=+0.066)

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
- **PATRÓN** `sigma_h` < `0.0018` → IC=+0.330 (n=45)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0018 (IC base=+0.266)

- **PATRÓN** `sigma_h` > `0.0038` → IC=+0.278 (n=43)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0038 (IC base=+0.266)

- **PATRÓN** `drift_60min` |x|≤ `0.0798` → IC=+0.276 (n=56)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0798 (IC base=+0.266)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.314 (n=116)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.266)

- **PATRÓN** `ibs_20min` > `0.6026` → IC=+0.291 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6026 (IC base=+0.266)

- **PATRÓN** `dist_vwap_pct` > `0.3229` → IC=+0.330 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3229 (IC base=+0.266)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.074` → IC=+0.312 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.074 (IC base=+0.266)

- **PATRÓN** `volumen_regimen` < `0.6564` → IC=+0.300 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6564 (IC base=+0.266)

- **PATRÓN** `volumen_regimen` > `0.7455` → IC=+0.267 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7455 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` < `0.1844` → IC=+0.304 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1844 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` < `2.7035` → IC=+0.309 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.7035 (IC base=+0.266)

- **PATRÓN** `libro_liquidez` > `13192.0581` → IC=+0.300 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13192.0581 (IC base=+0.266)

- **PATRÓN** `ballena_activa_n` < `441.0` → IC=+0.333 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 441.0 (IC base=+0.266)

- **PATRÓN** `sigma_h` < `0.002` → IC=+0.164 (n=117)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.002 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.1903` → IC=+0.177 (n=233)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.1903 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.167 (n=190)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 12.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.139 (n=275)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 18.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.4787` → IC=+0.193 (n=265)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.4787 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1465` → IC=+0.166 (n=276)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1465 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.3` → IC=+0.246 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.3 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.2713` → IC=+0.152 (n=265)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.2713 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `0.6787` → IC=+0.151 (n=236)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6787 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.0856` → IC=+0.234 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0856 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.606` → IC=+0.226 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.606 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `244.0` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 244.0 (IC base=+0.138)

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
- **FILTRO** `ibs_20min` > `0.8764` → IC=-0.180 (n=126)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8764
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=380)

- **PATRÓN** `ibs_20min` > `0.5742` → IC=+0.127 (n=81)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` > 0.5742 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.421` → IC=+0.159 (n=39)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 10.421 (IC base=+0.043)

### GBM_LATE_15M#SOL#15min
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
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0057 (IC base=+0.093)

- **PATRÓN** `hora_utc` > `23.0` → IC=+0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 23.0 (IC base=+0.093)

- **PATRÓN** `ibs_20min` > `0.3333` → IC=+0.207 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3333 (IC base=+0.093)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.093)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `sigma_ewma_delta_pct` > `6.284` → IC=-0.129 (n=122)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.284
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=652)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.08` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 8.08 (IC base=-0.036)

- **PATRÓN** `volumen_regimen` < `0.7863` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.7863 (IC base=-0.036)

- **PATRÓN** `dist_vwap_pct` < `0.1255` → IC=+0.231 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1255 (IC base=+0.015)

- **PATRÓN** `volumen_regimen` < `0.6973` → IC=+0.272 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6973 (IC base=+0.015)

- **PATRÓN** `volumen_regimen` > `1.1383` → IC=+0.224 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1383 (IC base=+0.015)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.155 (n=593)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0068 (IC base=+0.053)

- **PATRÓN** `ibs_20min` > `0.9461` → IC=+0.247 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9461 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` > `0.5183` → IC=+0.259 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5183 (IC base=+0.053)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.252` → IC=+0.131 (n=1082)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 2.252 (IC base=+0.053)

- **PATRÓN** `volumen_pendiente_norm` > `0.3396` → IC=+0.212 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3396 (IC base=+0.053)

- **PATRÓN** `volumen_spike_ratio` > `2.8554` → IC=+0.172 (n=333)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.8554 (IC base=+0.053)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.279 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.053)

- **PATRÓN** `ibs_20min` < `0.1024` → IC=+0.167 (n=904)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.1024 (IC base=+0.045)

- **PATRÓN** `dist_vwap_pct` > `0.1024` → IC=+0.202 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1024 (IC base=+0.045)

- **PATRÓN** `dist_vwap_pct` < `0.244` → IC=+0.187 (n=534)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.244 (IC base=+0.045)

- **PATRÓN** `volumen_regimen` < `0.7147` → IC=+0.188 (n=216)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.7147 (IC base=+0.045)

- **PATRÓN** `volumen_regimen` > `1.2553` → IC=+0.203 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2553 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` > `0.2058` → IC=+0.321 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2058 (IC base=+0.045)

- **PATRÓN** `volumen_spike_ratio` > `3.6434` → IC=+0.317 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.6434 (IC base=+0.045)

- **PATRÓN** `ballena_activa_n` < `61.0` → IC=+0.264 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 61.0 (IC base=+0.045)

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
- **FILTRO** `ibs_20min` < `0.0612` → IC=-0.167 (n=97)

  - _Acción_: SKIP cuando `ibs_20min` < 0.0612
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=292)

- **PATRÓN** `dist_vwap_pct` > `0.2954` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2954 (IC base=-0.022)

- **PATRÓN** `volumen_spike_ratio` < `1.696` → IC=+0.121 (n=27)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_spike_ratio` < 1.696 (IC base=-0.022)

- **PATRÓN** `volumen_regimen` < `0.6093` → IC=+0.179 (n=26)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.6093 (IC base=-0.015)

- **PATRÓN** `volumen_regimen` > `1.1074` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.1074 (IC base=-0.015)

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

- **PATRÓN** `volumen_pendiente_norm` < `0.3211` → IC=+0.402 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.3211 (IC base=+0.372)

- **PATRÓN** `volumen_pendiente_norm` > `0.1384` → IC=+0.389 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1384 (IC base=+0.372)

- **PATRÓN** `volumen_spike_ratio` < `2.9764` → IC=+0.444 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.9764 (IC base=+0.372)

- **PATRÓN** `libro_liquidez` > `1874.461` → IC=+0.415 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1874.461 (IC base=+0.372)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.6477` → IC=-0.132 (n=172)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6477
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=89)

- **FILTRO** `dist_vwap_pct` < `0.6073` → IC=-0.221 (n=41)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.6073
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=3)

- **FILTRO** `volumen_regimen` > `0.8629` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8629
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=23)

- **FILTRO** `libro_liquidez` < `8647.6879` → IC=-0.202 (n=65)

  - _Acción_: SKIP cuando `libro_liquidez` < 8647.6879
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=196)

- **FILTRO** `dist_vwap_pct` < `0.0665` → IC=-0.136 (n=53)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0665
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

- **FILTRO** `volumen_regimen` > `0.8463` → IC=-0.177 (n=29)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8463
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=31)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=727)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.45` → IC=-0.154 (n=160)

  - _Acción_: SKIP cuando `ibs_20min` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.148 (n=163)

- **FILTRO** `dist_vwap_pct` > `0.1358` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1358
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=41)

- **PATRÓN** `ibs_20min` > `0.45` → IC=+0.148 (n=163)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.45 (IC base=-0.002)

- **PATRÓN** `dist_vwap_pct` > `0.1881` → IC=+0.210 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1881 (IC base=-0.002)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.327 (n=108)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.0792` → IC=+0.164 (n=108)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.0792 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.194 (n=109)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 18.0 (IC base=+0.155)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.214 (n=117)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `0.9167` → IC=+0.242 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9167 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.4675` → IC=+0.289 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4675 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.172` → IC=+0.236 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.172 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` > `0.8296` → IC=+0.196 (n=215)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` > 0.8296 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.2623` → IC=+0.250 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2623 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `3.0896` → IC=+0.148 (n=268)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 3.0896 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `2.6132` → IC=+0.153 (n=122)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.6132 (IC base=+0.155)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.170 (n=328)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.01 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `2479.6478` → IC=+0.177 (n=289)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2479.6478 (IC base=+0.155)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.400 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=+0.155)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.280 (n=303)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.267)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.270 (n=307)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.267)

- **PATRÓN** `drift_60min` |x|≤ `0.3347` → IC=+0.269 (n=344)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3347 (IC base=+0.267)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.310 (n=177)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.267)

- **PATRÓN** `ibs_20min` < `0.2644` → IC=+0.343 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2644 (IC base=+0.267)

- **PATRÓN** `dist_vwap_pct` > `0.1611` → IC=+0.275 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1611 (IC base=+0.267)

- **PATRÓN** `dist_vwap_pct` < `0.2745` → IC=+0.269 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2745 (IC base=+0.267)

- **PATRÓN** `volumen_regimen` > `1.0811` → IC=+0.304 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0811 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` > `0.2787` → IC=+0.378 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2787 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` > `3.3154` → IC=+0.333 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.3154 (IC base=+0.267)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.211 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 49.0 (IC base=+0.267)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.158 (n=475)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0047 (IC base=+0.152)

- **PATRÓN** `sigma_h` > `0.0067` → IC=+0.216 (n=645)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0067 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=497)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.180 (n=529)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 6.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `0.916` → IC=+0.264 (n=948)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.916 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.5215` → IC=+0.246 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5215 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.966` → IC=+0.271 (n=687)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.966 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `1.224` → IC=+0.156 (n=774)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.224 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` > `0.63` → IC=+0.164 (n=774)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.63 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.1112` → IC=+0.175 (n=491)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1112 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `2.6369` → IC=+0.134 (n=1043)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.6369 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `1.5344` → IC=+0.133 (n=1185)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 1.5344 (IC base=+0.152)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.162 (n=1454)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.05 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `2526.7412` → IC=+0.191 (n=645)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2526.7412 (IC base=+0.152)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.218 (n=1348)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.2326` → IC=+0.214 (n=1187)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2326 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.252 (n=612)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` < `0.3798` → IC=+0.270 (n=1348)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3798 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` < `0.1604` → IC=+0.188 (n=1107)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.1604 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.494` → IC=+0.227 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.494 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` < `1.2366` → IC=+0.185 (n=1048)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 1.2366 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` > `0.8618` → IC=+0.190 (n=699)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 0.8618 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.2651` → IC=+0.249 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2651 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `1.6686` → IC=+0.222 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6686 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `3.0486` → IC=+0.233 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.0486 (IC base=+0.207)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.225 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 30.0 (IC base=+0.207)

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
- **PATRÓN** `sigma_h` < `0.0018` → IC=+0.287 (n=45)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0018 (IC base=+0.226)

- **PATRÓN** `sigma_h` > `0.0038` → IC=+0.333 (n=46)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0038 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.279 (n=134)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.6388` → IC=+0.285 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6388 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.3146` → IC=+0.338 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3146 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.971` → IC=+0.291 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.971 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` < `1.4274` → IC=+0.233 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.4274 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `0.9205` → IC=+0.258 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9205 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` < `0.1919` → IC=+0.228 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1919 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.3392` → IC=+0.342 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3392 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `1.5672` → IC=+0.312 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5672 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `11282.8623` → IC=+0.309 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11282.8623 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.201 (n=222)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.186)

- **PATRÓN** `sigma_h` > `0.002` → IC=+0.186 (n=227)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.002 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.1881` → IC=+0.210 (n=222)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1881 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.226 (n=177)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` < `0.301` → IC=+0.237 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.301 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` < `0.1273` → IC=+0.204 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1273 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.664` → IC=+0.275 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.664 (IC base=+0.186)

- **PATRÓN** `volumen_regimen` < `0.6283` → IC=+0.236 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6283 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` < `0.2596` → IC=+0.207 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2596 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.1352` → IC=+0.241 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1352 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` < `1.6134` → IC=+0.291 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6134 (IC base=+0.186)

- **PATRÓN** `libro_liquidez` > `12929.8594` → IC=+0.221 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12929.8594 (IC base=+0.186)

- **PATRÓN** `ballena_activa_n` < `223.0` → IC=+0.214 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 223.0 (IC base=+0.186)

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
- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.318 (n=42)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0022 (IC base=+0.265)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.267 (n=41)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.265)

- **PATRÓN** `drift_60min` |x|≤ `0.0952` → IC=+0.325 (n=55)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0952 (IC base=+0.265)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.284 (n=114)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.265)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.277 (n=110)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.265)

- **PATRÓN** `ibs_20min` > `0.5988` → IC=+0.316 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5988 (IC base=+0.265)

- **PATRÓN** `dist_vwap_pct` > `0.1317` → IC=+0.283 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1317 (IC base=+0.265)

- **PATRÓN** `dist_vwap_pct` < `0.2815` → IC=+0.280 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2815 (IC base=+0.265)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.328` → IC=+0.397 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.328 (IC base=+0.265)

- **PATRÓN** `volumen_regimen` > `0.6447` → IC=+0.292 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6447 (IC base=+0.265)

- **PATRÓN** `volumen_pendiente_norm` > `0.114` → IC=+0.309 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.114 (IC base=+0.265)

- **PATRÓN** `volumen_spike_ratio` > `2.0665` → IC=+0.285 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.0665 (IC base=+0.265)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.271 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.265)

- **PATRÓN** `libro_liquidez` > `10575.7678` → IC=+0.291 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10575.7678 (IC base=+0.265)

- **PATRÓN** `ballena_activa_n` < `230.0` → IC=+0.287 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 230.0 (IC base=+0.265)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.242 (n=165)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.1413` → IC=+0.195 (n=162)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.1413 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.216 (n=167)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` < `0.332` → IC=+0.251 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.332 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` < `0.1486` → IC=+0.185 (n=265)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.1486 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.358` → IC=+0.267 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.358 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `1.2367` → IC=+0.210 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2367 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` < `0.1688` → IC=+0.191 (n=137)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.1688 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` < `1.9099` → IC=+0.258 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9099 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `3214.3752` → IC=+0.183 (n=162)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 3214.3752 (IC base=+0.180)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **FILTRO** `ibs_20min` > `0.5455` → IC=-0.239 (n=86)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5455
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=264)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.209 (n=84)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.063)

- **PATRÓN** `ibs_20min` > `0.8667` → IC=+0.201 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8667 (IC base=+0.063)

- **PATRÓN** `dist_vwap_pct` > `0.5255` → IC=+0.173 (n=53)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.5255 (IC base=+0.063)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.386` → IC=+0.214 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.386 (IC base=+0.063)

- **PATRÓN** `libro_liquidez` > `2785.7274` → IC=+0.159 (n=83)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2785.7274 (IC base=+0.063)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 36.0 (IC base=+0.063)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.233 (n=88)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.235 (n=119)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.102)

- **PATRÓN** `ibs_20min` < `0.5455` → IC=+0.214 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5455 (IC base=+0.102)

- **PATRÓN** `dist_vwap_pct` > `0.5824` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.5824 (IC base=+0.102)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.906` → IC=+0.210 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.906 (IC base=+0.102)

- **PATRÓN** `volumen_regimen` > `0.862` → IC=+0.144 (n=175)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 0.862 (IC base=+0.102)

- **PATRÓN** `volumen_pendiente_norm` > `0.1169` → IC=+0.161 (n=60)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.1169 (IC base=+0.102)

- **PATRÓN** `volumen_spike_ratio` > `2.2667` → IC=+0.151 (n=61)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 2.2667 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `2136.6226` → IC=+0.169 (n=119)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2136.6226 (IC base=+0.102)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.294 (n=124)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.087` → IC=+0.167 (n=91)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.087 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=96)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.195 (n=103)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 6.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.253 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.3413` → IC=+0.230 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3413 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.39` → IC=+0.243 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.39 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `1.1814` → IC=+0.156 (n=271)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.1814 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` > `0.8308` → IC=+0.159 (n=180)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.8308 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.1987` → IC=+0.223 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1987 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.0973` → IC=+0.173 (n=157)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 2.0973 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.150 (n=275)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `2484.1984` → IC=+0.172 (n=242)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2484.1984 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.259 (n=293)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0073 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.285 (n=133)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.259 (n=143)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` < `0.1125` → IC=+0.343 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1125 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` > `0.3918` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3918 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.869` → IC=+0.266 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.869 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` > `1.0607` → IC=+0.306 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0607 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` > `0.2659` → IC=+0.326 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2659 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `3.3948` → IC=+0.289 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.3948 (IC base=+0.244)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.242 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.244)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.217 (n=118)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.055)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.127 (n=226)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` > 0.6 (IC base=+0.055)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.717` → IC=+0.262 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.717 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.184` → IC=+0.161 (n=54)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.184 (IC base=+0.055)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.295 (n=76)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.066)

- **PATRÓN** `drift_60min` |x|≤ `0.1672` → IC=+0.123 (n=152)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.62€ cuando `drift_60min` |x|≤ 0.1672 (IC base=+0.066)

- **PATRÓN** `ibs_20min` < `0.3846` → IC=+0.124 (n=200)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.3846 (IC base=+0.066)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.883` → IC=+0.223 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.883 (IC base=+0.066)

- **PATRÓN** `volumen_regimen` < `0.7501` → IC=+0.137 (n=100)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.7501 (IC base=+0.066)

- **PATRÓN** `volumen_spike_ratio` < `1.604` → IC=+0.183 (n=58)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.604 (IC base=+0.066)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 9.0 (IC base=+0.066)

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
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.203 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.191)

- **PATRÓN** `sigma_h` > `0.0027` → IC=+0.190 (n=27)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0027 (IC base=+0.191)

- **PATRÓN** `drift_60min` |x|≤ `0.2558` → IC=+0.230 (n=35)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2558 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.382 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` > `0.9442` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9442 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.738` → IC=+0.452 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.738 (IC base=+0.191)

- **PATRÓN** `volumen_regimen` < `0.9813` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9813 (IC base=+0.191)

- **PATRÓN** `volumen_regimen` > `1.0973` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0973 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` > `0.1778` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1778 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` < `2.3331` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3331 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` > `1.9173` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9173 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `3054.5848` → IC=+0.210 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3054.5848 (IC base=+0.191)

- **PATRÓN** `sigma_h` < `0.0025` → IC=+0.375 (n=22)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0025 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.2298` → IC=+0.217 (n=44)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2298 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` < `0.272` → IC=+0.152 (n=44)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.272 (IC base=+0.132)

- **PATRÓN** `ibs_20min` > `0.4281` → IC=+0.132 (n=17)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` > 0.4281 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.121` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.121 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `0.8238` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8238 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `10039.916` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10039.916 (IC base=+0.132)

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

- **FILTRO** `libro_liquidez` < `2083.1896` → IC=-0.174 (n=44)

  - _Acción_: SKIP cuando `libro_liquidez` < 2083.1896
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=45)

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

- **PATRÓN** `ibs_20min` > `0.6522` → IC=+0.143 (n=54)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.6522 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` > `0.2226` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.2226 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.99` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.99 (IC base=+0.085)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=54)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.085)

- **PATRÓN** `ibs_20min` < `0.0588` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0588 (IC base=+0.036)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.216 (n=554)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.159 (n=845)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 15.0 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.142 (n=602)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 6.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` > `0.9643` → IC=+0.292 (n=753)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9643 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` > `0.4917` → IC=+0.250 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4917 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.284` → IC=+0.235 (n=1103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.284 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.709` → IC=+0.127 (n=413)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 0.709 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` > `1.0814` → IC=+0.130 (n=425)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 1.0814 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.1827` → IC=+0.152 (n=398)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.1827 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `3.0803` → IC=+0.122 (n=1351)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 3.0803 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `1.6771` → IC=+0.133 (n=1206)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 1.6771 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.137 (n=1674)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.05 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `2904.8776` → IC=+0.176 (n=554)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2904.8776 (IC base=+0.130)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.230 (n=1347)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.208)

- **PATRÓN** `sigma_h` > `0.0039` → IC=+0.209 (n=1531)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0039 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.298` → IC=+0.213 (n=1531)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.298 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.231 (n=564)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` < `0.5222` → IC=+0.276 (n=1531)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5222 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` < `0.1593` → IC=+0.194 (n=973)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.1593 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.988` → IC=+0.243 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.988 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.488` → IC=+0.215 (n=1438)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.488 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` < `0.6112` → IC=+0.202 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6112 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` > `1.229` → IC=+0.196 (n=350)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` > 1.229 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.248` → IC=+0.247 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.248 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` < `1.6417` → IC=+0.239 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6417 (IC base=+0.208)

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
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.175 (n=121)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0028 (IC base=+0.154)

- **PATRÓN** `sigma_h` > `0.0038` → IC=+0.210 (n=60)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0038 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.297 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.3434` → IC=+0.262 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3434 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.2665` → IC=+0.312 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2665 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.391` → IC=+0.273 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.391 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `0.6608` → IC=+0.194 (n=60)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.6608 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` > `0.9228` → IC=+0.169 (n=119)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 0.9228 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` < `0.1588` → IC=+0.208 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1588 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `2.8883` → IC=+0.239 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.8883 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `7578.36` → IC=+0.252 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7578.36 (IC base=+0.154)

- **PATRÓN** `sigma_h` < `0.002` → IC=+0.207 (n=114)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.002 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.193` → IC=+0.193 (n=226)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.193 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.182 (n=259)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 6.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.173 (n=267)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 18.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` < `0.4244` → IC=+0.226 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4244 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` < `0.2327` → IC=+0.189 (n=284)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.2327 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.388` → IC=+0.248 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.388 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `0.6047` → IC=+0.216 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6047 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` > `0.8413` → IC=+0.188 (n=171)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` > 0.8413 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.1081` → IC=+0.308 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1081 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` < `1.5446` → IC=+0.297 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5446 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `5306.8576` → IC=+0.181 (n=230)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 5306.8576 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `273.0` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 273.0 (IC base=+0.172)

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
- **PATRÓN** `sigma_h` < `0.002` → IC=+0.177 (n=63)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.002 (IC base=+0.137)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.172 (n=62)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0046 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.0555` → IC=+0.172 (n=62)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.0555 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.199 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.3792` → IC=+0.243 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3792 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.4784` → IC=+0.273 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4784 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.344` → IC=+0.209 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.344 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.7651` → IC=+0.202 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7651 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `1.1314` → IC=+0.174 (n=84)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 1.1314 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2893` → IC=+0.328 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2893 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.9425` → IC=+0.260 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9425 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `7922.5621` → IC=+0.291 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7922.5621 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `192.0` → IC=+0.308 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 192.0 (IC base=+0.137)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.225 (n=129)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.2182` → IC=+0.159 (n=127)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2182 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.159 (n=130)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 6.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.153 (n=96)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 10.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.1814` → IC=+0.276 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1814 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.1545` → IC=+0.190 (n=56)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1545 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.492` → IC=+0.262 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.492 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.9536` → IC=+0.174 (n=127)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.9536 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` < `0.1747` → IC=+0.240 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1747 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.2263` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2263 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `1.8136` → IC=+0.242 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8136 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.5742` → IC=+0.232 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5742 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `6728.8499` → IC=+0.172 (n=65)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 6728.8499 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `114.0` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 114.0 (IC base=+0.148)

### GBM_LATE_15M_TARDIO#SOL#15min
- **FILTRO** `ibs_20min` < `0.5` → IC=-0.192 (n=76)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=254)

- **FILTRO** `ibs_20min` > `0.5` → IC=-0.164 (n=108)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.245 (n=233)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.233 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.030)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.923` → IC=+0.178 (n=144)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 2.923 (IC base=+0.030)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.155 (n=256)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0071 (IC base=+0.115)

- **PATRÓN** `drift_60min` |x|≤ `0.1852` → IC=+0.153 (n=171)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1852 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.182 (n=124)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.245 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` < `0.4821` → IC=+0.137 (n=257)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.4821 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.307` → IC=+0.176 (n=35)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 7.307 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.824` → IC=+0.135 (n=236)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 2.824 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `0.699` → IC=+0.170 (n=113)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.699 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` > `1.0749` → IC=+0.152 (n=116)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 1.0749 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` < `0.1693` → IC=+0.219 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1693 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` > `1.6525` → IC=+0.213 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6525 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `1442.4303` → IC=+0.186 (n=116)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 1442.4303 (IC base=+0.115)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.224 (n=150)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0065 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.0765` → IC=+0.212 (n=109)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0765 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.212 (n=109)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.181 (n=114)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 6.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.265 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.3757` → IC=+0.278 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3757 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.29` → IC=+0.223 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.29 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` > `0.6753` → IC=+0.157 (n=292)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.6753 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.1946` → IC=+0.208 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1946 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `2.7363` → IC=+0.144 (n=245)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.7363 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.7589` → IC=+0.152 (n=248)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.7589 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.160 (n=330)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `2491.4834` → IC=+0.157 (n=292)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2491.4834 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.289 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 36.0 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.300 (n=263)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.229)

- **PATRÓN** `drift_60min` |x|≤ `0.3308` → IC=+0.235 (n=394)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3308 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.278 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` < `0.4348` → IC=+0.293 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4348 (IC base=+0.229)

- **PATRÓN** `dist_vwap_pct` > `0.3918` → IC=+0.239 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3918 (IC base=+0.229)

- **PATRÓN** `dist_vwap_pct` < `0.1119` → IC=+0.240 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1119 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.567` → IC=+0.300 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.567 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.787` → IC=+0.237 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.787 (IC base=+0.229)

- **PATRÓN** `volumen_regimen` > `0.883` → IC=+0.255 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.883 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` > `0.264` → IC=+0.300 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.264 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` < `1.5061` → IC=+0.210 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5061 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` > `3.0855` → IC=+0.237 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.0855 (IC base=+0.229)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.163 (n=286)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.200 (n=38)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.042)

- **PATRÓN** `dist_vwap_pct` > `3.2039` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 3.2039 (IC base=+0.042)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.202 (n=199)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.2257` → IC=+0.183 (n=200)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.2257 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.163 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 15.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.244 (n=76)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.6417` → IC=+0.167 (n=226)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.6417 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` < `0.359` → IC=+0.156 (n=239)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.359 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.468` → IC=+0.148 (n=123)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 2.468 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.475` → IC=+0.148 (n=214)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 5.475 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.3682` → IC=+0.171 (n=226)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 1.3682 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` < `0.0968` → IC=+0.154 (n=189)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.0968 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.0752` → IC=+0.145 (n=122)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.0752 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.9176` → IC=+0.217 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9176 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.163 (n=286)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `7478.3992` → IC=+0.197 (n=226)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 7478.3992 (IC base=+0.144)

### GBM_LATE_5M#BTC#5min
- **FILTRO** `hora_utc` < `16.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.269 (n=11)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.187 (n=132)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0034 (IC base=+0.161)

- **PATRÓN** `sigma_h` > `0.0021` → IC=+0.164 (n=132)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0021 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.0879` → IC=+0.233 (n=58)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0879 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.160 (n=48)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 15.0 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.296 (n=47)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` < `0.2623` → IC=+0.211 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2623 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` < `0.1363` → IC=+0.174 (n=130)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.1363 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.868` → IC=+0.180 (n=123)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 5.868 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` < `1.2758` → IC=+0.172 (n=132)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 1.2758 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` > `0.6763` → IC=+0.192 (n=118)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` > 0.6763 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.1563` → IC=+0.250 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1563 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` < `1.827` → IC=+0.200 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.827 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `1.4126` → IC=+0.172 (n=132)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.4126 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `9861.9143` → IC=+0.179 (n=132)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 9861.9143 (IC base=+0.161)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `hora_utc` > `16.0` → IC=+0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.2171` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2171 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.504` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.504 (IC base=+0.141)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.278 (n=52)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.2126` → IC=+0.309 (n=40)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2126 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.273 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.300 (n=43)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.5506` → IC=+0.238 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5506 (IC base=+0.237)

- **PATRÓN** `ibs_20min` > `0.2593` → IC=+0.305 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2593 (IC base=+0.237)

- **PATRÓN** `dist_vwap_pct` > `0.4433` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4433 (IC base=+0.237)

- **PATRÓN** `dist_vwap_pct` < `0.1463` → IC=+0.241 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1463 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.688` → IC=+0.292 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.688 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.809` → IC=+0.239 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.809 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` < `1.5614` → IC=+0.303 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.5614 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.1318` → IC=+0.287 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1318 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `2.0669` → IC=+0.354 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0669 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `7445.2749` → IC=+0.271 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7445.2749 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 57.0 (IC base=+0.237)

### GBM_LATE_5M#SOL#5min
- **FILTRO** `sigma_ewma_delta_pct` < `1.963` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 1.963
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

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

- **PATRÓN** `dist_vwap_pct` < `0.2012` → IC=+0.231 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2012 (IC base=+0.100)

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
- **FILTRO** `drift_60min` |x|> `0.1252` → IC=-0.379 (n=31)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1252
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=62)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.423 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=58)

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

- **FILTRO** `sigma_ewma_delta_pct` > `4.524` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.524
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=26)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.6354` → IC=-0.462 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6354
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **FILTRO** `sigma_h` > `0.0018` → IC=-0.346 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0018
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `5.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=11)

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
- **PATRÓN** `hora_utc` > `13.0` → IC=+0.152 (n=21)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 13.0 (IC base=+0.114)

- **PATRÓN** `py_entrada` > `0.495` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `py_entrada` > 0.495 (IC base=+0.114)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.242 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.130)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.157 (n=33)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` < 0.505 (IC base=+0.130)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` > `13.0` → IC=+0.152 (n=21)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 13.0 (IC base=+0.114)

- **PATRÓN** `py_entrada` > `0.495` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `py_entrada` > 0.495 (IC base=+0.114)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.242 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.130)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.157 (n=33)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` < 0.505 (IC base=+0.130)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.123 (n=67)

- **FILTRO** `hora_utc` > `17.0` → IC=-0.333 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=84)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=84)

- **FILTRO** `libro_liquidez` < `1970.6128` → IC=-0.389 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 1970.6128
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=75)

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
- **FILTRO** `hora_utc` > `15.0` → IC=-0.152 (n=21)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.109 (n=44)

- **FILTRO** `libro_liquidez` < `3772.9492` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 3772.9492
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=49)

- **FILTRO** `ballena_activa_n` > `593.0` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `ballena_activa_n` > 593.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.157 (n=65)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.123 (n=59)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.157 (n=65)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `hora_utc` > `1.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=12)

- **FILTRO** `libro_liquidez` < `15405.8709` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `libro_liquidez` < 15405.8709
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `hora_utc` > `8.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9732` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9732
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=63)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.204 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=58)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `hora_utc` > `13.0` → IC=-0.125 (n=38)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=42)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `liq_usd_total` < `416.32` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `liq_usd_total` < 416.32
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=58)

- **FILTRO** `py_entrada` < `0.435` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.435
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=58)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2166.2663` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `libro_liquidez` < 2166.2663
  - _Potencial_: sin este filtro IC_bueno=+0.198 (n=41)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.065)

- **PATRÓN** `libro_liquidez` > `2166.2663` → IC=+0.198 (n=41)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2166.2663 (IC base=+0.065)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.155 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 4.0 (IC base=+0.104)

- **PATRÓN** `drift_20min_pct` |x|≤ `0.1328` → IC=+0.152 (n=67)

  - _Acción_: Kelly boost +0.76€ cuando `drift_20min_pct` |x|≤ 0.1328 (IC base=+0.104)

- **PATRÓN** `ibs_20min` > `0.0079` → IC=+0.138 (n=67)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 0.0079 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `2180.023` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2180.023 (IC base=+0.104)

### MOMENTUM_IBS_15M#BTC#15min
- **PATRÓN** `ibs_20min` < `0.9851` → IC=+0.157 (n=65)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.9851 (IC base=+0.068)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.250 (n=38)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.068)

- **PATRÓN** `drift_20min_pct` |x|≤ `0.0856` → IC=+0.121 (n=56)

  - _Acción_: Kelly boost +0.60€ cuando `drift_20min_pct` |x|≤ 0.0856 (IC base=+0.068)

- **PATRÓN** `libro_liquidez` > `20021.0576` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 20021.0576 (IC base=+0.068)

### MOMENTUM_IBS_15M#DOGE#15min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=41)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.090 (n=76)

- **PATRÓN** `hora_utc` < `2.0` → IC=+0.188 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 2.0 (IC base=+0.051)

- **PATRÓN** `drift_20min_pct` |x|≤ `0.053` → IC=+0.134 (n=39)

  - _Acción_: Kelly boost +0.67€ cuando `drift_20min_pct` |x|≤ 0.053 (IC base=+0.051)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.41` → IC=-0.207 (n=172)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=532)

- **FILTRO** `ibs_20min` < `0.7353` → IC=-0.157 (n=176)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7353
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=528)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.201 (n=185)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=573)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.204 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=82)

- **FILTRO** `py_entrada` < `0.38` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `py_entrada` < 0.38
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=82)

- **FILTRO** `ibs_20min` < `0.763` → IC=-0.203 (n=35)

  - _Acción_: SKIP cuando `ibs_20min` < 0.763
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=72)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.156 (n=59)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=66)

- **FILTRO** `ballena_activa_n` > `16.0` → IC=-0.141 (n=62)

  - _Acción_: SKIP cuando `ballena_activa_n` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=63)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.122 (n=88)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=46)

- **FILTRO** `py_entrada` > `0.54` → IC=-0.243 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.54
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=101)

- **FILTRO** `ibs_20min` > `0.1556` → IC=-0.202 (n=45)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1556
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=89)

- **FILTRO** `ballena_activa_n` > `64.0` → IC=-0.186 (n=33)

  - _Acción_: SKIP cuando `ballena_activa_n` > 64.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=101)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.146 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 7.0 (IC base=-0.029)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.154 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=87)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.140 (n=48)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=63)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.188 (n=30)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=93)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` > `0.505` → IC=-0.210 (n=29)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=110)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.192 (n=37)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 5.0 (IC base=-0.011)

### MOMENTUM_IBS_15M_BALLENA#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.173 (n=53)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=65)

- **FILTRO** `ibs_20min` < `0.7619` → IC=-0.175 (n=38)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7619
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=80)

- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.121 (n=56)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=62)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=94)

- **FILTRO** `ballena_activa_n` > `2.0` → IC=-0.152 (n=44)

  - _Acción_: SKIP cuando `ballena_activa_n` > 2.0
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=77)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.258 (n=31)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=94)

- **FILTRO** `ibs_20min` < `0.7457` → IC=-0.197 (n=31)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7457
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=94)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=110)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.306 (n=29)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=91)

- **FILTRO** `ibs_20min` > `0.2689` → IC=-0.274 (n=29)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2689
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=91)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `hora_utc` < `16.0` → IC=-0.300 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=125)

- **FILTRO** `hora_utc` > `19.0` → IC=-0.206 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=126)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=310)

### MOMENTUM_IBS_15M_FADE#BNB#15min
- **FILTRO** `libro_liquidez` < `2054.7357` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `libro_liquidez` < 2054.7357
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=49)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `ibs_20min` < `1.0` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `ibs_20min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=15)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `hora_utc` < `19.0` → IC=-0.300 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=13)

- **FILTRO** `drift_20min_pct` |x|> `0.2047` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.2047
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=52)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.273 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=46)

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

  - _Acción_: Kelly boost +0.90€ cuando `drift_7min_pct` |x|≤ 0.0658 (IC base=+0.044)

### MOMENTUM_IBS_5M_BALLENA
- **FILTRO** `hora_utc` < `10.0` → IC=-0.164 (n=602)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=1293)

- **FILTRO** `py_entrada` < `0.36` → IC=-0.264 (n=473)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=1422)

- **FILTRO** `ibs_7min` < `0.7377` → IC=-0.203 (n=473)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7377
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=1422)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.169 (n=641)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=1254)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.211 (n=559)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=1748)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.3` → IC=-0.239 (n=67)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=221)

- **FILTRO** `ibs_7min` < `0.9412` → IC=-0.167 (n=190)

  - _Acción_: SKIP cuando `ibs_7min` < 0.9412
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=98)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.136 (n=152)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=176)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.183 (n=159)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=169)

- **FILTRO** `drift_7min_pct` |x|> `0.1194` → IC=-0.171 (n=80)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1194
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=248)

- **FILTRO** `ibs_7min` > `0.8` → IC=-0.199 (n=81)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=247)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.219 (n=94)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=298)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.289 (n=88)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=304)

- **FILTRO** `ballena_activa_n` > `113.0` → IC=-0.157 (n=97)

  - _Acción_: SKIP cuando `ballena_activa_n` > 113.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=295)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.156 (n=91)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=324)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.191 (n=79)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=170)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.341 (n=61)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=188)

- **FILTRO** `ibs_7min` < `0.1984` → IC=-0.234 (n=62)

  - _Acción_: SKIP cuando `ibs_7min` < 0.1984
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=187)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.266 (n=62)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=187)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.258 (n=89)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=294)

- **FILTRO** `ibs_7min` > `0.8507` → IC=-0.149 (n=95)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8507
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=288)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.148 (n=86)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=263)

- **FILTRO** `py_entrada` < `0.39` → IC=-0.224 (n=85)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=264)

- **FILTRO** `ibs_7min` < `0.8464` → IC=-0.152 (n=87)

  - _Acción_: SKIP cuando `ibs_7min` < 0.8464
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=262)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.141 (n=168)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=181)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.140 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=271)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.174 (n=93)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=290)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `hora_utc` < `11.0` → IC=-0.149 (n=112)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=236)

- **FILTRO** `py_entrada` < `0.41` → IC=-0.250 (n=86)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=262)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.150 (n=161)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=187)

- **FILTRO** `ballena_activa_n` > `18.0` → IC=-0.233 (n=84)

  - _Acción_: SKIP cuando `ballena_activa_n` > 18.0
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=264)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.176 (n=100)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=305)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `10.0` → IC=-0.155 (n=85)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=184)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.232 (n=121)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=148)

- **FILTRO** `ibs_7min` < `0.7175` → IC=-0.326 (n=67)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7175
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=202)

- **FILTRO** `ballena_activa_n` > `17.0` → IC=-0.283 (n=67)

  - _Acción_: SKIP cuando `ballena_activa_n` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=202)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.242 (n=91)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=302)

- **FILTRO** `ibs_7min` > `0.8405` → IC=-0.180 (n=98)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8405
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=295)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=109)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=148)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=271)

### ORDER_FLOW_5M
- **FILTRO** `total_vol_5m` > `215.224` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `total_vol_5m` > 215.224
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `delta_ratio` |x|> `0.3994` → IC=+0.172 (n=181)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.86€ cuando `delta_ratio` |x|> 0.3994 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.192 (n=50)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 5.0 (IC base=+0.135)

- **PATRÓN** `total_vol_5m` < `550.649` → IC=+0.204 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 550.649 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.159 (n=39)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.135)

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

- **FILTRO** `sigma_h` > `0.0033` → IC=-0.262 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

### STREAK_FADE_15M
- **FILTRO** `hora_utc` < `8.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=11)

- **FILTRO** `ballena_activa_n` > `28.0` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `ballena_activa_n` > 28.0
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=23)

- **FILTRO** `streak_estiramiento` > `0.437` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.437
  - _Potencial_: sin este filtro IC_bueno=+0.389 (n=7)

### STREAK_FADE_5M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=94)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `ballena_activa_n` > `38.0` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `ballena_activa_n` > 38.0
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=20)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.184 (n=17)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` < 0.495 (IC base=+0.000)

- **PATRÓN** `libro_liquidez` > `3685.0104` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3685.0104 (IC base=+0.000)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `hora_utc` > `8.0` → IC=-0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=43)

- **FILTRO** `streak_estiramiento` > `0.644` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.644
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=49)

- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

### STREAK_MOM_5M
- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.123 (n=59)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=62)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `hora_utc` < `10.0` → IC=-0.214 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=48)

- **FILTRO** `hora_utc` > `9.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=49)

- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=37)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.140 (n=48)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 10.0 (IC base=+0.036)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.495 (IC base=+0.036)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `libro_liquidez` < `3496.0203` → IC=-0.133 (n=28)

  - _Acción_: SKIP cuando `libro_liquidez` < 3496.0203
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=28)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.141 (n=90)

- **PATRÓN** `hora_utc` > `20.0` → IC=+0.184 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 20.0 (IC base=-0.017)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.140 (n=84)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 16.0 (IC base=+0.098)

- **PATRÓN** `streak_len` < `3.0` → IC=+0.141 (n=90)

  - _Acción_: Kelly boost +0.71€ cuando `streak_len` < 3.0 (IC base=+0.098)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=753)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=442)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=450)

### UPDOWN_GBM#15min
- **FILTRO** `ibs_15` < `0.5` → IC=-0.170 (n=101)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.197 (n=335)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.158 (n=144)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0034 (IC base=+0.112)

- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.142 (n=149)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` > 0.0054 (IC base=+0.112)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0679` → IC=+0.129 (n=327)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.65€ cuando `delta_ratio_macro` |x|> 0.0679 (IC base=+0.112)

- **PATRÓN** `ibs_15` > `0.5` → IC=+0.197 (n=335)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.99€ cuando `ibs_15` > 0.5 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` > `0.3516` → IC=+0.199 (n=91)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.3516 (IC base=+0.112)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.26` → IC=+0.241 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.26 (IC base=+0.112)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.120 (n=335)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.01 (IC base=+0.112)

- **PATRÓN** `libro_liquidez` > `5349.0852` → IC=+0.167 (n=109)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 5349.0852 (IC base=+0.112)

- **PATRÓN** `ibs_15` < `0.125` → IC=+0.136 (n=256)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.68€ cuando `ibs_15` < 0.125 (IC base=+0.057)

### UPDOWN_GBM#5min
- **FILTRO** `hora_utc` > `8.0` → IC=-0.139 (n=120)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=147)

- **FILTRO** `ibs_15` < `0.1` → IC=-0.258 (n=64)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=203)

- **FILTRO** `sigma_ewma_delta_pct` > `5.1` → IC=-0.172 (n=65)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.1
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=202)

### UPDOWN_GBM#60min
- **FILTRO** `hora_utc` < `11.0` → IC=-0.269 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=150)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.0397` → IC=-0.227 (n=20)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0397
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=39)

- **FILTRO** `hora_utc` < `19.0` → IC=-0.200 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=17)

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.0887` → IC=+0.161 (n=54)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +0.80€ cuando `pct_spot_vs_ref` |x|≤ 0.0887 (IC base=+0.033)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.236` → IC=+0.136 (n=20)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 17.236 (IC base=+0.033)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.170 (n=98)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.03 (IC base=+0.033)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `sigma_h` < `0.0041` → IC=-0.227 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0041
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=20)

- **FILTRO** `dist_vwap_pct` < `0.5706` → IC=-0.210 (n=29)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.5706
  - _Potencial_: sin este filtro IC_bueno=+0.192 (n=11)

- **FILTRO** `libro_liquidez` < `12921.4246` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `libro_liquidez` < 12921.4246
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=20)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.154 (n=79)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0029 (IC base=+0.145)

- **PATRÓN** `sigma_h` > `0.0021` → IC=+0.158 (n=71)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0021 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.1916` → IC=+0.167 (n=79)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1916 (IC base=+0.145)

- **PATRÓN** `drift_15min` |x|≤ `0.4532` → IC=+0.173 (n=53)

  - _Acción_: Kelly boost +0.86€ cuando `drift_15min` |x|≤ 0.4532 (IC base=+0.145)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0763` → IC=+0.154 (n=79)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.77€ cuando `delta_ratio_macro` |x|> 0.0763 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=72)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.145)

- **PATRÓN** `ibs_15` > `0.9507` → IC=+0.263 (n=36)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9507 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.3682` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3682 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` < `0.1019` → IC=+0.223 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1019 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.367` → IC=+0.198 (n=51)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 7.367 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` < `23.789` → IC=+0.147 (n=83)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 23.789 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `8910.53` → IC=+0.237 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8910.53 (IC base=+0.145)

### UPDOWN_GBM#BTC#5min
- **FILTRO** `sigma_h` < `0.0035` → IC=-0.196 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0035
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=11)

- **FILTRO** `ibs_15` < `0.1827` → IC=-0.239 (n=21)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1827
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.0087` → IC=+0.167 (n=55)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +0.83€ cuando `pct_spot_vs_ref` |x|≤ 0.0087 (IC base=+0.092)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.135 (n=143)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0031 (IC base=+0.092)

- **PATRÓN** `drift_60min` |x|≤ `0.1243` → IC=+0.131 (n=109)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.1243 (IC base=+0.092)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.151 (n=81)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 5.0 (IC base=+0.092)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.035` → IC=+0.217 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.035 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `10527.9491` → IC=+0.153 (n=145)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 10527.9491 (IC base=+0.092)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.145 (n=136)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 25.0 (IC base=+0.092)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `ibs_15` < `0.616` → IC=-0.278 (n=16)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.616
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=51)

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1006` → IC=+0.196 (n=21)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +0.98€ cuando `pct_spot_vs_ref` |x|≤ 0.1006 (IC base=+0.024)

- **PATRÓN** `ibs_15` > `0.9253` → IC=+0.180 (n=23)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.90€ cuando `ibs_15` > 0.9253 (IC base=+0.024)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `ibs_15` < `0.5408` → IC=-0.235 (n=32)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5408
  - _Potencial_: sin este filtro IC_bueno=+0.294 (n=66)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.127 (n=65)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0039 (IC base=+0.120)

- **PATRÓN** `sigma_h` > `0.0028` → IC=+0.147 (n=66)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0028 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.1119` → IC=+0.135 (n=50)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.1119 (IC base=+0.120)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2385` → IC=+0.278 (n=25)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2385 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.141 (n=51)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 12.0 (IC base=+0.120)

- **PATRÓN** `ibs_15` > `0.5408` → IC=+0.294 (n=66)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5408 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.1005` → IC=+0.214 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1005 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.937` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.937 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `8808.1502` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 8808.1502 (IC base=+0.120)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.139 (n=59)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0033 (IC base=+0.115)

- **PATRÓN** `sigma_h` > `0.004` → IC=+0.159 (n=89)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.004 (IC base=+0.115)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1049` → IC=+0.136 (n=119)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio_macro` |x|> 0.1049 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.140 (n=98)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 12.0 (IC base=+0.115)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.135 (n=143)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 16.0 (IC base=+0.115)

- **PATRÓN** `ibs_15` < `0.2805` → IC=+0.164 (n=117)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.82€ cuando `ibs_15` < 0.2805 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` > `0.4562` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4562 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` < `22.914` → IC=+0.157 (n=132)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 22.914 (IC base=+0.115)

### UPDOWN_GBM#ETH#5min
- **FILTRO** `hora_utc` > `13.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=46)

- **FILTRO** `ibs_15` < `0.0049` → IC=-0.206 (n=15)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.0049
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=46)

- **FILTRO** `dist_vwap_pct` > `0.1641` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1641
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=46)

- **FILTRO** `sigma_ewma_delta_pct` > `5.626` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.626
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=37)

- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=111)

- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.175 (n=38)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0022 (IC base=+0.063)

- **PATRÓN** `drift_15min` |x|≤ `0.2984` → IC=+0.123 (n=75)

  - _Acción_: Kelly boost +0.62€ cuando `drift_15min` |x|≤ 0.2984 (IC base=+0.063)

### UPDOWN_GBM#ETH#60min
- **PATRÓN** `delta_ratio_macro` |x|> `0.1311` → IC=+0.125 (n=46)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.62€ cuando `delta_ratio_macro` |x|> 0.1311 (IC base=+0.037)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.175 (n=38)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.03 (IC base=+0.037)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `ibs_15` < `0.6` → IC=-0.177 (n=29)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.242 (n=29)

- **PATRÓN** `ibs_15` > `0.6` → IC=+0.242 (n=29)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6 (IC base=+0.033)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.764` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.764 (IC base=+0.033)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `ibs_15` < `0.5385` → IC=-0.242 (n=29)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5385
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=15)

- **FILTRO** `dist_vwap_pct` < `0.1891` → IC=-0.167 (n=31)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1891
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=13)

- **FILTRO** `libro_liquidez` < `3307.7933` → IC=-0.145 (n=29)

  - _Acción_: SKIP cuando `libro_liquidez` < 3307.7933
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=15)

- **PATRÓN** `sigma_h` > `0.008` → IC=+0.148 (n=52)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.008 (IC base=+0.065)

- **PATRÓN** `delta_ratio_macro` |x|> `0.3095` → IC=+0.175 (n=38)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio_macro` |x|> 0.3095 (IC base=+0.065)

- **PATRÓN** `ibs_15` < `0.0909` → IC=+0.191 (n=40)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.95€ cuando `ibs_15` < 0.0909 (IC base=+0.065)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=68)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.065)

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

- **PATRÓN** `delta_ratio_macro` |x|> `0.0962` → IC=+0.133 (n=156)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio_macro` |x|> 0.0962 (IC base=+0.060)

- **PATRÓN** `ibs_15` < `0.1379` → IC=+0.171 (n=77)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.85€ cuando `ibs_15` < 0.1379 (IC base=+0.060)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1958` → IC=+0.278 (n=79)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1958 (IC base=+0.269)

- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.309 (n=40)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0022 (IC base=+0.269)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.291 (n=41)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0033 (IC base=+0.269)

- **PATRÓN** `drift_60min` |x|≤ `0.1599` → IC=+0.290 (n=79)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1599 (IC base=+0.269)

- **PATRÓN** `drift_15min` |x|≤ `0.411` → IC=+0.286 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.411 (IC base=+0.269)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0706` → IC=+0.274 (n=91)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0706 (IC base=+0.269)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.348 (n=31)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.269)

- **PATRÓN** `ibs_15` > `0.7117` → IC=+0.326 (n=90)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7117 (IC base=+0.269)

- **PATRÓN** `dist_vwap_pct` > `0.3682` → IC=+0.382 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3682 (IC base=+0.269)

- **PATRÓN** `dist_vwap_pct` < `0.0842` → IC=+0.276 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0842 (IC base=+0.269)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.414` → IC=+0.304 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.414 (IC base=+0.269)

- **PATRÓN** `libro_liquidez` > `3271.2182` → IC=+0.281 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3271.2182 (IC base=+0.269)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.2061` → IC=+0.263 (n=57)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.2061 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.263 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.1514` → IC=+0.250 (n=50)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1514 (IC base=+0.227)

- **PATRÓN** `drift_15min` |x|≤ `0.4732` → IC=+0.275 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4732 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.263 (n=57)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.227)

- **PATRÓN** `ibs_15` < `0.9998` → IC=+0.233 (n=58)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.9998 (IC base=+0.227)

- **PATRÓN** `ibs_15` > `0.7314` → IC=+0.263 (n=57)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7314 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` > `0.3017` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3017 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.495` → IC=+0.237 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.495 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` < `15.813` → IC=+0.240 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 15.813 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `7219.8643` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7219.8643 (IC base=+0.227)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0035` → IC=+0.333 (n=22)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0035 (IC base=+0.326)

- **PATRÓN** `drift_60min` |x|≤ `0.1188` → IC=+0.380 (n=23)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1188 (IC base=+0.326)

- **PATRÓN** `delta_ratio_macro` |x|> `0.13` → IC=+0.417 (n=22)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.13 (IC base=+0.326)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.326)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.395 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.326)

- **PATRÓN** `ibs_15` > `0.854` → IC=+0.417 (n=22)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.854 (IC base=+0.326)

- **PATRÓN** `dist_vwap_pct` < `0.059` → IC=+0.357 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.059 (IC base=+0.326)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.588` → IC=+0.400 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.588 (IC base=+0.326)

- **PATRÓN** `libro_liquidez` > `2844.0749` → IC=+0.333 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2844.0749 (IC base=+0.326)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `ibs_15` < `0.419` → IC=-0.316 (n=85)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.419
  - _Potencial_: sin este filtro IC_bueno=+0.180 (n=173)

- **FILTRO** `ibs_15` > `0.531` → IC=-0.278 (n=16)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.531
  - _Potencial_: sin este filtro IC_bueno=+0.269 (n=50)

- **FILTRO** `sigma_ewma_delta_pct` > `12.848` → IC=-0.184 (n=267)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 12.848
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=1081)

- **PATRÓN** `ibs_15` > `0.419` → IC=+0.180 (n=173)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.90€ cuando `ibs_15` > 0.419 (IC base=-0.037)

- **PATRÓN** `ibs_15` < `0.531` → IC=+0.269 (n=50)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.531 (IC base=-0.072)

- **PATRÓN** `dist_vwap_pct` < `0.0929` → IC=+0.167 (n=46)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.0929 (IC base=-0.072)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.244 (n=88)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=203)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.239 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=224)

- **FILTRO** `libro_liquidez` < `14003.3235` → IC=-0.218 (n=218)

  - _Acción_: SKIP cuando `libro_liquidez` < 14003.3235
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=73)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.133 (n=58)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.003 (IC base=+0.062)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `drift_60min` |x|> `0.1985` → IC=-0.231 (n=24)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1985
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=73)

- **FILTRO** `ibs_15` < `0.563` → IC=-0.340 (n=48)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.563
  - _Potencial_: sin este filtro IC_bueno=+0.226 (n=49)

- **PATRÓN** `ibs_15` > `0.563` → IC=+0.226 (n=49)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.563 (IC base=-0.056)

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1184` → IC=+0.206 (n=32)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1184 (IC base=+0.160)

- **PATRÓN** `sigma_h` > `0.0038` → IC=+0.186 (n=33)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0038 (IC base=+0.160)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1167` → IC=+0.157 (n=33)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.79€ cuando `delta_ratio_macro` |x|> 0.1167 (IC base=+0.160)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.204 (n=25)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.160)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.176 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 14.0 (IC base=+0.160)

- **PATRÓN** `ibs_15` < `0.428` → IC=+0.324 (n=32)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.428 (IC base=+0.160)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.166` → IC=+0.188 (n=30)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 8.166 (IC base=+0.160)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0065` → IC=-0.184 (n=36)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0065
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=110)

- **FILTRO** `sigma_ewma_delta_pct` > `13.898` → IC=-0.208 (n=70)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 13.898
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=413)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.509` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 9.509 (IC base=-0.027)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.160 (n=98)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=63)

- **FILTRO** `libro_liquidez` < `2491.4834` → IC=-0.214 (n=40)

  - _Acción_: SKIP cuando `libro_liquidez` < 2491.4834
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=121)

- **FILTRO** `sigma_ewma_delta_pct` > `13.199` → IC=-0.219 (n=55)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 13.199
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=388)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.317 (n=58)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0033 (IC base=+0.273)

- **PATRÓN** `drift_60min` |x|≤ `0.1819` → IC=+0.285 (n=128)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1819 (IC base=+0.273)

- **PATRÓN** `drift_15min` |x|≤ `0.6305` → IC=+0.283 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.6305 (IC base=+0.273)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1879` → IC=+0.333 (n=58)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1879 (IC base=+0.273)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.306 (n=137)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.273)

- **PATRÓN** `ibs_15` > `0.9362` → IC=+0.351 (n=85)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9362 (IC base=+0.273)

- **PATRÓN** `dist_vwap_pct` > `0.3842` → IC=+0.348 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3842 (IC base=+0.273)

- **PATRÓN** `dist_vwap_pct` < `0.0774` → IC=+0.308 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0774 (IC base=+0.273)

- **PATRÓN** `sigma_ewma_delta_pct` < `20.742` → IC=+0.279 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 20.742 (IC base=+0.273)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.271 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.273)

- **PATRÓN** `libro_liquidez` > `8878.5012` → IC=+0.283 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8878.5012 (IC base=+0.273)

- **PATRÓN** `ballena_activa_n` < `304.0` → IC=+0.333 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 304.0 (IC base=+0.273)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1974` → IC=+0.269 (n=76)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1974 (IC base=+0.248)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.256 (n=76)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.248)

- **PATRÓN** `sigma_h` > `0.0022` → IC=+0.257 (n=68)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0022 (IC base=+0.248)

- **PATRÓN** `drift_60min` |x|≤ `0.1826` → IC=+0.282 (n=76)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1826 (IC base=+0.248)

- **PATRÓN** `drift_15min` |x|≤ `0.6581` → IC=+0.269 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.6581 (IC base=+0.248)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0919` → IC=+0.271 (n=68)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0919 (IC base=+0.248)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.283 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.248)

- **PATRÓN** `ibs_15` > `0.8877` → IC=+0.300 (n=68)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8877 (IC base=+0.248)

- **PATRÓN** `dist_vwap_pct` > `0.3582` → IC=+0.389 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3582 (IC base=+0.248)

- **PATRÓN** `dist_vwap_pct` < `0.0845` → IC=+0.300 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0845 (IC base=+0.248)

- **PATRÓN** `sigma_ewma_delta_pct` > `27.622` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 27.622 (IC base=+0.248)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.798` → IC=+0.250 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.798 (IC base=+0.248)

- **PATRÓN** `libro_liquidez` > `6079.7902` → IC=+0.255 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6079.7902 (IC base=+0.248)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` > `0.0028` → IC=+0.337 (n=47)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0028 (IC base=+0.303)

- **PATRÓN** `drift_15min` |x|≤ `0.3985` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3985 (IC base=+0.303)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1796` → IC=+0.423 (n=24)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1796 (IC base=+0.303)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.337 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.303)

- **PATRÓN** `ibs_15` > `0.9731` → IC=+0.423 (n=24)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9731 (IC base=+0.303)

- **PATRÓN** `dist_vwap_pct` > `0.2815` → IC=+0.328 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2815 (IC base=+0.303)

- **PATRÓN** `dist_vwap_pct` < `0.0769` → IC=+0.333 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0769 (IC base=+0.303)

- **PATRÓN** `sigma_ewma_delta_pct` < `19.88` → IC=+0.336 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 19.88 (IC base=+0.303)

- **PATRÓN** `libro_liquidez` > `10575.7678` → IC=+0.350 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10575.7678 (IC base=+0.303)

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

- **H-IBS-UPDOWN_GBM#SOL#5min**: dentro de BUY_NO, IBS < 0.0909 sube el IC de +0.065 a +0.191 en UPDOWN_GBM#SOL#5min (n=40). Ya aplicado como kelly_boost=+0.95€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5 sube el IC de +0.112 a +0.197 en UPDOWN_GBM#15min (n=335). Ya aplicado como kelly_boost=+0.99€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.9507 sube el IC de +0.145 a +0.263 en UPDOWN_GBM#BTC#15min (n=36). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5408 sube el IC de +0.120 a +0.294 en UPDOWN_GBM#ETH#15min (n=66). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_NO, IBS < 0.2805 sube el IC de +0.115 a +0.164 en UPDOWN_GBM#ETH#15min (n=117). Ya aplicado como kelly_boost=+0.82€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.033 a +0.242 en UPDOWN_GBM#SOL#15min (n=29). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.55 sube el IC de +0.085 a +0.182 en UPDOWN_GBM#XRP#15min (n=86). Ya aplicado como kelly_boost=+0.91€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1379 sube el IC de +0.060 a +0.171 en UPDOWN_GBM#XRP#15min (n=77). Ya aplicado como kelly_boost=+0.85€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#60min**: dentro de BUY_YES, IBS > 0.9253 sube el IC de +0.024 a +0.180 en UPDOWN_GBM#BTC#60min (n=23). Ya aplicado como kelly_boost=+0.90€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.419 sube el IC de -0.037 a +0.180 en UPDOWN_GBM_15M_TARDIO (n=173). Ya aplicado como kelly_boost=+0.90€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.531 sube el IC de -0.072 a +0.269 en UPDOWN_GBM_15M_TARDIO (n=50). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.563 sube el IC de -0.056 a +0.226 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=49). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.428 sube el IC de +0.160 a +0.324 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=32). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.9362 sube el IC de +0.273 a +0.351 en UPDOWN_GBM_IBS_ALTO (n=85). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8877 sube el IC de +0.248 a +0.300 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=68). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.9731 sube el IC de +0.303 a +0.423 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=24). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7117 sube el IC de +0.269 a +0.326 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=90). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS < 0.9998 sube el IC de +0.227 a +0.233 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=58). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.7314 sube el IC de +0.227 a +0.263 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=57). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.854 sube el IC de +0.326 a +0.417 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=22). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `ORDER_FLOW_5M#SOL#5min` — IC=+0.088 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `ORDER_FLOW_5M#SOL` — IC=+0.088 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `ORDER_FLOW_5M#BNB#5min` — IC=+0.200 n=38. Faltan ~2 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `ORDER_FLOW_5M#BNB` — IC=+0.200 n=38. Faltan ~2 resoluciones para umbral n≥40. ETA: ~1h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 501 | +0.051 | +41.56€ | 3 | 4 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 501 | +0.051 | +41.56€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 260 | +0.053 | +29.84€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 260 | +0.053 | +29.84€ | 2 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 212 | +0.028 | +0.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 212 | +0.028 | +0.79€ | 7 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 29 | +0.177 | +10.93€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 29 | +0.177 | +10.93€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 3804 | -0.113 | -581.05€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 482 | -0.021 | -21.48€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 3322 | -0.127 | -559.57€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 454 | -0.197 | -95.42€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 454 | -0.197 | -95.42€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 482 | -0.021 | -21.48€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 482 | -0.021 | -21.48€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 328 | -0.145 | -149.58€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 328 | -0.145 | -149.58€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 725 | -0.137 | -38.80€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 725 | -0.137 | -38.80€ | 2 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 973 | +0.011 | -117.55€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 973 | +0.011 | -117.55€ | 0 | 0 |
| 🚫 BALLENAS_TARDIAS#XRP | 842 | -0.230 | -158.23€ | 0 | 0 |
| 🚫 BALLENAS_TARDIAS#XRP#5min | 842 | -0.230 | -158.23€ | 1 | 0 |
| ✅ FAVORITO_CONFIRMADO | 16647 | +0.113 | -1086.40€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 3693 | +0.182 | -131.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 106 | -0.102 | -48.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 10173 | +0.086 | -914.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 2675 | +0.130 | +9.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 1719 | +0.035 | -377.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 14 | -0.044 | +0.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#240min | 5 | -0.089 | -6.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 1700 | +0.037 | -370.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 3690 | +0.136 | -48.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 1011 | +0.191 | -57.25€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 1688 | +0.108 | -34.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 949 | +0.139 | +65.73€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 1719 | +0.062 | -286.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 10 | +0.000 | -3.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 1708 | +0.063 | -281.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 3993 | +0.129 | -37.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 1364 | +0.167 | -9.17€ | 0 | 6 |
| 🚫 FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 1689 | +0.108 | -18.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 928 | +0.114 | -1.73€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 3814 | +0.131 | -264.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 1282 | +0.197 | -63.83€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 45 | +0.011 | -8.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 1689 | +0.080 | -138.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 798 | +0.136 | -54.82€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 1712 | +0.119 | -71.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 12 | +0.043 | +1.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 1699 | +0.120 | -71.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3786 | +0.165 | -342.87€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 3786 | +0.165 | -342.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 952 | +0.156 | -123.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 952 | +0.156 | -123.06€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 80 | -0.110 | -4.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 80 | -0.110 | -4.30€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 943 | +0.158 | -119.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 943 | +0.158 | -119.97€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 839 | +0.225 | -31.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 839 | +0.225 | -31.71€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 2 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 893 | +0.182 | -77.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 893 | +0.182 | -77.59€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 189 | +0.416 | -9.61€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 189 | +0.416 | -9.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 69 | +0.415 | -2.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 69 | +0.415 | -2.51€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 71 | +0.390 | -6.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 71 | +0.390 | -6.32€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 47 | +0.418 | -0.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 47 | +0.418 | -0.83€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 7307 | +0.187 | -719.66€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 7307 | +0.187 | -719.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 1367 | +0.098 | -310.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 1367 | +0.098 | -310.18€ | 0 | 1 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 1114 | +0.242 | -19.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 1114 | +0.242 | -19.11€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 1291 | +0.152 | -191.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 1291 | +0.152 | -191.68€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 1170 | +0.230 | -38.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 1170 | +0.230 | -38.29€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 1136 | +0.238 | -27.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 1136 | +0.238 | -27.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 1229 | +0.182 | -132.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 1229 | +0.182 | -132.85€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 2574 | +0.141 | +111.32€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 2574 | +0.141 | +111.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 1273 | +0.148 | +68.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 1273 | +0.148 | +68.98€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 1301 | +0.135 | +42.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 1301 | +0.135 | +42.34€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 571 | +0.303 | +9.06€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 571 | +0.303 | +9.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 241 | +0.274 | -9.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 241 | +0.274 | -9.00€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 265 | +0.305 | +9.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 265 | +0.305 | +9.43€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 65 | +0.381 | +8.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 65 | +0.381 | +8.63€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 239 | +0.409 | -11.73€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 239 | +0.409 | -11.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 105 | +0.406 | -5.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 105 | +0.406 | -5.47€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 110 | +0.411 | -6.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 110 | +0.411 | -6.40€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 24 | +0.346 | +0.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 24 | +0.346 | +0.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 14 | +0.263 | +8.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 10 | +0.167 | +5.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 11 | +0.190 | +6.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 10 | +0.167 | +5.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 372 | +0.096 | -15.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 36 | -0.053 | -8.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 336 | +0.112 | -6.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 250 | +0.079 | -13.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 36 | -0.053 | -8.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 214 | +0.102 | -5.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 122 | +0.129 | -1.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 122 | +0.129 | -1.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 275 | +0.273 | -23.71€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 275 | +0.273 | -23.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 275 | +0.273 | -23.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 275 | +0.273 | -23.71€ | 0 | 4 |
| ✅ GBM_LATE_15M | 4956 | +0.078 | +1806.75€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 4956 | +0.078 | +1806.75€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 843 | +0.176 | +534.73€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 843 | +0.176 | +534.73€ | 0 | 17 |
| ✅ GBM_LATE_15M#BTC | 521 | +0.181 | +281.37€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 521 | +0.181 | +281.37€ | 0 | 25 |
| ✅ GBM_LATE_15M#DOGE | 853 | +0.191 | +587.35€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 853 | +0.191 | +587.35€ | 0 | 18 |
| ✅ GBM_LATE_15M#ETH | 668 | -0.013 | +34.33€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 668 | -0.013 | +34.33€ | 1 | 2 |
| ✅ GBM_LATE_15M#SOL | 924 | -0.010 | +162.13€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 924 | -0.010 | +162.13€ | 3 | 4 |
| ✅ GBM_LATE_15M#XRP | 1147 | -0.001 | +206.84€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 1147 | -0.001 | +206.84€ | 1 | 5 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 5972 | +0.048 | +2218.47€ | 0 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 5972 | +0.048 | +2218.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 1126 | -0.028 | +510.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 1126 | -0.028 | +510.46€ | 1 | 3 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 1159 | -0.018 | +100.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 1159 | -0.018 | +100.48€ | 1 | 4 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 717 | +0.241 | +658.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 717 | +0.241 | +658.57€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 1038 | -0.026 | +41.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 1038 | -0.026 | +41.03€ | 7 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 1044 | +0.004 | +185.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 1044 | +0.004 | +185.44€ | 2 | 2 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 888 | +0.213 | +722.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 888 | +0.213 | +722.50€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 3692 | +0.179 | +2581.84€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 3692 | +0.179 | +2581.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 634 | +0.193 | +466.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 634 | +0.193 | +466.11€ | 0 | 16 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 513 | +0.201 | +372.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 513 | +0.201 | +372.50€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 630 | +0.201 | +486.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 630 | +0.201 | +486.64€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 487 | +0.210 | +377.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 487 | +0.210 | +377.43€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 680 | +0.084 | +296.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 680 | +0.084 | +296.14€ | 1 | 15 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 748 | +0.197 | +583.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 748 | +0.197 | +583.02€ | 0 | 23 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 637 | +0.060 | +85.49€ | 0 | 11 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 637 | +0.060 | +85.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 132 | +0.082 | +19.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 132 | +0.082 | +19.14€ | 2 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 119 | +0.161 | +41.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 119 | +0.161 | +41.72€ | 0 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 238 | -0.004 | +9.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 238 | -0.004 | +9.85€ | 4 | 3 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 147 | +0.064 | +16.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 147 | +0.064 | +16.05€ | 0 | 6 |
| ✅ GBM_LATE_15M_TARDIO | 4253 | +0.168 | +2770.58€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#15min | 4253 | +0.168 | +2770.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 807 | +0.182 | +553.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 807 | +0.182 | +553.90€ | 0 | 17 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 580 | +0.165 | +349.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 580 | +0.165 | +349.12€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 798 | +0.216 | +655.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 798 | +0.216 | +655.60€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 437 | +0.142 | +221.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 437 | +0.142 | +221.16€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 671 | +0.074 | +290.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 671 | +0.074 | +290.89€ | 2 | 14 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 960 | +0.191 | +699.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 960 | +0.191 | +699.90€ | 0 | 26 |
| ✅ GBM_LATE_5M | 417 | +0.116 | +158.85€ | 1 | 16 |
| ✅ GBM_LATE_5M#5min | 417 | +0.116 | +158.85€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 201 | +0.140 | +90.79€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 201 | +0.140 | +90.79€ | 1 | 14 |
| ✅ GBM_LATE_5M#DOGE | 13 | -0.108 | -4.42€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 13 | -0.108 | -4.42€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH | 115 | +0.209 | +75.79€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 115 | +0.209 | +75.79€ | 0 | 18 |
| ✅ GBM_LATE_5M#SOL | 50 | -0.058 | +1.63€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 50 | -0.058 | +1.63€ | 1 | 0 |
| ✅ GBM_LATE_5M#XRP | 38 | +0.025 | -4.94€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 38 | +0.025 | -4.94€ | 0 | 0 |
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
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 76 | -0.256 | -7.36€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 65 | -0.351 | -19.05€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 65 | -0.351 | -19.05€ | 2 | 0 |
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
| ✅ LEADLAG_BTC_XRP_15M | 94 | +0.125 | +23.18€ | 0 | 4 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 94 | +0.125 | +23.18€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 94 | +0.125 | +23.18€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 94 | +0.125 | +23.18€ | 0 | 4 |
| ✅ LIQUIDACIONES_15M | 202 | -0.113 | -29.52€ | 6 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 202 | -0.113 | -29.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 48 | -0.120 | -8.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 48 | -0.120 | -8.11€ | 1 | 0 |
| 🚫 LIQUIDACIONES_15M#DOGE | 22 | -0.208 | -5.32€ | 0 | 0 |
| 🚫 LIQUIDACIONES_15M#DOGE#15min | 22 | -0.208 | -5.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 42 | -0.023 | -2.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 42 | -0.023 | -2.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 39 | -0.037 | -2.70€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 39 | -0.037 | -2.70€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 46 | -0.167 | -8.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 46 | -0.167 | -8.95€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 145 | -0.153 | -25.31€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 145 | -0.153 | -25.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 54 | -0.143 | -8.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 54 | -0.143 | -8.84€ | 2 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE | 8 | -0.040 | -1.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 8 | -0.040 | -1.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 37 | -0.115 | -5.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 37 | -0.115 | -5.82€ | 1 | 0 |
| 🚫 LIQUIDACIONES_5M#SOL | 25 | -0.204 | -5.82€ | 0 | 0 |
| 🚫 LIQUIDACIONES_5M#SOL#5min | 25 | -0.204 | -5.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 20 | -0.182 | -4.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 20 | -0.182 | -4.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M | 314 | -0.003 | -6.07€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 314 | -0.003 | -6.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 105 | -0.014 | -8.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 105 | -0.014 | -8.11€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 103 | -0.024 | -2.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 103 | -0.024 | -2.59€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 106 | +0.028 | +4.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 106 | +0.028 | +4.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M | 1104 | +0.038 | +36.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 1104 | +0.038 | +36.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 149 | +0.089 | +33.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 149 | +0.089 | +33.35€ | 1 | 6 |
| ✅ MOMENTUM_IBS_15M#BTC | 202 | +0.069 | +18.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 202 | +0.069 | +18.24€ | 0 | 4 |
| ✅ MOMENTUM_IBS_15M#DOGE | 164 | +0.012 | -11.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 164 | +0.012 | -11.76€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 207 | +0.050 | +19.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 207 | +0.050 | +19.77€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M#SOL | 188 | -0.005 | -16.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 188 | -0.005 | -16.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 194 | +0.015 | -7.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 194 | +0.015 | -7.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 1462 | -0.022 | +66.94€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 1462 | -0.022 | +66.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 228 | -0.026 | +31.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 228 | -0.026 | +31.28€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 259 | -0.029 | -13.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 259 | -0.029 | -13.33€ | 6 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 234 | +0.009 | +49.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 234 | +0.009 | +49.23€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 257 | -0.013 | +4.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 257 | -0.013 | +4.82€ | 1 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 239 | -0.039 | +6.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 239 | -0.039 | +6.80€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 245 | -0.030 | -11.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 245 | -0.030 | -11.87€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 489 | -0.060 | -38.20€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 489 | -0.060 | -38.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 96 | -0.041 | -5.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 96 | -0.041 | -5.11€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 61 | -0.087 | -5.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 61 | -0.087 | -5.99€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 33 | -0.071 | -2.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 33 | -0.071 | -2.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 99 | -0.114 | -12.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 99 | -0.114 | -12.49€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 107 | -0.014 | -4.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 107 | -0.014 | -4.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 93 | -0.047 | -7.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 93 | -0.047 | -7.02€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 970 | +0.001 | +0.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 970 | +0.001 | +0.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 119 | -0.029 | -0.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 119 | -0.029 | -0.78€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 171 | +0.009 | -2.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 171 | +0.009 | -2.20€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 123 | +0.012 | +0.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 123 | +0.012 | +0.52€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#ETH | 194 | +0.005 | +5.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 194 | +0.005 | +5.37€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#SOL | 197 | +0.007 | +2.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 197 | +0.007 | +2.97€ | 0 | 1 |
| ✅ MOMENTUM_IBS_5M#XRP | 166 | -0.006 | -5.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 166 | -0.006 | -5.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 4202 | -0.057 | +201.88€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 4202 | -0.057 | +201.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 616 | -0.087 | +73.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 616 | -0.087 | +73.17€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 807 | -0.046 | +83.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 807 | -0.046 | +83.21€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 632 | -0.065 | +35.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 632 | -0.065 | +35.20€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 732 | -0.065 | -30.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 732 | -0.065 | -30.99€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 753 | -0.038 | -11.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 753 | -0.038 | -11.52€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 662 | -0.047 | +52.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 662 | -0.047 | +52.80€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 3537 | +0.008 | -4.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 3537 | +0.008 | -4.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 603 | +0.012 | +6.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 603 | +0.012 | +6.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 463 | +0.042 | +12.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 463 | +0.042 | +12.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 629 | +0.004 | -4.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 629 | +0.004 | -4.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 600 | +0.000 | -5.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 600 | +0.000 | -5.43€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 629 | +0.001 | -4.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 629 | +0.001 | -4.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 613 | -0.002 | -9.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 613 | -0.002 | -9.77€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 277 | +0.091 | +60.35€ | 1 | 4 |
| ✅ ORDER_FLOW_5M#5min | 141 | +0.122 | +47.75€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 38 | +0.200 | +27.80€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 38 | +0.200 | +27.80€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE | 25 | +0.093 | +6.33€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 25 | +0.093 | +6.33€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 16 | +0.089 | +5.33€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 16 | +0.089 | +5.33€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL | 32 | +0.088 | +4.95€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 32 | +0.088 | +4.95€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP | 30 | +0.062 | +3.34€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 30 | +0.062 | +3.34€ | 0 | 0 |
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
| ✅ STREAK_FADE_15M | 69 | -0.120 | -15.57€ | 4 | 0 |
| ✅ STREAK_FADE_15M#15min | 69 | -0.120 | -15.57€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 32 | -0.059 | -5.41€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 32 | -0.059 | -5.41€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 30 | -0.156 | -7.90€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 30 | -0.156 | -7.90€ | 0 | 0 |
| ✅ STREAK_FADE_5M | 436 | -0.018 | -20.22€ | 1 | 0 |
| ✅ STREAK_FADE_5M#5min | 436 | -0.018 | -20.22€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 136 | +0.007 | -1.09€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 136 | +0.007 | -1.09€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 136 | -0.015 | -7.78€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 136 | -0.015 | -7.78€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 68 | -0.043 | -4.71€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 68 | -0.043 | -4.71€ | 1 | 2 |
| ✅ STREAK_FADE_5M#XRP | 96 | -0.041 | -6.64€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 96 | -0.041 | -6.64€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 17 | -0.067 | -1.76€ | 0 | 0 |
| ✅ STREAK_FADE_60M#60min | 17 | -0.067 | -1.76€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 10 | -0.083 | -2.14€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 10 | -0.083 | -2.14€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 7 | +0.019 | +0.38€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 7 | +0.019 | +0.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 732 | +0.022 | +5.76€ | 1 | 0 |
| ✅ STREAK_MOM_5M#5min | 732 | +0.022 | +5.76€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 242 | +0.012 | -1.87€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 242 | +0.012 | -1.87€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 131 | -0.011 | -3.23€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 131 | -0.011 | -3.23€ | 3 | 2 |
| ✅ STREAK_MOM_5M#SOL | 198 | +0.025 | +1.15€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 198 | +0.025 | +1.15€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP | 161 | +0.058 | +9.71€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 161 | +0.058 | +9.71€ | 2 | 3 |
| ✅ STRUCT_NO_15M | 2042 | +0.007 | -21.93€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 2042 | +0.007 | -21.93€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 772 | +0.003 | -12.26€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 772 | +0.003 | -12.26€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 796 | +0.011 | -5.13€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 796 | +0.011 | -5.13€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 474 | +0.006 | -4.53€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 474 | +0.006 | -4.53€ | 2 | 0 |
| ✅ UPDOWN_GBM | 2811 | +0.029 | +204.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 1201 | +0.077 | +187.18€ | 1 | 9 |
| ✅ UPDOWN_GBM#240min | 131 | +0.011 | -1.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 1161 | -0.002 | +15.30€ | 3 | 0 |
| ✅ UPDOWN_GBM#60min | 271 | +0.002 | +4.57€ | 3 | 3 |
| ✅ UPDOWN_GBM#BNB | 123 | +0.100 | +27.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 116 | +0.119 | +29.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 6 | -0.075 | -2.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 545 | +0.047 | +63.98€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 145 | +0.078 | +8.85€ | 3 | 12 |
| ✅ UPDOWN_GBM#BTC#240min | 41 | +0.058 | +2.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 248 | +0.064 | +51.05€ | 2 | 7 |
| ✅ UPDOWN_GBM#BTC#60min | 93 | -0.016 | -0.19€ | 1 | 2 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 324 | +0.000 | +1.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 68 | +0.114 | +17.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 256 | -0.031 | -16.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 650 | +0.058 | +68.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 275 | +0.117 | +63.36€ | 1 | 17 |
| ✅ UPDOWN_GBM#ETH#240min | 41 | +0.058 | +1.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 210 | +0.019 | +1.41€ | 5 | 2 |
| ✅ UPDOWN_GBM#ETH#60min | 109 | +0.022 | +2.65€ | 0 | 2 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 545 | +0.003 | +2.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 237 | +0.006 | -3.08€ | 1 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 31 | -0.045 | -3.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 196 | +0.025 | +6.87€ | 3 | 4 |
| ✅ UPDOWN_GBM#SOL#60min | 69 | -0.007 | +2.11€ | 0 | 0 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 622 | +0.008 | +42.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 360 | +0.069 | +70.88€ | 0 | 9 |
| ✅ UPDOWN_GBM#XRP#240min | 17 | -0.112 | -2.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 245 | -0.071 | -25.06€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 119 | +0.269 | +3.58€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 119 | +0.269 | +3.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 75 | +0.227 | -7.07€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 75 | +0.227 | -7.07€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 44 | +0.326 | +10.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 44 | +0.326 | +10.65€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_TARDIO | 1947 | -0.061 | +433.91€ | 3 | 3 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 1947 | -0.061 | +433.91€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 143 | -0.066 | +102.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 143 | -0.066 | +102.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 378 | -0.147 | -19.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 378 | -0.147 | -19.58€ | 3 | 1 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 48 | +0.020 | +4.72€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 48 | +0.020 | +4.72€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 145 | +0.017 | +27.45€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 145 | +0.017 | +27.45€ | 2 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 629 | -0.034 | +218.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 629 | -0.034 | +218.84€ | 2 | 1 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 604 | -0.059 | +99.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 604 | -0.059 | +99.77€ | 3 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 10 | +0.000 | -0.15€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 10 | +0.000 | -0.15€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 10 | +0.000 | -0.15€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 10 | +0.000 | -0.15€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 170 | +0.273 | +103.97€ | 0 | 12 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 170 | +0.273 | +103.97€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 101 | +0.248 | +48.21€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 101 | +0.248 | +48.21€ | 0 | 13 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 69 | +0.303 | +55.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 69 | +0.303 | +55.76€ | 0 | 9 |
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
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.124) — sin ventaja clara. oversold(IBS<0.3): IC=-0.007 n=967 | neutral: IC=+0.024 n=936 | overbought(IBS>0.7): IC=+0.117 n=1242
  - _Datos_: n=3372 IC=+0.050 PNL=+349.32€

**🟡 H-HORA-GBM** — hora_utc causal automático en GBM (forward)
  - _Umbral_: n≥20 forward con hora_utc + alguna hora con n≥15 IC<-0.10 o >+0.10
  - _Acción_: El sistema lo aplica automáticamente vía FEATURE_RULES. Verificar en strategy_params.json.
  - _Estado_: H=16h: IC=+0.118 n=108 PNL=+28.67€ → BOOST | H=19h: IC=+0.101 n=146 PNL=+40.12€ → BOOST

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 2 celda(s) pasan gate riguroso completo de 75 evaluadas (n>=40) y 352 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.006 < 0.08 — monitorear
  - _Datos_: n=237 IC=+0.006 PNL=-3.08€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=304/15 IC=+0.255 PNL=+66.23€ | BTC: n=284/15 IC=+0.199 PNL=+4.00€ | SOL: n=369/15 IC=+0.373 PNL=+311.70€

**🟡 H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.098 n=46625 | tras_1loss IC=+0.054 n=33816 | tras_2loss IC=+0.012 n=15018/40 | gap=+0.086 (umbral 0.05)

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 16 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC, UPDOWN_GBM#SOL
  - _Bloqueante_: N_INSUFICIENTE


### ⏳ Acumulando datos

**⏳ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: 15
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: Falta 11 ops más en GBM@18h (IC actual=-0.067)
  - _Datos_: n=4 IC=-0.067 PNL=-3.02€

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.204 n=19/60 | contraria IC=-0.065 n=13 | gap=+0.269 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=29, boost estimado=+0.009. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 32/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=109/40 IC=+0.022 PNL=+2.65€ | BTC#60min: n=93/40 IC=-0.016 PNL=-0.19€ | SOL#60min: n=69/40 IC=-0.007 PNL=+2.11€

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.047 n=232 | contrario_BTC IC=+0.022 n=157/40 | gap=-0.025 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.156 > 0.08 con n=62 PNL=+28.27€
  - _Datos_: n=62 IC=+0.156 PNL=+28.27€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.125 > 0.08 con n=78 PNL=+19.16€
  - _Datos_: n=78 IC=+0.125 PNL=+19.16€

**⏳ H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: 25
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: 5/25 ops en el filtro definido (IC actual=+0.089 PNL=+6.13€)
  - _Datos_: n=5 IC=+0.089 PNL=+6.13€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.338 > 0.1 con n=813 PNL=+389.76€
  - _Datos_: n=813 IC=+0.338 PNL=+389.76€

**🟡 H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.083 > 0.08 con n=22 PNL=+8.36€
  - _Datos_: n=22 IC=+0.083 PNL=+8.36€

**⏳ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: 30
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: 10/30 ops en el filtro definido (IC actual=+0.042 PNL=+0.77€)
  - _Datos_: n=10 IC=+0.042 PNL=+0.77€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=2575 IC=+0.023 PNL=+151.06€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=2575 IC=+0.023 PNL=+151.06€

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
  - _Estado_: n=212 IC=+0.033 PNL=+12.04€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=212 IC=+0.033 PNL=+12.04€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=59 IC=-0.107 PNL=-7.47€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=59 IC=-0.107 PNL=-7.47€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=53 IC=+0.009 PNL=+0.42€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=53 IC=+0.009 PNL=+0.42€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.112 > 0.1 con n=436 PNL=+80.89€
  - _Datos_: n=436 IC=+0.112 PNL=+80.89€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=167 IC=+0.092 PNL=+43.27€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=167 IC=+0.092 PNL=+43.27€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=145 IC=+0.078 PNL=+8.85€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=145 IC=+0.078 PNL=+8.85€

**⏳ H-CUSTOM-DRIFT15-ZONA-MUERTA** — GBM#15min drift_15min ∈ [-0.3,+0.3] — zona muerta de señal
  - _Hipótesis_: Análisis n=127 GBM#15min: cuando drift_15min está entre -0.3 y +0.3 (mercado sin dirección clara) el IC es negativo (-0.043). Cuando drift>0.3 IC=+0.100 (n=28). Cuando drift<-1 IC=+0.048 (reversión). La señal requiere mercado con dirección clara.
  - _Umbral_: 50
  - _Acción_: Filtrar señales GBM#15min cuando drift_15min ∈ [-0.3, +0.3] — validar con n≥50 antes de implementar
  - _Estado_: 0/50 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-DRIFT15-MOMENTUM** — GBM#15min drift_15min > 0.3 — zona de momentum (señal fuerte)
  - _Hipótesis_: Cuando drift_15min > 0.3%/h el GBM captura bien la dirección: IC=+0.100 n=28 en todos GBM#15min; IC=+0.152 n=13 solo BTC. El mercado tiene dirección clara y el GBM la sigue. Hipótesis: este rango es donde la señal es real.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma IC>0.10 con n≥40 → boost ×1.2 en GBM#15min cuando drift_15min>0.3
  - _Estado_: n=757 IC=+0.073 PNL=+93.50€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=757 IC=+0.073 PNL=+93.50€

**⏳ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: 16/30 ops en el filtro definido (IC actual=-0.178 PNL=-2.92€)
  - _Datos_: n=16 IC=-0.178 PNL=-2.92€

**⏳ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: 20
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: 18/20 ops en el filtro definido (IC actual=+0.225 PNL=+14.99€)
  - _Datos_: n=18 IC=+0.225 PNL=+14.99€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=36 IC=+0.184 PNL=+12.51€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=36 IC=+0.184 PNL=+12.51€

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
  - _Estado_: n=222 IC=+0.058 PNL=+28.70€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=222 IC=+0.058 PNL=+28.70€

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
  - _Estado_: 4/30 ops en el filtro definido (IC actual=+0.067 PNL=+2.07€)
  - _Datos_: n=4 IC=+0.067 PNL=+2.07€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=655 IC=+0.065 PNL=+101.95€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=655 IC=+0.065 PNL=+101.95€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=334 IC=+0.042 PNL=+5.75€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=334 IC=+0.042 PNL=+5.75€

**⏳ H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: 40
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: 37/40 ops en el filtro definido (IC actual=+0.141 PNL=+12.57€)
  - _Datos_: n=37 IC=+0.141 PNL=+12.57€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.156 > 0.08 con n=94 PNL=-1.57€
  - _Datos_: n=94 IC=+0.156 PNL=-1.57€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.100 > 0.08 con n=83 PNL=+16.27€
  - _Datos_: n=83 IC=+0.100 PNL=+16.27€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=571 IC=+0.144 PNL=+1.44€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=571 IC=+0.144 PNL=+1.44€

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
  - _Estado_: n=404 IC=+0.042 PNL=+27.72€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=404 IC=+0.042 PNL=+27.72€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.174 > 0.02 con n=142 PNL=+61.20€
  - _Datos_: n=142 IC=+0.174 PNL=+61.20€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=86 IC=-0.125 PNL=+14.04€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=86 IC=-0.125 PNL=+14.04€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.444 > 0.1 con n=533 PNL=+436.37€
  - _Datos_: n=533 IC=+0.444 PNL=+436.37€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=1033 IC=+0.032 PNL=+60.57€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=1033 IC=+0.032 PNL=+60.57€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.161 > 0.1 con n=593 PNL=+203.55€
  - _Datos_: n=593 IC=+0.161 PNL=+203.55€

**⏳ H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: 40
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: 12/40 ops en el filtro definido (IC actual=-0.214 PNL=-6.49€)
  - _Datos_: n=12 IC=-0.214 PNL=-6.49€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=232 IC=+0.060 PNL=+36.86€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=232 IC=+0.060 PNL=+36.86€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=30 IC=-0.188 PNL=+2.99€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=30 IC=-0.188 PNL=+2.99€

**⏳ H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: 50
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: 38/50 ops en el filtro definido (IC actual=+0.150 PNL=+5.69€)
  - _Datos_: n=38 IC=+0.150 PNL=+5.69€

**⏳ H-CUSTOM-ETH15-BUYNO-PRECIO-ALTO** — ETH#15min BUY_NO con precio_yes>0.55 pierde (NO longshot contra favorito)
  - _Hipótesis_: Detectado 2026-07-02: ult.60 shadow ETH15 BUY_NO — py_mkt~0.5 wr=0.67 PNL=+29.3 (n=49); py_mkt 0.6-0.8 wr 0.33-0 PNL=-5.75 (n=9). Filtro RETURN NONE (no SKIP) aplicado en shadow_predict.py (PY_MKT_MAX_BUY_NO_ETH15=0.55) el mismo dia -- bloquea la GENERACIÓN de la fila, no solo la decisión. Esta hipotesis trackea la zona filtrada: si las ops que HABRIAN caido aqui siguen apareciendo en otras estrategias o el IC forward de la zona se vuelve positivo, revisar el filtro. CAVEAT: n=9, muestra chica — el filtro se aplico por asimetria de riesgo (afecta a dinero live), no por significancia. ⚠️ 05-Ago (fix): la clave del filtro decía 'py_mkt', que NUNCA existió ni en features de UPDOWN_GBM (T_h/delta_ratio_macro/drift_15min/drift_60min/pct_spot_vs_ref/sigma_h) ni como columna top-level de results.csv -- corregida a 'precio_yes_mercado' (columna real). Aun así, con la clave correcta esta hipótesis NUNCA podrá acumular n mientras el filtro RETURN NONE siga activo -- es el mismo patrón 'frozen by design' que H-CUSTOM-LATE15-PHOTO-FINISH (más abajo): la propia protección impide generar los datos necesarios para volver a evaluarla. Para monitorearla de verdad haría falta un logger separado que capture la señal SIN aplicar el filtro (mismo patrón que gate_bucket_propio con data/markets histórico) -- no construido, pendiente decisión.
  - _Umbral_: 20
  - _Acción_: Si IC forward de la zona >0 con n>=20 → retirar filtro; si confirma negativo → considerar extender a BTC/SOL 15min
  - _Estado_: 0/20 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-PRECIO-YES-BARATO** — BUY_YES con precio de mercado 0.30-0.40 — mercado infravalora YES
  - _Hipótesis_: Detectado 2026-07-03 en benchmark de calibración del mercado (7d, estrategias GBM): en el bucket precio_yes_mercado [0.3-0.4) la frecuencia real de YES fue 0.45 vs 0.35 implícito (+0.10, n=38). Posible sesgo favorito-longshot suave en binarios de 15min (complemento del LONGSHOT ya activo para BUY_NO con py<0.20). Si se confirma, BUY_YES comprado en esa banda lleva viento de cola estructural del propio mercado, independiente del modelo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → kelly_boost ×1.1 para BUY_YES con precio_yes_mercado en [0.30,0.40), simétrico al longshot BUY_NO existente
  - _Estado_: n=1727 IC=-0.133 PNL=+161.28€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1727 IC=-0.133 PNL=+161.28€

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
  - _Estado_: n=352 IC=+0.138 PNL=+121.47€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=352 IC=+0.138 PNL=+121.47€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.112 > 0.08 con n=436 PNL=+80.89€
  - _Datos_: n=436 IC=+0.112 PNL=+80.89€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=283 IC=+0.016 PNL=+11.59€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=283 IC=+0.016 PNL=+11.59€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.130 > 0.08 con n=411 PNL=+267.57€
  - _Datos_: n=411 IC=+0.130 PNL=+267.57€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.145 > 0.08 con n=105 PNL=+15.03€
  - _Datos_: n=105 IC=+0.145 PNL=+15.03€

**⏳ H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: 289
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: 105/289 ops en el filtro definido (IC actual=-0.248 PNL=-10.48€)
  - _Datos_: n=105 IC=-0.248 PNL=-10.48€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=854 IC=+0.158 PNL=+480.31€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=854 IC=+0.158 PNL=+480.31€

**⏳ H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: 40
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: 17/40 ops en el filtro definido (IC actual=+0.022 PNL=-1.83€)
  - _Datos_: n=17 IC=+0.022 PNL=-1.83€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=367 IC=-0.015 PNL=+15.32€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=367 IC=-0.015 PNL=+15.32€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.197 > 0.08 con n=311 PNL=+176.86€
  - _Datos_: n=311 IC=+0.197 PNL=+176.86€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=612 IC=+0.008 PNL=+140.19€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=612 IC=+0.008 PNL=+140.19€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.134 > 0.08 con n=173 PNL=-14.36€
  - _Datos_: n=173 IC=+0.134 PNL=-14.36€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.245 > 0.08 con n=738 PNL=-76.99€
  - _Datos_: n=738 IC=+0.245 PNL=-76.99€

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 5/40 ops en el filtro definido (IC actual=-0.018 PNL=+0.46€)
  - _Datos_: n=5 IC=-0.018 PNL=+0.46€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.130 n=52) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=52 IC=+0.130 PNL=+16.44€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.363 > 0.08 con n=49 PNL=+41.33€
  - _Datos_: n=49 IC=+0.363 PNL=+41.33€

**⏳ H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: 200
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: 189/200 ops en el filtro definido (IC actual=+0.442 PNL=+252.45€)
  - _Datos_: n=189 IC=+0.442 PNL=+252.45€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=1367 IC=+0.098 PNL=-310.18€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=1367 IC=+0.098 PNL=-310.18€

**⏳ H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: 40
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: 19/40 ops en el filtro definido (IC actual=+0.204 PNL=+9.88€)
  - _Datos_: n=19 IC=+0.204 PNL=+9.88€
