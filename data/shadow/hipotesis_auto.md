# Hipótesis automáticas — 2026-08-18 21:14 UTC
_Generado por shadow_postmortem.py sobre 67715 resoluciones (PNL=+6712.24€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.355` → IC=-0.143 (n=68)

  - _Acción_: SKIP cuando `py_entrada` < 0.355
  - _Potencial_: sin este filtro IC_bueno=+0.182 (n=149)

- **FILTRO** `banda_hit_calibrado` < `0.6142` → IC=-0.227 (n=53)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6142
  - _Potencial_: sin este filtro IC_bueno=+0.181 (n=164)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.377 (n=63)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=209)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.239 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.080)

- **PATRÓN** `n_total_lado` > `73.0` → IC=+0.202 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 73.0 (IC base=+0.080)

- **PATRÓN** `banda_hit_calibrado` > `0.6142` → IC=+0.181 (n=164)

  - _Acción_: Kelly boost +0.90€ cuando `banda_hit_calibrado` > 0.6142 (IC base=+0.080)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.140 (n=209)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.5 (IC base=+0.018)

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
  - _Potencial_: sin este filtro IC_bueno=+0.174 (n=84)

- **FILTRO** `banda_hit_calibrado` < `0.6267` → IC=-0.203 (n=35)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6267
  - _Potencial_: sin este filtro IC_bueno=+0.197 (n=74)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.132 (n=85)

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

- **PATRÓN** `py_entrada` > `0.33` → IC=+0.174 (n=84)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` > 0.33 (IC base=+0.068)

- **PATRÓN** `banda_hit_calibrado` > `0.6267` → IC=+0.197 (n=74)

  - _Acción_: Kelly boost +0.99€ cuando `banda_hit_calibrado` > 0.6267 (IC base=+0.068)

- **PATRÓN** `banda_z` > `8.673` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.673 (IC base=+0.068)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.132 (n=85)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.068)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.495 (IC base=-0.024)

### BALLENAS_TARDIAS
- **FILTRO** `n_ballenas` < `5.0` → IC=-0.126 (n=2137)

  - _Acción_: SKIP cuando `n_ballenas` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=1453)

- **FILTRO** `restante_s_al_confirmar` < `150.62` → IC=-0.253 (n=897)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 150.62
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=2693)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `117.22` → IC=-0.405 (n=93)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 117.22
  - _Potencial_: sin este filtro IC_bueno=-0.106 (n=280)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` > `641.03` → IC=-0.278 (n=115)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` > 641.03
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=347)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `13.68` → IC=-0.492 (n=119)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 13.68
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=243)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `concentracion_yes` < `1.0` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `concentracion_yes` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.128 (n=801)

- **FILTRO** `restante_s_al_confirmar` < `247.25` → IC=-0.156 (n=646)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 247.25
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=216)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `156.97` → IC=-0.280 (n=175)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 156.97
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=526)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.7` → IC=+0.191 (n=2311)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.7 (IC base=+0.092)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.164 (n=1165)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `2373.8543` → IC=+0.166 (n=1126)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2373.8543 (IC base=+0.092)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.158 (n=3965)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 7.0 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.152 (n=2869)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 11.0 (IC base=+0.152)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.286 (n=1497)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.152)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.190 (n=2018)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.02 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `4043.1829` → IC=+0.180 (n=818)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 4043.1829 (IC base=+0.152)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.206 (n=366)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.775` → IC=+0.357 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.775 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.202 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.228 (n=310)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.298 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.198 (n=438)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.196)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.140 (n=395)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.162 (n=341)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 15.0 (IC base=+0.131)

- **PATRÓN** `py_entrada` > `0.555` → IC=+0.142 (n=423)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` > 0.555 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `5033.4098` → IC=+0.165 (n=195)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 5033.4098 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.143 (n=138)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 17.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.199 (n=161)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.142)

- **PATRÓN** `py_entrada` < `0.395` → IC=+0.224 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.395 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `5296.1268` → IC=+0.176 (n=208)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 5296.1268 (IC base=+0.142)

### FAVORITO_CONFIRMADO#ETH#15min
- **PATRÓN** `hora_utc` < `11.0` → IC=+0.146 (n=461)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 11.0 (IC base=+0.112)

- **PATRÓN** `py_entrada` > `0.7` → IC=+0.304 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.7 (IC base=+0.112)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.313 (n=271)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.294)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.297 (n=269)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.294)

- **PATRÓN** `py_entrada` < `0.195` → IC=+0.399 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.195 (IC base=+0.294)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.297 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.294)

- **PATRÓN** `libro_liquidez` > `3362.7335` → IC=+0.352 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3362.7335 (IC base=+0.294)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=282)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.172 (n=248)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 16.0 (IC base=+0.146)

- **PATRÓN** `py_entrada` > `0.655` → IC=+0.240 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.655 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=273)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `2191.1992` → IC=+0.169 (n=270)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2191.1992 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `5697.4897` → IC=+0.190 (n=69)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 5697.4897 (IC base=+0.098)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.177 (n=580)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.186 (n=492)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 15.0 (IC base=+0.173)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.401 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.283 (n=118)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.237)

- **PATRÓN** `py_entrada` < `0.31` → IC=+0.352 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.31 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.253 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `913.9984` → IC=+0.247 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 913.9984 (IC base=+0.237)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `19.0` → IC=+0.253 (n=75)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 19.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.195 (n=152)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 13.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.333 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.215 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.122 (n=368)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.112)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.222 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.112)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.162 (n=258)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.02 (IC base=+0.112)

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
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 7.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.202 (n=913)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `3268.7028` → IC=+0.348 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3268.7028 (IC base=+0.178)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.163 (n=601)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 15.0 (IC base=+0.154)

- **PATRÓN** `py_entrada` < `0.75` → IC=+0.168 (n=693)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` < 0.75 (IC base=+0.154)

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
- **PATRÓN** `hora_utc` < `7.0` → IC=+0.189 (n=291)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 7.0 (IC base=+0.158)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.188 (n=229)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.7 (IC base=+0.158)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.218 (n=605)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.236 (n=399)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.316 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.218)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min
- **FILTRO** `py_entrada` > `0.755` → IC=-0.267 (n=58)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=20)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.193 (n=223)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.200 (n=275)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.172)

- **PATRÓN** `py_entrada` < `0.72` → IC=+0.186 (n=505)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` < 0.72 (IC base=+0.172)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.440 (n=114)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.417)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.422 (n=114)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.417)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.423 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.417)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.456 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.417)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.415 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.417)

- **PATRÓN** `libro_liquidez` > `3355.2252` → IC=+0.432 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3355.2252 (IC base=+0.417)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `12.0` → IC=+0.414 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.419)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.429 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.419)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.438 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.419)

- **PATRÓN** `libro_liquidez` > `8500.2314` → IC=+0.441 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8500.2314 (IC base=+0.419)

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
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.197 (n=1619)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 17.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.198 (n=3089)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 11.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.228 (n=3210)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.188)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` < `11.0` → IC=+0.130 (n=576)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 11.0 (IC base=+0.097)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.140 (n=420)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` > 0.73 (IC base=+0.097)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.294 (n=236)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.248)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.265 (n=236)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.248)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.320 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.248)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` < `7.0` → IC=+0.167 (n=367)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 7.0 (IC base=+0.151)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.215 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.151)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.240 (n=356)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.290 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.223)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.253 (n=253)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.246)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.260 (n=273)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.246)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.288 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.246)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.230 (n=272)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.208 (n=258)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.187)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.256 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.187)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.228 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.150)

- **PATRÓN** `restante_min` < `3.8` → IC=+0.168 (n=549)

  - _Acción_: Kelly boost +0.84€ cuando `restante_min` < 3.8 (IC base=+0.150)

- **PATRÓN** `restante_min` > `4.91` → IC=+0.202 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `restante_min` > 4.91 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.157 (n=1532)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 7.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.156 (n=1671)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 17.0 (IC base=+0.150)

- **PATRÓN** `lag_apertura_s` < `5.5` → IC=+0.213 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `lag_apertura_s` < 5.5 (IC base=+0.150)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.242 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.158)

- **PATRÓN** `restante_min` < `3.73` → IC=+0.176 (n=273)

  - _Acción_: Kelly boost +0.88€ cuando `restante_min` < 3.73 (IC base=+0.158)

- **PATRÓN** `restante_min` > `4.88` → IC=+0.194 (n=292)

  - _Acción_: Kelly boost +0.97€ cuando `restante_min` > 4.88 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.165 (n=851)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.158)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.164 (n=722)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 15.0 (IC base=+0.158)

- **PATRÓN** `lag_apertura_s` < `7.13` → IC=+0.195 (n=270)

  - _Acción_: Kelly boost +0.97€ cuando `lag_apertura_s` < 7.13 (IC base=+0.158)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.212 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.142)

- **PATRÓN** `restante_min` < `3.9` → IC=+0.149 (n=277)

  - _Acción_: Kelly boost +0.74€ cuando `restante_min` < 3.9 (IC base=+0.142)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.220 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `restante_min` > 4.95 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.147 (n=774)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 7.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.152 (n=847)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 17.0 (IC base=+0.142)

- **PATRÓN** `lag_apertura_s` < `3.26` → IC=+0.222 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `lag_apertura_s` < 3.26 (IC base=+0.142)

- **PATRÓN** `profundidad_ratio_no` > `11.8` → IC=+0.168 (n=278)

  - _Acción_: Kelly boost +0.84€ cuando `profundidad_ratio_no` > 11.8 (IC base=+0.142)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.309 (n=428)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.298)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.311 (n=406)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.298)

- **PATRÓN** `py_entrada` > `0.825` → IC=+0.383 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.825 (IC base=+0.298)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.284 (n=179)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.272)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.280 (n=175)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.272)

- **PATRÓN** `py_entrada` < `0.725` → IC=+0.287 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.725 (IC base=+0.272)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.346 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.272)

- **PATRÓN** `libro_liquidez` > `3930.7776` → IC=+0.279 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3930.7776 (IC base=+0.272)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.310 (n=198)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.299)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.318 (n=196)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.299)

- **PATRÓN** `py_entrada` > `0.81` → IC=+0.397 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.81 (IC base=+0.299)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.303 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.299)

- **PATRÓN** `libro_liquidez` > `1883.0341` → IC=+0.317 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1883.0341 (IC base=+0.299)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` < `13.0` → IC=+0.444 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.373)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.409 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.373)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.409 (n=173)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.409)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.433 (n=176)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.409)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.412 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.409)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.430 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.409)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.406 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.409)

- **PATRÓN** `libro_liquidez` > `2161.317` → IC=+0.416 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2161.317 (IC base=+0.409)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.401 (n=79)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.404)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.439 (n=80)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.404)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.416 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.404)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.419 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.404)

- **PATRÓN** `libro_liquidez` > `5330.8398` → IC=+0.446 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5330.8398 (IC base=+0.404)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.412 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.413)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.417 (n=70)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.413)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.415 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.413)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.428 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.413)

- **PATRÓN** `libro_liquidez` > `1842.491` → IC=+0.437 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1842.491 (IC base=+0.413)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.280 (n=139)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.259)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.409 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.278 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1401.7964` → IC=+0.315 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1401.7964 (IC base=+0.259)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.280 (n=139)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.259)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.409 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.278 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1401.7964` → IC=+0.315 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1401.7964 (IC base=+0.259)

### GBM_LATE_15M
- **PATRÓN** `hora_utc` < `6.0` → IC=+0.148 (n=441)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 6.0 (IC base=+0.100)

- **PATRÓN** `ibs_20min` > `0.9834` → IC=+0.265 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9834 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `0.5859` → IC=+0.315 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5859 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.749` → IC=+0.235 (n=605)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.749 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` < `1.294` → IC=+0.248 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.294 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` > `0.6419` → IC=+0.242 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6419 (IC base=+0.100)

- **PATRÓN** `ibs_20min` < `0.6598` → IC=+0.123 (n=2166)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.6598 (IC base=+0.078)

- **PATRÓN** `dist_vwap_pct` < `0.1461` → IC=+0.142 (n=548)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.1461 (IC base=+0.078)

- **PATRÓN** `volumen_regimen` < `1.3118` → IC=+0.140 (n=490)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.3118 (IC base=+0.078)

- **PATRÓN** `volumen_regimen` > `0.6936` → IC=+0.142 (n=437)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.6936 (IC base=+0.078)

- **PATRÓN** `volumen_pendiente_norm` > `0.3263` → IC=+0.285 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3263 (IC base=+0.078)

- **PATRÓN** `volumen_spike_ratio` < `1.7042` → IC=+0.247 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7042 (IC base=+0.078)

- **PATRÓN** `volumen_spike_ratio` > `2.8143` → IC=+0.221 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8143 (IC base=+0.078)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.297 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 57.0 (IC base=+0.078)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.168 (n=185)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.007 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.191 (n=147)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 6.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.292 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.508` → IC=+0.345 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.508 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.154 (n=299)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.06 (IC base=+0.121)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.309 (n=129)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.336 (n=65)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.1343` → IC=+0.340 (n=129)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1343 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.287 (n=205)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.284)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.294 (n=202)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.284)

- **PATRÓN** `ibs_20min` < `0.578` → IC=+0.331 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.578 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` < `0.0668` → IC=+0.313 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0668 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` > `0.24` → IC=+0.321 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.24 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` < `1.8119` → IC=+0.341 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8119 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` > `1.5851` → IC=+0.295 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5851 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.327 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `1915.807` → IC=+0.311 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1915.807 (IC base=+0.284)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0018` → IC=+0.311 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0018 (IC base=+0.263)

- **PATRÓN** `sigma_h` > `0.0035` → IC=+0.306 (n=34)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0035 (IC base=+0.263)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.315 (n=90)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.263)

- **PATRÓN** `ibs_20min` < `0.6521` → IC=+0.278 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6521 (IC base=+0.263)

- **PATRÓN** `ibs_20min` > `0.9149` → IC=+0.283 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9149 (IC base=+0.263)

- **PATRÓN** `dist_vwap_pct` > `0.55` → IC=+0.315 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.55 (IC base=+0.263)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.566` → IC=+0.339 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.566 (IC base=+0.263)

