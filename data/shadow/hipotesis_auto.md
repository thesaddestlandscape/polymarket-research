# Hipótesis automáticas — 2026-08-18 06:41 UTC
_Generado por shadow_postmortem.py sobre 59837 resoluciones (PNL=+6281.26€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.355` → IC=-0.143 (n=68)

  - _Acción_: SKIP cuando `py_entrada` < 0.355
  - _Potencial_: sin este filtro IC_bueno=+0.178 (n=147)

- **FILTRO** `banda_hit_calibrado` < `0.6142` → IC=-0.227 (n=53)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6142
  - _Potencial_: sin este filtro IC_bueno=+0.177 (n=162)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.377 (n=63)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.142 (n=205)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.234 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.076)

- **PATRÓN** `n_total_lado` > `74.0` → IC=+0.196 (n=54)

  - _Acción_: Kelly boost +0.98€ cuando `n_total_lado` > 74.0 (IC base=+0.076)

- **PATRÓN** `banda_hit_calibrado` > `0.6142` → IC=+0.177 (n=162)

  - _Acción_: Kelly boost +0.88€ cuando `banda_hit_calibrado` > 0.6142 (IC base=+0.076)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.142 (n=205)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.5 (IC base=+0.018)

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
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=82)

- **FILTRO** `banda_hit_calibrado` < `0.6267` → IC=-0.203 (n=35)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6267
  - _Potencial_: sin este filtro IC_bueno=+0.189 (n=72)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.123 (n=83)

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

- **PATRÓN** `py_entrada` > `0.33` → IC=+0.167 (n=82)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.33 (IC base=+0.060)

- **PATRÓN** `banda_hit_calibrado` > `0.6267` → IC=+0.189 (n=72)

  - _Acción_: Kelly boost +0.95€ cuando `banda_hit_calibrado` > 0.6267 (IC base=+0.060)

- **PATRÓN** `banda_z` > `8.876` → IC=+0.224 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.876 (IC base=+0.060)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.123 (n=83)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.060)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.143 (n=68)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.495 (IC base=-0.020)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `143.43` → IC=-0.267 (n=783)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 143.43
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=2352)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `112.74` → IC=-0.399 (n=87)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 112.74
  - _Potencial_: sin este filtro IC_bueno=-0.126 (n=263)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` > `638.33` → IC=-0.266 (n=109)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` > 638.33
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=328)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `113.85` → IC=-0.446 (n=147)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 113.85
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=147)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `243.2` → IC=-0.164 (n=530)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 243.2
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=177)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `140.27` → IC=-0.217 (n=185)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 140.27
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=558)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `156.96` → IC=-0.258 (n=151)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 156.96
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=453)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.7` → IC=+0.205 (n=2086)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.7 (IC base=+0.096)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.162 (n=1134)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `2373.5135` → IC=+0.165 (n=1098)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2373.5135 (IC base=+0.096)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.150 (n=3521)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.149 (n=2698)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 11.0 (IC base=+0.146)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.282 (n=1318)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.184 (n=1960)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.02 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `4023.461` → IC=+0.172 (n=792)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 4023.461 (IC base=+0.146)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.227 (n=119)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.775` → IC=+0.350 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.775 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.197 (n=433)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.01 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.227 (n=306)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.329 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.191 (n=416)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.01 (IC base=+0.190)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.142 (n=383)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.160 (n=333)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 15.0 (IC base=+0.132)

- **PATRÓN** `py_entrada` > `0.6` → IC=+0.167 (n=178)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.6 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `5033.4098` → IC=+0.165 (n=195)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 5033.4098 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.204 (n=160)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.141)

- **PATRÓN** `py_entrada` < `0.395` → IC=+0.220 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.395 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `4703.1735` → IC=+0.168 (n=227)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4703.1735 (IC base=+0.141)

### FAVORITO_CONFIRMADO#ETH#15min
- **PATRÓN** `hora_utc` < `11.0` → IC=+0.141 (n=444)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 11.0 (IC base=+0.109)

- **PATRÓN** `py_entrada` > `0.7` → IC=+0.298 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.7 (IC base=+0.109)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.304 (n=253)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.286)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.290 (n=255)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.286)

- **PATRÓN** `py_entrada` < `0.195` → IC=+0.405 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.195 (IC base=+0.286)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.289 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `3321.5477` → IC=+0.345 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3321.5477 (IC base=+0.286)

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

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 5697.4897 (IC base=+0.098)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.179 (n=544)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.188 (n=466)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 15.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.407 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.270 (n=111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.228)

- **PATRÓN** `py_entrada` < `0.31` → IC=+0.344 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.31 (IC base=+0.228)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.251 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.228)

- **PATRÓN** `libro_liquidez` > `909.0749` → IC=+0.235 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 909.0749 (IC base=+0.228)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `19.0` → IC=+0.253 (n=75)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 19.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.195 (n=149)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 13.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.340 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.195 (n=198)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.03 (IC base=+0.189)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.224 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.106)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.159 (n=256)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.02 (IC base=+0.106)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `12.0` → IC=-0.306 (n=60)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=62)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.198 (n=1153)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 7.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.185 (n=938)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` < 0.7 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.204 (n=882)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `3268.7028` → IC=+0.348 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3268.7028 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.170 (n=573)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 15.0 (IC base=+0.159)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.180 (n=579)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.73 (IC base=+0.159)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `13.0` → IC=-0.364 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=24)

- **FILTRO** `py_entrada` > `0.815` → IC=-0.409 (n=20)

  - _Acción_: SKIP cuando `py_entrada` > 0.815
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=24)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.417 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.326)

- **PATRÓN** `py_entrada` > `0.835` → IC=+0.370 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.835 (IC base=+0.326)

- **PATRÓN** `libro_liquidez` > `2916.5858` → IC=+0.343 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2916.5858 (IC base=+0.326)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=644)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.188 (n=286)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 7.0 (IC base=+0.161)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.196 (n=218)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.7 (IC base=+0.161)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.161 (n=358)

  - _Acción_: Kelly boost +0.81€ cuando `py_entrada` > 0.73 (IC base=+0.161)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.218 (n=565)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.230 (n=498)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.309 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.218)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min
- **FILTRO** `py_entrada` > `0.755` → IC=-0.267 (n=58)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=20)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.202 (n=213)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.201 (n=272)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.209 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.7 (IC base=+0.179)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.431 (n=114)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.413)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.417 (n=106)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.413)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.418 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.413)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.454 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.413)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.410 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.413)

- **PATRÓN** `libro_liquidez` > `3351.8902` → IC=+0.430 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3351.8902 (IC base=+0.413)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `12.0` → IC=+0.412 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.415)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.425 (n=38)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.415)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.429 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.415)

- **PATRÓN** `libro_liquidez` > `3461.8377` → IC=+0.427 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3461.8377 (IC base=+0.415)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.394 (n=45)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.375)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.380 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.375)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.389 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.375)

- **PATRÓN** `libro_liquidez` > `2004.8341` → IC=+0.386 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2004.8341 (IC base=+0.375)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `py_entrada` < `0.925` → IC=+0.409 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.925 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.413 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.425)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.204 (n=1422)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.206 (n=1786)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.232 (n=2832)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.194)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` < `11.0` → IC=+0.132 (n=536)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 11.0 (IC base=+0.102)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.141 (n=368)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` > 0.73 (IC base=+0.102)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.300 (n=213)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.254)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.265 (n=236)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.254)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.334 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.254)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` < `6.0` → IC=+0.179 (n=316)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 6.0 (IC base=+0.150)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.220 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.150)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.241 (n=311)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.299 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.261 (n=220)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.253)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.265 (n=228)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.253)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.289 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.253)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.255 (n=231)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.208 (n=258)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.263 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.202)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.226 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.149)

- **PATRÓN** `restante_min` < `3.78` → IC=+0.164 (n=474)

  - _Acción_: Kelly boost +0.82€ cuando `restante_min` < 3.78 (IC base=+0.149)

- **PATRÓN** `restante_min` > `4.91` → IC=+0.202 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `restante_min` > 4.91 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.154 (n=1436)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.157 (n=1449)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 17.0 (IC base=+0.149)

- **PATRÓN** `lag_apertura_s` < `5.42` → IC=+0.210 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `lag_apertura_s` < 5.42 (IC base=+0.149)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.239 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.154)

- **PATRÓN** `restante_min` < `3.72` → IC=+0.172 (n=236)

  - _Acción_: Kelly boost +0.86€ cuando `restante_min` < 3.72 (IC base=+0.154)

- **PATRÓN** `restante_min` > `4.88` → IC=+0.192 (n=251)

  - _Acción_: Kelly boost +0.96€ cuando `restante_min` > 4.88 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=717)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.165 (n=637)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 15.0 (IC base=+0.154)

- **PATRÓN** `lag_apertura_s` < `7.36` → IC=+0.193 (n=236)

  - _Acción_: Kelly boost +0.97€ cuando `lag_apertura_s` < 7.36 (IC base=+0.154)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.43` → IC=+0.175 (n=636)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.43 (IC base=+0.145)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.217 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `restante_min` > 4.95 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.151 (n=672)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 6.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.156 (n=730)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 17.0 (IC base=+0.145)

- **PATRÓN** `lag_apertura_s` < `3.15` → IC=+0.226 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `lag_apertura_s` < 3.15 (IC base=+0.145)

- **PATRÓN** `profundidad_ratio_no` > `14.5` → IC=+0.180 (n=239)

  - _Acción_: Kelly boost +0.90€ cuando `profundidad_ratio_no` > 14.5 (IC base=+0.145)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.305 (n=413)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.295)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.306 (n=394)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.295)

- **PATRÓN** `py_entrada` > `0.825` → IC=+0.380 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.825 (IC base=+0.295)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.277 (n=173)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.266)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.273 (n=170)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.266)

- **PATRÓN** `py_entrada` < `0.725` → IC=+0.280 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.725 (IC base=+0.266)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.344 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.266)

- **PATRÓN** `libro_liquidez` > `3909.8054` → IC=+0.273 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3909.8054 (IC base=+0.266)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.307 (n=190)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.297)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.311 (n=189)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.297)

- **PATRÓN** `py_entrada` > `0.81` → IC=+0.392 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.81 (IC base=+0.297)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.304 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.297)

- **PATRÓN** `libro_liquidez` > `1882.9092` → IC=+0.316 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1882.9092 (IC base=+0.297)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` < `13.0` → IC=+0.444 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.371)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.409 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.371)

- **PATRÓN** `libro_liquidez` > `943.1727` → IC=+0.372 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 943.1727 (IC base=+0.371)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.410 (n=176)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.405)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.429 (n=167)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.405)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.408 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.405)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.427 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.405)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.403 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.405)

- **PATRÓN** `libro_liquidez` > `2161.2964` → IC=+0.413 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2161.2964 (IC base=+0.405)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.396 (n=75)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.400)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.437 (n=77)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.400)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.411 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.400)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.417 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.400)

- **PATRÓN** `libro_liquidez` > `5722.415` → IC=+0.426 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5722.415 (IC base=+0.400)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.407 (n=73)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.409)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.412 (n=66)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.409)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.410 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.409)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.424 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.409)

- **PATRÓN** `libro_liquidez` > `1842.491` → IC=+0.433 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1842.491 (IC base=+0.409)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.285 (n=128)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.259)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.419 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.278 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1406.0028` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1406.0028 (IC base=+0.259)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.285 (n=128)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.259)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.419 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.278 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1406.0028` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1406.0028 (IC base=+0.259)

### GBM_LATE_15M
- **PATRÓN** `hora_utc` < `6.0` → IC=+0.148 (n=436)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 6.0 (IC base=+0.109)

- **PATRÓN** `ibs_20min` > `0.9955` → IC=+0.275 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9955 (IC base=+0.109)

- **PATRÓN** `dist_vwap_pct` > `0.5823` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5823 (IC base=+0.109)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.838` → IC=+0.240 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.838 (IC base=+0.109)

