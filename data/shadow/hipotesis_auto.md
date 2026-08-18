# Hipótesis automáticas — 2026-08-18 11:59 UTC
_Generado por shadow_postmortem.py sobre 62561 resoluciones (PNL=+6429.82€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.355` → IC=-0.143 (n=68)

  - _Acción_: SKIP cuando `py_entrada` < 0.355
  - _Potencial_: sin este filtro IC_bueno=+0.180 (n=148)

- **FILTRO** `banda_hit_calibrado` < `0.6142` → IC=-0.227 (n=53)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6142
  - _Potencial_: sin este filtro IC_bueno=+0.179 (n=163)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.377 (n=63)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.139 (n=206)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.237 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.078)

- **PATRÓN** `n_total_lado` > `74.0` → IC=+0.196 (n=54)

  - _Acción_: Kelly boost +0.98€ cuando `n_total_lado` > 74.0 (IC base=+0.078)

- **PATRÓN** `banda_hit_calibrado` > `0.6142` → IC=+0.179 (n=163)

  - _Acción_: Kelly boost +0.89€ cuando `banda_hit_calibrado` > 0.6142 (IC base=+0.078)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.139 (n=206)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.5 (IC base=+0.017)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `banda_hit_calibrado` < `0.6142` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6142
  - _Potencial_: sin este filtro IC_bueno=+0.191 (n=82)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.338 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=109)

- **PATRÓN** `py_entrada` > `0.705` → IC=+0.242 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.705 (IC base=+0.091)

- **PATRÓN** `n_total_lado` > `94.0` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 94.0 (IC base=+0.091)

- **PATRÓN** `banda_hit_calibrado` > `0.6142` → IC=+0.191 (n=82)

  - _Acción_: Kelly boost +0.95€ cuando `banda_hit_calibrado` > 0.6142 (IC base=+0.091)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.122 (n=109)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.495 (IC base=+0.007)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.278 (n=25)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=+0.171 (n=83)

- **FILTRO** `banda_hit_calibrado` < `0.6267` → IC=-0.203 (n=35)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6267
  - _Potencial_: sin este filtro IC_bueno=+0.193 (n=73)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.128 (n=84)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.353 (n=32)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=68)

- **FILTRO** `n_ballena_banda` < `30.0` → IC=-0.128 (n=49)

  - _Acción_: SKIP cuando `n_ballena_banda` < 30.0
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=51)

- **FILTRO** `hora_utc` < `11.0` → IC=-0.125 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=70)

- **PATRÓN** `py_entrada` > `0.33` → IC=+0.171 (n=83)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.33 (IC base=+0.064)

- **PATRÓN** `banda_hit_calibrado` > `0.6267` → IC=+0.193 (n=73)

  - _Acción_: Kelly boost +0.97€ cuando `banda_hit_calibrado` > 0.6267 (IC base=+0.064)

- **PATRÓN** `banda_z` > `8.876` → IC=+0.224 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.876 (IC base=+0.064)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.128 (n=84)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.02 (IC base=+0.064)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.143 (n=68)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.495 (IC base=-0.020)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `145.56` → IC=-0.262 (n=822)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 145.56
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=2468)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `113.6` → IC=-0.400 (n=88)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 113.6
  - _Potencial_: sin este filtro IC_bueno=-0.128 (n=267)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` > `639.83` → IC=-0.279 (n=111)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` > 639.83
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=336)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `141.73` → IC=-0.412 (n=157)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 141.73
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=157)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `n_ballenas` < `4.0` → IC=-0.153 (n=188)

  - _Acción_: SKIP cuando `n_ballenas` < 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.123 (n=571)

- **FILTRO** `restante_s_al_confirmar` < `244.14` → IC=-0.155 (n=569)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 244.14
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=190)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `140.8` → IC=-0.192 (n=193)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 140.8
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=581)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `158.17` → IC=-0.272 (n=160)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 158.17
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=481)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.7` → IC=+0.206 (n=2147)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.7 (IC base=+0.098)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.164 (n=1146)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `2373.5135` → IC=+0.166 (n=1109)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2373.5135 (IC base=+0.098)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.153 (n=3663)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 7.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.153 (n=2868)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 11.0 (IC base=+0.148)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.283 (n=1351)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.186 (n=1977)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.02 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `4023.461` → IC=+0.174 (n=801)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 4023.461 (IC base=+0.148)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.206 (n=352)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` > `0.775` → IC=+0.354 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.775 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.201 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.222 (n=296)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.327 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.193 (n=424)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.01 (IC base=+0.191)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=387)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.161 (n=337)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 15.0 (IC base=+0.133)

- **PATRÓN** `py_entrada` > `0.6` → IC=+0.169 (n=179)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` > 0.6 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `5033.4098` → IC=+0.165 (n=195)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 5033.4098 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.199 (n=161)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.140)

- **PATRÓN** `py_entrada` < `0.395` → IC=+0.218 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.395 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `5296.1268` → IC=+0.175 (n=204)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 5296.1268 (IC base=+0.140)

### FAVORITO_CONFIRMADO#ETH#15min
- **PATRÓN** `hora_utc` < `11.0` → IC=+0.147 (n=460)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 11.0 (IC base=+0.113)

- **PATRÓN** `py_entrada` > `0.7` → IC=+0.303 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.7 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.305 (n=259)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.287)

- **PATRÓN** `py_entrada` < `0.195` → IC=+0.395 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.195 (IC base=+0.287)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.290 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `3321.5477` → IC=+0.347 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3321.5477 (IC base=+0.287)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=278)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.168 (n=245)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 16.0 (IC base=+0.142)

- **PATRÓN** `py_entrada` > `0.655` → IC=+0.232 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.655 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.147 (n=270)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `2191.1992` → IC=+0.165 (n=267)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2191.1992 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `5697.4897` → IC=+0.190 (n=69)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 5697.4897 (IC base=+0.096)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.181 (n=556)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.190 (n=478)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.409 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.270 (n=111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.231)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.231 (n=225)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.231)

- **PATRÓN** `py_entrada` < `0.31` → IC=+0.347 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.31 (IC base=+0.231)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.253 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.231)

- **PATRÓN** `libro_liquidez` > `911.1943` → IC=+0.242 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 911.1943 (IC base=+0.231)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `19.0` → IC=+0.253 (n=75)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 19.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.199 (n=151)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.342 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.244 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `3467.6863` → IC=+0.183 (n=58)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 3467.6863 (IC base=+0.191)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.218 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.107)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.160 (n=257)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.02 (IC base=+0.107)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `11.0` → IC=-0.297 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=65)

- **FILTRO** `py_entrada` > `0.845` → IC=-0.379 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.845
  - _Potencial_: sin este filtro IC_bueno=-0.225 (n=96)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.197 (n=1168)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 7.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.184 (n=956)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` < 0.7 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.204 (n=896)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `3268.7028` → IC=+0.348 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3268.7028 (IC base=+0.183)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.164 (n=590)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 15.0 (IC base=+0.155)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.176 (n=588)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.73 (IC base=+0.155)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.259 (n=27)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.417 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.326)

- **PATRÓN** `py_entrada` > `0.835` → IC=+0.370 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.835 (IC base=+0.326)

- **PATRÓN** `libro_liquidez` > `2916.5858` → IC=+0.343 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2916.5858 (IC base=+0.326)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=660)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.189 (n=291)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 7.0 (IC base=+0.162)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.195 (n=221)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.7 (IC base=+0.162)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.163 (n=363)

  - _Acción_: Kelly boost +0.82€ cuando `py_entrada` > 0.73 (IC base=+0.162)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.222 (n=580)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.234 (n=513)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.313 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.221)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min
- **FILTRO** `py_entrada` > `0.755` → IC=-0.267 (n=58)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=20)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.202 (n=213)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.200 (n=275)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` < `0.72` → IC=+0.197 (n=483)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.72 (IC base=+0.180)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.439 (n=113)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.417)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.422 (n=113)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.417)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.423 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.417)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.456 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.417)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.414 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.417)

- **PATRÓN** `libro_liquidez` > `3351.8902` → IC=+0.432 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3351.8902 (IC base=+0.417)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `12.0` → IC=+0.412 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.418)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.427 (n=39)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.418)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.433 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.418)

- **PATRÓN** `libro_liquidez` > `6696.5886` → IC=+0.413 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6696.5886 (IC base=+0.418)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.415 (n=45)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.382)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.372 (n=45)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.382)

- **PATRÓN** `py_entrada` < `0.91` → IC=+0.400 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.91 (IC base=+0.382)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.395 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.382)

- **PATRÓN** `libro_liquidez` > `2008.7424` → IC=+0.394 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2008.7424 (IC base=+0.382)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.417 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.427)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.417 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.427)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.204 (n=1422)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.203 (n=1528)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.254 (n=1460)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` < `10.0` → IC=+0.126 (n=532)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 10.0 (IC base=+0.102)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.139 (n=383)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` > 0.73 (IC base=+0.102)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `16.0` → IC=+0.300 (n=248)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.256)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.265 (n=236)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.256)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.340 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.256)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` < `7.0` → IC=+0.167 (n=367)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 7.0 (IC base=+0.154)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.220 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.154)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.239 (n=497)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.228)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.229 (n=706)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.228)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.298 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.228)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.261 (n=220)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.251)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.265 (n=228)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.251)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.285 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.251)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.255 (n=231)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.207 (n=469)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.256 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.227 (n=566)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.150)

- **PATRÓN** `restante_min` < `3.79` → IC=+0.162 (n=498)

  - _Acción_: Kelly boost +0.81€ cuando `restante_min` < 3.79 (IC base=+0.150)

- **PATRÓN** `restante_min` > `4.91` → IC=+0.204 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `restante_min` > 4.91 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.157 (n=1342)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 7.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.157 (n=1542)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 17.0 (IC base=+0.150)

- **PATRÓN** `lag_apertura_s` < `5.48` → IC=+0.214 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `lag_apertura_s` < 5.48 (IC base=+0.150)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.240 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.154)

- **PATRÓN** `restante_min` < `3.72` → IC=+0.171 (n=247)

  - _Acción_: Kelly boost +0.85€ cuando `restante_min` < 3.72 (IC base=+0.154)

- **PATRÓN** `restante_min` > `4.88` → IC=+0.191 (n=260)

  - _Acción_: Kelly boost +0.95€ cuando `restante_min` > 4.88 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=760)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.166 (n=680)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 15.0 (IC base=+0.154)

- **PATRÓN** `lag_apertura_s` < `7.37` → IC=+0.191 (n=247)

  - _Acción_: Kelly boost +0.95€ cuando `lag_apertura_s` < 7.37 (IC base=+0.154)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.43` → IC=+0.178 (n=672)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.43 (IC base=+0.145)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.219 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `restante_min` > 4.95 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.151 (n=675)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 7.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.155 (n=780)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 17.0 (IC base=+0.145)

- **PATRÓN** `lag_apertura_s` < `3.18` → IC=+0.223 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `lag_apertura_s` < 3.18 (IC base=+0.145)

- **PATRÓN** `profundidad_ratio_no` > `13.5` → IC=+0.172 (n=251)

  - _Acción_: Kelly boost +0.86€ cuando `profundidad_ratio_no` > 13.5 (IC base=+0.145)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.307 (n=418)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.297)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.308 (n=399)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.297)

- **PATRÓN** `py_entrada` > `0.825` → IC=+0.382 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.825 (IC base=+0.297)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.280 (n=175)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.268)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.276 (n=172)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.268)

- **PATRÓN** `py_entrada` < `0.725` → IC=+0.283 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.725 (IC base=+0.268)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.346 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.268)

- **PATRÓN** `libro_liquidez` > `3909.8054` → IC=+0.275 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3909.8054 (IC base=+0.268)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.310 (n=193)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.299)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.314 (n=192)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.299)

- **PATRÓN** `py_entrada` > `0.81` → IC=+0.394 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.81 (IC base=+0.299)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.299)

- **PATRÓN** `libro_liquidez` > `1882.9092` → IC=+0.319 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1882.9092 (IC base=+0.299)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` < `13.0` → IC=+0.444 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.371)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.409 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.371)

- **PATRÓN** `libro_liquidez` > `943.1727` → IC=+0.372 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 943.1727 (IC base=+0.371)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.405 (n=166)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.406)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.430 (n=169)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.406)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.409 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.406)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.427 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.406)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.404 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.406)

- **PATRÓN** `libro_liquidez` > `2161.2964` → IC=+0.414 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2161.2964 (IC base=+0.406)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.397 (n=76)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.401)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.438 (n=78)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.401)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.412 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.401)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.417 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.401)

- **PATRÓN** `libro_liquidez` > `5722.415` → IC=+0.426 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5722.415 (IC base=+0.401)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.408 (n=74)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.410)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.413 (n=67)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.410)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.411 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.410)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.425 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.410)

- **PATRÓN** `libro_liquidez` > `1842.491` → IC=+0.434 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1842.491 (IC base=+0.410)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.288 (n=130)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.262)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.422 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.262)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.280 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.262)

- **PATRÓN** `libro_liquidez` > `1406.0028` → IC=+0.309 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1406.0028 (IC base=+0.262)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.288 (n=130)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.262)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.422 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.262)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.280 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.262)

- **PATRÓN** `libro_liquidez` > `1406.0028` → IC=+0.309 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1406.0028 (IC base=+0.262)

### GBM_LATE_15M
- **PATRÓN** `hora_utc` < `6.0` → IC=+0.148 (n=441)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 6.0 (IC base=+0.108)

- **PATRÓN** `ibs_20min` > `0.995` → IC=+0.277 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.995 (IC base=+0.108)

- **PATRÓN** `dist_vwap_pct` > `0.5682` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5682 (IC base=+0.108)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.794` → IC=+0.244 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.794 (IC base=+0.108)

