# Hipótesis automáticas — 2026-08-18 11:35 UTC
_Generado por shadow_postmortem.py sobre 62392 resoluciones (PNL=+6417.92€)_

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
- **FILTRO** `restante_s_al_confirmar` < `145.56` → IC=-0.263 (n=820)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 145.56
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=2462)

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
- **FILTRO** `n_ballenas` < `4.0` → IC=-0.149 (n=186)

  - _Acción_: SKIP cuando `n_ballenas` < 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.124 (n=570)

- **FILTRO** `restante_s_al_confirmar` < `244.14` → IC=-0.155 (n=567)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 244.14
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=189)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `140.27` → IC=-0.196 (n=192)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 140.27
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=579)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `158.17` → IC=-0.270 (n=159)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 158.17
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=480)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.7` → IC=+0.207 (n=2143)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.7 (IC base=+0.098)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.164 (n=1146)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `2373.5135` → IC=+0.166 (n=1109)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2373.5135 (IC base=+0.098)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.152 (n=3652)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 7.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.152 (n=2857)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 11.0 (IC base=+0.148)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.282 (n=1350)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.186 (n=1975)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.02 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `4022.4162` → IC=+0.173 (n=800)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 4022.4162 (IC base=+0.148)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.206 (n=352)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` > `0.775` → IC=+0.354 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.775 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.201 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.224 (n=295)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.327 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.194 (n=423)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.192)

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
- **PATRÓN** `hora_utc` < `11.0` → IC=+0.149 (n=459)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 11.0 (IC base=+0.114)

- **PATRÓN** `py_entrada` > `0.7` → IC=+0.303 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.7 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.304 (n=258)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.286)

- **PATRÓN** `py_entrada` < `0.195` → IC=+0.395 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.195 (IC base=+0.286)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.290 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `3301.4437` → IC=+0.347 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3301.4437 (IC base=+0.286)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.180 (n=555)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.189 (n=477)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 15.0 (IC base=+0.176)

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

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.183 (n=955)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` < 0.7 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.204 (n=896)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `3268.7028` → IC=+0.348 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3268.7028 (IC base=+0.183)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.163 (n=589)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 15.0 (IC base=+0.155)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.176 (n=587)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.73 (IC base=+0.155)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.155 (n=606)

  - _Acción_: Kelly boost +0.77€ cuando `py_entrada` > 0.71 (IC base=+0.155)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.223 (n=579)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.235 (n=512)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.313 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.222)

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
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.439 (n=112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.416)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.421 (n=112)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.416)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.422 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.416)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.456 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.416)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.414 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.416)

- **PATRÓN** `libro_liquidez` > `3351.8902` → IC=+0.432 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3351.8902 (IC base=+0.416)

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
- **PATRÓN** `py_entrada` < `0.925` → IC=+0.409 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.925 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.413 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.425)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.204 (n=1422)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.203 (n=1528)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.254 (n=1455)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` < `10.0` → IC=+0.126 (n=532)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 10.0 (IC base=+0.102)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.138 (n=382)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` > 0.73 (IC base=+0.102)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `16.0` → IC=+0.300 (n=248)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.256)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.265 (n=236)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.256)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.339 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.256)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` < `7.0` → IC=+0.167 (n=367)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 7.0 (IC base=+0.154)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.220 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.154)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.240 (n=494)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.229)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.229 (n=703)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.229)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.297 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.229)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.261 (n=220)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.251)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.265 (n=228)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.251)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.285 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.251)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.255 (n=231)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.207 (n=469)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.258 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.205)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.227 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.149)

- **PATRÓN** `restante_min` < `3.8` → IC=+0.159 (n=500)

  - _Acción_: Kelly boost +0.80€ cuando `restante_min` < 3.8 (IC base=+0.149)

- **PATRÓN** `restante_min` > `4.91` → IC=+0.204 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `restante_min` > 4.91 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.156 (n=1335)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 7.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.156 (n=1535)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 17.0 (IC base=+0.149)

- **PATRÓN** `lag_apertura_s` < `5.45` → IC=+0.213 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `lag_apertura_s` < 5.45 (IC base=+0.149)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.239 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.154)

- **PATRÓN** `restante_min` < `3.72` → IC=+0.169 (n=246)

  - _Acción_: Kelly boost +0.85€ cuando `restante_min` < 3.72 (IC base=+0.154)

- **PATRÓN** `restante_min` > `4.88` → IC=+0.191 (n=260)

  - _Acción_: Kelly boost +0.95€ cuando `restante_min` > 4.88 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=757)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.166 (n=677)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 15.0 (IC base=+0.154)

- **PATRÓN** `lag_apertura_s` < `7.37` → IC=+0.191 (n=247)

  - _Acción_: Kelly boost +0.95€ cuando `lag_apertura_s` < 7.37 (IC base=+0.154)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.43` → IC=+0.177 (n=669)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.43 (IC base=+0.143)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.219 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `restante_min` > 4.95 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.149 (n=671)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.153 (n=776)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 17.0 (IC base=+0.143)

- **PATRÓN** `lag_apertura_s` < `3.18` → IC=+0.223 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `lag_apertura_s` < 3.18 (IC base=+0.143)

- **PATRÓN** `profundidad_ratio_no` > `13.6` → IC=+0.175 (n=250)

  - _Acción_: Kelly boost +0.87€ cuando `profundidad_ratio_no` > 13.6 (IC base=+0.143)

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
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.286 (n=129)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.261)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.421 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.261)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.279 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.261)

- **PATRÓN** `libro_liquidez` > `1406.0028` → IC=+0.309 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1406.0028 (IC base=+0.261)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.286 (n=129)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.261)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.421 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.261)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.279 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.261)

- **PATRÓN** `libro_liquidez` > `1406.0028` → IC=+0.309 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1406.0028 (IC base=+0.261)

### GBM_LATE_15M
- **PATRÓN** `hora_utc` < `6.0` → IC=+0.148 (n=441)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 6.0 (IC base=+0.108)

- **PATRÓN** `ibs_20min` > `0.9943` → IC=+0.277 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9943 (IC base=+0.108)

- **PATRÓN** `dist_vwap_pct` > `0.5682` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5682 (IC base=+0.108)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.835` → IC=+0.244 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.835 (IC base=+0.108)

- **PATRÓN** `volumen_regimen` < `1.313` → IC=+0.235 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.313 (IC base=+0.108)

- **PATRÓN** `volumen_regimen` > `0.7541` → IC=+0.241 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7541 (IC base=+0.108)

- **PATRÓN** `volumen_pendiente_norm` > `0.3253` → IC=+0.177 (n=94)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.3253 (IC base=+0.108)

- **PATRÓN** `volumen_spike_ratio` > `1.6927` → IC=+0.131 (n=597)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 1.6927 (IC base=+0.108)

- **PATRÓN** `ibs_20min` < `0.6597` → IC=+0.122 (n=2099)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.6597 (IC base=+0.077)

- **PATRÓN** `volumen_regimen` < `0.6291` → IC=+0.148 (n=157)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.6291 (IC base=+0.077)

- **PATRÓN** `volumen_regimen` > `0.6936` → IC=+0.138 (n=421)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.6936 (IC base=+0.077)