- **PATRÓN** `volumen_regimen` < `1.3288` → IC=+0.222 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.3288 (IC base=+0.109)

- **PATRÓN** `volumen_regimen` > `0.7541` → IC=+0.229 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7541 (IC base=+0.109)

- **PATRÓN** `volumen_pendiente_norm` > `0.3253` → IC=+0.174 (n=90)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.3253 (IC base=+0.109)

- **PATRÓN** `volumen_spike_ratio` > `1.6853` → IC=+0.129 (n=577)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.6853 (IC base=+0.109)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.122 (n=1237)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.06 (IC base=+0.109)

- **PATRÓN** `ibs_20min` < `0.6585` → IC=+0.123 (n=2062)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.6585 (IC base=+0.079)

- **PATRÓN** `volumen_regimen` < `0.6331` → IC=+0.147 (n=154)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.6331 (IC base=+0.079)

- **PATRÓN** `volumen_regimen` > `0.6973` → IC=+0.136 (n=413)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.6973 (IC base=+0.079)

- **PATRÓN** `volumen_pendiente_norm` > `0.0856` → IC=+0.267 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0856 (IC base=+0.079)

- **PATRÓN** `volumen_spike_ratio` < `1.7094` → IC=+0.229 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7094 (IC base=+0.079)

- **PATRÓN** `volumen_spike_ratio` > `2.9485` → IC=+0.223 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9485 (IC base=+0.079)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.254 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 166.0 (IC base=+0.079)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.172 (n=172)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.007 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.189 (n=146)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 6.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.577` → IC=+0.345 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.577 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.1384` → IC=+0.144 (n=88)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.1384 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.174 (n=271)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.06 (IC base=+0.125)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.325 (n=61)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.278)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.325 (n=61)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.278)

- **PATRÓN** `drift_60min` |x|≤ `0.1349` → IC=+0.337 (n=121)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1349 (IC base=+0.278)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.280 (n=189)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.278)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.298 (n=122)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.278)

- **PATRÓN** `ibs_20min` < `0.5765` → IC=+0.325 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5765 (IC base=+0.278)

- **PATRÓN** `volumen_pendiente_norm` < `0.0707` → IC=+0.309 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0707 (IC base=+0.278)

- **PATRÓN** `volumen_pendiente_norm` > `0.1782` → IC=+0.318 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1782 (IC base=+0.278)

- **PATRÓN** `volumen_spike_ratio` < `1.8119` → IC=+0.336 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8119 (IC base=+0.278)

- **PATRÓN** `volumen_spike_ratio` > `1.5873` → IC=+0.292 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5873 (IC base=+0.278)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.318 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `1904.7343` → IC=+0.298 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1904.7343 (IC base=+0.278)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0017` → IC=+0.281 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0017 (IC base=+0.244)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.281 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.288 (n=83)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` < `0.699` → IC=+0.250 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.699 (IC base=+0.244)

- **PATRÓN** `ibs_20min` > `0.917` → IC=+0.274 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.917 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` > `0.6292` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6292 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.549` → IC=+0.330 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.549 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` < `0.6834` → IC=+0.312 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6834 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` < `0.1225` → IC=+0.303 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1225 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` < `2.7168` → IC=+0.294 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.7168 (IC base=+0.244)

- **PATRÓN** `libro_liquidez` > `13050.4574` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13050.4574 (IC base=+0.244)

- **PATRÓN** `sigma_h` < `0.0018` → IC=+0.153 (n=73)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0018 (IC base=+0.139)

- **PATRÓN** `sigma_h` > `0.0024` → IC=+0.160 (n=145)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0024 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.1869` → IC=+0.158 (n=191)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1869 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.190 (n=156)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 12.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.4564` → IC=+0.208 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4564 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.586` → IC=+0.257 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.586 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `1.3019` → IC=+0.153 (n=217)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.3019 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `0.6862` → IC=+0.163 (n=194)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.6862 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.13` → IC=+0.268 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.13 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.6765` → IC=+0.250 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6765 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `11192.8304` → IC=+0.140 (n=73)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 11192.8304 (IC base=+0.139)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.175 (n=115)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0074 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.190 (n=114)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 5.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.284 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.123` → IC=+0.292 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.123 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.4225` → IC=+0.175 (n=38)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.4225 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.8278` → IC=+0.124 (n=259)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 1.8278 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.156 (n=370)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.06 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `1914.6584` → IC=+0.150 (n=155)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1914.6584 (IC base=+0.133)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.342 (n=74)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.289 (n=74)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0075 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.0858` → IC=+0.316 (n=74)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0858 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.283 (n=233)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.284)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.294 (n=226)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.284)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.308 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.093` → IC=+0.306 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.093 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` > `0.4259` → IC=+0.400 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.4259 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` < `5.4013` → IC=+0.255 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 5.4013 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.289 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `1880.0598` → IC=+0.289 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1880.0598 (IC base=+0.284)

### GBM_LATE_15M#ETH#15min
- **PATRÓN** `drift_60min` |x|≤ `0.0673` → IC=+0.136 (n=31)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.0673 (IC base=+0.065)

- **PATRÓN** `ibs_20min` > `0.772` → IC=+0.182 (n=42)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.772 (IC base=+0.065)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.253` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.253 (IC base=+0.065)

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

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.152 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0053 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.475` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 4.475 (IC base=+0.151)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.151)

### GBM_LATE_15M#XRP#15min
- **PATRÓN** `volumen_regimen` < `0.7863` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.7863 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` < `0.6973` → IC=+0.269 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6973 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` > `1.3677` → IC=+0.225 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.3677 (IC base=+0.043)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `ibs_20min` > `0.9474` → IC=+0.233 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9474 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` > `0.1183` → IC=+0.169 (n=146)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1183 (IC base=+0.059)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.287` → IC=+0.132 (n=948)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 2.287 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.339` → IC=+0.187 (n=97)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.339 (IC base=+0.059)

- **PATRÓN** `volumen_spike_ratio` > `2.8983` → IC=+0.173 (n=279)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.8983 (IC base=+0.059)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.357 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 31.0 (IC base=+0.059)

- **PATRÓN** `ibs_20min` < `0.1` → IC=+0.165 (n=828)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.1 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` > `0.5173` → IC=+0.321 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5173 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` > `1.0773` → IC=+0.225 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0773 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.3619` → IC=+0.405 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3619 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` > `3.805` → IC=+0.306 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.805 (IC base=+0.049)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `sigma_ewma_delta_pct` > `5.003` → IC=-0.206 (n=100)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.003
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=522)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.078` → IC=+0.191 (n=82)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 5.078 (IC base=-0.011)

- **PATRÓN** `volumen_pendiente_norm` > `0.0487` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0487 (IC base=-0.011)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `volumen_regimen` < `0.5727` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.5727 (IC base=-0.003)

- **PATRÓN** `volumen_regimen` > `1.1078` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1078 (IC base=-0.003)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.279 (n=111)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0074 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.0643` → IC=+0.188 (n=110)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.0643 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.248 (n=157)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.106` → IC=+0.309 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.106 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` < `0.1461` → IC=+0.194 (n=230)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.1461 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.4263` → IC=+0.192 (n=37)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.4263 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` < `4.8756` → IC=+0.168 (n=248)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 4.8756 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `3.8997` → IC=+0.204 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.8997 (IC base=+0.182)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.201 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `1905.341` → IC=+0.215 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1905.341 (IC base=+0.182)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.404 (n=102)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.362)

- **PATRÓN** `drift_60min` |x|≤ `0.1847` → IC=+0.364 (n=101)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1847 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.387 (n=139)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.362)

- **PATRÓN** `ibs_20min` < `0.2958` → IC=+0.382 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2958 (IC base=+0.362)

- **PATRÓN** `volumen_pendiente_norm` < `0.3446` → IC=+0.375 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.3446 (IC base=+0.362)

- **PATRÓN** `volumen_pendiente_norm` > `0.1228` → IC=+0.386 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1228 (IC base=+0.362)

- **PATRÓN** `volumen_spike_ratio` < `3.2972` → IC=+0.429 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.2972 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `1855.026` → IC=+0.387 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1855.026 (IC base=+0.362)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `volumen_regimen` > `0.9213` → IC=-0.309 (n=19)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.9213
  - _Potencial_: sin este filtro IC_bueno=-0.109 (n=21)

- **FILTRO** `libro_liquidez` < `8587.8262` → IC=-0.191 (n=53)

  - _Acción_: SKIP cuando `libro_liquidez` < 8587.8262
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=161)

- **FILTRO** `volumen_regimen` > `0.8548` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8548
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=28)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.152 (n=44)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=669)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **PATRÓN** `ibs_20min` > `0.45` → IC=+0.142 (n=135)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.45 (IC base=+0.004)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.282 (n=99)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0065 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.0897` → IC=+0.144 (n=130)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.0897 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.140 (n=109)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.193 (n=99)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.9048` → IC=+0.217 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9048 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.312` → IC=+0.184 (n=55)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.312 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.12` → IC=+0.217 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.12 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` > `0.8047` → IC=+0.157 (n=196)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.8047 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.3135` → IC=+0.210 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3135 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=296)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.276 (n=284)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.276)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.286 (n=255)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.276)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.317 (n=129)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.276)

- **PATRÓN** `ibs_20min` < `0.303` → IC=+0.333 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.303 (IC base=+0.276)

- **PATRÓN** `dist_vwap_pct` > `0.5842` → IC=+0.357 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5842 (IC base=+0.276)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.602` → IC=+0.278 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.602 (IC base=+0.276)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.133` → IC=+0.278 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.133 (IC base=+0.276)

- **PATRÓN** `volumen_regimen` > `1.2726` → IC=+0.335 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2726 (IC base=+0.276)

- **PATRÓN** `volumen_pendiente_norm` > `0.2058` → IC=+0.357 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2058 (IC base=+0.276)

- **PATRÓN** `volumen_spike_ratio` > `3.7273` → IC=+0.283 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.7273 (IC base=+0.276)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.153 (n=399)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0047 (IC base=+0.137)

- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.193 (n=542)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0065 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.145 (n=401)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.157 (n=540)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.9206` → IC=+0.254 (n=792)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9206 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.2179` → IC=+0.144 (n=254)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.2179 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.44` → IC=+0.248 (n=792)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.44 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `0.6285` → IC=+0.133 (n=616)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 0.6285 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.1135` → IC=+0.159 (n=388)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.1135 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.144 (n=1323)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.06 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `2641.3694` → IC=+0.158 (n=396)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2641.3694 (IC base=+0.137)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.223 (n=1141)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.3035` → IC=+0.223 (n=1142)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3035 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.262 (n=527)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` < `0.3642` → IC=+0.286 (n=1141)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3642 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.745` → IC=+0.243 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.745 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` < `1.2618` → IC=+0.193 (n=884)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 1.2618 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` > `0.8864` → IC=+0.211 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8864 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.3248` → IC=+0.293 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3248 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` < `1.7113` → IC=+0.246 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7113 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `3.2928` → IC=+0.253 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.2928 (IC base=+0.216)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.157 (n=100)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0058 (IC base=+0.153)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.203 (n=136)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.212 (n=137)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.327 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.514` → IC=+0.354 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.514 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.1492` → IC=+0.162 (n=66)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.1492 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.08` → IC=+0.175 (n=321)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.08 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.278 (n=79)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.280)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.309 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.280)