- **PATRÓN** `volumen_regimen` < `1.313` → IC=+0.235 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.313 (IC base=+0.108)

- **PATRÓN** `volumen_regimen` > `0.7541` → IC=+0.241 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7541 (IC base=+0.108)

- **PATRÓN** `volumen_pendiente_norm` > `0.3253` → IC=+0.177 (n=94)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.3253 (IC base=+0.108)

- **PATRÓN** `volumen_spike_ratio` > `1.6927` → IC=+0.131 (n=597)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 1.6927 (IC base=+0.108)

- **PATRÓN** `ibs_20min` < `0.6597` → IC=+0.122 (n=2101)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.6597 (IC base=+0.077)

- **PATRÓN** `volumen_regimen` < `0.6331` → IC=+0.150 (n=158)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6331 (IC base=+0.077)

- **PATRÓN** `volumen_regimen` > `0.6951` → IC=+0.138 (n=421)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.6951 (IC base=+0.077)

- **PATRÓN** `volumen_pendiente_norm` > `0.0892` → IC=+0.275 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0892 (IC base=+0.077)

- **PATRÓN** `volumen_spike_ratio` < `1.5756` → IC=+0.238 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5756 (IC base=+0.077)

- **PATRÓN** `volumen_spike_ratio` > `2.9145` → IC=+0.233 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9145 (IC base=+0.077)

- **PATRÓN** `ballena_activa_n` < `245.0` → IC=+0.256 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 245.0 (IC base=+0.077)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.180 (n=176)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.007 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.191 (n=147)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 6.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.300 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.577` → IC=+0.347 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.577 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2139` → IC=+0.139 (n=59)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.2139 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.171 (n=278)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.06 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.331 (n=63)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.281)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.333 (n=64)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.281)

- **PATRÓN** `drift_60min` |x|≤ `0.2086` → IC=+0.320 (n=165)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2086 (IC base=+0.281)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.284 (n=197)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.281)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.303 (n=130)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.281)

- **PATRÓN** `ibs_20min` < `0.5765` → IC=+0.331 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5765 (IC base=+0.281)

- **PATRÓN** `volumen_pendiente_norm` < `0.0708` → IC=+0.300 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0708 (IC base=+0.281)

- **PATRÓN** `volumen_pendiente_norm` > `0.1782` → IC=+0.329 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1782 (IC base=+0.281)

- **PATRÓN** `volumen_spike_ratio` < `1.8142` → IC=+0.331 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8142 (IC base=+0.281)

- **PATRÓN** `volumen_spike_ratio` > `1.5873` → IC=+0.295 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5873 (IC base=+0.281)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.324 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `1914.6582` → IC=+0.316 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1914.6582 (IC base=+0.281)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0018` → IC=+0.294 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0018 (IC base=+0.256)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.294 (n=32)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.256)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.294 (n=95)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.256)

- **PATRÓN** `ibs_20min` < `0.699` → IC=+0.265 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.699 (IC base=+0.256)

- **PATRÓN** `ibs_20min` > `0.9174` → IC=+0.285 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9174 (IC base=+0.256)

- **PATRÓN** `dist_vwap_pct` > `0.6067` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6067 (IC base=+0.256)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.858` → IC=+0.336 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.858 (IC base=+0.256)

- **PATRÓN** `volumen_regimen` < `1.4038` → IC=+0.271 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.4038 (IC base=+0.256)

- **PATRÓN** `volumen_pendiente_norm` < `0.1838` → IC=+0.308 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1838 (IC base=+0.256)

- **PATRÓN** `volumen_spike_ratio` < `2.7168` → IC=+0.306 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.7168 (IC base=+0.256)

- **PATRÓN** `libro_liquidez` > `11282.8623` → IC=+0.300 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11282.8623 (IC base=+0.256)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.150 (n=224)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0034 (IC base=+0.143)

- **PATRÓN** `sigma_h` > `0.0024` → IC=+0.147 (n=151)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0024 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.1869` → IC=+0.163 (n=197)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1869 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.190 (n=156)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 12.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` < `0.4773` → IC=+0.208 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4773 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.365` → IC=+0.250 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.365 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `1.2895` → IC=+0.159 (n=224)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2895 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` > `0.6827` → IC=+0.158 (n=200)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.6827 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.1281` → IC=+0.276 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1281 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `1.6686` → IC=+0.264 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6686 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `11311.9325` → IC=+0.149 (n=75)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 11311.9325 (IC base=+0.143)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.177 (n=159)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0071 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.209 (n=132)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.283 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.106` → IC=+0.298 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.106 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.4216` → IC=+0.191 (n=40)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.4216 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `3.9033` → IC=+0.137 (n=122)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 3.9033 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.157 (n=383)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.06 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `1915.8272` → IC=+0.158 (n=159)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 1915.8272 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.135)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.348 (n=77)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.280)

- **PATRÓN** `drift_60min` |x|≤ `0.0858` → IC=+0.308 (n=76)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0858 (IC base=+0.280)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.287 (n=233)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.280)

- **PATRÓN** `ibs_20min` < `0.5011` → IC=+0.308 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5011 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.093` → IC=+0.311 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.093 (IC base=+0.280)

- **PATRÓN** `volumen_pendiente_norm` > `0.4178` → IC=+0.405 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.4178 (IC base=+0.280)

- **PATRÓN** `volumen_spike_ratio` < `2.0261` → IC=+0.292 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0261 (IC base=+0.280)

- **PATRÓN** `volumen_spike_ratio` > `3.1011` → IC=+0.250 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.1011 (IC base=+0.280)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.284 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.280)

### GBM_LATE_15M#ETH#15min
- **PATRÓN** `drift_60min` |x|≤ `0.0705` → IC=+0.157 (n=33)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.0705 (IC base=+0.064)

- **PATRÓN** `ibs_20min` > `0.772` → IC=+0.160 (n=45)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.772 (IC base=+0.064)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.421` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.421 (IC base=+0.064)

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

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.180 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0054 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `19.0` → IC=+0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 19.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` > `0.5714` → IC=+0.283 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5714 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.915` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 3.915 (IC base=+0.159)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `2758.2556` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2758.2556 (IC base=+0.159)

### GBM_LATE_15M#XRP#15min
- **PATRÓN** `volumen_regimen` < `0.7863` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.7863 (IC base=-0.008)

- **PATRÓN** `volumen_regimen` < `0.6973` → IC=+0.274 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6973 (IC base=+0.039)

- **PATRÓN** `volumen_regimen` > `1.3677` → IC=+0.232 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.3677 (IC base=+0.039)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `ibs_20min` > `0.9448` → IC=+0.236 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9448 (IC base=+0.056)

- **PATRÓN** `dist_vwap_pct` > `0.3235` → IC=+0.191 (n=66)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.3235 (IC base=+0.056)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.242` → IC=+0.132 (n=970)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 2.242 (IC base=+0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.3377` → IC=+0.193 (n=99)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.3377 (IC base=+0.056)

- **PATRÓN** `volumen_spike_ratio` > `2.8797` → IC=+0.176 (n=285)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.8797 (IC base=+0.056)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.353 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 30.0 (IC base=+0.056)

- **PATRÓN** `ibs_20min` < `0.1` → IC=+0.166 (n=838)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.1 (IC base=+0.047)

- **PATRÓN** `dist_vwap_pct` > `0.5114` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5114 (IC base=+0.047)

- **PATRÓN** `volumen_regimen` > `1.0773` → IC=+0.216 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0773 (IC base=+0.047)

- **PATRÓN** `volumen_pendiente_norm` > `0.3546` → IC=+0.384 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3546 (IC base=+0.047)

- **PATRÓN** `volumen_spike_ratio` > `3.7889` → IC=+0.303 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.7889 (IC base=+0.047)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.224 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 58.0 (IC base=+0.047)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `sigma_ewma_delta_pct` > `5.003` → IC=-0.209 (n=101)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.003
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=524)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.363` → IC=+0.175 (n=118)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 3.363 (IC base=-0.013)

- **PATRÓN** `volumen_pendiente_norm` > `0.1149` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1149 (IC base=-0.013)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `volumen_regimen` < `1.0528` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.0528 (IC base=+0.003)

- **PATRÓN** `volumen_regimen` < `0.5727` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.5727 (IC base=-0.005)

- **PATRÓN** `volumen_regimen` > `1.1078` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1078 (IC base=-0.005)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.281 (n=112)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0075 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.0628` → IC=+0.193 (n=112)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.0628 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.248 (n=161)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.096` → IC=+0.313 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.096 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` < `0.1441` → IC=+0.190 (n=237)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.1441 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.4263` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.4263 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` < `4.8756` → IC=+0.164 (n=254)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 4.8756 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `3.9033` → IC=+0.209 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.9033 (IC base=+0.181)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.199 (n=360)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.06 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `1909.8884` → IC=+0.214 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1909.8884 (IC base=+0.181)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.405 (n=103)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.364)

- **PATRÓN** `drift_60min` |x|≤ `0.1856` → IC=+0.367 (n=103)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1856 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.389 (n=142)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.364)

- **PATRÓN** `ibs_20min` < `0.3056` → IC=+0.378 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3056 (IC base=+0.364)

- **PATRÓN** `volumen_pendiente_norm` < `0.2282` → IC=+0.379 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2282 (IC base=+0.364)

- **PATRÓN** `volumen_pendiente_norm` > `0.1228` → IC=+0.389 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1228 (IC base=+0.364)

- **PATRÓN** `volumen_spike_ratio` < `2.9702` → IC=+0.430 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.9702 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `1859.1658` → IC=+0.406 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1859.1658 (IC base=+0.364)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `volumen_regimen` > `0.9213` → IC=-0.309 (n=19)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.9213
  - _Potencial_: sin este filtro IC_bueno=-0.109 (n=21)

- **FILTRO** `libro_liquidez` < `8591.1411` → IC=-0.195 (n=57)

  - _Acción_: SKIP cuando `libro_liquidez` < 8591.1411
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=171)

- **FILTRO** `volumen_regimen` > `0.8548` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8548
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=28)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.152 (n=44)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=677)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.4444` → IC=-0.140 (n=137)

  - _Acción_: SKIP cuando `ibs_20min` < 0.4444
  - _Potencial_: sin este filtro IC_bueno=+0.131 (n=139)

- **FILTRO** `dist_vwap_pct` > `0.1234` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1234
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=40)

- **FILTRO** `volumen_regimen` > `1.2342` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.2342
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=37)

- **PATRÓN** `ibs_20min` > `0.4444` → IC=+0.131 (n=139)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` > 0.4444 (IC base=-0.004)

- **PATRÓN** `dist_vwap_pct` > `0.1719` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1719 (IC base=-0.004)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.292 (n=99)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0066 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.0897` → IC=+0.147 (n=131)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.0897 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.140 (n=109)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 17.0 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.193 (n=99)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 5.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` > `0.9048` → IC=+0.219 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9048 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` > `0.312` → IC=+0.190 (n=56)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.312 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.516` → IC=+0.210 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.516 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` > `0.5938` → IC=+0.144 (n=296)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 0.5938 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.3138` → IC=+0.210 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3138 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=298)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `2465.9778` → IC=+0.132 (n=264)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2465.9778 (IC base=+0.129)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.280 (n=98)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.275)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.283 (n=261)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.275)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.313 (n=148)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.275)

- **PATRÓN** `ibs_20min` < `0.3125` → IC=+0.333 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3125 (IC base=+0.275)

- **PATRÓN** `dist_vwap_pct` > `0.5558` → IC=+0.357 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5558 (IC base=+0.275)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.387` → IC=+0.283 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.387 (IC base=+0.275)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.107` → IC=+0.277 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.107 (IC base=+0.275)

- **PATRÓN** `volumen_regimen` > `0.8997` → IC=+0.312 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8997 (IC base=+0.275)

- **PATRÓN** `volumen_pendiente_norm` > `0.2868` → IC=+0.362 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2868 (IC base=+0.275)

- **PATRÓN** `volumen_spike_ratio` > `3.7273` → IC=+0.296 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.7273 (IC base=+0.275)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.159 (n=406)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0047 (IC base=+0.140)

- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.198 (n=551)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0065 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.156 (n=548)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.9223` → IC=+0.259 (n=807)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9223 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.2154` → IC=+0.149 (n=260)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.2154 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.413` → IC=+0.247 (n=806)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.413 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `0.6258` → IC=+0.138 (n=627)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.6258 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.113` → IC=+0.163 (n=396)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.113 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.147 (n=1354)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.06 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `2653.0544` → IC=+0.172 (n=404)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2653.0544 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.222 (n=1174)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.3007` → IC=+0.220 (n=1174)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3007 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.272 (n=595)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` < `0.3724` → IC=+0.283 (n=1174)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3724 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.631` → IC=+0.237 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.631 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` > `0.8761` → IC=+0.206 (n=607)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8761 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.2708` → IC=+0.284 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2708 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` < `2.0525` → IC=+0.232 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0525 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `3.1879` → IC=+0.246 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.1879 (IC base=+0.214)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.248 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 96.0 (IC base=+0.214)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.160 (n=101)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0058 (IC base=+0.154)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.218 (n=101)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0076 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.209 (n=139)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.331 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.478` → IC=+0.358 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.478 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.1505` → IC=+0.152 (n=67)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.1505 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.08` → IC=+0.175 (n=327)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.08 (IC base=+0.154)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.288 (n=83)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.282)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.337 (n=41)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.282)