- **PATRÓN** `volumen_pendiente_norm` > `0.0892` → IC=+0.274 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0892 (IC base=+0.077)

- **PATRÓN** `volumen_spike_ratio` < `1.576` → IC=+0.238 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.576 (IC base=+0.077)

- **PATRÓN** `volumen_spike_ratio` > `2.9145` → IC=+0.232 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9145 (IC base=+0.077)

- **PATRÓN** `ballena_activa_n` < `245.0` → IC=+0.250 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 245.0 (IC base=+0.077)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.178 (n=175)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.007 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.191 (n=147)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 6.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.577` → IC=+0.347 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.577 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2139` → IC=+0.139 (n=59)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.2139 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.170 (n=277)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.06 (IC base=+0.125)

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
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.279)

- **PATRÓN** `drift_60min` |x|≤ `0.0858` → IC=+0.308 (n=76)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0858 (IC base=+0.279)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.286 (n=232)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.279)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.307 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.279)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.108` → IC=+0.306 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.108 (IC base=+0.279)

- **PATRÓN** `volumen_pendiente_norm` > `0.4178` → IC=+0.405 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.4178 (IC base=+0.279)

- **PATRÓN** `volumen_spike_ratio` < `2.0427` → IC=+0.271 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0427 (IC base=+0.279)

- **PATRÓN** `volumen_spike_ratio` > `3.1342` → IC=+0.246 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.1342 (IC base=+0.279)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.283 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.279)

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

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.7863 (IC base=-0.006)

- **PATRÓN** `volumen_regimen` < `0.6973` → IC=+0.274 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6973 (IC base=+0.038)

- **PATRÓN** `volumen_regimen` > `1.3677` → IC=+0.225 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.3677 (IC base=+0.038)

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

- **PATRÓN** `volumen_regimen` > `1.0767` → IC=+0.211 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0767 (IC base=+0.047)

- **PATRÓN** `volumen_pendiente_norm` > `0.3516` → IC=+0.384 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3516 (IC base=+0.047)

- **PATRÓN** `volumen_spike_ratio` > `3.7886` → IC=+0.303 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.7886 (IC base=+0.047)

- **PATRÓN** `ballena_activa_n` < `61.0` → IC=+0.219 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 61.0 (IC base=+0.047)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `sigma_ewma_delta_pct` > `5.003` → IC=-0.209 (n=101)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.003
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=523)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.413` → IC=+0.172 (n=117)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 3.413 (IC base=-0.014)

- **PATRÓN** `volumen_pendiente_norm` > `0.1149` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1149 (IC base=-0.014)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `volumen_regimen` < `1.0528` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.0528 (IC base=+0.003)

- **PATRÓN** `volumen_regimen` < `0.5727` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.5727 (IC base=-0.004)

- **PATRÓN** `volumen_regimen` > `1.1078` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1078 (IC base=-0.004)

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

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.404 (n=102)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.363)

- **PATRÓN** `drift_60min` |x|≤ `0.1856` → IC=+0.365 (n=102)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1856 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.388 (n=141)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.363)

- **PATRÓN** `ibs_20min` < `0.3009` → IC=+0.384 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3009 (IC base=+0.363)

- **PATRÓN** `volumen_pendiente_norm` < `0.3211` → IC=+0.377 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.3211 (IC base=+0.363)

- **PATRÓN** `volumen_pendiente_norm` > `0.1228` → IC=+0.389 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1228 (IC base=+0.363)

- **PATRÓN** `volumen_spike_ratio` < `2.9764` → IC=+0.430 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.9764 (IC base=+0.363)

- **PATRÓN** `libro_liquidez` > `1857.661` → IC=+0.406 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1857.661 (IC base=+0.363)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `volumen_regimen` > `0.9213` → IC=-0.309 (n=19)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.9213
  - _Potencial_: sin este filtro IC_bueno=-0.109 (n=21)

- **FILTRO** `libro_liquidez` < `8587.8262` → IC=-0.207 (n=56)

  - _Acción_: SKIP cuando `libro_liquidez` < 8587.8262
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=171)

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
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.274)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.282 (n=260)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.274)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.313 (n=148)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.274)

- **PATRÓN** `ibs_20min` < `0.3125` → IC=+0.333 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3125 (IC base=+0.274)

- **PATRÓN** `dist_vwap_pct` > `0.5772` → IC=+0.357 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5772 (IC base=+0.274)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.387` → IC=+0.283 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.387 (IC base=+0.274)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.107` → IC=+0.276 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.107 (IC base=+0.274)

- **PATRÓN** `volumen_regimen` > `0.8997` → IC=+0.311 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8997 (IC base=+0.274)

- **PATRÓN** `volumen_pendiente_norm` > `0.2868` → IC=+0.362 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2868 (IC base=+0.274)

- **PATRÓN** `volumen_spike_ratio` > `3.6746` → IC=+0.296 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.6746 (IC base=+0.274)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.159 (n=406)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0047 (IC base=+0.139)

- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.198 (n=550)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0065 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.156 (n=548)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.9223` → IC=+0.259 (n=806)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9223 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.2154` → IC=+0.149 (n=260)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.2154 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.418` → IC=+0.247 (n=806)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.418 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `0.6258` → IC=+0.138 (n=627)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.6258 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.1135` → IC=+0.163 (n=395)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.1135 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.147 (n=1353)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.06 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `2654.5546` → IC=+0.172 (n=403)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2654.5546 (IC base=+0.139)

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
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0058 (IC base=+0.153)

- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.218 (n=101)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0075 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.209 (n=139)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.330 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.482` → IC=+0.357 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.482 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.2097` → IC=+0.160 (n=48)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.2097 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.08` → IC=+0.174 (n=326)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.08 (IC base=+0.153)

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
- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.197 (n=500)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0068 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.148 (n=541)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 17.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.290 (n=626)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `0.3273` → IC=+0.173 (n=151)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.3273 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.29` → IC=+0.231 (n=1002)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.29 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.1809` → IC=+0.135 (n=343)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.1809 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` > `1.6961` → IC=+0.123 (n=1056)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` > 1.6961 (IC base=+0.117)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.124 (n=1658)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.06 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2708.8088` → IC=+0.147 (n=496)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 2708.8088 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `114.0` → IC=+0.213 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 114.0 (IC base=+0.117)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.234 (n=1139)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.223)