- **PATRÓN** `drift_60min` |x|≤ `0.2245` → IC=+0.321 (n=104)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2245 (IC base=+0.280)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.303 (n=120)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.280)

- **PATRÓN** `ibs_20min` < `0.0607` → IC=+0.405 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0607 (IC base=+0.280)

- **PATRÓN** `volumen_pendiente_norm` < `0.08` → IC=+0.314 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.08 (IC base=+0.280)

- **PATRÓN** `volumen_spike_ratio` < `1.8801` → IC=+0.375 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8801 (IC base=+0.280)

- **PATRÓN** `libro_spread` < `0.08` → IC=+0.301 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.08 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `1926.44` → IC=+0.333 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1926.44 (IC base=+0.280)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0017` → IC=+0.258 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0017 (IC base=+0.204)

- **PATRÓN** `sigma_h` > `0.0031` → IC=+0.250 (n=42)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0031 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.268 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `0.7674` → IC=+0.258 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7674 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `0.5406` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5406 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.011` → IC=+0.286 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.011 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` > `0.9007` → IC=+0.234 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9007 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.0992` → IC=+0.271 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0992 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` < `1.4783` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4783 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `1.9813` → IC=+0.233 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9813 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `7185.4978` → IC=+0.250 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7185.4978 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.193 (n=210)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0034 (IC base=+0.190)

- **PATRÓN** `sigma_h` > `0.0024` → IC=+0.199 (n=141)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0024 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.1928` → IC=+0.201 (n=185)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1928 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.260 (n=148)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` < `0.282` → IC=+0.236 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.282 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.586` → IC=+0.297 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.586 (IC base=+0.190)

- **PATRÓN** `volumen_regimen` < `0.6405` → IC=+0.250 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6405 (IC base=+0.190)

- **PATRÓN** `volumen_regimen` > `1.1074` → IC=+0.201 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1074 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` < `0.2719` → IC=+0.218 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2719 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.136` → IC=+0.297 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.136 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` < `1.6686` → IC=+0.292 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6686 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `10996.8422` → IC=+0.194 (n=70)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 10996.8422 (IC base=+0.190)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.188 (n=91)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0075 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.1483` → IC=+0.167 (n=184)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1483 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.179 (n=104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 16.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.206 (n=100)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.301 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.868` → IC=+0.331 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.868 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` < `0.2322` → IC=+0.136 (n=212)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` < 0.2322 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.0546` → IC=+0.208 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0546 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `4.0428` → IC=+0.146 (n=97)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 4.0428 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.192 (n=199)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.04 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `1956.263` → IC=+0.199 (n=91)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 1956.263 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.324 (n=123)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.307)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.316 (n=47)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.307)

- **PATRÓN** `drift_60min` |x|≤ `0.1721` → IC=+0.363 (n=93)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1721 (IC base=+0.307)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.318 (n=130)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.307)

- **PATRÓN** `ibs_20min` < `0.24` → IC=+0.332 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.24 (IC base=+0.307)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.746` → IC=+0.344 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.746 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` > `0.3361` → IC=+0.357 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3361 (IC base=+0.307)

- **PATRÓN** `volumen_spike_ratio` < `3.4774` → IC=+0.326 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.4774 (IC base=+0.307)

- **PATRÓN** `volumen_spike_ratio` > `2.1707` → IC=+0.300 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1707 (IC base=+0.307)

- **PATRÓN** `libro_liquidez` > `1874.461` → IC=+0.337 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1874.461 (IC base=+0.307)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.002` → IC=+0.321 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.002 (IC base=+0.269)

- **PATRÓN** `sigma_h` > `0.0029` → IC=+0.292 (n=51)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0029 (IC base=+0.269)

- **PATRÓN** `drift_60min` |x|≤ `0.1726` → IC=+0.296 (n=52)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1726 (IC base=+0.269)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.287 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.269)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.278 (n=70)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.269)

- **PATRÓN** `ibs_20min` > `0.7743` → IC=+0.323 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7743 (IC base=+0.269)

- **PATRÓN** `dist_vwap_pct` > `0.224` → IC=+0.271 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.224 (IC base=+0.269)

- **PATRÓN** `dist_vwap_pct` < `0.3343` → IC=+0.283 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3343 (IC base=+0.269)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.124` → IC=+0.429 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.124 (IC base=+0.269)

- **PATRÓN** `volumen_regimen` > `0.6809` → IC=+0.285 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6809 (IC base=+0.269)

- **PATRÓN** `volumen_pendiente_norm` > `0.1159` → IC=+0.314 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1159 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` < `1.632` → IC=+0.308 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.632 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` > `2.6482` → IC=+0.294 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6482 (IC base=+0.269)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.264 (n=138)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.1417` → IC=+0.214 (n=138)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1417 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.243 (n=142)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.3077` → IC=+0.264 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3077 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.358` → IC=+0.272 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.358 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `1.2379` → IC=+0.226 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2379 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` < `0.0873` → IC=+0.247 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0873 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.24` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.24 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `1.9183` → IC=+0.289 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9183 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `5263.5402` → IC=+0.198 (n=94)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 5263.5402 (IC base=+0.199)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **FILTRO** `ibs_20min` < `0.875` → IC=-0.121 (n=143)

  - _Acción_: SKIP cuando `ibs_20min` < 0.875
  - _Potencial_: sin este filtro IC_bueno=+0.190 (n=143)

- **FILTRO** `ibs_20min` > `0.5909` → IC=-0.253 (n=75)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5909
  - _Potencial_: sin este filtro IC_bueno=+0.230 (n=228)

- **PATRÓN** `ibs_20min` > `0.875` → IC=+0.190 (n=143)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.875 (IC base=+0.035)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.462` → IC=+0.191 (n=66)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 7.462 (IC base=+0.035)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.218 (n=101)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.110)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.144 (n=237)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 4.0 (IC base=+0.110)

- **PATRÓN** `ibs_20min` < `0.5909` → IC=+0.230 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5909 (IC base=+0.110)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.145` → IC=+0.235 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.145 (IC base=+0.110)

- **PATRÓN** `volumen_regimen` > `0.871` → IC=+0.156 (n=152)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.871 (IC base=+0.110)

- **PATRÓN** `volumen_pendiente_norm` > `0.1257` → IC=+0.245 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1257 (IC base=+0.110)

- **PATRÓN** `volumen_spike_ratio` < `1.5937` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.5937 (IC base=+0.110)

- **PATRÓN** `volumen_spike_ratio` > `2.7817` → IC=+0.214 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7817 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `2302.5984` → IC=+0.231 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2302.5984 (IC base=+0.110)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.263 (n=78)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.115)

- **PATRÓN** `drift_60min` |x|≤ `0.2098` → IC=+0.130 (n=206)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.2098 (IC base=+0.115)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.173 (n=111)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 7.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.221 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` > `0.2825` → IC=+0.182 (n=64)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.2825 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` < `0.0656` → IC=+0.137 (n=166)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.0656 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.396` → IC=+0.227 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.396 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` > `0.327` → IC=+0.179 (n=26)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.327 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` < `1.6027` → IC=+0.138 (n=67)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.6027 (IC base=+0.115)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=238)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.01 (IC base=+0.115)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.273 (n=214)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0063 (IC base=+0.262)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.271 (n=216)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.262)

- **PATRÓN** `drift_60min` |x|≤ `0.0834` → IC=+0.262 (n=82)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0834 (IC base=+0.262)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.278 (n=115)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.262)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.296 (n=96)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.262)

- **PATRÓN** `ibs_20min` < `0.3069` → IC=+0.307 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3069 (IC base=+0.262)

- **PATRÓN** `dist_vwap_pct` > `0.2916` → IC=+0.346 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2916 (IC base=+0.262)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.019` → IC=+0.296 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.019 (IC base=+0.262)

- **PATRÓN** `volumen_regimen` > `0.9066` → IC=+0.316 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9066 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` > `0.3717` → IC=+0.385 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3717 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` > `3.1082` → IC=+0.296 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.1082 (IC base=+0.262)

- **PATRÓN** `libro_liquidez` > `2565.5748` → IC=+0.268 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2565.5748 (IC base=+0.262)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.195 (n=80)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 17.0 (IC base=+0.040)

- **PATRÓN** `ibs_20min` > `0.9824` → IC=+0.164 (n=102)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.9824 (IC base=+0.040)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.989` → IC=+0.247 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.989 (IC base=+0.040)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.280 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.040)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.874` → IC=+0.227 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.874 (IC base=+0.040)

- **PATRÓN** `volumen_spike_ratio` < `1.7456` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.7456 (IC base=+0.040)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=20)

- **FILTRO** `libro_liquidez` < `6436.909` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 6436.909
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.250 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.2693` → IC=+0.167 (n=34)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.2693 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.200 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.2407` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2407 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.363` → IC=+0.267 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.363 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `1.218` → IC=+0.167 (n=34)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.218 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` > `0.7034` → IC=+0.176 (n=35)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.7034 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.0902` → IC=+0.382 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0902 (IC base=+0.141)

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
- **PATRÓN** `sigma_h` > `0.0067` → IC=+0.198 (n=491)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0067 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.148 (n=541)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 17.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.290 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` > `0.3318` → IC=+0.171 (n=147)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.3318 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.302` → IC=+0.231 (n=989)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.302 (IC base=+0.116)

- **PATRÓN** `volumen_pendiente_norm` > `0.1809` → IC=+0.137 (n=337)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.1809 (IC base=+0.116)

- **PATRÓN** `ballena_activa_n` < `107.0` → IC=+0.207 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 107.0 (IC base=+0.116)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.234 (n=1101)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.229)

- **PATRÓN** `sigma_h` > `0.0038` → IC=+0.237 (n=1248)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0038 (IC base=+0.229)

- **PATRÓN** `drift_60min` |x|≤ `0.1566` → IC=+0.230 (n=831)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1566 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.240 (n=1323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` < `0.4851` → IC=+0.289 (n=1246)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4851 (IC base=+0.229)

- **PATRÓN** `dist_vwap_pct` < `0.1532` → IC=+0.202 (n=851)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1532 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.153` → IC=+0.264 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.153 (IC base=+0.229)

- **PATRÓN** `volumen_regimen` < `0.6183` → IC=+0.211 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6183 (IC base=+0.229)

- **PATRÓN** `volumen_regimen` > `1.0809` → IC=+0.224 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0809 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` > `0.1878` → IC=+0.296 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1878 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` < `2.0219` → IC=+0.287 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0219 (IC base=+0.229)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.191 (n=244)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0063 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.159 (n=256)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 11.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.307 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.422` → IC=+0.359 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.422 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.2094` → IC=+0.148 (n=52)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2094 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.180 (n=254)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.06 (IC base=+0.133)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.320 (n=59)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.292)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.325 (n=61)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.2108` → IC=+0.341 (n=155)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2108 (IC base=+0.292)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.299 (n=162)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.292)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.302 (n=160)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.292)

- **PATRÓN** `ibs_20min` < `0.5701` → IC=+0.337 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5701 (IC base=+0.292)

- **PATRÓN** `volumen_pendiente_norm` < `0.0708` → IC=+0.325 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0708 (IC base=+0.292)

- **PATRÓN** `volumen_spike_ratio` < `1.9246` → IC=+0.333 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9246 (IC base=+0.292)

- **PATRÓN** `volumen_spike_ratio` > `2.7667` → IC=+0.321 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7667 (IC base=+0.292)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.325 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `1893.2646` → IC=+0.317 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1893.2646 (IC base=+0.292)

### GBM_LATE_15M_TARDIO#BTC#15min
- **FILTRO** `ibs_20min` < `0.4026` → IC=-0.198 (n=61)

  - _Acción_: SKIP cuando `ibs_20min` < 0.4026
  - _Potencial_: sin este filtro IC_bueno=+0.273 (n=126)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.156 (n=94)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0026 (IC base=+0.119)

- **PATRÓN** `sigma_h` > `0.0031` → IC=+0.151 (n=64)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0031 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.208 (n=94)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.4026` → IC=+0.273 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4026 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `0.3557` → IC=+0.333 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3557 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.193` → IC=+0.225 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.193 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` > `0.9222` → IC=+0.156 (n=94)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.9222 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` < `0.1561` → IC=+0.177 (n=97)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` < 0.1561 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.1037` → IC=+0.174 (n=41)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1037 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `2.8769` → IC=+0.232 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.8769 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `8402.6268` → IC=+0.242 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8402.6268 (IC base=+0.119)

- **PATRÓN** `sigma_h` < `0.0018` → IC=+0.201 (n=75)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0018 (IC base=+0.170)

- **PATRÓN** `sigma_h` > `0.0024` → IC=+0.180 (n=145)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0024 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.1869` → IC=+0.184 (n=191)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1869 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.190 (n=217)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 6.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` < `0.402` → IC=+0.217 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.402 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.232` → IC=+0.263 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.232 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` < `1.3306` → IC=+0.176 (n=217)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 1.3306 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` > `1.1365` → IC=+0.203 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1365 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.0932` → IC=+0.311 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0932 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` < `1.5708` → IC=+0.304 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5708 (IC base=+0.170)