- **PATRÓN** `drift_60min` |x|≤ `0.2245` → IC=+0.318 (n=108)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2245 (IC base=+0.282)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.305 (n=126)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.282)

- **PATRÓN** `ibs_20min` < `0.0513` → IC=+0.407 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0513 (IC base=+0.282)

- **PATRÓN** `volumen_pendiente_norm` < `0.081` → IC=+0.308 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.081 (IC base=+0.282)

- **PATRÓN** `volumen_pendiente_norm` > `0.2197` → IC=+0.267 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2197 (IC base=+0.282)

- **PATRÓN** `volumen_spike_ratio` < `1.9432` → IC=+0.360 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9432 (IC base=+0.282)

- **PATRÓN** `volumen_spike_ratio` > `2.4332` → IC=+0.267 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4332 (IC base=+0.282)

- **PATRÓN** `libro_spread` < `0.08` → IC=+0.308 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.08 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `1933.4502` → IC=+0.337 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1933.4502 (IC base=+0.282)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0017` → IC=+0.265 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0017 (IC base=+0.213)

- **PATRÓN** `sigma_h` > `0.003` → IC=+0.261 (n=44)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.003 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.253 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `0.7674` → IC=+0.265 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7674 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` > `0.5248` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5248 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.011` → IC=+0.292 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.011 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` > `0.7493` → IC=+0.227 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7493 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.1033` → IC=+0.284 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1033 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `1.4774` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4774 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `1.9813` → IC=+0.245 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9813 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `11170.0615` → IC=+0.294 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11170.0615 (IC base=+0.213)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.200 (n=191)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.1928` → IC=+0.205 (n=191)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1928 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.255 (n=149)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` < `0.2977` → IC=+0.244 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2977 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.678` → IC=+0.278 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.678 (IC base=+0.190)

- **PATRÓN** `volumen_regimen` < `0.6392` → IC=+0.260 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6392 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.1352` → IC=+0.278 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1352 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` < `2.7301` → IC=+0.268 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.7301 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `11034.5851` → IC=+0.203 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11034.5851 (IC base=+0.190)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.188 (n=94)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0076 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.1472` → IC=+0.163 (n=188)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1472 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.179 (n=104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 16.0 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.206 (n=100)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.300 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.804` → IC=+0.338 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.804 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` < `0.2311` → IC=+0.132 (n=221)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` < 0.2311 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `2.0258` → IC=+0.200 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0258 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `3.9092` → IC=+0.141 (n=101)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 3.9092 (IC base=+0.152)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.202 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `1956.8086` → IC=+0.198 (n=94)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 1956.8086 (IC base=+0.152)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.325 (n=95)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.305)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.305 (n=126)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.305)

- **PATRÓN** `drift_60min` |x|≤ `0.1735` → IC=+0.366 (n=95)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1735 (IC base=+0.305)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.325 (n=95)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.305)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.303 (n=125)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.305)

- **PATRÓN** `ibs_20min` < `0.2421` → IC=+0.335 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2421 (IC base=+0.305)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.781` → IC=+0.348 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.781 (IC base=+0.305)

- **PATRÓN** `volumen_pendiente_norm` > `0.3308` → IC=+0.357 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3308 (IC base=+0.305)

- **PATRÓN** `volumen_spike_ratio` < `3.417` → IC=+0.308 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.417 (IC base=+0.305)

- **PATRÓN** `volumen_spike_ratio` > `6.1025` → IC=+0.300 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 6.1025 (IC base=+0.305)

- **PATRÓN** `libro_liquidez` > `1887.4151` → IC=+0.316 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1887.4151 (IC base=+0.305)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0021` → IC=+0.328 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0021 (IC base=+0.278)

- **PATRÓN** `sigma_h` > `0.0029` → IC=+0.300 (n=53)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0029 (IC base=+0.278)

- **PATRÓN** `drift_60min` |x|≤ `0.1726` → IC=+0.304 (n=54)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1726 (IC base=+0.278)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.298 (n=82)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.278)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.289 (n=74)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.278)

- **PATRÓN** `ibs_20min` > `0.8662` → IC=+0.338 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8662 (IC base=+0.278)

- **PATRÓN** `dist_vwap_pct` < `0.3189` → IC=+0.288 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3189 (IC base=+0.278)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.979` → IC=+0.429 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.979 (IC base=+0.278)

- **PATRÓN** `volumen_regimen` > `1.1756` → IC=+0.328 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1756 (IC base=+0.278)

- **PATRÓN** `volumen_pendiente_norm` > `0.1159` → IC=+0.314 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1159 (IC base=+0.278)

- **PATRÓN** `volumen_spike_ratio` < `1.632` → IC=+0.315 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.632 (IC base=+0.278)

- **PATRÓN** `volumen_spike_ratio` > `2.6068` → IC=+0.300 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6068 (IC base=+0.278)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.264 (n=142)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.194)

- **PATRÓN** `drift_60min` |x|≤ `0.1417` → IC=+0.201 (n=142)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1417 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.220 (n=212)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` < `0.314` → IC=+0.262 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.314 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.862` → IC=+0.267 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.862 (IC base=+0.194)

- **PATRÓN** `volumen_regimen` < `1.2379` → IC=+0.215 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2379 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` < `0.0843` → IC=+0.230 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0843 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.2357` → IC=+0.233 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2357 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` < `2.2674` → IC=+0.265 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2674 (IC base=+0.194)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **FILTRO** `ibs_20min` > `0.5833` → IC=-0.256 (n=76)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5833
  - _Potencial_: sin este filtro IC_bueno=+0.222 (n=235)

- **PATRÓN** `ibs_20min` > `0.8889` → IC=+0.185 (n=144)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.8889 (IC base=+0.035)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.984` → IC=+0.147 (n=131)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 2.984 (IC base=+0.035)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.214 (n=103)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.225 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.104)

- **PATRÓN** `ibs_20min` < `0.5833` → IC=+0.222 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5833 (IC base=+0.104)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.987` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.987 (IC base=+0.104)

- **PATRÓN** `volumen_regimen` > `0.8699` → IC=+0.146 (n=156)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.8699 (IC base=+0.104)

- **PATRÓN** `volumen_pendiente_norm` > `0.1257` → IC=+0.220 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1257 (IC base=+0.104)

- **PATRÓN** `volumen_spike_ratio` > `1.5628` → IC=+0.136 (n=105)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.5628 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `2364.9128` → IC=+0.200 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2364.9128 (IC base=+0.104)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.278 (n=79)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.2098` → IC=+0.133 (n=208)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.2098 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.173 (n=111)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 7.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.225 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `0.2825` → IC=+0.187 (n=65)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.2825 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.0626` → IC=+0.141 (n=168)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.0626 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.38` → IC=+0.227 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.38 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.1006` → IC=+0.139 (n=236)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.1006 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` > `0.6045` → IC=+0.126 (n=236)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.6045 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.3221` → IC=+0.179 (n=26)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.3221 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.5866` → IC=+0.152 (n=67)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.5866 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.126 (n=241)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2464.8952` → IC=+0.129 (n=211)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2464.8952 (IC base=+0.120)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.276 (n=221)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0063 (IC base=+0.264)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.270 (n=224)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.264)

- **PATRÓN** `drift_60min` |x|≤ `0.0834` → IC=+0.270 (n=85)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0834 (IC base=+0.264)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.278 (n=115)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.264)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.296 (n=96)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.264)

- **PATRÓN** `ibs_20min` < `0.3103` → IC=+0.306 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3103 (IC base=+0.264)

- **PATRÓN** `dist_vwap_pct` > `0.1675` → IC=+0.321 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1675 (IC base=+0.264)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.92` → IC=+0.296 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.92 (IC base=+0.264)

- **PATRÓN** `volumen_regimen` > `1.0872` → IC=+0.326 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0872 (IC base=+0.264)

- **PATRÓN** `volumen_pendiente_norm` > `0.2787` → IC=+0.357 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2787 (IC base=+0.264)

- **PATRÓN** `volumen_spike_ratio` > `3.805` → IC=+0.314 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.805 (IC base=+0.264)

- **PATRÓN** `libro_liquidez` > `2599.2247` → IC=+0.274 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2599.2247 (IC base=+0.264)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 30.0 (IC base=+0.264)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.195 (n=80)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 17.0 (IC base=+0.038)

- **PATRÓN** `ibs_20min` > `0.9824` → IC=+0.164 (n=102)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.9824 (IC base=+0.038)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.989` → IC=+0.247 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.989 (IC base=+0.038)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.280 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.042)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.859` → IC=+0.227 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.859 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` < `2.7938` → IC=+0.121 (n=101)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.7938 (IC base=+0.042)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=21)

- **FILTRO** `libro_liquidez` < `4949.0692` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_liquidez` < 4949.0692
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.257 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.1923` → IC=+0.190 (n=27)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.1923 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.210 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.2407` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2407 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.27` → IC=+0.357 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.27 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `1.218` → IC=+0.176 (n=35)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 1.218 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` > `0.7034` → IC=+0.176 (n=35)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.7034 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.091` → IC=+0.389 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.091 (IC base=+0.148)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0024` → IC=+0.237 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0024 (IC base=+0.231)

- **PATRÓN** `sigma_h` > `0.0027` → IC=+0.241 (n=25)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0027 (IC base=+0.231)

- **PATRÓN** `drift_60min` |x|≤ `0.2558` → IC=+0.250 (n=34)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2558 (IC base=+0.231)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.306 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.231)

- **PATRÓN** `ibs_20min` > `0.9601` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9601 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.738` → IC=+0.452 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.738 (IC base=+0.231)

- **PATRÓN** `volumen_regimen` < `0.9739` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9739 (IC base=+0.231)

- **PATRÓN** `volumen_regimen` > `1.0973` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0973 (IC base=+0.231)

- **PATRÓN** `volumen_pendiente_norm` > `0.1004` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1004 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` > `2.1374` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1374 (IC base=+0.231)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.326 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.103)

- **PATRÓN** `drift_60min` |x|≤ `0.3225` → IC=+0.167 (n=46)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.3225 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.227 (n=31)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.103)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.996` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.996 (IC base=+0.103)

- **PATRÓN** `volumen_regimen` < `0.6933` → IC=+0.283 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6933 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `9336.2451` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9336.2451 (IC base=+0.103)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` > `0.6852` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6852
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=61)

- **FILTRO** `dist_vwap_pct` > `0.19` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.19
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=65)

- **FILTRO** `volumen_pendiente_norm` > `0.1087` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1087
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=39)

- **FILTRO** `libro_liquidez` < `2536.4746` → IC=-0.154 (n=53)

  - _Acción_: SKIP cuando `libro_liquidez` < 2536.4746
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=28)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.144 (n=57)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 1.0 (IC base=+0.017)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.989` → IC=+0.188 (n=30)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 7.989 (IC base=+0.017)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.198 (n=501)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0068 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.148 (n=541)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 17.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.290 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `0.3273` → IC=+0.173 (n=151)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.3273 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.287` → IC=+0.231 (n=1002)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.287 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.1809` → IC=+0.135 (n=343)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.1809 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` > `1.6961` → IC=+0.123 (n=1056)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` > 1.6961 (IC base=+0.117)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.124 (n=1659)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.06 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2706.764` → IC=+0.147 (n=497)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 2706.764 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `155.0` → IC=+0.210 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 155.0 (IC base=+0.117)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.233 (n=1141)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.223)

- **PATRÓN** `sigma_h` > `0.0038` → IC=+0.230 (n=1296)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0038 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.250 (n=589)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` < `0.4925` → IC=+0.286 (n=1295)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4925 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` < `0.1489` → IC=+0.200 (n=879)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1489 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.069` → IC=+0.254 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.069 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.483` → IC=+0.223 (n=1216)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.483 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` < `0.6181` → IC=+0.209 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6181 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` > `1.0749` → IC=+0.225 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0749 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.1845` → IC=+0.273 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1845 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` < `1.6573` → IC=+0.274 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6573 (IC base=+0.223)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.219 (n=169)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.136 (n=369)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 6.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.159 (n=265)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 11.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.365` → IC=+0.354 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.365 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.1438` → IC=+0.129 (n=87)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` > 0.1438 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.177 (n=261)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.06 (IC base=+0.134)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.325 (n=61)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.295)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.325 (n=61)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.295)