- **PATRÓN** `sigma_h` > `0.0038` → IC=+0.229 (n=1294)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0038 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.250 (n=589)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` < `0.4925` → IC=+0.286 (n=1294)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4925 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` < `0.1489` → IC=+0.200 (n=879)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1489 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.067` → IC=+0.254 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.067 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.483` → IC=+0.223 (n=1214)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.483 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` < `0.618` → IC=+0.208 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.618 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` > `1.0749` → IC=+0.224 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0749 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.1845` → IC=+0.273 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1845 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` < `1.6485` → IC=+0.273 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6485 (IC base=+0.223)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.218 (n=168)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.158 (n=264)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 11.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.301 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.422` → IC=+0.360 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.422 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.1442` → IC=+0.129 (n=87)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` > 0.1442 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.176 (n=260)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.06 (IC base=+0.133)

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

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.369 (n=82)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.272)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.275 (n=118)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.272)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.321 (n=82)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.272)

- **PATRÓN** `ibs_20min` < `0.5385` → IC=+0.335 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5385 (IC base=+0.272)

- **PATRÓN** `volumen_pendiente_norm` < `0.2348` → IC=+0.219 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2348 (IC base=+0.272)

- **PATRÓN** `volumen_pendiente_norm` > `0.3726` → IC=+0.308 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3726 (IC base=+0.272)

- **PATRÓN** `volumen_spike_ratio` < `1.7297` → IC=+0.295 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7297 (IC base=+0.272)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.293 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.272)

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

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.297 (n=289)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.256)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.307 (n=164)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.256)

- **PATRÓN** `ibs_20min` < `0.175` → IC=+0.373 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.175 (IC base=+0.256)

- **PATRÓN** `dist_vwap_pct` > `0.392` → IC=+0.372 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.392 (IC base=+0.256)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.348` → IC=+0.313 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.348 (IC base=+0.256)

- **PATRÓN** `volumen_regimen` > `1.2406` → IC=+0.321 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2406 (IC base=+0.256)

- **PATRÓN** `volumen_pendiente_norm` > `0.2728` → IC=+0.350 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2728 (IC base=+0.256)

- **PATRÓN** `volumen_spike_ratio` < `1.5061` → IC=+0.241 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5061 (IC base=+0.256)

- **PATRÓN** `volumen_spike_ratio` > `2.6744` → IC=+0.253 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6744 (IC base=+0.256)

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
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=154)

- **PATRÓN** `drift_60min` |x|≤ `0.0923` → IC=+0.152 (n=21)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.0923 (IC base=-0.008)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.174 (n=127)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0039 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.0785` → IC=+0.211 (n=43)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0785 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.204 (n=52)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.498` → IC=+0.136 (n=127)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.498 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.363` → IC=+0.136 (n=42)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 9.363 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.046` → IC=+0.134 (n=110)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 6.046 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.4143` → IC=+0.143 (n=127)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.4143 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.2396` → IC=+0.147 (n=134)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.2396 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `2.5735` → IC=+0.181 (n=111)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 2.5735 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=154)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `6919.3015` → IC=+0.167 (n=127)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 6919.3015 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `126.0` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 126.0 (IC base=+0.120)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` > `0.0021` → IC=+0.133 (n=77)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` > 0.0021 (IC base=+0.106)

- **PATRÓN** `drift_60min` |x|≤ `0.0673` → IC=+0.214 (n=26)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0673 (IC base=+0.106)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.200 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.106)

- **PATRÓN** `ibs_20min` < `0.1112` → IC=+0.148 (n=52)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.1112 (IC base=+0.106)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.318` → IC=+0.136 (n=64)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 6.318 (IC base=+0.106)

- **PATRÓN** `volumen_pendiente_norm` > `0.1646` → IC=+0.156 (n=30)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.1646 (IC base=+0.106)

- **PATRÓN** `volumen_spike_ratio` < `3.1655` → IC=+0.146 (n=77)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 3.1655 (IC base=+0.106)

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
- **FILTRO** `ibs_20min` < `0.6544` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6544
  - _Potencial_: sin este filtro IC_bueno=+0.198 (n=41)

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
- **PATRÓN** `py_entrada` < `0.505` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.505 (IC base=+0.167)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` < `0.505` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.505 (IC base=+0.167)

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

- **PATRÓN** `drift_20min_pct` |x|≤ `0.0528` → IC=+0.162 (n=63)

  - _Acción_: Kelly boost +0.81€ cuando `drift_20min_pct` |x|≤ 0.0528 (IC base=+0.065)

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
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.141)

- **PATRÓN** `drift_20min_pct` |x|≤ `0.0609` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_20min_pct` |x|≤ 0.0609 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.1322` → IC=+0.167 (n=34)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.1322 (IC base=+0.141)

### MOMENTUM_IBS_15M#SOL#15min
- **FILTRO** `ibs_20min` > `0.9048` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `ibs_20min` > 0.9048
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=18)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `hora_utc` < `10.0` → IC=-0.120 (n=135)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=141)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.180 (n=120)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=156)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.157 (n=68)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=208)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.265 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=31)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=30)

- **FILTRO** `ibs_20min` < `0.8235` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8235
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=23)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=25)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.139 (n=34)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=21)

- **FILTRO** `ibs_20min` > `0.1545` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1545
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=37)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=27)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `py_entrada` > 0.5 (IC base=+0.000)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=26)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.222 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.089)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.5 (IC base=+0.089)

- **PATRÓN** `drift_20min_pct` |x|≤ `0.1351` → IC=+0.132 (n=36)

  - _Acción_: Kelly boost +0.66€ cuando `drift_20min_pct` |x|≤ 0.1351 (IC base=+0.089)

- **PATRÓN** `libro_liquidez` > `11243.3198` → IC=+0.192 (n=37)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 11243.3198 (IC base=+0.089)