- **PATRÓN** `libro_liquidez` > `4830.6975` → IC=+0.184 (n=194)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 4830.6975 (IC base=+0.170)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.245 (n=100)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0075 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.239 (n=117)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `0.7222` → IC=+0.257 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7222 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.924` → IC=+0.352 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.924 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` < `0.1461` → IC=+0.170 (n=210)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` < 0.1461 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` < `2.2157` → IC=+0.167 (n=100)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.2157 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `4.1058` → IC=+0.170 (n=104)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 4.1058 (IC base=+0.174)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.194 (n=322)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.06 (IC base=+0.174)

- **PATRÓN** `libro_liquidez` > `1915.1184` → IC=+0.196 (n=136)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 1915.1184 (IC base=+0.174)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.366 (n=80)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.289)

- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.290 (n=79)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0075 (IC base=+0.289)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.321 (n=82)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.289)

- **PATRÓN** `ibs_20min` < `0.5337` → IC=+0.342 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5337 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.332` → IC=+0.291 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.332 (IC base=+0.289)

- **PATRÓN** `volumen_pendiente_norm` < `0.2457` → IC=+0.248 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2457 (IC base=+0.289)

- **PATRÓN** `volumen_pendiente_norm` > `0.3976` → IC=+0.308 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3976 (IC base=+0.289)

- **PATRÓN** `volumen_spike_ratio` < `3.7526` → IC=+0.288 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.7526 (IC base=+0.289)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.288 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.289)

### GBM_LATE_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_20min` < `0.3103` → IC=-0.255 (n=47)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3103
  - _Potencial_: sin este filtro IC_bueno=+0.201 (n=142)

- **PATRÓN** `sigma_h` < `0.0019` → IC=+0.200 (n=48)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0019 (IC base=+0.086)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.154 (n=53)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.086)

- **PATRÓN** `ibs_20min` > `0.3103` → IC=+0.201 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3103 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` > `0.4214` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.4214 (IC base=+0.086)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.604` → IC=+0.216 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.604 (IC base=+0.086)

- **PATRÓN** `volumen_regimen` < `0.7759` → IC=+0.177 (n=63)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.7759 (IC base=+0.086)

- **PATRÓN** `volumen_pendiente_norm` > `0.2893` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2893 (IC base=+0.086)

- **PATRÓN** `volumen_spike_ratio` > `2.3201` → IC=+0.274 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3201 (IC base=+0.086)

- **PATRÓN** `libro_liquidez` > `7930.353` → IC=+0.220 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7930.353 (IC base=+0.086)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.219 (n=94)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.05` → IC=+0.206 (n=32)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.05 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.167 (n=94)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 4.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.1374` → IC=+0.300 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1374 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.0972` → IC=+0.260 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.0972 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.753` → IC=+0.278 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.753 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.8847` → IC=+0.214 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8847 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` < `0.0641` → IC=+0.409 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0641 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.8037` → IC=+0.362 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8037 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `4951.8866` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 4951.8866 (IC base=+0.151)

### GBM_LATE_15M_TARDIO#SOL#15min
- **FILTRO** `ibs_20min` < `0.5` → IC=-0.193 (n=73)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=237)

- **FILTRO** `ibs_20min` > `0.5833` → IC=-0.186 (n=68)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5833
  - _Potencial_: sin este filtro IC_bueno=+0.258 (n=209)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.230 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.013)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.923` → IC=+0.162 (n=137)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 2.923 (IC base=+0.013)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.176 (n=183)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.006 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.176` → IC=+0.174 (n=139)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.176 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.218 (n=101)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` < `0.5833` → IC=+0.258 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5833 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.1758` → IC=+0.176 (n=171)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1758 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.235` → IC=+0.250 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.235 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.7176` → IC=+0.192 (n=92)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.7176 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` > `1.1028` → IC=+0.160 (n=95)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 1.1028 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` < `0.1535` → IC=+0.375 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1535 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `1.6077` → IC=+0.370 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6077 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `2.2143` → IC=+0.403 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2143 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `1560.0837` → IC=+0.319 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1560.0837 (IC base=+0.149)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.207 (n=97)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0066 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.0717` → IC=+0.190 (n=98)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.0717 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.181 (n=111)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 6.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.241 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.322` → IC=+0.268 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.322 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.298` → IC=+0.220 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.298 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` > `0.6753` → IC=+0.137 (n=260)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.6753 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.1933` → IC=+0.161 (n=60)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.1933 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=296)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `2586.8192` → IC=+0.128 (n=194)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 2586.8192 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.294 (n=279)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.261)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.282 (n=337)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.261)

- **PATRÓN** `ibs_20min` < `0.1613` → IC=+0.373 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1613 (IC base=+0.261)

- **PATRÓN** `dist_vwap_pct` > `0.4043` → IC=+0.395 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4043 (IC base=+0.261)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.88` → IC=+0.354 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.88 (IC base=+0.261)

- **PATRÓN** `volumen_regimen` > `1.2502` → IC=+0.333 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2502 (IC base=+0.261)

- **PATRÓN** `volumen_pendiente_norm` > `0.2776` → IC=+0.386 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2776 (IC base=+0.261)

- **PATRÓN** `volumen_spike_ratio` < `1.5061` → IC=+0.260 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5061 (IC base=+0.261)

- **PATRÓN** `volumen_spike_ratio` > `2.6958` → IC=+0.261 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6958 (IC base=+0.261)

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
  - _Potencial_: sin este filtro IC_bueno=+0.137 (n=133)

- **PATRÓN** `drift_60min` |x|≤ `0.0923` → IC=+0.152 (n=21)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.0923 (IC base=-0.008)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.150 (n=98)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0037 (IC base=+0.100)

- **PATRÓN** `drift_60min` |x|≤ `0.0725` → IC=+0.175 (n=38)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.0725 (IC base=+0.100)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.204 (n=52)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.127` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 11.127 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` < `1.5368` → IC=+0.132 (n=112)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.5368 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` < `0.1748` → IC=+0.129 (n=103)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1748 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` < `2.5735` → IC=+0.167 (n=97)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.5735 (IC base=+0.100)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.137 (n=133)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `6428.6136` → IC=+0.146 (n=111)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 6428.6136 (IC base=+0.100)

- **PATRÓN** `ballena_activa_n` < `117.0` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 117.0 (IC base=+0.100)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` > `0.0026` → IC=+0.146 (n=46)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` > 0.0026 (IC base=+0.104)

- **PATRÓN** `drift_60min` |x|≤ `0.0856` → IC=+0.188 (n=30)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.0856 (IC base=+0.104)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.204 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.104)

- **PATRÓN** `ibs_20min` < `0.3449` → IC=+0.156 (n=59)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.3449 (IC base=+0.104)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.168` → IC=+0.152 (n=44)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 3.168 (IC base=+0.104)

- **PATRÓN** `volumen_regimen` < `1.6055` → IC=+0.123 (n=67)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 1.6055 (IC base=+0.104)

- **PATRÓN** `volumen_pendiente_norm` > `0.0935` → IC=+0.143 (n=40)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.0935 (IC base=+0.104)

- **PATRÓN** `volumen_spike_ratio` < `2.4757` → IC=+0.156 (n=59)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4757 (IC base=+0.104)

### GBM_LATE_60M
- **FILTRO** `ibs_20min` < `0.6842` → IC=-0.173 (n=50)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6842
  - _Potencial_: sin este filtro IC_bueno=+0.231 (n=102)

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

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.171 (n=138)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0054 (IC base=+0.054)

- **PATRÓN** `drift_60min` |x|≤ `0.1312` → IC=+0.194 (n=34)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1312 (IC base=+0.054)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.316 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` > `0.1249` → IC=+0.156 (n=59)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1249 (IC base=+0.054)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.183` → IC=+0.229 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.183 (IC base=+0.054)

- **PATRÓN** `volumen_regimen` > `1.1022` → IC=+0.225 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1022 (IC base=+0.054)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `sigma_h` > `0.0053` → IC=-0.180 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=45)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.186 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=35)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.321 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.059)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` > `0.1642` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1642 (IC base=+0.059)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `hora_utc` > `5.0` → IC=-0.360 (n=41)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=22)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.224 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.353 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` < `0.1239` → IC=+0.191 (n=40)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.1239 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.347` → IC=+0.346 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.347 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` < `0.8241` → IC=+0.167 (n=34)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8241 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `1.0919` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0919 (IC base=+0.087)

- **PATRÓN** `libro_liquidez` > `2351.5975` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2351.5975 (IC base=+0.087)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0165` → IC=-0.309 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0165
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=58)

- **FILTRO** `ibs_20min` > `0.2381` → IC=-0.308 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2381
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=12)

- **PATRÓN** `sigma_h` > `0.0136` → IC=+0.237 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0136 (IC base=-0.007)

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

- **FILTRO** `ibs_20min` < `0.3671` → IC=-0.300 (n=23)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3671
  - _Potencial_: sin este filtro IC_bueno=-0.284 (n=72)

- **FILTRO** `dist_vwap_pct` < `0.1009` → IC=-0.352 (n=52)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1009
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=43)

- **FILTRO** `libro_liquidez` < `1468.1795` → IC=-0.340 (n=23)

  - _Acción_: SKIP cuando `libro_liquidez` < 1468.1795
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
- **FILTRO** `drift_60min` |x|> `0.0825` → IC=-0.350 (n=18)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.0825
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `ibs_20min` > `0.6061` → IC=+0.147 (n=131)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.6061 (IC base=+0.057)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.188 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 15.0 (IC base=+0.044)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6942` → IC=-0.333 (n=28)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6942
  - _Potencial_: sin este filtro IC_bueno=+0.177 (n=29)

- **FILTRO** `volumen_regimen` < `0.8896` → IC=-0.133 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8896
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=29)

- **PATRÓN** `ibs_20min` > `0.6942` → IC=+0.177 (n=29)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.6942 (IC base=-0.076)

- **PATRÓN** `drift_60min` |x|≤ `0.1318` → IC=+0.167 (n=28)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1318 (IC base=+0.107)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.265 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.107)