- **PATRÓN** `drift_60min` |x|≤ `0.2138` → IC=+0.340 (n=160)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2138 (IC base=+0.295)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.302 (n=170)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.295)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.306 (n=168)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.295)

- **PATRÓN** `ibs_20min` < `0.5701` → IC=+0.342 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5701 (IC base=+0.295)

- **PATRÓN** `volumen_pendiente_norm` < `0.1103` → IC=+0.319 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1103 (IC base=+0.295)

- **PATRÓN** `volumen_spike_ratio` < `1.9246` → IC=+0.328 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9246 (IC base=+0.295)

- **PATRÓN** `volumen_spike_ratio` > `2.8455` → IC=+0.333 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8455 (IC base=+0.295)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.333 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.295)

- **PATRÓN** `libro_liquidez` > `1973.46` → IC=+0.341 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1973.46 (IC base=+0.295)

### GBM_LATE_15M_TARDIO#BTC#15min
- **FILTRO** `ibs_20min` < `0.2513` → IC=-0.214 (n=47)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2513
  - _Potencial_: sin este filtro IC_bueno=+0.240 (n=144)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.157 (n=97)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0027 (IC base=+0.127)

- **PATRÓN** `sigma_h` > `0.0031` → IC=+0.157 (n=65)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0031 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.202 (n=102)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.2513` → IC=+0.240 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2513 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.3501` → IC=+0.339 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3501 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.048` → IC=+0.245 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.048 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.6746` → IC=+0.160 (n=48)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.6746 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` > `1.1082` → IC=+0.172 (n=65)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 1.1082 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` < `0.1581` → IC=+0.186 (n=100)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.1581 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.1037` → IC=+0.182 (n=42)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.1037 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `2.9369` → IC=+0.240 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.9369 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `8789.4973` → IC=+0.246 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8789.4973 (IC base=+0.127)

- **PATRÓN** `sigma_h` < `0.0018` → IC=+0.205 (n=76)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0018 (IC base=+0.173)

- **PATRÓN** `sigma_h` > `0.0024` → IC=+0.178 (n=150)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0024 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.1874` → IC=+0.185 (n=195)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.1874 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.193 (n=223)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 6.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` < `0.4047` → IC=+0.223 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4047 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.258` → IC=+0.261 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.258 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `0.6183` → IC=+0.210 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6183 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `1.1277` → IC=+0.209 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1277 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.0953` → IC=+0.318 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0953 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` < `1.8705` → IC=+0.293 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8705 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `4894.1824` → IC=+0.185 (n=198)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 4894.1824 (IC base=+0.173)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.248 (n=101)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0075 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.239 (n=117)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.332 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.924` → IC=+0.354 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.924 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` < `0.1464` → IC=+0.170 (n=213)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` < 0.1464 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` < `1.9578` → IC=+0.158 (n=77)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.9578 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `4.1252` → IC=+0.173 (n=105)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 4.1252 (IC base=+0.172)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.192 (n=326)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.06 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `1915.5084` → IC=+0.193 (n=138)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 1915.5084 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.371 (n=83)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.273)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.275 (n=118)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.273)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.304 (n=100)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.273)

- **PATRÓN** `ibs_20min` < `0.5421` → IC=+0.335 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5421 (IC base=+0.273)

- **PATRÓN** `volumen_pendiente_norm` < `0.2348` → IC=+0.221 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2348 (IC base=+0.273)

- **PATRÓN** `volumen_pendiente_norm` > `0.3726` → IC=+0.308 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3726 (IC base=+0.273)

- **PATRÓN** `volumen_spike_ratio` < `1.7297` → IC=+0.295 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7297 (IC base=+0.273)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.295 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.273)

### GBM_LATE_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_20min` < `0.3253` → IC=-0.245 (n=49)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3253
  - _Potencial_: sin este filtro IC_bueno=+0.205 (n=147)

- **PATRÓN** `sigma_h` < `0.0019` → IC=+0.179 (n=51)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0019 (IC base=+0.091)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.154 (n=53)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.091)

- **PATRÓN** `ibs_20min` > `0.3253` → IC=+0.205 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3253 (IC base=+0.091)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.604` → IC=+0.214 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.604 (IC base=+0.091)

- **PATRÓN** `volumen_regimen` < `0.7759` → IC=+0.172 (n=65)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.7759 (IC base=+0.091)

- **PATRÓN** `volumen_pendiente_norm` > `0.2893` → IC=+0.318 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2893 (IC base=+0.091)

- **PATRÓN** `volumen_spike_ratio` > `1.9963` → IC=+0.250 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9963 (IC base=+0.091)

- **PATRÓN** `libro_liquidez` > `6581.0543` → IC=+0.239 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6581.0543 (IC base=+0.091)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.216 (n=100)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.0843` → IC=+0.174 (n=44)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0843 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.192 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 16.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` < `0.3` → IC=+0.244 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.1263` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1263 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.713` → IC=+0.271 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.713 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `0.8857` → IC=+0.200 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8857 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` < `0.0669` → IC=+0.337 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0669 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `2.2519` → IC=+0.271 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2519 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `1.6957` → IC=+0.318 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6957 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `5079.8508` → IC=+0.214 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5079.8508 (IC base=+0.142)

### GBM_LATE_15M_TARDIO#SOL#15min
- **FILTRO** `ibs_20min` < `0.5` → IC=-0.193 (n=73)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=237)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.230 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.013)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.923` → IC=+0.162 (n=137)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 2.923 (IC base=+0.013)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.210 (n=98)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.2773` → IC=+0.156 (n=193)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.2773 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.218 (n=101)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.5833` → IC=+0.247 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5833 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1737` → IC=+0.165 (n=177)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1737 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.427` → IC=+0.233 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.427 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.863` → IC=+0.147 (n=205)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 2.863 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.7176` → IC=+0.177 (n=97)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.7176 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `1.1028` → IC=+0.153 (n=99)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 1.1028 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` < `0.1535` → IC=+0.327 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1535 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.5635` → IC=+0.327 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5635 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `1354.4143` → IC=+0.253 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1354.4143 (IC base=+0.138)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.210 (n=98)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0066 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.0729` → IC=+0.193 (n=99)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.0729 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.181 (n=111)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 6.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.243 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` > `0.3125` → IC=+0.259 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3125 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.293` → IC=+0.218 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.293 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `1.1814` → IC=+0.130 (n=295)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1814 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` > `0.6753` → IC=+0.141 (n=263)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.6753 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.1933` → IC=+0.161 (n=60)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.1933 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `1.5848` → IC=+0.125 (n=246)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 1.5848 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=299)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `2587.3393` → IC=+0.131 (n=196)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2587.3393 (IC base=+0.129)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.294 (n=290)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.257)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.307 (n=164)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.257)

- **PATRÓN** `ibs_20min` < `0.1765` → IC=+0.374 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1765 (IC base=+0.257)

- **PATRÓN** `dist_vwap_pct` > `0.392` → IC=+0.372 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.392 (IC base=+0.257)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.368` → IC=+0.313 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.368 (IC base=+0.257)

- **PATRÓN** `volumen_regimen` > `1.2502` → IC=+0.321 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2502 (IC base=+0.257)

- **PATRÓN** `volumen_pendiente_norm` > `0.326` → IC=+0.357 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.326 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` < `1.5061` → IC=+0.241 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5061 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` > `2.6958` → IC=+0.267 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6958 (IC base=+0.257)

### GBM_LATE_5M
- **FILTRO** `sigma_h` < `0.0034` → IC=-0.182 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=41)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=45)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.156 (n=155)

- **PATRÓN** `drift_60min` |x|≤ `0.0923` → IC=+0.152 (n=21)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.0923 (IC base=-0.008)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.177 (n=128)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0039 (IC base=+0.122)

- **PATRÓN** `drift_60min` |x|≤ `0.0785` → IC=+0.211 (n=43)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0785 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.204 (n=52)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.3898` → IC=+0.135 (n=113)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.3898 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.363` → IC=+0.136 (n=42)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 9.363 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.074` → IC=+0.132 (n=112)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 6.074 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `1.4143` → IC=+0.146 (n=128)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.4143 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.2332` → IC=+0.154 (n=134)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.2332 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `3.1507` → IC=+0.167 (n=127)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 3.1507 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.156 (n=155)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `6919.3015` → IC=+0.169 (n=128)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 6919.3015 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `126.0` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 126.0 (IC base=+0.122)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` > `0.0021` → IC=+0.138 (n=78)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` > 0.0021 (IC base=+0.110)

- **PATRÓN** `drift_60min` |x|≤ `0.0673` → IC=+0.214 (n=26)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0673 (IC base=+0.110)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.200 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.110)

- **PATRÓN** `ibs_20min` < `0.1112` → IC=+0.148 (n=52)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.1112 (IC base=+0.110)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.318` → IC=+0.142 (n=65)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 6.318 (IC base=+0.110)

- **PATRÓN** `volumen_pendiente_norm` > `0.1646` → IC=+0.156 (n=30)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.1646 (IC base=+0.110)

- **PATRÓN** `volumen_spike_ratio` < `3.1655` → IC=+0.150 (n=78)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 3.1655 (IC base=+0.110)

- **PATRÓN** `volumen_spike_ratio` > `1.4653` → IC=+0.138 (n=78)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.4653 (IC base=+0.110)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `hora_utc` < `7.0` → IC=+0.340 (n=23)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.273)

- **PATRÓN** `ibs_20min` > `0.2032` → IC=+0.326 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2032 (IC base=+0.273)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.713` → IC=+0.308 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.713 (IC base=+0.273)

- **PATRÓN** `volumen_pendiente_norm` < `0.0872` → IC=+0.315 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0872 (IC base=+0.273)

- **PATRÓN** `libro_liquidez` > `7633.9254` → IC=+0.283 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7633.9254 (IC base=+0.273)

### GBM_LATE_60M
- **FILTRO** `ibs_20min` < `0.7083` → IC=-0.167 (n=52)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7083
  - _Potencial_: sin este filtro IC_bueno=+0.241 (n=106)

- **FILTRO** `drift_60min` |x|> `0.0945` → IC=-0.289 (n=17)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.0945
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=35)

- **FILTRO** `ibs_20min` > `0.6567` → IC=-0.263 (n=36)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6567
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=70)

- **FILTRO** `dist_vwap_pct` > `0.1008` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1008
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=49)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.178 (n=141)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0054 (IC base=+0.060)

- **PATRÓN** `drift_60min` |x|≤ `0.1223` → IC=+0.192 (n=37)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1223 (IC base=+0.060)

- **PATRÓN** `ibs_20min` > `0.9873` → IC=+0.315 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9873 (IC base=+0.060)

- **PATRÓN** `dist_vwap_pct` > `0.1247` → IC=+0.156 (n=62)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1247 (IC base=+0.060)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.949` → IC=+0.230 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.949 (IC base=+0.060)

- **PATRÓN** `volumen_regimen` > `1.0949` → IC=+0.191 (n=40)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 1.0949 (IC base=+0.060)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `1.0` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `ibs_20min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.293 (n=27)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.180 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=45)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.186 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=35)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.321 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.063)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.063)

- **PATRÓN** `dist_vwap_pct` > `0.1642` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1642 (IC base=+0.063)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `hora_utc` > `5.0` → IC=-0.360 (n=41)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=22)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.233 (n=28)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.095)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.361 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` < `0.1209` → IC=+0.204 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1209 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.138` → IC=+0.322 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.138 (IC base=+0.095)

- **PATRÓN** `volumen_regimen` < `0.8241` → IC=+0.176 (n=35)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.8241 (IC base=+0.095)

- **PATRÓN** `volumen_regimen` > `1.0919` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0919 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `2351.5975` → IC=+0.227 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2351.5975 (IC base=+0.095)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0165` → IC=-0.309 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0165
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=58)