- **PATRÓN** `volumen_regimen` < `0.6564` → IC=+0.306 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6564 (IC base=+0.263)

- **PATRÓN** `volumen_pendiente_norm` < `0.1716` → IC=+0.312 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1716 (IC base=+0.263)

- **PATRÓN** `volumen_spike_ratio` < `2.7036` → IC=+0.321 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.7036 (IC base=+0.263)

- **PATRÓN** `libro_liquidez` > `12045.4998` → IC=+0.312 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12045.4998 (IC base=+0.263)

- **PATRÓN** `sigma_h` < `0.0018` → IC=+0.171 (n=80)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0018 (IC base=+0.144)

- **PATRÓN** `sigma_h` > `0.0029` → IC=+0.158 (n=109)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0029 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.1881` → IC=+0.170 (n=210)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1881 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.170 (n=225)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 8.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.4773` → IC=+0.205 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4773 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` < `0.1366` → IC=+0.164 (n=257)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1366 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.472` → IC=+0.234 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.472 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.2823` → IC=+0.160 (n=239)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2823 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `0.6821` → IC=+0.162 (n=214)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6821 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.13` → IC=+0.254 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.13 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.5142` → IC=+0.250 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5142 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `12133.9239` → IC=+0.171 (n=80)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 12133.9239 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `235.0` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 235.0 (IC base=+0.144)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.172 (n=123)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0075 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.209 (n=132)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.266 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.958` → IC=+0.286 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.958 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.4157` → IC=+0.159 (n=42)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.4157 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.145 (n=409)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.06 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `1919.501` → IC=+0.129 (n=168)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 1919.501 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.352 (n=79)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.0858` → IC=+0.312 (n=78)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0858 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.289 (n=164)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.286)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.294 (n=241)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.286)

- **PATRÓN** `ibs_20min` < `0.5082` → IC=+0.314 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5082 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.108` → IC=+0.316 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.108 (IC base=+0.286)

- **PATRÓN** `volumen_pendiente_norm` > `0.4259` → IC=+0.405 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.4259 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` < `2.0261` → IC=+0.304 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0261 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` > `3.1011` → IC=+0.263 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.1011 (IC base=+0.286)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.291 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.286)

### GBM_LATE_15M#ETH#15min
- **PATRÓN** `drift_60min` |x|≤ `0.0993` → IC=+0.138 (n=45)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.0993 (IC base=+0.062)

- **PATRÓN** `ibs_20min` > `0.5406` → IC=+0.129 (n=68)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` > 0.5406 (IC base=+0.062)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.253` → IC=+0.214 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.253 (IC base=+0.062)

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

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.157 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.006 (IC base=+0.108)

- **PATRÓN** `ibs_20min` > `0.375` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.375 (IC base=+0.108)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.108)

### GBM_LATE_15M#XRP#15min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.439` → IC=+0.144 (n=57)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 8.439 (IC base=-0.022)

- **PATRÓN** `volumen_regimen` < `0.7863` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.7863 (IC base=-0.022)

- **PATRÓN** `volumen_regimen` < `0.6973` → IC=+0.278 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6973 (IC base=+0.039)

- **PATRÓN** `volumen_regimen` > `1.3906` → IC=+0.232 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.3906 (IC base=+0.039)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `ibs_20min` > `0.9419` → IC=+0.229 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9419 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` > `0.1186` → IC=+0.169 (n=164)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1186 (IC base=+0.049)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.204` → IC=+0.125 (n=1007)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` > 2.204 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.3352` → IC=+0.195 (n=103)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.3352 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` > `2.1908` → IC=+0.153 (n=439)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.1908 (IC base=+0.049)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.254 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.049)

- **PATRÓN** `ibs_20min` < `0.1` → IC=+0.165 (n=861)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.1 (IC base=+0.048)

- **PATRÓN** `dist_vwap_pct` > `0.5042` → IC=+0.265 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5042 (IC base=+0.048)

- **PATRÓN** `volumen_regimen` > `1.0742` → IC=+0.214 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0742 (IC base=+0.048)

- **PATRÓN** `volumen_pendiente_norm` > `0.3496` → IC=+0.357 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3496 (IC base=+0.048)

- **PATRÓN** `volumen_spike_ratio` > `3.7273` → IC=+0.312 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.7273 (IC base=+0.048)

- **PATRÓN** `ballena_activa_n` < `74.0` → IC=+0.307 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 74.0 (IC base=+0.048)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `sigma_ewma_delta_pct` > `5.016` → IC=-0.210 (n=105)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.016
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=530)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.363` → IC=+0.167 (n=124)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 3.363 (IC base=-0.017)

- **PATRÓN** `volumen_pendiente_norm` > `0.1149` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1149 (IC base=-0.017)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `volumen_regimen` < `1.0528` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.0528 (IC base=-0.013)

- **PATRÓN** `volumen_regimen` < `0.5591` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.5591 (IC base=-0.009)

- **PATRÓN** `volumen_regimen` > `1.1078` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 1.1078 (IC base=-0.009)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.290 (n=117)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0074 (IC base=+0.176)

- **PATRÓN** `drift_60min` |x|≤ `0.0611` → IC=+0.206 (n=117)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0611 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.248 (n=161)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.287 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.958` → IC=+0.302 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.958 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` < `0.1388` → IC=+0.184 (n=254)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.1388 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.4225` → IC=+0.207 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.4225 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` < `4.7523` → IC=+0.162 (n=270)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 4.7523 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `3.8419` → IC=+0.188 (n=123)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 3.8419 (IC base=+0.176)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.192 (n=381)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.06 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `1915.1084` → IC=+0.202 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1915.1084 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.225 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 31.0 (IC base=+0.176)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.407 (n=106)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.369)

- **PATRÓN** `drift_60min` |x|≤ `0.1847` → IC=+0.372 (n=107)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1847 (IC base=+0.369)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.395 (n=150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.369)

- **PATRÓN** `ibs_20min` < `0.2414` → IC=+0.387 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2414 (IC base=+0.369)

- **PATRÓN** `volumen_pendiente_norm` < `0.3211` → IC=+0.389 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.3211 (IC base=+0.369)

- **PATRÓN** `volumen_pendiente_norm` > `0.1288` → IC=+0.397 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1288 (IC base=+0.369)

- **PATRÓN** `volumen_spike_ratio` < `2.9594` → IC=+0.436 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.9594 (IC base=+0.369)

- **PATRÓN** `libro_liquidez` > `1869.9762` → IC=+0.427 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1869.9762 (IC base=+0.369)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.6396` → IC=-0.127 (n=159)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6396
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=82)

- **FILTRO** `dist_vwap_pct` < `0.3632` → IC=-0.225 (n=38)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.3632
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=5)

- **FILTRO** `volumen_regimen` > `0.8629` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8629
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=22)

- **FILTRO** `libro_liquidez` < `8611.2001` → IC=-0.210 (n=60)

  - _Acción_: SKIP cuando `libro_liquidez` < 8611.2001
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=181)

- **FILTRO** `volumen_regimen` > `0.7318` → IC=-0.159 (n=39)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.7318
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.152 (n=44)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=694)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.45` → IC=-0.155 (n=143)

  - _Acción_: SKIP cuando `ibs_20min` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.135 (n=146)

- **FILTRO** `dist_vwap_pct` > `0.1234` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1234
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=40)

- **FILTRO** `volumen_regimen` > `1.2342` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.2342
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=37)

- **PATRÓN** `ibs_20min` > `0.45` → IC=+0.135 (n=146)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 0.45 (IC base=-0.009)

- **PATRÓN** `dist_vwap_pct` > `0.1776` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.1776 (IC base=-0.009)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.296 (n=101)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0066 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.1343` → IC=+0.145 (n=201)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.1343 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.137 (n=111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.207 (n=114)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` > `0.9048` → IC=+0.224 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9048 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `0.322` → IC=+0.210 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.322 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.12` → IC=+0.221 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.12 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` > `0.5938` → IC=+0.147 (n=301)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.5938 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.3138` → IC=+0.225 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3138 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=305)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `2467.2556` → IC=+0.135 (n=269)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2467.2556 (IC base=+0.133)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.293 (n=273)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.282)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.321 (n=160)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.282)

- **PATRÓN** `ibs_20min` < `0.3171` → IC=+0.334 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3171 (IC base=+0.282)

- **PATRÓN** `dist_vwap_pct` > `0.5491` → IC=+0.375 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5491 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.236` → IC=+0.286 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.236 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.001` → IC=+0.285 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.001 (IC base=+0.282)

- **PATRÓN** `volumen_regimen` > `1.3017` → IC=+0.337 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.3017 (IC base=+0.282)

- **PATRÓN** `volumen_pendiente_norm` > `0.2891` → IC=+0.379 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2891 (IC base=+0.282)

- **PATRÓN** `volumen_spike_ratio` > `3.6746` → IC=+0.311 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.6746 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `2861.3406` → IC=+0.288 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2861.3406 (IC base=+0.282)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.148 (n=424)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0047 (IC base=+0.137)

- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.191 (n=578)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0066 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.142 (n=428)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.158 (n=425)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 5.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.9206` → IC=+0.248 (n=847)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9206 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.2246` → IC=+0.142 (n=286)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.2246 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.94` → IC=+0.265 (n=624)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.94 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.1782` → IC=+0.141 (n=658)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.1782 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `0.6236` → IC=+0.138 (n=658)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.6236 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.1112` → IC=+0.154 (n=423)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.1112 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.143 (n=1431)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.06 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `2682.2064` → IC=+0.174 (n=424)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2682.2064 (IC base=+0.137)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.221 (n=1222)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.2382` → IC=+0.223 (n=1076)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2382 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.258 (n=565)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` < `0.3729` → IC=+0.280 (n=1222)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3729 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.677` → IC=+0.234 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.677 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.285` → IC=+0.215 (n=1206)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.285 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` < `1.2502` → IC=+0.191 (n=950)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 1.2502 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` > `0.8726` → IC=+0.202 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8726 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.2701` → IC=+0.281 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2701 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` < `2.0432` → IC=+0.231 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0432 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `3.1117` → IC=+0.242 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.1117 (IC base=+0.214)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.274 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 57.0 (IC base=+0.214)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.157 (n=106)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0058 (IC base=+0.149)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.207 (n=145)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.224 (n=121)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.8817` → IC=+0.284 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8817 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.61` → IC=+0.370 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.61 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.2097` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.2097 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.08` → IC=+0.167 (n=343)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.08 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.286 (n=87)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.285)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.322 (n=43)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.2186` → IC=+0.317 (n=113)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2186 (IC base=+0.285)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.311 (n=130)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.285)

- **PATRÓN** `ibs_20min` < `0.0505` → IC=+0.389 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0505 (IC base=+0.285)

- **PATRÓN** `volumen_pendiente_norm` < `0.1025` → IC=+0.315 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1025 (IC base=+0.285)

- **PATRÓN** `volumen_pendiente_norm` > `0.2006` → IC=+0.274 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2006 (IC base=+0.285)

- **PATRÓN** `volumen_spike_ratio` < `1.8801` → IC=+0.370 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8801 (IC base=+0.285)

- **PATRÓN** `libro_spread` < `0.08` → IC=+0.310 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.08 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `1962.1404` → IC=+0.344 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1962.1404 (IC base=+0.285)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0017` → IC=+0.250 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0017 (IC base=+0.215)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.306 (n=34)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.260 (n=102)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` > `0.8703` → IC=+0.263 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8703 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` > `0.5681` → IC=+0.300 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5681 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.296` → IC=+0.294 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.296 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` < `1.1299` → IC=+0.217 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1299 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` > `0.8987` → IC=+0.214 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8987 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.196` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.196 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `1.4774` → IC=+0.241 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4774 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `1.9486` → IC=+0.245 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9486 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `11341.8291` → IC=+0.306 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11341.8291 (IC base=+0.215)

- **PATRÓN** `sigma_h` < `0.0018` → IC=+0.209 (n=77)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0018 (IC base=+0.183)

- **PATRÓN** `sigma_h` > `0.002` → IC=+0.184 (n=204)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.002 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.1925` → IC=+0.204 (n=201)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1925 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.217 (n=217)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` < `0.2977` → IC=+0.236 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2977 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.472` → IC=+0.274 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.472 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `0.637` → IC=+0.222 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.637 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` > `0.6916` → IC=+0.184 (n=204)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 0.6916 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.136` → IC=+0.265 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.136 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` < `2.516` → IC=+0.243 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.516 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `11565.2208` → IC=+0.205 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11565.2208 (IC base=+0.183)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.153 (n=99)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0056 (IC base=+0.145)

- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.170 (n=198)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0065 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.1472` → IC=+0.155 (n=198)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1472 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.158 (n=115)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 16.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.206 (n=100)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.286 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.804` → IC=+0.319 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.804 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` < `0.2301` → IC=+0.123 (n=237)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.2301 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.4145` → IC=+0.134 (n=39)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.4145 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `2.0039` → IC=+0.198 (n=104)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.0039 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.172 (n=227)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.04 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `1970.8484` → IC=+0.153 (n=99)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 1970.8484 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.328 (n=97)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.310)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.311 (n=130)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.310)