### MOMENTUM_IBS_15M_BALLENA#SOL#15min
- **FILTRO** `ibs_20min` > `0.88` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `ibs_20min` > 0.88
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=26)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **PATRÓN** `py_entrada` > `0.505` → IC=+0.132 (n=17)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` > 0.505 (IC base=+0.010)

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
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=383)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.324 (n=180)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=580)

- **FILTRO** `ibs_7min` < `0.76` → IC=-0.240 (n=190)

  - _Acción_: SKIP cuando `ibs_7min` < 0.76
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=570)

- **FILTRO** `ballena_activa_n` > `21.0` → IC=-0.213 (n=186)

  - _Acción_: SKIP cuando `ballena_activa_n` > 21.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=574)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.284 (n=169)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=527)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.204 (n=42)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=86)

- **FILTRO** `ballena_activa_n` > `2.0` → IC=-0.156 (n=88)

  - _Acción_: SKIP cuando `ballena_activa_n` > 2.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=40)

- **FILTRO** `py_entrada` > `0.54` → IC=-0.177 (n=60)

  - _Acción_: SKIP cuando `py_entrada` > 0.54
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=34)

- **PATRÓN** `py_entrada` < `0.54` → IC=+0.167 (n=34)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.54 (IC base=-0.052)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `5.0` → IC=-0.237 (n=36)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=130)

- **FILTRO** `py_entrada` < `0.4` → IC=-0.256 (n=39)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=127)

- **FILTRO** `ibs_7min` < `0.8501` → IC=-0.174 (n=41)

  - _Acción_: SKIP cuando `ibs_7min` < 0.8501
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=125)

- **FILTRO** `ballena_activa_n` > `65.0` → IC=-0.155 (n=56)

  - _Acción_: SKIP cuando `ballena_activa_n` > 65.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=110)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.179 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=86)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.293 (n=27)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=85)

- **FILTRO** `drift_7min_pct` |x|> `0.0678` → IC=-0.186 (n=33)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.0678
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=79)

- **FILTRO** `ballena_activa_n` > `57.0` → IC=-0.250 (n=38)

  - _Acción_: SKIP cuando `ballena_activa_n` > 57.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=74)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `10.0` → IC=-0.185 (n=52)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=61)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.367 (n=28)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=85)

- **FILTRO** `ibs_7min` < `0.2222` → IC=-0.300 (n=28)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2222
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=85)

- **FILTRO** `libro_liquidez` < `2496.9172` → IC=-0.210 (n=74)

  - _Acción_: SKIP cuando `libro_liquidez` < 2496.9172
  - _Potencial_: sin este filtro IC_bueno=+0.134 (n=39)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.339 (n=29)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=94)

- **FILTRO** `ibs_7min` > `0.2771` → IC=-0.250 (n=30)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2771
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=93)

- **PATRÓN** `libro_liquidez` > `2496.9172` → IC=+0.134 (n=39)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2496.9172 (IC base=-0.091)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.222 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=78)

- **FILTRO** `py_entrada` < `0.4` → IC=-0.392 (n=35)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=77)

- **FILTRO** `ibs_7min` < `0.837` → IC=-0.300 (n=28)

  - _Acción_: SKIP cuando `ibs_7min` < 0.837
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=84)

- **FILTRO** `ballena_activa_n` > `29.0` → IC=-0.293 (n=27)

  - _Acción_: SKIP cuando `ballena_activa_n` > 29.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=85)

- **FILTRO** `libro_liquidez` < `8699.3721` → IC=-0.180 (n=73)

  - _Acción_: SKIP cuando `libro_liquidez` < 8699.3721
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=39)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.176 (n=69)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=42)

- **FILTRO** `ibs_7min` > `0.1656` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `ibs_7min` > 0.1656
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=84)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.200 (n=38)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=94)

- **FILTRO** `py_entrada` < `0.45` → IC=-0.243 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=99)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.181 (n=67)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=65)

- **FILTRO** `ballena_activa_n` > `16.0` → IC=-0.258 (n=31)

  - _Acción_: SKIP cuando `ballena_activa_n` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=101)

- **PATRÓN** `libro_liquidez` > `4054.8826` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4054.8826 (IC base=+0.020)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.154 (n=53)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=56)

- **FILTRO** `py_entrada` < `0.38` → IC=-0.357 (n=26)

  - _Acción_: SKIP cuando `py_entrada` < 0.38
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=83)

- **FILTRO** `ibs_7min` < `0.7143` → IC=-0.328 (n=27)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7143
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=82)

- **FILTRO** `ballena_activa_n` > `18.0` → IC=-0.278 (n=25)

  - _Acción_: SKIP cuando `ballena_activa_n` > 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=84)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.300 (n=43)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=88)

- **FILTRO** `ibs_7min` > `0.2792` → IC=-0.176 (n=32)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2792
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=99)

- **FILTRO** `libro_liquidez` < `2790.9578` → IC=-0.159 (n=86)

  - _Acción_: SKIP cuando `libro_liquidez` < 2790.9578
  - _Potencial_: sin este filtro IC_bueno=+0.138 (n=45)

- **PATRÓN** `py_entrada` < `0.52` → IC=+0.123 (n=67)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.52 (IC base=-0.056)

- **PATRÓN** `libro_liquidez` > `2790.9578` → IC=+0.138 (n=45)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2790.9578 (IC base=-0.056)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **PATRÓN** `ibs_7min` > `0.9327` → IC=+0.133 (n=88)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_7min` > 0.9327 (IC base=+0.051)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=57)

- **FILTRO** `libro_liquidez` < `10993.3675` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `libro_liquidez` < 10993.3675
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=49)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `libro_liquidez` < `9404.1511` → IC=-0.132 (n=55)

  - _Acción_: SKIP cuando `libro_liquidez` < 9404.1511
  - _Potencial_: sin este filtro IC_bueno=+0.172 (n=56)

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

### STREAK_FADE_5M
- **FILTRO** `hora_utc` > `12.0` → IC=-0.150 (n=38)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=74)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=85)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.125 (n=38)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 4.0 (IC base=-0.018)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `5.0` → IC=-0.154 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=13)

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
  - _Potencial_: sin este filtro IC_bueno=+0.162 (n=63)

- **PATRÓN** `hora_utc` > `20.0` → IC=+0.184 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 20.0 (IC base=+0.009)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.208 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.100)

- **PATRÓN** `streak_len` < `3.0` → IC=+0.162 (n=63)

  - _Acción_: Kelly boost +0.81€ cuando `streak_len` < 3.0 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `3533.817` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 3533.817 (IC base=+0.100)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=672)

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
  - _Acción_: Kelly boost +0.61€ cuando `ibs_15` < 0.5556 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.5656` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5656 (IC base=+0.070)

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
  - _Potencial_: sin este filtro IC_bueno=+0.176 (n=32)

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.0283` → IC=+0.128 (n=49)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +0.64€ cuando `pct_spot_vs_ref` |x|≤ 0.0283 (IC base=+0.076)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.157 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0031 (IC base=+0.076)

- **PATRÓN** `drift_60min` |x|≤ `0.1223` → IC=+0.184 (n=17)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1223 (IC base=+0.076)

- **PATRÓN** `drift_15min` |x|≤ `0.3343` → IC=+0.214 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3343 (IC base=+0.076)

- **PATRÓN** `hora_utc` < `2.0` → IC=+0.152 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 2.0 (IC base=+0.076)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.475` → IC=+0.141 (n=37)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.475 (IC base=+0.076)

- **PATRÓN** `ballena_activa_n` < `3.0` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 3.0 (IC base=+0.076)

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

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.227 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.081)

- **PATRÓN** `drift_15min` |x|≤ `0.2122` → IC=+0.136 (n=20)

  - _Acción_: Kelly boost +0.68€ cuando `drift_15min` |x|≤ 0.2122 (IC base=+0.081)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2912` → IC=+0.156 (n=30)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.78€ cuando `delta_ratio_macro` |x|> 0.2912 (IC base=+0.081)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.130 (n=44)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 8.0 (IC base=+0.081)

- **PATRÓN** `ibs_15` < `0.1` → IC=+0.364 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1 (IC base=+0.081)

- **PATRÓN** `libro_liquidez` > `4112.971` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4112.971 (IC base=+0.081)

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
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1583 (IC base=+0.092)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0943` → IC=+0.150 (n=98)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.75€ cuando `delta_ratio_macro` |x|> 0.0943 (IC base=+0.092)

- **PATRÓN** `hora_utc` < `19.0` → IC=+0.128 (n=111)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 19.0 (IC base=+0.092)

- **PATRÓN** `ibs_15` < `0.2258` → IC=+0.207 (n=73)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2258 (IC base=+0.092)

- **PATRÓN** `dist_vwap_pct` > `0.1184` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1184 (IC base=+0.092)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.858` → IC=+0.134 (n=110)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 9.858 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `2524.7561` → IC=+0.131 (n=109)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2524.7561 (IC base=+0.092)

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

- **FILTRO** `sigma_h` < `0.0042` → IC=-0.158 (n=270)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0042
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=811)

- **FILTRO** `sigma_ewma_delta_pct` > `12.766` → IC=-0.156 (n=213)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 12.766
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=868)

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
- **FILTRO** `sigma_ewma_delta_pct` > `13.855` → IC=-0.195 (n=57)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 13.855
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

- **FILTRO** `sigma_ewma_delta_pct` > `4.857` → IC=-0.152 (n=113)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.857
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=241)

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