- **PATRÓN** `ibs_20min` < `0.1524` → IC=+0.159 (n=39)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.1524 (IC base=+0.107)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.574` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 3.574 (IC base=+0.107)

- **PATRÓN** `volumen_regimen` < `0.5802` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.5802 (IC base=+0.107)

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

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.150 (n=18)

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

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.157 (n=68)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 18.0 (IC base=+0.096)

- **PATRÓN** `drift_20min_pct` |x|≤ `0.0526` → IC=+0.231 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `drift_20min_pct` |x|≤ 0.0526 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `14257.7047` → IC=+0.167 (n=67)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 14257.7047 (IC base=+0.096)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2239.29` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 2239.29
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=15)

### MOMENTUM_IBS_15M#SOL#15min
- **FILTRO** `ibs_20min` > `0.9048` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `ibs_20min` > 0.9048
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=18)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `hora_utc` < `4.0` → IC=-0.256 (n=39)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=166)

- **FILTRO** `py_entrada` < `0.47` → IC=-0.173 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=155)

- **PATRÓN** `hora_utc` < `2.0` → IC=+0.243 (n=72)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 2.0 (IC base=+0.047)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `libro_liquidez` < `2127.3472` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `libro_liquidez` < 2127.3472
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `ibs_20min` < `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `ibs_20min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `hora_utc` > `2.0` → IC=-0.121 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 2.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=13)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `libro_liquidez` < `11848.682` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_liquidez` < 11848.682
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.231 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.159)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.5 (IC base=+0.159)

- **PATRÓN** `ibs_20min` > `0.0944` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0944 (IC base=+0.159)

### MOMENTUM_IBS_15M_BALLENA#SOL#15min
- **FILTRO** `hora_utc` > `4.0` → IC=-0.133 (n=28)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **PATRÓN** `ballena_activa_n` < `1.0` → IC=+0.132 (n=17)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 1.0 (IC base=+0.024)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `hora_utc` < `16.0` → IC=-0.300 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=88)

- **FILTRO** `hora_utc` > `19.0` → IC=-0.206 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=89)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.159 (n=39)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=51)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=69)

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

### MOMENTUM_IBS_5M#SOL#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1118` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1118
  - _Potencial_: sin este filtro IC_bueno=+0.127 (n=57)

- **PATRÓN** `drift_7min_pct` |x|≤ `0.1118` → IC=+0.127 (n=57)

  - _Acción_: Kelly boost +0.64€ cuando `drift_7min_pct` |x|≤ 0.1118 (IC base=+0.046)

### MOMENTUM_IBS_5M_BALLENA
- **FILTRO** `hora_utc` < `3.0` → IC=-0.203 (n=116)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=452)

- **FILTRO** `py_entrada` < `0.39` → IC=-0.291 (n=137)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=431)

- **FILTRO** `ibs_7min` < `0.7692` → IC=-0.222 (n=142)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7692
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=426)

- **FILTRO** `ballena_activa_n` > `20.0` → IC=-0.229 (n=138)

  - _Acción_: SKIP cuando `ballena_activa_n` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=430)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.283 (n=118)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=363)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `ballena_activa_n` > `2.0` → IC=-0.122 (n=72)

  - _Acción_: SKIP cuando `ballena_activa_n` > 2.0
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=27)

- **FILTRO** `py_entrada` > `0.53` → IC=-0.198 (n=41)

  - _Acción_: SKIP cuando `py_entrada` > 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.196 (n=21)

- **PATRÓN** `py_entrada` < `0.53` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.53 (IC base=-0.062)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `5.0` → IC=-0.237 (n=36)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=85)

- **FILTRO** `py_entrada` < `0.43` → IC=-0.219 (n=30)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=91)

- **FILTRO** `ballena_activa_n` > `73.0` → IC=-0.242 (n=29)

  - _Acción_: SKIP cuando `ballena_activa_n` > 73.0
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=92)

- **FILTRO** `hora_utc` > `6.0` → IC=-0.154 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=51)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=49)

- **FILTRO** `drift_7min_pct` |x|> `0.0675` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.0675
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=51)

- **FILTRO** `ballena_activa_n` > `50.0` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `ballena_activa_n` > 50.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=50)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `3.0` → IC=-0.214 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=71)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.413 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=69)

- **FILTRO** `ibs_7min` < `0.2222` → IC=-0.333 (n=22)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2222
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=68)

- **FILTRO** `libro_liquidez` < `2676.4096` → IC=-0.221 (n=59)

  - _Acción_: SKIP cuando `libro_liquidez` < 2676.4096
  - _Potencial_: sin este filtro IC_bueno=+0.197 (n=31)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.328 (n=27)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=57)

- **FILTRO** `ibs_7min` > `0.2661` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2661
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=64)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `3.0` → IC=-0.250 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=60)

- **FILTRO** `py_entrada` < `0.4` → IC=-0.380 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=55)

- **FILTRO** `ibs_7min` < `0.8167` → IC=-0.309 (n=19)

  - _Acción_: SKIP cuando `ibs_7min` < 0.8167
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=59)

- **FILTRO** `ballena_activa_n` > `29.0` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `ballena_activa_n` > 29.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=59)

- **FILTRO** `libro_liquidez` < `8454.1975` → IC=-0.160 (n=51)

  - _Acción_: SKIP cuando `libro_liquidez` < 8454.1975
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=27)

- **FILTRO** `hora_utc` > `3.0` → IC=-0.148 (n=52)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=27)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `hora_utc` < `3.0` → IC=-0.200 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=77)

- **FILTRO** `py_entrada` < `0.46` → IC=-0.292 (n=22)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=73)

- **FILTRO** `ibs_7min` < `0.875` → IC=-0.258 (n=31)

  - _Acción_: SKIP cuando `ibs_7min` < 0.875
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=64)

- **FILTRO** `ballena_activa_n` > `16.0` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `ballena_activa_n` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=72)

- **FILTRO** `libro_liquidez` < `3862.8762` → IC=-0.133 (n=47)

  - _Acción_: SKIP cuando `libro_liquidez` < 3862.8762
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=48)

- **PATRÓN** `hora_utc` < `2.0` → IC=+0.190 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 2.0 (IC base=+0.011)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `3.0` → IC=-0.167 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=66)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.274 (n=29)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=56)

- **FILTRO** `ibs_7min` < `0.7191` → IC=-0.370 (n=21)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7191
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=64)

- **FILTRO** `ballena_activa_n` > `17.0` → IC=-0.326 (n=21)

  - _Acción_: SKIP cuando `ballena_activa_n` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=64)

- **FILTRO** `libro_liquidez` < `3608.1023` → IC=-0.121 (n=56)

  - _Acción_: SKIP cuando `libro_liquidez` < 3608.1023
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=29)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.333 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=71)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.160 (n=48)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` < 0.5 (IC base=-0.016)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=49)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.156 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 18.0 (IC base=+0.053)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **PATRÓN** `libro_liquidez` > `9403.9837` → IC=+0.189 (n=43)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 9403.9837 (IC base=+0.034)

### ORDER_FLOW_5M
- **FILTRO** `total_vol_5m` > `215.224` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `total_vol_5m` > 215.224
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `delta_ratio` |x|> `0.401` → IC=+0.157 (n=129)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.78€ cuando `delta_ratio` |x|> 0.401 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.150 (n=58)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 18.0 (IC base=+0.130)

- **PATRÓN** `total_vol_5m` < `389.535` → IC=+0.263 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 389.535 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.130)

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
- **FILTRO** `hora_utc` > `15.0` → IC=-0.167 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=81)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=76)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.214 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=-0.024)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `4.0` → IC=-0.143 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=15)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` < 0.495 (IC base=-0.061)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `hora_utc` > `13.0` → IC=-0.265 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=31)

- **FILTRO** `streak_estiramiento` > `0.6628` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.6628
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=31)

### STREAK_MOM_5M
- **FILTRO** `ballena_activa_n` > `35.0` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `ballena_activa_n` > 35.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=42)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.123 (n=51)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 27.0 (IC base=+0.031)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `hora_utc` > `8.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=37)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.198 (n=41)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 10.0 (IC base=+0.074)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `py_entrada` < 0.495 (IC base=+0.074)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=61)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.208 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.103)

- **PATRÓN** `streak_len` < `3.0` → IC=+0.167 (n=61)

  - _Acción_: Kelly boost +0.83€ cuando `streak_len` < 3.0 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `3533.817` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 3533.817 (IC base=+0.103)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=657)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=361)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=369)

### UPDOWN_GBM#15min
- **FILTRO** `ibs_15` < `0.5675` → IC=-0.164 (n=135)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5675
  - _Potencial_: sin este filtro IC_bueno=+0.224 (n=277)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.125 (n=206)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` > 0.0047 (IC base=+0.097)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1508` → IC=+0.120 (n=206)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.60€ cuando `delta_ratio_macro` |x|> 0.1508 (IC base=+0.097)

- **PATRÓN** `ibs_15` > `0.5675` → IC=+0.224 (n=277)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5675 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.4172` → IC=+0.182 (n=61)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.4172 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.027` → IC=+0.222 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.027 (IC base=+0.097)

- **PATRÓN** `ibs_15` < `0.5332` → IC=+0.128 (n=323)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.64€ cuando `ibs_15` < 0.5332 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` > `0.5751` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5751 (IC base=+0.081)

### UPDOWN_GBM#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0045` → IC=-0.154 (n=183)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0045
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=62)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.0711` → IC=-0.135 (n=61)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.0711
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=184)

- **FILTRO** `ibs_15` < `0.0909` → IC=-0.274 (n=60)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.0909
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=185)

- **FILTRO** `dist_vwap_pct` > `0.2843` → IC=-0.133 (n=47)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2843
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=178)

- **FILTRO** `sigma_ewma_delta_pct` > `5.327` → IC=-0.188 (n=62)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.327
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=183)

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
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0387` → IC=-0.206 (n=15)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0387
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `libro_liquidez` < `10617.4307` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 10617.4307
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=6)

- **PATRÓN** `sigma_h` > `0.002` → IC=+0.130 (n=71)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` > 0.002 (IC base=+0.115)

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
- **FILTRO** `sigma_h` < `0.0034` → IC=-0.214 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

- **FILTRO** `ibs_15` < `0.0668` → IC=-0.324 (n=15)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.0668
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=15)

- **PATRÓN** `drift_60min` |x|≤ `0.1514` → IC=+0.156 (n=30)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1514 (IC base=+0.041)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.866` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.866 (IC base=+0.041)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `ibs_15` < `0.9182` → IC=-0.150 (n=38)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.9182
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=21)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `ibs_15` < `0.6973` → IC=-0.152 (n=44)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6973
  - _Potencial_: sin este filtro IC_bueno=+0.330 (n=45)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1329` → IC=+0.223 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1329 (IC base=+0.093)

- **PATRÓN** `ibs_15` > `0.6973` → IC=+0.330 (n=45)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6973 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` < `0.1005` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1005 (IC base=+0.093)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.937` → IC=+0.188 (n=30)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 8.937 (IC base=+0.093)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.184 (n=74)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0051 (IC base=+0.158)

- **PATRÓN** `sigma_h` > `0.0042` → IC=+0.207 (n=56)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0042 (IC base=+0.158)

- **PATRÓN** `drift_60min` |x|≤ `0.4834` → IC=+0.167 (n=85)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.4834 (IC base=+0.158)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1157` → IC=+0.179 (n=76)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.1157 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.190 (n=56)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 13.0 (IC base=+0.158)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.167 (n=79)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 14.0 (IC base=+0.158)

- **PATRÓN** `ibs_15` < `0.3247` → IC=+0.178 (n=85)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.89€ cuando `ibs_15` < 0.3247 (IC base=+0.158)