- **PATRÓN** `drift_60min` |x|≤ `0.1716` → IC=+0.369 (n=97)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1716 (IC base=+0.310)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.330 (n=98)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.310)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.308 (n=128)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.310)

- **PATRÓN** `ibs_20min` < `0.2453` → IC=+0.339 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2453 (IC base=+0.310)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.875` → IC=+0.353 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.875 (IC base=+0.310)

- **PATRÓN** `volumen_pendiente_norm` > `0.3361` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3361 (IC base=+0.310)

- **PATRÓN** `volumen_spike_ratio` < `3.4561` → IC=+0.320 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.4561 (IC base=+0.310)

- **PATRÓN** `volumen_spike_ratio` > `6.1025` → IC=+0.308 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 6.1025 (IC base=+0.310)

- **PATRÓN** `libro_liquidez` > `1911.9404` → IC=+0.324 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1911.9404 (IC base=+0.310)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0021` → IC=+0.312 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0021 (IC base=+0.250)

- **PATRÓN** `sigma_h` > `0.003` → IC=+0.271 (n=59)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.003 (IC base=+0.250)

- **PATRÓN** `drift_60min` |x|≤ `0.1726` → IC=+0.290 (n=60)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1726 (IC base=+0.250)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.253 (n=83)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.250)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.271 (n=81)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.250)

- **PATRÓN** `ibs_20min` > `0.7312` → IC=+0.302 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7312 (IC base=+0.250)

- **PATRÓN** `dist_vwap_pct` < `0.3632` → IC=+0.285 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3632 (IC base=+0.250)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.807` → IC=+0.403 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.807 (IC base=+0.250)

- **PATRÓN** `volumen_regimen` > `0.6466` → IC=+0.280 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6466 (IC base=+0.250)

- **PATRÓN** `volumen_pendiente_norm` > `0.1159` → IC=+0.292 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1159 (IC base=+0.250)

- **PATRÓN** `volumen_spike_ratio` < `1.6243` → IC=+0.267 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6243 (IC base=+0.250)

- **PATRÓN** `volumen_spike_ratio` > `2.5456` → IC=+0.275 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5456 (IC base=+0.250)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.250 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.250)

- **PATRÓN** `libro_liquidez` > `2528.5027` → IC=+0.247 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2528.5027 (IC base=+0.250)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.267 (n=148)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.1413` → IC=+0.207 (n=148)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1413 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.214 (n=225)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` < `0.3172` → IC=+0.255 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3172 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.358` → IC=+0.262 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.358 (IC base=+0.190)

- **PATRÓN** `volumen_regimen` < `1.2379` → IC=+0.219 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2379 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` < `0.083` → IC=+0.222 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.083 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.24` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.24 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` < `1.9357` → IC=+0.290 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9357 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.190 (n=256)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.01 (IC base=+0.190)

- **PATRÓN** `ballena_activa_n` < `108.0` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 108.0 (IC base=+0.190)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **FILTRO** `ibs_20min` > `0.381` → IC=-0.194 (n=109)

  - _Acción_: SKIP cuando `ibs_20min` > 0.381
  - _Potencial_: sin este filtro IC_bueno=+0.264 (n=214)

- **PATRÓN** `ibs_20min` > `0.875` → IC=+0.184 (n=150)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.875 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.4` → IC=+0.190 (n=69)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 7.4 (IC base=+0.043)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.235 (n=81)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.109)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.243 (n=111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.109)

- **PATRÓN** `ibs_20min` < `0.381` → IC=+0.264 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.381 (IC base=+0.109)

- **PATRÓN** `dist_vwap_pct` > `0.5773` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.5773 (IC base=+0.109)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.974` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.974 (IC base=+0.109)

- **PATRÓN** `volumen_regimen` > `0.8699` → IC=+0.146 (n=162)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.8699 (IC base=+0.109)

- **PATRÓN** `volumen_pendiente_norm` > `0.1184` → IC=+0.211 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1184 (IC base=+0.109)

- **PATRÓN** `volumen_spike_ratio` > `2.2667` → IC=+0.185 (n=52)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.2667 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `2407.6604` → IC=+0.235 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2407.6604 (IC base=+0.109)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.239 (n=113)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.0828` → IC=+0.155 (n=82)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.0828 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.173 (n=111)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 7.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.227 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `0.2945` → IC=+0.176 (n=72)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.2945 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.0667` → IC=+0.137 (n=169)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.0667 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.308` → IC=+0.222 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.308 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.1183` → IC=+0.138 (n=244)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.1183 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.327` → IC=+0.177 (n=29)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.327 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `2.9818` → IC=+0.129 (n=208)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 2.9818 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.127 (n=250)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2468.9826` → IC=+0.127 (n=218)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 2468.9826 (IC base=+0.120)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.283 (n=228)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.266)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.274 (n=232)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.266)

- **PATRÓN** `drift_60min` |x|≤ `0.0817` → IC=+0.286 (n=87)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0817 (IC base=+0.266)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.281 (n=121)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.266)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.296 (n=96)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.266)

- **PATRÓN** `ibs_20min` < `0.3141` → IC=+0.308 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3141 (IC base=+0.266)

- **PATRÓN** `dist_vwap_pct` > `0.1301` → IC=+0.327 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1301 (IC base=+0.266)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.824` → IC=+0.296 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.824 (IC base=+0.266)

- **PATRÓN** `volumen_regimen` > `0.9` → IC=+0.310 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` > `0.2728` → IC=+0.365 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2728 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` > `1.7731` → IC=+0.265 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7731 (IC base=+0.266)

- **PATRÓN** `libro_liquidez` > `2636.658` → IC=+0.273 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2636.658 (IC base=+0.266)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 30.0 (IC base=+0.266)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.200 (n=108)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.040)

- **PATRÓN** `ibs_20min` > `0.9524` → IC=+0.170 (n=107)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.9524 (IC base=+0.040)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.717` → IC=+0.244 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.717 (IC base=+0.040)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.290 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.050)

- **PATRÓN** `ibs_20min` < `0.1429` → IC=+0.147 (n=120)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.1429 (IC base=+0.050)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.079` → IC=+0.239 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.079 (IC base=+0.050)

- **PATRÓN** `volumen_spike_ratio` < `2.6304` → IC=+0.122 (n=109)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.6304 (IC base=+0.050)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **FILTRO** `hora_utc` < `10.0` → IC=-0.283 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=21)

- **FILTRO** `volumen_regimen` < `0.9228` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9228
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=21)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.232 (n=39)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.2654` → IC=+0.183 (n=39)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.2654 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `19.0` → IC=+0.147 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 19.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.227 (n=31)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` < `0.1986` → IC=+0.256 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1986 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.889` → IC=+0.326 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.889 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `1.178` → IC=+0.159 (n=39)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.178 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` > `0.7151` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 0.7151 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.0902` → IC=+0.395 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0902 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `1.8271` → IC=+0.308 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8271 (IC base=+0.150)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0024` → IC=+0.237 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0024 (IC base=+0.217)

- **PATRÓN** `sigma_h` > `0.0027` → IC=+0.214 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0027 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.2558` → IC=+0.250 (n=34)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2558 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.284 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` > `0.9601` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9601 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.738` → IC=+0.452 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.738 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` < `0.9739` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9739 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` > `1.0973` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0973 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.1004` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1004 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` < `2.3331` → IC=+0.250 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3331 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.1374` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1374 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `3054.5848` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3054.5848 (IC base=+0.217)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.340 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.121)

- **PATRÓN** `drift_60min` |x|≤ `0.3225` → IC=+0.186 (n=49)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.3225 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.250 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` < `0.272` → IC=+0.144 (n=43)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.272 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.121` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.121 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `1.2077` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 1.2077 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `9264.2772` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9264.2772 (IC base=+0.121)

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

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.147 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 15.0 (IC base=+0.021)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.144 (n=57)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 1.0 (IC base=+0.021)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.989` → IC=+0.188 (n=30)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 7.989 (IC base=+0.021)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.132 (n=36)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` > 0.0059 (IC base=+0.041)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.197 (n=516)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0068 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.143 (n=573)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 17.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.96` → IC=+0.280 (n=701)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.96 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `0.3462` → IC=+0.176 (n=168)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.3462 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.251` → IC=+0.229 (n=1036)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.251 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.1809` → IC=+0.135 (n=362)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.1809 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2726.373` → IC=+0.152 (n=515)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 2726.373 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.176 (n=168)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 142.0 (IC base=+0.117)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.233 (n=1202)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.225)

- **PATRÓN** `sigma_h` > `0.0038` → IC=+0.232 (n=1364)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0038 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.236 (n=1247)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.287 (n=1371)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` < `0.1545` → IC=+0.199 (n=902)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1545 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.055` → IC=+0.253 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.055 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.498` → IC=+0.226 (n=1272)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.498 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` < `0.6189` → IC=+0.210 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6189 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` > `1.0629` → IC=+0.217 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0629 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` < `0.1128` → IC=+0.250 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1128 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.1795` → IC=+0.266 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1795 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` < `2.0113` → IC=+0.273 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0113 (IC base=+0.225)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.202 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 59.0 (IC base=+0.225)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.215 (n=177)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.159 (n=265)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 11.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` > `0.9463` → IC=+0.288 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9463 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.154` → IC=+0.352 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.154 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2113` → IC=+0.161 (n=57)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.2113 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.161 (n=281)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.06 (IC base=+0.129)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.315 (n=63)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.298)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.331 (n=63)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.298)

- **PATRÓN** `drift_60min` |x|≤ `0.2132` → IC=+0.339 (n=166)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2132 (IC base=+0.298)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.306 (n=178)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.298)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.310 (n=172)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.298)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.351 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.298)

- **PATRÓN** `volumen_pendiente_norm` < `0.069` → IC=+0.340 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.069 (IC base=+0.298)

- **PATRÓN** `volumen_spike_ratio` < `1.8956` → IC=+0.339 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8956 (IC base=+0.298)

- **PATRÓN** `volumen_spike_ratio` > `2.7667` → IC=+0.344 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7667 (IC base=+0.298)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.343 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.298)

- **PATRÓN** `libro_liquidez` > `1980.3` → IC=+0.361 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1980.3 (IC base=+0.298)

### GBM_LATE_15M_TARDIO#BTC#15min
- **FILTRO** `ibs_20min` < `0.4138` → IC=-0.187 (n=65)

  - _Acción_: SKIP cuando `ibs_20min` < 0.4138
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=133)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.147 (n=100)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0027 (IC base=+0.125)

- **PATRÓN** `sigma_h` > `0.0031` → IC=+0.171 (n=68)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0031 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.199 (n=101)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.4138` → IC=+0.278 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4138 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `0.3609` → IC=+0.300 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3609 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.71` → IC=+0.259 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.71 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `0.6564` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6564 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` > `0.9107` → IC=+0.153 (n=99)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.9107 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` < `0.1561` → IC=+0.179 (n=107)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` < 0.1561 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `2.8608` → IC=+0.224 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.8608 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `8838.1476` → IC=+0.243 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8838.1476 (IC base=+0.125)

- **PATRÓN** `sigma_h` < `0.0018` → IC=+0.204 (n=79)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0018 (IC base=+0.172)

- **PATRÓN** `sigma_h` > `0.0029` → IC=+0.176 (n=109)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0029 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.1874` → IC=+0.183 (n=206)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.1874 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.190 (n=240)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 6.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` < `0.4222` → IC=+0.226 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4222 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` < `0.135` → IC=+0.188 (n=254)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.135 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.232` → IC=+0.255 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.232 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `1.3025` → IC=+0.179 (n=235)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 1.3025 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` > `0.856` → IC=+0.190 (n=156)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 0.856 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.0974` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0974 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` < `1.6006` → IC=+0.328 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6006 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `5039.1995` → IC=+0.184 (n=210)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 5039.1995 (IC base=+0.172)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.238 (n=105)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0075 (IC base=+0.170)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.239 (n=117)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` > `0.717` → IC=+0.246 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.717 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.923` → IC=+0.339 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.923 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` < `0.2322` → IC=+0.167 (n=247)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` < 0.2322 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` < `2.1733` → IC=+0.151 (n=107)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.1733 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` > `4.0232` → IC=+0.161 (n=110)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 4.0232 (IC base=+0.170)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.188 (n=341)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.06 (IC base=+0.170)

- **PATRÓN** `libro_liquidez` > `1854.4986` → IC=+0.189 (n=210)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 1854.4986 (IC base=+0.170)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.364 (n=86)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.277)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.281 (n=176)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.277)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.304 (n=100)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.277)

- **PATRÓN** `ibs_20min` < `0.5455` → IC=+0.336 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5455 (IC base=+0.277)

- **PATRÓN** `volumen_pendiente_norm` < `0.2317` → IC=+0.229 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2317 (IC base=+0.277)

- **PATRÓN** `volumen_pendiente_norm` > `0.3726` → IC=+0.315 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3726 (IC base=+0.277)

- **PATRÓN** `volumen_spike_ratio` < `3.6434` → IC=+0.256 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.6434 (IC base=+0.277)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.300 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.277)

### GBM_LATE_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_20min` < `0.345` → IC=-0.217 (n=51)

  - _Acción_: SKIP cuando `ibs_20min` < 0.345
  - _Potencial_: sin este filtro IC_bueno=+0.201 (n=155)

- **PATRÓN** `sigma_h` < `0.0019` → IC=+0.204 (n=52)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0019 (IC base=+0.096)