- **H-IBS-UPDOWN_GBM#SOL#5min**: dentro de BUY_NO, IBS < 0.1 sube el IC de +0.081 a +0.364 en UPDOWN_GBM#SOL#5min (n=20). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5676 sube el IC de +0.096 a +0.221 en UPDOWN_GBM#15min (n=278). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.9375 sube el IC de +0.115 a +0.235 en UPDOWN_GBM#BTC#15min (n=32). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.7055 sube el IC de +0.098 a +0.330 en UPDOWN_GBM#ETH#15min (n=45). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_NO, IBS < 0.3241 sube el IC de +0.150 a +0.181 en UPDOWN_GBM#ETH#15min (n=89). Ya aplicado como kelly_boost=+0.91€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_NO, IBS > 0.0279 sube el IC de +0.150 a +0.192 en UPDOWN_GBM#ETH#15min (n=89). Ya aplicado como kelly_boost=+0.96€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.033 a +0.242 en UPDOWN_GBM#SOL#15min (n=29). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.4444 sube el IC de +0.081 a +0.153 en UPDOWN_GBM#XRP#15min (n=96). Ya aplicado como kelly_boost=+0.77€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.2258 sube el IC de +0.092 a +0.207 en UPDOWN_GBM#XRP#15min (n=73). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
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
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min` — IC=+0.425 n=38. Faltan ~2 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL` — IC=+0.425 n=38. Faltan ~2 resoluciones para umbral n≥40. ETA: ~1h.

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
| ✅ BALLENAS_TARDIAS | 3240 | -0.115 | -498.99€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 447 | -0.012 | -7.56€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 2793 | -0.131 | -491.43€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 355 | -0.198 | -106.44€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 355 | -0.198 | -106.44€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 447 | -0.012 | -7.56€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 447 | -0.012 | -7.56€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 303 | -0.166 | -149.30€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 303 | -0.166 | -149.30€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 725 | -0.137 | -38.80€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 725 | -0.137 | -38.80€ | 2 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 771 | -0.008 | -90.13€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 771 | -0.008 | -90.13€ | 1 | 0 |
| 🚫 BALLENAS_TARDIAS#XRP | 639 | -0.218 | -106.77€ | 0 | 0 |
| 🚫 BALLENAS_TARDIAS#XRP#5min | 639 | -0.218 | -106.77€ | 1 | 0 |
| ✅ FAVORITO_CONFIRMADO | 13820 | +0.117 | -770.10€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 3310 | +0.181 | -111.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 98 | -0.100 | -46.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 7834 | +0.088 | -629.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 2578 | +0.131 | +18.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 1324 | +0.035 | -285.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 13 | -0.065 | -2.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 1307 | +0.038 | -277.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 3171 | +0.140 | -1.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 904 | +0.194 | -36.09€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 41 | -0.105 | -20.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 1307 | +0.111 | -9.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 919 | +0.140 | +64.73€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 1320 | +0.056 | -227.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 9 | -0.021 | -3.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 1310 | +0.057 | -221.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 3424 | +0.127 | -47.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 1221 | +0.161 | -25.42€ | 0 | 6 |
| 🚫 FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 1302 | +0.106 | -13.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 889 | +0.115 | -0.46€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 3264 | +0.137 | -189.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 1151 | +0.197 | -46.21€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 39 | +0.012 | -7.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 1304 | +0.086 | -89.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 770 | +0.139 | -46.23€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 1317 | +0.131 | -18.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 12 | +0.043 | +1.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 1304 | +0.132 | -18.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3390 | +0.163 | -311.02€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 3390 | +0.163 | -311.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 850 | +0.155 | -110.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 850 | +0.155 | -110.59€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 78 | -0.113 | -5.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 78 | -0.113 | -5.72€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 842 | +0.162 | -101.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 842 | +0.162 | -101.42€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 749 | +0.222 | -37.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 749 | +0.222 | -37.28€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 1 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 792 | +0.180 | -69.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 792 | +0.180 | -69.76€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 165 | +0.416 | -8.29€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 165 | +0.416 | -8.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 59 | +0.418 | -1.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 59 | +0.418 | -1.60€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 66 | +0.382 | -6.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 66 | +0.382 | -6.91€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 38 | +0.425 | +0.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 38 | +0.425 | +0.18€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 5580 | +0.196 | -469.39€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 5580 | +0.196 | -469.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 1048 | +0.102 | -229.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 1048 | +0.102 | -229.63€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 864 | +0.256 | +1.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 864 | +0.256 | +1.76€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 987 | +0.154 | -141.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 987 | +0.154 | -141.43€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 904 | +0.229 | -28.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 904 | +0.229 | -28.76€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 863 | +0.251 | -4.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 863 | +0.251 | -4.49€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 914 | +0.205 | -66.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 914 | +0.205 | -66.84€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1981 | +0.149 | +105.68€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 1981 | +0.149 | +105.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 982 | +0.154 | +63.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 982 | +0.154 | +63.12€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 999 | +0.143 | +42.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 999 | +0.143 | +42.56€ | 0 | 6 |
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
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 241 | +0.261 | -26.76€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 241 | +0.261 | -26.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 241 | +0.261 | -26.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 241 | +0.261 | -26.76€ | 0 | 4 |
| ✅ GBM_LATE_15M | 4399 | +0.088 | +1560.23€ | 0 | 15 |
| ✅ GBM_LATE_15M#15min | 4399 | +0.088 | +1560.23€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 762 | +0.177 | +481.13€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 762 | +0.177 | +481.13€ | 0 | 18 |
| ✅ GBM_LATE_15M#BTC | 423 | +0.178 | +205.09€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 423 | +0.178 | +205.09€ | 0 | 22 |
| ✅ GBM_LATE_15M#DOGE | 767 | +0.192 | +525.63€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 767 | +0.192 | +525.63€ | 0 | 18 |
| ✅ GBM_LATE_15M#ETH | 593 | +0.001 | +37.24€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 593 | +0.001 | +37.24€ | 0 | 3 |
| ✅ GBM_LATE_15M#SOL | 830 | +0.007 | +77.91€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 830 | +0.007 | +77.91€ | 3 | 6 |
| ✅ GBM_LATE_15M#XRP | 1024 | +0.024 | +233.24€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 1024 | +0.024 | +233.24€ | 0 | 3 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 5414 | +0.051 | +1611.73€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 5414 | +0.051 | +1611.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 1038 | -0.028 | +188.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 1038 | -0.028 | +188.10€ | 1 | 2 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 1026 | -0.002 | +119.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 1026 | -0.002 | +119.54€ | 0 | 3 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 649 | +0.239 | +589.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 649 | +0.239 | +589.26€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 948 | -0.013 | +27.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 948 | -0.013 | +27.14€ | 4 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 971 | +0.004 | +90.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 971 | +0.004 | +90.04€ | 3 | 2 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 782 | +0.202 | +597.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 782 | +0.202 | +597.65€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 3176 | +0.176 | +2162.13€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 3176 | +0.176 | +2162.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 565 | +0.191 | +408.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 565 | +0.191 | +408.22€ | 0 | 18 |
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
| ✅ GBM_LATE_15M_TARDIO | 3708 | +0.167 | +2364.32€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 3708 | +0.167 | +2364.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 733 | +0.187 | +514.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 733 | +0.187 | +514.09€ | 0 | 17 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 486 | +0.156 | +259.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 486 | +0.156 | +259.78€ | 1 | 23 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 731 | +0.218 | +603.45€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 731 | +0.218 | +603.45€ | 0 | 17 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 328 | +0.112 | +124.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 328 | +0.112 | +124.94€ | 1 | 19 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 601 | +0.074 | +238.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 601 | +0.074 | +238.05€ | 1 | 14 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 829 | +0.197 | +624.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 829 | +0.197 | +624.01€ | 0 | 22 |
| ✅ GBM_LATE_5M | 230 | +0.086 | +56.33€ | 3 | 13 |
| ✅ GBM_LATE_5M#5min | 230 | +0.086 | +56.33€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 115 | +0.064 | +17.98€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 115 | +0.064 | +17.98€ | 0 | 7 |
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
| ✅ LEADLAG_BTC_XRP_15M | 50 | +0.154 | +13.66€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 50 | +0.154 | +13.66€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 50 | +0.154 | +13.66€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 50 | +0.154 | +13.66€ | 0 | 1 |
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
| ✅ MOMENTUM_IBS_15M | 419 | +0.032 | +2.08€ | 1 | 1 |
| ✅ MOMENTUM_IBS_15M#15min | 419 | +0.032 | +2.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 67 | +0.007 | -1.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 67 | +0.007 | -1.78€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 72 | +0.054 | +6.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 72 | +0.054 | +6.02€ | 0 | 2 |
| ✅ MOMENTUM_IBS_15M#DOGE | 65 | -0.022 | -11.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 65 | -0.022 | -11.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 75 | +0.097 | +17.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 75 | +0.097 | +17.76€ | 0 | 3 |
| ✅ MOMENTUM_IBS_15M#SOL | 70 | -0.014 | -9.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 70 | -0.014 | -9.45€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 70 | +0.056 | +0.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 70 | +0.056 | +0.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 569 | -0.017 | +5.27€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 569 | -0.017 | +5.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 90 | -0.011 | +19.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 90 | -0.011 | +19.57€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 99 | -0.045 | -7.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 99 | -0.045 | -7.02€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 94 | -0.010 | +6.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 94 | -0.010 | +6.97€ | 1 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 95 | +0.036 | +1.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 95 | +0.036 | +1.23€ | 1 | 4 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 93 | -0.079 | -16.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 93 | -0.079 | -16.25€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 98 | +0.010 | +0.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 98 | +0.010 | +0.76€ | 0 | 2 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 1456 | -0.079 | -37.96€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 1456 | -0.079 | -37.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 222 | -0.080 | +1.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 222 | -0.080 | +1.55€ | 3 | 1 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 278 | -0.075 | +71.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 278 | -0.075 | +71.06€ | 8 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 236 | -0.088 | -35.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 236 | -0.088 | -35.81€ | 6 | 1 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 223 | -0.118 | -38.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 223 | -0.118 | -38.31€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 257 | -0.037 | -4.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 257 | -0.037 | -4.24€ | 4 | 1 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 240 | -0.079 | -32.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 240 | -0.079 | -32.20€ | 7 | 2 |
| ✅ MOMENTUM_IBS_5M_FADE | 1421 | +0.017 | +5.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 1421 | +0.017 | +5.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 242 | +0.029 | +8.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 242 | +0.029 | +8.77€ | 0 | 1 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 208 | +0.033 | -0.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 208 | +0.033 | -0.32€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 245 | +0.006 | -1.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 245 | +0.006 | -1.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 246 | +0.008 | -0.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 246 | +0.008 | -0.69€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 248 | +0.016 | +1.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 248 | +0.016 | +1.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 232 | +0.009 | -3.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 232 | +0.009 | -3.01€ | 0 | 0 |
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
| ✅ STREAK_FADE_15M | 44 | -0.130 | -12.64€ | 0 | 0 |
| ✅ STREAK_FADE_15M#15min | 44 | -0.130 | -12.64€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 18 | -0.045 | -4.15€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 18 | -0.045 | -4.15€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 21 | -0.152 | -6.28€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 21 | -0.152 | -6.28€ | 0 | 0 |
| ✅ STREAK_FADE_5M | 330 | -0.024 | -19.53€ | 2 | 1 |
| ✅ STREAK_FADE_5M#5min | 330 | -0.024 | -19.53€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 78 | +0.050 | +3.69€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 78 | +0.050 | +3.69€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 114 | -0.009 | -6.55€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 114 | -0.009 | -6.55€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 62 | -0.094 | -9.24€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 62 | -0.094 | -9.24€ | 2 | 1 |
| ✅ STREAK_FADE_5M#XRP | 76 | -0.064 | -7.43€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 76 | -0.064 | -7.43€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 15 | -0.066 | -1.71€ | 0 | 0 |
| ✅ STREAK_FADE_60M#60min | 15 | -0.066 | -1.71€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 9 | -0.061 | -1.63€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 9 | -0.061 | -1.63€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 563 | +0.026 | +6.69€ | 1 | 0 |
| ✅ STREAK_MOM_5M#5min | 563 | +0.026 | +6.69€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 169 | -0.003 | -4.66€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 169 | -0.003 | -4.66€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 115 | -0.004 | -1.76€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 115 | -0.004 | -1.76€ | 2 | 2 |
| ✅ STREAK_MOM_5M#SOL | 148 | +0.047 | +4.51€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 148 | +0.047 | +4.51€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP | 131 | +0.064 | +8.61€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 131 | +0.064 | +8.61€ | 1 | 4 |
| ✅ STRUCT_NO_15M | 1807 | +0.013 | -8.74€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 1807 | +0.013 | -8.74€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 691 | +0.006 | -8.33€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 691 | +0.006 | -8.33€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 712 | +0.017 | -0.88€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 712 | +0.017 | -0.88€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 404 | +0.017 | +0.47€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 404 | +0.017 | +0.47€ | 2 | 0 |
| ✅ UPDOWN_GBM | 2022 | +0.018 | +88.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 880 | +0.083 | +140.00€ | 1 | 6 |
| ✅ UPDOWN_GBM#240min | 116 | +0.009 | -1.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 733 | -0.029 | -38.78€ | 4 | 0 |
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
| ✅ UPDOWN_GBM#ETH | 474 | +0.052 | +44.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 208 | +0.129 | +51.25€ | 1 | 16 |
| ✅ UPDOWN_GBM#ETH#240min | 35 | +0.041 | +0.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 119 | -0.004 | -4.42€ | 4 | 7 |
| ✅ UPDOWN_GBM#ETH#60min | 97 | +0.005 | -1.72€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 355 | -0.007 | +1.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 146 | +0.013 | +1.11€ | 1 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 29 | -0.016 | -0.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 104 | +0.000 | +0.77€ | 2 | 6 |
| ✅ UPDOWN_GBM#SOL#60min | 64 | -0.015 | +0.81€ | 2 | 0 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 450 | +0.022 | +47.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 272 | +0.088 | +67.70€ | 0 | 14 |
| ✅ UPDOWN_GBM#XRP#240min | 17 | -0.112 | -2.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 161 | -0.071 | -17.75€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 105 | +0.238 | -4.25€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 105 | +0.238 | -4.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 69 | +0.204 | -10.17€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 69 | +0.204 | -10.17€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 36 | +0.289 | +5.92€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 36 | +0.289 | +5.92€ | 0 | 1 |
| ✅ UPDOWN_GBM_15M_TARDIO | 1585 | -0.046 | +164.50€ | 3 | 2 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 1585 | -0.046 | +164.50€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 102 | -0.077 | -4.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 102 | -0.077 | -4.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 316 | -0.132 | -6.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 316 | -0.132 | -6.59€ | 3 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 39 | -0.012 | +0.96€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 39 | -0.012 | +0.96€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 129 | -0.004 | +19.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 129 | -0.004 | +19.46€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 507 | -0.009 | +93.91€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 507 | -0.009 | +93.91€ | 1 | 1 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 492 | -0.036 | +60.95€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 492 | -0.036 | +60.95€ | 3 | 0 |
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
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**🟡 H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread=0.152: overbought→boost, oversold→filtro | oversold(IBS<0.3): IC=-0.033 n=696 | neutral: IC=+0.004 n=691 | overbought(IBS>0.7): IC=+0.119 n=933
  - _Datos_: n=2484 IC=+0.039 PNL=+164.31€