- **PATRÓN** `ibs_15` > `0.0292` → IC=+0.209 (n=84)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.0292 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `0.1727` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1727 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` < `17.598` → IC=+0.209 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 17.598 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `10905.3195` → IC=+0.267 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10905.3195 (IC base=+0.158)

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

- **PATRÓN** `ibs_15` > `0.0732` → IC=+0.122 (n=35)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.61€ cuando `ibs_15` > 0.0732 (IC base=+0.056)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `ibs_15` < `0.6` → IC=-0.177 (n=29)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.242 (n=29)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.0898` → IC=-0.167 (n=19)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.0898
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=57)

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

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.214 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.086)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.143 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 8.0 (IC base=+0.086)

- **PATRÓN** `ibs_15` < `0.0952` → IC=+0.357 (n=19)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.0952 (IC base=+0.086)

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

- **PATRÓN** `drift_60min` |x|≤ `0.1447` → IC=+0.203 (n=35)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1447 (IC base=+0.100)

- **PATRÓN** `delta_ratio_macro` |x|> `0.094` → IC=+0.153 (n=93)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio_macro` |x|> 0.094 (IC base=+0.100)

- **PATRÓN** `hora_utc` < `19.0` → IC=+0.141 (n=104)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 19.0 (IC base=+0.100)

- **PATRÓN** `ibs_15` < `0.2` → IC=+0.222 (n=70)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `0.127` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.127 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.138` → IC=+0.144 (n=88)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 5.138 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `2522.0608` → IC=+0.141 (n=104)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2522.0608 (IC base=+0.100)

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

- **PATRÓN** `ibs_15` > `0.9071` → IC=+0.257 (n=35)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9071 (IC base=+0.204)

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
- **FILTRO** `ibs_15` < `0.5659` → IC=-0.269 (n=106)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5659
  - _Potencial_: sin este filtro IC_bueno=+0.241 (n=106)

- **FILTRO** `sigma_ewma_delta_pct` > `12.735` → IC=-0.141 (n=207)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 12.735
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=854)

- **PATRÓN** `ibs_15` > `0.5659` → IC=+0.241 (n=106)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5659 (IC base=-0.033)

- **PATRÓN** `ibs_15` < `0.2364` → IC=+0.300 (n=28)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2364 (IC base=-0.048)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.236 (n=70)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=168)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.209 (n=53)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=185)

- **FILTRO** `sigma_ewma_delta_pct` < `9.186` → IC=-0.215 (n=135)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 9.186
  - _Potencial_: sin este filtro IC_bueno=-0.138 (n=103)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `sigma_h` > `0.0048` → IC=-0.182 (n=20)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=64)

- **FILTRO** `ibs_15` < `0.4479` → IC=-0.386 (n=42)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.4479
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=42)

- **PATRÓN** `ibs_15` > `0.4479` → IC=+0.159 (n=42)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.80€ cuando `ibs_15` > 0.4479 (IC base=-0.116)

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.0411` → IC=+0.206 (n=15)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.0411 (IC base=+0.189)

- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.208 (n=22)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0045 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.260 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.189)

- **PATRÓN** `ibs_15` < `0.2364` → IC=+0.333 (n=22)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2364 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.094` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.094 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `3786.4324` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3786.4324 (IC base=+0.189)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` > `13.898` → IC=-0.190 (n=56)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 13.898
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=320)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.371` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.371 (IC base=+0.012)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` < `0.0054` → IC=-0.138 (n=67)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0054
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=67)

- **FILTRO** `libro_liquidez` < `2507.6219` → IC=-0.174 (n=44)

  - _Acción_: SKIP cuando `libro_liquidez` < 2507.6219
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=90)

- **FILTRO** `sigma_ewma_delta_pct` > `7.734` → IC=-0.159 (n=80)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.734
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=268)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` > `0.0032` → IC=+0.255 (n=47)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0032 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.1815` → IC=+0.252 (n=103)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1815 (IC base=+0.241)

- **PATRÓN** `drift_15min` |x|≤ `0.6305` → IC=+0.253 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.6305 (IC base=+0.241)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0679` → IC=+0.262 (n=103)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0679 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.287 (n=92)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.241)

- **PATRÓN** `ibs_15` > `0.9356` → IC=+0.317 (n=69)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9356 (IC base=+0.241)

- **PATRÓN** `dist_vwap_pct` > `0.3632` → IC=+0.324 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3632 (IC base=+0.241)

- **PATRÓN** `dist_vwap_pct` < `0.0834` → IC=+0.290 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0834 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `14.106` → IC=+0.250 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 14.106 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.98` → IC=+0.247 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.98 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `5059.1554` → IC=+0.246 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5059.1554 (IC base=+0.241)

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
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.250 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.255)

- **PATRÓN** `sigma_h` > `0.0027` → IC=+0.284 (n=35)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0027 (IC base=+0.255)

- **PATRÓN** `drift_60min` |x|≤ `0.1348` → IC=+0.250 (n=34)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1348 (IC base=+0.255)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1879` → IC=+0.400 (n=18)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1879 (IC base=+0.255)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.255)

- **PATRÓN** `ibs_15` > `0.9678` → IC=+0.400 (n=18)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9678 (IC base=+0.255)