- **PATRÓN** `drift_60min` |x|≤ `0.052` → IC=+0.148 (n=52)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.052 (IC base=+0.096)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.161 (n=57)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.345` → IC=+0.201 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.345 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.4271` → IC=+0.140 (n=23)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.4271 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.566` → IC=+0.216 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.566 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` < `0.7651` → IC=+0.171 (n=68)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.7651 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.29` → IC=+0.292 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.29 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` > `1.4389` → IC=+0.214 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4389 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `7083.9363` → IC=+0.253 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7083.9363 (IC base=+0.096)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.228 (n=112)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.2636` → IC=+0.149 (n=112)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.2636 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.176 (n=100)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 6.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.3` → IC=+0.240 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.1944` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1944 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.7` → IC=+0.259 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.7 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `0.8856` → IC=+0.210 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8856 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` < `0.1393` → IC=+0.323 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1393 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.2709` → IC=+0.283 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2709 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.4319` → IC=+0.280 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4319 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `6728.8499` → IC=+0.218 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6728.8499 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `128.0` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 128.0 (IC base=+0.147)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.230 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.017)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.923` → IC=+0.167 (n=139)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 2.923 (IC base=+0.017)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.165 (n=234)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0069 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.1759` → IC=+0.171 (n=156)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1759 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.217 (n=111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.236 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` < `0.1781` → IC=+0.161 (n=181)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1781 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.427` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.427 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.931` → IC=+0.148 (n=217)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 2.931 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `0.703` → IC=+0.205 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.703 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` > `1.2477` → IC=+0.163 (n=78)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 1.2477 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` < `0.1742` → IC=+0.306 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1742 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `2.4483` → IC=+0.287 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4483 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `1.6077` → IC=+0.300 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6077 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `1393.5337` → IC=+0.250 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1393.5337 (IC base=+0.142)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.193 (n=138)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0063 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.0741` → IC=+0.192 (n=102)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.0741 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=115)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.181 (n=111)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 6.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.248 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `0.329` → IC=+0.246 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.329 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.293` → IC=+0.213 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.293 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` > `0.6734` → IC=+0.137 (n=271)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.6734 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.327` → IC=+0.188 (n=30)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.327 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `1.7606` → IC=+0.126 (n=228)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 1.7606 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.147 (n=310)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `2472.2755` → IC=+0.134 (n=271)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2472.2755 (IC base=+0.128)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.287 (n=345)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0073 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.279 (n=315)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.259)

- **PATRÓN** `ibs_20min` < `0.1857` → IC=+0.367 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1857 (IC base=+0.259)

- **PATRÓN** `dist_vwap_pct` > `0.3858` → IC=+0.348 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3858 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.869` → IC=+0.322 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.869 (IC base=+0.259)

- **PATRÓN** `volumen_regimen` > `0.883` → IC=+0.297 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.883 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` > `0.326` → IC=+0.367 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.326 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` < `1.5056` → IC=+0.283 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5056 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` > `2.6664` → IC=+0.263 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6664 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `2841.183` → IC=+0.269 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2841.183 (IC base=+0.259)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.212 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.259)

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
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=182)

- **PATRÓN** `drift_60min` |x|≤ `0.0923` → IC=+0.152 (n=21)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.0923 (IC base=-0.008)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.173 (n=148)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0039 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.15` → IC=+0.186 (n=100)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.15 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.204 (n=52)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.140 (n=148)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.5 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.52` → IC=+0.149 (n=35)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 11.52 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `1.4038` → IC=+0.153 (n=148)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.4038 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` < `0.2331` → IC=+0.141 (n=157)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` < 0.2331 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `2.8806` → IC=+0.158 (n=147)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.8806 (IC base=+0.118)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.147 (n=182)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `7518.5292` → IC=+0.140 (n=148)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 7518.5292 (IC base=+0.118)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.145 (n=91)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0032 (IC base=+0.110)

- **PATRÓN** `drift_60min` |x|≤ `0.0712` → IC=+0.227 (n=31)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0712 (IC base=+0.110)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.129 (n=68)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 9.0 (IC base=+0.110)

- **PATRÓN** `ibs_20min` < `0.1047` → IC=+0.182 (n=61)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.1047 (IC base=+0.110)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.34` → IC=+0.130 (n=79)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` < 6.34 (IC base=+0.110)

- **PATRÓN** `volumen_pendiente_norm` > `0.1563` → IC=+0.203 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1563 (IC base=+0.110)

- **PATRÓN** `volumen_spike_ratio` < `2.7111` → IC=+0.145 (n=91)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.7111 (IC base=+0.110)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.278 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.231)

- **PATRÓN** `sigma_h` > `0.002` → IC=+0.230 (n=35)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.002 (IC base=+0.231)

- **PATRÓN** `drift_60min` |x|≤ `0.2097` → IC=+0.321 (n=26)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2097 (IC base=+0.231)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.333 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.231)

- **PATRÓN** `ibs_20min` > `0.2009` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2009 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.567` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.567 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.809` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.809 (IC base=+0.231)

- **PATRÓN** `volumen_regimen` < `1.4038` → IC=+0.306 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.4038 (IC base=+0.231)

- **PATRÓN** `volumen_pendiente_norm` < `0.0808` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0808 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` < `1.8229` → IC=+0.315 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8229 (IC base=+0.231)

- **PATRÓN** `libro_liquidez` > `7397.5021` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7397.5021 (IC base=+0.231)

### GBM_LATE_60M
- **FILTRO** `ibs_20min` < `0.7083` → IC=-0.173 (n=53)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7083
  - _Potencial_: sin este filtro IC_bueno=+0.232 (n=110)

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

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.176 (n=143)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0054 (IC base=+0.058)

- **PATRÓN** `ibs_20min` > `0.7083` → IC=+0.232 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7083 (IC base=+0.058)

- **PATRÓN** `dist_vwap_pct` > `0.1249` → IC=+0.138 (n=67)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.1249 (IC base=+0.058)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.521` → IC=+0.217 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.521 (IC base=+0.058)

- **PATRÓN** `volumen_regimen` > `1.0933` → IC=+0.174 (n=41)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 1.0933 (IC base=+0.058)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.7342` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7342
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
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.058)

- **PATRÓN** `ibs_20min` > `0.7342` → IC=+0.198 (n=41)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.7342 (IC base=+0.058)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `hora_utc` > `5.0` → IC=-0.360 (n=41)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=22)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.233 (n=28)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.122 (n=88)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 5.0 (IC base=+0.102)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.365 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.102)

- **PATRÓN** `dist_vwap_pct` < `0.2012` → IC=+0.226 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2012 (IC base=+0.102)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.41` → IC=+0.322 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.41 (IC base=+0.102)

- **PATRÓN** `volumen_regimen` < `0.5932` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.5932 (IC base=+0.102)

- **PATRÓN** `volumen_regimen` > `1.0696` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0696 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `2351.5975` → IC=+0.235 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2351.5975 (IC base=+0.102)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0165` → IC=-0.309 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0165
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=58)

- **FILTRO** `ibs_20min` > `0.2381` → IC=-0.308 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2381
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=12)

- **PATRÓN** `sigma_h` > `0.0135` → IC=+0.250 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0135 (IC base=-0.013)

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
- **FILTRO** `ibs_20min` < `0.5407` → IC=-0.286 (n=26)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5407
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=20)

- **FILTRO** `dist_vwap_pct` < `0.0931` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0931
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=13)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` < `9.988` → IC=-0.462 (n=24)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 9.988
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **FILTRO** `sigma_h` > `0.0018` → IC=-0.346 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0018
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `ibs_20min` < `0.6` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.441 (n=15)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `ibs_20min` > `0.6429` → IC=+0.149 (n=132)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` > 0.6429 (IC base=+0.062)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.186 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 15.0 (IC base=+0.026)

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

- **PATRÓN** `drift_60min` |x|≤ `0.1242` → IC=+0.177 (n=29)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.1242 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.094)

- **PATRÓN** `ibs_20min` < `0.3394` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.3394 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.84` → IC=+0.167 (n=34)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 3.84 (IC base=+0.094)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `0.9489` → IC=+0.283 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9489 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.991` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.991 (IC base=+0.174)

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
- **PATRÓN** `hora_utc` < `8.0` → IC=+0.309 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.210)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.505 (IC base=+0.210)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` < `8.0` → IC=+0.309 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.210)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.505 (IC base=+0.210)

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
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=25)

- **FILTRO** `libro_liquidez` < `5915.3552` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_liquidez` < 5915.3552
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=20)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.133 (n=28)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=26)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9732` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9732
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=61)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.204 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=56)

### MOMENTUM_IBS_15M#BNB#15min
- **PATRÓN** `libro_liquidez` > `2255.3349` → IC=+0.140 (n=23)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 2255.3349 (IC base=-0.011)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.176 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 8.0 (IC base=+0.123)

- **PATRÓN** `drift_20min_pct` |x|≤ `0.0647` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_20min_pct` |x|≤ 0.0647 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.0947` → IC=+0.179 (n=26)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.0947 (IC base=+0.123)

### MOMENTUM_IBS_15M#BTC#15min
- **PATRÓN** `hora_utc` < `5.0` → IC=+0.167 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 5.0 (IC base=+0.054)

- **PATRÓN** `drift_20min_pct` |x|≤ `0.0549` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `drift_20min_pct` |x|≤ 0.0549 (IC base=+0.054)

- **PATRÓN** `ibs_20min` > `0.1002` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.1002 (IC base=+0.054)

- **PATRÓN** `libro_liquidez` > `20061.6367` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 20061.6367 (IC base=+0.054)

### MOMENTUM_IBS_15M#DOGE#15min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=23)

- **FILTRO** `ibs_20min` > `0.7917` → IC=-0.167 (n=28)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7917
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=15)

### MOMENTUM_IBS_15M#ETH#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.114)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.204 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.114)

- **PATRÓN** `drift_20min_pct` |x|≤ `0.0569` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_20min_pct` |x|≤ 0.0569 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `15313.5075` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15313.5075 (IC base=+0.114)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.42` → IC=-0.270 (n=98)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=299)

- **FILTRO** `ibs_20min` < `0.7265` → IC=-0.233 (n=99)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7265
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=298)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.210 (n=98)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=299)

- **FILTRO** `libro_liquidez` < `2147.8152` → IC=-0.144 (n=262)

  - _Acción_: SKIP cuando `libro_liquidez` < 2147.8152
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=135)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `hora_utc` < `10.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.096 (n=45)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.130 (n=44)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=37)

- **FILTRO** `ibs_20min` < `0.7175` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7175
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=47)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `hora_utc` > `18.0` → IC=-0.265 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=53)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.242 (n=29)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=39)

- **FILTRO** `ballena_activa_n` > `28.0` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `ballena_activa_n` > 28.0
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=45)

- **FILTRO** `hora_utc` > `9.0` → IC=-0.148 (n=52)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=27)

- **FILTRO** `ibs_20min` > `0.1707` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1707
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=53)

- **FILTRO** `ballena_activa_n` > `49.0` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `ballena_activa_n` > 49.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=60)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.233 (n=28)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=38)

- **FILTRO** `ibs_20min` < `0.7235` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7235
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=50)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.224 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=37)

- **FILTRO** `ballena_activa_n` > `19.0` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `ballena_activa_n` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=49)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.214 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.5 (IC base=+0.058)

- **PATRÓN** `drift_20min_pct` |x|≤ `0.0739` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `drift_20min_pct` |x|≤ 0.0739 (IC base=+0.058)

### MOMENTUM_IBS_15M_BALLENA#SOL#15min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.190 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=38)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.259 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=38)

- **FILTRO** `ibs_20min` < `0.7241` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7241
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=49)

- **FILTRO** `ballena_activa_n` > `20.0` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=49)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.326 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=51)

- **FILTRO** `ibs_20min` < `0.7349` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7349
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=54)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=57)

- **FILTRO** `libro_liquidez` < `602.3442` → IC=-0.158 (n=36)

  - _Acción_: SKIP cuando `libro_liquidez` < 602.3442
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=36)

- **FILTRO** `py_entrada` > `0.53` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=54)

- **PATRÓN** `py_entrada` < `0.515` → IC=+0.128 (n=49)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.515 (IC base=+0.021)

- **PATRÓN** `libro_liquidez` > `2677.2264` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2677.2264 (IC base=+0.021)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `hora_utc` < `16.0` → IC=-0.300 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=99)

- **FILTRO** `hora_utc` > `19.0` → IC=-0.206 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.118 (n=100)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=154)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `ibs_20min` < `0.9919` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `ibs_20min` < 0.9919
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `hora_utc` < `19.0` → IC=-0.300 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

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
- **FILTRO** `hora_utc` < `14.0` → IC=-0.151 (n=537)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=570)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.289 (n=263)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=844)

- **FILTRO** `ibs_7min` < `0.7242` → IC=-0.245 (n=276)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7242
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=831)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.202 (n=273)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=834)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.208 (n=289)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=880)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.221 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=133)

- **FILTRO** `ballena_activa_n` > `2.0` → IC=-0.180 (n=123)

  - _Acción_: SKIP cuando `ballena_activa_n` > 2.0
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=51)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.210 (n=36)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=129)

- **FILTRO** `drift_7min_pct` |x|> `0.1123` → IC=-0.198 (n=41)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1123
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=124)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.158 (n=71)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=166)

- **FILTRO** `py_entrada` < `0.38` → IC=-0.276 (n=56)

  - _Acción_: SKIP cuando `py_entrada` < 0.38
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=181)

- **FILTRO** `ibs_7min` < `0.8176` → IC=-0.221 (n=59)

  - _Acción_: SKIP cuando `ibs_7min` < 0.8176
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=178)

- **FILTRO** `ballena_activa_n` > `102.0` → IC=-0.189 (n=59)

  - _Acción_: SKIP cuando `ballena_activa_n` > 102.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=178)

- **FILTRO** `py_entrada` > `0.56` → IC=-0.220 (n=48)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=149)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.192 (n=76)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=79)

- **FILTRO** `py_entrada` < `0.28` → IC=-0.425 (n=38)

  - _Acción_: SKIP cuando `py_entrada` < 0.28
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=117)

- **FILTRO** `ibs_7min` < `0.7` → IC=-0.255 (n=51)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=104)

- **FILTRO** `ballena_activa_n` > `16.0` → IC=-0.250 (n=38)

  - _Acción_: SKIP cuando `ballena_activa_n` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=117)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.198 (n=94)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.090 (n=103)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.250 (n=90)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=95)

- **FILTRO** `ibs_7min` < `0.837` → IC=-0.229 (n=46)

  - _Acción_: SKIP cuando `ibs_7min` < 0.837
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=139)

- **FILTRO** `ballena_activa_n` > `2.0` → IC=-0.177 (n=122)

  - _Acción_: SKIP cuando `ballena_activa_n` > 2.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=63)

- **FILTRO** `libro_liquidez` < `9023.0458` → IC=-0.169 (n=122)

  - _Acción_: SKIP cuando `libro_liquidez` < 9023.0458
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=63)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.146 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=161)

- **FILTRO** `py_entrada` < `0.42` → IC=-0.236 (n=51)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=156)

- **FILTRO** `ibs_7min` < `0.7857` → IC=-0.192 (n=50)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7857
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=157)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.269 (n=76)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=73)

- **FILTRO** `ibs_7min` < `0.7368` → IC=-0.304 (n=49)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7368
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=100)

- **FILTRO** `ballena_activa_n` > `18.0` → IC=-0.289 (n=36)

  - _Acción_: SKIP cuando `ballena_activa_n` > 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=113)

- **FILTRO** `libro_liquidez` < `1961.2126` → IC=-0.170 (n=98)

  - _Acción_: SKIP cuando `libro_liquidez` < 1961.2126
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=51)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.240 (n=71)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=138)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.158 (n=74)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` < 0.5 (IC base=-0.031)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=71)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=83)