**🟡 H-HORA-GBM** — hora_utc causal automático en GBM (forward)
  - _Umbral_: n≥20 forward con hora_utc + alguna hora con n≥15 IC<-0.10 o >+0.10
  - _Acción_: El sistema lo aplica automáticamente vía FEATURE_RULES. Verificar en strategy_params.json.
  - _Estado_: H=14h: IC=+0.120 n=90 PNL=+25.02€ → BOOST | H=23h: IC=-0.149 n=112 PNL=-29.64€ → FILTRAR

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.013 < 0.08 — monitorear
  - _Datos_: n=146 IC=+0.013 PNL=+1.11€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=289/15 IC=+0.256 PNL=+69.14€ | BTC: n=270/15 IC=+0.199 PNL=+8.22€ | SOL: n=351/15 IC=+0.372 PNL=+309.10€

**🟡 H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.108 n=36609 | tras_1loss IC=+0.063 n=25484 | tras_2loss IC=+0.021 n=11068/40 | gap=+0.087 (umbral 0.05)

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 12 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC, UPDOWN_GBM#SOL
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
  - _Estado_: alineada_con_outcome_prev IC=+0.148 n=11/60 | contraria IC=-0.064 n=11 | gap=+0.212 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=13, boost estimado=-0.013. Necesita 7 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 21/50 ops con delta_ratio feature