- **FILTRO** `ibs_20min` > `0.2381` → IC=-0.308 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2381
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=12)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` > `0.0046` → IC=-0.300 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0046
  - _Potencial_: sin este filtro IC_bueno=-0.294 (n=71)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.423 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.212 (n=57)

- **FILTRO** `dist_vwap_pct` > `0.0767` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.0767
  - _Potencial_: sin este filtro IC_bueno=-0.287 (n=78)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.375 (n=22)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.263 (n=74)

- **FILTRO** `drift_60min` |x|> `0.1877` → IC=-0.292 (n=22)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1877
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=68)

- **FILTRO** `ibs_20min` < `0.3707` → IC=-0.308 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3707
  - _Potencial_: sin este filtro IC_bueno=-0.284 (n=72)

- **FILTRO** `dist_vwap_pct` > `0.3683` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3683
  - _Potencial_: sin este filtro IC_bueno=-0.275 (n=78)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.276 (n=74)

- **FILTRO** `libro_liquidez` < `1591.3597` → IC=-0.346 (n=24)

  - _Acción_: SKIP cuando `libro_liquidez` < 1591.3597
  - _Potencial_: sin este filtro IC_bueno=-0.270 (n=72)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `volumen_regimen` < `1.6138` → IC=-0.286 (n=26)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.6138
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `dist_vwap_pct` < `0.0931` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0931
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=13)

- **FILTRO** `libro_liquidez` < `4361.6218` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `libro_liquidez` < 4361.6218
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=20)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` < `9.988` → IC=-0.462 (n=24)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 9.988
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **FILTRO** `sigma_h` > `0.0018` → IC=-0.346 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0018
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `volumen_regimen` < `1.0086` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.0086
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.441 (n=15)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `ibs_20min` > `0.6061` → IC=+0.147 (n=131)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.6061 (IC base=+0.057)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.188 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 15.0 (IC base=+0.027)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6942` → IC=-0.333 (n=28)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6942
  - _Potencial_: sin este filtro IC_bueno=+0.177 (n=29)

- **FILTRO** `volumen_regimen` < `0.8896` → IC=-0.133 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8896
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=29)

- **PATRÓN** `ibs_20min` > `0.6942` → IC=+0.177 (n=29)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.6942 (IC base=-0.076)

- **PATRÓN** `drift_60min` |x|≤ `0.129` → IC=+0.167 (n=28)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.129 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.265 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.097)

- **PATRÓN** `ibs_20min` < `0.0252` → IC=+0.167 (n=31)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.0252 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.84` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 3.84 (IC base=+0.097)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **PATRÓN** `ibs_20min` > `0.9489` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9489 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.991` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.991 (IC base=+0.167)

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
- **PATRÓN** `py_entrada` < `0.505` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.505 (IC base=+0.176)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` < `0.505` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.505 (IC base=+0.176)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `17.0` → IC=-0.333 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=84)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
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
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=22)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.214 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.208 (n=22)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=20)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9732` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9732
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=60)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.204 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=55)

### MOMENTUM_IBS_15M
- **FILTRO** `hora_utc` < `14.0` → IC=-0.364 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=148)

- **PATRÓN** `drift_20min_pct` |x|≤ `0.0528` → IC=+0.167 (n=64)

  - _Acción_: Kelly boost +0.83€ cuando `drift_20min_pct` |x|≤ 0.0528 (IC base=+0.065)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2239.29` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 2239.29
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=15)

### MOMENTUM_IBS_15M#BTC#15min
- **PATRÓN** `hora_utc` < `5.0` → IC=+0.167 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 5.0 (IC base=+0.053)

- **PATRÓN** `ibs_20min` > `0.0888` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.0888 (IC base=+0.053)

### MOMENTUM_IBS_15M#ETH#15min
- **PATRÓN** `hora_utc` < `4.0` → IC=+0.200 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.148)

- **PATRÓN** `drift_20min_pct` |x|≤ `0.0609` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_20min_pct` |x|≤ 0.0609 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.06` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.06 (IC base=+0.148)

### MOMENTUM_IBS_15M#SOL#15min
- **FILTRO** `ibs_20min` > `0.9048` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `ibs_20min` > 0.9048
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=18)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `hora_utc` < `10.0` → IC=-0.120 (n=135)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=147)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.175 (n=124)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=158)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.153 (n=70)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=212)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.265 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=32)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=30)

- **FILTRO** `ibs_20min` < `0.8235` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8235
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=24)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=26)

- **FILTRO** `ballena_activa_n` > `34.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `ballena_activa_n` > 34.0
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=30)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.139 (n=34)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=21)

- **FILTRO** `ibs_20min` > `0.1545` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1545
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=37)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.133 (n=28)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=26)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.208 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.097)

- **PATRÓN** `drift_20min_pct` |x|≤ `0.1351` → IC=+0.141 (n=37)

  - _Acción_: Kelly boost +0.71€ cuando `drift_20min_pct` |x|≤ 0.1351 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `11300.9393` → IC=+0.192 (n=37)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 11300.9393 (IC base=+0.097)

### MOMENTUM_IBS_15M_BALLENA#SOL#15min
- **FILTRO** `ibs_20min` > `0.8571` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8571
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=25)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **PATRÓN** `py_entrada` > `0.505` → IC=+0.132 (n=17)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` > 0.505 (IC base=+0.000)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.132 (n=17)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` < 0.5 (IC base=+0.010)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `hora_utc` < `16.0` → IC=-0.300 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=88)

- **FILTRO** `hora_utc` > `19.0` → IC=-0.206 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=89)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=82)

- **FILTRO** `libro_liquidez` < `2575.3307` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 2575.3307
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=78)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `ibs_20min` < `0.9919` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `ibs_20min` < 0.9919
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `hora_utc` < `18.0` → IC=-0.333 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=11)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `ibs_20min` < `0.2368` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2368
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=6)

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
- **FILTRO** `hora_utc` < `10.0` → IC=-0.160 (n=377)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=403)

- **FILTRO** `py_entrada` < `0.38` → IC=-0.316 (n=194)

  - _Acción_: SKIP cuando `py_entrada` < 0.38
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=586)

- **FILTRO** `ibs_7min` < `0.7655` → IC=-0.246 (n=195)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7655
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=585)

- **FILTRO** `ballena_activa_n` > `20.0` → IC=-0.206 (n=192)

  - _Acción_: SKIP cuando `ballena_activa_n` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=588)

- **FILTRO** `libro_liquidez` < `3008.5956` → IC=-0.141 (n=514)

  - _Acción_: SKIP cuando `libro_liquidez` < 3008.5956
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=266)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.280 (n=175)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=535)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.211 (n=43)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=88)

- **FILTRO** `ballena_activa_n` > `2.0` → IC=-0.159 (n=89)

  - _Acción_: SKIP cuando `ballena_activa_n` > 2.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=42)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.214 (n=47)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=48)

- **FILTRO** `drift_7min_pct` |x|> `0.0876` → IC=-0.133 (n=47)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.0876
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=48)

- **PATRÓN** `py_entrada` < `0.53` → IC=+0.147 (n=32)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` < 0.53 (IC base=-0.057)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `5.0` → IC=-0.237 (n=36)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=134)

- **FILTRO** `py_entrada` < `0.4` → IC=-0.256 (n=39)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=131)

- **FILTRO** `ballena_activa_n` > `65.0` → IC=-0.155 (n=56)

  - _Acción_: SKIP cuando `ballena_activa_n` > 65.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=114)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.190 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=86)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.300 (n=28)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=85)

- **FILTRO** `drift_7min_pct` |x|> `0.0678` → IC=-0.186 (n=33)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.0678
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=80)

- **FILTRO** `ballena_activa_n` > `58.0` → IC=-0.250 (n=38)

  - _Acción_: SKIP cuando `ballena_activa_n` > 58.0
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=75)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `10.0` → IC=-0.185 (n=52)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=63)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.367 (n=28)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=87)

- **FILTRO** `ibs_7min` < `0.2222` → IC=-0.300 (n=28)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2222
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=87)

- **FILTRO** `libro_liquidez` < `2494.9356` → IC=-0.214 (n=75)

  - _Acción_: SKIP cuando `libro_liquidez` < 2494.9356
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=40)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.344 (n=30)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=95)

- **FILTRO** `ibs_7min` > `0.2736` → IC=-0.258 (n=31)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2736
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=94)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.222 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=81)

- **FILTRO** `py_entrada` < `0.4` → IC=-0.395 (n=36)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=79)

- **FILTRO** `ibs_7min` < `0.837` → IC=-0.300 (n=28)

  - _Acción_: SKIP cuando `ibs_7min` < 0.837
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=87)

- **FILTRO** `ballena_activa_n` > `29.0` → IC=-0.300 (n=28)

  - _Acción_: SKIP cuando `ballena_activa_n` > 29.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=87)

- **FILTRO** `libro_liquidez` < `8591.26` → IC=-0.175 (n=75)

  - _Acción_: SKIP cuando `libro_liquidez` < 8591.26
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=40)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.167 (n=73)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=42)

- **FILTRO** `ibs_7min` > `0.0812` → IC=-0.134 (n=39)

  - _Acción_: SKIP cuando `ibs_7min` > 0.0812
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=76)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.200 (n=38)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=100)

- **FILTRO** `py_entrada` < `0.46` → IC=-0.222 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=104)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.181 (n=67)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=71)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.250 (n=34)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=104)

- **PATRÓN** `libro_liquidez` > `4054.8826` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4054.8826 (IC base=+0.015)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.154 (n=53)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=58)

- **FILTRO** `py_entrada` < `0.38` → IC=-0.357 (n=26)

  - _Acción_: SKIP cuando `py_entrada` < 0.38
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=85)

- **FILTRO** `ibs_7min` < `0.7143` → IC=-0.328 (n=27)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7143
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=84)

- **FILTRO** `ballena_activa_n` > `18.0` → IC=-0.278 (n=25)

  - _Acción_: SKIP cuando `ballena_activa_n` > 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=86)

- **FILTRO** `libro_liquidez` < `3494.4084` → IC=-0.180 (n=73)

  - _Acción_: SKIP cuando `libro_liquidez` < 3494.4084
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=38)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.324 (n=32)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=102)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.144 (n=57)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.5 (IC base=-0.051)

- **PATRÓN** `libro_liquidez` > `2649.4846` → IC=+0.125 (n=46)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 2649.4846 (IC base=-0.051)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **PATRÓN** `ibs_7min` > `0.9355` → IC=+0.134 (n=91)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_7min` > 0.9355 (IC base=+0.055)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=60)

- **FILTRO** `libro_liquidez` < `10993.5371` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_liquidez` < 10993.5371
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=51)

### ORDER_FLOW_5M
- **FILTRO** `total_vol_5m` > `215.224` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `total_vol_5m` > 215.224
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `delta_ratio` |x|> `0.401` → IC=+0.149 (n=132)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.75€ cuando `delta_ratio` |x|> 0.401 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.141 (n=62)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 18.0 (IC base=+0.127)

- **PATRÓN** `total_vol_5m` < `389.535` → IC=+0.269 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 389.535 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.123 (n=51)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.127)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.2125` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.2125
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=38)

- **FILTRO** `pct_vs_K` |x|> `4.6307` → IC=-0.469 (n=30)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.6307
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=61)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0029` → IC=-0.350 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0029
  - _Potencial_: sin este filtro IC_bueno=+0.375 (n=14)

- **FILTRO** `T_h` > `87.9936` → IC=-0.423 (n=24)

  - _Acción_: SKIP cuando `T_h` > 87.9936
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=13)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0132` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0132
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `T_h` > `144.5498` → IC=-0.397 (n=27)

  - _Acción_: SKIP cuando `T_h` > 144.5498
  - _Potencial_: sin este filtro IC_bueno=-0.133 (n=28)

- **FILTRO** `sigma_h` > `0.0034` → IC=-0.333 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=14)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` > `0.0034` → IC=-0.324 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0034
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `T_h` > `95.1632` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `T_h` > 95.1632
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **FILTRO** `sigma_h` > `0.0033` → IC=-0.237 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=6)

### STREAK_FADE_15M
- **FILTRO** `streak_estiramiento` > `0.4411` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4411
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=6)

### STREAK_FADE_5M
- **FILTRO** `hora_utc` > `12.0` → IC=-0.150 (n=38)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=75)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=86)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.125 (n=38)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 4.0 (IC base=-0.013)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `4.0` → IC=-0.143 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `libro_liquidez` < `3627.5123` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `libro_liquidez` < 3627.5123
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=20)

- **FILTRO** `hora_utc` < `14.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` < 0.495 (IC base=-0.061)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `hora_utc` > `8.0` → IC=-0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=27)

- **FILTRO** `streak_estiramiento` > `0.644` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.644
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=33)

### STREAK_MOM_5M
- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=54)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `hora_utc` < `10.0` → IC=-0.214 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.182 (n=42)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=38)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.182 (n=42)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 10.0 (IC base=+0.056)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `py_entrada` < 0.495 (IC base=+0.056)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=64)

- **PATRÓN** `hora_utc` > `20.0` → IC=+0.184 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 20.0 (IC base=+0.009)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.208 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.105)

- **PATRÓN** `streak_len` < `3.0` → IC=+0.167 (n=64)

  - _Acción_: Kelly boost +0.83€ cuando `streak_len` < 3.0 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `3533.817` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 3533.817 (IC base=+0.105)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=673)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=372)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=380)