- **PATRÓN** `drift_7min_pct` |x|≤ `0.0246` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `drift_7min_pct` |x|≤ 0.0246 (IC base=+0.060)

- **PATRÓN** `libro_liquidez` > `10993.3675` → IC=+0.132 (n=74)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 10993.3675 (IC base=+0.060)

### ORDER_FLOW_5M
- **FILTRO** `total_vol_5m` > `215.224` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `total_vol_5m` > 215.224
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `delta_ratio` |x|> `0.4012` → IC=+0.164 (n=141)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.82€ cuando `delta_ratio` |x|> 0.4012 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.158 (n=71)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 18.0 (IC base=+0.135)

- **PATRÓN** `total_vol_5m` < `357.983` → IC=+0.238 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 357.983 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.149 (n=55)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.02 (IC base=+0.135)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.2125` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.2125
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=38)

- **FILTRO** `pct_vs_K` |x|> `4.502` → IC=-0.470 (n=31)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.502
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=63)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.257 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=-0.142)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0028` → IC=-0.329 (n=39)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0028
  - _Potencial_: sin este filtro IC_bueno=+0.312 (n=14)

- **FILTRO** `T_h` > `87.9756` → IC=-0.426 (n=25)

  - _Acción_: SKIP cuando `T_h` > 87.9756
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=13)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0132` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0132
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `T_h` > `95.1632` → IC=-0.337 (n=41)

  - _Acción_: SKIP cuando `T_h` > 95.1632
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=17)

- **FILTRO** `sigma_h` > `0.0034` → IC=-0.337 (n=41)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=15)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` > `0.0034` → IC=-0.324 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0033` → IC=-0.237 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **FILTRO** `T_h` > `111.9957` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `T_h` > 111.9957
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **FILTRO** `sigma_h` > `0.0035` → IC=-0.237 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0035
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

### STREAK_FADE_15M
- **FILTRO** `hora_utc` < `8.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `streak_estiramiento` > `0.4156` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4156
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

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
- **FILTRO** `ballena_activa_n` > `20.0` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `ballena_activa_n` > 20.0
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.154 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=13)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=16)

- **FILTRO** `hora_utc` < `14.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.495 (IC base=-0.035)

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
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=62)

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
- **FILTRO** `libro_liquidez` < `3496.0203` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_liquidez` < 3496.0203
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=27)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=72)

- **PATRÓN** `hora_utc` > `20.0` → IC=+0.184 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 20.0 (IC base=+0.000)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.208 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.073)

- **PATRÓN** `streak_len` < `3.0` → IC=+0.122 (n=72)

  - _Acción_: Kelly boost +0.61€ cuando `streak_len` < 3.0 (IC base=+0.073)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=696)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=393)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=401)

### UPDOWN_GBM#15min
- **FILTRO** `ibs_15` < `0.5714` → IC=-0.155 (n=137)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5714
  - _Potencial_: sin este filtro IC_bueno=+0.221 (n=281)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.130 (n=209)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` > 0.0048 (IC base=+0.098)

- **PATRÓN** `ibs_15` > `0.5714` → IC=+0.221 (n=281)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5714 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `0.4246` → IC=+0.172 (n=62)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.4246 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.027` → IC=+0.224 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.027 (IC base=+0.098)

- **PATRÓN** `ibs_15` < `0.45` → IC=+0.127 (n=371)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.64€ cuando `ibs_15` < 0.45 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` > `0.5751` → IC=+0.189 (n=43)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.5751 (IC base=+0.081)

### UPDOWN_GBM#5min
- **FILTRO** `hora_utc` > `8.0` → IC=-0.133 (n=118)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=134)

- **FILTRO** `ibs_15` < `0.1461` → IC=-0.241 (n=83)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1461
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=169)

- **FILTRO** `dist_vwap_pct` > `0.2843` → IC=-0.133 (n=47)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2843
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=179)

- **FILTRO** `sigma_ewma_delta_pct` > `5.225` → IC=-0.177 (n=63)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.225
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=189)

### UPDOWN_GBM#60min
- **FILTRO** `hora_utc` < `11.0` → IC=-0.269 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=132)

- **FILTRO** `ibs_15` < `0.592` → IC=-0.183 (n=39)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.592
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=117)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.0016` → IC=-0.200 (n=28)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0016
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=30)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.122 (n=80)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.03 (IC base=+0.000)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `sigma_h` < `0.0039` → IC=-0.324 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0039
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=15)

- **FILTRO** `ibs_15` < `0.3405` → IC=-0.265 (n=15)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.3405
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=15)

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

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.0186` → IC=+0.131 (n=63)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +0.65€ cuando `pct_spot_vs_ref` |x|≤ 0.0186 (IC base=+0.091)

- **PATRÓN** `sigma_h` < `0.0021` → IC=+0.273 (n=42)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0021 (IC base=+0.091)

- **PATRÓN** `drift_60min` |x|≤ `0.147` → IC=+0.146 (n=63)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.147 (IC base=+0.091)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.952` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.952 (IC base=+0.091)

- **PATRÓN** `libro_liquidez` > `10025.3913` → IC=+0.125 (n=94)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 10025.3913 (IC base=+0.091)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `ibs_15` < `0.6848` → IC=-0.214 (n=19)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6848
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=40)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `ibs_15` < `0.7055` → IC=-0.146 (n=46)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.7055
  - _Potencial_: sin este filtro IC_bueno=+0.333 (n=46)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1329` → IC=+0.208 (n=46)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1329 (IC base=+0.096)

- **PATRÓN** `ibs_15` > `0.7055` → IC=+0.333 (n=46)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7055 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` < `0.1005` → IC=+0.207 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1005 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.937` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 8.937 (IC base=+0.096)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.167 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0028 (IC base=+0.140)

- **PATRÓN** `sigma_h` > `0.004` → IC=+0.210 (n=67)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.004 (IC base=+0.140)

- **PATRÓN** `drift_15min` |x|≤ `0.5015` → IC=+0.138 (n=45)

  - _Acción_: Kelly boost +0.69€ cuando `drift_15min` |x|≤ 0.5015 (IC base=+0.140)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1157` → IC=+0.141 (n=90)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.71€ cuando `delta_ratio_macro` |x|> 0.1157 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.149 (n=92)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 7.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.153 (n=93)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 14.0 (IC base=+0.140)

- **PATRÓN** `ibs_15` < `0.3247` → IC=+0.160 (n=101)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.80€ cuando `ibs_15` < 0.3247 (IC base=+0.140)

- **PATRÓN** `ibs_15` > `0.0304` → IC=+0.180 (n=101)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.90€ cuando `ibs_15` > 0.0304 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.4732` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4732 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `23.05` → IC=+0.196 (n=100)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` < 23.05 (IC base=+0.140)

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
  - _Potencial_: sin este filtro IC_bueno=+0.132 (n=55)

- **PATRÓN** `sigma_h` < `0.0019` → IC=+0.208 (n=22)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0019 (IC base=+0.073)

- **PATRÓN** `drift_15min` |x|≤ `0.4204` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `drift_15min` |x|≤ 0.4204 (IC base=+0.073)

- **PATRÓN** `ballena_activa_n` < `3.0` → IC=+0.132 (n=55)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 3.0 (IC base=+0.073)

### UPDOWN_GBM#ETH#60min
- **PATRÓN** `delta_ratio_macro` |x|> `0.1688` → IC=+0.145 (n=29)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.73€ cuando `delta_ratio_macro` |x|> 0.1688 (IC base=+0.023)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.02 (IC base=+0.023)

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

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.130 (n=44)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 8.0 (IC base=+0.046)

- **PATRÓN** `ibs_15` < `0.1034` → IC=+0.300 (n=28)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1034 (IC base=+0.046)

### UPDOWN_GBM#SOL#60min
- **FILTRO** `hora_utc` < `16.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=10)

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

- **PATRÓN** `drift_60min` |x|≤ `0.1146` → IC=+0.217 (n=44)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1146 (IC base=+0.106)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0793` → IC=+0.151 (n=130)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio_macro` |x|> 0.0793 (IC base=+0.106)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.137 (n=122)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 16.0 (IC base=+0.106)

- **PATRÓN** `ibs_15` < `0.2353` → IC=+0.189 (n=88)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.94€ cuando `ibs_15` < 0.2353 (IC base=+0.106)

- **PATRÓN** `dist_vwap_pct` > `0.127` → IC=+0.227 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.127 (IC base=+0.106)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.421` → IC=+0.154 (n=108)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 5.421 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `2605.055` → IC=+0.152 (n=116)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 2605.055 (IC base=+0.106)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1934` → IC=+0.257 (n=72)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1934 (IC base=+0.248)

- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.289 (n=36)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0022 (IC base=+0.248)

- **PATRÓN** `sigma_h` > `0.0032` → IC=+0.250 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0032 (IC base=+0.248)

- **PATRÓN** `drift_60min` |x|≤ `0.1599` → IC=+0.270 (n=72)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1599 (IC base=+0.248)

- **PATRÓN** `drift_15min` |x|≤ `0.4089` → IC=+0.263 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4089 (IC base=+0.248)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1438` → IC=+0.254 (n=55)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1438 (IC base=+0.248)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.256 (n=80)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.248)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.257 (n=72)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.248)

- **PATRÓN** `ibs_15` > `0.7088` → IC=+0.309 (n=82)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7088 (IC base=+0.248)

- **PATRÓN** `dist_vwap_pct` > `0.3445` → IC=+0.328 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3445 (IC base=+0.248)

- **PATRÓN** `dist_vwap_pct` < `0.0842` → IC=+0.261 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0842 (IC base=+0.248)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.854` → IC=+0.284 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.854 (IC base=+0.248)

- **PATRÓN** `libro_liquidez` > `3141.8886` → IC=+0.250 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3141.8886 (IC base=+0.248)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.2095` → IC=+0.245 (n=53)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.2095 (IC base=+0.208)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.245 (n=53)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.1567` → IC=+0.235 (n=47)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1567 (IC base=+0.208)

- **PATRÓN** `drift_15min` |x|≤ `0.411` → IC=+0.269 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.411 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.241 (n=52)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.208)

- **PATRÓN** `ibs_15` < `0.9942` → IC=+0.209 (n=53)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.9942 (IC base=+0.208)

- **PATRÓN** `ibs_15` > `0.7314` → IC=+0.245 (n=53)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7314 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `0.2982` → IC=+0.350 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2982 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.854` → IC=+0.214 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.854 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` < `15.945` → IC=+0.208 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 15.945 (IC base=+0.208)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `dist_vwap_pct` < `0.058` → IC=+0.350 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.058 (IC base=+0.305)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.414` → IC=+0.389 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.414 (IC base=+0.305)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `ibs_15` < `0.6371` → IC=-0.252 (n=115)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6371
  - _Potencial_: sin este filtro IC_bueno=+0.235 (n=115)

- **FILTRO** `sigma_ewma_delta_pct` > `12.903` → IC=-0.155 (n=227)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 12.903
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=920)

- **PATRÓN** `ibs_15` > `0.6371` → IC=+0.235 (n=115)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6371 (IC base=-0.042)

- **PATRÓN** `ibs_15` < `0.2364` → IC=+0.312 (n=30)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2364 (IC base=-0.049)

- **PATRÓN** `dist_vwap_pct` < `0.0929` → IC=+0.159 (n=42)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.0929 (IC base=-0.049)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0033` → IC=-0.224 (n=85)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=167)

- **FILTRO** `hora_utc` < `7.0` → IC=-0.253 (n=79)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.169 (n=173)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.209 (n=53)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=199)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `drift_60min` |x|> `0.2095` → IC=-0.239 (n=21)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2095
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=66)

- **FILTRO** `ibs_15` < `0.4646` → IC=-0.367 (n=43)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.4646
  - _Potencial_: sin este filtro IC_bueno=+0.152 (n=44)

- **PATRÓN** `ibs_15` > `0.4646` → IC=+0.152 (n=44)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.76€ cuando `ibs_15` > 0.4646 (IC base=-0.107)

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1184` → IC=+0.219 (n=30)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1184 (IC base=+0.181)

- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.180 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0045 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.1816` → IC=+0.180 (n=23)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.1816 (IC base=+0.181)

- **PATRÓN** `drift_15min` |x|≤ `0.6645` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `drift_15min` |x|≤ 0.6645 (IC base=+0.181)

- **PATRÓN** `ibs_15` < `0.3879` → IC=+0.312 (n=30)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3879 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.307` → IC=+0.224 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 8.307 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `3786.4324` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 3786.4324 (IC base=+0.181)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` > `14.141` → IC=-0.182 (n=61)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 14.141
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=351)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.749` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.749 (IC base=-0.004)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` < `0.005` → IC=-0.160 (n=48)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=100)

- **FILTRO** `libro_liquidez` < `2477.03` → IC=-0.192 (n=37)

  - _Acción_: SKIP cuando `libro_liquidez` < 2477.03
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=111)

- **FILTRO** `sigma_ewma_delta_pct` > `7.956` → IC=-0.137 (n=89)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.956
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=286)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` > `0.0027` → IC=+0.284 (n=72)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0027 (IC base=+0.252)

- **PATRÓN** `drift_60min` |x|≤ `0.1819` → IC=+0.264 (n=108)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1819 (IC base=+0.252)

- **PATRÓN** `drift_15min` |x|≤ `0.6305` → IC=+0.263 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.6305 (IC base=+0.252)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0673` → IC=+0.273 (n=108)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0673 (IC base=+0.252)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.300 (n=98)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.252)

- **PATRÓN** `ibs_15` > `0.9358` → IC=+0.324 (n=72)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9358 (IC base=+0.252)

- **PATRÓN** `dist_vwap_pct` > `0.3696` → IC=+0.333 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3696 (IC base=+0.252)

- **PATRÓN** `dist_vwap_pct` < `0.0774` → IC=+0.294 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0774 (IC base=+0.252)

- **PATRÓN** `sigma_ewma_delta_pct` > `14.467` → IC=+0.255 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 14.467 (IC base=+0.252)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.98` → IC=+0.262 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.98 (IC base=+0.252)

- **PATRÓN** `libro_liquidez` > `5299.0462` → IC=+0.257 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5299.0462 (IC base=+0.252)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.2049` → IC=+0.254 (n=67)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.2049 (IC base=+0.233)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.239 (n=67)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.233)

- **PATRÓN** `sigma_h` > `0.0022` → IC=+0.254 (n=59)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0022 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.1837` → IC=+0.268 (n=67)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1837 (IC base=+0.233)

- **PATRÓN** `drift_15min` |x|≤ `0.6592` → IC=+0.254 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.6592 (IC base=+0.233)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0911` → IC=+0.238 (n=59)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0911 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.290 (n=60)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.233)

- **PATRÓN** `ibs_15` < `0.9998` → IC=+0.239 (n=67)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.9998 (IC base=+0.233)

- **PATRÓN** `ibs_15` > `0.8845` → IC=+0.271 (n=59)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8845 (IC base=+0.233)

- **PATRÓN** `dist_vwap_pct` > `0.3722` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3722 (IC base=+0.233)

- **PATRÓN** `dist_vwap_pct` < `0.0966` → IC=+0.269 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0966 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.763` → IC=+0.237 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.763 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.495` → IC=+0.245 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.495 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `5486.381` → IC=+0.261 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5486.381 (IC base=+0.233)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.269 (n=37)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.272)

- **PATRÓN** `sigma_h` > `0.0028` → IC=+0.295 (n=37)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0028 (IC base=+0.272)

- **PATRÓN** `drift_60min` |x|≤ `0.1546` → IC=+0.269 (n=37)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1546 (IC base=+0.272)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1843` → IC=+0.405 (n=19)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1843 (IC base=+0.272)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.318 (n=31)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.272)

- **PATRÓN** `ibs_15` > `0.9815` → IC=+0.405 (n=19)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9815 (IC base=+0.272)

- **PATRÓN** `dist_vwap_pct` < `0.0728` → IC=+0.346 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0728 (IC base=+0.272)

- **PATRÓN** `sigma_ewma_delta_pct` < `16.209` → IC=+0.275 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 16.209 (IC base=+0.272)

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
- **FILTRO** `pct_spot_vs_ref` |x|> `0.109` → IC=-0.278 (n=16)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.109
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.278 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2205` → IC=-0.278 (n=16)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2205
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
- **PATRÓN** `T_h` < `111.9997` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `T_h` < 111.9997 (IC base=+0.021)

- **PATRÓN** `T_h` > `146.1132` → IC=+0.453 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1132 (IC base=+0.352)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` < `100.962` → IC=+0.346 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 100.962 (IC base=+0.276)