**⏳ H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 0 celda(s) pasan gate riguroso completo de 22 evaluadas (n>=40) y 251 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=97/40 IC=+0.005 PNL=-1.72€ | BTC#60min: n=85/40 IC=-0.063 PNL=-9.73€ | SOL#60min: n=64/40 IC=-0.015 PNL=+0.81€

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.062 n=142 | contrario_BTC IC=-0.031 n=79/40 | gap=-0.093 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.139 > 0.08 con n=59 PNL=+24.18€
  - _Datos_: n=59 IC=+0.139 PNL=+24.18€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.118 > 0.08 con n=74 PNL=+16.44€
  - _Datos_: n=74 IC=+0.118 PNL=+16.44€

**⏳ H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: 25
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: 3/25 ops en el filtro definido (IC actual=+0.045 PNL=+2.21€)
  - _Datos_: n=3 IC=+0.045 PNL=+2.21€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.343 > 0.1 con n=775 PNL=+396.95€
  - _Datos_: n=775 IC=+0.343 PNL=+396.95€

**⏳ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: 15
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: 8/15 ops en el filtro definido (IC actual=-0.040 PNL=-0.32€)
  - _Datos_: n=8 IC=-0.040 PNL=-0.32€

**⏳ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: 30
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: 5/30 ops en el filtro definido (IC actual=+0.018 PNL=-0.00€)
  - _Datos_: n=5 IC=+0.018 PNL=-0.00€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=1868 IC=+0.014 PNL=+75.64€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=1868 IC=+0.014 PNL=+75.64€

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
  - _Estado_: n=188 IC=+0.000 PNL=-3.68€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=188 IC=+0.000 PNL=-3.68€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=58 IC=-0.100 PNL=-6.96€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=58 IC=-0.100 PNL=-6.96€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=35 IC=+0.013 PNL=+0.27€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=35 IC=+0.013 PNL=+0.27€

**〰️ H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: n=414 IC=+0.096 PNL=+54.12€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=414 IC=+0.096 PNL=+54.12€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=105 IC=+0.014 PNL=+0.92€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=105 IC=+0.014 PNL=+0.92€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=118 IC=+0.050 PNL=-4.61€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=118 IC=+0.050 PNL=-4.61€

**⏳ H-CUSTOM-DRIFT15-ZONA-MUERTA** — GBM#15min drift_15min ∈ [-0.3,+0.3] — zona muerta de señal
  - _Hipótesis_: Análisis n=127 GBM#15min: cuando drift_15min está entre -0.3 y +0.3 (mercado sin dirección clara) el IC es negativo (-0.043). Cuando drift>0.3 IC=+0.100 (n=28). Cuando drift<-1 IC=+0.048 (reversión). La señal requiere mercado con dirección clara.
  - _Umbral_: 50
  - _Acción_: Filtrar señales GBM#15min cuando drift_15min ∈ [-0.3, +0.3] — validar con n≥50 antes de implementar
  - _Estado_: 0/50 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-DRIFT15-MOMENTUM** — GBM#15min drift_15min > 0.3 — zona de momentum (señal fuerte)
  - _Hipótesis_: Cuando drift_15min > 0.3%/h el GBM captura bien la dirección: IC=+0.100 n=28 en todos GBM#15min; IC=+0.152 n=13 solo BTC. El mercado tiene dirección clara y el GBM la sigue. Hipótesis: este rango es donde la señal es real.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma IC>0.10 con n≥40 → boost ×1.2 en GBM#15min cuando drift_15min>0.3
  - _Estado_: n=548 IC=+0.078 PNL=+62.84€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=548 IC=+0.078 PNL=+62.84€

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
  - _Estado_: 14/20 ops en el filtro definido (IC actual=+0.131 PNL=+8.58€)
  - _Datos_: n=14 IC=+0.131 PNL=+8.58€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=31 IC=+0.136 PNL=+4.66€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=31 IC=+0.136 PNL=+4.66€

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
  - _Estado_: n=73 IC=+0.020 PNL=+8.12€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=73 IC=+0.020 PNL=+8.12€

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
  - _Estado_: 2/30 ops en el filtro definido (IC actual=+0.025 PNL=+0.98€)
  - _Datos_: n=2 IC=+0.025 PNL=+0.98€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=393 IC=+0.085 PNL=+86.05€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=393 IC=+0.085 PNL=+86.05€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=289 IC=+0.040 PNL=-4.05€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=289 IC=+0.040 PNL=-4.05€