### UPDOWN_GBM#15min
- **FILTRO** `ibs_15` < `0.5676` → IC=-0.159 (n=136)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5676
  - _Potencial_: sin este filtro IC_bueno=+0.221 (n=278)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.122 (n=207)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` > 0.0047 (IC base=+0.096)

- **PATRÓN** `ibs_15` > `0.5676` → IC=+0.221 (n=278)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5676 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.4139` → IC=+0.182 (n=61)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.4139 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.021` → IC=+0.222 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.021 (IC base=+0.096)

- **PATRÓN** `ibs_15` < `0.5556` → IC=+0.121 (n=352)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.61€ cuando `ibs_15` < 0.5556 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` > `0.5656` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5656 (IC base=+0.071)

### UPDOWN_GBM#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0044` → IC=-0.150 (n=184)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0044
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=62)

- **FILTRO** `ibs_15` < `0.0909` → IC=-0.274 (n=60)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.0909
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=186)

- **FILTRO** `dist_vwap_pct` > `0.2843` → IC=-0.133 (n=47)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2843
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=179)

- **FILTRO** `sigma_ewma_delta_pct` > `5.384` → IC=-0.188 (n=62)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.384
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=184)

### UPDOWN_GBM#60min
- **FILTRO** `hora_utc` < `11.0` → IC=-0.269 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=126)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.0016` → IC=-0.200 (n=28)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0016
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=30)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.132 (n=74)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.03 (IC base=+0.000)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0298` → IC=-0.222 (n=16)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0298
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `libro_liquidez` < `12200.4416` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 12200.4416
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=6)

- **PATRÓN** `sigma_h` > `0.0021` → IC=+0.131 (n=63)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` > 0.0021 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.157 (n=68)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 4.0 (IC base=+0.115)

- **PATRÓN** `ibs_15` > `0.9375` → IC=+0.235 (n=32)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9375 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` > `0.3722` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3722 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` < `0.0966` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.0966 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `8349.505` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8349.505 (IC base=+0.115)

### UPDOWN_GBM#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1001` → IC=-0.206 (n=15)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1001
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

- **FILTRO** `ibs_15` < `0.0668` → IC=-0.324 (n=15)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.0668
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=16)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.805` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.805 (IC base=+0.051)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `ibs_15` < `0.9182` → IC=-0.150 (n=38)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.9182
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=21)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `ibs_15` < `0.7055` → IC=-0.138 (n=45)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.7055
  - _Potencial_: sin este filtro IC_bueno=+0.330 (n=45)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1329` → IC=+0.223 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1329 (IC base=+0.098)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.136 (n=31)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 6.0 (IC base=+0.098)

- **PATRÓN** `ibs_15` > `0.7055` → IC=+0.330 (n=45)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7055 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` < `0.0929` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0929 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.57` → IC=+0.188 (n=30)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 8.57 (IC base=+0.098)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.175 (n=78)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.005 (IC base=+0.150)

- **PATRÓN** `sigma_h` > `0.0042` → IC=+0.205 (n=59)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0042 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.4701` → IC=+0.159 (n=89)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.4701 (IC base=+0.150)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1143` → IC=+0.171 (n=80)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.85€ cuando `delta_ratio_macro` |x|> 0.1143 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.187 (n=65)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 12.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.155 (n=85)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 14.0 (IC base=+0.150)

- **PATRÓN** `ibs_15` < `0.3241` → IC=+0.181 (n=89)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.91€ cuando `ibs_15` < 0.3241 (IC base=+0.150)

- **PATRÓN** `ibs_15` > `0.0279` → IC=+0.192 (n=89)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.96€ cuando `ibs_15` > 0.0279 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1596` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1596 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `17.886` → IC=+0.207 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 17.886 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `10940.0688` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10940.0688 (IC base=+0.150)

### UPDOWN_GBM#ETH#5min
- **FILTRO** `ibs_15` < `0.0681` → IC=-0.200 (n=18)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.0681
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=37)

- **FILTRO** `dist_vwap_pct` > `0.1774` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1774
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=40)

- **FILTRO** `sigma_ewma_delta_pct` > `5.662` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.662
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=32)

- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.157 (n=33)

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.0283` → IC=+0.128 (n=49)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +0.64€ cuando `pct_spot_vs_ref` |x|≤ 0.0283 (IC base=+0.067)

- **PATRÓN** `sigma_h` < `0.0023` → IC=+0.184 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0023 (IC base=+0.067)

- **PATRÓN** `drift_60min` |x|≤ `0.1223` → IC=+0.184 (n=17)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1223 (IC base=+0.067)

- **PATRÓN** `drift_15min` |x|≤ `0.3343` → IC=+0.214 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3343 (IC base=+0.067)

- **PATRÓN** `hora_utc` < `2.0` → IC=+0.152 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 2.0 (IC base=+0.067)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.475` → IC=+0.125 (n=38)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` < 4.475 (IC base=+0.067)

- **PATRÓN** `ballena_activa_n` < `3.0` → IC=+0.157 (n=33)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 3.0 (IC base=+0.067)

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

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.239 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.071)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.125 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 12.0 (IC base=+0.071)

- **PATRÓN** `ibs_15` < `0.1154` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1154 (IC base=+0.071)

### UPDOWN_GBM#SOL#60min
- **FILTRO** `sigma_h` > `0.0061` → IC=-0.222 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0061
  - _Potencial_: sin este filtro IC_bueno=+0.237 (n=17)

- **FILTRO** `hora_utc` < `16.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=10)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.005` → IC=+0.163 (n=96)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.005 (IC base=+0.081)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0626` → IC=+0.133 (n=96)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio_macro` |x|> 0.0626 (IC base=+0.081)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.167 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 6.0 (IC base=+0.081)

- **PATRÓN** `ibs_15` > `0.4444` → IC=+0.153 (n=96)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.77€ cuando `ibs_15` > 0.4444 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` > `0.4266` → IC=+0.241 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4266 (IC base=+0.081)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.277` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.277 (IC base=+0.081)

- **PATRÓN** `libro_liquidez` > `2503.3208` → IC=+0.136 (n=86)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2503.3208 (IC base=+0.081)

- **PATRÓN** `drift_60min` |x|≤ `0.1583` → IC=+0.218 (n=37)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1583 (IC base=+0.095)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0971` → IC=+0.160 (n=98)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio_macro` |x|> 0.0971 (IC base=+0.095)

- **PATRÓN** `hora_utc` < `19.0` → IC=+0.132 (n=112)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 19.0 (IC base=+0.095)

- **PATRÓN** `ibs_15` < `0.234` → IC=+0.210 (n=74)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.234 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` > `0.1184` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1184 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.941` → IC=+0.134 (n=110)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 9.941 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `2524.7561` → IC=+0.134 (n=110)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2524.7561 (IC base=+0.095)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1958` → IC=+0.250 (n=70)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1958 (IC base=+0.238)

- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.284 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0022 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0031` → IC=+0.237 (n=36)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0031 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.1599` → IC=+0.264 (n=70)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1599 (IC base=+0.238)

- **PATRÓN** `drift_15min` |x|≤ `0.4081` → IC=+0.257 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4081 (IC base=+0.238)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2385` → IC=+0.259 (n=27)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2385 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.267 (n=28)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.257 (n=72)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.238)

- **PATRÓN** `ibs_15` > `0.7823` → IC=+0.308 (n=71)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7823 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` > `0.3445` → IC=+0.315 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3445 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` < `0.0842` → IC=+0.256 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0842 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.495` → IC=+0.276 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.495 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `3141.8886` → IC=+0.240 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3141.8886 (IC base=+0.238)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.2095` → IC=+0.241 (n=52)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.2095 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.241 (n=52)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.1567` → IC=+0.229 (n=46)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1567 (IC base=+0.204)

- **PATRÓN** `drift_15min` |x|≤ `0.4089` → IC=+0.260 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4089 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.236 (n=51)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.200 (n=48)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.204)

- **PATRÓN** `ibs_15` < `0.9942` → IC=+0.204 (n=52)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.9942 (IC base=+0.204)

- **PATRÓN** `ibs_15` > `0.7314` → IC=+0.241 (n=52)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7314 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `0.1936` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1936 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.854` → IC=+0.214 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.854 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` < `15.813` → IC=+0.217 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 15.813 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `6736.1852` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6736.1852 (IC base=+0.204)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `dist_vwap_pct` < `0.059` → IC=+0.342 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.059 (IC base=+0.289)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `ibs_15` < `0.5833` → IC=-0.273 (n=108)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5833
  - _Potencial_: sin este filtro IC_bueno=+0.255 (n=108)

- **FILTRO** `sigma_ewma_delta_pct` > `12.785` → IC=-0.153 (n=214)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 12.785
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=869)

- **PATRÓN** `ibs_15` > `0.5833` → IC=+0.255 (n=108)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5833 (IC base=-0.034)

- **PATRÓN** `ibs_15` < `0.2364` → IC=+0.306 (n=29)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2364 (IC base=-0.052)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.253 (n=79)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.154 (n=163)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.209 (n=53)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=189)

- **FILTRO** `sigma_ewma_delta_pct` < `9.186` → IC=-0.217 (n=136)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 9.186
  - _Potencial_: sin este filtro IC_bueno=-0.148 (n=106)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `drift_60min` |x|> `0.2095` → IC=-0.239 (n=21)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2095
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=64)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.0562` → IC=-0.196 (n=21)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.0562
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=64)

- **FILTRO** `ibs_15` < `0.4479` → IC=-0.386 (n=42)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.4479
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=43)

- **PATRÓN** `ibs_15` > `0.4479` → IC=+0.167 (n=43)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.83€ cuando `ibs_15` > 0.4479 (IC base=-0.109)

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.0411` → IC=+0.206 (n=15)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.0411 (IC base=+0.196)

- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.208 (n=22)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0045 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.260 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.196)

- **PATRÓN** `ibs_15` < `0.246` → IC=+0.340 (n=23)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.246 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.307` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 8.307 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `3786.4324` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3786.4324 (IC base=+0.196)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` > `13.898` → IC=-0.200 (n=58)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 13.898
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=328)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.749` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.749 (IC base=+0.008)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` < `0.0054` → IC=-0.134 (n=69)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0054
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=69)

- **FILTRO** `libro_liquidez` < `2519.5422` → IC=-0.160 (n=45)

  - _Acción_: SKIP cuando `libro_liquidez` < 2519.5422
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=93)

- **FILTRO** `sigma_ewma_delta_pct` > `7.938` → IC=-0.159 (n=83)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.938
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=272)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` > `0.0026` → IC=+0.261 (n=69)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0026 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.1815` → IC=+0.255 (n=104)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1815 (IC base=+0.243)

- **PATRÓN** `drift_15min` |x|≤ `0.6305` → IC=+0.255 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.6305 (IC base=+0.243)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0679` → IC=+0.264 (n=104)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0679 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.289 (n=93)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.243)

- **PATRÓN** `ibs_15` > `0.9358` → IC=+0.317 (n=69)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9358 (IC base=+0.243)

- **PATRÓN** `dist_vwap_pct` > `0.3632` → IC=+0.324 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3632 (IC base=+0.243)

- **PATRÓN** `dist_vwap_pct` < `0.0774` → IC=+0.290 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0774 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` > `14.106` → IC=+0.250 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 14.106 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.98` → IC=+0.250 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.98 (IC base=+0.243)

- **PATRÓN** `libro_liquidez` > `5195.5881` → IC=+0.246 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5195.5881 (IC base=+0.243)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.2049` → IC=+0.246 (n=65)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.2049 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.231 (n=65)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.227)

- **PATRÓN** `sigma_h` > `0.0022` → IC=+0.250 (n=58)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0022 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.1837` → IC=+0.261 (n=65)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1837 (IC base=+0.227)

- **PATRÓN** `drift_15min` |x|≤ `0.6592` → IC=+0.246 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.6592 (IC base=+0.227)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0911` → IC=+0.233 (n=58)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0911 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.283 (n=58)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.227)

- **PATRÓN** `ibs_15` < `0.9998` → IC=+0.231 (n=65)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.9998 (IC base=+0.227)

- **PATRÓN** `ibs_15` > `0.9362` → IC=+0.278 (n=43)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9362 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` > `0.3017` → IC=+0.357 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3017 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` < `0.0845` → IC=+0.289 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0845 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `27.672` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 27.672 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.438` → IC=+0.235 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.438 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `5427.2622` → IC=+0.256 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5427.2622 (IC base=+0.227)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.257 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.259)

- **PATRÓN** `sigma_h` > `0.0028` → IC=+0.284 (n=35)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0028 (IC base=+0.259)