- **PATRÓN** `dist_vwap_pct` < `0.0769` → IC=+0.300 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0769 (IC base=+0.255)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.888` → IC=+0.260 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.888 (IC base=+0.255)

- **PATRÓN** `sigma_ewma_delta_pct` < `16.209` → IC=+0.257 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 16.209 (IC base=+0.255)

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

- **H-IBS-UPDOWN_GBM#SOL#5min**: dentro de BUY_NO, IBS < 0.0952 sube el IC de +0.086 a +0.357 en UPDOWN_GBM#SOL#5min (n=19). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5675 sube el IC de +0.097 a +0.224 en UPDOWN_GBM#15min (n=277). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.9375 sube el IC de +0.115 a +0.235 en UPDOWN_GBM#BTC#15min (n=32). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6973 sube el IC de +0.093 a +0.330 en UPDOWN_GBM#ETH#15min (n=45). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_NO, IBS < 0.3247 sube el IC de +0.158 a +0.178 en UPDOWN_GBM#ETH#15min (n=85). Ya aplicado como kelly_boost=+0.89€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_NO, IBS > 0.0292 sube el IC de +0.158 a +0.209 en UPDOWN_GBM#ETH#15min (n=84). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.033 a +0.242 en UPDOWN_GBM#SOL#15min (n=29). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.4444 sube el IC de +0.081 a +0.153 en UPDOWN_GBM#XRP#15min (n=96). Ya aplicado como kelly_boost=+0.77€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.2 sube el IC de +0.100 a +0.222 en UPDOWN_GBM#XRP#15min (n=70). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.5659 sube el IC de -0.033 a +0.241 en UPDOWN_GBM_15M_TARDIO (n=106). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.2364 sube el IC de -0.048 a +0.300 en UPDOWN_GBM_15M_TARDIO (n=28). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.4479 sube el IC de -0.116 a +0.159 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=42). Ya aplicado como kelly_boost=+0.80€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.2364 sube el IC de +0.189 a +0.333 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=22). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.9356 sube el IC de +0.241 a +0.317 en UPDOWN_GBM_IBS_ALTO (n=69). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS < 0.9998 sube el IC de +0.227 a +0.231 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=65). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.9362 sube el IC de +0.227 a +0.278 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=43). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.9678 sube el IC de +0.255 a +0.400 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=18). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7823 sube el IC de +0.238 a +0.308 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=71). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS < 0.9942 sube el IC de +0.204 a +0.204 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=52). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.9071 sube el IC de +0.204 a +0.257 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=35). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min` — IC=+0.289 n=36. Faltan ~4 resoluciones para umbral n≥40. ETA: ~3h.
- **LIVE-CANDIDATA**: `UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH` — IC=+0.289 n=36. Faltan ~4 resoluciones para umbral n≥40. ETA: ~3h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min` — IC=+0.425 n=38. Faltan ~2 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL` — IC=+0.425 n=38. Faltan ~2 resoluciones para umbral n≥40. ETA: ~1h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 483 | +0.044 | +38.08€ | 3 | 4 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 483 | +0.044 | +38.08€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 252 | +0.043 | +24.96€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 252 | +0.043 | +24.96€ | 2 | 4 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 207 | +0.021 | -0.09€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 207 | +0.021 | -0.09€ | 6 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 24 | +0.231 | +13.21€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 24 | +0.231 | +13.21€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 3135 | -0.117 | -475.82€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 437 | -0.006 | -6.14€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 2698 | -0.134 | -469.69€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 350 | -0.196 | -102.44€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 350 | -0.196 | -102.44€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 437 | -0.006 | -6.14€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 437 | -0.006 | -6.14€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 294 | -0.172 | -148.69€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 294 | -0.172 | -148.69€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 707 | -0.138 | -38.01€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 707 | -0.138 | -38.01€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 743 | -0.021 | -89.55€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 743 | -0.021 | -89.55€ | 1 | 0 |
| 🚫 BALLENAS_TARDIAS#XRP | 604 | -0.214 | -91.00€ | 0 | 0 |
| 🚫 BALLENAS_TARDIAS#XRP#5min | 604 | -0.214 | -91.00€ | 1 | 0 |
| ✅ FAVORITO_CONFIRMADO | 13395 | +0.116 | -793.86€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 3256 | +0.178 | -127.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 98 | -0.100 | -46.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 7477 | +0.086 | -636.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 2564 | +0.131 | +16.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 1265 | +0.034 | -275.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 13 | -0.065 | -2.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 1248 | +0.038 | -267.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 3088 | +0.140 | -6.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 887 | +0.191 | -42.76€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 41 | -0.105 | -20.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 1245 | +0.112 | -7.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 915 | +0.139 | +63.60€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 1261 | +0.052 | -226.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 9 | -0.021 | -3.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 1251 | +0.053 | -221.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 3340 | +0.125 | -55.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 1201 | +0.158 | -30.11€ | 0 | 7 |
| 🚫 FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 1243 | +0.103 | -17.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 884 | +0.116 | +1.08€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 3182 | +0.137 | -194.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 1134 | +0.195 | -50.14€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 39 | +0.012 | -7.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 1244 | +0.086 | -88.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 765 | +0.138 | -48.04€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 1259 | +0.122 | -34.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 12 | +0.043 | +1.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 1246 | +0.123 | -35.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3325 | +0.163 | -304.05€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 3325 | +0.163 | -304.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 834 | +0.159 | -103.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 834 | +0.159 | -103.18€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 73 | -0.087 | -3.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 73 | -0.087 | -3.17€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 826 | +0.161 | -101.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 826 | +0.161 | -101.62€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 735 | +0.218 | -40.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 735 | +0.218 | -40.25€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 1 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 778 | +0.179 | -69.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 778 | +0.179 | -69.58€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 159 | +0.413 | -9.08€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 159 | +0.413 | -9.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 57 | +0.415 | -1.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 57 | +0.415 | -1.78€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 62 | +0.375 | -7.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 62 | +0.375 | -7.52€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 38 | +0.425 | +0.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 38 | +0.425 | +0.18€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 5340 | +0.194 | -467.23€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 5340 | +0.194 | -467.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 1010 | +0.102 | -221.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 1010 | +0.102 | -221.42€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 824 | +0.254 | -0.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 824 | +0.254 | -0.52€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 944 | +0.150 | -141.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 944 | +0.150 | -141.00€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 867 | +0.224 | -33.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 867 | +0.224 | -33.91€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 820 | +0.253 | -2.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 820 | +0.253 | -2.11€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 875 | +0.202 | -68.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 875 | +0.202 | -68.27€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1895 | +0.149 | +102.09€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 1895 | +0.149 | +102.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 942 | +0.154 | +58.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 942 | +0.154 | +58.95€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 953 | +0.145 | +43.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 953 | +0.145 | +43.15€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 524 | +0.295 | -2.33€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 524 | +0.295 | -2.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 220 | +0.266 | -13.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 220 | +0.266 | -13.27€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 244 | +0.297 | +4.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 244 | +0.297 | +4.48€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 60 | +0.371 | +6.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 60 | +0.371 | +6.46€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 219 | +0.405 | -12.36€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 219 | +0.405 | -12.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 98 | +0.400 | -6.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 98 | +0.400 | -6.41€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 97 | +0.409 | -6.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 97 | +0.409 | -6.09€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 24 | +0.346 | +0.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 24 | +0.346 | +0.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 239 | +0.259 | -27.60€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 239 | +0.259 | -27.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 239 | +0.259 | -27.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 239 | +0.259 | -27.60€ | 0 | 4 |
| ✅ GBM_LATE_15M | 4302 | +0.090 | +1536.94€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 4302 | +0.090 | +1536.94€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 746 | +0.175 | +465.63€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 746 | +0.175 | +465.63€ | 0 | 18 |
| ✅ GBM_LATE_15M#BTC | 408 | +0.171 | +184.28€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 408 | +0.171 | +184.28€ | 0 | 22 |
| ✅ GBM_LATE_15M#DOGE | 748 | +0.193 | +516.67€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 748 | +0.193 | +516.67€ | 0 | 19 |
| ✅ GBM_LATE_15M#ETH | 581 | +0.003 | +40.46€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 581 | +0.003 | +40.46€ | 0 | 3 |
| ✅ GBM_LATE_15M#SOL | 817 | +0.010 | +84.04€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 817 | +0.010 | +84.04€ | 3 | 3 |
| ✅ GBM_LATE_15M#XRP | 1002 | +0.032 | +245.86€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 1002 | +0.032 | +245.86€ | 0 | 3 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 5318 | +0.052 | +1618.18€ | 0 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 5318 | +0.052 | +1618.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 1021 | -0.026 | +192.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 1021 | -0.026 | +192.07€ | 1 | 2 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 1006 | +0.000 | +126.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 1006 | +0.000 | +126.47€ | 0 | 2 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 639 | +0.239 | +582.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 639 | +0.239 | +582.19€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 927 | -0.009 | +38.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 927 | -0.009 | +38.22€ | 4 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 956 | +0.006 | +94.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 956 | +0.006 | +94.86€ | 0 | 1 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 769 | +0.200 | +584.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 769 | +0.200 | +584.36€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 3101 | +0.176 | +2110.03€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 3101 | +0.176 | +2110.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 553 | +0.190 | +396.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 553 | +0.190 | +396.52€ | 0 | 16 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 402 | +0.196 | +268.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 402 | +0.196 | +268.86€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 549 | +0.206 | +435.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 549 | +0.206 | +435.35€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 376 | +0.220 | +292.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 376 | +0.220 | +292.97€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 589 | +0.074 | +239.45€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 589 | +0.074 | +239.45€ | 2 | 11 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 632 | +0.191 | +476.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 632 | +0.191 | +476.88€ | 0 | 22 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 522 | +0.040 | +39.72€ | 0 | 6 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 522 | +0.040 | +39.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 90 | +0.043 | -4.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 90 | +0.043 | -4.47€ | 2 | 8 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 111 | +0.164 | +45.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 111 | +0.164 | +45.68€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 224 | -0.013 | +3.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 224 | -0.013 | +3.57€ | 4 | 2 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 97 | +0.015 | -5.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 97 | +0.015 | -5.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO | 3618 | +0.168 | +2332.65€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#15min | 3618 | +0.168 | +2332.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 717 | +0.186 | +498.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 717 | +0.186 | +498.59€ | 0 | 17 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 476 | +0.151 | +246.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 476 | +0.151 | +246.86€ | 1 | 22 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 716 | +0.226 | +614.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 716 | +0.226 | +614.28€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 313 | +0.113 | +123.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 313 | +0.113 | +123.70€ | 1 | 19 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 587 | +0.077 | +240.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 587 | +0.077 | +240.15€ | 2 | 14 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 809 | +0.197 | +609.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 809 | +0.197 | +609.07€ | 0 | 20 |
| ✅ GBM_LATE_5M | 209 | +0.069 | +34.71€ | 3 | 11 |
| ✅ GBM_LATE_5M#5min | 209 | +0.069 | +34.71€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 102 | +0.058 | +12.36€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 102 | +0.058 | +12.36€ | 0 | 8 |
| ✅ GBM_LATE_5M#ETH | 54 | +0.179 | +23.38€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 54 | +0.179 | +23.38€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL | 43 | -0.078 | -2.66€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 43 | -0.078 | -2.66€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP | 10 | +0.083 | +1.62€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 10 | +0.083 | +1.62€ | 0 | 0 |
| ✅ GBM_LATE_60M | 482 | -0.052 | +55.40€ | 4 | 6 |
| ✅ GBM_LATE_60M#60min | 482 | -0.052 | +55.40€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 168 | -0.006 | +5.79€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 168 | -0.006 | +5.79€ | 2 | 3 |
| ✅ GBM_LATE_60M#ETH | 170 | -0.035 | +32.45€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 170 | -0.035 | +32.45€ | 1 | 7 |
| ✅ GBM_LATE_60M#SOL | 144 | -0.123 | +17.15€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 144 | -0.123 | +17.15€ | 2 | 1 |
| 🚫 GBM_LATE_60M_FADE | 189 | -0.301 | -32.44€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 189 | -0.301 | -32.44€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 75 | -0.253 | -6.85€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 75 | -0.253 | -6.85€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 64 | -0.348 | -18.54€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 64 | -0.348 | -18.54€ | 2 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 50 | -0.288 | -7.05€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 50 | -0.288 | -7.05€ | 1 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 297 | +0.052 | +11.71€ | 0 | 2 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 297 | +0.052 | +11.71€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 116 | +0.017 | +5.71€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 116 | +0.017 | +5.71€ | 2 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 65 | +0.142 | +9.31€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 65 | +0.142 | +9.31€ | 0 | 2 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 116 | +0.034 | -3.31€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 116 | +0.034 | -3.31€ | 1 | 5 |
| ✅ LEADLAG_BTC_XRP_15M | 47 | +0.153 | +12.88€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 47 | +0.153 | +12.88€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 47 | +0.153 | +12.88€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 47 | +0.153 | +12.88€ | 0 | 1 |
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
| ✅ LIQUIDACIONES_5M | 76 | -0.167 | -13.99€ | 2 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 76 | -0.167 | -13.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 21 | -0.109 | -2.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 21 | -0.109 | -2.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE | 8 | -0.040 | -1.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 8 | -0.040 | -1.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 17 | -0.112 | -2.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 17 | -0.112 | -2.75€ | 0 | 0 |
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
| ✅ MOMENTUM_IBS_15M | 364 | +0.044 | +12.53€ | 1 | 3 |
| ✅ MOMENTUM_IBS_15M#15min | 364 | +0.044 | +12.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 59 | -0.008 | -2.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 59 | -0.008 | -2.96€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 60 | +0.081 | +9.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 60 | +0.081 | +9.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 60 | -0.016 | -8.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 60 | -0.016 | -8.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 62 | +0.141 | +24.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 62 | +0.141 | +24.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 62 | -0.016 | -10.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 62 | -0.016 | -10.60€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 61 | +0.071 | +1.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 61 | +0.071 | +1.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 428 | +0.005 | +28.51€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 428 | +0.005 | +28.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 67 | -0.036 | +14.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 67 | -0.036 | +14.38€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 72 | -0.041 | -4.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 72 | -0.041 | -4.95€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 72 | +0.041 | +13.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 72 | +0.041 | +13.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 72 | +0.068 | +8.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 72 | +0.068 | +8.72€ | 1 | 3 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 70 | -0.042 | -7.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 70 | -0.042 | -7.36€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 75 | +0.033 | +4.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 75 | +0.033 | +4.29€ | 0 | 1 |
| ✅ MOMENTUM_IBS_15M_FADE | 211 | -0.110 | -26.21€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 211 | -0.110 | -26.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 25 | -0.093 | -3.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 25 | -0.093 | -3.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 39 | -0.110 | -4.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 39 | -0.110 | -4.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 26 | -0.143 | -4.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 26 | -0.143 | -4.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 47 | -0.153 | -8.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 47 | -0.153 | -8.12€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 40 | -0.071 | -3.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 40 | -0.071 | -3.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 34 | -0.056 | -2.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 34 | -0.056 | -2.24€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 954 | +0.001 | +1.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 954 | +0.001 | +1.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 119 | -0.029 | -0.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 119 | -0.029 | -0.78€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 171 | +0.009 | -2.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 171 | +0.009 | -2.20€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 123 | +0.012 | +0.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 123 | +0.012 | +0.52€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#ETH | 189 | +0.008 | +5.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 189 | +0.008 | +5.90€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 193 | +0.008 | +3.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 193 | +0.008 | +3.83€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#XRP | 159 | -0.009 | -5.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 159 | -0.009 | -5.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 1049 | -0.070 | -92.58€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 1049 | -0.070 | -92.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 161 | -0.064 | +8.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 161 | -0.064 | +8.94€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 196 | -0.076 | -23.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 196 | -0.076 | -23.15€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 174 | -0.074 | -28.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 174 | -0.074 | -28.43€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 157 | -0.104 | -18.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 157 | -0.104 | -18.55€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 183 | -0.057 | -14.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 183 | -0.057 | -14.53€ | 5 | 1 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 178 | -0.044 | -16.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 178 | -0.044 | -16.86€ | 6 | 1 |
| ✅ MOMENTUM_IBS_5M_FADE | 1091 | +0.014 | -2.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 1091 | +0.014 | -2.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 183 | +0.041 | +9.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 183 | +0.041 | +9.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 165 | +0.039 | -0.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 165 | +0.039 | -0.16€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 186 | -0.011 | -4.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 186 | -0.011 | -4.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 190 | +0.000 | -4.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 190 | +0.000 | -4.73€ | 0 | 1 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 189 | -0.003 | -2.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 189 | -0.003 | -2.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 178 | +0.022 | -0.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 178 | +0.022 | -0.51€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 209 | +0.073 | +31.68€ | 1 | 4 |
| ✅ ORDER_FLOW_5M#5min | 73 | +0.100 | +19.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 18 | +0.225 | +16.68€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 18 | +0.225 | +16.68€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE | 15 | +0.022 | +1.28€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 15 | +0.022 | +1.28€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL | 20 | +0.045 | +0.36€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 20 | +0.045 | +0.36€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP | 17 | +0.022 | -0.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 17 | +0.022 | -0.62€ | 0 | 0 |
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
| ✅ STREAK_FADE_15M | 43 | -0.144 | -13.10€ | 0 | 0 |
| ✅ STREAK_FADE_15M#15min | 43 | -0.144 | -13.10€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 18 | -0.045 | -4.15€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 18 | -0.045 | -4.15€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 20 | -0.182 | -6.74€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 20 | -0.182 | -6.74€ | 0 | 0 |
| ✅ STREAK_FADE_5M | 314 | -0.029 | -20.23€ | 2 | 1 |
| ✅ STREAK_FADE_5M#5min | 314 | -0.029 | -20.23€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 70 | +0.042 | +2.82€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 70 | +0.042 | +2.82€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 113 | -0.004 | -6.04€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 113 | -0.004 | -6.04€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 61 | -0.087 | -8.73€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 61 | -0.087 | -8.73€ | 1 | 1 |
| ✅ STREAK_FADE_5M#XRP | 70 | -0.083 | -8.27€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 70 | -0.083 | -8.27€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 15 | -0.066 | -1.71€ | 0 | 0 |
| ✅ STREAK_FADE_60M#60min | 15 | -0.066 | -1.71€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 9 | -0.061 | -1.63€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 9 | -0.061 | -1.63€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 535 | +0.033 | +9.72€ | 1 | 1 |
| ✅ STREAK_MOM_5M#5min | 535 | +0.033 | +9.72€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 158 | +0.013 | -2.07€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 158 | +0.013 | -2.07€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 112 | +0.000 | -0.85€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 112 | +0.000 | -0.85€ | 1 | 2 |
| ✅ STREAK_MOM_5M#SOL | 141 | +0.045 | +3.46€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 141 | +0.045 | +3.46€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP | 124 | +0.071 | +9.18€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 124 | +0.071 | +9.18€ | 1 | 3 |
| ✅ STRUCT_NO_15M | 1772 | +0.011 | -11.57€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 1772 | +0.011 | -11.57€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 676 | +0.006 | -8.58€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 676 | +0.006 | -8.58€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 703 | +0.015 | -2.14€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 703 | +0.015 | -2.14€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 393 | +0.014 | -0.85€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 393 | +0.014 | -0.85€ | 2 | 0 |
| ✅ UPDOWN_GBM | 1941 | +0.018 | +93.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 842 | +0.089 | +147.80€ | 1 | 7 |
| ✅ UPDOWN_GBM#240min | 112 | +0.026 | +0.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 694 | -0.037 | -43.71€ | 5 | 0 |
| ✅ UPDOWN_GBM#60min | 246 | -0.024 | -10.64€ | 2 | 1 |
| ✅ UPDOWN_GBM#BNB | 78 | +0.062 | +8.53€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 71 | +0.089 | +10.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 6 | -0.075 | -2.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 342 | -0.006 | -11.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 117 | +0.055 | -4.10€ | 2 | 6 |
| ✅ UPDOWN_GBM#BTC#240min | 33 | +0.071 | +2.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 89 | -0.028 | -1.75€ | 2 | 2 |
| ✅ UPDOWN_GBM#BTC#60min | 85 | -0.063 | -9.73€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 288 | +0.003 | +3.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 53 | +0.154 | +19.98€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 235 | -0.032 | -16.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 454 | +0.050 | +41.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 201 | +0.131 | +50.80€ | 1 | 15 |
| ✅ UPDOWN_GBM#ETH#240min | 34 | +0.056 | +0.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 107 | -0.023 | -7.66€ | 3 | 1 |
| ✅ UPDOWN_GBM#ETH#60min | 97 | +0.005 | -1.72€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 339 | -0.004 | +3.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 135 | +0.018 | +1.10€ | 2 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 28 | +0.000 | -0.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 100 | +0.000 | +1.67€ | 2 | 3 |
| ✅ UPDOWN_GBM#SOL#60min | 64 | -0.015 | +0.81€ | 2 | 0 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 438 | +0.025 | +49.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 265 | +0.092 | +69.87€ | 0 | 14 |
| ✅ UPDOWN_GBM#XRP#240min | 16 | -0.089 | -2.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 157 | -0.072 | -17.66€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 105 | +0.238 | -4.25€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 105 | +0.238 | -4.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 69 | +0.204 | -10.17€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 69 | +0.204 | -10.17€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 36 | +0.289 | +5.92€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 36 | +0.289 | +5.92€ | 0 | 1 |
| ✅ UPDOWN_GBM_15M_TARDIO | 1549 | -0.043 | +177.36€ | 2 | 2 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 1549 | -0.043 | +177.36€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 99 | -0.074 | -2.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 99 | -0.074 | -2.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 309 | -0.130 | -2.22€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 309 | -0.130 | -2.22€ | 3 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 37 | -0.013 | +0.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 37 | -0.013 | +0.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 127 | -0.012 | +16.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 127 | -0.012 | +16.14€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 495 | -0.003 | +98.63€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 495 | -0.003 | +98.63€ | 1 | 1 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 482 | -0.031 | +66.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 482 | -0.031 | +66.56€ | 3 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 5 | -0.054 | -1.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 5 | -0.054 | -1.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 5 | -0.054 | -1.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 5 | -0.054 | -1.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 137 | +0.241 | +59.56€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 137 | +0.241 | +59.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 86 | +0.227 | +29.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 86 | +0.227 | +29.79€ | 0 | 14 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 51 | +0.255 | +29.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 51 | +0.255 | +29.77€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 321 | -0.067 | -27.02€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#5min | 321 | -0.067 | -27.02€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 205 | -0.012 | -11.89€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 205 | -0.012 | -11.89€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 17 | +0.067 | +3.83€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 17 | +0.067 | +3.83€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#DOGE | 19 | -0.249 | -5.61€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#DOGE#5min | 19 | -0.249 | -5.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 28 | -0.167 | -4.42€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 28 | -0.167 | -4.42€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 28 | -0.200 | -4.70€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 28 | -0.200 | -4.70€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 24 | -0.154 | -4.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 24 | -0.154 | -4.23€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 910 | +0.285 | +386.45€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 270 | +0.199 | +8.22€ | 0 | 2 |
| ✅ WEEKLY_PRICE#ETH | 289 | +0.256 | +69.14€ | 0 | 1 |
| ✅ WEEKLY_PRICE#SOL | 351 | +0.372 | +309.10€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**🟡 H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread=0.158: overbought→boost, oversold→filtro | oversold(IBS<0.3): IC=-0.036 n=660 | neutral: IC=+0.002 n=668 | overbought(IBS>0.7): IC=+0.122 n=910
  - _Datos_: n=2393 IC=+0.039 PNL=+160.52€