- **PATRÓN** `pct_dist` |x|≤ `0.6014` → IC=+0.276 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `pct_dist` |x|≤ 0.6014 (IC base=+0.276)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `111.9838` → IC=+0.320 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9838 (IC base=+0.314)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1359` → IC=+0.457 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1359 (IC base=+0.425)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#SOL#5min**: dentro de BUY_NO, IBS < 0.1034 sube el IC de +0.046 a +0.300 en UPDOWN_GBM#SOL#5min (n=28). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5714 sube el IC de +0.098 a +0.221 en UPDOWN_GBM#15min (n=281). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.9375 sube el IC de +0.115 a +0.235 en UPDOWN_GBM#BTC#15min (n=32). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.7055 sube el IC de +0.096 a +0.333 en UPDOWN_GBM#ETH#15min (n=46). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_NO, IBS < 0.3247 sube el IC de +0.140 a +0.160 en UPDOWN_GBM#ETH#15min (n=101). Ya aplicado como kelly_boost=+0.80€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_NO, IBS > 0.0304 sube el IC de +0.140 a +0.180 en UPDOWN_GBM#ETH#15min (n=101). Ya aplicado como kelly_boost=+0.90€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.033 a +0.242 en UPDOWN_GBM#SOL#15min (n=29). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.55 sube el IC de +0.085 a +0.182 en UPDOWN_GBM#XRP#15min (n=86). Ya aplicado como kelly_boost=+0.91€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.2353 sube el IC de +0.106 a +0.189 en UPDOWN_GBM#XRP#15min (n=88). Ya aplicado como kelly_boost=+0.94€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6371 sube el IC de -0.042 a +0.235 en UPDOWN_GBM_15M_TARDIO (n=115). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.2364 sube el IC de -0.049 a +0.312 en UPDOWN_GBM_15M_TARDIO (n=30). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.4646 sube el IC de -0.107 a +0.152 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=44). Ya aplicado como kelly_boost=+0.76€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3879 sube el IC de +0.181 a +0.312 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=30). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.9358 sube el IC de +0.252 a +0.324 en UPDOWN_GBM_IBS_ALTO (n=72). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS < 0.9998 sube el IC de +0.233 a +0.239 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=67). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8845 sube el IC de +0.233 a +0.271 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=59). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.9815 sube el IC de +0.272 a +0.405 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=19). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7088 sube el IC de +0.248 a +0.309 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=82). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS < 0.9942 sube el IC de +0.208 a +0.209 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=53). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.7314 sube el IC de +0.208 a +0.245 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=53). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min` — IC=+0.305 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH` — IC=+0.305 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min` — IC=+0.427 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL` — IC=+0.427 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 489 | +0.046 | +39.63€ | 3 | 4 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 489 | +0.046 | +39.63€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 252 | +0.043 | +24.96€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 252 | +0.043 | +24.96€ | 2 | 4 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 210 | +0.024 | -0.34€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 210 | +0.024 | -0.34€ | 7 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 27 | +0.224 | +15.01€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 27 | +0.224 | +15.01€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 3402 | -0.113 | -534.69€ | 2 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 462 | -0.024 | -18.13€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 2940 | -0.127 | -516.57€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 373 | -0.183 | -97.05€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 373 | -0.183 | -97.05€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 462 | -0.024 | -18.13€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 462 | -0.024 | -18.13€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 311 | -0.161 | -150.75€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 311 | -0.161 | -150.75€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 725 | -0.137 | -38.80€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 725 | -0.137 | -38.80€ | 2 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 830 | +0.001 | -100.60€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 830 | +0.001 | -100.60€ | 0 | 0 |
| 🚫 BALLENAS_TARDIAS#XRP | 701 | -0.223 | -129.36€ | 0 | 0 |
| 🚫 BALLENAS_TARDIAS#XRP#5min | 701 | -0.223 | -129.36€ | 1 | 0 |
| ✅ FAVORITO_CONFIRMADO | 14671 | +0.115 | -849.51€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 3419 | +0.182 | -103.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 99 | -0.104 | -47.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 8548 | +0.086 | -725.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 2605 | +0.132 | +27.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 1442 | +0.032 | -315.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 13 | -0.065 | -2.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 1425 | +0.035 | -307.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 3324 | +0.141 | +0.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 933 | +0.196 | -32.88€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 41 | -0.105 | -20.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 1423 | +0.113 | -9.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 927 | +0.138 | +62.83€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 1440 | +0.054 | -252.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 9 | -0.021 | -3.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 1430 | +0.055 | -246.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 3595 | +0.127 | -38.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 1263 | +0.162 | -18.35€ | 0 | 7 |
| 🚫 FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 1420 | +0.105 | -16.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 900 | +0.117 | +5.30€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 3431 | +0.135 | -206.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 1189 | +0.198 | -48.62€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 40 | +0.000 | -9.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 1424 | +0.082 | -108.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 778 | +0.141 | -40.75€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 1439 | +0.125 | -36.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 12 | +0.043 | +1.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 1426 | +0.126 | -36.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3494 | +0.159 | -341.36€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 3494 | +0.159 | -341.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 876 | +0.154 | -115.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 876 | +0.154 | -115.73€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 78 | -0.113 | -5.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 78 | -0.113 | -5.72€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 866 | +0.158 | -109.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 866 | +0.158 | -109.64€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 775 | +0.218 | -42.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 775 | +0.218 | -42.04€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 1 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 820 | +0.172 | -81.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 820 | +0.172 | -81.98€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 167 | +0.417 | -8.03€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 167 | +0.417 | -8.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 60 | +0.419 | -1.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 60 | +0.419 | -1.50€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 66 | +0.382 | -6.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 66 | +0.382 | -6.91€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 39 | +0.427 | +0.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 39 | +0.427 | +0.34€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 6072 | +0.188 | -574.28€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 6072 | +0.188 | -574.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 1138 | +0.097 | -258.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 1138 | +0.097 | -258.21€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 933 | +0.248 | -9.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 933 | +0.248 | -9.13€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 1069 | +0.151 | -157.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 1069 | +0.151 | -157.84€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 974 | +0.223 | -38.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 974 | +0.223 | -38.09€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 946 | +0.246 | -12.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 946 | +0.246 | -12.03€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 1012 | +0.187 | -98.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 1012 | +0.187 | -98.98€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 2178 | +0.150 | +126.00€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 2178 | +0.150 | +126.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 1076 | +0.158 | +76.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 1076 | +0.158 | +76.52€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 1102 | +0.142 | +49.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 1102 | +0.142 | +49.49€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 539 | +0.298 | +3.05€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 539 | +0.298 | +3.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 226 | +0.272 | -9.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 226 | +0.272 | -9.81€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 252 | +0.299 | +5.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 252 | +0.299 | +5.81€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 61 | +0.373 | +7.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 61 | +0.373 | +7.05€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 228 | +0.409 | -11.14€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 228 | +0.409 | -11.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 102 | +0.404 | -5.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 102 | +0.404 | -5.88€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 102 | +0.413 | -5.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 102 | +0.413 | -5.41€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 24 | +0.346 | +0.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 24 | +0.346 | +0.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 251 | +0.259 | -28.96€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 251 | +0.259 | -28.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 251 | +0.259 | -28.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 251 | +0.259 | -28.96€ | 0 | 4 |
| ✅ GBM_LATE_15M | 4576 | +0.086 | +1621.43€ | 0 | 14 |
| ✅ GBM_LATE_15M#15min | 4576 | +0.086 | +1621.43€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 798 | +0.174 | +495.07€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 798 | +0.174 | +495.07€ | 0 | 17 |
| ✅ GBM_LATE_15M#BTC | 451 | +0.180 | +230.21€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 451 | +0.180 | +230.21€ | 0 | 24 |
| ✅ GBM_LATE_15M#DOGE | 803 | +0.188 | +540.43€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 803 | +0.188 | +540.43€ | 0 | 17 |
| ✅ GBM_LATE_15M#ETH | 610 | -0.002 | +34.01€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 610 | -0.002 | +34.01€ | 0 | 3 |
| ✅ GBM_LATE_15M#SOL | 857 | +0.004 | +82.07€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 857 | +0.004 | +82.07€ | 3 | 3 |
| ✅ GBM_LATE_15M#XRP | 1057 | +0.019 | +239.65€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 1057 | +0.019 | +239.65€ | 0 | 4 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 5594 | +0.048 | +1649.15€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 5594 | +0.048 | +1649.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 1074 | -0.030 | +187.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 1074 | -0.030 | +187.80€ | 1 | 2 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 1060 | -0.010 | +99.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 1060 | -0.010 | +99.24€ | 0 | 3 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 679 | +0.237 | +612.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 679 | +0.237 | +612.34€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 979 | -0.020 | +8.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 979 | -0.020 | +8.77€ | 6 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 994 | +0.003 | +100.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 994 | +0.003 | +100.77€ | 3 | 2 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 808 | +0.209 | +640.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 808 | +0.209 | +640.23€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 3323 | +0.175 | +2239.30€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 3323 | +0.175 | +2239.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 592 | +0.189 | +420.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 592 | +0.189 | +420.96€ | 0 | 17 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 439 | +0.194 | +290.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 439 | +0.194 | +290.30€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 588 | +0.200 | +452.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 588 | +0.200 | +452.05€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 413 | +0.208 | +300.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 413 | +0.208 | +300.29€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 623 | +0.078 | +260.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 623 | +0.078 | +260.34€ | 1 | 11 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 668 | +0.196 | +515.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 668 | +0.196 | +515.35€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 547 | +0.045 | +42.77€ | 0 | 7 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 547 | +0.045 | +42.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 100 | +0.039 | -6.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 100 | +0.039 | -6.39€ | 2 | 10 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 115 | +0.167 | +45.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 115 | +0.167 | +45.11€ | 0 | 19 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 225 | -0.011 | +4.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 225 | -0.011 | +4.98€ | 4 | 3 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 107 | +0.032 | -0.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 107 | +0.032 | -0.93€ | 0 | 1 |
| ✅ GBM_LATE_15M_TARDIO | 3878 | +0.168 | +2489.91€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 3878 | +0.168 | +2489.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 768 | +0.184 | +530.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 768 | +0.184 | +530.68€ | 0 | 17 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 510 | +0.154 | +270.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 510 | +0.154 | +270.31€ | 1 | 23 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 757 | +0.218 | +626.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 757 | +0.218 | +626.91€ | 0 | 17 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 354 | +0.118 | +135.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 354 | +0.118 | +135.35€ | 1 | 22 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 626 | +0.080 | +272.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 626 | +0.080 | +272.43€ | 0 | 15 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 863 | +0.198 | +654.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 863 | +0.198 | +654.23€ | 0 | 23 |
| ✅ GBM_LATE_5M | 258 | +0.088 | +72.34€ | 3 | 11 |
| ✅ GBM_LATE_5M#5min | 258 | +0.088 | +72.34€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 134 | +0.073 | +27.78€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 134 | +0.073 | +27.78€ | 0 | 7 |
| ✅ GBM_LATE_5M#ETH | 70 | +0.194 | +39.22€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 70 | +0.194 | +39.22€ | 0 | 11 |
| ✅ GBM_LATE_5M#SOL | 44 | -0.065 | +3.71€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 44 | -0.065 | +3.71€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP | 10 | +0.083 | +1.62€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 10 | +0.083 | +1.62€ | 0 | 0 |
| ✅ GBM_LATE_60M | 493 | -0.048 | +72.52€ | 4 | 5 |
| ✅ GBM_LATE_60M#60min | 493 | -0.048 | +72.52€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 170 | -0.006 | +4.90€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 170 | -0.006 | +4.90€ | 3 | 2 |
| ✅ GBM_LATE_60M#ETH | 174 | -0.023 | +43.65€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 174 | -0.023 | +43.65€ | 1 | 8 |
| ✅ GBM_LATE_60M#SOL | 149 | -0.122 | +23.97€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 149 | -0.122 | +23.97€ | 2 | 1 |
| 🚫 GBM_LATE_60M_FADE | 190 | -0.302 | -32.95€ | 9 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 190 | -0.302 | -32.95€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 75 | -0.253 | -6.85€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 75 | -0.253 | -6.85€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 64 | -0.348 | -18.54€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 64 | -0.348 | -18.54€ | 2 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 51 | -0.292 | -7.56€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 51 | -0.292 | -7.56€ | 2 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 307 | +0.047 | +12.25€ | 0 | 2 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 307 | +0.047 | +12.25€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 120 | +0.016 | +5.07€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 120 | +0.016 | +5.07€ | 2 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 71 | +0.116 | +10.49€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 71 | +0.116 | +10.49€ | 0 | 3 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 116 | +0.034 | -3.31€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 116 | +0.034 | -3.31€ | 1 | 5 |
| ✅ LEADLAG_BTC_XRP_15M | 58 | +0.167 | +21.93€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 58 | +0.167 | +21.93€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 58 | +0.167 | +21.93€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 58 | +0.167 | +21.93€ | 0 | 2 |
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
| ✅ LIQUIDACIONES_5M | 87 | -0.118 | -11.54€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 87 | -0.118 | -11.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 28 | +0.000 | -0.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 28 | +0.000 | -0.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE | 8 | -0.040 | -1.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 8 | -0.040 | -1.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 20 | -0.136 | -3.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 20 | -0.136 | -3.33€ | 0 | 0 |
| 🚫 LIQUIDACIONES_5M#SOL | 16 | -0.178 | -4.14€ | 0 | 0 |
| 🚫 LIQUIDACIONES_5M#SOL#5min | 16 | -0.178 | -4.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 14 | -0.131 | -3.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 14 | -0.131 | -3.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M | 299 | +0.002 | -5.26€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 299 | +0.002 | -5.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 101 | -0.005 | -7.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 101 | -0.005 | -7.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 97 | -0.005 | -0.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 97 | -0.005 | -0.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 101 | +0.015 | +2.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 101 | +0.015 | +2.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M | 599 | +0.031 | +1.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 599 | +0.031 | +1.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 96 | +0.061 | +9.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 96 | +0.061 | +9.62€ | 0 | 4 |
| ✅ MOMENTUM_IBS_15M#BTC | 103 | +0.062 | +9.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 103 | +0.062 | +9.14€ | 0 | 4 |
| ✅ MOMENTUM_IBS_15M#DOGE | 96 | -0.010 | -13.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 96 | -0.010 | -13.02€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 105 | +0.070 | +18.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 105 | +0.070 | +18.25€ | 0 | 4 |
| ✅ MOMENTUM_IBS_15M#SOL | 98 | -0.030 | -18.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 98 | -0.030 | -18.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 101 | +0.024 | -4.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 101 | +0.024 | -4.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 845 | -0.042 | -11.47€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 845 | -0.042 | -11.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 135 | -0.047 | +18.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 135 | -0.047 | +18.05€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 147 | -0.077 | -19.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 147 | -0.077 | -19.49€ | 6 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 136 | -0.022 | +8.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 136 | -0.022 | +8.52€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 148 | -0.007 | -4.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 148 | -0.007 | -4.76€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 136 | -0.065 | -8.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 136 | -0.065 | -8.94€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 143 | -0.031 | -4.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 143 | -0.031 | -4.84€ | 5 | 2 |
| ✅ MOMENTUM_IBS_15M_FADE | 307 | -0.073 | -24.83€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 307 | -0.073 | -24.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 47 | -0.031 | -2.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 47 | -0.031 | -2.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 49 | -0.147 | -8.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 49 | -0.147 | -8.02€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 28 | -0.133 | -4.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 28 | -0.133 | -4.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 55 | -0.114 | -7.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 55 | -0.114 | -7.20€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 70 | -0.028 | -1.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 70 | -0.028 | -1.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 58 | -0.017 | -1.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 58 | -0.017 | -1.35€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 2276 | -0.069 | +48.90€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 2276 | -0.069 | +48.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 339 | -0.095 | +9.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 339 | -0.095 | +9.16€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 434 | -0.057 | +81.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 434 | -0.057 | +81.07€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 352 | -0.076 | -18.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 352 | -0.076 | -18.19€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 377 | -0.088 | -31.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 377 | -0.088 | -31.49€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 416 | -0.034 | +10.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 416 | -0.034 | +10.83€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 358 | -0.067 | -2.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 358 | -0.067 | -2.47€ | 5 | 1 |
| ✅ MOMENTUM_IBS_5M_FADE | 2081 | +0.022 | +29.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 2081 | +0.022 | +29.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 354 | +0.014 | +6.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 354 | +0.014 | +6.54€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 297 | +0.038 | +7.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 297 | +0.038 | +7.60€ | 1 | 2 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 360 | +0.028 | +6.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 360 | +0.028 | +6.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 359 | +0.013 | +3.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 359 | +0.013 | +3.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 364 | +0.022 | +4.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 364 | +0.022 | +4.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 347 | +0.019 | +0.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 347 | +0.019 | +0.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 225 | +0.082 | +41.12€ | 1 | 4 |
| ✅ ORDER_FLOW_5M#5min | 89 | +0.115 | +28.52€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 25 | +0.241 | +22.36€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 25 | +0.241 | +22.36€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE | 16 | +0.000 | -0.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 16 | +0.000 | -0.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL | 24 | +0.077 | +2.85€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 24 | +0.077 | +2.85€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP | 20 | +0.045 | +0.50€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 20 | +0.045 | +0.50€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 218 | -0.136 | -7.98€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 89 | -0.181 | -19.76€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 76 | -0.192 | -16.80€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 13 | -0.065 | -2.96€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 87 | -0.140 | -2.43€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 72 | -0.149 | -3.66€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 15 | -0.066 | +1.23€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 42 | -0.023 | +14.21€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 37 | +0.013 | +15.46€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 5 | -0.054 | -1.25€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 185 | -0.136 | -5.00€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 33 | -0.129 | -2.99€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 114 | -0.267 | -24.37€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 47 | -0.194 | -5.25€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 45 | -0.181 | -4.23€ | 1 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 51 | -0.255 | -10.96€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 49 | -0.245 | -9.94€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 16 | -0.356 | -8.16€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#atexpiry | 15 | -0.331 | -7.65€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 109 | -0.257 | -21.82€ | 0 | 0 |
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
| ✅ STREAK_FADE_15M | 48 | -0.140 | -13.74€ | 3 | 0 |
| ✅ STREAK_FADE_15M#15min | 48 | -0.140 | -13.74€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 19 | -0.068 | -4.71€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 19 | -0.068 | -4.71€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 24 | -0.154 | -6.82€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 24 | -0.154 | -6.82€ | 0 | 0 |
| ✅ STREAK_FADE_5M | 360 | -0.025 | -20.72€ | 2 | 1 |
| ✅ STREAK_FADE_5M#5min | 360 | -0.025 | -20.72€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 93 | +0.026 | +2.11€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 93 | +0.026 | +2.11€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 126 | -0.016 | -7.65€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 126 | -0.016 | -7.65€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 64 | -0.076 | -8.25€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 64 | -0.076 | -8.25€ | 2 | 1 |
| ✅ STREAK_FADE_5M#XRP | 77 | -0.057 | -6.93€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 77 | -0.057 | -6.93€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 15 | -0.066 | -1.71€ | 0 | 0 |
| ✅ STREAK_FADE_60M#60min | 15 | -0.066 | -1.71€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 9 | -0.061 | -1.63€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 9 | -0.061 | -1.63€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 602 | +0.021 | +2.69€ | 1 | 0 |
| ✅ STREAK_MOM_5M#5min | 602 | +0.021 | +2.69€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 190 | +0.010 | -2.35€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 190 | +0.010 | -2.35€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 115 | -0.004 | -1.76€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 115 | -0.004 | -1.76€ | 2 | 2 |
| ✅ STREAK_MOM_5M#SOL | 156 | +0.032 | +2.41€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 156 | +0.032 | +2.41€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP | 141 | +0.045 | +4.40€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 141 | +0.045 | +4.40€ | 2 | 3 |
| ✅ STRUCT_NO_15M | 1877 | +0.017 | -0.96€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 1877 | +0.017 | -0.96€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 715 | +0.009 | -6.80€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 715 | +0.009 | -6.80€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 737 | +0.021 | +2.21€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 737 | +0.021 | +2.21€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 425 | +0.025 | +3.62€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 425 | +0.025 | +3.62€ | 2 | 0 |
| ✅ UPDOWN_GBM | 2255 | +0.025 | +150.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 979 | +0.088 | +177.96€ | 1 | 6 |
| ✅ UPDOWN_GBM#240min | 121 | +0.012 | -0.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 856 | -0.019 | -15.14€ | 4 | 0 |
| ✅ UPDOWN_GBM#60min | 252 | -0.024 | -10.98€ | 3 | 1 |
| ✅ UPDOWN_GBM#BNB | 99 | +0.104 | +21.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 92 | +0.128 | +22.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 6 | -0.075 | -2.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 420 | +0.014 | +11.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 124 | +0.040 | -6.62€ | 2 | 6 |
| ✅ UPDOWN_GBM#BTC#240min | 37 | +0.064 | +2.33€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 156 | +0.044 | +24.11€ | 2 | 5 |
| ✅ UPDOWN_GBM#BTC#60min | 85 | -0.063 | -9.73€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 303 | +0.002 | -0.50€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 61 | +0.119 | +15.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 242 | -0.029 | -15.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 522 | +0.053 | +49.78€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 226 | +0.123 | +51.21€ | 1 | 14 |
| ✅ UPDOWN_GBM#ETH#240min | 37 | +0.038 | +0.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 142 | +0.007 | -0.25€ | 4 | 3 |
| ✅ UPDOWN_GBM#ETH#60min | 102 | +0.010 | -0.89€ | 0 | 2 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 409 | -0.004 | +5.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 175 | +0.025 | +7.06€ | 1 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 29 | -0.016 | -0.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 128 | -0.008 | -0.54€ | 2 | 2 |
| ✅ UPDOWN_GBM#SOL#60min | 65 | -0.022 | -0.36€ | 1 | 0 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 500 | +0.026 | +64.93€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 301 | +0.097 | +88.45€ | 0 | 14 |
| ✅ UPDOWN_GBM#XRP#240min | 17 | -0.112 | -2.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 182 | -0.076 | -20.62€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 109 | +0.248 | -1.72€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 109 | +0.248 | -1.72€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 70 | +0.208 | -9.20€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 70 | +0.208 | -9.20€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 39 | +0.305 | +7.48€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 39 | +0.305 | +7.48€ | 0 | 2 |
| ✅ UPDOWN_GBM_15M_TARDIO | 1684 | -0.047 | +193.18€ | 2 | 3 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 1684 | -0.047 | +193.18€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 116 | -0.085 | -7.02€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 116 | -0.085 | -7.02€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 328 | -0.142 | -18.17€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 328 | -0.142 | -18.17€ | 3 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 42 | +0.000 | +2.20€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 42 | +0.000 | +2.20€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 132 | -0.007 | +17.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 132 | -0.007 | +17.56€ | 2 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 543 | -0.008 | +116.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 543 | -0.008 | +116.65€ | 1 | 1 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 523 | -0.031 | +81.96€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 523 | -0.031 | +81.96€ | 3 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 8 | -0.040 | -1.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 8 | -0.040 | -1.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 8 | -0.040 | -1.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 8 | -0.040 | -1.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 143 | +0.252 | +68.80€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 143 | +0.252 | +68.80€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 88 | +0.233 | +32.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 88 | +0.233 | +32.53€ | 0 | 14 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 55 | +0.272 | +36.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 55 | +0.272 | +36.27€ | 0 | 8 |
| ✅ UPDOWN_OU_5M | 355 | -0.055 | -24.93€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#5min | 355 | -0.055 | -24.93€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 228 | +0.000 | -9.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 228 | +0.000 | -9.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 18 | +0.090 | +4.73€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 18 | +0.090 | +4.73€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#DOGE | 25 | -0.204 | -5.66€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#DOGE#5min | 25 | -0.204 | -5.66€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 29 | -0.177 | -4.93€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 29 | -0.177 | -4.93€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 28 | -0.200 | -4.70€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 28 | -0.200 | -4.70€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 27 | -0.155 | -4.76€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 27 | -0.155 | -4.76€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 933 | +0.285 | +382.06€ | 0 | 2 |
| ✅ WEEKLY_PRICE#BTC | 277 | +0.199 | +5.61€ | 0 | 2 |
| ✅ WEEKLY_PRICE#ETH | 296 | +0.255 | +66.82€ | 0 | 1 |
| ✅ WEEKLY_PRICE#SOL | 360 | +0.373 | +309.64€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.135) — sin ventaja clara. oversold(IBS<0.3): IC=-0.016 n=792 | neutral: IC=+0.009 n=759 | overbought(IBS>0.7): IC=+0.119 n=1006
  - _Datos_: n=2742 IC=+0.044 PNL=+235.98€

**🟡 H-HORA-GBM** — hora_utc causal automático en GBM (forward)
  - _Umbral_: n≥20 forward con hora_utc + alguna hora con n≥15 IC<-0.10 o >+0.10
  - _Acción_: El sistema lo aplica automáticamente vía FEATURE_RULES. Verificar en strategy_params.json.
  - _Estado_: H=19h: IC=+0.110 n=121 PNL=+34.16€ → BOOST | H=23h: IC=-0.149 n=112 PNL=-29.64€ → FILTRAR

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 1 celda(s) pasan gate riguroso completo de 54 evaluadas (n>=40) y 290 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.025 < 0.08 — monitorear
  - _Datos_: n=175 IC=+0.025 PNL=+7.06€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=296/15 IC=+0.255 PNL=+66.82€ | BTC: n=277/15 IC=+0.199 PNL=+5.61€ | SOL: n=360/15 IC=+0.373 PNL=+309.64€

**🟡 H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.103 n=39463 | tras_1loss IC=+0.060 n=27951 | tras_2loss IC=+0.020 n=12237/40 | gap=+0.084 (umbral 0.05)

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
  - _Estado_: alineada_con_outcome_prev IC=+0.152 n=13/60 | contraria IC=-0.043 n=12 | gap=+0.195 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=15, boost estimado=+0.027. Necesita 5 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 24/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=102/40 IC=+0.010 PNL=-0.89€ | BTC#60min: n=85/40 IC=-0.063 PNL=-9.73€ | SOL#60min: n=65/40 IC=-0.022 PNL=-0.36€

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.077 n=173 | contrario_BTC IC=-0.020 n=100/40 | gap=-0.097 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.120 > 0.08 con n=77 PNL=+18.48€
  - _Datos_: n=77 IC=+0.120 PNL=+18.48€

**⏳ H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: 25
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: 4/25 ops en el filtro definido (IC actual=+0.067 PNL=+4.17€)
  - _Datos_: n=4 IC=+0.067 PNL=+4.17€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.341 > 0.1 con n=794 PNL=+391.67€
  - _Datos_: n=794 IC=+0.341 PNL=+391.67€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=17 IC=+0.022 PNL=+4.57€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=17 IC=+0.022 PNL=+4.57€

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
  - _Estado_: n=2063 IC=+0.018 PNL=+108.60€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=2063 IC=+0.018 PNL=+108.60€

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
  - _Estado_: n=194 IC=+0.000 PNL=-4.02€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=194 IC=+0.000 PNL=-4.02€

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
  - _Estado_: n=40 IC=+0.024 PNL=+3.19€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=40 IC=+0.024 PNL=+3.19€

**〰️ H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: n=418 IC=+0.098 PNL=+56.72€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=418 IC=+0.098 PNL=+56.72€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=131 IC=+0.079 PNL=+29.21€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=131 IC=+0.079 PNL=+29.21€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=124 IC=+0.040 PNL=-6.62€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=124 IC=+0.040 PNL=-6.62€

**⏳ H-CUSTOM-DRIFT15-ZONA-MUERTA** — GBM#15min drift_15min ∈ [-0.3,+0.3] — zona muerta de señal
  - _Hipótesis_: Análisis n=127 GBM#15min: cuando drift_15min está entre -0.3 y +0.3 (mercado sin dirección clara) el IC es negativo (-0.043). Cuando drift>0.3 IC=+0.100 (n=28). Cuando drift<-1 IC=+0.048 (reversión). La señal requiere mercado con dirección clara.
  - _Umbral_: 50
  - _Acción_: Filtrar señales GBM#15min cuando drift_15min ∈ [-0.3, +0.3] — validar con n≥50 antes de implementar
  - _Estado_: 0/50 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🟡 H-CUSTOM-DRIFT15-MOMENTUM** — GBM#15min drift_15min > 0.3 — zona de momentum (señal fuerte)
  - _Hipótesis_: Cuando drift_15min > 0.3%/h el GBM captura bien la dirección: IC=+0.100 n=28 en todos GBM#15min; IC=+0.152 n=13 solo BTC. El mercado tiene dirección clara y el GBM la sigue. Hipótesis: este rango es donde la señal es real.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma IC>0.10 con n≥40 → boost ×1.2 en GBM#15min cuando drift_15min>0.3
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.082 > 0.08 con n=611 PNL=+84.83€
  - _Datos_: n=611 IC=+0.082 PNL=+84.83€

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
  - _Estado_: n=100 IC=+0.039 PNL=+14.19€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=100 IC=+0.039 PNL=+14.19€

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
  - _Estado_: n=474 IC=+0.097 PNL=+121.19€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=474 IC=+0.097 PNL=+121.19€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=298 IC=+0.033 PNL=-6.06€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=298 IC=+0.033 PNL=-6.06€

**⏳ H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: 40
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: 24/40 ops en el filtro definido (IC actual=+0.077 PNL=+3.10€)
  - _Datos_: n=24 IC=+0.077 PNL=+3.10€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.137 > 0.08 con n=89 PNL=-5.02€
  - _Datos_: n=89 IC=+0.137 PNL=-5.02€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.098 > 0.08 con n=80 PNL=+16.80€
  - _Datos_: n=80 IC=+0.098 PNL=+16.80€

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
  - _Estado_: n=330 IC=+0.021 PNL=+2.32€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=330 IC=+0.021 PNL=+2.32€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.167 > 0.02 con n=112 PNL=+43.76€
  - _Datos_: n=112 IC=+0.167 PNL=+43.76€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.445 > 0.1 con n=523 PNL=+435.60€
  - _Datos_: n=523 IC=+0.445 PNL=+435.60€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=972 IC=+0.019 PNL=+21.70€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=972 IC=+0.019 PNL=+21.70€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.150 > 0.1 con n=563 PNL=+168.75€
  - _Datos_: n=563 IC=+0.150 PNL=+168.75€

**⏳ H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: 40
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: 12/40 ops en el filtro definido (IC actual=-0.214 PNL=-6.49€)
  - _Datos_: n=12 IC=-0.214 PNL=-6.49€

**🟡 H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.106 > 0.1 con n=173 PNL=+54.43€
  - _Datos_: n=173 IC=+0.106 PNL=+54.43€

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
  - _Estado_: 28/50 ops en el filtro definido (IC actual=+0.100 PNL=+1.12€)
  - _Datos_: n=28 IC=+0.100 PNL=+1.12€

**⏳ H-CUSTOM-ETH15-BUYNO-PRECIO-ALTO** — ETH#15min BUY_NO con precio_yes>0.55 pierde (NO longshot contra favorito)
  - _Hipótesis_: Detectado 2026-07-02: ult.60 shadow ETH15 BUY_NO — py_mkt~0.5 wr=0.67 PNL=+29.3 (n=49); py_mkt 0.6-0.8 wr 0.33-0 PNL=-5.75 (n=9). Filtro RETURN NONE (no SKIP) aplicado en shadow_predict.py (PY_MKT_MAX_BUY_NO_ETH15=0.55) el mismo dia -- bloquea la GENERACIÓN de la fila, no solo la decisión. Esta hipotesis trackea la zona filtrada: si las ops que HABRIAN caido aqui siguen apareciendo en otras estrategias o el IC forward de la zona se vuelve positivo, revisar el filtro. CAVEAT: n=9, muestra chica — el filtro se aplico por asimetria de riesgo (afecta a dinero live), no por significancia. ⚠️ 05-Ago (fix): la clave del filtro decía 'py_mkt', que NUNCA existió ni en features de UPDOWN_GBM (T_h/delta_ratio_macro/drift_15min/drift_60min/pct_spot_vs_ref/sigma_h) ni como columna top-level de results.csv -- corregida a 'precio_yes_mercado' (columna real). Aun así, con la clave correcta esta hipótesis NUNCA podrá acumular n mientras el filtro RETURN NONE siga activo -- es el mismo patrón 'frozen by design' que H-CUSTOM-LATE15-PHOTO-FINISH (más abajo): la propia protección impide generar los datos necesarios para volver a evaluarla. Para monitorearla de verdad haría falta un logger separado que capture la señal SIN aplicar el filtro (mismo patrón que gate_bucket_propio con data/markets histórico) -- no construido, pendiente decisión.
  - _Umbral_: 20
  - _Acción_: Si IC forward de la zona >0 con n>=20 → retirar filtro; si confirma negativo → considerar extender a BTC/SOL 15min
  - _Estado_: 0/20 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-PRECIO-YES-BARATO** — BUY_YES con precio de mercado 0.30-0.40 — mercado infravalora YES
  - _Hipótesis_: Detectado 2026-07-03 en benchmark de calibración del mercado (7d, estrategias GBM): en el bucket precio_yes_mercado [0.3-0.4) la frecuencia real de YES fue 0.45 vs 0.35 implícito (+0.10, n=38). Posible sesgo favorito-longshot suave en binarios de 15min (complemento del LONGSHOT ya activo para BUY_NO con py<0.20). Si se confirma, BUY_YES comprado en esa banda lleva viento de cola estructural del propio mercado, independiente del modelo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → kelly_boost ×1.1 para BUY_YES con precio_yes_mercado en [0.30,0.40), simétrico al longshot BUY_NO existente
  - _Estado_: n=1379 IC=-0.147 PNL=+60.67€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1379 IC=-0.147 PNL=+60.67€

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
  - _Estado_: n=318 IC=+0.144 PNL=+107.61€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=318 IC=+0.144 PNL=+107.61€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.098 > 0.08 con n=418 PNL=+56.72€
  - _Datos_: n=418 IC=+0.098 PNL=+56.72€

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
  - _Estado_: 55/289 ops en el filtro definido (IC actual=-0.325 PNL=-21.39€)
  - _Datos_: n=55 IC=-0.325 PNL=-21.39€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=810 IC=+0.156 PNL=+431.22€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=810 IC=+0.156 PNL=+431.22€

**⏳ H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: 40
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: 14/40 ops en el filtro definido (IC actual=+0.044 PNL=+0.04€)
  - _Datos_: n=14 IC=+0.044 PNL=+0.04€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=339 IC=-0.002 PNL=+23.38€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=339 IC=-0.002 PNL=+23.38€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.203 > 0.08 con n=281 PNL=+158.61€
  - _Datos_: n=281 IC=+0.203 PNL=+158.61€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=559 IC=+0.028 PNL=+149.95€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=559 IC=+0.028 PNL=+149.95€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.131 > 0.08 con n=158 PNL=-10.82€
  - _Datos_: n=158 IC=+0.131 PNL=-10.82€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.245 > 0.08 con n=657 PNL=-71.16€
  - _Datos_: n=657 IC=+0.245 PNL=-71.16€

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 4/40 ops en el filtro definido (IC actual=+0.000 PNL=+1.83€)
  - _Datos_: n=4 IC=+0.000 PNL=+1.83€

**⏳ H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: 40
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: 36/40 ops en el filtro definido (IC actual=+0.210 PNL=+20.58€)
  - _Datos_: n=36 IC=+0.210 PNL=+20.58€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.354 > 0.08 con n=46 PNL=+36.65€
  - _Datos_: n=46 IC=+0.354 PNL=+36.65€

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
  - _Estado_: n=1138 IC=+0.097 PNL=-258.21€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=1138 IC=+0.097 PNL=-258.21€

**⏳ H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: 40
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: 17/40 ops en el filtro definido (IC actual=+0.157 PNL=+5.75€)
  - _Datos_: n=17 IC=+0.157 PNL=+5.75€