- **PATRÓN** `drift_60min` |x|≤ `0.1478` → IC=+0.257 (n=35)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1478 (IC base=+0.259)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1879` → IC=+0.400 (n=18)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1879 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.300 (n=28)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.259)

- **PATRÓN** `ibs_15` > `0.9731` → IC=+0.400 (n=18)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9731 (IC base=+0.259)

- **PATRÓN** `dist_vwap_pct` < `0.0769` → IC=+0.308 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0769 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` < `16.209` → IC=+0.263 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 16.209 (IC base=+0.259)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.047` → IC=-0.180 (n=23)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.047
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

- **FILTRO** `sigma_h` > `0.0028` → IC=-0.196 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0028
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `drift_60min` |x|> `0.1471` → IC=-0.206 (n=15)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1471
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

### UPDOWN_OU_5M#DOGE#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1055` → IC=-0.289 (n=17)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1055
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.278 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2109` → IC=-0.265 (n=15)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2109
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

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
- **PATRÓN** `T_h` < `111.9997` → IC=+0.138 (n=56)

  - _Acción_: Kelly boost +0.69€ cuando `T_h` < 111.9997 (IC base=+0.004)

- **PATRÓN** `T_h` > `146.1132` → IC=+0.453 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1132 (IC base=+0.355)

- **PATRÓN** `ratio` > `1.016` → IC=+0.450 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.016 (IC base=+0.355)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` < `100.962` → IC=+0.343 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 100.962 (IC base=+0.281)