**🟡 H-HORA-GBM** — hora_utc causal automático en GBM (forward)
  - _Umbral_: n≥20 forward con hora_utc + alguna hora con n≥15 IC<-0.10 o >+0.10
  - _Acción_: El sistema lo aplica automáticamente vía FEATURE_RULES. Verificar en strategy_params.json.
  - _Estado_: H=14h: IC=+0.120 n=90 PNL=+25.02€ → BOOST | H=23h: IC=-0.149 n=112 PNL=-29.64€ → FILTRAR

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.018 < 0.08 — monitorear
  - _Datos_: n=135 IC=+0.018 PNL=+1.10€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=289/15 IC=+0.256 PNL=+69.14€ | BTC: n=270/15 IC=+0.199 PNL=+8.22€ | SOL: n=351/15 IC=+0.372 PNL=+309.10€

**🟡 H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.109 n=35202 | tras_1loss IC=+0.065 n=24340 | tras_2loss IC=+0.022 n=10529/40 | gap=+0.087 (umbral 0.05)

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
  - _Estado_: alineada_con_outcome_prev IC=+0.148 n=11/60 | contraria IC=-0.083 n=10 | gap=+0.231 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=12, boost estimado=+0.022. Necesita 8 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 20/50 ops con delta_ratio feature

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
  - _Estado_: alineado_BTC IC=+0.053 n=130 | contrario_BTC IC=-0.027 n=72/40 | gap=-0.080 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.150 > 0.08 con n=58 PNL=+26.22€
  - _Datos_: n=58 IC=+0.150 PNL=+26.22€

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
  - _Estado_: n=1806 IC=+0.018 PNL=+94.98€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=1806 IC=+0.018 PNL=+94.98€

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
  - _Estado_: n=412 IC=+0.097 PNL=+54.24€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=412 IC=+0.097 PNL=+54.24€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=97 IC=-0.005 PNL=-4.72€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=97 IC=-0.005 PNL=-4.72€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=117 IC=+0.055 PNL=-4.10€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=117 IC=+0.055 PNL=-4.10€

**⏳ H-CUSTOM-DRIFT15-ZONA-MUERTA** — GBM#15min drift_15min ∈ [-0.3,+0.3] — zona muerta de señal
  - _Hipótesis_: Análisis n=127 GBM#15min: cuando drift_15min está entre -0.3 y +0.3 (mercado sin dirección clara) el IC es negativo (-0.043). Cuando drift>0.3 IC=+0.100 (n=28). Cuando drift<-1 IC=+0.048 (reversión). La señal requiere mercado con dirección clara.
  - _Umbral_: 50
  - _Acción_: Filtrar señales GBM#15min cuando drift_15min ∈ [-0.3, +0.3] — validar con n≥50 antes de implementar
  - _Estado_: 0/50 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🟡 H-CUSTOM-DRIFT15-MOMENTUM** — GBM#15min drift_15min > 0.3 — zona de momentum (señal fuerte)
  - _Hipótesis_: Cuando drift_15min > 0.3%/h el GBM captura bien la dirección: IC=+0.100 n=28 en todos GBM#15min; IC=+0.152 n=13 solo BTC. El mercado tiene dirección clara y el GBM la sigue. Hipótesis: este rango es donde la señal es real.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma IC>0.10 con n≥40 → boost ×1.2 en GBM#15min cuando drift_15min>0.3
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.084 > 0.08 con n=531 PNL=+66.16€
  - _Datos_: n=531 IC=+0.084 PNL=+66.16€

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
  - _Estado_: n=29 IC=+0.145 PNL=+5.48€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=29 IC=+0.145 PNL=+5.48€

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
  - _Estado_: n=363 IC=+0.095 PNL=+90.92€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=363 IC=+0.095 PNL=+90.92€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=278 IC=+0.043 PNL=-1.71€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=278 IC=+0.043 PNL=-1.71€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.082 > 0.08 con n=77 PNL=+14.41€
  - _Datos_: n=77 IC=+0.082 PNL=+14.41€

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
  - _Estado_: n=294 IC=+0.027 PNL=+7.40€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=294 IC=+0.027 PNL=+7.40€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.157 > 0.02 con n=100 PNL=+33.80€
  - _Datos_: n=100 IC=+0.157 PNL=+33.80€

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
  - _Estado_: n=948 IC=+0.018 PNL=+18.53€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=948 IC=+0.018 PNL=+18.53€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.145 > 0.1 con n=533 PNL=+151.23€
  - _Datos_: n=533 IC=+0.145 PNL=+151.23€

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
  - _Estado_: n=138 IC=+0.100 PNL=+37.93€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=138 IC=+0.100 PNL=+37.93€

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
  - _Estado_: n=1132 IC=-0.131 PNL=+124.08€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1132 IC=-0.131 PNL=+124.08€

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
  - _Estado_: n=289 IC=+0.139 PNL=+84.76€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=289 IC=+0.139 PNL=+84.76€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.097 > 0.08 con n=412 PNL=+54.24€
  - _Datos_: n=412 IC=+0.097 PNL=+54.24€

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
  - _Estado_: 29/289 ops en el filtro definido (IC actual=-0.242 PNL=-0.28€)
  - _Datos_: n=29 IC=-0.242 PNL=-0.28€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=746 IC=+0.159 PNL=+399.22€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=746 IC=+0.159 PNL=+399.22€

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
  - _Estado_: n=322 IC=+0.000 PNL=+23.43€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=322 IC=+0.000 PNL=+23.43€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.206 > 0.08 con n=260 PNL=+143.19€
  - _Datos_: n=260 IC=+0.206 PNL=+143.19€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=538 IC=+0.041 PNL=+161.31€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=538 IC=+0.041 PNL=+161.31€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.251 > 0.08 con n=612 PNL=-63.07€
  - _Datos_: n=612 IC=+0.251 PNL=-63.07€

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
  - _Estado_: 36/40 ops en el filtro definido (IC actual=+0.368 PNL=+28.68€)
  - _Datos_: n=36 IC=+0.368 PNL=+28.68€

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
  - _Estado_: n=1010 IC=+0.102 PNL=-221.42€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=1010 IC=+0.102 PNL=-221.42€

**⏳ H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: 40
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: 15/40 ops en el filtro definido (IC actual=+0.154 PNL=+6.63€)
  - _Datos_: n=15 IC=+0.154 PNL=+6.63€