**⏳ H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: 40
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: 22/40 ops en el filtro definido (IC actual=+0.083 PNL=+3.19€)
  - _Datos_: n=22 IC=+0.083 PNL=+3.19€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.140 > 0.08 con n=87 PNL=-4.06€
  - _Datos_: n=87 IC=+0.140 PNL=-4.06€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.087 > 0.08 con n=78 PNL=+15.24€
  - _Datos_: n=78 IC=+0.087 PNL=+15.24€

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
  - _Estado_: n=304 IC=+0.026 PNL=+5.57€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=304 IC=+0.026 PNL=+5.57€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.148 > 0.02 con n=103 PNL=+32.36€
  - _Datos_: n=103 IC=+0.148 PNL=+32.36€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.444 > 0.1 con n=513 PNL=+432.32€
  - _Datos_: n=513 IC=+0.444 PNL=+432.32€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=951 IC=+0.018 PNL=+18.89€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=951 IC=+0.018 PNL=+18.89€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.147 > 0.1 con n=539 PNL=+156.14€
  - _Datos_: n=539 IC=+0.147 PNL=+156.14€

**⏳ H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: 40
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: 11/40 ops en el filtro definido (IC actual=-0.190 PNL=-4.96€)
  - _Datos_: n=11 IC=-0.190 PNL=-4.96€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=145 IC=+0.092 PNL=+35.75€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=145 IC=+0.092 PNL=+35.75€

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
  - _Estado_: 27/50 ops en el filtro definido (IC actual=+0.086 PNL=-0.30€)
  - _Datos_: n=27 IC=+0.086 PNL=-0.30€

**⏳ H-CUSTOM-ETH15-BUYNO-PRECIO-ALTO** — ETH#15min BUY_NO con precio_yes>0.55 pierde (NO longshot contra favorito)
  - _Hipótesis_: Detectado 2026-07-02: ult.60 shadow ETH15 BUY_NO — py_mkt~0.5 wr=0.67 PNL=+29.3 (n=49); py_mkt 0.6-0.8 wr 0.33-0 PNL=-5.75 (n=9). Filtro RETURN NONE (no SKIP) aplicado en shadow_predict.py (PY_MKT_MAX_BUY_NO_ETH15=0.55) el mismo dia -- bloquea la GENERACIÓN de la fila, no solo la decisión. Esta hipotesis trackea la zona filtrada: si las ops que HABRIAN caido aqui siguen apareciendo en otras estrategias o el IC forward de la zona se vuelve positivo, revisar el filtro. CAVEAT: n=9, muestra chica — el filtro se aplico por asimetria de riesgo (afecta a dinero live), no por significancia. ⚠️ 05-Ago (fix): la clave del filtro decía 'py_mkt', que NUNCA existió ni en features de UPDOWN_GBM (T_h/delta_ratio_macro/drift_15min/drift_60min/pct_spot_vs_ref/sigma_h) ni como columna top-level de results.csv -- corregida a 'precio_yes_mercado' (columna real). Aun así, con la clave correcta esta hipótesis NUNCA podrá acumular n mientras el filtro RETURN NONE siga activo -- es el mismo patrón 'frozen by design' que H-CUSTOM-LATE15-PHOTO-FINISH (más abajo): la propia protección impide generar los datos necesarios para volver a evaluarla. Para monitorearla de verdad haría falta un logger separado que capture la señal SIN aplicar el filtro (mismo patrón que gate_bucket_propio con data/markets histórico) -- no construido, pendiente decisión.
  - _Umbral_: 20
  - _Acción_: Si IC forward de la zona >0 con n>=20 → retirar filtro; si confirma negativo → considerar extender a BTC/SOL 15min
  - _Estado_: 0/20 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-PRECIO-YES-BARATO** — BUY_YES con precio de mercado 0.30-0.40 — mercado infravalora YES
  - _Hipótesis_: Detectado 2026-07-03 en benchmark de calibración del mercado (7d, estrategias GBM): en el bucket precio_yes_mercado [0.3-0.4) la frecuencia real de YES fue 0.45 vs 0.35 implícito (+0.10, n=38). Posible sesgo favorito-longshot suave en binarios de 15min (complemento del LONGSHOT ya activo para BUY_NO con py<0.20). Si se confirma, BUY_YES comprado en esa banda lleva viento de cola estructural del propio mercado, independiente del modelo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → kelly_boost ×1.1 para BUY_YES con precio_yes_mercado en [0.30,0.40), simétrico al longshot BUY_NO existente
  - _Estado_: n=1206 IC=-0.143 PNL=+78.73€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1206 IC=-0.143 PNL=+78.73€

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
  - _Estado_: n=298 IC=+0.143 PNL=+94.05€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=298 IC=+0.143 PNL=+94.05€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.096 > 0.08 con n=414 PNL=+54.12€
  - _Datos_: n=414 IC=+0.096 PNL=+54.12€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=220 IC=-0.018 PNL=-9.78€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=220 IC=-0.018 PNL=-9.78€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.126 > 0.08 con n=375 PNL=+193.08€
  - _Datos_: n=375 IC=+0.126 PNL=+193.08€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.115 > 0.08 con n=94 PNL=+2.08€
  - _Datos_: n=94 IC=+0.115 PNL=+2.08€

**⏳ H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: 289
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: 36/289 ops en el filtro definido (IC actual=-0.289 PNL=-7.78€)
  - _Datos_: n=36 IC=-0.289 PNL=-7.78€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=773 IC=+0.158 PNL=+411.51€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=773 IC=+0.158 PNL=+411.51€

**⏳ H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: 40
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: 12/40 ops en el filtro definido (IC actual=+0.000 PNL=-2.54€)
  - _Datos_: n=12 IC=+0.000 PNL=-2.54€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=327 IC=+0.002 PNL=+24.45€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=327 IC=+0.002 PNL=+24.45€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.209 > 0.08 con n=266 PNL=+150.14€
  - _Datos_: n=266 IC=+0.209 PNL=+150.14€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=547 IC=+0.032 PNL=+151.67€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=547 IC=+0.032 PNL=+151.67€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.127 > 0.08 con n=156 PNL=-12.25€
  - _Datos_: n=156 IC=+0.127 PNL=-12.25€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.254 > 0.08 con n=623 PNL=-61.89€
  - _Datos_: n=623 IC=+0.254 PNL=-61.89€

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 3/40 ops en el filtro definido (IC actual=-0.015 PNL=-0.17€)
  - _Datos_: n=3 IC=-0.015 PNL=-0.17€

**⏳ H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: 40
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: 31/40 ops en el filtro definido (IC actual=+0.167 PNL=+10.83€)
  - _Datos_: n=31 IC=+0.167 PNL=+10.83€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 38/40 ops en el filtro definido (IC actual=+0.375 PNL=+31.25€)
  - _Datos_: n=38 IC=+0.375 PNL=+31.25€

**⏳ H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: 200
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: 188/200 ops en el filtro definido (IC actual=+0.442 PNL=+250.61€)
  - _Datos_: n=188 IC=+0.442 PNL=+250.61€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=1048 IC=+0.102 PNL=-229.63€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=1048 IC=+0.102 PNL=-229.63€

**⏳ H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: 40
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: 15/40 ops en el filtro definido (IC actual=+0.154 PNL=+6.63€)
  - _Datos_: n=15 IC=+0.154 PNL=+6.63€