- **PATRÓN** `pct_dist` |x|≤ `0.6014` → IC=+0.276 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `pct_dist` |x|≤ 0.6014 (IC base=+0.281)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `111.9838` → IC=+0.328 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9838 (IC base=+0.318)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `135.9977` → IC=+0.440 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 135.9977 (IC base=+0.426)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#SOL#5min**: dentro de BUY_NO, IBS < 0.1154 sube el IC de +0.071 a +0.326 en UPDOWN_GBM#SOL#5min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5676 sube el IC de +0.096 a +0.221 en UPDOWN_GBM#15min (n=278). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.9375 sube el IC de +0.115 a +0.235 en UPDOWN_GBM#BTC#15min (n=32). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.7055 sube el IC de +0.098 a +0.330 en UPDOWN_GBM#ETH#15min (n=45). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_NO, IBS < 0.3241 sube el IC de +0.150 a +0.181 en UPDOWN_GBM#ETH#15min (n=89). Ya aplicado como kelly_boost=+0.91€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_NO, IBS > 0.0279 sube el IC de +0.150 a +0.192 en UPDOWN_GBM#ETH#15min (n=89). Ya aplicado como kelly_boost=+0.96€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.033 a +0.242 en UPDOWN_GBM#SOL#15min (n=29). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.4444 sube el IC de +0.081 a +0.153 en UPDOWN_GBM#XRP#15min (n=96). Ya aplicado como kelly_boost=+0.77€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.234 sube el IC de +0.095 a +0.210 en UPDOWN_GBM#XRP#15min (n=74). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.5833 sube el IC de -0.034 a +0.255 en UPDOWN_GBM_15M_TARDIO (n=108). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.2364 sube el IC de -0.052 a +0.306 en UPDOWN_GBM_15M_TARDIO (n=29). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.4479 sube el IC de -0.109 a +0.167 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=43). Ya aplicado como kelly_boost=+0.83€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.246 sube el IC de +0.196 a +0.340 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.9358 sube el IC de +0.243 a +0.317 en UPDOWN_GBM_IBS_ALTO (n=69). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS < 0.9998 sube el IC de +0.227 a +0.231 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=65). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.9362 sube el IC de +0.227 a +0.278 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=43). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.9731 sube el IC de +0.259 a +0.400 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=18). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7823 sube el IC de +0.238 a +0.308 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=71). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS < 0.9942 sube el IC de +0.204 a +0.204 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=52). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.7314 sube el IC de +0.204 a +0.241 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=52). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min` — IC=+0.289 n=36. Faltan ~4 resoluciones para umbral n≥40. ETA: ~3h.
- **LIVE-CANDIDATA**: `UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH` — IC=+0.289 n=36. Faltan ~4 resoluciones para umbral n≥40. ETA: ~3h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min` — IC=+0.427 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL` — IC=+0.427 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 485 | +0.044 | +36.60€ | 3 | 4 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 485 | +0.044 | +36.60€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 252 | +0.043 | +24.96€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 252 | +0.043 | +24.96€ | 2 | 4 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 208 | +0.024 | +0.48€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 208 | +0.024 | +0.48€ | 6 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 25 | +0.204 | +11.17€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 25 | +0.204 | +11.17€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 3245 | -0.114 | -500.24€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 447 | -0.012 | -7.56€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 2798 | -0.131 | -492.69€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 355 | -0.198 | -106.44€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 355 | -0.198 | -106.44€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 447 | -0.012 | -7.56€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 447 | -0.012 | -7.56€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 303 | -0.166 | -149.30€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 303 | -0.166 | -149.30€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 725 | -0.137 | -38.80€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 725 | -0.137 | -38.80€ | 2 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 774 | -0.006 | -89.24€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 774 | -0.006 | -89.24€ | 1 | 0 |
| 🚫 BALLENAS_TARDIAS#XRP | 641 | -0.218 | -108.91€ | 0 | 0 |
| 🚫 BALLENAS_TARDIAS#XRP#5min | 641 | -0.218 | -108.91€ | 1 | 0 |
| ✅ FAVORITO_CONFIRMADO | 13851 | +0.117 | -770.16€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 3314 | +0.181 | -112.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 98 | -0.100 | -46.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 7861 | +0.089 | -628.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 2578 | +0.131 | +18.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 1328 | +0.035 | -284.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 13 | -0.065 | -2.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 1311 | +0.038 | -276.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 3176 | +0.140 | -3.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 905 | +0.194 | -38.13€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 41 | -0.105 | -20.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 1311 | +0.112 | -9.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 919 | +0.140 | +64.73€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 1324 | +0.057 | -226.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 9 | -0.021 | -3.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 1314 | +0.058 | -220.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 3430 | +0.127 | -44.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 1223 | +0.160 | -25.12€ | 0 | 6 |
| 🚫 FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 1306 | +0.107 | -10.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 889 | +0.115 | -0.46€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 3271 | +0.137 | -192.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 1152 | +0.198 | -45.54€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 39 | +0.012 | -7.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 1310 | +0.085 | -92.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 770 | +0.139 | -46.23€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 1322 | +0.131 | -18.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 12 | +0.043 | +1.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 1309 | +0.132 | -19.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3392 | +0.163 | -311.66€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 3392 | +0.163 | -311.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 851 | +0.155 | -110.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 851 | +0.155 | -110.16€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 78 | -0.113 | -5.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 78 | -0.113 | -5.72€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 842 | +0.162 | -101.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 842 | +0.162 | -101.42€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 750 | +0.221 | -38.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 750 | +0.221 | -38.36€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 1 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 792 | +0.180 | -69.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 792 | +0.180 | -69.76€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 166 | +0.417 | -8.13€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 166 | +0.417 | -8.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 59 | +0.418 | -1.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 59 | +0.418 | -1.60€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 66 | +0.382 | -6.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 66 | +0.382 | -6.91€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 39 | +0.427 | +0.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 39 | +0.427 | +0.34€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 5599 | +0.196 | -474.20€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 5599 | +0.196 | -474.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 1049 | +0.102 | -229.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 1049 | +0.102 | -229.39€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 867 | +0.256 | +1.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 867 | +0.256 | +1.22€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 990 | +0.154 | -141.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 990 | +0.154 | -141.66€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 907 | +0.228 | -29.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 907 | +0.228 | -29.17€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 868 | +0.251 | -5.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 868 | +0.251 | -5.58€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 918 | +0.203 | -69.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 918 | +0.203 | -69.62€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1988 | +0.150 | +109.04€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 1988 | +0.150 | +109.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 985 | +0.154 | +63.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 985 | +0.154 | +63.42€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 1003 | +0.145 | +45.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 1003 | +0.145 | +45.62€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 529 | +0.297 | +0.20€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 529 | +0.297 | +0.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 222 | +0.268 | -12.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 222 | +0.268 | -12.38€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 247 | +0.299 | +6.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 247 | +0.299 | +6.12€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 60 | +0.371 | +6.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 60 | +0.371 | +6.46€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 221 | +0.406 | -12.05€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 221 | +0.406 | -12.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 99 | +0.401 | -6.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 99 | +0.401 | -6.24€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 98 | +0.410 | -5.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 98 | +0.410 | -5.95€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 24 | +0.346 | +0.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 24 | +0.346 | +0.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 242 | +0.262 | -26.60€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 242 | +0.262 | -26.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 242 | +0.262 | -26.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 242 | +0.262 | -26.60€ | 0 | 4 |
| ✅ GBM_LATE_15M | 4404 | +0.088 | +1563.58€ | 0 | 15 |
| ✅ GBM_LATE_15M#15min | 4404 | +0.088 | +1563.58€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 763 | +0.177 | +483.25€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 763 | +0.177 | +483.25€ | 0 | 18 |
| ✅ GBM_LATE_15M#BTC | 423 | +0.178 | +205.09€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 423 | +0.178 | +205.09€ | 0 | 22 |
| ✅ GBM_LATE_15M#DOGE | 768 | +0.192 | +527.55€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 768 | +0.192 | +527.55€ | 0 | 18 |
| ✅ GBM_LATE_15M#ETH | 593 | +0.001 | +37.24€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 593 | +0.001 | +37.24€ | 0 | 3 |
| ✅ GBM_LATE_15M#SOL | 831 | +0.007 | +76.83€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 831 | +0.007 | +76.83€ | 3 | 6 |
| ✅ GBM_LATE_15M#XRP | 1026 | +0.024 | +233.61€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 1026 | +0.024 | +233.61€ | 0 | 3 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 5420 | +0.051 | +1614.90€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 5420 | +0.051 | +1614.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 1040 | -0.028 | +189.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 1040 | -0.028 | +189.58€ | 1 | 2 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 1027 | -0.002 | +118.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 1027 | -0.002 | +118.47€ | 0 | 3 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 650 | +0.239 | +591.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 650 | +0.239 | +591.18€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 949 | -0.013 | +26.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 949 | -0.013 | +26.07€ | 4 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 971 | +0.004 | +90.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 971 | +0.004 | +90.04€ | 3 | 2 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 783 | +0.202 | +599.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 783 | +0.202 | +599.57€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 3177 | +0.176 | +2164.26€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 3177 | +0.176 | +2164.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 566 | +0.192 | +410.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 566 | +0.192 | +410.35€ | 0 | 18 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 415 | +0.198 | +278.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 415 | +0.198 | +278.66€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 563 | +0.204 | +442.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 563 | +0.204 | +442.82€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 388 | +0.218 | +298.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 388 | +0.218 | +298.93€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 599 | +0.071 | +237.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 599 | +0.071 | +237.13€ | 1 | 10 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 646 | +0.194 | +496.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 646 | +0.194 | +496.38€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 524 | +0.040 | +39.46€ | 0 | 6 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 524 | +0.040 | +39.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 92 | +0.043 | -4.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 92 | +0.043 | -4.74€ | 2 | 8 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 111 | +0.164 | +45.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 111 | +0.164 | +45.68€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 224 | -0.013 | +3.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 224 | -0.013 | +3.57€ | 4 | 2 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 97 | +0.015 | -5.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 97 | +0.015 | -5.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO | 3711 | +0.167 | +2370.29€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 3711 | +0.167 | +2370.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 734 | +0.188 | +516.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 734 | +0.188 | +516.22€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 486 | +0.156 | +259.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 486 | +0.156 | +259.78€ | 1 | 23 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 732 | +0.218 | +605.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 732 | +0.218 | +605.37€ | 0 | 17 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 328 | +0.112 | +124.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 328 | +0.112 | +124.94€ | 1 | 19 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 601 | +0.074 | +238.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 601 | +0.074 | +238.05€ | 1 | 14 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 830 | +0.197 | +625.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 830 | +0.197 | +625.93€ | 0 | 22 |
| ✅ GBM_LATE_5M | 231 | +0.088 | +58.30€ | 3 | 13 |
| ✅ GBM_LATE_5M#5min | 231 | +0.088 | +58.30€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 116 | +0.068 | +19.95€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 116 | +0.068 | +19.95€ | 0 | 8 |
| ✅ GBM_LATE_5M#ETH | 62 | +0.219 | +39.38€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 62 | +0.219 | +39.38€ | 0 | 5 |
| ✅ GBM_LATE_5M#SOL | 43 | -0.078 | -2.66€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 43 | -0.078 | -2.66€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP | 10 | +0.083 | +1.62€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 10 | +0.083 | +1.62€ | 0 | 0 |
| ✅ GBM_LATE_60M | 488 | -0.047 | +68.97€ | 4 | 6 |
| ✅ GBM_LATE_60M#60min | 488 | -0.047 | +68.97€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 169 | -0.003 | +6.56€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 169 | -0.003 | +6.56€ | 3 | 3 |
| ✅ GBM_LATE_60M#ETH | 172 | -0.029 | +35.38€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 172 | -0.029 | +35.38€ | 1 | 7 |
| ✅ GBM_LATE_60M#SOL | 147 | -0.117 | +27.03€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 147 | -0.117 | +27.03€ | 2 | 0 |
| 🚫 GBM_LATE_60M_FADE | 190 | -0.302 | -32.95€ | 9 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 190 | -0.302 | -32.95€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 75 | -0.253 | -6.85€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 75 | -0.253 | -6.85€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 64 | -0.348 | -18.54€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 64 | -0.348 | -18.54€ | 2 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 51 | -0.292 | -7.56€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 51 | -0.292 | -7.56€ | 2 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 301 | +0.045 | +7.57€ | 0 | 2 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 301 | +0.045 | +7.57€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 117 | +0.013 | +3.77€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 117 | +0.013 | +3.77€ | 2 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 68 | +0.114 | +7.11€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 68 | +0.114 | +7.11€ | 0 | 2 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 116 | +0.034 | -3.31€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 116 | +0.034 | -3.31€ | 1 | 5 |
| ✅ LEADLAG_BTC_XRP_15M | 51 | +0.160 | +15.58€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 51 | +0.160 | +15.58€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 51 | +0.160 | +15.58€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 51 | +0.160 | +15.58€ | 0 | 1 |
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
| ✅ LIQUIDACIONES_5M | 78 | -0.163 | -13.88€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 78 | -0.163 | -13.88€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 22 | -0.083 | -2.19€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 22 | -0.083 | -2.19€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE | 8 | -0.040 | -1.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 8 | -0.040 | -1.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 18 | -0.135 | -3.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 18 | -0.135 | -3.26€ | 0 | 0 |
| 🚫 LIQUIDACIONES_5M#SOL | 15 | -0.199 | -4.64€ | 0 | 0 |
| 🚫 LIQUIDACIONES_5M#SOL#5min | 15 | -0.199 | -4.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 14 | -0.131 | -3.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 14 | -0.131 | -3.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M | 292 | +0.010 | -2.81€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 292 | +0.010 | -2.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 99 | -0.005 | -7.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 99 | -0.005 | -7.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 94 | +0.010 | +0.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 94 | +0.010 | +0.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 99 | +0.025 | +3.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 99 | +0.025 | +3.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M | 421 | +0.032 | +3.49€ | 1 | 1 |
| ✅ MOMENTUM_IBS_15M#15min | 421 | +0.032 | +3.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 67 | +0.007 | -1.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 67 | +0.007 | -1.78€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 72 | +0.054 | +6.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 72 | +0.054 | +6.02€ | 0 | 2 |
| ✅ MOMENTUM_IBS_15M#DOGE | 65 | -0.022 | -11.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 65 | -0.022 | -11.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 76 | +0.103 | +19.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 76 | +0.103 | +19.68€ | 0 | 3 |
| ✅ MOMENTUM_IBS_15M#SOL | 71 | -0.021 | -9.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 71 | -0.021 | -9.96€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 70 | +0.056 | +0.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 70 | +0.056 | +0.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 576 | -0.016 | +7.18€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 576 | -0.016 | +7.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 91 | -0.005 | +21.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 91 | -0.005 | +21.13€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 100 | -0.039 | -6.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 100 | -0.039 | -6.53€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 95 | -0.015 | +5.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 95 | -0.015 | +5.90€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 97 | +0.035 | +2.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 97 | +0.035 | +2.08€ | 1 | 3 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 94 | -0.073 | -15.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 94 | -0.073 | -15.08€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 99 | +0.005 | -0.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 99 | +0.005 | -0.31€ | 0 | 2 |
| ✅ MOMENTUM_IBS_15M_FADE | 224 | -0.128 | -31.83€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 224 | -0.128 | -31.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 29 | -0.113 | -4.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 29 | -0.113 | -4.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 44 | -0.152 | -7.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 44 | -0.152 | -7.44€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 26 | -0.143 | -4.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 26 | -0.143 | -4.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 48 | -0.160 | -8.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 48 | -0.160 | -8.63€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 40 | -0.071 | -3.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 40 | -0.071 | -3.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 37 | -0.090 | -3.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 37 | -0.090 | -3.77€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 963 | +0.001 | -0.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 963 | +0.001 | -0.07€ | 0 | 0 |
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
| ✅ MOMENTUM_IBS_5M#XRP | 159 | -0.009 | -5.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 159 | -0.009 | -5.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 1490 | -0.081 | -46.57€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 1490 | -0.081 | -46.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 226 | -0.088 | -2.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 226 | -0.088 | -2.17€ | 4 | 1 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 283 | -0.075 | +69.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 283 | -0.075 | +69.93€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 240 | -0.095 | -40.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 240 | -0.095 | -40.10€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 230 | -0.116 | -39.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 230 | -0.116 | -39.10€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 266 | -0.037 | -4.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 266 | -0.037 | -4.01€ | 4 | 1 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 245 | -0.079 | -31.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 245 | -0.079 | -31.12€ | 6 | 2 |
| ✅ MOMENTUM_IBS_5M_FADE | 1447 | +0.018 | +8.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 1447 | +0.018 | +8.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 246 | +0.032 | +10.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 246 | +0.032 | +10.99€ | 0 | 1 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 211 | +0.035 | +0.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 211 | +0.035 | +0.17€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 249 | +0.006 | -1.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 249 | +0.006 | -1.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 250 | +0.012 | +0.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 250 | +0.012 | +0.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 254 | +0.012 | +0.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 254 | +0.012 | +0.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 237 | +0.011 | -2.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 237 | +0.011 | -2.55€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 213 | +0.072 | +31.71€ | 1 | 4 |
| ✅ ORDER_FLOW_5M#5min | 77 | +0.095 | +19.11€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 18 | +0.225 | +16.68€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 18 | +0.225 | +16.68€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE | 15 | +0.022 | +1.28€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 15 | +0.022 | +1.28€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL | 21 | +0.022 | -0.97€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 21 | +0.022 | -0.97€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP | 19 | +0.023 | -0.72€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 19 | +0.023 | -0.72€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 215 | -0.131 | -6.45€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 87 | -0.174 | -18.74€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 74 | -0.184 | -15.78€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 13 | -0.065 | -2.96€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 86 | -0.136 | -1.92€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 71 | -0.144 | -3.15€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 15 | -0.066 | +1.23€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 42 | -0.023 | +14.21€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 37 | +0.013 | +15.46€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 5 | -0.054 | -1.25€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 182 | -0.130 | -3.47€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 33 | -0.129 | -2.99€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 109 | -0.275 | -25.44€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 45 | -0.202 | -6.50€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 43 | -0.189 | -5.48€ | 1 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 49 | -0.265 | -11.29€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 47 | -0.255 | -10.27€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 15 | -0.331 | -7.65€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#atexpiry | 14 | -0.306 | -7.14€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 104 | -0.264 | -22.89€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 5 | -0.089 | -2.55€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 48 | +0.240 | +4.75€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC | 17 | -0.022 | -2.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 17 | -0.022 | -2.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 15 | +0.199 | +1.27€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 15 | +0.199 | +1.27€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 16 | +0.356 | +6.43€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 16 | +0.356 | +6.43€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 48 | +0.240 | +4.75€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 45 | -0.117 | -12.16€ | 1 | 0 |
| ✅ STREAK_FADE_15M#15min | 45 | -0.117 | -12.16€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 18 | -0.045 | -4.15€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 18 | -0.045 | -4.15€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 22 | -0.125 | -5.80€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 22 | -0.125 | -5.80€ | 0 | 0 |
| ✅ STREAK_FADE_5M | 333 | -0.022 | -19.03€ | 2 | 1 |
| ✅ STREAK_FADE_5M#5min | 333 | -0.022 | -19.03€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 80 | +0.049 | +3.69€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 80 | +0.049 | +3.69€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 114 | -0.009 | -6.55€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 114 | -0.009 | -6.55€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 62 | -0.094 | -9.24€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 62 | -0.094 | -9.24€ | 2 | 1 |
| ✅ STREAK_FADE_5M#XRP | 77 | -0.057 | -6.93€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 77 | -0.057 | -6.93€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 15 | -0.066 | -1.71€ | 0 | 0 |
| ✅ STREAK_FADE_60M#60min | 15 | -0.066 | -1.71€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 9 | -0.061 | -1.63€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 9 | -0.061 | -1.63€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 566 | +0.026 | +7.63€ | 1 | 0 |
| ✅ STREAK_MOM_5M#5min | 566 | +0.026 | +7.63€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 171 | -0.003 | -4.68€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 171 | -0.003 | -4.68€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 115 | -0.004 | -1.76€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 115 | -0.004 | -1.76€ | 2 | 2 |
| ✅ STREAK_MOM_5M#SOL | 148 | +0.047 | +4.51€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 148 | +0.047 | +4.51€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP | 132 | +0.067 | +9.57€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 132 | +0.067 | +9.57€ | 1 | 4 |
| ✅ STRUCT_NO_15M | 1809 | +0.013 | -8.77€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 1809 | +0.013 | -8.77€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 692 | +0.006 | -8.84€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 692 | +0.006 | -8.84€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 713 | +0.018 | -0.40€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 713 | +0.018 | -0.40€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 404 | +0.017 | +0.47€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 404 | +0.017 | +0.47€ | 2 | 0 |
| ✅ UPDOWN_GBM | 2025 | +0.018 | +87.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 881 | +0.083 | +141.88€ | 1 | 6 |
| ✅ UPDOWN_GBM#240min | 116 | +0.009 | -1.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 735 | -0.030 | -42.08€ | 4 | 0 |
| ✅ UPDOWN_GBM#60min | 246 | -0.024 | -10.64€ | 2 | 1 |
| ✅ UPDOWN_GBM#BNB | 85 | +0.075 | +12.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 78 | +0.100 | +13.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 6 | -0.075 | -2.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 362 | -0.003 | -10.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 118 | +0.050 | -4.61€ | 2 | 6 |
| ✅ UPDOWN_GBM#BTC#240min | 34 | +0.056 | +1.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 107 | -0.005 | +0.43€ | 2 | 1 |
| ✅ UPDOWN_GBM#BTC#60min | 85 | -0.063 | -9.73€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 294 | -0.003 | -4.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 58 | +0.100 | +10.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 236 | -0.029 | -15.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 475 | +0.051 | +43.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 208 | +0.129 | +51.25€ | 1 | 16 |
| ✅ UPDOWN_GBM#ETH#240min | 35 | +0.041 | +0.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 120 | -0.008 | -6.10€ | 4 | 7 |
| ✅ UPDOWN_GBM#ETH#60min | 97 | +0.005 | -1.72€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 356 | -0.008 | +0.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 146 | +0.013 | +1.11€ | 1 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 29 | -0.016 | -0.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 105 | -0.005 | -0.85€ | 2 | 3 |
| ✅ UPDOWN_GBM#SOL#60min | 64 | -0.015 | +0.81€ | 2 | 0 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 451 | +0.023 | +48.93€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 273 | +0.089 | +69.58€ | 0 | 14 |
| ✅ UPDOWN_GBM#XRP#240min | 17 | -0.112 | -2.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 161 | -0.071 | -17.75€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 105 | +0.238 | -4.25€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 105 | +0.238 | -4.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 69 | +0.204 | -10.17€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 69 | +0.204 | -10.17€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 36 | +0.289 | +5.92€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 36 | +0.289 | +5.92€ | 0 | 1 |
| ✅ UPDOWN_GBM_15M_TARDIO | 1587 | -0.046 | +164.13€ | 2 | 2 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 1587 | -0.046 | +164.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 102 | -0.077 | -4.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 102 | -0.077 | -4.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 316 | -0.132 | -6.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 316 | -0.132 | -6.59€ | 3 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 39 | -0.012 | +0.96€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 39 | -0.012 | +0.96€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 129 | -0.004 | +19.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 129 | -0.004 | +19.46€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 508 | -0.010 | +92.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 508 | -0.010 | +92.84€ | 1 | 1 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 493 | -0.035 | +61.66€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 493 | -0.035 | +61.66€ | 3 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 8 | -0.040 | -1.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 8 | -0.040 | -1.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 8 | -0.040 | -1.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 8 | -0.040 | -1.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 138 | +0.243 | +61.48€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 138 | +0.243 | +61.48€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 86 | +0.227 | +29.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 86 | +0.227 | +29.79€ | 0 | 14 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 52 | +0.259 | +31.69€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 52 | +0.259 | +31.69€ | 0 | 8 |
| ✅ UPDOWN_OU_5M | 337 | -0.063 | -27.16€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#5min | 337 | -0.063 | -27.16€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 215 | -0.007 | -10.98€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 215 | -0.007 | -10.98€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 17 | +0.067 | +3.83€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 17 | +0.067 | +3.83€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#DOGE | 24 | -0.231 | -6.15€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#DOGE#5min | 24 | -0.231 | -6.15€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 28 | -0.167 | -4.42€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 28 | -0.167 | -4.42€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 28 | -0.200 | -4.70€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 28 | -0.200 | -4.70€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 25 | -0.167 | -4.74€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 25 | -0.167 | -4.74€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 910 | +0.285 | +386.45€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 270 | +0.199 | +8.22€ | 0 | 2 |
| ✅ WEEKLY_PRICE#ETH | 289 | +0.256 | +69.14€ | 0 | 1 |
| ✅ WEEKLY_PRICE#SOL | 351 | +0.372 | +309.10€ | 0 | 1 |